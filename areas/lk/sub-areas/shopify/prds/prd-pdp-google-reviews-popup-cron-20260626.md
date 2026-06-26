# PRD — PDP Google Reviews Popup + atualização semanal

Status: draft para aprovação de escopo  
Owner: LK Shopify  
Data: 2026-06-26  
Superfície: Shopify PDP / Trust Bar mobile+desktop  
Risco: A2 theme + cron + Shopify metafield write recorrente

## 1. Contexto

Lucas quer que o item da Trust Bar do PDP que mostra as avaliações do Google — hoje exibido como algo próximo de `420 avaliações no Google` — vire um CTA clicável. Ao clicar, deve abrir um popup/modal com design premium LK e uma seleção das melhores avaliações do Google: as mais recentes, positivas e completas.

Também é necessário manter os dados atualizados semanalmente por cron, evitando conteúdo estático/stale.

Contexto histórico útil:

- Já existe uso de `shop.metafields.lk_google.reviews`/dados Google Reviews em superfícies da LK.
- Foi observado anteriormente que a fonte exibida podia ficar stale: tema mostrando `4.9 / 384`, enquanto cron recente indicava `4.9 / 418` em 2026-06-22.
- Portanto, este PRD deve tratar não só o modal visual, mas também a fonte de verdade e atualização semanal.

## 2. Objetivo

Aumentar confiança e prova social no PDP, transformando o número de avaliações da Trust Bar em uma experiência verificável e premium:

1. Clique em `420 avaliações no Google` abre popup LK.
2. Popup mostra avaliação agregada e lista curada automaticamente das melhores avaliações.
3. Cron semanal busca/seleciona reviews atualizadas e grava payload consumível pelo tema.
4. Tema nunca quebra se a API/cron falhar: usa último payload válido e fallback seguro.

## 3. Não objetivos

Fora do escopo deste PRD:

- Alterar preço, estoque, disponibilidade, checkout, Tiny, GMC, Klaviyo, Meta, WhatsApp ou campanhas.
- Criar reviews fake ou editar o texto de avaliações.
- Enviar mensagem para clientes.
- Mudar a nota/quantidade manualmente sem fonte Google ou payload validado.
- Fazer write direto em Production Shopify Asset API. Production deve vir por GitHub/PR/merge/readback.

## 4. Usuário e caso de uso

### Usuário

Visitante do PDP, especialmente mobile, avaliando confiança antes de comprar produto premium/sob encomenda.

### Jornada

1. Cliente vê Trust Bar no PDP.
2. Identifica `4.9 no Google` / `420 avaliações`.
3. Clica no bloco de avaliações.
4. Modal abre sem sair da página.
5. Cliente vê:
   - nota agregada;
   - total de avaliações;
   - selo `Google Reviews`;
   - 5 a 8 avaliações reais, completas e positivas;
   - link discreto para ver no Google, se disponível.
6. Cliente fecha modal e continua compra.

## 5. Requisitos funcionais

### RF1 — Trust Bar clicável

O item da Trust Bar referente ao Google Reviews deve ser botão/acessível:

- usar `<button>` ou elemento com `role="button"` apenas se necessário;
- manter visual atual da Trust Bar;
- cursor/feedback sutil no hover/focus;
- `aria-haspopup="dialog"`;
- `aria-controls="lk-google-reviews-modal"`;
- abrir modal ao clique/Enter/Espaço.

### RF2 — Modal/popup LK

O modal deve seguir design premium LK:

- overlay claro/escuro discreto;
- card central desktop e bottom-sheet/centered card mobile conforme melhor UX;
- tipografia LK (`DM Sans`, `Cormorant` se já usada no PDP);
- bordas finas, fundo off-white/white, espaçamento premium;
- estrelas douradas/sutis;
- botão fechar no topo;
- fechar por ESC, backdrop e botão;
- focus trap e retorno de foco ao botão da Trust Bar.

Conteúdo mínimo:

- título: `Avaliações no Google`;
- resumo: `4.9/5` + `420 avaliações` ou valores do payload;
- subtítulo: `Clientes reais sobre a experiência LK Sneakers`;
- lista de reviews;
- data relativa ou mês/ano quando disponível;
- link `Ver avaliações no Google` quando URL existir.

