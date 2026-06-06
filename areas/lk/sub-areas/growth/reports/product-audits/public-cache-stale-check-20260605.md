# Public storefront stale-cache check — product description cleanup

- Data: 2026-06-05
- Contexto: Admin/GraphQL e REST mostram descrições corrigidas; QA público encontrou uma PDP ainda servindo HTML antigo.

## Evidência

- Produto: `tenis-adidas-gazelle-stack-collegiate-green-cream-white-verde`
- Admin REST/GraphQL: descrição nova presente.
- Storefront público via HTML: ainda exibe trecho antigo `Estoque próprio: envio em até 2 dias úteis` e FAQPage antigo no HTML.
- Tentativa segura: toque REST com body_html atual + trailing newline; `updated_at` mudou, mas HTML público ainda serviu versão antiga no teste imediato.

## Interpretação

- Provável cache/storefront render delay ou camada pública servindo versão anterior para algumas PDPs.
- Tema ativo já contém FAQ genérico mais neutro em `sections/lk-pdp.liquid`; busca no tema ativo não encontrou a frase antiga nessa seção.
- O único hit no tema ativo para linguagem operacional foi `templates/llms-full.txt.liquid`, que é arquivo de AI/source, não o bloco PDP visível.

## Próximo passo seguro

- Revalidar público depois da janela de cache.
- Se persistir, abrir pacote de aprovação para investigação/patch de tema/llms ou mecanismo de cache; não executar write em theme production sem aprovação explícita.
