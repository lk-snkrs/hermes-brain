# Receipt — LK WhatsApp responder / mais variações de perguntas

Data: 2026-05-26  
Área: LK Operações / WhatsApp responder  
Status: implementado e verificado

## Pedido limpo
Lucas pediu para pensar em outras perguntas que ele ou o time possam fazer ao Hermes no WhatsApp e implementar mais possibilidades de resposta.

## O que foi feito
- Adicionada intenção de ajuda/exemplos (`ajuda`, `perguntas`, `comandos`, `possibilidades`).
- Expandida intenção de vendas para reconhecer `ticket`, `comparar`, `vs`, `top produtos`, `top tamanhos`.
- Adicionadas janelas de tempo: `trimestre`, `YTD/ano`, `MTD/mês até agora`.
- Adicionada busca de vendas por termos de produto/modelo, não só SKU. Ex.: `New Balance 204L`.
- Adicionado comparativo `hoje vs ontem`.
- Adicionada resposta de top tamanhos/variantes.
- Melhorada resposta genérica para devolver exemplos úteis em vez de uma frase curta.

## Exemplos agora suportados
- `@Hermes quais perguntas posso fazer?`
- `@Hermes tem U204LMMA 38?`
- `@Hermes manda estoque atualizado do U204LMMA`
- `@Hermes quantos U204LMMC venderam nos últimos 3 meses?`
- `@Hermes quanto vendeu New Balance 204L no mês?`
- `@Hermes top produtos da semana`
- `@Hermes top tamanhos New Balance 204L no mês`
- `@Hermes vendas YTD`
- `@Hermes compara hoje vs ontem`
- `@Hermes visitas do site`

## Verificações
- `py_compile`: OK.
- Selftest offline/parser: OK.
- Selftest live Tiny read-only: OK.
- Shopify live read-only:
  - `quanto vendeu New Balance 204L no mês?` respondeu 28 unidades em 23 pedidos, por tamanho.
  - `compara hoje vs ontem` respondeu comparação de pedidos/itens/receita.
- Health local `/wacli`: 200 OK.
- Processo ativo: `lk_hermes_whatsapp_responder.py --port 8787`, PID 160433.

## Guardrails
- Sem write Shopify/Tiny.
- Sem contato externo.
- Sem promessa de disponibilidade/preço/reserva para cliente.
- Sem alteração em Docker, gateway principal, Traefik ou VPS.

## Próximas melhorias candidatas
- Consulta de margem/lucro por SKU se houver fonte confiável de custo.
- Alertas de ruptura/baixo estoque por categoria quando houver fonte local confiável e rápida.
- Respostas por canal mais detalhadas: site vs loja/POS vs marketplaces, mantendo Shopify como fonte oficial de pedidos.