### RF3 — Seleção automática das melhores avaliações

Cron deve montar lista `featured_reviews` com 5 a 8 itens.

Critério recomendado de score:

```text
score =
  rating_score + completeness_score + recency_score + helpfulness_proxy - risk_penalties
```

Onde:

- `rating_score`: priorizar 5 estrelas, aceitar 4 estrelas se muito completa;
- `completeness_score`: texto com pelo menos 120 caracteres, ideal 180+;
- `recency_score`: preferir últimas avaliações, mas não sacrificar qualidade;
- `helpfulness_proxy`: texto menciona atendimento, autenticidade, loja, entrega, produto, experiência;
- `risk_penalties`: remover texto vazio, avaliações ofensivas, reclamações, dados pessoais, linguagem ruim ou conteúdo potencialmente sensível.

Ordenação no modal:

1. top 3 por score geral;
2. depois alternar recência e completude para parecer vivo, não artificial.

### RF4 — Fonte de dados/payload Shopify

O tema deve consumir um payload único em metafield de loja, por exemplo:

`shop.metafields.lk_google.reviews_payload`

Formato proposto:

```json
{
  "source": "google_business_profile",
  "place_url": "https://...",
  "rating": 4.9,
  "total_reviews": 420,
  "updated_at": "2026-06-26T00:00:00-03:00",
  "featured_reviews": [
    {
      "author_name": "Nome Público",
      "rating": 5,
      "relative_time_description": "há 2 semanas",
      "text": "Texto público da avaliação...",
      "review_url": "https://..."
    }
  ]
}
```

Fallbacks:

- Se `reviews_payload` existe e é válido, usar ele.
- Se `reviews_payload` falhar, usar metafield legado `lk_google.reviews` para nota/contagem e ocultar lista detalhada.
- Se não houver nenhum dado, manter Trust Bar sem abrir modal ou abrir modal com mensagem curta: `Avaliações temporariamente indisponíveis`.

### RF5 — Cron semanal

Criar/ajustar cron semanal para:

1. buscar reviews no Google Business Profile ou fonte Google autorizada;
2. normalizar payload;
3. selecionar reviews por score;
4. validar schema JSON;
5. gravar metafield Shopify `lk_google.reviews_payload`;
6. registrar receipt local/Brain;
7. silent-OK em sucesso;
8. alertar Lucas apenas se houver falha acionável por mais de 1 ciclo ou se payload ficar stale acima do limite.

Cadência recomendada:

- 1x por semana, segunda-feira 07:30 BRT;
- reprocessar no máximo 1 vez em caso de falha transitória;
- stale threshold: alertar se `updated_at` > 10 dias.

### RF6 — Segurança e privacidade

- Não imprimir tokens Google/Shopify.
- Usar Doppler `lc-keys/prd` e helper Hermes.
- Não salvar secrets no Brain/receipts/logs.
- Não exibir dados pessoais além do nome público já exibido pelo Google.
- Truncar texto muito longo no modal, mantendo expansão visual elegante se necessário.

## 6. Requisitos não funcionais

- Modal não deve aumentar CLS perceptível.
- JS deve ser pequeno e escopado ao PDP.
- Sem dependência de chamada client-side ao Google; tudo server/cron/metafield.
- A página deve funcionar se JS falhar.
- Acessibilidade: teclado, ESC, foco, labels, contraste.
- Mobile-first: popup precisa caber em viewport pequena e rolar internamente.

## 7. Arquitetura recomendada

### Camada A — Dados

Cron semanal em Hermes/infra local:

`google_reviews_weekly_sync`

Responsabilidades:

- autenticar com Google via Doppler/OAuth/service config já aprovado;
- buscar reviews da LK;
- montar `reviews_payload`;
- fazer Shopify metafield write aprovado;
- readback do metafield;
- receipt.

### Camada B — Shopify/theme

Tema no GitHub:

- `sections/lk-pdp.liquid`: botão Trust Bar + modal container + Liquid lendo metafield;
- opcional `assets/lk-google-reviews-modal.js` se separar JS for melhor;
- opcional `snippets/lk-google-reviews-modal.liquid` para manter PDP limpo.

Recomendação: criar snippet separado se o bloco Liquid ficar maior que ~80 linhas.

### Camada C — QA

- DEV theme primeiro;
- PR GitHub para `production`;
- readback Shopify DEV e Production;
- QA público em PDP com Trust Bar;
- teste teclado/mobile.

## 8. Estados de UI

### Estado completo

- nota + total;
- lista 5–8 avaliações;
- link Google.

### Estado payload válido sem reviews detalhadas

- nota + total;
- mensagem: `Confira nossas avaliações públicas no Google.`;
- link Google.

### Estado stale

- storefront ainda usa último payload válido;
- cron alerta internamente se stale > 10 dias;
- não mostrar erro técnico ao cliente.

### Estado sem dados

- Trust Bar mantém texto estático se já existir;
- clique pode ser desativado para não abrir modal vazio.

## 9. Critérios de aceite

### Theme/UX

- [ ] Clicar no bloco de Google Reviews da Trust Bar abre modal.
- [ ] Modal segue visual LK e não parece widget externo genérico.
- [ ] Mobile 390px funciona sem cortar conteúdo.
- [ ] ESC/backdrop/fechar funcionam.
- [ ] Foco retorna ao botão após fechar.
- [ ] Sem alteração em outros blocos da Trust Bar.

### Dados

- [ ] Payload JSON válido em metafield Shopify.
- [ ] Mostra rating e total vindos do payload.
- [ ] Mostra 5–8 reviews filtradas.
- [ ] Não mostra reviews vazias/ofensivas/sensíveis.
- [ ] Se payload ausente, PDP não quebra.

### Cron

- [ ] Cron semanal roda silent-OK em sucesso.
- [ ] Readback confirma metafield atualizado.
- [ ] Falha não apaga payload anterior.
- [ ] Alerta só se falha acionável/stale > 10 dias.
- [ ] Logs/receipts com `values_printed=false` para secrets.

### Deploy

- [ ] DEV/unpublished primeiro.
- [ ] PR GitHub para `production`.
- [ ] Shopify Production readback separado de GitHub readback.
- [ ] Receipt Memory OS após execução.

## 10. Riscos e mitigação

| Risco | Impacto | Mitigação |
|---|---:|---|
| API Google não retorna texto suficiente | Modal pobre | fallback com menos reviews + link Google |
| Metafield stale | Perda de confiança | cron weekly + stale alert >10 dias |
| Tema quebra se JSON inválido | PDP impactado | validação schema antes do write + fallback Liquid |
| Modal pesado no mobile | CRO negativo | JS escopado, CSS leve, QA 390px |
| Shell/secret leak | Segurança | Doppler-first, logs sanitizados |
| Write recorrente Shopify sem aprovação | Governança | approval packet específico para cron + metafield write |

## 11. Plano de implementação

### Fase 0 — Descoberta read-only

- Verificar fonte atual do número `420 avaliações` na Trust Bar.
- Verificar metafields existentes `lk_google.*`.
- Verificar se já existe cron Google Reviews e qual payload ele produz.
- Verificar credenciais Google disponíveis no Doppler por nome, sem imprimir valores.

### Fase 1 — PRD aprovado → design técnico

- Definir nome final do metafield.
- Definir source Google final.
- Definir número de reviews exibidas: recomendado 6.
- Definir se modal fica inline no `lk-pdp.liquid` ou snippet.

### Fase 2 — Theme DEV

- Implementar botão acessível na Trust Bar.
- Implementar modal LK.
- Ler payload de metafield com fallback seguro.
- Upload DEV após aprovação explícita.
- QA DEV mobile/desktop.

### Fase 3 — Cron/metafield

- Implementar/ajustar cron semanal.
- Dry-run com payload local.
- Write em Shopify metafield somente após aprovação explícita.
- Readback.

### Fase 4 — Production

- PR para `production`.
- Merge aprovado.
- Readback GitHub + Shopify Production.
- QA público.
- Receipt.

