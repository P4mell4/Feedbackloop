# ADR-001 — Escolha da Stack de Evolução

- **Status:** Aceito
- **Data:** 2026-09-21
- **Decisão:** Evoluir a stack Python + Streamlit + OpenAI, adicionando persistência, anonimização, cache, observabilidade, testes e automação de deploy.

## Contexto

O protótipo já possui uma aplicação Streamlit, pipeline Python, integração com OpenAI e interface de LLM mockável. O briefing determina explicitamente que a dívida técnica deve ser refatorada, e não que o sistema seja reescrito do zero.

Além disso, o projeto precisa atender requisitos de privacidade, custo, qualidade, CI/CD, deploy e operação.

## Alternativas consideradas

### 1. Manter e evoluir a stack atual

Preserva a maior quantidade possível do investimento existente e reduz risco de reescrita.

### 2. Migrar para FastAPI com frontend separado

Fornece uma separação de API e interface mais convencional para produtos maiores, porém introduz uma mudança arquitetural relevante sem ser necessária para os objetivos desta etapa.

### 3. Substituir o provedor por modelo local

Reduz a necessidade de enviar conteúdo a um provedor externo, mas aumenta a complexidade de infraestrutura, operação e capacidade computacional, além de não ser necessária para cumprir o escopo atual.

## Decisão

Manteremos:

- Python como linguagem principal;
- Streamlit como interface;
- interface abstrata `ClienteLLM`;
- OpenAI como provedor inicial permitido pelo briefing;
- pytest para testes;
- uma camada de persistência;
- mecanismos de anonimização antes do LLM;
- cache por conteúdo/configuração;
- GitHub Actions para CI/CD.

O deploy será tratado separadamente na ADR-002.

## Consequências positivas

- Menor risco de reescrita.
- Aproveitamento dos testes e da separação UI/pipeline existentes.
- Evolução incremental.
- Menor tempo até uma versão publicável.
- Facilidade para demonstrar a relação entre protótipo e produto final.

## Consequências negativas

- Streamlit continuará acoplando parte da experiência de interface ao Python.
- Será necessário organizar melhor o código à medida que novas responsabilidades forem adicionadas.
- A persistência e a observabilidade introduzirão componentes adicionais.

## Princípio de evolução

Nenhuma mudança estrutural será feita apenas por preferência tecnológica. Cada novo componente deve resolver uma necessidade identificada na auditoria ou no briefing.
