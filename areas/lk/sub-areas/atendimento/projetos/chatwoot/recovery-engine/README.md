# Motor de Recuperação — Chatwoot fork LK (lk-chatwoot)

Status: **EM PRODUÇÃO** (imagem `lk-chatwoot:v2-recovery17`) · fluxos automáticos **DESLIGADOS por decisão do Lucas** (prontos para ligar)
Atualizado em: `2026-06-10`
Fonte: `/opt/data/lk-chatwoot-v2` (VPS Hostinger 72.60.150.124, **com git local** desde 10/jun)
Construído por: Claude (Cowork) em sessões com Lucas · Documentado no Brain para uso do Hermes Agent

## O que é

Fork self-hosted do Chatwoot v4.14.1 com um **motor próprio de recuperação de carrinho abandonado + journeys de marketing por WhatsApp**, integrado a Shopify (lk-sneakerss.myshopify.com), Klaviyo e Evolution API. Substitui o BiteSpeed (referência all-time: R$ 429.554 journey revenue · 3,08% conversão).

Painel: https://chat.lkskrs.online → `/app/accounts/1/settings/recovery` (abas Journeys / Dashboard / Audiências / Broadcast / Config) — também na sidebar principal ("Recuperação").

## Capacidades

- **Carrinho abandonado**: régua de 3 toques (delays configuráveis) que cancela na compra; dedup persistente; claim atômico anti-duplicação; checagem "já comprou" antes de cada toque.
- **Ciclo do pedido**: criado / aprovado(pago) / enviado / entregue / follow-up pós-venda, com dedup por (pedido, tipo).
- **Gatilhos por tag** do pedido Shopify (ex.: `encomenda` → template), dedup 30d.
- **Broadcast por segmento RFM** (champions/vip/loyal/repeat/one_timer/winback) com cap de 7 dias por contato, amostra e agendamento.
- **Customer 360** ao vivo da Shopify no sidebar da conversa e na página de contato (LTV, pedidos clicáveis, rastreio).
- **Captura Klaviyo** de carrinho anônimo (flows Checkout Started + Added to Cart → webhook).
- **Templates por nome** (biblioteca `nome :: texto`, multilinha) com **interpolação**: `{{nome}} {{produto}} {{valor}} {{link}} {{pedido}} {{rastreio}}`.
- **WhatsApp real via Evolution API** (instância "LK Flagship", 551123671467, bridgeada à inbox #3 Channel::Api).

## Documentos deste pacote

- `ARQUITETURA.md` — componentes, fluxos e chaves de configuração.
- `ESTADO-ATUAL.md` — estado exato em 10/jun/2026 (flags, templates, números).
- `RUNBOOK.md` — operação: build/deploy/hot-patch/rollback/migração/diagnóstico.
- `AUDIT-FIXES-2026-06-10.md` — audit de 3 frentes + todas as correções aplicadas.

## Guardrails (alinhados ao hub Atendimento)

- Fluxos automáticos só ligam com decisão explícita do Lucas (hoje: `SHOPIFY_RECOVERY_ENABLED=false`, `SHOPIFY_NOTIFY_ENABLED=false`).
- **Delays ainda em valores demo (1,2,3 min)** — trocar para `60,1440,2880` AO LIGAR; followup demo (2 min) → sugerido 4320.
- Mensagem visível a cliente exige canal pronto + template resolvível; placeholders/nomes não resolvidos NUNCA são enviados (lição do incidente "(vazio)" de 10/jun).
- Broadcast com Evolution conectado agora é REAL (status 'ready'); amostra simulada não envia nada.