## 12. Rollback

### Rollback theme

- Reverter PR/commit do modal.
- Trust Bar volta a comportamento anterior sem popup.
- Nenhum impacto em produto/preço/estoque.

### Rollback dados

- Desativar cron.
- Manter último payload válido ou restaurar backup do metafield anterior.
- Se necessário, remover clique do modal e manter Trust Bar estática.

## 13. Aprovações necessárias

Este PRD ainda não autoriza execução.

Para implementar, Lucas precisa aprovar separadamente:

1. **Descoberta read-only** — verificar tema/metafields/cron atual.
2. **DEV theme write** — subir modal no DEV/unpublished.
3. **Shopify metafield write + cron semanal** — escrever payload e agendar rotina.
4. **Production merge** — PR/merge para `production` após QA DEV.

Frase sugerida para próximo passo seguro:

> Aprovo descoberta read-only do PDP Google Reviews popup + fonte/cron atual.

## 14. Descoberta read-only aprovada — 2026-06-26

Aprovação recebida: Lucas respondeu `Aprovo` ao próximo passo seguro de descoberta read-only. Nenhum write externo foi executado nesta fase.

### 14.1 Estado atual do tema Production

Readback Shopify Production theme `155065417950`, asset `sections/lk-pdp.liquid`:

- SHA12: `68cbf5f7b498`.
- A Trust Bar do PDP já usa `shop.metafields.lk_google.reviews.value`.
- O item Google já é um `<button>` com `id="lk-reviews-trigger"`.
- O label atual é:

```liquid
Google<br>{{ reviews_json.rating | default: "4.9" }} · {{ reviews_json.count | default: 376 }} avaliações
```

- Já existe markup/CSS de `lk-reviews-modal` no próprio `lk-pdp.liquid`.
- Porém o JS atual não abre esse modal LK. O handler existente só trata o modal Judge.me (`pdp-reviews-modal`) e um fallback de scroll; não há handler dedicado para `#lk-reviews-modal`, `#lk-reviews-close` e backdrop.

Interpretação: parte da feature já foi iniciada no tema, mas está incompleta: falta ligar o botão da Trust Bar ao modal LK e popular reviews no payload.

### 14.2 Estado atual do metafield Shopify

Read-only GraphQL Admin em namespace `lk_google`:

- Metafield existente: `shop.metafields.lk_google.reviews`.
- Tipo: `json`.
- `updatedAt`: `2026-06-25T16:45:02Z`.
- Payload atual tem chaves:
  - `checked_at`
  - `count`
  - `place_id`
  - `rating`
  - `source`
  - `updated_at`
  - `userRatingCount`
- Valor atual sanitizado: rating `4.9`, count `420`.
- Não existe `featured_reviews` nem `reviews` utilizável no payload atual.

Interpretação: o tema tenta iterar `reviews_json.reviews`, mas o metafield atual só tem nota/contagem. Por isso a lista de avaliações fica vazia.

### 14.3 Estado atual do cron

Cron profile-local existente:

- Job: `LK Google reviews checkout monitor`.
- Script: `lk_google_reviews_monitor.sh` → `lk_google_reviews_monitor.py`.
- Agenda: `0 13 * * 1` (semanal, segunda, UTC; equivale ~10:00 BRT sem DST).
- Delivery: `local`.
- Último status registrado: `ok`.
- Estado atual: rating `4.9`, `userRatingCount: 420`, `last_status: ok_same`.
- Último artifact: `/opt/data/profiles/lk-shopify/cron/output/lk-google-reviews-monitor/2026-06-25_16-45-43.json`.

O script atual:

- usa Google Places API para buscar `rating`, `userRatingCount`, `googleMapsUri`;
- sincroniza apenas `shop.metafields.lk_google.reviews` com rating/count/place_id;
- não busca nem ranqueia textos de reviews;
- já segue contrato `values_printed=false` e silent-OK.

Interpretação: devemos reaproveitar este cron, não criar outro do zero, mas expandir seu payload e validação.

### 14.4 Credenciais e fonte Google

Verificação Doppler runtime com `hermes_doppler.py run --profile lk-shopify`:

- `GOOGLE_API_KEY`: presente.
- `GOOGLE_PLACES_API_KEY`: presente.
- `SHOPIFY_ACCESS_TOKEN`: presente.
- `SHOPIFY_STORE`: presente.
- `SHOPIFY_STORE_URL`: presente.
- `SHOPIFY_ADMIN_TOKEN`: presente.
- `SHOPIFY_API_TOKEN`: presente.
- `LK_GOOGLE_PLACE_ID`: ausente no runtime, mas `place_id` existe no metafield/state.
- `DOPPLER_TOKEN`: ausente no child env, como esperado.
- `values_printed=false`.

Probe read-only Google Places com field mask `reviews`:

- Google retornou rating `4.9`, total `420`.
- Retornou 5 reviews.
- Todos os 5 reviews retornados têm rating 5.
- Comprimentos de texto retornados: `47`, `155`, `22`, `366`, `373` caracteres.
- Todos têm metadata de tempo/publicação.

Interpretação importante: Google Places parece suficiente para um modal com até 5 avaliações públicas retornadas pela API. Se Lucas quiser 6–8 ou “últimas melhores” em profundidade, precisaremos validar uma fonte mais rica (ex.: Google Business Profile API com permissões adequadas ou DataForSEO Business Data Google Reviews). A versão mínima segura deve assumir 5 reviews.

## 15. Design técnico recomendado pós-descoberta

### Opção recomendada — expandir o que já existe

1. Reaproveitar `shop.metafields.lk_google.reviews` em vez de criar novo metafield inicialmente.
2. Expandir payload com:
   - `reviews`: lista filtrada de até 5 reviews retornadas pela Google Places API;
   - `googleMapsUri`;
   - `reviews_updated_at`;
   - `schema_version: 2`.
3. Ajustar o Liquid para aceitar `reviews_json.reviews` e fallback se lista vazia.
4. Adicionar JS dedicado para `#lk-reviews-trigger` abrir `#lk-reviews-modal` com ESC/backdrop/close/focus return.
5. Atualizar cron existente `lk_google_reviews_monitor.py`, mantendo silent-OK e write somente no metafield aprovado.

Vantagem: menor superfície, aproveita cron/metafield já existentes, reduz risco de duplicação.

### Alternativa — novo metafield `reviews_payload`

Criar `shop.metafields.lk_google.reviews_payload` e deixar `reviews` legado intacto.

Vantagem: separa legado de payload novo.  
Desvantagem: exige mudar tema para duas fontes e manter dois payloads, mais chance de drift.

Recomendação: só usar esta alternativa se quisermos preservar `reviews` estritamente como rating/count.

## 16. Próximo approval packet

A descoberta read-only está concluída. Para executar a implementação mínima em DEV, escopo sugerido:

1. Theme DEV/unpublished:
   - ligar `#lk-reviews-trigger` ao `#lk-reviews-modal`;
   - melhorar fallback de lista vazia;
   - preservar design LK existente;
   - não alterar outros itens da Trust Bar.
2. Cron/metafield DEV/produção operacional:
   - expandir `lk_google.reviews` com até 5 reviews públicas retornadas pela API;
   - scoring simples: rating 5 + maior texto primeiro + metadata de tempo;
   - readback Shopify metafield;
   - fallback: se API falhar, manter payload anterior e não apagar reviews.

Aprovação necessária para próximo passo:

> Aprovo DEV theme + expansão do cron/metafield `lk_google.reviews` para o popup Google Reviews, sem Production merge ainda.

## 17. Nova aprovação e bloqueio de fonte — 2026-06-26

Lucas aprovou a implementação e especificou: `Adicionar 10 reviews no modal`.

### 17.1 Conflito descoberto antes do write

A exigência de 10 reviews conflita com a fonte atual validada:

- Google Places API atual retorna no máximo 5 reviews para Place Details/Places API.
- Probe real da LK retornou exatamente 5 reviews.
- Doppler/profile não apresentou credencial dedicada para fontes alternativas como Google Business Profile Reviews API, Outscraper, SerpApi ou DataForSEO business reviews.
- Portanto, executar agora usando apenas a fonte atual entregaria no máximo 5 reviews, não os 10 aprovados.

