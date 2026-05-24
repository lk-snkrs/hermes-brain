# LK SEO/CRO — Camada Claude SEO Scorecard

Data: 2026-05-18
Status: executado read-only; camada adicionada após correção de processo do Lucas.

## Correção de processo

Lucas perguntou se o fluxo estava usando a skill Claude SEO. Veredito: até o Bloco 3, a priorização comercial estava correta e os packets seguiam princípios de SEO, mas ainda faltava materializar explicitamente a camada das skills Claude SEO (`seo-page`, `seo-content`, `seo-ecommerce`) como scorecard diagnóstico.

Correção aplicada neste bloco: a fila continua começando por vendas, GA4, GSC, Shopify live e membership exato. A camada Claude SEO entra depois, como diagnóstico secundário e enriquecimento dos packets, não como ranking por HTML público.

## Artefatos

- Script: `scripts/lk_seo_cro_claude_seo_scorecard_20260518.py`
- JSON: `reports/lk-seo-cro-claude-seo-scorecard-2026-05-18.json`
- Markdown: `reports/lk-seo-cro-claude-seo-scorecard-2026-05-18.md`
- Fonte: `reports/lk-seo-cro-p1-approval-packets-2026-05-18.json`

## Skills aplicadas

- `seo-page`: title/meta/H1/canonical/OG/imagens/schema técnico.
- `seo-content`: estrutura, conteúdo público, sinais de confiança/E-E-A-T.
- `seo-ecommerce`: schema e sinais e-commerce/product/listing.

## Resultado

- URLs analisadas: 8.
- Public fetch OK: 8/8.
- Média Claude SEO: 95,2/100.
- Writes externos: 0.

## Principais achados

- A base técnica pública das top URLs está forte.
- O score médio alto confirma que a maior vantagem agora não é “corrigir HTML aleatório”, e sim aplicar refinamentos seletivos nos P1 comercialmente importantes.
- Pontos recorrentes:
  - Poucos H2s/seções estruturadas em collections.
  - Sinais de confiança/E-E-A-T pouco evidentes no trecho público estático.
  - Title longo em Lululemon e no PDP Onitsuka Kill Bill, reforçando os packets SEO title/meta.

## Scores por packet

- `lk-seo-cro-p1-2026-05-18-01` Onitsuka Tiger todos os modelos: 96/100.
- `lk-seo-cro-p1-2026-05-18-02` New Balance 204L: 96/100.
- `lk-seo-cro-p1-2026-05-18-03` Air Jordan Travis Scott: 96/100.
- `lk-seo-cro-p1-2026-05-18-04` Lululemon: 92/100.
- `lk-seo-cro-p1-2026-05-18-05` Adidas Samba Jane: 96/100.
- `lk-seo-cro-p1-2026-05-18-06` Onitsuka Kill Bill PDP: 94/100.
- `lk-seo-cro-p1-2026-05-18-07` Onitsuka Mexico 66: 96/100.
- `lk-seo-cro-p1-2026-05-18-08` Nike Mind 001: 96/100.

## Decisão operacional

O fluxo correto daqui para frente é:

1. Roteador comercial: vendas, GA4, GSC, Shopify, Tiny/GMC quando disponíveis.
2. Decision-grade refresh: Shopify live + membership exato.
3. Approval packets: payload, alvo, rollback.
4. Claude SEO scorecard: `seo-page`, `seo-content`, `seo-ecommerce` como diagnóstico secundário obrigatório.
5. Aplicação somente se Lucas aprovar explicitamente payload + alvo + rollback.

## Guardrails

Não foi executado:

- Shopify Admin write/mutation;
- alteração de tema/conteúdo;
- Tiny API/write;
- Merchant/feed write;
- GA4/GSC write;
- campanha/envio externo;
- WhatsApp/e-mail;
- preço/estoque;
- cron novo.
