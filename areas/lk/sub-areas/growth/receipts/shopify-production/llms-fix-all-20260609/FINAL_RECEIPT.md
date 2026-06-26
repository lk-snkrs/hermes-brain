# Receipt — LK LLM/GEO Fix All 2026-06-09

Data: 2026-06-09T18:21:05.282744+00:00
Executor: LK Growth / Hermes
Aprovação Lucas: “CORRIGIR TUDO EM PARALELO E USANDO SUB AGENTES”
Escopo: Shopify production theme — arquivos AI/GEO, agent instructions, robots, schema FAQ condicional.

## Resultado executivo

Executado com sucesso parcial/seguro:

- `/llms.txt` foi enxugado de ~51k para ~5k caracteres e ficou estratégico, com 31 URLs públicas no readback.
- `/agents.md` foi enxugado de ~9.7k para ~5k e deixou de prometer fluxo MCP/UCP funcional; agora marca MCP/UCP como experimental até validação real de tools.
- `/llms-full.txt` manteve o inventário completo, mas removeu promoção de sitemap agentic e ajustou bloco de agentes para não vender MCP como funcional.
- `/robots.txt` deixou de promover `sitemap_agentic_discovery.xml`, porque a rota real é externa/nativa e segue fraca.
- Adicionado snippet não visual `snippets/lk-growth-geo-faq-schema.liquid`.
- `layout/theme.liquid` passou a renderizar o snippet condicional no `<head>`.
- FAQPage validado por readback em:
  - `/collections/nike-vomero-premium`
  - `/pages/crocs-relampago-mcqueen-guia`
  - `/pages/loja-fisica`
  - `/pages/sobre-a-lk`

## Assets alterados em produção

- `templates/llms.txt.liquid`
- `templates/llms-full.txt.liquid`
- `templates/agents.md.liquid`
- `templates/robots.txt.liquid`
- `snippets/lk-growth-geo-faq-schema.liquid`
- `layout/theme.liquid`

Asset criado e removido durante tentativa técnica:

- `templates/sitemap_agentic_discovery.xml.liquid` — removido, pois Shopify/rota nativa externa não serviu o template no root.

## Readback final público

- `/llms.txt`: 200, 5.030 chars, Source Map presente, 31 URLs, termos críticos 0.
- `/llms-full.txt`: 200, 122.351 chars, Source Map presente, 492 URLs, termos críticos 0.
- `/agents.md`: 200, 5.072 chars, Source Map presente, 22 URLs, UCP/MCP marcado como experimental, termos críticos 0.
- `/robots.txt`: 200, não promove sitemap agentic fraco, termos críticos 0.
- `/.well-known/ucp`: 200, rota externa/nativa Shopify.
- `/sitemap_agentic_discovery.xml`: 200, ainda lista só `/agents.md`; não é promovido nos arquivos controlados.
- `/api/ucp/mcp`: 422, erro externo/nativo `UCP discovery failed / Missing profile uri`.

Termos críticos zerados nos arquivos centrais:

- pronta entrega: 0
- encomenda: 0
- estoque: 0
- sob encomenda: 0
- prazo de entrega: 0
- confirme disponibilidade: 0

## Validação schema FAQ

Reteste público com cache-buster confirmou `FAQPage` e perguntas LK em:

- Nike Vomero Premium: OK.
- Crocs Relâmpago McQueen guia: OK.
- Loja Física: OK.
- Sobre a LK: OK.

Observação: houve uma ocorrência transitória de 503 em duas leituras com cache-buster e uma variação de cache em `/pages/sobre-a-lk`; retries retornaram 200 e schema OK. Sem `Liquid error`.

## Subagentes / paralelização lógica

- Worker A — AI source map: `llms.txt` curto e prioridade GEO.
- Worker B — Agent correctness: `agents.md` e `llms-full.txt` sem promessa quebrada de MCP.
- Worker C — Discovery/robots: tentativa de sitemap template, rollback do asset não servido e remoção de promoção em robots.
- Worker D — Schema: FAQPage condicional nas páginas sem schema.
- Worker E — QA/receipt: readback, monitor e secret scan.

## Blockers reais

### UCP/MCP

Não corrigido na origem porque não está em asset de theme Shopify. Evidência:

- `/.well-known/ucp` é JSON externo/nativo e aponta endpoints `lk-sneakerss.myshopify.com`.
- `POST /api/ucp/mcp` continua 422 com `Missing profile uri`, inclusive no domínio myshopify.
- Correção provável exige configuração nativa Shopify/UCP/app/proxy fora do theme.

Mitigação aplicada:

- `agents.md` e `llms-full.txt` agora tratam MCP/UCP como experimental e pedem validação do endpoint antes de qualquer uso.

### sitemap_agentic_discovery.xml

Não corrigido na origem porque a rota root não é servida pelo template criado no theme.

Mitigação aplicada:

- Removida promoção desse sitemap em `robots.txt`, `llms.txt`, `llms-full.txt` e `agents.md`.
- Rota continua pública com 1 URL, mas não é mais usada como fonte prioritária controlada pela LK Growth.

## Rollback

Backups em:

- `assets-before/`

Rollback manual:

- Reaplicar arquivos correspondentes de `assets-before/` para os assets alterados.
- Remover `snippets/lk-growth-geo-faq-schema.liquid`.
- Remover o render do snippet `lk-growth-geo-faq-schema` de `layout/theme.liquid` ou restaurar `layout__theme.liquid` do backup.

## Sem alterações fora do escopo

Não alterado:

- Produto, preço, estoque/disponibilidade, imagens, GTIN, coleções via metafield, Ads, GMC/feed, Klaviyo/WhatsApp, checkout, pagamentos.

## Arquivos de evidência

- `public-readback-final.json`
- `assets-before/`
- `assets-candidate/`
- `diffs/`