### 17.2 Status de segurança

Nenhum novo write externo foi executado após essa aprovação porque o requisito material (`10 reviews`) não é cumprível com a fonte atual sem escolher outra fonte ou aceitar fallback.

### 17.3 Caminhos possíveis

**Opção A — implementar agora com fonte atual, preparada para até 10**

- Modal e schema aceitam até 10 reviews.
- Cron popula as 5 reviews disponíveis via Google Places.
- Quando uma fonte com 10 reviews existir, o mesmo payload passa a exibir 10.
- Mais rápido, mas não cumpre visualmente “10 reviews” agora.

**Opção B — investigar/aprovar fonte alternativa para 10 reviews antes de DEV**

- Validar Google Business Profile API, DataForSEO Business Data Google Reviews, Outscraper ou outra fonte aprovada.
- Depois implementar modal com 10 reais.
- Cumpre requisito, mas exige credencial/fonte nova e potencial custo/integração.

**Opção C — usar 5 reais + CTA para Google agora**

- Mostrar as 5 reais retornadas pela API oficial.
- CTA `Ver todas as avaliações no Google` cobre o restante.
- Menor risco de compliance e menor prazo.

### 17.4 Decisão registrada

Lucas escolheu: `Implementar 5 reais + CTA Google agora`.

## 18. Execução aprovada — 5 reviews reais + CTA Google — 2026-06-26

Escopo executado:

- Sem merge Production theme.
- Metafield Shopify `shop.metafields.lk_google.reviews` expandido com reviews reais retornadas pelo Google Places.
- DEV/unpublished theme atualizado para abrir modal Google Reviews pelo botão da Trust Bar.

### 18.1 Cron/metafield

Script atualizado:

- `/opt/data/profiles/lk-shopify/scripts/lk_google_reviews_monitor.py`

Mudanças:

- Field mask Google Places agora inclui `reviews`.
- Normaliza reviews públicas com nome, inicial, rating, data relativa/publicação e texto.
- Seleciona até 5 reviews reais, ordenando por rating e completude do texto.
- Mantém `schema_version: 2`, `googleMapsUri`, `reviews_source_limit: 5`, `reviews_updated_at`.
- Se API falhar no futuro, script mantém o último payload válido conforme contrato anterior.

Execução aprovada do cron:

- rc `0`.
- Shopify metafield sync: `ok_updated`.
- Rating/count preservados: `4.9` / `420`.
- `reviews_count`: `5`.
- `values_printed=false`.
- Artifact: `/opt/data/profiles/lk-shopify/cron/output/lk-google-reviews-monitor/2026-06-26_08-50-06.json`.

Readback metafield sanitizado:

- `updatedAt`: `2026-06-26T08:50:06Z`.
- value bytes: `3026`.
- JSON keys agora incluem `reviews`, `googleMapsUri`, `reviews_source_limit`, `reviews_updated_at`, `schema_version`.

### 18.2 DEV theme

Theme DEV/unpublished:

- Theme ID: `155065450718`.
- Asset: `sections/lk-pdp.liquid`.
- HTTP PUT: `200`.
- Readback: `200`.
- Antes SHA12: `68cbf5f7b498`.
- Target/readback SHA12: `b5e6d0d63935`.

Checks de readback:

- `openLkGoogleReviewsModal`: presente.
- Modal preparado para `limit: 10`: presente.
- CTA Google dinâmico via `reviews_json.googleMapsUri`: presente.
- fallback de lista vazia: presente.
- botão `id="lk-reviews-trigger"`: presente.

### 18.3 QA público DEV preview

URL testada com `preview_theme_id=155065450718` em PDP com encomenda:

- HTTP `200`.
- `#lk-reviews-trigger`: presente.
- `#lk-reviews-modal`: presente.
- JS `openLkGoogleReviewsModal`: presente.
- Cards renderizados: `5`.
- CTA `Ver todas as avaliações no Google`: presente.
- Fallback vazio: ausente, porque reviews reais renderizaram.
- Trust Bar mostra `4.9 · 420 avaliações`.

