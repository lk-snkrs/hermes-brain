# Template — Preview/Aprovação LK Shopify

Use este template sempre que LK Shopify preparar criação/alteração de produto, coleção, página, SEO fields, menu, tema/dev theme, inventory mirror ou qualquer write Shopify/Tiny relacionado.

## 1. Veredito curto

- Tipo de ação:
- Alvo exato:
- Risco: A1 preview / A3 write externo / A4 produção-sensível
- Status recomendado: preview-only / draft / active / dev theme / produção

## 2. Fonte viva e evidências

- Shopify read-only consultado em:
- Tiny consultado em, quando envolver estoque/SKU:
- Outras fontes: GOAT / StockX / Droper / GSC / GA4 / GMC / Judge.me / tema
- Lacunas ou incertezas:

## 3. Snapshot antes

- Campo/objeto atual:
- IDs/handles/variant IDs envolvidos:
- Backup/rollback path previsto:
- Hash/contagem/estado antes quando aplicável:

## 4. Alteração proposta

Listar exatamente cada campo que será escrito.

- Produto/coleção/página/tema/menu:
- Campo:
- Valor atual:
- Valor novo:
- Motivo:
- Fonte/critério:

## 5. Padrão canônico aplicado

Marcar o padrão aprovado que está sendo reutilizado, em vez de inventar um novo formato:

- Produto/upload: `lk-shopify-product-upload`
- Read-only/catálogo/order/customer: `lk-shopify-readonly`
- SKU/Tiny: Tiny `codigo` como referência, Shopify como superfície
- Coleção/source page/editorial: padrão Moon Shoe + `PADRAO-GUIAS-EDITORIAIS-LK.md`
- Theme/CRO: dev theme + screenshot/QA mobile-first antes de produção
- Menu/tag/SEO field: exception pattern correspondente da skill `lk-shopify-readonly`
- Outro padrão aprovado:

## 6. Readback e verificação esperados

- Consulta de readback:
- Condição de sucesso:
- Condição de falha:
- Como provar que nada fora do escopo mudou:

## 7. Rollback

- Como desfazer:
- Dados necessários para rollback:
- Tempo/risco do rollback:

## 8. O que NÃO está aprovado

- Preço/estoque/status/publicação, se não listado acima
- Tiny write, se não listado acima
- GMC/Klaviyo/Meta/WhatsApp/email/campanha
- Theme production publish, se não listado acima
- Contato com cliente/fornecedor

## 9. Texto de aprovação para Telegram

Copiar no Telegram com campos inline, não apenas link local:

> Aprovo LK Shopify executar exatamente este preview: [ação], [alvo], [campos], [status], com snapshot/readback/receipt/rollback. Não aprovo preço/estoque/campanha/contato externo fora do que está listado.
