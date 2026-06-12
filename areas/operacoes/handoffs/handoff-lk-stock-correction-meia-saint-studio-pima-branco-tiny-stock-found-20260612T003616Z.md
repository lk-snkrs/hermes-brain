# Correção de handoff LK Stock → LC Hermes — Meia Saint Studio Pima Branco

Data/hora: 2026-06-12T00:36:16Z
Agente/profile: `lk-stock`
Empresa/área: LK Sneakers / Stock OS / Tiny read-only fallback
Responsável humano: Lucas Cimino

## Correção

O handoff anterior classificou corretamente a ausência de vínculo Shopify→Stock OS, mas ficou incompleto: faltou executar fallback read-only no Tiny por título para descobrir o estoque real da meia.

## Resultado live Tiny read-only

Busca Tiny `produtos.pesquisa` por `Meia Saint Studio Pima Branco` retornou candidato exato:

- Tiny id: `1071195617`
- Tiny código/SKU: vazio
- Nome: `Meia Saint Studio Pima Branco`
- Situação: `A`
- Depósito oficial: `LK | CONTROLE ESTOQUE`
- Saldo: `1.0`
- `desconsiderar`: `N`

## Diagnóstico corrigido

Existem duas verdades separadas:

1. **Estoque existe no Tiny:** há `1` unidade da `Meia Saint Studio Pima Branco` no depósito oficial.
2. **Vínculo operacional continua quebrado:** Shopify variant `48283857780958` segue sem SKU/barcode/metafield/mapping local, e o produto Tiny também está com `codigo` vazio.

Portanto, o erro não era “não existe estoque”; o erro operacional era o lookup do Stock OS não ter fallback de busca por título no Tiny quando a identidade Shopify estava vazia.

## Decisão segura atual

- Para estoque interno: `confirmado via Tiny read-only`, saldo `1`.
- Para automação/Stock OS: ainda precisa criar alias/mapping local ou preencher chave operacional.
- Reposição automática: não aprovar; há saldo 1 e identidade quebrada.
- Tiny write: `0`.
- Shopify write: `0`.
- Writes externos: `0`.
- Pronta entrega pública/promessa ao cliente: `0` sem fluxo de atendimento aprovado.

## Próxima correção sistêmica necessária

Adicionar ao procedimento do lk-stock uma regra de exceção:

Se Shopify/DB local não resolve porque SKU/barcode/metafield estão vazios, executar fallback read-only no Tiny por título/handle normalizado antes de concluir “sem estoque”. Classificar o resultado como `stock_found_by_title_fallback_identity_unlinked` quando encontrar candidato exato por nome mas sem código operacional.

## Mensagem para LC Hermes

> Correção: a meia foi encontrada no Tiny por busca read-only de título. Tiny id `1071195617`, nome `Meia Saint Studio Pima Branco`, código vazio, saldo `1` no depósito `LK | CONTROLE ESTOQUE`. A falha foi do Stock OS/lookup: ele parou na ausência de chave Shopify→Tiny/DB e não fez fallback por título. O vínculo operacional continua quebrado, mas o estoque existe.

## Onde fica documentado

`areas/operacoes/handoffs/handoff-lk-stock-correction-meia-saint-studio-pima-branco-tiny-stock-found-20260612T003616Z.md`
