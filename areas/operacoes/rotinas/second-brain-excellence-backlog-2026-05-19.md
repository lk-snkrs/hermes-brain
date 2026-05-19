# Second Brain excellence backlog — runtime, skills, Mordomo e Mission

Data: 2026-05-19
Owner: Hermes Geral
Status: implementação documental P0; runtime/live reconciliation em andamento

## Diagnóstico honesto

A arquitetura está no caminho certo: Brain como source of truth, separação LK/Zipper/SPITI, guardrails, docs, health check e skills. O ponto fraco restante não é conceito; é reconciliação operacional viva.

## P0 — Runtime/crons/canais reconciliados com fonte viva

Fonte viva verificada em 2026-05-19 via `cronjob list`:

- `749ee30b51eb` — Mesa COO diária Telegram — ativo — diário 08h30 BRT — entrega origin.
- `f5a23dd6a1bd` — Lucas Brain daily intelligence loop — ativo.
- `edd06fe19397` — Hermes runtime + cron watchdog — ativo.
- `7c688553e293` — LK Daily Sales Brief — ativo.
- `953b9055458e` — LK Weekly CEO Review — ativo.
- `4ced266825f0` / `051f05ce17c1` — Mordomo WhatsApp pessoal resumo/scan — ativos.
- `ac0b440e2643` — Mordomo Telegram gateway watchdog — ativo.
- `71b2636add5d` — LK WhatsApp Hermes responder watchdog — ativo.
- `876d54c62ccd` — LK Growth Telegram gateway watchdog — ativo.
- Vários jobs LK/GMC/SEO estão pausados; a Mesa deve tratar isso como fato vivo, não como erro automático.

Próximo passo técnico: gerar inventário versionado automaticamente a partir de `cronjob list`, com campos `job_id`, nome, schedule, destino, estado, last_status, risco e owner.

## P0 — Herança OpenClaw / cerebro-cimino

Regra nova:

- Referências históricas a OpenClaw/Amora/Bruno podem permanecer como fonte metodológica.
- Caminhos operacionais como `/root/cerebro-cimino`, comandos antigos de commit/push e instruções de agentes legados não podem ser runtime truth.
- Todo arquivo legado deve ter aviso de manutenção ou ser migrado para caminhos Hermes-native.

Pendência viva detectada: agentes LK/Zipper ainda têm blocos com `cerebro-cimino/...`; precisam de patch em lote cuidadoso para caminhos Brain atuais e bloqueios Hermes-native.

## P0 — Skills com auditoria viva

Registro mínimo por skill crítica:

- Nome da skill.
- Dono: Hermes Geral, LK, Zipper, SPITI, Mordomo, infra.
- Última execução observada.
- Última alteração.
- Risco: read-only, preview, external-send, infra, credential-sensitive.
- Teste/validação esperada.
- Próxima revisão.

A auditoria não deve ser manual eterna. O caminho certo é combinar:

1. metadados do Curator/skill usage quando disponíveis;
2. `cronjob list` para skills em rotinas;
3. busca em reports recentes;
4. owner/risk versionados no Brain.

## P0 — Mordomo operacionalizado

Estado: já existem rotinas vivas para scan/resumo/watchdog, mas Mission/Brain ainda precisam separar claramente:

- Mordomo pessoal do Lucas;
- LK/Zipper/SPITI operacionais;
- drafts internos vs external sends;
- what gets surfaced na Mesa COO.

Guardrail permanente: Mordomo nunca envia e-mail/WhatsApp/cliente/fornecedor sozinho; prepara rascunho/preview e pede aprovação explícita no turno atual.

## P0 — Mission Control alinhado ao Brain

Mission Control deve parar de expor módulos e passar a representar a Mesa COO:

1. Decisão agora.
2. Bloqueado por Lucas.
3. Hermes pode fazer sozinho.
4. Riscos.
5. Fontes/evidência/receipts.

O PRD canônico de rebuild está em `mission-control-cimino/docs/rebuild/mission-control-zero-based-rebuild-prd-2026-05-19.md`.

## Definição de excelente

O sistema chega a excelente quando:

- `/mesa` e cron diário entregam uma COO surface útil em Telegram;
- Brain contém runtime/canais/crons reconciliados com fonte viva;
- herança OpenClaw/cerebro não comanda nenhuma operação;
- skills críticas têm owner, risco e última execução;
- Mordomo aparece como operador seguro de inbox/follow-up, não como bot solto;
- Mission Control mostra a mesma realidade da Mesa, com menos card/marker creep.
