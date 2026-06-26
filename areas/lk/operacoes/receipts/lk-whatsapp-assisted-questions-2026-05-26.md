# Receipt — LK WhatsApp responder / venda assistida, grade ideal, canal e pulso

Data: 2026-05-26  
Área: LK Operações / WhatsApp responder  
Status: implementado e verificado

## Pedido limpo
Lucas aprovou seguir com o próximo bloco de perguntas para o Hermes no WhatsApp LK.

## O que foi implementado
- Intenção `assist` para venda assistida/read-only:
  - `cliente quer New Balance 38, o que temos?`
  - `alternativas para U204LMMC 38`
- Intenção `pulse` para resumo executivo:
  - `pulso LK agora`
  - `resumo comercial de hoje`
- Perguntas de grade ideal/recompra:
  - `quais tamanhos preciso comprar do 204L?`
- Qualidade de catálogo ativo:
  - `produtos ativos sem imagem`
  - mantém `sem SKU` / `sem tamanho`.
- Canal loja/site mais natural:
  - `o que vende mais na loja física?`
  - `top produtos do site`.
- Help atualizado com os novos exemplos.

## Comportamento
- Venda assistida consulta estoque em modo read-only e retorna opções internas com tamanho/SKU/saldo.
- Se não achar tamanho exato, deixa claro e sugere opções próximas em estoque.
- Grade ideal cruza Shopify vendas com estoque local/Tiny para sugerir comprar/repor vs observar.
- Pulso LK resume hoje: pedidos, itens, receita, top itens e qualidade de dados.

## Verificações
- `py_compile`: OK.
- Selftest offline/parser: OK.
- Selftest live Tiny read-only: OK.
- Testes live read-only executados para:
  - venda assistida New Balance;
  - alternativa U204LMMC 38;
  - grade ideal 204L;
  - catálogo ativo sem imagem;
  - loja física top produtos;
  - pulso LK agora.
- Responder reiniciado na porta 8787.
- Health local `/wacli`: 200 OK.

## Guardrails
- Sem write Shopify/Tiny.
- Sem compra automática.
- Sem reserva.
- Sem contato com cliente/fornecedor.
- Sem alteração em Docker, gateway, Traefik ou VPS.
