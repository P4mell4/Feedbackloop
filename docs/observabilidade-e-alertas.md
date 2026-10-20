# Observabilidade e alertas

> **Estado deste documento: PROPOSTA/SIMULAÇÃO.** O módulo de exemplo registra métricas
> em memória e cria eventos de alerta locais; ele não envia notificações externas nem
> constitui, sozinho, um dashboard de produção.

## Métricas

| Métrica | Fórmula / definição | Limite ilustrativo | Destino esperado |
|---|---|---|---|
| Volume de requisições | Contagem de análises recebidas no período | Acompanhar tendência; sem alerta inicial | Dashboard operacional |
| Taxa de erro | `requisições com erro / requisições totais` | > 5% em janela definida | Canal/sistema de alertas a configurar |
| Latência p50 | Percentil 50 das durações registradas | Acompanhar tendência | Dashboard operacional |
| Latência p95 | Percentil 95 das durações registradas | > 10 s em janela definida | Canal/sistema de alertas a configurar |
| Latência p99 | Percentil 99 das durações registradas | Acompanhar tendência | Dashboard operacional |
| Acertos de cache | Quantidade de leituras atendidas pelo cache | Sem limite fixo; calcular taxa de acerto | Dashboard operacional |
| Custo estimado | Tokens de entrada/saída × preço vigente do modelo | Limite mensal definido pelo responsável | Dashboard e alerta de orçamento |
| Qualidade | Acurácia por tema/sentimento em conjunto rotulado | Definir após baseline | Relatório de avaliação |

## Definições importantes

- O p95/p99 exige um conjunto de observações; não deve ser inferido a partir de uma única execução.
- O módulo de exemplo usa nearest-rank para percentis. Mantenha o mesmo método ao comparar medições.
- O custo é uma estimativa, a menos que os dados de uso e a tabela de preços sejam confirmados pelo provedor.
- Não incluir respostas, nomes, e-mails, prompts completos ou outros dados pessoais nas métricas.

## Teste local reproduzível

O teste automatizado `tests/test_observability.py` verifica:
1. Registro de duração e cálculo de percentis.
2. Contagem de erros e cálculo da taxa.
3. Geração de um evento quando um limite é ultrapassado.

Comando:

```bash
pytest -q tests/test_observability.py
```

## Evidência esperada para o backlog

- [ ] Saída do teste automatizado anexada ao registro de evidências.
- [ ] Captura do dashboard mostrando volume, erros, p50/p95/p99 e acertos de cache.
- [ ] Regra de alerta configurada com limite, janela e destino.
- [ ] Teste controlado que ultrapasse o limite e demonstre o alerta no destino configurado.
- [ ] Registro da data, ambiente, versão do código e resultado.

**Limitação atual:** `alert_destination="console/teste"` é somente um destino de demonstração. Para declarar um alerta real, integrar a aplicação ao serviço escolhido e testar a notificação de ponta a ponta.
