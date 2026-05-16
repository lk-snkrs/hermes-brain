# LK OS — Telegram-Inline Approval Rewrites for GMC P1 Gates, 2026-05-12

Generated at: `2026-05-12T23:02:42.899026+00:00`

## Status

`telegram_inline_rewrites_ready_no_external_write`

Este arquivo converte os principais gates GMC P1 para superfície de decisão compatível com Telegram. Ele é trilha de auditoria local; a regra operacional é que qualquer aprovação futura deve colar o conteúdo relevante inline no chat, não apenas apontar para este caminho.

## Fontes consultadas

- `fact/derived_reconciliation`: relatórios GMC locais já gerados em `reports/`.
- `fact_tiny_stock`: ainda pendente no packet P1-B em background; nenhuma chamada Tiny nova foi feita por este rewrite.
- `manual_approval`: execução anterior já registrada para P1 core attrs 4 campos.

## Não executado

- Tiny call manual: 0
- Shopify call/write: 0
- Merchant call/write/delete: 0
- Feed/fetch: 0
- Banco/POS/local inventory setting: 0
- Campanha/envio/fornecedor/Notion: 0

---

## Rewrite 1 — P1 core attributes: NÃO pedir aprovação pelo packet antigo

### Veredito Telegram-ready

Não pedir aprovação para o antigo pacote geral `title/link/imageLink/price/availability`.

Motivo: o escopo seguro de 4 campos já foi aplicado e verificado separadamente:

- Candidatos aplicados e verificados no relatório final: 1.627 exact online product IDs.
- Campos atualizados: `title`, `link`, `imageLink`, `price`.
- Campo excluído: `availability`.
- Motivo da exclusão: Tiny é fonte de verdade de estoque.
- Ainda faltando `availability` no status pós-apply: 1.616 produtos, conforme relatório final já registrado.

### O que isto autoriza

Nada. É um bloqueio operacional contra uso de approval packet obsoleto.

### O que não autoriza

- Não autoriza update em `availability`.
- Não autoriza reexecutar o packet antigo de 1.627 linhas.
- Não autoriza delete/insert/fetch/feed.

### Frase se Lucas perguntar por core attrs

`Core attrs 4 campos já foram aplicados e verificados; não usar o approval packet antigo. Próximo gate é availability separado, somente com Tiny OK.`

---

## Rewrite 2 — P1-B availability: aprovação futura somente depois do Tiny terminar

### Veredito Telegram-ready atual

Ainda não pedir aprovação de `availability`. O packet Tiny P1-B está em andamento/backpressure e `availability` só pode ser proposta quando cada linha tiver resposta Tiny oficial OK.

### Texto de aprovação futuro — usar só após conclusão do Tiny

`Preciso de resposta — GMC P1-B availability`

`Fonte de verdade: Tiny ERP, código exato por SKU/oferta, preferencialmente depósito LK | CONTROLE ESTOQUE.`

`Resumo do packet final:`

- `ready_in_stock`: preencher com contagem final Tiny OK > 0.
- `ready_out_of_stock`: preencher com contagem final Tiny OK = 0.
- `blocked_tiny_stock_api_error`: preencher com linhas Tiny não-OK/erro/backpressure.
- `excluded`: qualquer linha sem evidência Tiny OK.

`O que a aprovação autoriza:`

- Atualizar somente `availability` em produtos online exatos do Merchant que estejam no conjunto `ready`.
- Usar apenas valores `in stock` ou `out of stock` derivados de resposta Tiny OK.
- Rodar fail-fast em lote pequeno primeiro, com rollback snapshot privado antes do write.

`O que a aprovação NÃO autoriza:`

- Não autoriza Shopify/Tiny/DB/POS writes.
- Não autoriza feed/fetch/datafeed.
- Não autoriza sourcing, compra, fornecedor, Droper/StockX/GOAT, Notion/Júlio.
- Não autoriza transformar erro Tiny em `out of stock`.

`Opções:`

1. `Aprovar lote piloto availability` — autoriza somente os primeiros 25 produtos ready com evidência Tiny OK, com rollback e verificação pós-delay.
2. `Pausar` — não executa nada no Merchant.
3. `Revisar antes` — eu colo no Telegram os 25 primeiros product IDs + valores Tiny para validação humana antes de pedir apply.

