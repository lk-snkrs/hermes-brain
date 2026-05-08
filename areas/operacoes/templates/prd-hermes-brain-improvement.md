# PRD — [nome da melhoria]

## 1. Contexto

Qual material, problema ou oportunidade originou este PRD?

- Fonte:
- Data:
- Pasta/arquivo de análise:
- Relação com Lucas/LK/Zipper/SPITI/Hermes:

## 2. Problema

Descrever o problema real. Evitar “implementar porque o material sugeriu”.

## 3. Objetivo

O que deve melhorar no Hermes Brain ou na operação?

## 4. Não objetivos

Listar explicitamente o que não será feito nesta fase, especialmente produção, deploy, envio externo, mutações de banco e merge automático.

## 5. Usuários

- Lucas:
- Hermes Geral:
- Área/agente afetado:
- Futuro mantenedor:

## 6. Decisão Hermes-native

Resumo da matriz:

- O que o material ensina:
- O que Hermes já faz diferente:
- Decisão: aplicar/adaptar/deferir/rejeitar
- Por quê:

## 7. Requisitos funcionais

- RF1:
- RF2:
- RF3:

## 8. Requisitos não funcionais

- Português por padrão.
- Sem inventar dados.
- Fato, interpretação e recomendação separados.
- Segredos via Doppler; nunca valores em docs.
- `possible_secrets 0` antes de commit/PR.
- Health check do Brain passando quando o repo for alterado.

## 9. Guardrails e aprovações

Ações permitidas nesta fase:

- documentação local;
- branch/worktree;
- PR draft;
- leitura read-only.

Ações bloqueadas sem aprovação Lucas:

- merge em `main`;
- deploy;
- VPS/Docker/Traefik/volumes/redes;
- envio WhatsApp/email/campanha/post;
- mutação de dados;
- exposição/alteração de secrets;
- contato com cliente/colecionador/parceiro.

## 10. Arquitetura / arquivos

Arquivos a criar/alterar:

- `...`

Arquivos a preservar:

- `...`

## 11. Plano de implementação

### Fase 0 — Análise

### Fase 1 — Documentação

### Fase 2 — PR/validação

### Fase 3 — Produção, se aplicável

## 12. Critérios de pronto

- [ ] Artefatos criados.
- [ ] Índices atualizados.
- [ ] `python3 scripts/brain_health_check.py` OK, se repo alterado.
- [ ] Secret scan com `possible_secrets 0`.
- [ ] Diff revisado.
- [ ] Nenhuma ação externa/produtiva não aprovada.
- [ ] PR draft aberto, se aplicável.

## 13. Riscos

- Burocratizar o Hermes copiando framework externo.
- Duplicar lógica já existente no Brain.
- Documentar segredo ou dado pessoal.
- Confundir rotina documentada com cron ativo.
- Executar ação externa antes de aprovação.

## 14. Follow-up

- Próxima fase recomendada:
- Pendências:
- Decisão necessária do Lucas:
