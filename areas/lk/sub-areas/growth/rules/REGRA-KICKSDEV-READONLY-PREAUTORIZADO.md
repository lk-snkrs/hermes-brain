# REGRA — KicksDev read-only pré-autorizado para LK Growth

Data: 2026-06-07T20:49:48.437600+00:00
Decisão: Lucas autorizou permanentemente o uso da API KicksDev pelo agente LK Growth para consultas read-only.

## Regra operacional

- O agente LK Growth pode consultar a API KicksDev usando as chaves existentes no Doppler **sem pedir nova autorização a cada vez**, quando o objetivo for diagnóstico, enriquecimento, descoberta de GTIN/EAN/UPC, preço/market signal, imagens ou match de produto.
- Escopo permitido sem nova aprovação: **read-only**.
- Não expor credenciais, tokens, headers ou respostas que contenham segredo.
- Registrar fonte, endpoint/tipo de consulta, timestamp, match e confiança quando o dado for usado para decisão.

## Continua exigindo aprovação explícita atual

- Aplicar GTIN/barcode em Shopify.
- Alterar Google Merchant Center, supplemental feed ou Content API.
- Alterar preço, estoque, disponibilidade, copy pública ou qualquer dado customer-facing.
- Usar dado KicksDev de forma automática se o match não for confiável.

## Guardrail GTIN

- GTIN/EAN/UPC só pode ser aplicado quando houver match confiável por style SKU/produto/variante.
- Não inventar códigos.
- Se KicksDev não retornar GTIN/EAN/UPC ou retornar dado ambíguo, manter como bloqueado e reportar.