`Minha recomendação: opção 3 primeiro, porque availability afeta venda/anúncio e Tiny está sofrendo backpressure.`

---

## Rewrite 3 — Local C/D 63 IDs antigos LIA: se for pedir aprovação, colar lista exata

### Veredito Telegram-ready

Há um pacote local/POS de limpeza com 63 IDs antigos `local:pt:BR:LIA_<old_sku>`. Este pacote não mexe em produtos online. Se for pedir execução, o Telegram deve conter a lista abaixo, não apenas CSV/JSON.

### O que a aprovação autorizaria

- Deletar somente estes 63 product IDs locais antigos no Merchant.
- Preservar replacements locais já presentes.
- Verificar `old gone + replacement present` depois do delay de consistência.
- Usar snapshot privado de rollback já registrado antes de execução.

### O que a aprovação NÃO autorizaria

- Não autoriza tocar produtos online.
- Não autoriza Shopify, Tiny, POS, banco, feed, campanha, envio ou fornecedor.
- Não autoriza deletar nenhum ID fora da lista inline.

### Lista exata dos 63 IDs antigos

- Boné 5 Panel Aimé Leon Dore Unisphere Azul — 1 IDs antigos
  - `local:pt:BR:LIA_ALD-8631262-OS`
- Camisa Manga Curta Boxy Saint Studio Egípcio Listrada Marinho — 4 IDs antigos
  - `local:pt:BR:LIA_SST-2772190-L`
  - `local:pt:BR:LIA_SST-2772190-M`
  - `local:pt:BR:LIA_SST-2772190-S`
  - `local:pt:BR:LIA_SST-2772190-XL`
- Camiseta Boxy Saint Studio Supima Preto — 4 IDs antigos
  - `local:pt:BR:LIA_SST-2837726-L`
  - `local:pt:BR:LIA_SST-2837726-M`
  - `local:pt:BR:LIA_SST-2837726-S`
  - `local:pt:BR:LIA_SST-2837726-XL`
- Camiseta Pace Waffle Knit Off White — 3 IDs antigos
  - `local:pt:BR:LIA_PAC-5280094-M`
  - `local:pt:BR:LIA_PAC-5280094-S`
  - `local:pt:BR:LIA_PAC-5280094-XL`
- Camiseta Represent Clo Revere Manor Aged White Branco — 4 IDs antigos
  - `local:pt:BR:LIA_REP-4481630-L`
  - `local:pt:BR:LIA_REP-4481630-M`
  - `local:pt:BR:LIA_REP-4481630-S`
  - `local:pt:BR:LIA_REP-4481630-XL`
- Camiseta Represent Clo Revere Manor Stained Black Preto — 4 IDs antigos
  - `local:pt:BR:LIA_REP-4448862-L`
  - `local:pt:BR:LIA_REP-4448862-M`
  - `local:pt:BR:LIA_REP-4448862-S`
  - `local:pt:BR:LIA_REP-4448862-XL`
- Camiseta Represent Clo Shark Jaws Off Black Preto — 4 IDs antigos
  - `local:pt:BR:LIA_REP-4547166-L`
  - `local:pt:BR:LIA_REP-4547166-M`
  - `local:pt:BR:LIA_REP-4547166-S`
  - `local:pt:BR:LIA_REP-4547166-XL`
- Camiseta Represent Clo Storms In Heaven Black Preto — 4 IDs antigos
  - `local:pt:BR:LIA_REP-4645470-L`
  - `local:pt:BR:LIA_REP-4645470-M`
  - `local:pt:BR:LIA_REP-4645470-S`
  - `local:pt:BR:LIA_REP-4645470-XL`
- Moletom Represent Clo Masking Tape Initial Cedar Marrom — 4 IDs antigos
  - `local:pt:BR:LIA_REP-7451998-L`
  - `local:pt:BR:LIA_REP-7451998-M`
  - `local:pt:BR:LIA_REP-7451998-S`
  - `local:pt:BR:LIA_REP-7451998-XL`
- Pop Mart Labubu The Monsters Coca Cola Series Happy Factor Vinyl Plush Pingente — 1 IDs antigos
  - `local:pt:BR:LIA_LAB-0132830-OS`
