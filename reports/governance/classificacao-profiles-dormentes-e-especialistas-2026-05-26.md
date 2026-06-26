# Classificação — profiles dormentes e especialistas

Data: 2026-05-26  
Escopo: documentação local/read-only. Sem iniciar, pausar, remover ou reiniciar gateways.

## Profiles ativos observados

- `/opt/data` — Hermes Geral / Main: ativo.
- `/opt/data/profiles/lk-growth` — LK Growth: ativo.
- `/opt/data/profiles/mordomo` — Mordomo: ativo.
- `/opt/data/profiles/spiti` — SPITI: ativo.

## Profiles preparados/dormentes ou auxiliares

### `/opt/data/profiles/lk-ops`
- Classificação: especialista preparado, não confirmado como gateway ativo nesta leitura.
- Dono lógico: LK Ops/Atendimento.
- Status recomendado: manter preparado; não ativar/migrar crons sem pacote runtime.
- Risco se ativado errado: promessa comercial, estoque/preço/disponibilidade sem fonte Tiny.

### `/opt/data/profiles/lk-shopify`
- Classificação: especialista preparado.
- Dono lógico: LK Shopify.
- Status recomendado: manter como preview/read-only até token/gateway/approval packet.
- Risco se ativado errado: write em Shopify/Tiny sem snapshot/readback.

### `/opt/data/profiles/lk-trends`
- Classificação: especialista preparado/radar.
- Dono lógico: LK Trends/Sourcing intelligence.
- Status recomendado: manter read-only; sem compra/negociação/reserva sem aprovação.
- Risco se ativado errado: confundir oportunidade com autorização de compra.

### `/opt/data/profiles/brain-process`
- Classificação: auxiliar de governança/documentação.
- Dono lógico: Brain Process / Hermes Geral.
- Status recomendado: marcar como auxiliar; não expor como bot público.
- Risco se ativado errado: duplicar governança ou gerar ruído.

### `/opt/data/profiles/hermes-ops-readonly`
- Classificação: auxiliar read-only.
- Dono lógico: Operações Hermes.
- Status recomendado: manter dormente/readonly até caso de uso claro.
- Risco se ativado errado: sobrepor Hermes Geral.

### `/opt/data/profiles/lk-analyst-readonly`
- Classificação: analista read-only LK.
- Dono lógico: LK análise/BI.
- Status recomendado: manter dormente/readonly; não virar executor de Ops/Growth por conveniência.
- Risco se ativado errado: métricas sem fonte viva ou output duplicado.

### `/opt/data/profiles/lk-content-reviewer`
- Classificação: revisor read-only LK.
- Dono lógico: LK Growth/conteúdo, mas como auxiliar.
- Status recomendado: manter como auxiliar; não criar canal/runtime público sem demanda.
- Risco se ativado errado: ruído editorial e conflito com LK Growth.

## Decisão recomendada

Não apagar, pausar ou ativar nada automaticamente. Ação segura agora é só documentação e critérios:

1. marcar dono lógico;
2. marcar status atual;
3. definir gatilho de ativação;
4. preparar approval packet se houver runtime/cron/gateway.
