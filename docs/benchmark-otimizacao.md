# Benchmark da otimização por cache

> **SIMULAÇÃO ILUSTRATIVA — NÃO É UMA MEDIÇÃO REAL DO PROJETO.**
> Substitua os valores deste exemplo pelos resultados obtidos ao executar o benchmark
> na mesma máquina, com a mesma amostra e as mesmas configurações.

## Objetivo

Avaliar se o cache de classificações reduz chamadas repetidas ao modelo e o tempo de
execução ao reanalisar respostas iguais, sem alterar a classificação retornada.

## Metodologia proposta

- Amostra: 20 respostas sintéticas; 10 textos únicos, cada um repetido duas vezes.
- Modelo: cliente falso determinístico durante o teste funcional.
- Versão do prompt: `classificacao-v1`.
- TTL: 86.400 segundos.
- Capacidade máxima: 500 entradas.
- Execuções: uma rodada sem cache e uma rodada com cache, reiniciando métricas entre rodadas.
- O resumo final deve ser medido separadamente, pois este exemplo cacheia apenas classificações.

## Exemplo de resultados simulados

| Métrica | Sem cache | Com cache |
|---|---:|---:|
| Respostas de entrada | 20 | 20 |
| Textos únicos após sanitização | 10 | 10 |
| Chamadas de classificação | 20 | 10 |
| Acertos de cache | 0 | 10 |
| Falhas de cache | 20 | 10 |
| Chamadas de resumo | 1 | 1 |
| Chamadas totais ao cliente | 21 | 11 |
| Redução de chamadas totais | — | 47,6% |

**Como interpretar:** os números acima são calculados para demonstrar a forma de apresentação, não foram medidos na execução real do FeedbackLoop. O tempo e o custo em reais/dólares não foram preenchidos porque dependem do provedor, do modelo, dos tokens e do ambiente de execução.

## Cálculos

- Taxa de acerto do cache = `acertos / (acertos + falhas)`.
- Redução de chamadas = `(chamadas_sem_cache - chamadas_com_cache) / chamadas_sem_cache × 100`.
- Custo estimado = `tokens_entrada × preço_entrada + tokens_saída × preço_saída`, usando a tabela de preços vigente do modelo escolhido.

## Resultado real a registrar

| Campo | Valor medido |
|---|---|
| Data e versão do código | PREENCHER |
| Amostra/arquivo usado | PREENCHER (usar dados sintéticos) |
| Chamadas sem cache | PREENCHER |
| Chamadas com cache | PREENCHER |
| Tempo sem cache (s) | PREENCHER |
| Tempo com cache (s) | PREENCHER |
| Custo estimado sem cache | PREENCHER |
| Custo estimado com cache | PREENCHER |
| Comando/teste executado | `pytest -q` e script de benchmark |
| Limitações | Cache em memória é perdido ao reiniciar e não é compartilhado entre instâncias. |
