# LK — Approval packet: recuperação full-funnel por WhatsApp

Data UTC: 2026-05-20
Agente: Hermes LK Growth

## Contexto

Lucas sinalizou que a LK deve recuperar não só checkout abandonado, mas também carrinho/intenção ampla, com maior volume de mensagens. O fluxo ativo atual cobre apenas Shopify `abandonedCheckouts` com telefone válido e não captura todo add-to-cart/intenção.

## Decisão proposta

Construir uma arquitetura full-funnel em camadas:

1. Checkout abandonado com telefone — manter e endurecer o fluxo atual.
2. Carrinho/intenção ampla — capturar eventos de produto/carrinho/begin checkout em Supabase, inicialmente log-only.
3. Identity resolution — mapear sessão/email/customer/Crisp para telefone confiável.
4. Régua WhatsApp — disparar apenas quando houver telefone confiável, abandono validado, dedup e cap.

## Guardrail comercial

Apesar da necessidade de volume, não fazer blast indiscriminado. WhatsApp é customer-facing e tem risco de bloqueio, reclamação, queda de qualidade do número e perda de entregabilidade. A régua deve ser agressiva em cobertura, mas controlada em elegibilidade.

## Fase 0 — Imediata / sem envio

- Inventariar fontes disponíveis: Shopify Customer Events, tema Shopify, Crisp session data, Klaviyo/Shopify customer data, n8n workflows antigos.
- Criar tabelas Supabase para eventos e identidade.
- Capturar eventos `product_view`, `add_to_cart`, `cart_update`, `begin_checkout`, `checkout_created`.
- Não enviar mensagem ainda.
- Medir por 24h: volume total, identificados por email, identificados por telefone, recuperáveis por WhatsApp, compradores antes do envio.

Risco: baixo.
Aprovação necessária: nenhuma para auditoria/read-only; sim para inserir script/eventos no tema production.

## Fase 1 — WhatsApp controlado

- Enviar T1 apenas para eventos com telefone confiável.
- Rechecar compra antes do envio.
- Cap inicial: 1 sequência ativa por telefone por 96h.
- Registrar Crisp `request_id`, callback, status, opt-out e falhas.
- Kill switch n8n + Supabase flag.

Aprovação necessária: explícita de Lucas antes de qualquer envio real.

## Fase 2 — Escala

- Relaxar critérios com base em dados reais: valor mínimo, categorias, sessões repetidas, produto premium, recorrência de interesse.
- Criar filas por prioridade.
- Medir receita recuperada, reclamação, bloqueios, opt-outs e conversão.

## Riscos

- Envio excessivo pode afetar qualidade WhatsApp/Meta.
- Captura de intenção sem telefone não permite WhatsApp direto.
- Mensagens de recuperação são Marketing, não Utility.
- Ativar workflows antigos inativos é arriscado: placeholders, Meta direto, sem Supabase/callback.

## Recomendação

Não ativar workflows antigos. Criar fluxo novo com observabilidade primeiro e disparo controlado depois.

## Aprovação necessária para writes/customer-facing

- Inserir script/evento no tema production.
- Criar/alterar workflow n8n ativo.
- Enviar mensagens reais.
- Criar cupons/descontos.
- Alterar templates Meta/Crisp.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `LK — Approval packet: recuperação full-funnel por WhatsApp` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `LK — Approval packet: recuperação full-funnel por WhatsApp` no caminho `areas/lk/sub-areas/crm/decisions/2026-05-20-full-funnel-whatsapp-recovery-approval-packet.md`.
- Owner operacional: LK Atendimento / CRM / Operações, com governança Hermes Geral e aprovação final Lucas.

### Escopo permitido
- Escopo permitido somente após aprovação explícita: executar apenas os itens, IDs, fluxos, mensagens, campos, coleções, arquivos ou rotinas descritos neste packet, sem ampliar alvo por inferência.
- Pode fazer localmente sem nova aprovação: validação documental, preview, auditoria read-only, receipt e classificação de blockers.

### O que continua bloqueado
- Não pode fazer mensagem a cliente, WhatsApp/e-mail, campanha, Chatwoot/webhook/runtime, contato externo, preço, disponibilidade, reserva, negociação, reembolso ou logística sem aprovação específica.
- Aprovação genérica como `seguir`, `fazer tudo` ou contexto antigo não amplia escopo; novo alvo exige novo approval packet.

### Risco
- Risco principal: transformar preview/packet em autorização ampla e executar ação sensível fora do escopo exato.
- Mitigação: fail-closed, approval textual específica, backup/snapshot quando aplicável, readback e receipt com contagens.

### Rollback
- Rollback obrigatório: reverter somente a alteração aprovada usando backup/snapshot/artefato anterior quando aplicável; se a ação foi apenas preview/read-only, rollback é manter sem execução e registrar o bloqueio.
- Qualquer rollback que toque sistema externo exige o mesmo escopo aprovado, readback e receipt.

### Verificação / readback
- Verificação obrigatória: readback do artefato/preview, ledger/receipt local, amostragem de contatos/conversas quando aplicável e confirmação de zero envio externo não aprovado.
- Se houver divergência de identidade, fonte, escopo ou aprovação, bloquear execução e registrar causa sanitizada.

### Opções de aprovação
- Aprovar exatamente o escopo descrito neste packet.
- Aprovar apenas preview/dry-run/read-only.
- Ajustar alvo/limite antes de executar.
- Bloquear execução e manter como histórico/rascunho.

### Secret hygiene
- Usar credenciais somente via Doppler/wrapper seguro quando houver integração; não imprimir tokens, refresh tokens, passwords, service-account JSON, API keys ou connection strings.
- Relatórios e receipts devem manter `values_printed=false` e redigir qualquer valor sensível como `[REDACTED]`.
