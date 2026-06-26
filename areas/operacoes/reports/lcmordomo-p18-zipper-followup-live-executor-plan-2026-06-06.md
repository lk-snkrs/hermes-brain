# LC Mordomo OS — P1.8 Zipper follow-up live/idempotent executor plan

**Data:** 2026-06-06T12:54:32.511063+00:00
**Escopo:** plano local para o executor live/idempotente de follow-ups Zipper.
**Modo:** dry-run/fixture; nenhum envio real, Telegram, e-mail, cron, Supabase, produção ou infra alterado.

## Resultado executivo

- Itens avaliados: 5
- Envios reais agora: não
- Contrato: follow-up só seria liberado depois de histórico bruto do mesmo canal, bloqueio material e dedupe live.

Buckets:
- `blocked_sensitive_material`: 2
- `needs_lucas_context`: 3

## Itens

### 1. Rafaela Rocha — Rodrigo Braga

- Bucket: `needs_lucas_context`
- Intent: `post_pdf_followup`
- Ação planejada: `keep_local_or_escalate_context`
- Envio liberado por este passo: não
- Histórico anexado: 0 mensagem(ns)
- Bloqueios: classificação local não libera executor: needs_lucas_context

### 2. Camila Paschoalin

- Bucket: `blocked_sensitive_material`
- Intent: `post_unavailable_work_alternatives_followup`
- Ação planejada: `keep_local_or_escalate_context`
- Envio liberado por este passo: não
- Histórico anexado: 0 mensagem(ns)
- Bloqueios: classificação local não libera executor: blocked_sensitive_material

### 3. Clau Xavier — Adriana Duque

- Bucket: `needs_lucas_context`
- Intent: `post_pdf_followup`
- Ação planejada: `keep_local_or_escalate_context`
- Envio liberado por este passo: não
- Histórico anexado: 0 mensagem(ns)
- Bloqueios: classificação local não libera executor: needs_lucas_context

### 4. Brenda

- Bucket: `blocked_sensitive_material`
- Intent: `followup_or_interest`
- Ação planejada: `keep_local_or_escalate_context`
- Envio liberado por este passo: não
- Histórico anexado: 0 mensagem(ns)
- Bloqueios: classificação local não libera executor: blocked_sensitive_material

### 5. Marcus Bitencourt

- Bucket: `needs_lucas_context`
- Intent: `post_pdf_followup`
- Ação planejada: `keep_local_or_escalate_context`
- Envio liberado por este passo: não
- Histórico anexado: 0 mensagem(ns)
- Bloqueios: classificação local não libera executor: needs_lucas_context

## Próximo passo

Conectar este planner a um leitor live/read-only do mesmo canal (`wacli messages list`/Gmail conforme o caso), ainda em dry-run. Só depois criar sender/cron com kill-switch e aprovação de ativação se a classe continuar A1/A2.
