# Auditoria do Protótipo — FeedbackLoop

**Etapa:** 1 — Auditoria e decisões documentadas  
**Projeto:** FeedbackLoop — Survey Insights  
**Status:** Auditoria inicial

## 1. Objetivo da auditoria

Avaliar o protótipo herdado antes de sua evolução para um serviço publicável, identificando lacunas funcionais, técnicas, operacionais, de segurança, privacidade e qualidade.

A regra adotada é evoluir e refatorar o protótipo existente, sem reescrevê-lo do zero.

## 2. Estado atual identificado

O sistema é uma aplicação Python/Streamlit para análise em lote de respostas abertas de pesquisas de clima. O fluxo atual é:

1. receber respostas por texto, CSV ou dados sintéticos;
2. enviar cada resposta ao LLM para classificação de tema e sentimento;
3. agregar os resultados;
4. solicitar ao LLM um resumo executivo;
5. apresentar o resumo e a tabela de classificações.

A lógica de negócio já está separada da interface no pacote `feedbackloop/`, e existe uma interface de LLM mockável para permitir testes offline.

## 3. Pontos positivos herdados

- Separação inicial entre UI e lógica de negócio.
- Cliente de LLM encapsulado em uma classe com método `completar()`.
- Testes offline com cliente fake.
- Funções puras de parsing, contagem e montagem de resumo.
- Dados de demonstração explicitamente sintéticos.
- `.gitignore` já contempla `.env`, ambientes virtuais e arquivos de saída.
- O resumo mantém números calculados pelo código separados do texto qualitativo gerado pelo modelo.

## 4. Lacunas e dívida técnica

### 4.1 Privacidade e LGPD — prioridade crítica

As respostas são enviadas ao provedor de IA sem anonimização prévia. O próprio protótipo informa que nomes identificáveis seguem crus para o LLM.

**Risco:** exposição desnecessária de dados pessoais e descumprimento da regra definida no briefing.

**Ação:** criar uma etapa obrigatória de anonimização antes de qualquer chamada ao LLM, com estratégia híbrida de padrões/regex + reconhecimento de entidades quando necessário. O sistema deve operar sobre o texto anonimizado.

Também será necessário documentar finalidade, base legal, retenção e limitações. O briefing determina retenção máxima de 90 dias para logs.

### 4.2 Taxonomia de temas

O modelo recebe liberdade para inventar o tema de cada resposta. Isso pode pulverizar a análise.

**Ação:** definir uma taxonomia controlada de aproximadamente 10 temas e exigir que o classificador escolha somente entre esses rótulos.

Taxonomia inicial proposta:
- Carga de trabalho
- Liderança
- Remuneração e benefícios
- Reconhecimento e carreira
- Comunicação
- Ferramentas e processos
- Cultura e ambiente
- Trabalho remoto/híbrido
- Desenvolvimento e aprendizagem
- Outros

A taxonomia deverá ser validada com o contexto de negócio antes de ser considerada definitiva.

### 4.3 Custo e ausência de cache

O pipeline realiza uma chamada por resposta e outra para o resumo. Repetir a mesma análise repete o custo.

**Ação:** gerar uma chave determinística do conjunto de entrada + versão da taxonomia/prompt/modelo e utilizar cache/persistência para reutilizar classificações e análises já processadas.

### 4.4 Persistência

O resultado desaparece ao fechar a aplicação.

**Ação:** adicionar persistência das análises e de seus metadados essenciais, permitindo histórico e comparação futura.

### 4.5 Tratamento de erros

O fluxo atual possui tratamento mínimo de erro e depende do retorno esperado do LLM.

**Ação:** adicionar tratamento explícito para indisponibilidade do provedor, respostas inválidas, timeout, entradas vazias e falhas de persistência.

### 4.6 Observabilidade

Não há métricas operacionais suficientes.

**Ação:** registrar eventos estruturados sem conteúdo pessoal, incluindo duração, quantidade de respostas, cache hit/miss, falhas e estimativa de custo. Logs devem respeitar o limite de retenção de 90 dias definido no briefing.

### 4.7 Avaliação de qualidade

Os testes atuais verificam principalmente a lógica e o fluxo com LLM mockado. Não há conjunto de validação para medir a qualidade real das classificações e do resumo.

**Ação:** criar um pequeno conjunto de avaliação anotado, uma rubrica e testes de regressão. A avaliação deve medir pelo menos:
- aderência à taxonomia;
- acerto do sentimento;
- validade estrutural da saída;
- qualidade factual do resumo em relação aos dados fornecidos;
- ausência de temas inventados fora da taxonomia.

### 4.8 Configuração

O modelo utilizado pelo cliente de LLM está hardcoded.

**Ação:** mover modelo e parâmetros relevantes para configuração por ambiente, mantendo valores seguros no código apenas quando forem defaults não sensíveis.

### 4.9 Entrada CSV

A coluna esperada está hardcoded como `resposta`.

**Ação:** manter compatibilidade com `resposta`, mas permitir configuração/seleção da coluna ou detectar candidatos conhecidos (`resposta`, `comentario`, `comentário`, `feedback`).

### 4.10 Deploy e CI/CD

O protótipo roda localmente e não possui pipeline de CI/CD.

**Ação:** configurar GitHub Actions para testes e deploy automático da branch principal, além de ambientes separados.

## 5. Riscos prioritários

| Prioridade | Risco | Tratamento |
|---|---|---|
| Crítica | PII enviada ao LLM sem anonimização | Bloquear análise se anonimização falhar |
| Alta | Tema inconsistente | Taxonomia controlada |
| Alta | Reprocessamento e custo | Cache + hash de entrada |
| Alta | Falha de deploy/execução | CI/CD + smoke tests + rollback |
| Alta | Resultado perdido | Persistência |
| Média | Falta de observabilidade | Logs e métricas sem PII |
| Média | Qualidade não medida | Dataset de validação + rubrica |
| Média | Modelo hardcoded | Configuração por ambiente |
| Média | CSV rígido | Configuração/detecção da coluna |

## 6. Critério de aceite da evolução

O sistema será considerado pronto para a primeira versão publicada quando:

- nenhum texto identificável entrar no prompt sem passar pela anonimização;
- a classificação utilizar taxonomia controlada;
- análises repetidas possam ser atendidas por cache;
- resultados sejam persistidos;
- falhas do LLM sejam tratadas;
- existam testes automatizados e smoke tests;
- exista CI/CD;
- desenvolvimento e produção estejam separados;
- secrets não estejam no código nem no histórico público;
- exista URL pública;
- rollback tenha sido executado e registrado;
- documentação e release estejam publicadas.

## 7. Observação sobre o baseline

O repositório herdado já contém testes offline, mas a execução desses testes ainda deve ser feita no ambiente local antes da primeira alteração. Este documento não considera os testes como “passando” sem essa execução.
