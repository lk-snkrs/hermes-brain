# LKGOC Gold Source — New Balance 204L Hero/Guide

Última atualização: 2026-06-08T20:45Z  
Dono: `[LK] Otimização de Coleções` / `lk-collection-optimizer`  
Status: **Gold Source visual, editorial e operacional do LKGOC**  
Aprovação Lucas: “Agora ficou ótimo… perfeito… para trabalhar como padrão gold.”

---

## 1. Resumo executivo

O estado atual da coleção **New Balance 204L** no tema `lk-new-theme/dev` é a referência canônica para futuras otimizações LKGOC.

Este padrão deve ser usado como base para:

- hero editorial de coleção;
- collage visual no topo;
- Guia LK pós-grid;
- FAQ/schema da coleção;
- QA visual desktop/mobile;
- fluxo DEV → QA → aprovação Lucas → produção.

**Regra central:** não reinventar layout. Replicar o 204L e adaptar somente conteúdo, imagens, links, produtos, FAQ/schema e nuances comerciais da coleção alvo.

---

## 2. Identificação técnica do ambiente

- Loja: `lk-sneakerss.myshopify.com`
- Tema referência: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role operacional: `unpublished`
- Preview DEV: `https://lk-sneakerss.myshopify.com/collections/new-balance-204l?preview_theme_id=155065450718`
- Coleção referência: `/collections/new-balance-204l`
- Arquivo principal do bloco: `snippets/lk-goc-collection.liquid`
- Arquivo de overrides tardios/runtimes: `layout/theme.liquid`
- Produção: **não alterada** neste ciclo.

### Observação sobre preview

Em algumas validações headless/públicas, o Shopify removeu ou ignorou `preview_theme_id` sem sessão/admin ativa. Nesses casos, a validação visual deve ser feita:

1. logado/admin;
2. pelo editor do tema;
3. ou por sessão que realmente sirva o `lk-new-theme/dev`.

A validação remota dos assets foi feita por `shopify theme pull` após os pushes.

---

## 3. Escopo do Gold Source

Este documento cobre o padrão LKGOC de **coleção/hero/guia**, não uma auditoria Growth completa dos 18 tópicos.

Inclui:

- estrutura de hero;
- comportamento do collage;
- tipografia editorial;
- imagem principal;
- comportamento desktop/mobile;
- regras de replicação;
- QA mínimo;
- rollback;
- receipts/evidências.

Não inclui como decision-grade:

- GA4;
- GSC;
- GMC;
- campanhas;
- receita/conversão;
- priorização comercial ampla.

Esses itens continuam sendo escopo Growth quando a pergunta for performance/SEO/receita.

---

## 4. Estrutura canônica do Hero 204L

### 4.1 Section root

Classe/identificador canônico:

```liquid
<section class="lk-goc-coll-preview lk-goc-coll-preview--204l lk-204l-coll-preview" aria-label="Contexto editorial New Balance 204L">
```

Regras:

- manter `aria-label` específico da coleção para escopo fino de CSS/JS;
- usar `lk-goc-*` como namespace preferencial;
- manter aliases legados `lk-204l-*` enquanto existirem dependências do tema;
- não remover aliases sem QA completo em todas as coleções que usam o padrão.

### 4.2 Copy/editorial

Estrutura:

```liquid
<div class="lk-goc-copy lk-204l-copy">
  <p class="lk-goc-kicker">Curadoria LK</p>
  <h2 class="lk-collection-v2__headline">Perfil baixo, leitura fashion.</h2>
  <p>{{ lk_204l_desc }}</p>
  <button class="lk-goc-read-more lk-204l-read-more" type="button">Ler mais</button>
</div>
```

Regras editoriais:

- tom premium, minimalista, humano e comercial;
- não usar “pronta entrega”, “estoque” ou taxonomia operacional como argumento público;
- se necessário, disponibilidade/prazo ficam para atendimento/chat;
- curadoria, autenticidade, proporção, styling e atendimento humano são os pilares de linguagem;
- texto deve ser citável por AI Search, mas sem soar genérico/SEO stuffing.

