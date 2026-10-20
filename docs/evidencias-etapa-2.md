# Evidências da Etapa 2

> Atualizar somente após executar cada ação. As linhas com “simulado” não comprovam execução real.

| Requisito | Evidência | Estado |
|---|---|---|
| Privacidade antes do LLM | `tests/test_privacy.py` + inspeção do prompt recebido pelo cliente fake | Exemplo preparado; executar |
| Taxonomia canônica | `tests/test_taxonomy.py` | Exemplo preparado; executar |
| Cache/TTL/LRU | `tests/test_cache.py` | Exemplo preparado; executar |
| Observabilidade | `tests/test_observability.py` | Exemplo preparado; executar |
| Retenção | `tests/test_retention.py` | Teste de regra em memória; não prova exclusão real |
| Qualidade | `tests/test_quality.py` | Exemplo preparado; validar conjunto rotulado |
| Benchmark | `docs/benchmark-otimizacao.md` | Tabela ilustrativa; substituir por medições |
| Alerta | `docs/observabilidade-e-alertas.md` | Destino local simulado; integrar alerta real |
| Segurança | `docs/seguranca-e-rotacao-de-credenciais.md` | Executar varredura no repositório real |
| README | `README-secoes-propostas.md` | Modelo para integrar ao README principal |
| Vídeo de 3–5 min | Arquivo/link a preencher | Pendente |

## Roteiro sugerido para o vídeo

1. Mostrar o filtro de privacidade antes da chamada ao cliente fake.
2. Repetir a mesma resposta e demonstrar o acerto de cache.
3. Mostrar os testes de expiração e limite.
4. Mostrar métricas e o evento de alerta simulado.
5. Explicar o que ainda precisa de integração real: dashboard persistente, notificação externa, exclusão agendada e benchmark com medições.
