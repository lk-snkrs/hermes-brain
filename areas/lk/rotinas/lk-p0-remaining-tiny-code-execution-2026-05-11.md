# Execução aprovada — P0 restantes: preenchimento de codigo Tiny (7 itens) — 2026-05-11

## Escopo aprovado

Lucas aprovou em Telegram: preencher `codigo` Tiny dos 7 itens candidatos com os SKUs Shopify propostos, sem alterar Shopify, preço, estoque ou produto.

## Resultado final

- Candidatos aprovados: 7
- Tiny writes finais verificados ao vivo: 7/7
- Falhas finais: 0
- Shopify writes: 0
- Alterações de preço/estoque/produto detectadas na verificação final: 0

## Códigos preenchidos no Tiny

- Tiny `1069545385` — `Tênis Nike Mind 002 Light Khaki Bege - 41`
  - `codigo`: `NKE-9054174-41`
  - preço: `2999.99`; unidade: `UN`; situação: `A`; tipo: `P`
  - grade: `{"Tamanho do calçado": "41"}`
- Tiny `1070120736` — `Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom - 42.5`
  - `codigo`: `ONI-0995678-425`
  - preço: `2999.99`; unidade: `UN`; situação: `A`; tipo: `P`
  - grade: `{"Tamanho do calçado": "42.5"}`
- Tiny `1069544047` — `Tênis New Balance 204L Cortado Marrom - 37`
  - `codigo`: `NB-0254942-37`
  - preço: `2799.99`; unidade: `UN`; situação: `A`; tipo: `P`
  - grade: `{"Tamanho do calçado": "37"}`
- Tiny `1070119554` — `Tênis Onitsuka Tiger Mexico 66 Sabot Pure Silver Cream Cinza - 38`
  - `codigo`: `ONI-6772830-38`
  - preço: `2199.99`; unidade: `UN`; situação: `A`; tipo: `P`
  - grade: `{"Tamanho do calçado": "38"}`
- Tiny `1069542767` — `Moletom Alo Yoga Cropped Serenity Coverup Black Preto - S/P`
  - `codigo`: `ALO-8506462-S`
  - preço: `1799.99`; unidade: `UN`; situação: `A`; tipo: `P`
  - grade: `{"Tamanho": "S/P"}`
- Tiny `1069544315` — `Calça Saint Studio Alfaiataria Leve Prega Dupla Cinza - L/G`
  - `codigo`: `SST-4542302-L`
  - preço: `619.99`; unidade: `UN`; situação: `A`; tipo: `P`
  - grade: `{"Tamanho": "L/G"}`
- Tiny `1069930823` — `Camiseta Pace Buero Washed Black Preto - S/P`
  - `codigo`: `PAC-1197278-S`
  - preço: `319.99`; unidade: `UN`; situação: `A`; tipo: `P`
  - grade: `{"Tamanho": "S/P"}`

## Observação operacional

- A primeira tentativa usou payload com `grade` para todos os itens. Nos 4 calçados, funcionou sem mudança adjacente.
- Nos 3 itens de vestuário, o Tiny normalizou pontuação do nome (`S-P`/`L-G` para `S/P`/`L/G`). Como isso violava o guardrail de não alterar produto, o script fez rollback automático desses 3 códigos.
- Após cooldown de rate limit, os 3 itens de vestuário foram reexecutados com payload sem `grade`, mantendo nome e campos adjacentes intactos. Verificação final confirmou `codigo` correto nos 7 itens.
- Tiny exige `sequencia` dentro do registro `produto` no wrapper `produtos[].produto`; `produto.obter` não retorna esse campo para variações filhas, então usar `sequencia: "1"` para single-record writes.
- Para evitar bloqueio `API Bloqueada - Excedido o número de acessos`, usar espaçamento conservador entre chamadas em writes Tiny.

## Artefatos

- `reports/lk-p0-remaining-tiny-code-execution-2026-05-11.json`
- `reports/lk-p0-remaining-tiny-code-execution-retry-apparel-2026-05-11.json`
- `reports/lk-p0-remaining-tiny-code-final-verification-2026-05-11.json`
- `scripts/lk_p0_remaining_tiny_code_execute_20260511.py`
- `scripts/lk_p0_remaining_tiny_code_retry_apparel_20260511.py`
- `scripts/lk_p0_remaining_tiny_code_final_verify_20260511.py`

## Pendências remanescentes

Após estes 7, continuam bloqueados os 6 itens já classificados no preview por falta de SKU Shopify, match Tiny ambíguo ou ausência de cadastro/mapeamento canônico seguro.
