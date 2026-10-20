# Matriz de Decisão de Stack — FeedbackLoop

## 1. Objetivo

Escolher a arquitetura de evolução preservando o protótipo existente e reduzindo risco operacional, de privacidade e de custo.

Os pesos foram definidos antes da comparação das alternativas.

## 2. Critérios e pesos

| Critério | Peso |
|---|---:|
| Compatibilidade com o protótipo herdado | 20% |
| Segurança, privacidade e controle de dados | 20% |
| Facilidade de deploy e operação | 15% |
| CI/CD e rollback | 15% |
| Custo e eficiência para o orçamento | 15% |
| Testabilidade e manutenção | 10% |
| Facilidade de evolução da aplicação | 5% |
| **Total** | **100%** |

Escala: 1 = fraco, 5 = excelente.

## 3. Alternativas

### A — Manter Streamlit/Python + OpenAI + persistência PostgreSQL + Render

| Critério | Peso | Nota | Pontuação |
|---|---:|---:|---:|
| Compatibilidade | 20 | 5 | 1,00 |
| Segurança/privacidade | 20 | 4 | 0,80 |
| Deploy/operação | 15 | 5 | 0,75 |
| CI/CD/rollback | 15 | 5 | 0,75 |
| Custo | 15 | 4 | 0,60 |
| Testabilidade/manutenção | 10 | 5 | 0,50 |
| Evolução | 5 | 4 | 0,20 |
| **Total** | **100** | | **4,60 / 5** |

### B — Migrar para FastAPI + frontend separado + OpenAI + PostgreSQL + Render

| Critério | Peso | Nota | Pontuação |
|---|---:|---:|---:|
| Compatibilidade | 20 | 3 | 0,60 |
| Segurança/privacidade | 20 | 4 | 0,80 |
| Deploy/operação | 15 | 3 | 0,45 |
| CI/CD/rollback | 15 | 4 | 0,60 |
| Custo | 15 | 3 | 0,45 |
| Testabilidade/manutenção | 10 | 5 | 0,50 |
| Evolução | 5 | 5 | 0,25 |
| **Total** | **100** | | **3,65 / 5** |

### C — Streamlit + LLM local + banco local

| Critério | Peso | Nota | Pontuação |
|---|---:|---:|---:|
| Compatibilidade | 20 | 4 | 0,80 |
| Segurança/privacidade | 20 | 5 | 1,00 |
| Deploy/operação | 15 | 2 | 0,30 |
| CI/CD/rollback | 15 | 2 | 0,30 |
| Custo | 15 | 3 | 0,45 |
| Testabilidade/manutenção | 10 | 3 | 0,30 |
| Evolução | 5 | 3 | 0,15 |
| **Total** | **100** | | **3,30 / 5** |

## 4. Decisão

A alternativa A será adotada como baseline de arquitetura.

A decisão privilegia evolução incremental: preserva Python, Streamlit e a interface de LLM já existentes, enquanto acrescenta as capacidades necessárias para transformar o protótipo em produto operável.

A escolha não significa que todos os componentes estão definitivamente fechados. O banco e alguns serviços auxiliares poderão ser ajustados durante a implementação caso o custo, a disponibilidade ou os requisitos de produção indiquem outra solução compatível.

## 5. Observação

As notas são uma avaliação de engenharia para este trabalho acadêmico, não uma medição universal das plataformas.
