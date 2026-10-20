# ADR-002 — Plataforma de Deploy

- **Status:** Aceito
- **Data:** 2026-09-21
- **Decisão:** Utilizar Render como plataforma de hospedagem da aplicação web.

## Contexto

O briefing permite Streamlit Cloud, Hugging Face Spaces, Render ou Vercel. O projeto precisa demonstrar URL pública, ambientes separados, CI/CD acionado por push na branch principal e rollback real.

Como o projeto é uma aplicação Python/Streamlit, a plataforma escolhida deve facilitar execução do processo Python, configuração de variáveis de ambiente e integração com GitHub.

## Alternativas consideradas

- Streamlit Cloud
- Hugging Face Spaces
- Render
- Vercel

## Decisão

Adotar Render para o ambiente de produção e manter um ambiente de desenvolvimento/staging separado.

A configuração final deverá manter secrets fora do repositório e usar variáveis específicas por ambiente.

## Motivos

1. Boa compatibilidade com aplicações Python.
2. Integração com repositório Git.
3. Configuração de variáveis de ambiente fora do código.
4. Adequação ao fluxo de deploy automático exigido pela atividade.
5. Possibilidade de demonstrar uma estratégia de rollback baseada em versões do repositório/deploy.

## Consequências

### Positivas

- Simplifica a publicação da aplicação.
- Mantém o projeto próximo da estrutura local.
- Facilita a demonstração de CI/CD.

### Negativas

- Recursos de hospedagem podem possuir limitações ou custos conforme a configuração.
- O ambiente de persistência deverá ser tratado separadamente; não devemos assumir que o filesystem local da aplicação seja armazenamento permanente.

## Validação

Antes da entrega, será obrigatório executar um deploy de staging, validar os smoke tests e executar um rollback real em ambiente controlado.
