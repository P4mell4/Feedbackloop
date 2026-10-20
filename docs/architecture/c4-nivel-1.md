# C4 — Nível 1: Contexto do Sistema

```mermaid
C4Context
    title FeedbackLoop — Diagrama de Contexto

    Person(rh, "Analista de RH", "Envia respostas abertas e consulta os insights")
    System(feedbackloop, "FeedbackLoop Survey Insights", "Analisa respostas abertas, classifica temas e sentimentos e produz resumo executivo")
    System_Ext(llm, "Provedor de LLM", "Classificação e geração qualitativa")
    System_Ext(db, "Banco de dados", "Persistência das análises e metadados")
    System_Ext(github, "GitHub Actions", "CI/CD e automação do projeto")

    Rel(rh, feedbackloop, "Envia respostas e consulta resultados")
    Rel(feedbackloop, llm, "Envia somente texto previamente anonimizado")
    Rel(feedbackloop, db, "Persiste resultados e metadados sem necessidade de PII")
    Rel(github, feedbackloop, "Publica novas versões")
```

## Leitura

O sistema central é o FeedbackLoop. O usuário interage com a aplicação para fornecer respostas e consultar a análise.

O provedor de LLM é um sistema externo e recebe apenas conteúdo após a etapa de anonimização. A persistência fica fora da interface e o GitHub Actions participa do ciclo de entrega.
