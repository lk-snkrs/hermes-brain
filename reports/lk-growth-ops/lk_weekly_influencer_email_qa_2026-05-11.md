# QA — LK Weekly Influencer Email / produto-first

Data do QA: 2026-05-11
Escopo: revisão local/read-only de HTML/MIME/preview e aderência LK para relatório semanal influencer × produto × SKU × tamanho. Nenhum envio/campanha/write externo foi executado.

## Artefatos revisados

- Rotina: `/opt/data/hermes_bruno_ingest/hermes-brain-lk-gmail-safe-html-20260510/areas/lk/sub-areas/trafego-pago/rotinas/weekly-influencer-sales-email.md`
- HTML inline: `/opt/data/hermes_bruno_ingest/hermes-brain-lk-gmail-safe-html-20260510/reports/lk-weekly-gmail-safe-html-2026-05-09/email-preview-inline.html`
- MIME preview: `/opt/data/hermes_bruno_ingest/hermes-brain-lk-gmail-safe-html-20260510/reports/lk-weekly-gmail-safe-html-2026-05-09/email-preview.eml`
- Health check Brain: `/opt/data/hermes_bruno_ingest/hermes-brain-lk-gmail-safe-html-20260510/reports/brain-health-check-2026-05-10-lk-weekly-influencer-email-gmail-fix.json`
- Imagens CID extraídas para inspeção local: `/opt/data/kanban/boards/lk-growth-ops/workspaces/t_0b17108f/extracted_images/`

## Veredito

Não aprovar envio ainda.

O relatório está bem encaminhado em produto-first e tem MIME/HTML real, mas há bloqueios de marca/compatibilidade antes de qualquer envio ou aprovação executiva: divergência de canal Klaviyo vs Gmail, uso de CSS `display:grid` no HTML de e-mail, seção de criativos/imagens dentro do e-mail semanal apesar da rotina dizer que criativos ficam fora por padrão, e inconsistência de nome canônico `Silvia Henz` vs registros Brain/Shopify como `Silvia Heinz`.

## Checklist de conformidade

| Critério | Status | Evidência |
|---|---:|---|
| Produto-first com influencer × produto × SKU × tamanho | PASS | HTML contém 17 `rank-row`, 22 menções a SKU e 21 menções a `Tam.`. Cada linha principal combina influencer + produto vendido + SKU/tamanho. |
| Shopify como verdade de produto/receita | PASS com ressalva | Copy afirma “ponte Shopify segura” e produto só entra com evidência Shopify. Necessário validar origem dos totais em dados atuais antes de enviar. |
| Meta como sinal, não verdade de produto | PASS | Hero e seção “Sinal Meta sem produto” tratam Meta como sinal; `meta_signal_only` aparece 4 vezes. |
| MIME/HTML real | PASS | `.eml` é `multipart/related` com `multipart/alternative`, `text/plain`, `text/html` e 6 imagens inline por CID. |
| LK/Klaviyo-real | FAIL | Artefato é “gmail-safe”; headers do `.eml`: From/To `lucas@zippergaleria.com.br`. Não há evidência de template/preview Klaviyo real nem sender LK configurado no artefato revisado. |
| Gmail/mobile-safe inline | FAIL | HTML não tem `<style>` nem CSS variables, mas contém `display:grid` nos cards de criativo. Em e-mail isso é risco de layout quebrado; a própria rotina diz não depender de grid. |
| Sem termos internos proibidos | PASS | No HTML: 0 menções a `DesignMD`, 0 a `Cloudflare`, 0 a `dashboard`. |
| Sem envio real / sem writes externos | PASS | Revisão local somente. |
| Criativos / thumbnails adequados | FAIL para envio semanal; WARN visual | O `.eml` contém 6 imagens inline e seção “Influencer × criativo × venda”. A rotina define que o cron semanal deve ficar sem criativos por padrão. Visualmente as imagens não são pretas/ilegíveis, mas algumas são casuais/selfie e precisam de curadoria antes de material executivo. |
| Nome canônico de influencer | FAIL | HTML/script usam `Silvia Henz`; Brain/relatórios operacionais usam `Silvia Heinz`. Risco de confusão operacional e tracking. |

