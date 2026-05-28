# MEMORY — LK E-commerce

## Decisões ativas

- LK E-commerce é camada de coordenação/read-only; execução produtiva deve ir ao especialista dono.
- Shopify é superfície; Tiny é verdade de estoque.
- Alterações de checkout, tema, preço, estoque, produto, campanha e contato externo exigem aprovação explícita.

## Guardrails lembrados

- Quando o problema tocar mais de uma área, abrir handoff claro em vez de misturar execução.