### 18.4 Rollback

Theme DEV:

- Restaurar `/opt/data/profiles/lk-shopify/workdirs/pdp-google-reviews-modal-20260626/dev_before_sections__lk-pdp.liquid` no DEV theme `155065450718`.

Cron/script:

- Restaurar `/opt/data/profiles/lk-shopify/workdirs/pdp-google-reviews-modal-20260626/backups/lk_google_reviews_monitor.py.before`.

Metafield:

- Restaurar formato anterior de `shop.metafields.lk_google.reviews` com apenas rating/count/place_id, se Lucas quiser remover reviews do payload. Backup de estado antes: `/opt/data/profiles/lk-shopify/workdirs/pdp-google-reviews-modal-20260626/backups/lk_google_reviews_state.json.before`.

### 18.5 Correção DEV pós-feedback Lucas — Liquid errors + clique do modal

Lucas testou o link DEV e reportou:

- Liquid error por snippet ausente `snippets/lk-variante-tokyo-taekwondo-20260624.liquid`.
- Liquid syntax error no snippet `snippets/lk-variante-bestsellers-1-3-20260624.liquid` por aspas internas em títulos.
- Clique na Trust Bar Google não abria o popup.

Root cause confirmado:

1. DEV theme chamava snippet `lk-variante-tokyo-taekwondo-20260624`, mas o asset não existia no DEV.
2. O snippet `lk-variante-bestsellers-1-3-20260624` tinha strings Liquid delimitadas por aspas duplas contendo apelidos também em aspas duplas (`"Black Cat"`, `"Core Black Wonder"`), quebrando parse.
3. O JS do modal Google rodava antes do markup `#lk-reviews-modal` existir no DOM; por isso o binding não era aplicado.

Correções executadas em DEV:

- Upload DEV do snippet ausente `snippets/lk-variante-tokyo-taekwondo-20260624.liquid`.
- Correção e upload DEV do snippet `snippets/lk-variante-bestsellers-1-3-20260624.liquid`, removendo aspas internas problemáticas nos títulos.
- Reupload DEV de `sections/lk-pdp.liquid` com `initLkGoogleReviewsModal()` rodando imediatamente + `DOMContentLoaded` + `load`.

Readbacks:

- Tokyo snippet: PUT `200`, readback SHA12 `8f8fe2d00b18`.
- Bestsellers snippet: PUT `200`, readback SHA12 `6289568b7f94` após repoll.
- PDP section DEV: PUT `200`, readback SHA12 `073276393bfe`.

Verificação pós-correção:

- DEV preview HTTP `200`.
- Liquid errors: `0`.
- `#lk-reviews-trigger`: presente.
- `#lk-reviews-modal`: presente.
- `initLkGoogleReviewsModal`: presente.
- Reviews renderizadas: `5`.
- CTA Google presente.
- Browser headless/CDP: antes do clique modal fechado; depois do clique `open=true`, `display=block`, `bodyOverflow=hidden`, sem exceptions JS.

### 18.6 Feedback Lucas — reviews antigas e fonte Judge.me

Lucas observou que as 5 avaliações retornadas pelo Google Places estavam antigas (~6 meses) e apontou que o Judge.me também contém avaliações do Google.

Descoberta read-only adicional:

- Judge.me está ativo no storefront e contém fonte `google-business`.
- API Judge.me read-only funcionou com shop domain `lk-sneakerss.myshopify.com` usando credencial Doppler; `values_printed=false`.
- Em `per_page=50`, Judge.me retornou 43 reviews `google-business`.
- Em `per_page=100`, havia 61 reviews `google-business` nos primeiros 100 resultados.
- Existem pelo menos 28 reviews elegíveis com:
  - `source = google-business`;
  - rating `5`;
  - texto com pelo menos 20 caracteres;
  - `published=true`;
  - `hidden=false`.
- Datas das primeiras reviews elegíveis incluem:
  - `2026-06-24`;
  - `2026-06-23`;
  - `2026-06-20`;
  - `2026-06-09`;
  - `2026-06-08`;
  - `2026-06-01`;
  - `2026-05-16`;
  - `2026-05-13`;
  - `2026-05-05`.

