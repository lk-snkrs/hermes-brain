# LK Sales Reports WhatsApp Send — 2026-05-16

## Contexto

Lucas aprovou no turno atual: gerar os relatórios de vendas LK e mandar no grupo WhatsApp “LK Vendas” usando wacli.

## Ação executada

- Gerador criado/rodado: `scripts/lk_os_sales_reports_whatsapp_email_designmd_20260516.py`.
- Artefatos gerados:
  - JSON: `reports/lk-sales-reports/lk-sales-reports-20260516T180219-0300.json`
  - WhatsApp: `reports/lk-sales-reports/lk-sales-reports-whatsapp-20260516T180219-0300.txt`
  - HTML e-mail DesignMD: `reports/lk-sales-reports/lk-sales-reports-email-designmd-20260516T180219-0300.html`
- Grupo localizado via wacli:
  - Conta: `pessoal`
  - Nome no wacli: `[LK] Vendas/Trocas/Envios`
  - JID: `120363314625506305@g.us`
- Envio WhatsApp executado com aprovação explícita de Lucas no turno atual.
- Resultado wacli: `success=true`, `sent=true`.
- Message ID: `3EB02C94485F061140AF88`.
- Verificação: `messages show --chat 120363314625506305@g.us --id 3EB02C94485F061140AF88 --json` retornou a mensagem enviada no grupo.

## Conteúdo enviado

Resumo WhatsApp com:

- vendas de ontem, 15/05;
- pulso comercial de 16/05 até 18:02 BRT;
- loja física parcial de 16/05 até 18:02 BRT, marcado como parcial antes de 19h30;
- fonte Shopify read-only;
- separação online vs loja/POS;
- sem dados de cliente;
- sem alteração em Shopify/Tiny/campanhas.

## Números principais enviados

- Vendas de ontem: R$ 44.564,85 em 14 vendas.
- Online ontem: R$ 22.334,94 em 5 vendas.
- Loja ontem: R$ 22.229,91 em 9 vendas.
- Pulso 16/05 até 18:02: R$ 33.698,98 em 14 vendas.
- Online hoje até 18:02: R$ 16.329,06 em 6 vendas.
- Loja hoje até 18:02: R$ 17.369,92 em 8 vendas.

## Seller/POS guardrail

O Shopify POS retornou ID interno de usuário/staff, mas o gerador não expôs ID bruto como vendedor no grupo. A mensagem marcou:

`needs_mapping: Shopify POS retornou ID interno, ainda sem nome do vendedor`

Próximo passo para o report 19h30: mapear com segurança o ID POS para nome de vendedor ou encontrar fonte POS/Tiny mais confiável.

## Segurança

- Secret scan do texto WhatsApp: 0 achados.
- Nenhum token/secret impresso.
- Nenhum dado de cliente incluído.
- Nenhum write Shopify/Tiny/Meta/Google/Klaviyo executado.
- Ação externa executada: somente o envio WhatsApp aprovado por Lucas para o grupo LK Vendas.
