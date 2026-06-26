# LK OS — Contrato wacli/OpenClaw WhatsApp

Status: `contract_ready_for_review_no_external_action`
Data: 2026-05-13
Escopo: LK Sneakers / LK OS / WhatsApp multi-conta

## Veredito

O `wacli` entra no LK OS como **camada de observabilidade, intake e preview**, não como canal de envio automático.

A primeira conta operacional é `lk-compras`. O WhatsApp da loja física (`lk-loja`) fica planejado para etapa futura. A conta pessoal do Lucas (`pessoal`) fica como validação técnica e não deve virar fonte operacional da LK sem escopo separado.

## Estado técnico atual

- `pessoal`: conectado, WhatsApp pessoal Lucas, uso técnico/validação.
- `lk-compras`: conectado, WhatsApp Business Compras LK, sync inicial em andamento.
- `lk-loja`: futuro, ainda não conectado.

Snapshot sanitizado do store `lk-compras` no momento da integração:

- Chats totais no store local: 50.
- Grupos no store local: 34.
- Mensagens sincronizadas no store local: 2.216 no primeiro snapshot; processo de sync continuava avançando depois disso.

Não registrar nomes de contatos, telefones, JIDs, textos de mensagens ou anexos em relatórios públicos/Telegram sem autorização específica.

## Classificação de risco

### A0/A1 — permitido sem nova aprovação quando no escopo

- Verificar status de autenticação.
- Listar contas configuradas sem expor telefones em relatório público.
- Ver estatísticas agregadas do store (`store stats`).
- Desenhar schemas, rotinas, contratos e previews sem dados sensíveis.
- Criar documentos Brain/skills/guardrails.

### A2 — preparar com preview; aplicar só se escopo estiver claro

- Leitura pontual de mensagens/chats para classificar sinais, desde que:
  - janela limitada;
  - saída sanitizada;
  - sem PII em Telegram;
  - sem envio/resposta.
- Geração de fila interna de oportunidades, exemplos:
  - possível ruptura;
  - pedido especial;
  - solicitação de compra;
  - follow-up de fornecedor;
  - link/screenshot de produto.

### A3/A4 — exige aprovação explícita atual de Lucas

- Enviar qualquer WhatsApp.
- Responder cliente, fornecedor ou grupo.
- Criar task Notion/n8n/Notion produtiva a partir de conversa.
- Acionar fornecedor, grupo de compras ou Júlio.
- Exportar conversa com PII.
- Criar cron/sync recorrente de leitura de mensagens.
- Usar mensagem de cliente/fornecedor em relatório externo.
- Comprar, reservar, repor estoque, escolher importador/logística ou combinar pagamento.

## Comandos wacli aprováveis por classe

### Read-only técnico seguro

```bash
/opt/data/bin/wacli accounts list --json
/opt/data/bin/wacli --account lk-compras auth status --json
/opt/data/bin/wacli --account lk-compras --read-only store stats --json
```

### Read-only sensível — usar só com janela/objetivo e sanitização

```bash
/opt/data/bin/wacli --account lk-compras --read-only chats list --json --limit N
/opt/data/bin/wacli --account lk-compras --read-only messages list --json --chat CHAT_JID --limit N
/opt/data/bin/wacli --account lk-compras --read-only messages list --json --after YYYY-MM-DD --limit N
```

Saída desses comandos deve ser tratada como sensível. Para Telegram/Brain público, converter para:

- contagem;
- categoria;
- data/hora aproximada;
- origem genérica (`grupo`, `fornecedor`, `cliente`, `interno`);
- hash interno se precisar deduplicar;
- resumo sem nome/telefone/texto literal, salvo autorização.

### Bloqueado sem aprovação explícita

```bash
/opt/data/bin/wacli --account lk-compras send text ...
/opt/data/bin/wacli --account lk-compras send file ...
/opt/data/bin/wacli --account lk-compras send voice ...
/opt/data/bin/wacli --account lk-compras chats mark-read ...
/opt/data/bin/wacli --account lk-compras chats archive ...
```

