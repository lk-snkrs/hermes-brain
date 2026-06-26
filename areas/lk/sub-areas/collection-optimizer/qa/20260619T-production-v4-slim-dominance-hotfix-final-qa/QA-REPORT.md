# QA final público — production v4 slim dominance

- Data UTC: 2026-06-19T16:54:03.664469+00:00
- Após merge asset + inline fallback + cache-bust invisível.

## Resultado computado
- adidas-handball-spezial / desktop: inner=OK; resumo_white=NÃO OK; labels=NÃO OK; asset=https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=151439757389105438591780406209
- adidas-handball-spezial / mobile: inner=NÃO OK; resumo_white=NÃO OK; labels=OK; asset=https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=124403439822505553251781887515
- new-balance-1906l / desktop: inner=NÃO OK; resumo_white=NÃO OK; labels=OK; asset=https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=124403439822505553251781887515
- new-balance-1906l / mobile: inner=NÃO OK; resumo_white=NÃO OK; labels=OK; asset=https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=124403439822505553251781887515
- alo-yoga-1 / desktop: inner=NÃO OK; resumo_white=NÃO OK; labels=OK; asset=https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=124403439822505553251781887515
- alo-yoga-1 / mobile: inner=NÃO OK; resumo_white=NÃO OK; labels=OK; asset=https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=124403439822505553251781887515
- air-jordan-1-low / desktop: inner=NÃO OK; resumo_white=NÃO OK; labels=OK; asset=https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=124403439822505553251781887515
- air-jordan-1-low / mobile: inner=NÃO OK; resumo_white=NÃO OK; labels=OK; asset=https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=124403439822505553251781887515

## Verdict

**Público ainda não estabilizado; cache/CDN alternando versões antigas e novas.**

- Writes aplicados com readback admin OK.
- QA público ainda pode ver HTML/CSS antigo em alguns edges.
- Recomendado revalidar em 30–60 min antes de escalar novo batch.