# Post-mortem

## 1. Resumo

um incidente durante a evolução do FeedbackLoop para validar o procedimento de recuperação da aplicação.

O objetivo do exercício foi verificar se uma versão anterior poderia ser restaurada de forma controlada.

## 2. Impacto

Durante o cenário, a versão mais recente da aplicação foi considerada inadequada para produção.

Não houve impacto em usuários reais, pois o cenário foi realizado como exercício controlado.

## 3. Detecção

O problema foi identificado durante a validação da versão antes da manutenção da versão em produção.

## 4. Resposta

Foi realizada a recuperação de uma versão anterior conhecida como estável.

O procedimento utilizado foi:

```text
Identificar versão estável
        ↓
Selecionar versão anterior
        ↓
Executar rollback
        ↓
Verificar aplicação
        ↓
Executar smoke tests
```

## 5. Resultado

Após o rollback, a aplicação foi novamente verificada por meio dos testes definidos para o projeto.


## 6. Causa

O cenário foi provocado intencionalmente para validar o procedimento de recuperação.

## 7. Ações preventivas

* manter versões identificáveis;
* utilizar Semantic Versioning;
* registrar alterações no CHANGELOG;
* executar testes antes do deploy;
* manter processo de rollback documentado;
* executar smoke tests após publicação.

## 8. Aprendizados

O exercício demonstrou a importância de não considerar o deploy como etapa final isolada.

Uma aplicação publicada precisa também possuir mecanismos documentados para verificar a versão publicada e retornar a uma versão conhecida quando necessário.