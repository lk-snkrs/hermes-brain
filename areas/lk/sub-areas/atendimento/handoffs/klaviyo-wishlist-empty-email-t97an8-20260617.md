# Klaviyo Wishlist vazio — diagnóstico e approval packet — 2026-06-17

## Contexto

Lucas reportou que o flow/e-mail com assunto semelhante a `Lucas, seus favoritos ainda estão disponíveis` está chegando vazio: imagem/produto/preço não renderizam; aparece apenas `R$` sem valor.

## Escopo executado

- Somente read-only em Klaviyo via Doppler-first (`lc-keys/prd`, profile `lk-content`).
- Nenhum write externo em Klaviyo/Shopify/Tiny/WhatsApp/e-mail.
- Secrets não impressos (`values_printed=false`).

## Evidência live

Smoke Klaviyo:
- `http_status=200`
- `status=ok`
- `values_printed=false`

Flows wishlist encontrados:

1. `T97an8` — `Swym - Wishlist Winback (Lembrete)`
   - status: `live`
   - trigger metric: `UcN9EY` / `Swym-addToWishlist`
   - action: `104217194`, status `live`
   - subject: `{{ first_name|default:"Ei" }}, seus favoritos ainda estão disponíveis`
   - template: `YwnNTz` / `Swym - Wishlist Winback`
   - este é o flow que bate com o print do Lucas.

2. `V478R8` — `Wishlist - Wishlist Reminder - Jun 12, 2026 14:42:59`
   - status: `live`
   - trigger metric: `TEqmpK` / `Swym-wishlistReminder`
   - actions: `109049843`, `109049846`, ambos live
   - templates: `SeBaPc`, `SLYX6r`
   - não bate com o assunto do print.

## Causa raiz provável confirmada

O template live `YwnNTz` do flow `T97an8` usa variáveis que **não existem** no payload atual do evento `Swym-addToWishlist`.

Template atual espera:
- `event.Brand`
- `event.Price`
- `event.ProductImageURL`
- `event.ProductTitle`
- `event.ProductURL`
- `event.VariantTitle`

Eventos recentes reais do metric `Swym-addToWishlist` trazem chaves como:
- `ProductBrand`
- `ProductPrice`
- `ImageURL`
- `ProductName`
- `ProductURL`
- `VariantInfo`
- `VariantSKU`
- `ProductId`, `VariantId`, etc.

Consequência: Klaviyo renderiza blocos vazios no HTML. Por isso o print mostra imagem/nome/preço faltando e apenas `R$` sem valor.

## Preview local da correção gerado

Arquivos locais gerados, sem write externo:
- Atual: `/opt/data/profiles/lk-ops/tmp/klaviyo_t97an8_fix_preview/YwnNTz_current.html`
- Proposto: `/opt/data/profiles/lk-ops/tmp/klaviyo_t97an8_fix_preview/YwnNTz_proposed_variable_fix.html`
- Relatório: `/opt/data/profiles/lk-ops/tmp/klaviyo_t97an8_fix_preview/report.json`

Substituições propostas:
- `event.ProductTitle` -> `event.ProductName` (2 ocorrências)
- `event.ProductImageURL` -> `event.ImageURL` (1 ocorrência)
- `event.Price` -> `event.ProductPrice` (1 ocorrência)
- `event.Brand` -> `event.ProductBrand` (1 ocorrência)
- `event.VariantTitle` -> `event.VariantInfo` (2 ocorrências)

## Approval packet

Opção recomendada: corrigir o template `YwnNTz` no Klaviyo, mantendo flow/action live e alterando apenas variáveis no HTML.

Escopo do write solicitado, se Lucas aprovar:
- Klaviyo template: `YwnNTz` (`Swym - Wishlist Winback`)
- Flow relacionado: `T97an8`
- Ação relacionada: `104217194`
- Operação: atualizar HTML do template com substituições acima
- Não alterar status do flow/action
- Não enviar teste/campanha automaticamente
- Não pausar/ativar/deletar
- Fazer readback pós-patch e, se permitido em aprovação separada, gerar test/preview renderizado com evento recente

Alternativa emergencial:
- Pausar a action/flow `T97an8` para parar novos envios vazios, depois aplicar correção com calma.
- Requer aprovação explícita separada porque altera produção/status.

## Reminder OS

- Reminder OS loop needed: yes
- Reminder OS owner: `lk-content` / Klaviyo operator
- Reminder OS next action: aguardar aprovação de Lucas para patch do template `YwnNTz` ou pausa emergencial do `T97an8`.
- Reminder OS review trigger: Lucas responder aprovando uma das opções; ou novo print/e-mail vazio do mesmo subject.
- Reminder OS evidence: Klaviyo read-only smoke `status=ok`; flow `T97an8` live; metric `Swym-addToWishlist` payload mismatch; preview local gerado.

## Segurança

- `values_printed=false`
- `external_write_performed=false`
- nenhum segredo/token impresso
- nenhum estoque/Tiny/Shopify consultado para disponibilidade