Interpretação: Judge.me é uma fonte melhor para o modal do que Google Places quando o objetivo é recência e volume. Google Places deve continuar como fonte de rating/count/place link, enquanto Judge.me pode alimentar os textos do modal.

Caveat operacional:

- `JUDGEME_API_TOKEN`/`JUDGEME_PRIVATE_TOKEN` aparecem no Doppler genérico, mas não apareceram no runtime com `--profile lk-shopify` durante a primeira tentativa. Antes de transformar isso em cron permanente profile-local, validar/injetar o acesso via helper/profile de forma Doppler-first sem copiar secrets.

Approval recebido e executado em DEV/metafield/cron:

> Lucas aprovou trocar a fonte dos textos do popup Google Reviews para Judge.me `google-business`, mantendo rating/count do Google Places, em DEV/metafield/cron, sem Production merge.

Execução 2026-06-26:

- Patch em `/opt/data/profiles/lk-shopify/scripts/lk_google_reviews_monitor.py`.
- Google Places permanece fonte de `rating`, `count/userRatingCount`, `place_id` e `googleMapsUri`.
- Judge.me `source=google-business` passa a alimentar os textos do modal.
- Filtros aplicados: `published=true`, `hidden=false`, `rating=5`, texto mínimo 20 caracteres.
- Schema do metafield `shop.metafields.lk_google.reviews` atualizado para `schema_version=3`.
- `source=google_places+judgeme_google_business` e `reviews_source=judgeme_google_business`.
- Reviews no payload: `10`.
- Datas recentes verificadas no payload/render: `24 jun. 2026`, `23 jun. 2026`, `20 jun. 2026`, `9 jun. 2026`, `8 jun. 2026`.
- `rating=4.9` e `count=420` preservados.
- Wrapper `lk_google_reviews_monitor.sh` ajustado para Doppler canonical run porque o profile-scoped run não injetava Judge.me; sem copiar/imprimir secrets.

Verificação pós-execução:

- Shopify metafield readback: `schema_version=3`, `reviews_source=judgeme_google_business`, `reviews_count=10`, `values_printed=false`.
- DEV preview HTTP `200`.
- Liquid errors: `0`.
- Modal renderiza `10` cards.
- Datas recentes aparecem no HTML DEV.
- Texto relativo antigo `6 meses atrás` não aparece no modal DEV.
- Browser/CDP: clique no Google Trust Bar abre modal (`display=block`, `bodyOverflow=hidden`) e JS exceptions `0`.

Receipt: `areas/lk/sub-areas/shopify/receipts/pdp-google-reviews-judgeme-source-dev-metafield-cron-20260626.md`.

### 18.7 Próxima decisão

Production merge aprovado e executado em 2026-06-26:

- PR GitHub: `#107` — `https://github.com/lk-snkrs/lk-new-theme/pull/107`.
- Base: `production`.
- Arquivo único: `sections/lk-pdp.liquid`.
- Merge commit: `6f722440772ec0d57b3901251c45819b2b54823c`.
- GitHub production content SHA: `755d7427f21205aaded759e0c30498ef9f3830e3`.
- Shopify Production Theme `155065417950` readback HTTP `200`, SHA12 `6485ef6cd984`.
- Checks readback: `initLkGoogleReviewsModal`, `limit: 10`, `reviews_json.googleMapsUri` presentes; `Curadoria LK` count preservado em `21`.
- QA público no PDP Saint George: HTTP `200`, Liquid errors `0`, trigger/modal presentes, 10 cards, datas recentes de Judge.me renderizadas, clique na Trust Bar Google abre modal, JS exceptions `0`.
- Fora do escopo: Curadoria LK bonés ALD não entrou em Production neste PR.

Rollback: reverter PR `#107` / merge commit `6f722440772ec0d57b3901251c45819b2b54823c` no GitHub `production` e aguardar sync Shopify.

Receipt: `areas/lk/sub-areas/shopify/receipts/pdp-google-reviews-modal-production-merge-20260626.md`.
