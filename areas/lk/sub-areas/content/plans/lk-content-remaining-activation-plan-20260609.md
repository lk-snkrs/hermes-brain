# LK Content — Plano de ativação restante

Data: 2026-06-09
Status: plano operacional v0 após releitura do PRD

## Decisões de Lucas

1. Renan round-trip será amanhã.
2. Dashboard executivo: seguir com PRD em Next.js, depois GitHub privado e Vercel preview, mantendo MVP read-only.
3. Calendar mirror: fazer.
4. Segment/Flow safe smoke: fazer.
5. Advanced KDP / webhook nativo Klaviyo: fazer.

## Trilha 2 — Dashboard Next.js

### Caminho recomendado

1. PRD local aprovado.
2. Criar app Next.js read-only.
3. Usar adapters server-side para ler artefatos sanitizados:
   - campaign registry;
   - calendário local;
   - receipts;
   - brand-guide;
   - métricas.
4. Rodar build local.
5. Secret scan.
6. Criar repo GitHub privado.
7. Subir Vercel preview.

### Guardrails

- Nenhum secret no repo.
- Nenhum write externo pelo dashboard.
- Nenhuma chamada client-side para Klaviyo/Doppler/Shopify/Tiny/Google.
- Dashboard é leitura/decisão, não painel de envio.

## Trilha 3 — Calendar mirror

### MVP

Criar rotina segura que transforma planejamento editorial em eventos do calendário LK Content:

- briefing;
- pesquisa;
- preview;
- draft;
- revisão;
- aprovação;
- envio planejado;
- pós-mortem.

### Guardrails

- Somente calendário `lk@lksneakers.com.br`.
- Criar/atualizar apenas eventos com marcador LK Content.
- Não deletar eventos.
- Não mexer em calendário pessoal/geral.
- Receipt sanitizado após smoke.

## Trilha 4 — Segment/Flow safe smoke

### MVP

1. Auditar flows existentes read-only.
2. Escolher um flow de baixo risco para análise, sem ativar nem editar.
3. Criar proposta de melhoria documental.
4. Criar segmento teste seguro somente se escopo e naming forem confirmados.
5. Validar que flow activation continua bloqueada por dupla confirmação.

### Guardrails

- Sem ativar flow.
- Sem enviar mensagem.
- Sem deletar segmento/lista/flow.
- Segmento teste deve ser claramente marcado como teste e reversível.

## Trilha 5 — Advanced KDP / Klaviyo native webhook

### Situação atual

- Hermes/Vercel/worker: OK.
- Endpoint assinado: OK.
- Doppler secrets: OK.
- Klaviyo Webhooks API: bloqueada por Advanced KDP.

### Ação

Preparar mensagem para suporte/Klaviyo solicitando habilitação de Advanced KDP ou acesso a System Webhooks API.

### Enquanto isso

Fallback oficial permanece:

- watchdog read-only 2h;
- Reporting API;
- campaign registry;
- checks 2h/24h/72h.

## Ordem de execução recomendada

1. Criar dashboard Next.js local read-only.
2. Ativar Calendar mirror smoke.
3. Rodar Flow audit read-only.
4. Só depois criar segmento teste seguro.
5. Enviar/abrir solicitação Advanced KDP no Klaviyo/support.
6. Após Advanced KDP habilitado, criar subscription webhook nativa e testar evento real.