Copy atual de referência:

> O New Balance 204L traduz a busca pelo tênis slim com leitura de moda: uma silhueta baixa, leve e elegante, com referências de corrida retrô e acabamento em camurça e mesh. Na LK Sneakers, a curadoria prioriza colorways desejadas como Timberwolf, Mushroom, Silver Metallic e Black Magnet para quem quer um par discreto, proporcional e fácil de usar com denim amplo, alfaiataria casual e peças minimalistas. A escolha ideal passa por cor, composição e intenção de uso — a equipe LK ajuda a comparar os pares e encontrar a melhor opção com atendimento humano.

### 4.3 Collage visual

Estrutura atual:

```liquid
<div class="lk-goc-collage lk-204l-collage" aria-label="Curadoria visual New Balance 204L">
  <button class="lk-goc-card lk-goc-card--large lk-204l-card lk-204l-card--large" ...>
    <img ... alt="Rosalía usando New Balance 204L em campanha editorial">
    <em class="lk-goc-open-photo lk-204l-open-photo">Ler mais <b>↘</b></em>
    <span>Rosalía · campanha 204L</span>
  </button>
  <button class="lk-goc-card lk-204l-card" ...>...</button>
  <button class="lk-goc-card lk-204l-card" ...>...</button>
</div>
```

Regras:

- 1 card principal grande;
- 2 cards complementares;
- imagem principal deve ter leitura editorial forte;
- labels devem ser discretos e úteis;
- o card principal precisa preservar corpo/silhueta, sem corte central ruim;
- se a imagem tiver pessoa/modelo, preferir alinhamento que preserve styling e proporção.

---

## 5. Padrão visual desktop

### 5.1 Alinhamento do topo

Regra gold:

- o topo do collage editorial deve começar na mesma altura real do `.coll-banner__title`;
- não usar chute fixo quando o tema tiver variação de banner/breadcrumb;
- runtime escopado mede `getBoundingClientRect().top` do título e do collage e ajusta `translateY()`.

Implementação atual em `layout/theme.liquid`:

```html
<script id="lk-goc-204l-desktop-collage-title-top-align-20260608">
```

Comportamento:

- roda apenas se existir o bloco `Contexto editorial New Balance 204L`;
- roda apenas em desktop `min-width: 990px`;
- em mobile remove inline `transform` e `margin-bottom`;
- recalcula em:
  - `DOMContentLoaded`;
  - `load`;
  - delays pós-render: 120ms, 450ms, 1000ms;
  - `resize`;
  - `shopify:section:load`.

### 5.2 Crumbs/breadcrumbs

Problema encontrado:

- `.coll-banner__crumbs` aparecia como faixa/linha na zona visual do collage;
- isso cortava ou sujava o topo da imagem principal.

Correção gold:

```css
html body.template-collection:has(.lk-goc-coll-preview[aria-label="Contexto editorial New Balance 204L"]) .coll-banner__crumbs{
  display:none!important;
  visibility:hidden!important;
  height:0!important;
  margin:0!important;
  padding:0!important;
  overflow:hidden!important;
}
```

Também foi removido o `border-bottom` do `.coll-banner` no contexto 204L.

### 5.3 Pull vertical inicial

Baseline CSS tardio:

```css
transform:translateY(-18px)!important;
margin-bottom:-18px!important;
```

Esse valor não é o mecanismo final de precisão. Ele é o fallback/base antes do runtime medir e ajustar exatamente pelo topo do título.

---

## 6. Imagem principal Rosalía

### 6.1 Problema corrigido

A imagem principal estava alinhada pelo centro/miolo e não pelo bottom, o que prejudicava a leitura da modelo/silhueta.

### 6.2 Regra gold

```css
object-position:center bottom!important;
```

Aplicada em dois pontos para vencer overrides globais/tardios:

1. `snippets/lk-goc-collection.liquid`:

```html
<style id="lk-goc-204l-font-tune-20260608T193945Z">
```

2. `layout/theme.liquid`:

```html
<style id="lk-goc-204l-crumbs-image-overlap-fix-20260608">
```

