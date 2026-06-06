# Regra LKGOC — paridade 204L sem seletores frágeis

Registrado em: 2026-06-05T10:09:57Z
Origem: incidente QA New Balance 9060 Full LKGOC DEV.
Gold source visual: New Balance 204L.

## Regra obrigatória
Toda coleção Full LKGOC que copiar/adaptar o padrão visual 204L deve herdar **também os overrides finais de acabamento** do padrão, não apenas a estrutura HTML/classes principais.

## Não fazer
- Não validar paridade somente por classe principal, background, altura ou contagem de blocos.
- Não trocar `aria-label`/handle/texto e assumir que os overrides finais continuarão aplicando.
- Não deixar CSS canônico preso apenas a seletor textual como:
  - `aria-label="Contexto editorial New Balance 204L"`
- Não enviar preview ao Lucas sem medir H1, headline, padding e line-height no mobile.
- Não aceitar diferença pequena de tipografia/alinhamento em título/subtítulo como “ok”; no LKGOC isso é quebra de padrão.

## Causa raiz registrada
No 9060, o bloco foi clonado do 204L, mas parte do CSS final mobile estava amarrada ao seletor:
`aria-label="Contexto editorial New Balance 204L"`.

Ao adaptar o aria-label para 9060, o bloco saiu de alguns overrides finais. Isso causou:
- título da coleção com `padding: 0 16px` em vez de `padding: 0`;
- título com `font-size` menor por herdar regra base/clamp;
- subtítulo com `font-size/line-height` diferente do 204L.

## Critério de aceite obrigatório mobile
Comparar coleção alvo vs 204L em viewport 390px antes de qualquer approval packet:

- `.coll-banner__title`
  - `x` equivalente;
  - `padding-left: 0px`;
  - `padding-right: 0px`;
  - `font-size: 40px` quando usando padrão 204L atual;
  - `line-height: 1.02` / ~`40.8px`.

- `.lk-collection-v2__headline`
  - `font-size: 31px` quando usando padrão 204L atual;
  - `line-height: 1` / ~`31px`;
  - `letter-spacing: -.045em`;
  - `font-family: Cormorant Garamond`;
  - alinhamento e margem iguais à 204L.

## Critério de aceite desktop
Além de hero/guia/grid/background, medir:
- H1 `.coll-banner__title`;
- headline `.lk-collection-v2__headline`;
- kicker `.lk-goc-kicker`/`.lk-204l-kicker`;
- parágrafo principal;
- container/copy/collage.

## Implementação recomendada
Preferir hooks estáveis por classe:
- `.lk-goc-coll-preview--204l`
- `.lk-goc-coll-preview--[handle]`
- `.lk-204l-coll-preview`

Se for necessário manter `aria-label` por compatibilidade, duplicar explicitamente para a coleção alvo ou migrar para classe canônica. Nunca depender apenas do texto do `aria-label` para acabamento visual crítico.

## Checklist QA obrigatório antes de mostrar preview
- [ ] Theme DEV é `role: unpublished` verificado por API.
- [ ] Produção/main não tocada.
- [ ] Screenshot 204L desktop e mobile.
- [ ] Screenshot coleção alvo desktop e mobile.
- [ ] Métricas computadas para H1/headline/kicker/parágrafo.
- [ ] Comparação lado a lado salva no workdir.
- [ ] Nenhuma frase operacional proibida em descrição/FAQ pública.
- [ ] Receipt com causa raiz e correção.

## Atualização — guia LK canônico por classe `lk-goc-*`
Registrado em: 2026-06-05T10:36:37Z

O mesmo princípio de evitar patches por coleção vale para o Guia Editorial LK dentro das collections.

### Regra obrigatória para guias dentro de coleção
- O painel deve usar classe canônica `lk-goc-guide-panel`.
- Elementos internos devem usar aliases canônicos `lk-goc-guide-*`, mantendo compatibilidade temporária com `lk-guide-standard-*` e `lk-lkgoc-*` quando necessário.
- O contrato visual deve ser class-based, não handle-based. Evitar CSS específico como `#lk-guia-new-balance-9060` quando a intenção for padrão LKGOC reutilizável.
- O padrão visual do guia deve ser validado contra o gold source 204L em desktop e mobile antes de preview/approval.

### Classes canônicas mínimas
- `lk-goc-guide-panel`
- `lk-goc-guide-panel__eyebrow`
- `lk-goc-guide-panel__intro`
- `lk-goc-guide-grid`
- `lk-goc-guide-card`
- `lk-goc-guide-card--wide`
- `lk-goc-guide-faq`
- `lk-goc-guide-media`
- `lk-goc-guide-panel__cta`

### Critério de aceite adicional
Em QA, medir em 390px e 1440px:
- classe do painel contém `lk-goc-guide-panel`;
- contrato canônico carregado;
- nenhum style específico da coleção substitui o contrato geral;
- `display`, `grid-template-columns`, `background`, `padding`, `margin`, H2 e card/FAQ/media/CTA batem com o padrão 204L.

