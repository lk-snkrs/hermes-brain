# Rotina — Consulta de vendas de obras Zipper

## O que faz

Consulta o banco Zipper Vendas para responder perguntas comerciais com evidência.

## Fonte de verdade

- Supabase Zipper Vendas `pcstqxpdzibheuopjkas`.
- Tabela citada: `vendas_tango`.

## Quando usar

- Antes de afirmar que obra/artista vende bem.
- Antes de montar abordagem comercial.
- Antes de comparar canais ou origem de pedido.

## Credenciais

Buscar via Doppler `lc-keys/prd`; nunca versionar valores.

- `SUPABASE_ZIPPER_VENDAS_URL`
- `SUPABASE_ZIPPER_VENDAS_SERVICE_KEY`

## Verificação

1. Consultar fonte real.
2. Informar período analisado.
3. Separar Zipper Vendas de SPITI.
4. Se dado estiver ausente, responder com ressalva.
