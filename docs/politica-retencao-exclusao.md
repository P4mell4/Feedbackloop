# Política de retenção e exclusão — proposta

> A política abaixo é uma proposta técnica para revisão. Prazo, finalidade e base legal
> precisam ser aprovados pelo responsável pelo tratamento de dados antes de uso real.

- Respostas originais: não persistir por padrão.
- Prompts e respostas completos do modelo: não registrar em logs.
- Logs técnicos: remover ou anonimizar dados pessoais; retenção máxima proposta de 90 dias.
- Métricas agregadas: manter apenas o necessário para operação e avaliação, com prazo definido.
- Resultados persistidos futuramente: documentar finalidade, permissões, prazo e exclusão por registro.

## Mecanismo de referência

`feedbackloop/retention.py` contém uma função de exemplo que filtra registros vencidos em memória. Isso não é uma tarefa agendada nem exclui registros de uma base real.

Para produção, integrar a rotina à persistência escolhida (por exemplo, SQL `DELETE` por timestamp), executar por agendador e registrar apenas contagem, duração e status da exclusão. O teste `tests/test_retention.py` cobre a regra de corte, não uma exclusão em produção.
