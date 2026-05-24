# LK GMC API/data sources investigation — 2026-05-21

Gerado em: `2026-05-21T21:25:25.205972+00:00`

## Escopo
- Investigação read-only das fontes/API conectadas ao Google Merchant Center da LK.
- Nenhum write/fetchNow/feed upload/Shopify/campanha executado.

## Endpoints verificados
- content_api_datafeeds: `{'ok': True, 'status': 200, 'count': 0}`
- content_api_products: `{'ok': True, 'status': 200, 'count': 19652}`
- content_api_productstatuses: `{'ok': False, 'status': None, 'count': 14236}`
- merchant_api_datasources_attempts: `{'v1': {'ok': True, 'status': 200, 'count': 3, 'error': None}, 'v1beta': {'ok': False, 'status': 409, 'count': 0, 'error': {'error': {'code': 409, 'message': 'The v1beta version of the Merchant API was discontinued on February 28, 2026 and is no longer available. Please upgrade to v1 version. See https://developers.google.com/merchant/api/guides/compatibility/migrate-v1beta-v1 for more details', 'status': 'ABORTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.ErrorInfo', 'reason': 'deleted', 'domain': 'merchantapi.googleapis.com', 'metadata': {'HELP_CENTER_LINK': 'https://developers.google.com/merchant/api/guides/compatibility/migrate-v1beta-v1', 'REASON': 'V1BETA_RAMP_DOWN'}}]}}}}`
- merchant_api_productinputs_attempts: `{'v1:10636492695': {'ok': False, 'status': 404, 'count': 0, 'error': {'raw': '<!DOCTYPE html>\n<html lang=en>\n  <meta charset=utf-8>\n  <meta name=viewport content="initial-scale=1, minimum-scale=1, width=device-width">\n  <title>Error 404 (Not Found)!!1</title>\n  <style>\n    *{margin:0;padding:0}html,code{font:15px/22px arial,sans-serif}html{background:#fff;color:#222;padding:15px}body{margin:7% auto 0;max-width:390px;min-height:180px;padding:30px 0 15px}* > body{background:url(//www.google.com/images/errors/robot.png) 100% 5px no-repeat;padding-right:205px}p{margin:11px 0 22px;overflow:hidden}ins{color:#777;text-decoration:none}a img{border:0}@media screen and (max-width:772px){body{background:none;margin-top:0;max-width:none;padding-right:0}}#logo{background:url(//www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png) no-repeat;margin-left:-5px}@media only screen and (min-resolution:192dpi){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat 0% 0%/100% 100%;-moz-border-image:url(//www.'}}, 'v1beta:10636492695': {'ok': False, 'status': 404, 'count': 0, 'error': {'raw': '<!DOCTYPE html>\n<html lang=en>\n  <meta charset=utf-8>\n  <meta name=viewport content="initial-scale=1, minimum-scale=1, width=device-width">\n  <title>Error 404 (Not Found)!!1</title>\n  <style>\n    *{margin:0;padding:0}html,code{font:15px/22px arial,sans-serif}html{background:#fff;color:#222;padding:15px}body{margin:7% auto 0;max-width:390px;min-height:180px;padding:30px 0 15px}* > body{background:url(//www.google.com/images/errors/robot.png) 100% 5px no-repeat;padding-right:205px}p{margin:11px 0 22px;overflow:hidden}ins{color:#777;text-decoration:none}a img{border:0}@media screen and (max-width:772px){body{background:none;margin-top:0;max-width:none;padding-right:0}}#logo{background:url(//www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png) no-repeat;margin-left:-5px}@media only screen and (min-resolution:192dpi){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat 0% 0%/100% 100%;-moz-border-image:url(//www.'}}}`

## Data sources — Merchant API
- `10525577766` — displayName=`lksneakers.com.br` input=`AUTOFEED` primary=`False` supplemental=`False` local=`False`
- `10636384718` — displayName=`Content API` input=`API` primary=`True` supplemental=`False` local=`False`
- `10636492695` — displayName=`Content API` input=`API` primary=`True` supplemental=`False` local=`False`

## Datafeeds — Content API legado
- Nenhum datafeed legado retornado.

## Catálogo/status carregado
- products carregados via Content API: `19652`
- productstatuses carregados via Content API: `14236`
- top issue codes: `{'price_updated': 1065, 'strikethrough_price_updated': 619, 'missing_item_attribute_for_product_type': 578, 'local_stores_lack_inventory': 23, 'restricted_gtin': 13, 'restricted_nfs_policy_violation': 4, 'image_link_internal_error': 4, 'condition_updated_from_detected': 3, 'reserved_gtin': 3, 'pause_expired': 2}`

## Veredito preliminar
- Merchant API lista mais de uma dataSource; isso pode ser normal se houver fonte primária + suplementar/local/legado, mas precisa governança clara.
- dataSource 10636492695 existe/é referenciada como fonte API usada pelos scripts aprovados de ProductInputs.

## Não executado
- Merchant/Content API writes
- fetchNow
- feed upload
- Shopify writes
- theme production publish
- campaign/customer/supplier contact
- printing secrets