## Achados detalhados

1. Canal/preview não comprovam Klaviyo real
   - O card pede “preview LK/Klaviyo real”. O artefato revisado é Gmail-safe e o `.eml` tem headers `From: lucas@zippergaleria.com.br` e `To: lucas@zippergaleria.com.br`.
   - Isso pode servir como preview técnico local, mas não deve ser apresentado como Klaviyo-ready sem preview/render do template Klaviyo ou equivalência explícita.

2. CSS incompatível com e-mail
   - O HTML é majoritariamente inline, sem `<style>` e sem CSS variables, o que é bom.
   - Porém os cards de criativo têm `display:grid; grid-template-columns:190px minmax(0,1fr); gap:16px` no inline style. Como aparece após `display:block`, o `grid` vence em clientes que interpretam CSS sequencialmente; em Gmail/mobile pode quebrar.
   - Correção recomendada: converter cards de criativo para tabela ou blocos 100% empilhados, sem grid/flex como dependência.

3. Criativos dentro do e-mail semanal
   - A rotina diz: “Criativos continuam fora do e-mail semanal por padrão” e `--include-creative-assets` deve ser explícito; envio com criativos exige QA/aprovação.
   - O `.eml` revisado contém 6 imagens inline por CID e seção “Influencer × criativo × venda”. Isso é útil para preview interno, mas não deveria ser o e-mail semanal padrão.
   - Recomendação: gerar duas saídas distintas e nomeadas:
     - `weekly_email_no_creatives` para cron/aprovação de envio;
     - `internal_creative_preview` para análise executiva local.

4. Qualidade visual dos criativos
   - As 6 imagens CID extraídas não estão pretas, ilegíveis ou com letterbox/sidebar forte.
   - Mesmo assim, algumas têm estética muito casual/selfie ou enquadramento social. Para material executivo LK, curar/selecionar manualmente antes de anexar em qualquer e-mail externo.

5. Nome de influencer inconsistente
   - HTML e script usam `Silvia Henz`.
   - Relatórios Brain e matriz SKU/estoque usam `Silvia Heinz` como canônico.
   - Recomendação: padronizar label final para `Silvia Heinz` e manter aliases internos (`henz`, `heinz`, `silvia`) apenas na camada de matching, nunca na copy executiva.

6. Assunto e posicionamento
   - Assunto atual: `LK — Vendas Influencers semanal (2026-05-03 a 2026-05-09)`.
   - Melhor produto-first: `LK — Influencer × Produto vendido | 03–09/05`.
   - Evita soar como dashboard e aproxima do objetivo operacional.

## Itens que passaram

- Estrutura produto-first clara: primeiro ranking de produtos vendidos, depois sinais Meta sem produto.
- SKU/tamanho aparecem em praticamente todas as linhas de produto.
- Copy explica corretamente que Meta é sinal de mídia e Shopify é a ponte para produto.
- Sem termos proibidos no corpo HTML revisado (`DesignMD`, `Cloudflare`, `dashboard`).
- Health check Brain revisado sem FAIL/WARN.

## Correções mínimas antes de nova aprovação

1. Gerar artefato semanal sem seção de criativos e sem imagens CID para o fluxo recorrente padrão.
2. Gerar/fornecer preview Klaviyo real ou documentar que este fluxo é Gmail-only e não atende ao requisito Klaviyo.
3. Remover `display:grid` do HTML de e-mail; usar tabela/blocos inline-safe.
4. Corrigir `Silvia Henz` para `Silvia Heinz` na copy final; aliases só internos.
5. Revalidar uma amostra dos totais Shopify/revenue contra a fonte truth atual antes de envio.
6. Se houver versão executiva com criativos, manter local-only até curadoria visual e aprovação explícita do Lucas.

## Status final

Aprovado apenas como rascunho técnico local para QA.
Não aprovado para envio real, Klaviyo, Gmail externo ou material executivo com criativos.