- Shorts Represent Clo Owners Club Flat White Branco — 4 IDs antigos
  - `local:pt:BR:LIA_REP-7288158-L`
  - `local:pt:BR:LIA_REP-7288158-M`
  - `local:pt:BR:LIA_REP-7288158-S`
  - `local:pt:BR:LIA_REP-7288158-XL`
- Tênis Adidas Tokyo Crew White Floral Embroidery Branco — 7 IDs antigos
  - `local:pt:BR:LIA_ADI-3400542-34`
  - `local:pt:BR:LIA_ADI-3400542-35`
  - `local:pt:BR:LIA_ADI-3400542-36`
  - `local:pt:BR:LIA_ADI-3400542-37`
  - `local:pt:BR:LIA_ADI-3400542-38`
  - `local:pt:BR:LIA_ADI-3400542-39`
  - `local:pt:BR:LIA_ADI-3400542-40`
- Tênis Onitsuka Tiger Mexico 66 SD Metallic Series Pale Mint Cream Azul — 9 IDs antigos
  - `local:pt:BR:LIA_ONI-5436510-34`
  - `local:pt:BR:LIA_ONI-5436510-35`
  - `local:pt:BR:LIA_ONI-5436510-36`
  - `local:pt:BR:LIA_ONI-5436510-37`
  - `local:pt:BR:LIA_ONI-5436510-38`
  - `local:pt:BR:LIA_ONI-5436510-39`
  - `local:pt:BR:LIA_ONI-5436510-40`
  - `local:pt:BR:LIA_ONI-5436510-41`
  - `local:pt:BR:LIA_ONI-5436510-42`
- Tênis Onitsuka Tiger Mexico 66 Sabot Birch Peacoat Bege — 10 IDs antigos
  - `local:pt:BR:LIA_ONI-3740254-34`
  - `local:pt:BR:LIA_ONI-3740254-35`
  - `local:pt:BR:LIA_ONI-3740254-36`
  - `local:pt:BR:LIA_ONI-3740254-37`
  - `local:pt:BR:LIA_ONI-3740254-38`
  - `local:pt:BR:LIA_ONI-3740254-39`
  - `local:pt:BR:LIA_ONI-3740254-40`
  - `local:pt:BR:LIA_ONI-3740254-41`
  - `local:pt:BR:LIA_ONI-3740254-42`
  - `local:pt:BR:LIA_ONI-3740254-43`

### Bloco de aprovação correto no Telegram

`Preciso de resposta — GMC Local C/D 63 IDs antigos`

1. `Aprovar delete exato dos 63 IDs locais listados acima` — autoriza somente esses 63 deletes no Merchant local, com rollback snapshot e verificação pós-delay.
2. `Pausar` — não executa nada.
3. `Revisar item por item` — eu separo por produto/título antes de qualquer apply.

`Minha recomendação: opção 1 só se quisermos limpar diagnósticos locais agora; caso contrário, priorizar P1-B availability após Tiny.`

---

## Rewrite 4 — Package B2 Shopify live: no-op, não pedir aprovação

### Veredito Telegram-ready

Não há execução B2 para aprovar.

- Linhas avaliadas: 854 variants ativos com SKU no Shopify live.
- Candidatos prontos para aprovação: 0.
- Status: same-ID/no-op válido pelo guard anti-delete.

### O que isto autoriza

Nada. É fechamento de gate.

### O que não autoriza

- Não autoriza insert-new/delete-old.
- Não autoriza Merchant write/delete.
- Não autoriza Shopify/Tiny/feed/POS/DB.

---

## Fila recomendada após este rewrite

1. Aguardar o watchdog do Tiny P1-B sem fazer novas chamadas manuais Tiny.
2. Quando Tiny finalizar, gerar mensagem Telegram inline com contagens finais e, se houver `ready`, colar primeiro lote de 25 IDs + valores `availability` para revisão/aprovação.
3. Só depois considerar Local C/D 63 IDs, porque é cleanup local e menos urgente que `availability` online.

## Audit references locais

- `reports/lk-gmc-2026-05-12-p1-core-attrs-4field-apply-final.md`
- `reports/lk-gmc-2026-05-12-p1-availability-tiny-packet-resume-status.md`
- `reports/lk-gmc-2026-05-12-local-cd-final-approval-packet.md`
- `reports/lk-gmc-2026-05-12-package-b2-shopify-live-preview.md`
