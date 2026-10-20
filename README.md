# FeedbackLoop

Sistema de análise de respostas abertas de pesquisas organizacionais utilizando Inteligência Artificial.

## Sobre o projeto

O FeedbackLoop é uma aplicação desenvolvida para auxiliar na análise de respostas abertas de pesquisas. O sistema recebe respostas textuais, realiza uma classificação temática e de sentimento utilizando um modelo de linguagem e apresenta os resultados de forma consolidada.

O projeto parte de um protótipo funcional e evolui sua arquitetura para atender requisitos de segurança, privacidade, controle de qualidade, persistência, observabilidade, testes automatizados e implantação contínua.

## Problema

A análise manual de grandes volumes de respostas abertas pode consumir tempo e dificultar a identificação de padrões.

O protótipo original já permitia realizar classificações utilizando um modelo de linguagem, porém apresentava limitações importantes para uma utilização mais próxima de um ambiente de produção, incluindo:

* envio de informações potencialmente pessoais ao modelo;
* ausência de uma taxonomia controlada;
* reprocessamento de respostas já analisadas;
* ausência de persistência adequada;
* tratamento limitado de erros;
* pouca observabilidade;
* ausência de pipeline de CI/CD;
* ausência de ambiente de produção publicado.

## Solução

A evolução do FeedbackLoop introduz uma arquitetura com camadas de proteção e controle antes da utilização do modelo de linguagem.

O fluxo principal passa a ser:

```text
Entrada
   ↓
Validação
   ↓
Privacy Layer
   ↓
Taxonomia controlada
   ↓
Cache
   ↓
LLM
   ↓
Validação da resposta
   ↓
Persistência
   ↓
Resultados
```

A Privacy Layer é responsável por remover ou substituir informações pessoais identificáveis antes que o conteúdo seja encaminhado ao modelo de linguagem.

A classificação temática utiliza uma taxonomia controlada, evitando que o modelo crie categorias arbitrárias.

## Arquitetura

A arquitetura foi documentada utilizando o modelo C4.

Documentação:

* [C4 — Nível 1](docs/architecture/c4-nivel-1.md)
* [C4 — Nível 2](docs/architecture/c4-nivel-2.md)

## Stack

A solução mantém a base tecnológica do protótipo e evolui sua arquitetura:

* Python
* Streamlit
* OpenAI / modelo de linguagem
* PostgreSQL
* GitHub Actions
* Render
* Pytest

A decisão da stack está documentada em:

* [Matriz de decisão](docs/matriz-decisao-stack.md)
* [ADR-001 — Escolha da Stack](docs/adr/ADR-001-escolha-da-stack.md)
* [ADR-002 — Plataforma de Deploy](docs/adr/ADR-002-plataforma-de-deploy.md)

## Privacidade

Antes do envio de uma resposta ao modelo de linguagem, o conteúdo passa por uma camada de anonimização.

São tratados padrões de informações como:

* e-mail;
* CPF;
* telefone;
* URLs;
* nomes identificados por padrões de alta confiança.

A aplicação não deve recuperar, solicitar ou inferir informações removidas pela camada de privacidade.

## Taxonomia

As respostas são classificadas utilizando uma lista controlada de temas:

1. Carga de trabalho
2. Liderança
3. Remuneração e benefícios
4. Reconhecimento e carreira
5. Comunicação
6. Ferramentas e processos
7. Cultura e ambiente
8. Trabalho remoto/híbrido
9. Desenvolvimento e aprendizagem
10. Outros

Categorias não reconhecidas são normalizadas para `Outros`.

## Como executar localmente

### 1. Clonar o repositório

```bash
git clone [URL_DO_REPOSITORIO]
cd FeedbackLoop
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Copie:

```text
.env.example
```

para:

```text
.env
```

e preencha as variáveis necessárias.

Nunca publique o arquivo `.env`.

### 5. Executar os testes

```bash
pytest -q
```

### 6. Executar a aplicação

```bash
streamlit run app.py
```

## Testes

O projeto utiliza testes automatizados para verificar componentes como:

* anonimização;
* proteção contra envio de PII;
* normalização da taxonomia;
* classificação;
* contagem;
* processamento do pipeline.

Resultado do teste inicial do protótipo:

```text
7 passed in 0.30s
```

> Esse resultado corresponde à execução do baseline antes das novas alterações.

Os resultados das versões posteriores devem ser registrados na documentação de evidências.

## CI/CD

O projeto utiliza GitHub Actions para automatizar validações e implantação.

Fluxo esperado:

```text
Push na branch main
        ↓
GitHub Actions
        ↓
Instalação das dependências
        ↓
Execução dos testes
        ↓
Deploy
```

O arquivo do workflow está localizado em:

```text
.github/workflows/deploy.yml
```

## Ambientes

O projeto utiliza ambientes separados para desenvolvimento/staging e produção.

As credenciais e configurações de cada ambiente devem ser mantidas separadamente.

## Deploy

Plataforma escolhida:

```text
Render
```

URL pública:

```text
[URL_PUBLICA_DA_APLICACAO]
```

> Substituir pelo endereço real após o deploy.

## Smoke Tests

Foram definidos três testes principais de funcionamento:

### Smoke Test 01 — Fluxo principal

Entrada válida → processamento → resultado apresentado.

### Smoke Test 02 — Privacidade

Entrada contendo informação pessoal → anonimização → conteúdo seguro enviado ao processamento.

### Smoke Test 03 — Tratamento de erro

Entrada inválida ou falha controlada → aplicação apresenta comportamento esperado sem interromper o fluxo de forma inadequada.

As evidências dos testes estão documentadas em:

```text
docs/evidencias.md
```

## Rollback

O projeto deve possuir um procedimento de rollback capaz de restaurar uma versão anterior da aplicação.

A evidência do rollback real será registrada em:

```text
docs/evidencias.md
```

## Release

A versão inicial da solução será publicada utilizando Semantic Versioning.

Exemplo:

```text
v1.0.0
```

As alterações são registradas em:

```text
CHANGELOG.md
```

## Documentação

### Auditoria

[Auditoria do protótipo](docs/auditoria-prototipo.md)

### Decisões arquiteturais

[ADR-001](docs/adr/ADR-001-escolha-da-stack.md)

[ADR-002](docs/adr/ADR-002-plataforma-de-deploy.md)

### Arquitetura

[C4 Nível 1](docs/architecture/c4-nivel-1.md)

[C4 Nível 2](docs/architecture/c4-nivel-2.md)

### Evidências

[Evidências da entrega](docs/evidencias.md)

### Post-mortem

[Post-mortem](docs/postmortem.md)

## Status do projeto

O projeto encontra-se em evolução a partir de um protótipo funcional.

As etapas de implementação e validação são registradas progressivamente para diferenciar funcionalidades desenvolvidas de funcionalidades efetivamente testadas em ambiente real.
