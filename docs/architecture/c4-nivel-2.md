# C4 — Nível 2: Containers/Componentes Principais

```mermaid
C4Container
    title FeedbackLoop — Diagrama de Containers

    Person(user, "Analista de RH", "Usuário do produto")

    System_Boundary(app, "FeedbackLoop") {
        Container(ui, "Streamlit UI", "Python / Streamlit", "Entrada de CSV/texto e apresentação dos resultados")
        Container(orchestrator, "Pipeline de análise", "Python", "Orquestra anonimização, cache, classificação, agregação e resumo")
        Container(privacy, "Privacy Layer", "Python", "Detecta e substitui PII antes de qualquer chamada ao LLM")
        Container(cache, "Cache", "Python + persistência", "Evita reprocessamento de entradas/configurações já analisadas")
        Container(storage, "Persistência", "PostgreSQL", "Armazena análises, metadados e resultados necessários ao produto")
        Container(llmclient, "Cliente LLM", "Python", "Abstração do provedor de IA")
        Container(obs, "Observabilidade", "Python logging/metrics", "Registra eventos operacionais sem conteúdo pessoal")
    }

    System_Ext(llm, "OpenAI", "Provedor de LLM")
    System_Ext(ci, "GitHub Actions", "CI/CD")

    Rel(user, ui, "Envia respostas / consulta resultados")
    Rel(ui, orchestrator, "Solicita análise")
    Rel(orchestrator, privacy, "Anonimiza entradas")
    Rel(orchestrator, cache, "Consulta e grava cache")
    Rel(orchestrator, llmclient, "Solicita classificação/resumo")
    Rel(llmclient, llm, "API com texto anonimizado")
    Rel(orchestrator, storage, "Persiste resultados")
    Rel(orchestrator, obs, "Emite eventos e métricas")
    Rel(ci, app, "Executa testes e publica versão")
```

## Regra arquitetural crítica

O caminho entre `Pipeline de análise` e `OpenAI` deve passar obrigatoriamente pela `Privacy Layer`. Nenhuma chamada ao LLM deve ser feita com o texto original quando houver possibilidade de identificação pessoal.
