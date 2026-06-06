# LK Growth — SOP decision-grade para packets de coleção SEO/GEO/CRO

Atualizado: 2026-06-05

## Regra Lucas — approval UX

Sempre que houver aprovação necessária em Telegram, entregar o approval packet com **Botão Inline** quando o canal/runtime disponibilizar esse recurso. Se o runtime atual não expuser ferramenta de botão, deixar o pacote em formato `APPROVAL_PACKET` e sinalizar explicitamente que deve ser enviado pelo Hermes com botão inline.

## Regra de qualidade: Packet A/B não é só “trocar texto”

Para qualquer packet de coleção que altere SEO/meta, descrição, FAQ, schema, guia, template ou tema, usar a lógica abaixo antes de recomendar produção.

### 1. Shopify/theme discovery

- Identificar se o problema vem de collection SEO fields, `descriptionHtml`, metafield, snippet, section ou template.
- Registrar theme alvo quando houver tema: `theme_id`, `name`, `role`.
- DEV obrigatório para qualquer alteração de theme/layout/schema renderizado.
- Production write direto só com aprovação explícita, backup, readback e rollback.

### 2. GSC — demanda real da LK

- Usar GSC para páginas/queries: impressões, cliques, CTR, posição, indexação e sitemap.
- Priorizar mudanças por páginas com impressões/posição e CTR sensível.
- Se GSC não estiver disponível no runtime, declarar `GSC ausente — não decision-grade completo`.

### 3. GA4/Shopify — impacto comercial

- Cruzar landing pages com sessões, add_to_cart, checkout, pedidos, receita e CVR quando possível.
- Shopify/GA4 prevalecem sobre intuição de SEO.
- Se GA4 não estiver disponível no runtime, declarar `GA4 ausente — impacto comercial parcial`.

### 4. DataForSEO/SERP/AI visibility

- Usar DataForSEO para volume, intenção, SERP live, concorrentes, PAA e snippets.
- Para GEO/AI, usar APIs de AI visibility/LLM mentions quando disponíveis; se houver 402/sem acesso, declarar limitação.
- Separar SERP transacional, informacional e mista.

### 5. Ahrefs/autoridade/gap competitivo

- Rodar probe read-only Ahrefs quando disponível.
- Usar para autoridade/backlinks/gap; não substituir GSC/GA4.
- Se endpoint disponível só em nível domínio, declarar granularidade limitada.

### 6. Camada Claude SEO / skill SEO

- Carregar/usar as referências da skill SEO/LK SEO antes de escrever proposta final.
- Aplicar checklist `seo-content`, `seo-ecommerce`, `seo-page`, `seo-geo`, `seo-dataforseo` quando houver dados.
- Não afirmar “rodei Claude” se foi apenas uso de skill/docs locais; declarar como `Claude SEO skill checklist aplicado localmente`.

## Saída obrigatória do packet

- Fatos, interpretação, recomendação.
- Fontes verificadas e ausentes.
- Escopo autorizado e escopo proibido.
- Risco, esforço, impacto esperado.
- Backup, readback, rollback.
- D+7/D+14 impact review.
- Approval packet com botão inline quando disponível.

## Guardrail operacional — mensagem/campo de encomenda

- Não alterar campo, badge, mensagem, metafield, tag, lógica ou qualquer fonte operacional que exiba `Sujeito a encomenda` sem aprovação explícita e separada de Lucas.
- Packets de SEO/GEO/FAQ podem ajustar copy editorial de collections apenas quando o escopo aprovado indicar `descriptionHtml`/SEO/meta, mas não podem tocar disponibilidade, produto, variante, estoque, checkout, tag operacional ou regra de fulfillment.
- Se `Sujeito a encomenda` aparecer como campo/mensagem operacional, tratar como fonte de verdade comercial/atendimento e excluir do lote por padrão.
