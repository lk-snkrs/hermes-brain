# QA local — v8

Checks executados:
- Padrão LKGOC consultado: 204L collection + Moon Shoe guide.
- Ledger consultado: 9060 e 530 já constam como LKGOC Production; v8 trata esses dois como refresh/AI visibility, não nova LKGOC.
- Shopify lido em read-only para handles/body_html; sem alteração externa.
- DataForSEO usado para volume, intent e SERP.
- Guardrail preservado: não transformar disponibilidade/prazo/estoque em taxonomia pública; não consultar estoque; não prometer disponibilidade.

Problemas atuais detectados antes de aplicar:
- New Balance 530: body_html atual tem copy marketplace, promessa operacional e FAQ truncado (“itens selecionados: envio em”).
- Alo Yoga: body_html atual tem FAQ truncado e linguagem operacional.
- Adidas Tokyo: narrativa atual parece atribuir a linha a Tokyo 2020; SERP aponta inspiração anos 70/Japan/Tóquio 1964. Corrigir factual antes de produção.
- Nike Air Rift: copy atual é aceitável mas curta; v8 melhora citabilidade e editorialidade.
- Air Jordan 1 Low: coleção específica rankeia na SERP, mas precisa tom curatorial menos transacional.

Bloqueios para produção:
- Qualquer alteração de body_html, SEO title/meta, schema, llms.txt ou theme precisa aprovação explícita de Lucas com escopo.
- Se envolver LKGOC visual/theme: DEV/unpublished verificado por API → QA → approval → merge production.
