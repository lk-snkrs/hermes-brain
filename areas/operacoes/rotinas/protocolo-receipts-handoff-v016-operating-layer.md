# Protocolo v0.16 — Receipts e Handoff padrão entre agentes

Data: 2026-06-06T16:40:25Z
Status: operacional/documental aprovado por Lucas — não altera runtime
Escopo: Hermes Geral, Mordomo, LK Growth, LK Shopify, LK Collection Optimizer, LK Ops, LK Trends, SPITI e futuros especialistas.

## Objetivo

Padronizar o rastro operacional entre agentes para que nenhum profile vire uma ilha. Todo trabalho relevante deve fechar o ciclo:

`pedido → roteamento → execução segura → evidência → receipt/handoff → Brain → próxima decisão`

Este protocolo não reduz a autonomia do especialista. Ele apenas obriga um recibo mínimo quando houver impacto, decisão, risco, approval, output material ou aprendizado reutilizável.

## Quando é obrigatório

Registrar receipt/handoff sempre que houver pelo menos um gatilho:

- decisão de Lucas, Renan ou outro responsável humano;
- output material entregue para empresa, cliente, campanha, site, coleção, operação ou relatório;
- uso de workers/subagents temporários;
- approval packet A2/A3/A4;
- write externo, publicação, deploy, alteração em dado vivo ou rollback;
- erro, bloqueio, fonte ausente, conflito entre agentes ou risco operacional;
- mudança de autonomia, rotina, skill, modelo, cron, channel, MCP ou Dashboard;
- aprendizado que deve sobreviver ao chat.

## Níveis de registro

### R0 — Nota local curta

Para tarefas pequenas sem risco: registrar no daily/hot/área se tiver continuidade. Não precisa Telegram.

### R1 — Receipt simples

Para output material sem write externo.

Campos mínimos:

```md
# Receipt — [área/tarefa]
Data/hora:
Agente/profile:
Empresa/área:
Pedido original:
Classificação de risco: A0/A1/A2/A3/A4
O que foi feito:
Fontes/evidências:
Artefatos gerados:
O que não foi feito:
Próximo passo:
```

### R2 — Handoff especialista → Hermes Central

Obrigatório quando o trabalho nasce ou termina em profile especialista.

Campos mínimos:

```md
# Handoff especialista → Hermes Central
Data/hora:
Agente/profile origem:
Agente/profile destino, se houver:
Empresa/área:
Pedido original:
Playbook usado:
Workers/subagents usados:
Workers pulados e motivo:
Fontes consultadas:
Output/artefato:
Aprovação recebida:
Writes externos:
Riscos/bloqueios:
Onde foi documentado no Brain:
Próximo passo:
```

### R3 — Receipt com rollback

Obrigatório para qualquer ação A3/A4 aprovada.

Campos adicionais:

```md
Escopo aprovado:
Snapshot/backup:
Comando/ação executada:
Readback/verificação:
Rollback testado/disponível:
Responsável por monitorar:
Kill criteria:
```

## Contrato por agente

### Hermes Geral

- Roteia, governa, consolida e cobra receipts.
- Não executa tarefa de especialista por conveniência quando houver owner claro.
- Pode criar docs, PRDs, matrizes, receipts e approval packets locais.

### LK Growth

- Registra hipóteses, SEO/GEO/CRO/content, calendário, Growth packets e handoffs para Shopify/LKGOC.
- Deve registrar workers selecionados/pulados quando tarefa for multi-stream.

### LK Shopify

- Registra preview/diff/readback/rollback/QA para Shopify surface.
- Qualquer Shopify/theme/Tiny write precisa receipt R3.

### LK Collection Optimizer

- Registra LKGOC scorecard, coleção, Guia LK, experiência visual, QA e handoff peer para Growth/Shopify.

### Mordomo

- Registra follow-ups relevantes, exceções, bloqueios e envios externos aprovados ou auto-enviados dentro da exceção aprovada.
- Não precisa avisar Telegram em silent-OK.

### SPITI

- Registra Hub/Financial/lotes/leilão/CRM com fonte e incerteza explícitas. Silêncio é melhor que dado errado.

### Zipper

- Enquanto documental/read-only, registrar previews, fontes e bloqueios. Contato externo, preço, disponibilidade e logística sensível exigem aprovação.

## Padrão de storage

- Rotinas/protocolos: `areas/operacoes/rotinas/`
- Governance reports: `reports/governance/`
- Receipts globais: `receipts/`
- Receipts por área: `areas/<empresa>/.../receipts/`
- Handoffs operacionais: `areas/operacoes/handoffs/` ou sub-área dona.

## Regra anti-ruído Telegram

Receipt não significa Telegram. Telegram só recebe:

- decisão necessária;
- falha/exceção atual e não recuperada;
- risco novo;
- ação relevante concluída quando Lucas pediu retorno;
- relatório executivo que Lucas pediu explicitamente;
- approval packet com opções claras.

Silent-OK deve ficar local/Brain.

Referências obrigatórias:

- `reports/governance/hermes-v016-telegram-noise-receipts-audit-2026-06-06.md` — matriz canônica de Telegram noise / receipts / handoffs.
- `areas/operacoes/rotinas/template-receipt-executivo-telegram-safe-v016.md` — template único para entregar resultado executivo no Telegram e receipt completo no Brain.
- `areas/operacoes/rotinas/template-approval-packet-cron-delivery-telegram-v016.md` — template obrigatório antes de qualquer mudança nominal de cron delivery.

## Regra Kanban → Telegram

Para boards/capability pilots:

- movimentação interna de card não vai para Telegram;
- comentários técnicos de card ficam no Kanban/Brain;
- card `done` gera receipt no Brain;
- card bloqueado por decisão humana gera Telegram curto com opções claras;
- erro de execução só vai para Telegram se for atual, acionável e não recuperado;
- assignee/worker/dispatch continua exigindo approval separado quando houver risco A2/A3/A4.

## Regra para cron delivery

Nenhum cron existente deve mudar `deliver`, schedule, script, prompt, estado ou runtime só porque a matriz recomenda menos ruído. Mudança real exige approval packet separado com lista nominal de jobs, campo atual/proposto, rollback e verificação.

## Checklist de conformidade

Antes de chamar uma frente de “operante”, verificar:

- [ ] existe owner/profile claro;
- [ ] existe playbook/rotina aplicável;
- [ ] existe local de receipt;
- [ ] workers temporários, se usados, foram listados;
- [ ] writes externos têm approval + rollback + readback;
- [ ] secrets não aparecem;
- [ ] próximo passo humano ou automático está claro;
- [ ] aprendizado recorrente virou rotina/skill quando aplicável.
