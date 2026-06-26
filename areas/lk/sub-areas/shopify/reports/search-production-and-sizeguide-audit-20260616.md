# LK Shopify — Search Production QA + Size Guide Audit

Data: 2026-06-16
Perfil: lk-shopify
Escopo: read-only QA público + auditoria estática de Guia de Tamanhos

## Frente 1 — QA público final da busca Production

Rodada pública em `https://lksneakers.com.br/search?type=product&q=...`.

Resultado: todos os probes retornaram HTTP 200 e sem `Liquid error`.

### Queries validadas

- `mind` → `/collections/nike-mind-001` / `Nike Mind 001 e 002`
- `nike mind` → `/collections/nike-mind-001` / `Nike Mind 001 e 002`
- `mind 001` → `/collections/nike-mind-001` / `Nike Mind 001 e 002`
- `mind 002` → `/collections/nike-mind-001` / `Nike Mind 001 e 002`
- `nike` → `/collections/nike-todos-os-modelos` / `Nike`
- `vomero` → `/collections/nike-vomero-premium` / `Nike Vomero Premium`
- `vomero 5` → `/collections/nike-vomero-5` + `/collections/nike-vomero-premium`
- `204l` → `/collections/new-balance-204l`
- `9060` → `/collections/new-balance-9060`
- `530` → `/collections/new-balance-530`
- `yeezy` → `/collections/yeezy`
- `samba` → `/collections/samba`

### Interpretação

A correção Nike Mind publicada em Production está operacional no HTML público. O controle `nike` continua apontando para a coleção ampla, enquanto `mind`/`nike mind` agora priorizam a família correta.

## Frente 2 — Auditoria Size Guide por família

Auditoria estática read-only em PDPs públicos de amostra. Objetivo: verificar se a copy/tabela renderizada no HTML público bate com a regra comercial por família.

### Amostras auditadas

- Yeezy Slide: `yeezy-slide-onyx`
- Yeezy 350: `yeezy-350-v2-carbon-beluga`
- Nike Mind 001: `slide-nike-mind-001-black-chrome-preto`
- Nike Mind 002: `tenis-nike-mind-002-sail-bege`
- Jordan 1 Mid: `air-jordan-1-mid-aqua-blue-tint`
- Jordan 1 High: `tenis-air-jordan-1-high-og-shattered-backboard-laranja`
- Jordan 1 Low: `tenis-air-jordan-1-low-og-obsidian-unc-azul`

Todos os PDPs amostrados retornaram HTTP 200 e sem `Liquid error`.

### Leitura por família

#### Yeezy Slide

Status: OK na amostra.

Evidência textual:

- Modal identifica `Yeezy Slide`.
- Copy indica que o modelo veste pequeno.
- Recomenda comprar um tamanho acima.
- Grade agrupada `34/35`, `36/37`, `38/39`, `40/41`, `42/43`, `44/45` aparece no PDP.

#### Yeezy 350 / 350 V2

Status: OK na amostra.

Evidência textual:

- Modal identifica `Adidas Yeezy`.
- Copy cita especialmente `Boost 350 V2`.
- Recomenda subir meio número/meio tamanho.
- Não foi identificado conflito com a regra LK atual.

#### Nike Mind 001

Status: OK na amostra.

Evidência textual:

- Modal identifica `Nike Mind 001`.
- Copy recomenda comprar o `próximo tamanho Nike acima`.
- Não aparecem tamanhos Nike BR inválidos `38.5` ou `41.5` na área focada do guia.
- A lógica está alinhada com a regra de grade Nike válida.

#### Nike Mind 002

Status: OK na amostra.

Evidência textual:

- Modal identifica `Nike Mind 002`.
- Copy diz que o modelo masculino tem forma correta.
- Recomenda comprar tamanho habitual.
- Usa grade Nike com conversões US masculino, US feminino, EU e CM.

#### Jordan 1 Mid

Status: OK na amostra.

Evidência textual:

- Modal identifica `Jordan 1 Mid`.
- Copy recomenda comprar um tamanho inteiro acima do habitual.
- Tabela usa tamanhos inteiros: `34→35`, `35→36`, `36→37`, `37→38`, etc.
- Texto explica que Jordan 1 Mid/High não trabalham com meio ponto na grade BR.

#### Jordan 1 High

Status: OK na amostra.

Evidência textual:

- Modal identifica `Jordan 1 High`.
- Copy recomenda comprar um tamanho inteiro acima do habitual.
- A tabela focada não traz os meios pontos proibidos na recomendação Mid/High.

#### Jordan 1 Low

Status: OK na amostra.

Evidência textual:

- Modal identifica `Jordan 1 Low`.
- Copy diz que costuma vestir normal.
- Recomenda comprar tamanho habitual.
- Observação: a grade padrão pode conter meios pontos/conversões, mas isso não conflita com a regra atual porque Jordan 1 Low permanece TTS/habitual; a restrição de tabela inteira é específica para Mid/High.

## Risco / bloqueio

- Nenhum write foi feito nesta frente de Size Guide.
- A auditoria foi estática/HTML público. Para aprovação visual final de modal, o próximo nível é browser QA com clique mobile `390x844`, incluindo overlay/backdrop e screenshot.
- Não foi feita promessa de estoque/disponibilidade.

## Artefatos

- Dados consolidados: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/dual-front-qa-sizeguide-20260616/search-production-and-sizeguide-static-audit.json`
- Auditoria focada Size Guide: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/dual-front-qa-sizeguide-20260616/sizeguide-focused-audit-v2.json`

## Próximo passo recomendado

1. Não precisa mexer agora em Search Production: QA passou.
2. Não precisa abrir correção imediata em Size Guide: amostras passaram.
3. Próxima melhoria com maior potencial: browser QA visual mobile do Guia de Tamanhos em 4 PDPs críticos (`Yeezy Slide`, `Nike Mind 001`, `Jordan 1 Mid`, `Jordan 1 Low`) para validar clique, backdrop preto 70%, topo da tela coberto e ausência de overflow.
