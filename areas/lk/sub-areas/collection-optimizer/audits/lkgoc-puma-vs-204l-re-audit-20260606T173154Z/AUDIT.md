# Re-audit — Puma Speedcat LKGOC vs Gold Source New Balance 204L

Data UTC: 20260606T173154Z
Status: **FAIL — FIDELIDADE LKGOC NÃO COMPROVADA / BUILD PUMA NÃO DEVE IR PARA PRODUCTION**

## Motivo do audit

Lucas apontou que a Puma Speedcat ficou totalmente fora do padrão definido pelo New Balance 204L. Este audit reavalia a entrega com o critério correto: **fidelidade visual e estrutural ao Gold Source 204L**, não apenas renderização técnica sem erro.

## Escopo

- Gold Source: `https://lksneakers.com.br/collections/new-balance-204l`
- Puma DEV DOM: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-dev-build-20260606T171642Z/qa-final/dev-preview-dom-python-cookie.html`
- Tema DEV usado anteriormente: `155065450718` / `role: unpublished`
- Production: não será tocado neste audit.

## Resultado executivo

O audit confirma que o erro principal foi de processo e critério de aceite:

1. O QA anterior validou **presença técnica**: hero, guia, FAQPage, imagens Vogue/Overkill, ausência de Liquid error.
2. O QA anterior **não validou fidelidade visual real** ao Gold Source 204L.
3. O build Puma foi tratado como uma branch LKGOC própria/adaptada, quando deveria ter sido uma **cópia controlada do padrão 204L**, mudando somente conteúdo, links, mídia e nuances comerciais.
4. Portanto, a entrega Puma em DEV deve ser considerada **reprovada para Production**.

## Checks automáticos

```json
{
  "puma_dev_has_lkgoc": true,
  "puma_uses_exact_204l_namespace_density": true,
  "puma_guide_after_grid": false,
  "puma_hero_before_grid": false,
  "puma_has_faq_schema": true,
  "puma_has_editorial_sources": true,
  "puma_no_liquid_error": true,
  "gold_source_detected": true
}
```

## Métricas DOM resumidas

### Gold 204L público

- bytes: `627407`
- lk-goc count: `102`
- lk-204l count: `236`
- lk-lkgoc count: `5`
- section count: `4`
- style tags: `31`
- product grid pos: `-1`
- guide pos: `29216`
- FAQPage: `True`

### Puma DEV preview DOM

- bytes: `632689`
- lk-goc count: `124`
- lk-204l count: `227`
- lk-lkgoc count: `5`
- section count: `4`
- style tags: `31`
- product grid pos: `-1`
- guide pos: `31191`
- FAQPage: `True`

## Violações identificadas

- QA anterior aceitou critérios técnicos/editoriais isolados (fontes, schema, ordem) sem gate visual de fidelidade ao 204L.

## Por que eu errei

- Eu confundi **“passar no QA técnico”** com **“estar fiel ao padrão LKGOC aprovado”**.
- O gate anterior perguntava se havia hero, guia, FAQ e mídia editorial; ele não perguntava se o resultado era praticamente o mesmo shell visual do 204L.
- Eu aceitei uma implementação por branch (`puma-speedcat`) dentro do componente único, mas não forcei a branch a ser uma adaptação mínima do bloco 204L.
- Eu não rodei um diff estrutural/visual contra o Gold Source antes de declarar PASS.
- A frase “usar padrão New Balance 204L” deveria ter sido tratada como requisito bloqueante, não como referência estética geral.

## Decisão operacional

- Puma Speedcat DEV atual: **reprovado visualmente**.
- Production: **continua bloqueado**.
- Próximo rebuild deve começar por extrair o shell 204L como contrato canônico e só depois substituir copy/mídia/FAQ da Puma.

## Correção recomendada — sem executar ainda

1. Congelar o build Puma atual como evidência de falha.
2. Extrair o shell real do 204L do componente/template atual.
3. Criar checklist de equivalência obrigatória:
   - mesma hierarquia de seções;
   - mesma densidade editorial;
   - mesmos padrões de espaçamento;
   - mesma lógica de hero/collage;
   - mesma ordem: hero → grid → guia;
   - FAQ no mesmo padrão;
   - apenas conteúdo e mídias alterados.
4. Rebuild Puma no DEV a partir do shell 204L, não de branch customizada.
5. QA visual lado a lado 204L vs Puma antes de qualquer aprovação.

## Artefatos

- DOM metrics: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-puma-vs-204l-re-audit-20260606T173154Z/DOM-METRICS.json`
- Gold HTML snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-puma-vs-204l-re-audit-20260606T173154Z/gold_204l_public.html`
- Puma DEV DOM snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-puma-vs-204l-re-audit-20260606T173154Z/puma-dev-dom.snapshot.html`
- Marker extracts: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-puma-vs-204l-re-audit-20260606T173154Z`


## Comparação do componente Liquid — 204L vs Puma

Fonte analisada: candidato DEV aplicado em `snippets/lk-goc-collection.liquid`.

### Branch hero / topo

- 204L bytes: `169647`
- Puma bytes: `174537`
- Similaridade de classes, Jaccard: `0.812`
- Ratio bytes Puma/204L: `1.029`

### Branch guia

- 204L bytes: `68010`
- Puma bytes: `73530`
- Similaridade de classes, Jaccard: `0.936`
- Ratio bytes Puma/204L: `1.081`

### Leitura crítica

Mesmo dentro do componente único, a Puma virou uma implementação própria. O padrão correto não é “estar no mesmo snippet”; é **reusar o shell 204L com substituição controlada**. A comparação por branch mostra que esse gate não foi formalizado antes do PASS.

Arquivo detalhado: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-puma-vs-204l-re-audit-20260606T173154Z/LIQUID-BLOCK-COMPARISON.json`


## Evidência visual

Foi gerada uma comparação lado a lado para revisão humana:

- Screenshot 204L desktop: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-puma-vs-204l-re-audit-20260606T173154Z/gold-204l-desktop.png`
- Screenshot Puma DEV desktop: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-dev-build-20260606T171642Z/qa-final/puma-speedcat-lkgoc-dev-dom-desktop.png`
- Comparativo lado a lado: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-puma-vs-204l-re-audit-20260606T173154Z/VISUAL-SIDE-BY-SIDE-204L-vs-PUMA.png`

Esse comparativo deve virar artefato obrigatório de QA antes de qualquer PASS LKGOC.