Mesmo comandos aparentemente pequenos como mark-read/archive alteram estado operacional do WhatsApp e devem ser tratados como write.

## Schema de fila LK OS WhatsApp Signal

Cada sinal extraído do WhatsApp deve virar registro interno sanitizado:

```json
{
  "signal_id": "sha256(account|chat|message|timestamp)",
  "account": "lk-compras",
  "source_type": "group|dm|unknown",
  "timestamp_brt": "YYYY-MM-DDTHH:MM:SS-03:00",
  "signal_class": "stockout_related|supplier_opportunity|customer_request|drop_hype|followup|internal_ops|unknown",
  "confidence": "low|medium|high",
  "pii_level": "none|low|medium|high",
  "product_evidence": {
    "name_guess": null,
    "sku": null,
    "size": null,
    "link_domain": null
  },
  "recommended_next_step": "ignore|watchlist|validate_stock|prepare_sourcing_preview|prepare_reply_preview|needs_human_review",
  "approval_required_before": ["send", "contact", "purchase", "external_task", "write"],
  "sanitized_summary": "Resumo sem PII e sem texto literal sensível."
}
```

## Rotas operacionais

### 1. Stockout / recompra

1. Sinal chega via `lk-compras`.
2. Hermes classifica como `stockout_related` ou `customer_request`.
3. Hermes valida SKU/tamanho contra Shopify/Tiny em read-only.
4. Se houver stockout real: Droper primeiro; se Droper não tiver, StockX/GOAT fallback.
5. Hermes prepara preview para Lucas/Júlio/Notion.
6. Envio/tarefa/compra só com aprovação explícita.

### 2. Fornecedor / oportunidade

1. Sinal chega via grupo/DM.
2. Hermes não responde.
3. Classifica como `supplier_opportunity`.
4. Cruza com sell-through, Tiny e demanda real.
5. Gera watchlist ou preview de validação.
6. Contato externo só com aprovação.

### 3. CRM/cliente

1. Sinal de cliente só pode virar resumo sanitizado.
2. Antes de qualquer resposta: cruzar com Shopify/Supabase/Klaviyo se necessário.
3. Gerar copy preview.
4. Enviar WhatsApp/Klaviyo/email só com aprovação.

## Formato de aprovação inline para envio futuro

Se um dia houver pedido para enviar WhatsApp, a aprovação no Telegram deve trazer tudo inline:

```text
Aprovação solicitada — WhatsApp LK Compras
Conta: lk-compras
Destino: [grupo/fornecedor/cliente sanitizado]
Motivo: [stockout/pedido especial/follow-up]
Texto exato a enviar:
"..."
Não autoriza: compra, reserva, preço, Shopify/Tiny write, novo follow-up automático.
Para aprovar, responda: APROVO ENVIAR LK-COMPRAS [código]
```

Sem esse formato, não enviar.

## Próximo bloco seguro recomendado

Criar um **watch/read-only manual** de 24h para `lk-compras`:

- sem cron;
- sem envio;
- sem nomes/telefones/texto literal no Telegram;
- saída: contagem de sinais por categoria + 3 exemplos sanitizados no máximo;
- objetivo: calibrar se o canal realmente alimenta stockout/sourcing/compra.

Isso ainda deve ser aprovado antes de ler conteúdo de conversas em lote, porque `lk-compras` contém PII e contato operacional.

## Não executado

- nenhum WhatsApp enviado;
- nenhuma conversa exportada em claro;
- nenhum contato com cliente/fornecedor/grupo;
- nenhum cron criado;
- nenhum write em Shopify, Tiny, banco, Klaviyo, Meta, Google, Notion, n8n ou Merchant;
- nenhuma compra, reserva ou reposição executada.
