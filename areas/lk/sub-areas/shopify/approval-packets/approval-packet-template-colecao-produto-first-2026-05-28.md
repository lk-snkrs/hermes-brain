# Approval packet — Template LK coleção produto-first

Data: 2026-05-28  
Origem: Mesa COO — Decisão 1/3  
Resposta de Lucas: `Fazer`  
Dono executor: LK Shopify  
Co-dono/revisor: LK Growth  
Status: **read-only/local preparado; nenhum Shopify write executado**

## 1. Veredito curto

Preparado o pacote read-only para transformar o padrão “coleção LK produto-first” em template canônico operacional.

Artefato principal:

- `areas/lk/sub-areas/shopify/templates/template-colecao-produto-first-lk.md`

Este packet **não altera Shopify**. Ele só define o padrão, critérios de uso, limites, rollback e próxima aprovação necessária.

## 2. Por que isso importa

A coleção New Balance 204L provou que, para coleções comerciais da LK, o layout deve priorizar compra e descoberta de produto:

- produtos aparecem primeiro;
- topo fica minimalista;
- guia/FAQ/schema entram depois;
- CTA fica discreto;
- SEO/GEO não pode empurrar produto para baixo nem virar bloco editorial pesado antes do grid.

Sem template canônico, cada próxima coleção corre risco de virar um layout novo, com critérios diferentes e mais retrabalho.

## 3. Evidência usada

Fontes consultadas:

- `reports/daily-consolidation/2026-05-27.md`
  - linhas 40–45: execução e pendência do padrão 204L/produto-first.
  - linhas 144–151: amanhã recomendado inclui concluir/revisar padrão se Lucas aprovar.
  - linhas 154–158: golden pattern Shopify Production e propagação para skills/templates.
- `reports/governance/lk-shopify-golden-pattern-propagation-2026-05-27.md`
  - LK Shopify como rota explícita `lk-shopify-surface`.
  - LK Growth define/mede SEO/GEO/CRO/conteúdo.
  - writes futuros seguem snapshot → preview → aprovação escopada → execução → readback → receipt → rollback.
- `areas/lk/sub-areas/shopify/templates/preview-aprovacao-shopify.md`
  - superfície canônica de aprovação LK Shopify.
- `areas/lk/sub-areas/shopify/AGENTS.md`
  - LK Shopify como especialista da superfície Shopify.
- Skills carregadas na sessão:
  - `mesa`
  - `lk-shopify-readonly`
  - `lk-shopify-product-upload`
  - `lk-seo-weekly-improvement`

## 4. Template canônico proposto

Resumo do template criado:

### Estrutura padrão

1. Topo minimalista:
   - kicker curto;
   - H1 direto;
   - descrição curta;
   - CTA discreto se necessário.

2. Produtos primeiro:
   - grid aparece cedo;
   - mobile-first;
   - ordenação comercial quando disponível;
   - não bloquear produto por storytelling/SEO.

3. Confiança/atalhos leves:
   - curadoria exclusiva;
   - autenticidade;
   - atendimento humano;
   - loja física quando pertinente;
   - `Falar no chat` discreto.

4. Guia/editorial depois do grid:
   - contexto do modelo;
   - styling;
   - comparação;
   - links/source page quando existir.

5. FAQ/schema no final:
   - perguntas reais;
   - `FAQPage` só se FAQ visível e aprovado;
   - evitar promessa pública de estoque/prazo.

## 5. Critérios de uso

Usar quando:

- coleção tiver intenção comercial clara;
- for marca/modelo/collab/curadoria;
- tráfego orgânico/pago/social for esperado;
- SEO/GEO for importante, mas não deve prejudicar UX de compra;
- coleção tiver produtos suficientes para justificar grid como protagonista.

Não usar automaticamente quando:

- for source page/editorial puro;
- for guia sem objetivo de compra imediata;
- for landing campaign experimental;
- exigir design especial aprovado separadamente.

## 6. Responsabilidades

### LK Shopify

Responsável por:

- transformar o template em preview Shopify quando houver coleção-alvo;
- validar handle/collection/theme/asset/template;
- preparar snapshot/readback/receipt/rollback;
- executar somente após aprovação escopada.

### LK Growth

Responsável por:

- validar SEO/GEO/CRO;
- aprovar conteúdo pós-grid, FAQ e schema;
- garantir aderência ao padrão de guias editoriais;
- medir impacto depois de aplicado.

### Hermes Geral / Mesa COO

Responsável por:

- orquestrar a decisão;
- cobrar handoff/receipt;
- impedir que aprovação de template vire Shopify write automático.

## 7. Rollback

Para este packet/template local:

- rollback documental: remover/reverter:
  - `areas/lk/sub-areas/shopify/templates/template-colecao-produto-first-lk.md`
  - este packet.

Para aplicação futura em Shopify:

1. snapshot antes;
2. backup com timestamp;
3. dev/unpublished theme quando envolver layout/theme;
4. readback API/hash/DOM/screenshot;
5. produção só após aprovação separada;
6. rollback por re-upload/reaplicação do snapshot anterior.

## 8. Limites / o que NÃO foi aprovado

Este `Fazer` da Mesa aprovou preparar o packet read-only. Ele **não aprova**:

- alteração em Shopify production;
- alteração em dev theme;
- criação/edição de coleção viva;
- mudança de produtos, ordem, preço, estoque, status, SKU, tags, SEO field ou metafields;
- publicação de guia/source page;
- Klaviyo, WhatsApp, Meta, GMC, campanha ou qualquer envio externo;
- promessa de disponibilidade/prazo/reserva.

## 9. Próxima aprovação necessária

Para tornar este template uma regra oficial ativa do LK Shopify/Growth, Lucas pode aprovar a oficialização documental com:

> Aprovo oficializar o template LK coleção produto-first como padrão de preview para próximas coleções, sem Shopify write automático. Cada aplicação real continua exigindo preview, snapshot, readback, receipt e rollback.

Para aplicar em uma coleção real específica, usar outro approval com o handle da coleção e campos exatos.

## 10. Sequência enviada/preparada para especialistas

### Para LK Shopify

> Preparar próximas coleções usando `template-colecao-produto-first-lk.md` como padrão de preview. Nenhum write automático. Em qualquer coleção-alvo, montar preview no formato `preview-aprovacao-shopify.md`, com snapshot/readback/rollback e limites explícitos.

### Para LK Growth

> Revisar o bloco pós-grid: guia editorial, FAQ, schema, citability/GEO e CRO. Usar `PADRAO-GUIAS-EDITORIAIS-LK.md` quando virar guia/source page. Não priorizar HTML isolado sem impacto comercial.

## 11. Receipt

Resultado desta execução:

- Template local proposto criado.
- Approval packet local criado.
- Nenhum Shopify/Tiny/theme/GMC/Klaviyo/WhatsApp/email/produção alterado.
- Próxima decisão: Lucas aprovar ou ajustar a oficialização documental do template.
