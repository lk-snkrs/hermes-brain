# Approval Packet — Puma Speedcat LKGOC DEV

Status: pronto para revisão em DEV, não Production.

## Preview
`https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718`

## Mudança proposta
Aplicar na coleção Puma Speedcat o padrão LKGOC/204L já aprovado:
- mesmo template base da collection 204L;
- mesmo shell visual escuro/premium;
- texto, imagens e FAQ adaptados para Puma Speedcat;
- guia pós-grid;
- sem linguagem pública de pronta entrega/estoque.

## Impacto esperado
- Melhor leitura editorial da coleção;
- melhora de SEO/GEO para `puma speedcat`, `puma speedcat original`, `puma speedcat feminino`, `puma speedcat vermelho`, `puma speedcat preto`;
- redução de ruído de copy antiga com estoque/entrega;
- experiência mobile mais próxima da 204L.

## Risco
Baixo no DEV. Para Production, risco visual moderado porque envolve tema/collection customer-facing.

## Rollback
Reverter snippet `snippets/lk-goc-collection.liquid`, section `sections/lk-collection.liquid` e template `templates/collection.puma-speedcat.json` para backups locais/estado anterior.

## Approval necessário
Aprovação explícita de Lucas para promover para Production após revisão visual mobile/desktop.