Motivo do reforço no `theme.liquid`:

- havia override tardio global no tema aplicando `object-position:center 24%` para `.lk-204l-card--large img`;
- como esse CSS vinha depois do snippet em algumas cascatas, o ajuste bottom precisava existir no final do documento.

---

## 7. Tipografia gold do Hero

Bloco técnico:

```html
<style id="lk-goc-204l-font-tune-20260608T193945Z">
```

### 7.1 Kicker

Elemento:

```html
<p class="lk-goc-kicker">Curadoria LK</p>
```

Valor gold desktop:

```css
font-size:18px!important;
line-height:1.16!important;
```

Objetivo:

- dar presença editorial ao selo “Curadoria LK”;
- manter leitura premium, sem ficar promocional.

### 7.2 Headline

Elemento:

```html
<h2 class="lk-collection-v2__headline">Perfil baixo, leitura fashion.</h2>
```

Valor gold desktop:

```css
font-size:29px!important;
line-height:1.01!important;
```

Objetivo:

- headline leve, premium e proporcional;
- evitar competir com título da coleção no banner;
- manter Cormorant/estética editorial.

---

## 8. Mobile gold

Regras consolidadas:

- mobile não deve herdar transform desktop;
- no runtime de alinhamento, se viewport `< 990px`, remover inline `transform` e `margin-bottom` do collage;
- preservar comportamento aprovado de mobile:
  - produto/hero com leitura limpa;
  - “Ler mais” visível/controlado;
  - cards complementares controlados no estado aberto;
  - sem overflow horizontal;
  - sem collage invadindo título/banner.

Referência técnica existente:

```html
<style id="lk-goc-204l-mobile-polish-20260608">
```

---

## 9. Guia LK / pós-grid

O 204L também é referência de guia, mas o ciclo documentado aqui foi majoritariamente hero/collage.

Regras para Guia LK:

- usar seção após grid/produtos conforme padrão LKGOC;
- manter tom editorial e consultivo;
- FAQ único — evitar FAQ duplicado do tema;
- FAQ/schema deve responder dúvidas reais da coleção;
- conteúdo precisa ser citável e legível para AI Search;
- sem promessas de disponibilidade, estoque ou prazo;
- CTA deve levar para coleção/produtos/atendimento humano conforme contexto.

Quando replicar para nova coleção, validar:

- H2 do guia;
- cards/benefícios;
- FAQ visível;
- JSON-LD/FAQ schema, se aplicado;
- links internos;
- ausência de duplicidade de FAQ.

---

## 10. Arquivos e blocos técnicos atuais

### 10.1 `snippets/lk-goc-collection.liquid`

Bloco 204L:

- case/handle: `new-balance-204l`
- section aria: `Contexto editorial New Balance 204L`
- collage aria: `Curadoria visual New Balance 204L`
- imagem principal: Rosalía campanha 204L
- ajuste de fonte/bottom:

```html
<style id="lk-goc-204l-font-tune-20260608T193945Z">
```

Inclui:

```css
.lk-goc-kicker { font-size:18px; line-height:1.16; }
.lk-collection-v2__headline { font-size:29px; line-height:1.01; }
.lk-goc-card--large img, .lk-204l-card--large img { object-position:center bottom; }
```

### 10.2 `layout/theme.liquid`

Bloco anti-overlap:

```html
<style id="lk-goc-204l-crumbs-image-overlap-fix-20260608">
```

Inclui:

- hide `.coll-banner__crumbs`;
- remove border do `.coll-banner`;
- fallback desktop `translateY(-18px)`;
- override tardio de `object-position:center bottom`.

Runtime de alinhamento:

```html
<script id="lk-goc-204l-desktop-collage-title-top-align-20260608">
```

Inclui:

- medição real de `.coll-banner__title`;
- medição real de `.lk-goc-collage` / `.lk-204l-collage`;
- cálculo de delta;
- ajuste de `transform` e `margin-bottom`;
- reexecução pós-render/responsive;
- mobile cleanup.

---

## 11. Receipts/evidências do ciclo

Receipts criados em:

```text
areas/lk/sub-areas/collection-optimizer/receipts/theme-dev/
```

### 11.1 Font tune

Diretório:

```text
lkgoc-204l-font-tune-20260608T193945Z
```

Conteúdo:

- backup antes da alteração;
- candidate;
- receipt;
- ajuste:
  - `Curadoria LK` 18px;
  - headline 29px.

### 11.2 Rosalía bottom alignment

Diretório:

```text
lkgoc-204l-rosalia-bottom-align-20260608T200450Z
```

Conteúdo:

- backup antes da alteração;
- candidate;
- receipt;
- ajuste:
  - imagem principal `object-position:center bottom!important`.

### 11.3 Crumbs/image overlap fix

Diretório:

```text
lkgoc-204l-crumbs-image-overlap-fix-20260608T201640Z
```

Conteúdo:

- backup de `layout/theme.liquid`;
- candidate;
- receipt;
- ajuste:
  - esconder crumbs;
  - remover border-bottom;
  - reduzir pull base;
  - reforçar bottom image no CSS tardio.

### 11.4 Desktop title/collage top alignment

Diretório:

```text
lkgoc-204l-desktop-collage-title-top-align-20260608T202950Z
```

Conteúdo:

- backup de `layout/theme.liquid`;
- candidate;
- receipt;
- ajuste:
  - runtime medido para alinhar collage ao topo real do `.coll-banner__title`.

---

## 12. Evidência de execução

Executado via Shopify CLI com Doppler-first:

- `shopify theme list` confirmou `lk-new-theme/dev` como `[unpublished]` e ID `155065450718`.
- `shopify theme push --theme 155065450718 --allow-live=false` retornou sucesso.
- `shopify theme pull --theme 155065450718` confirmou presença dos blocos remotos.

Confirmações por pull remoto:

- `lk-goc-204l-font-tune-20260608T193945Z` presente;
- `font-size:18px!important` presente;
- `font-size:29px!important` presente;
- `object-position:center bottom!important` presente;
- `lk-goc-204l-crumbs-image-overlap-fix-20260608` presente;
- `.coll-banner__crumbs` com `display:none!important` presente;
- `translateY(-18px)!important` presente;
- `lk-goc-204l-desktop-collage-title-top-align-20260608` presente;
- script usa `.coll-banner__title`;
- script usa `getBoundingClientRect().top`;
- script aplica `setProperty('transform', ...)`;
- script é desktop-only por `(min-width: 990px)`.

---

## 13. Worker/QA contract

Para novas execuções LKGOC não triviais, usar subconjunto mínimo dos workers definidos em `AGENTS.md`.

Neste ciclo, como a execução foi uma sequência de correções visuais diretas solicitadas por Lucas em uma coleção já em DEV, a validação foi feita por:

- leitura de arquivos;
- diff;
- push DEV com `--allow-live=false`;
- pull remoto/readback;
- receipts e rollback.

Para rollout em nova coleção, acionar/registrar ao menos:

1. **LKGOC Experience Architect** — valida que está replicando Gold 204L e não redesenhando;
2. **Shopify DEV Preview Builder** — materializa em tema `unpublished` verificado;
3. **Visual QA Mobile/Desktop Worker** — faz comparação visual e bloqueia overflow/placeholder/erro;
4. **Rollback & Receipt Verifier** — garante backup, rollback e evidência.

---

## 14. Checklist de replicação para nova coleção

Antes de escrever:

- [ ] Confirmar coleção alvo/handle.
- [ ] Confirmar tema DEV com `role: unpublished` por API/CLI.
- [ ] Abrir Gold Source 204L como referência.
- [ ] Verificar se já existe bloco LKGOC da coleção.
- [ ] Definir imagens editoriais e produto/coleção.
- [ ] Definir copy premium sem termos de estoque/pronta entrega.
- [ ] Definir FAQ/Guia LK.
- [ ] Criar rollback local.

Durante implementação:

- [ ] Usar namespace `lk-goc-*`.
- [ ] Manter aliases legados necessários.
- [ ] Não criar novo design system.
- [ ] Replicar estrutura do hero 204L.
- [ ] Adaptar `aria-label` da coleção.
- [ ] Adaptar kicker/headline/texto.
- [ ] Adaptar imagem principal e `alt`.
- [ ] Garantir imagem principal com `object-position` adequado.
- [ ] Garantir collage alinhado ao título/banner.
- [ ] Evitar crumbs/linhas cortando imagem.
- [ ] Garantir mobile sem transform desktop.
- [ ] Garantir “Ler mais” funcional/sem duplicidade.
- [ ] Garantir guia/FAQ sem duplicidade.

Após implementação:

- [ ] Push somente para DEV/unpublished.
- [ ] Pull remoto/readback do asset.
- [ ] QA desktop.
- [ ] QA mobile.
- [ ] Registrar screenshots quando disponíveis.
- [ ] Registrar receipt.
- [ ] Registrar rollback.
- [ ] Enviar approval packet para Lucas.
- [ ] Só promover para produção com aprovação explícita atual.

---

## 15. QA visual mínimo

Desktop:

- [ ] Topo do collage começa alinhado ao topo do `.coll-banner__title`.
- [ ] Crumbs não aparecem cortando imagem.
- [ ] Sem faixa/linha preta indesejada sobre o collage.
- [ ] Rosalía/card principal alinhado por bottom.
- [ ] Headline não compete com título principal.
- [ ] Kicker “Curadoria LK” legível e premium.
- [ ] Texto sem excesso de densidade.
- [ ] Cards menores não ficam comprimidos.

Mobile:

- [ ] Sem overflow horizontal.
- [ ] Collage não herda `translateY` desktop.
- [ ] Imagem principal mantém leitura limpa.
- [ ] “Ler mais” aparece/controla abertura conforme padrão.
- [ ] Cards complementares só aparecem no estado correto.
- [ ] Guia/FAQ não duplica.

Técnico:

- [ ] Sem Liquid error.
- [ ] Sem console error crítico do script LKGOC.
- [ ] `aria-label` correto.
- [ ] Asset remoto contém bloco esperado.
- [ ] Produção intacta.

---

## 16. Rollback consolidado

Para reverter apenas fonte/bottom no snippet:

- remover bloco:

```html
<style id="lk-goc-204l-font-tune-20260608T193945Z">...</style>
```

em `snippets/lk-goc-collection.liquid`.

Para reverter crumbs/overlap:

- remover bloco:

```html
<style id="lk-goc-204l-crumbs-image-overlap-fix-20260608">...</style>
```

em `layout/theme.liquid`.

Para reverter runtime de alinhamento:

- remover bloco:

```html
<script id="lk-goc-204l-desktop-collage-title-top-align-20260608">...</script>
```

em `layout/theme.liquid`.

Depois:

1. push para `lk-new-theme/dev` com `--allow-live=false`;
2. pull remoto para confirmar;
3. registrar receipt de rollback;
4. nunca aplicar rollback em production sem approval explícito.

---

## 17. Guardrails permanentes

- Produção nunca é área de teste.
- `DEV/unpublished → QA → approval Lucas → produção` é obrigatório.
- Nome do tema não basta; role precisa ser `unpublished`.
- Se `role: main/live`, abortar writes.
- Não usar estoque/pronta entrega como linguagem pública.
- Se a demanda envolver disponibilidade/grade/ruptura, handoff obrigatório para `[LK] Estoque Loja Física` / `lk-stock`.
- Usar Doppler-first para credenciais.
- Não imprimir secrets em receipts/logs.
- Receipts devem conter evidência e rollback.

---

## 18. Decisão canônica

A partir desta data, quando Lucas pedir “fazer no padrão LKGOC”, “seguir o gold”, “usar o padrão 204L” ou similar, o agente deve interpretar como:

> Replicar o padrão visual/editorial/operacional do New Balance 204L documentado neste arquivo, em DEV/unpublished, com QA e approval antes de qualquer produção.

Nome curto operacional:

**Gold 204L**

Nome completo:

**LKGOC Gold Source — New Balance 204L Hero/Guide**
