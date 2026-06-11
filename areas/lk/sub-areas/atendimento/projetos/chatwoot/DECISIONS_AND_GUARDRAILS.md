# Decisions and Guardrails — Chatwoot / Elle / LK Atendimento

## Decisões canônicas

1. **LK Atendimento é o dono lógico** da frente Chatwoot/Elle/WhatsApp operacional.
2. **Tiny é fonte de verdade de estoque**; Chatwoot e Shopify não são ledger de estoque.
3. **Shopify é gatilho/contexto/superfície**, não fonte final para prometer disponibilidade.
4. **Chatwoot pode receber contexto interno, labels, notas privadas e tickets**, quando aprovado e verificado.
5. **Mensagem ao cliente por Chatwoot/WhatsApp/Evolution é external-write** e exige aprovação escopada, fonte viva e receipt.
6. **PÓS VENDA LK FLAGSHIP** foi criado como camada interna; guardrail documentado: sem mensagem ao cliente via Chatwoot ainda.
7. **Secrets ficam no Doppler**, nunca no Brain. O Brain pode registrar presença/status sanitizado, não valores.
8. **Receipts novos em `receipts/` devem usar `hermes_memory_os_receipt_writer.py`**.

## Permitido sem aprovação adicional

- Ler e organizar documentos locais do Brain.
- Criar índices, summaries, manifests e receipts locais sanitizados.
- Diagnósticos read-only.
- Dry-run local sem write externo.
- Rascunhos internos e approval packets.

## Bloqueado sem aprovação escopada

- Enviar mensagem externa para cliente/fornecedor/parceiro.
- Alterar Chatwoot Cloud/self-hosted, Shopify, Tiny, WhatsApp, Evolution API ou CRM.
- Criar campanha, template ativo ou automação de envio.
- Prometer preço, estoque, reserva, prazo, troca, desconto ou negociação.
- Alterar Docker/VPS/gateway/cron/runtime/provider.
- Copiar tokens, secrets, passwords, service accounts ou connection strings para Brain/Git/Telegram.

## Protocolo para qualquer próximo write externo

1. Escopo exato do sistema e ação.
2. Fonte viva consultada.
3. Snapshot antes.
4. Preview da alteração/mensagem.
5. Aprovação explícita do Lucas para aquele escopo.
6. Execução limitada ao escopo.
7. Readback/validação.
8. Receipt no Brain.
9. Rollback/critério de reversão documentado.
