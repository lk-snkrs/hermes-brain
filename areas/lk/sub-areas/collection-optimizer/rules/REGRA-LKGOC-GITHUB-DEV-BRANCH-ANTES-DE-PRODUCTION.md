# REGRA — LKGOC GitHub DEV branch antes de Production

Registrado em: 20260608T150751Z
Status: **BLOQUEANTE / CANÔNICO / CORREÇÃO LUCAS**

## Correção Lucas

O fluxo correto do LKGOC **não é escrever direto no Shopify Production/main**.

Fluxo obrigatório:

1. Trabalhar no **GitHub na branch DEV**.
2. Gerar/validar preview em ambiente DEV/unpublished quando aplicável.
3. Fazer QA visual/readback/side-by-side com Gold Source 204L.
4. Enviar approval packet para Lucas.
5. Após aprovação explícita, fazer **merge da branch DEV para a branch Production**.
6. Só então seguir o deploy/promoção controlada para production, com rollback, receipt e revisão de impacto.

## Proibição absoluta

- Nunca fazer write direto em Shopify Production/main.
- Nunca tratar theme `role=main` como área de teste.
- Nunca aplicar patch independente em production fora do fluxo GitHub DEV → merge Production.
- Mesmo com urgência, a exceção precisa ser aprovada explicitamente por Lucas com escopo nominal; default é **não executar**.

## Como o agente deve comunicar

Ao mencionar production, dizer:

> Production só recebe mudança via GitHub: branch DEV aprovada → merge para branch Production → deploy/promoção controlada.

Não dizer apenas “sem write production sem aprovação”, pois isso pode sugerir que write direto seria aceitável com aprovação. O padrão correto é **merge via GitHub**.
