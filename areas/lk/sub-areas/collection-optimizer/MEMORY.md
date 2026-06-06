# MEMORY — [LK] Otimização de Coleções

## Decisões duráveis

- O LKGOC pertence ao agente permanente `[LK] Otimização de Coleções` (`lk-collection-optimizer`).
- LK Growth e LK Shopify são agentes pares/independentes; não são pais do LKGOC.
- Workers LKGOC são temporários e escolhidos por demanda; nunca ativar todos por padrão.
- Otimização LKGOC Full usa material existente só como inventário/evidência e reconstrói a experiência do zero.
- Tema production nunca recebe write direto por padrão; usar DEV/branch, approval, PR/merge/deploy/readback/receipt.
