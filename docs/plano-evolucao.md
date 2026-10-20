# Plano de Evolução — FeedbackLoop

## Fase 1 — Auditoria e baseline

- [x] Ler README e BRIEFING
- [x] Mapear arquitetura atual
- [x] Identificar dívida técnica
- [x] Definir critérios de decisão
- [x] Criar matriz de decisão
- [x] Criar ADR-001
- [x] Criar ADR-002
- [x] Criar C4 níveis 1 e 2
- [ ] Executar testes baseline localmente
- [ ] Verificar secrets no histórico com gitleaks

## Fase 2 — Hardening e LGPD

- [ ] Implementar anonimização de PII
- [ ] Tornar anonimização bloqueante
- [ ] Fixar taxonomia de temas
- [ ] Melhorar tratamento de respostas inválidas do LLM
- [ ] Mover modelo/parâmetros para configuração
- [ ] Adicionar logging sem PII
- [ ] Adicionar cache
- [ ] Criar dataset de validação
- [ ] Criar rubrica de qualidade

## Fase 3 — Persistência e operação

- [ ] Adicionar banco de dados
- [ ] Persistir análises
- [ ] Criar histórico
- [ ] Medir custo/latência
- [ ] Documentar retenção máxima de logs de 90 dias

## Fase 4 — CI/CD e deploy

- [ ] Criar workflow GitHub Actions
- [ ] Separar staging e produção
- [ ] Configurar secrets por ambiente
- [ ] Publicar URL
- [ ] Executar três smoke tests
- [ ] Criar release SemVer
- [ ] Atualizar CHANGELOG
- [ ] Executar rollback real
- [ ] Registrar evidência

## Fase 5 — Entrega

- [ ] README v1 completo
- [ ] Post-mortem
- [ ] Vídeo de 3–5 minutos
