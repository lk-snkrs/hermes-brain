## 2026-05-11 — LK OS Weekly Quote Validation Preview read-only

- Criado e executado `scripts/lk_os_weekly_quote_validation_preview_20260511.py`, convertendo a fila semanal Stock/SKU em preview interno de validação/cotação.
- Resultado: 14 linhas avaliadas, 8 grupos de cotação por família, quantidade referência de cotação `26` unidades, sendo referência de disponibilidade/preço e não compra aprovada.
- Foram calculados preço médio vendido Shopify, tetos de custo para margens alvo 45/50/55%, gate de lead time e status de bloqueio SKU/Tiny para 3 linhas.
- Artefatos: `areas/lk/rotinas/weekly-quote-validation-preview-readonly-2026-05-11.md`, `reports/lk-os-weekly-quote-validation-preview-2026-05-04_2026-05-10.md`, `.json` e `.csv`.
- Nenhum fornecedor foi contatado; nenhuma compra, PO, write Shopify/Tiny, preço, estoque, campanha, cron ou envio externo foi executado.

## 2026-05-11 — LK OS Weekly Stock/SKU Action Plan read-only

- Criado e executado `scripts/lk_os_weekly_stock_sku_action_plan_20260511.py`, fila operacional P0/P1 derivada do Weekly CEO Review.
- Resultado: 14 linhas, sendo 6 P0 e 8 P1; status de ação: 6 candidatos a cotação preview, 5 para validar antes de cotar e 3 que exigem resolução SKU/Tiny antes de sourcing.
- Sinal de receita Shopify nas linhas: `R$ 89.669,71`; Tiny continua como `fact_tiny_stock` no depósito `LK | CONTROLE ESTOQUE`.
- Artefatos: `areas/lk/rotinas/weekly-stock-sku-action-plan-readonly-2026-05-11.md`, `reports/lk-os-weekly-stock-sku-action-plan-2026-05-04_2026-05-10.md`, `.json` e `.csv`.
- Nenhuma compra, PO, contato fornecedor, alteração Shopify/Tiny, preço, estoque, campanha, cron ou envio externo foi executado.

## 2026-05-11 — LK OS Weekly CEO Review read-only

- Criado e executado `scripts/lk_os_weekly_ceo_review_20260511.py`, revisão semanal executiva read-only do LK OS para 2026-05-04 a 2026-05-10.
- Resultado: Shopify `R$ 312.261,74` em 97 pedidos; GA4 29.605 sessões e 55 transações GA4; conversão aproximada pedidos Shopify / sessões GA4 `0,33%`.
- Estoque Tiny nos SKUs vendidos: 8 ruptura, 3 baixo estoque vs venda da semana, 3 desconhecidos/mapeamento sem candidato seguro ou saldo legível, 1 OK na amostra.
- Meta Ads e Metricool/Google Ads entram como `platform_signal`: Meta gasto `R$ 9.374,42`, Metricool/Google Ads 21 linhas/status 200; nenhum ROAS operacional declarado sem reconciliação.
- Artefatos: `areas/lk/rotinas/weekly-ceo-review-readonly-2026-05-11.md`, `reports/lk-os-weekly-ceo-review-2026-05-04_2026-05-10.md`, `.json`, e previews Telegram `.md`/`.json`.
- Nenhum Telegram automático, cron, campanha, fornecedor, compra, alteração em Shopify/Tiny, banco de produção ou envio externo foi executado.

## 2026-05-11 — LK OS Daily Sales Brief Telegram preview e silêncio

- Adicionado ao `scripts/lk_os_daily_sales_brief_20260511.py` o preview Telegram-ready do briefing diário, sem envio externo.
- Contrato de silêncio: `would_notify=true` apenas para P0/P1, falha de API ou pedido explícito do Lucas; caso contrário, manter canal em silêncio.
- Para 2026-05-10, o preview marcou `trigger=p0_p1_anomaly`, com Shopify `R$ 34.809,92` em 9 pedidos, GA4 4.301 sessões e Tiny com 4 ruptura, 3 baixo estoque e 3 unknown nos SKUs vendidos checados.
- Artefatos: `reports/lk-os-daily-sales-brief-telegram-preview-2026-05-10.md` e `.json`.
- Nenhum Telegram automático, cron, campanha, fornecedor, compra, alteração em Shopify/Tiny, banco de produção ou envio externo foi executado.

## 2026-05-11 — LK OS Daily Sales Brief real read-only

- Criado e executado `scripts/lk_os_daily_sales_brief_20260511.py`, primeiro briefing diário real do LK OS usando Shopify + GA4 + Tiny.
- Janela: dia fechado 2026-05-10 BRT.
- Resultado: Shopify `R$ 34.809,92` em 9 pedidos; GA4 4.301 sessões e 8 transações GA4; conversão aproximada pedidos Shopify / sessões GA4 `0,21%`.
- Estoque Tiny nos SKUs vendidos: 4 ruptura, 1 baixo estoque vs venda do dia, 5 desconhecidos/mapeamento sem candidato seguro ou saldo legível.
- Artefatos: `areas/lk/rotinas/daily-sales-brief-readonly-2026-05-11.md`, `reports/lk-os-daily-sales-brief-2026-05-10.md`, `reports/lk-os-daily-sales-brief-2026-05-10.json`.
- Nenhum write, cron, campanha, envio, alteração de estoque/preço, banco de produção, Shopify/Tiny/Klaviyo/Notion/Meta/Google/Metricool/n8n ou infra foi executado.

## 2026-05-11 — LK OS Tiny freshness report read-only

- PR #90 do Data Spine snapshot foi squash-merged e o clone local do Brain foi sincronizado em `origin/main` no commit `02b8223`.
- Criado e executado `scripts/lk_os_tiny_freshness_report_20260511.py`, relatório read-only específico para saúde/latência do Tiny ERP e visibilidade do depósito `LK | CONTROLE ESTOQUE`.
- Resultado: status `green`, 6/6 buscas OK, 8/8 checks de estoque OK, depósito oficial visto em 8/8, mediana 379 ms, p95 1442 ms, 0 erros.
- Relatórios públicos: `reports/lk-os-tiny-freshness-report-2026-05-11.md` e `.json`; saída privada auditável em `/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots/` com permissão restrita.
- Nenhum write, cron, campanha, envio, alteração de estoque/preço, banco de produção, Shopify/Tiny/Klaviyo/Notion/Meta/Google/Metricool/n8n ou infra foi executado.

## 2026-05-11 — LK OS Data Spine snapshot read-only executado

- Criado e executado `scripts/lk_os_data_spine_snapshots_20260511.py`, com snapshot read-only de Shopify, Tiny, GA4, Meta Ads, Metricool/Google Ads e Klaviyo.
- Resultado: 6/6 fontes OK; relatório público em `reports/lk-os-data-spine-snapshot-2026-05-11.md` e JSON sanitizado em `reports/lk-os-data-spine-snapshot-2026-05-11.json`.
- Saída privada auditável salva fora do Git em `/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots/` com permissão restrita.
- Atualizado o plano mestre do LK OS para marcar o primeiro bloco de scripts read-only com contagem/freshness como concluído em v0.1.
- Nenhum write, cron, campanha, envio, alteração de estoque/preço, banco de produção, Shopify/Tiny/Klaviyo/Notion/Meta/Google/Metricool/n8n ou infra foi executado.

## 2026-05-11 — LK OS Fase 1 Data Spine read-only iniciado

- Criada rotina `areas/lk/rotinas/data-spine-readonly-2026-05-11.md` para consolidar fonte da verdade, matriz Doppler sem valores, entidades canônicas, regras de reconciliação e lacunas.
- Criado contrato `areas/lk/contexto/data-spine-v0.1.md` com classes de fonte: `fact_shopify`, `fact_tiny_stock`, `fact_ga4`, `platform_signal`, `derived_reconciliation`, `manual_approval` e `unknown`.
- Atualizado o PRD e plano mestre do LK OS: Fase 1 agora está iniciada; scripts read-only por fonte seguem como próximo passo técnico.
- Nenhum write, cron, campanha, envio, banco de produção, Shopify/Tiny/Klaviyo/Notion/Meta/Google/n8n ou infra foi alterado.

## 2026-05-11 — Correção de link Klaviyo

- Lucas testou o link direto sugerido para a campanha Klaviyo e ele retornou página inexistente.
- Removida a orientação de usar deep link não verificado; a rotina agora manda localizar a campanha pelo painel Klaviyo usando nome ou Campaign ID.
- Regra registrada: link de Klaviyo só deve ser salvo como link clicável quando for verificado no painel logado; link de API serve apenas como evidência técnica.

## 2026-05-11 — LK Klaviyo P1 mantida em Draft

- Registrada a decisão do Lucas de manter a campanha P1 de CRM/Klaviyo em `Draft`, sem envio, sem agendamento e sem flow.
- Rotina `areas/lk/sub-areas/crm/rotinas/klaviyo-p1-draft-campaign-2026-05-11.md` atualizada com o Campaign ID e link operacional provável para revisão no Klaviyo.
- Próximo bloco recomendado: seguir o PRD por fases, priorizando a base que desbloqueia execução recorrente sem criar campanhas automáticas.

## 2026-05-11 — LK CRM/Klaviyo P1 draft documentado no PRD

- Consolidada a Fase 5 do LK OS no PRD e no plano mestre: a campanha P1 de recompra/curadoria chegou até rascunho Klaviyo, sem envio ou agendamento.
- Documentada a rotina `areas/lk/sub-areas/crm/rotinas/klaviyo-p1-draft-campaign-2026-05-11.md` com List ID `U8YCCE`, Template ID `XUSEtu` e Campaign ID `01KRC1DPTY615GF5FNBPXMPKY6` em `Draft`.
- Reforçado o padrão CRM premium: HTML customer-facing sem jargão interno, PII fora do Brain, e aprovação final obrigatória antes de qualquer envio.
- Próximo passo: manter Draft, confirmar template no campaign message e decidir com Lucas entre envio aprovado, P2 ou WhatsApp concierge.

## 2026-05-11 — LK SEO/CRO Weekly Improvement operacionalizado

- Criada skill canônica `lk-seo-weekly-improvement` para o módulo semanal de SEO/CRO com nota Claude SEO, meta de evolução e fila de melhoria de PDP/páginas.
- Documentada rotina `areas/lk/rotinas/seo-cro-weekly-improvement-loop.md` e indexada em `empresa/skills/_index.md` / `empresa/rotinas/_index.md`.
- Atualizada Fase 6 do LK OS para refletir que SEO deve virar fila de melhoria, não relatório solto.
- Guardrail mantido: auditoria e preview são read-only; alterações em Shopify/tema/feed/conteúdo público exigem aprovação explícita.

## 2026-05-11 — LK Fila B residual priorizada para revisão manual

- Cruzada a Fila B residual pós-saneamento com o relatório de estoque/venda já existente para decidir a sequência antes de nova Fila A.
- Resultado: 15 variants residuais também aparecem na fila de venda/ruptura existente; 51 ambíguos seguem como P1; 374 sem SKU Shopify como P2; 857 com SKU Shopify sem Tiny seguro como P3.
- Artefatos: `areas/lk/rotinas/shopify-tiny-fila-b-residual-priorizada-2026-05-11.md` e `reports/lk-shopify-tiny-residual-fila-b-prioritized-review-2026-05-11.json`.
- Etapa read-only: sem Shopify/Tiny write, sem sourcing, compra, contato fornecedor, estoque, preço, campanhas, clientes, banco, VPS/Docker ou secrets.

## 2026-05-11 — LK Fila B residual classificada pós-saneamento Shopify/Tiny

- Classificados os 1.282 variants pulados por segurança na normalização catálogo completo Shopify SKU→Tiny, sem novos writes externos.
- Quebra operacional: 857 com SKU Shopify mas sem match Tiny seguro; 374 sem SKU Shopify e sem match Tiny seguro; 40 sem SKU com ambiguidade título+tamanho; 11 com SKU e ambiguidade título+tamanho.
- Próxima sequência segura: resolver primeiro 51 ambíguos, depois 374 variants sem SKU, depois 857 com SKU sem match Tiny seguro; só então gerar nova Fila A de sourcing/reposição.
- Artefatos: `areas/lk/rotinas/shopify-tiny-fila-b-residual-pos-saneamento-2026-05-11.md` e `reports/lk-shopify-tiny-residual-fila-b-2026-05-11.json`.
- Produção, Shopify, Tiny, preço, estoque, campanha, cliente, fornecedor, banco, VPS/Docker e secrets não foram alterados nesta etapa.

## 2026-05-11 — LK Shopify SKUs padronizados para Tiny no catálogo completo

- Após Lucas pedir “seguir” para todos os produtos com SKUs diferentes, comparei o catálogo completo Shopify com o Tiny e executei apenas updates SKU-only com match seguro.
- Escopo lido: 2.271 produtos Shopify / 15.041 variants; 18.001 produtos Tiny; 15.746 produtos Tiny com `codigo` não-vazio.
- Resultado: 505 variants Shopify divergentes alinhadas exatamente ao `codigo` Tiny e verificadas live; 0 falhas; 13.254 variants já estavam idênticas antes da execução.
- Critério de segurança: 238 updates por SKU normalizado único, 11 por SKU normalizado + título/tamanho, 256 por produto+tamanho único; 1.282 variants foram puladas por ambiguidade, ausência de match seguro ou Tiny sem `codigo`.
- Backup/rollback por `variant_id` registrado em `reports/lk-shopify-tiny-all-sku-diff-plan-2026-05-11.json` e verificação em `reports/lk-shopify-tiny-all-sku-normalization-execution-2026-05-11.json`.
- Não alterei preço, estoque, título, handle, imagens, coleções, campanhas, clientes, Klaviyo/WhatsApp, fornecedores, Tiny, banco, VPS/Docker ou secrets.

## 2026-05-11 — LK Shopify SKUs padronizados para Tiny

- Com aprovação explícita do Lucas no Telegram, executei a padronização de SKUs da Shopify para ficarem idênticos ao `codigo` do Tiny em variants com alta confiança e código Tiny não-vazio.
- Resultado: 8 variants Shopify alteradas e verificadas live com sucesso via REST `PUT /variants/{id}.json`; 0 falhas; backup/rollback por `variant_id` registrado.
- Alterações: Onitsuka Tiger Mexico 66 Kill Bill Amarelo tamanhos 35, 36, 37, 39, 40 e 42.5; Onitsuka Tiger Mexico 66 Chrome Silver Prata tamanhos 35.5 e 37.
- Itens com código Tiny vazio, já idênticos, ou sem variant Shopify encontrada com confiança suficiente foram pulados sem write.
- Não alterei preço, estoque, título, handle, imagens, coleções, campanhas, Klaviyo/WhatsApp, fornecedores, Tiny, banco, VPS/Docker ou secrets.

## 2026-05-11 — LK Stock Fila B saneada + Fila A preview

- Executado o pedido “B depois A”: gerado `areas/lk/rotinas/stock-sku-saneamento-b-e-preview-a-2026-05-11.md` e o JSON auditável `reports/lk-stock-sku-saneamento-b-e-preview-a-2026-05-11.json`.
- Fila B read-only: 33 linhas analisadas; 14 tiveram SKU candidato atual encontrado na Shopify, 8 tiveram candidato Tiny para mapeamento/alias, 11 seguem para revisão manual de cadastro Shopify antes de qualquer decisão comercial.
- Fila A read-only: 103 linhas elegíveis para preview de sourcing/reposição; top P0/P1 ranqueados por ruptura, venda e velocidade estimada vs lead time padrão.
- Criados cards Mission Control unassigned para saneamento SKU, preview sourcing, lead time real e Data Spine.
- Produção, Shopify, Tiny, fornecedores, compras, campanhas, WhatsApp/Klaviyo, banco, VPS/Docker e secrets não foram alterados.

## 2026-05-10 — LK Gmail-safe HTML email rendering

- Corrigido o e-mail semanal LK para não depender de `<style>`, `@import`, CSS variables ou grid que o Gmail/mobile pode ignorar, causando aparência de texto puro.
- O envio por Gmail agora transforma o HTML DesignMD LK em HTML compatível com e-mail usando estilos inline antes de montar o MIME.
- Validação local e envio real corrigido: MIME `multipart/related` + `multipart/alternative`, 6 imagens CID, HTML com estilos inline, 0 `<style>`, 0 `var(--...)`, 0 `file://` e 0 termos sensíveis.
- Gmail message id do reenvio corrigido: `19e133a240640a9b`.
- Regra operacional reforçada: e-mails/relatórios LK por e-mail devem renderizar como HTML visual real; se aparecerem como texto/plain ou sem DesignMD, é falha.

## 2026-05-10 — LK inline creative email MIME preview

- Adicionado suporte seguro a MIME `multipart/related` com imagens inline via CID para a seção opcional de criativos do relatório semanal.
- O cron/e-mail padrão continua sem criativos; `--send --include-creative-assets` ainda bloqueia sem a flag explícita `--allow-send-creative-assets-inline`.
- Novo `--email-mime-preview` escreve o `.eml` exato que seria enviado, sem envio externo, permitindo validar `cid:`, imagens anexadas e ausência de `file://`/tokens antes de liberar.
- Validação local `2026-05-03..2026-05-09`: 6 imagens inline preparadas, MIME `multipart/related`, HTML com `src="cid:..."`, 0 `file://`, 0 termos sensíveis, browser QA do HTML aprovado.

## 2026-05-10 — LK creative sales view correction

- Corrigida a leitura dos criativos no relatório semanal: a seção opcional deixou de ser “vídeos depois do ranking” e passou a seguir `influencer → criativo → vendas → produtos`.
- Cada card mostra influencer, imagem do criativo, compras/spend/valor atribuído Meta do anúncio, pedidos/receita Shopify por `ad_id` exato e produtos vendidos ligados ao criativo quando há ponte segura.
- Produtos só são atribuídos ao criativo quando o Shopify traz `ad_id` Meta exato; vendas por texto/cupom permanecem no nível influencer para não inventar qual vídeo gerou o pedido.
- Preview local `2026-05-03..2026-05-09`: Fiorela mostrou 1 pedido / R$ 8.729,97 e 4 produtos ligados ao criativo por `ad_id`; demais cards ficam explicitamente sem produto por falta de ponte exata.
- Browser QA validou imagens reais carregadas, sem cards pretos/quebrados, e layout claro em DesignMD LK.

## 2026-05-10 — LK weekly report creative preview flag

- O relatório semanal `scripts/lk_weekly_influencer_sales_report.py` agora aceita `--include-creative-assets` para montar uma prévia HTML local com seção “Criativos em veiculação” usando os assets reais colhidos pelo `lk_weekly_creative_audit.py`.
- A flag faz curadoria mínima: exige imagem local existente, bloqueia frames pretos, rejeita miniaturas pequenas, deduplica por asset e limita a quantidade exibida.
- Guardrail: o cron/e-mail semanal continua sem criativos por padrão; `--include-creative-assets` é bloqueado com `--send` até existir fluxo de anexo/inline-image e QA visual novo.
- Validação local `2026-05-03..2026-05-09`: 6 criativos reais incluídos na prévia, DesignMD LK validado no browser, sem cards pretos/quebrados e sem query params sensíveis.
- Produção, VPS/Docker, bancos, campaigns, Shopify/Tiny/Klaviyo/WhatsApp, secrets, crons e envios externos não foram alterados.

## 2026-05-10 — LK creative asset harvesting

- Corrigida a auditoria de criativos para realmente obter imagens úteis dos anúncios Meta, não apenas iframes de preview.
- `scripts/lk_weekly_creative_audit.py` agora consulta creative/video/adimages, baixa assets locais, evita fallback 64×64 quando há alternativa, detecta frames pretos/sidebars com `ffmpeg` e renderiza contact sheet DesignMD LK com imagens locais.
- Validação `2026-05-03..2026-05-09`: 12 ads auditados, 12 assets escolhidos, todos `1080×1920`; browser QA aprovou 12 cards com imagens reais carregadas, sem blocos pretos/quebrados e sem thumbnail 64×64 borrada.
- Guardrails: local/read-only, sem envio externo, sem alteração de campanhas/cron/Shopify/Tiny/banco/VPS; JSON/HTML versionados não persistem URLs-fonte nem tokens/secrets.
- Ressalva de curadoria: #02/#07 Lala são visualmente redundantes; #11 Lala é lifestyle menos produto-first, então remover/substituir antes de eventual envio executivo.

## 2026-05-10 — LK local creative audit guardrail

- Adicionado `scripts/lk_weekly_creative_audit.py`, auditoria local/read-only para criativos Meta em veiculação, separada do e-mail semanal.
- O script ranqueia top ads por compras/valor/spend canônicos, usa a regra Maicon `ad_name` no script semanal e gera JSON + HTML DesignMD LK em `/opt/data/lk_weekly_creative_audits/`.
- Guardrail mantido: não usa `thumbnail_url` 64×64 no e-mail; usa apenas iframes de preview Meta sem parâmetros de token/secret e exige QA visual manual antes de promover criativo para relatório executivo.
- Validação `2026-05-03..2026-05-09`: 8 ads auditados, 32 iframe URLs sem token; browser QA aprovou o layout premium, mas mostrou vários previews pretos/sem frame útil, então criativos continuam fora do e-mail até asset nítido/validado.
- Produção, VPS/Docker, bancos, campaigns, Shopify/Tiny/Klaviyo/WhatsApp, secrets, crons e envios externos não foram alterados.

## 2026-05-10 — LK Maicon ad_name influencer rule

- Confirmada e operacionalizada a orientação do Maicon: no Meta, o nome da influencer deve ser lido primeiro em `ad_name` e múltiplos anúncios/ad_ids da mesma influencer precisam ser somados.
- Scripts semanal e mensal agora fazem matching por prioridade `ad_name → adset_name → campaign_name`, mantendo adset/campaign apenas como fallback/discovery.
- Validação abril/2026: `180` rows Meta, `104` anúncios/influencer Pareto-compatible matched, `104` via `ad_name`, `0` via adset/campaign; números globais Meta continuam batendo com Pareto.
- Validação semanal `2026-05-03..2026-05-09`: `113` matches atuais via `ad_name`; relatório segue sem envio externo no teste.
- Produção, VPS/Docker, bancos, campaigns, Shopify/Tiny/Klaviyo/WhatsApp, secrets, crons e envios externos não foram alterados.

## 2026-05-10 — LK Monthly Pareto HTML executive preview

- O script mensal Pareto-compatible agora também gera `.html` executivo em DesignMD LK, além de `.md` e `.json`.
- Preview abril/2026 validado visualmente: header premium LK, Direct destacado em card e linhas de tabela, canais GA4 completos, dashboards Meta/Google separados e influencers preenchidos.
- Corrigida padronização visual/numérica: moeda, sessões, percentuais e ROAS em formato brasileiro (`11,04x`, `20,48x`).
- Registrado que a prévia mensal é local/dry-run e sem envio externo ou cron automático até autorização explícita do Lucas.
- Produção, VPS/Docker, bancos, campaigns, Shopify/Tiny/Klaviyo/WhatsApp, secrets, crons e envios externos não foram alterados.

## 2026-05-10 — LK Direct channel summary fix

- Ajustado o relatório mensal Pareto-compatible para deixar `Direct` explícito no resumo executivo, não apenas canais pagos.
- Abril/2026 agora destaca: Direct `R$ 100.759,70`, `12.801` sessões, `35` pedidos, conversão `3,40%`.
- A listagem de canais GA4 passou a incluir top 12 canais, cobrindo pagos, orgânicos, Direct, referral, shopping, e-mail e paid other.
- Documentada a regra: receita real por canal = GA4 completo; dashboards Meta/Google ficam separados como atribuição de plataforma.

## 2026-05-10 — LK Pareto source calculation fix

- Corrigido ponto levantado por Lucas: o script agora aprende/reproduz **como** a Pareto calcula, sem copiar números do PDF como fonte.
- Implementadas consultas reais: GA4 Data API para resumo e-commerce/canais/source-medium; Meta Marketing API para dashboard Meta; Metricool Google Ads API para dashboard Google.
- Abril/2026 agora é calculado diretamente das fontes: GA4 `R$ 722.636,36`, `233 pedidos`, `166.003 sessões`; ROAS geral = GA4 receita / (Meta spend + Google spend) = `11,04`.
- Receita real por canal agora vem de GA4: `Paid Social R$ 211.329,00`, `facebook / paid R$ 181.859,02`, `google / cpc R$ 130.069,50`, etc.
- Google Ads via Metricool bate spend 100% (`R$ 26.481,76`); valor atribuído atual da API fica `R$ 209.636,37` vs PDF `R$ 207.240,45` (~98,84%), tratado como variação de export/API dentro da tolerância operacional.
- Atualizados `scripts/lk_monthly_pareto_reconciliation.py`, `reports/lk-pareto-april-2026/pareto-compatible-script-output.*`, `reconciliation-audit.md` e a rotina `pareto-monthly-reconciliation.md`.
- Produção, VPS/Docker, bancos, campaigns, Shopify/Tiny/Klaviyo/WhatsApp, secrets e envios externos não foram alterados.

## 2026-05-10 — LK channel-sales logic correction

- Corrigida a lógica da reconciliação Pareto: dashboards de Meta/Google são métricas atribuídas de plataforma, não venda real por canal.
- O relatório mensal agora mostra a venda e-commerce real (`R$ 722.636,36`) separada dos valores de plataforma: Meta Ads Manager `R$ 797.654,65` e Google Ads `R$ 207.240,45`.
- Adicionadas as referências Pareto/GA4 para contribuição real de canais/origens: `Paid Social R$ 211.329`, `facebook / paid R$ 181.859,02`, `google / cpc R$ 130.069,50`, `Paid Search R$ 51.137`, `Cross-network R$ 58.924`.
- Atualizados `scripts/lk_monthly_pareto_reconciliation.py`, `reports/lk-pareto-april-2026/reconciliation-audit.md`, `pareto-compatible-script-output.*` e `areas/lk/sub-areas/trafego-pago/rotinas/pareto-monthly-reconciliation.md`.
- Produção, VPS/Docker, bancos, campaigns, Shopify/Tiny/Klaviyo/WhatsApp, secrets e envios externos não foram alterados.

## 2026-05-10 — LK Meta attribution label correction

- Corrigida a interpretação da reconciliação Pareto: o campo Meta que o PDF chama de `Receita` agora é rotulado nos relatórios LK como `valor atribuído Meta no gerenciador`, não como venda/receita real da LK.
- Abril/2026 mantém match de 100% com o campo Meta/Ads Manager da Pareto: R$ 38.954,76 spend, 229 compras atribuídas, R$ 797.654,65 valor atribuído, ROAS Meta 20,48.
- Adicionado alerta explícito: a LK/Pareto e-commerce vendeu R$ 722.636,36; como o valor atribuído Meta excede esse total em R$ 75.018,29, não é correto dizer que “a Meta vendeu R$ 797 mil”.
- Atualizados `scripts/lk_monthly_pareto_reconciliation.py`, `reports/lk-pareto-april-2026/reconciliation-audit.md`, `pareto-compatible-script-output.*` e a rotina `pareto-monthly-reconciliation.md`.
- Produção, VPS/Docker, bancos, secrets, campanhas, Shopify/Tiny/Klaviyo/WhatsApp e envios externos não foram alterados.

## 2026-05-10 — LK Monthly Pareto reconciliation script

- Adicionado `scripts/lk_monthly_pareto_reconciliation.py`, script read-only para gerar reconciliação mensal Meta em modo `Pareto-compatible` e `Lucas-operacional`.
- Rodado para abril/2026 e versionado output em `reports/lk-pareto-april-2026/pareto-compatible-script-output.md` e `.json`.
- O script confirmou Meta global 100% alinhado ao PDF Pareto: R$ 38.954,76 spend, 229 compras, R$ 797.654,65 valor Meta, ROAS 20,48 e CPA R$ 170,11.
- Modo Pareto-compatible separa `Maria`, `Maria Fernanda` e `Mariah`; abril mostrou Maria com 2 compras/R$ 741,54 e Maria Fernanda/Mariah com zero compra Meta.
- Produção, VPS/Docker, bancos, secrets, campanhas, Shopify/Tiny/Klaviyo/WhatsApp e envios externos não foram alterados.

## 2026-05-10 — LK Pareto April reconciliation + Maria split

- Versionada auditoria `reports/lk-pareto-april-2026/reconciliation-audit.md` comparando o PDF do Maicon/Pareto de abril/2026 com Meta Ads direto e Shopify Admin.
- Confirmado que Meta global de abril bate exatamente com Pareto: R$ 38.954,76 spend, 229 compras, R$ 797.654,65 valor Meta, ROAS 20,48 e CPA R$ 170,11.
- Registrada regra Lucas: aderência 99%+ é operacionalmente correta; diferenças pequenas de poucos reais não devem travar a análise quando a metodologia está alinhada.
- Criada rotina `areas/lk/sub-areas/trafego-pago/rotinas/pareto-monthly-reconciliation.md` com dois modos: `Pareto-compatible` e `Lucas-operacional`.
- Corrigido `scripts/lk_weekly_influencer_sales_report.py` para separar `Maria`, `Maria Fernanda` e `Mariah` no matching, seguindo a lógica Pareto-compatible.
- Produção, VPS/Docker, bancos, secrets, campanhas, Shopify/Tiny/Klaviyo/WhatsApp e envios externos não foram alterados.

## 2026-05-10 — LK Weekly Influencer Email DesignMD + product ranking correction

- Corrigido o e-mail semanal de influencers após feedback do Lucas: o template anterior ignorava o DesignMD LK e usava cards de criativos Meta borrados/errados.
- `scripts/lk_weekly_influencer_sales_report.py` agora renderiza o e-mail no sistema visual LK (`areas/lk/design/DESIGN.md`): fundo paper, header preto, linguagem editorial/premium, títulos serifados e UI minimalista.
- Estrutura do relatório corrigida para ranking produto-first: `influencer × produto vendido × SKU × tamanho`, agregado por influencer + SKU + variante/tamanho para evitar duplicidade por variações de título Shopify.
- Thumbnails/criativos Meta foram removidos do e-mail semanal; Meta fica como sinal secundário e produtos/receita vêm do Shopify com ponte segura.
- Preview visual validado em `reports/lk-weekly-influencer-sales-2026-05-09/designmd-product-ranking-preview.html` e screenshot `designmd-product-ranking-preview.png`: 17 linhas produto/SKU, 20 unidades, R$ 76.399,80 de receita com ponte, 0 imagens no HTML e 0 padrões de secret.
- Produção, VPS/Docker, bancos, secrets, campanhas, Shopify/Tiny/Klaviyo/WhatsApp e cron runtime não foram alterados; apenas prompt do cron Hermes foi atualizado para evitar regressão.

## 2026-05-10 — LK Weekly Influencer Email top creatives

- Atualizado `scripts/lk_weekly_influencer_sales_report.py` para buscar imagens públicas e seguras dos top anúncios Meta da semana e renderizar seção visual vertical/mobile no topo do e-mail HTML.
- O script bloqueia persistência/renderização de URLs de criativo com `access_token`, `appsecret_proof` ou `client_secret` em query string.
- Preview gerado em `reports/lk-weekly-influencer-sales-2026-05-09/preview-with-top-creatives.html` e screenshot em `reports/lk-weekly-influencer-sales-2026-05-09/top-creatives-email-preview.png`.
- Teste dry-run gerou 12 criativos com imagem e 0 padrões de token no HTML/JSON; browser preview validou cards verticais e contraste do rodapé.
- Produção, VPS/Docker, bancos, secrets, campanhas, Shopify/Tiny/Klaviyo/WhatsApp, cron e runtime não foram alterados.

## 2026-05-10 — LK Weekly Influencer Attribution Gap Audit

- Adicionado `reports/lk-weekly-influencer-sales-2026-05-09/attribution-gap-audit.md` após rechecagem dos influencers ainda zerados no Shopify depois da correção de `ad_id`.
- Confirmado que Fiorela foi o caso corrigido por ponte `ad_id` exata; Lala Noleto, Ju Mesquita, Arlindo e Mariah seguem como `meta_signal_only` nesta janela, sem ponte Shopify segura.
- Identificado 1 pedido potencial por `campaign_id`/`adset_id` genérico, mas mantido como não atribuível porque a estrutura agrupa vários influencers e geraria falso positivo.
- Produção, VPS/Docker, bancos, secrets, campanhas, Shopify/Tiny/Klaviyo/WhatsApp, cron e runtime não foram alterados.

## 2026-05-10 — LK Weekly Influencer Sales Email HTML + ad_id attribution fix

- Corrigido o envio Gmail da newsletter semanal para `Content-Type: text/html`, evitando cliente exibir a peça como corpo em texto/Markdown.
- Corrigida a ponte Shopify do relatório semanal para aceitar `ad_id` Meta exato vindo de `utm_content`/`ad_id`/`fb_ad_id`, além de ponte textual.
- `campaign_id`/`adset_id` genéricos continuam bloqueados como ponte de produto, porque podem agrupar vários influencers; `ad_id` exato prevalece sobre matches textuais fracos poluídos por fornecedor/tag interna.
- Reprocessamento teste de `2026-05-03..2026-05-09`: Fiorela deixou de aparecer zerada em Shopify e passou a mostrar 1 pedido / R$ 8.729,97 por `ad_id Meta`, com produtos nome + SKU + tamanho.
- Envio teste HTML validado com Gmail `message_id` `19e11fe1a8112eca`; metadata Gmail confirmou `mimeType: text/html`.
- Produção, VPS/Docker, bancos, secrets, campanhas, Shopify/Tiny/Klaviyo/WhatsApp e runtime não foram alterados.

## 2026-05-10 — LK Weekly Influencer Sales Email Gmail validation

- Validado envio real do e-mail semanal de influencers: Gmail `message_id` `19e11e34e2b85b52`.
- Corrigida a seleção de credenciais Gmail no script para testar conjuntos nomeados e usar o primeiro OAuth válido, sem imprimir secrets.
- O envio teste gerou relatório `lk-weekly-influencer-sales-2026-05-09.*` e manteve Meta/Shopify read-only.

## 2026-05-10 — LK Weekly Influencer Sales Email + Mission Control

- Documentada e versionada a rotina `areas/lk/sub-areas/trafego-pago/rotinas/weekly-influencer-sales-email.md`.
- Adicionado script read-only `scripts/lk_weekly_influencer_sales_report.py` para gerar relatório semanal comparativo de influencers: últimos 7 dias completos vs 7 dias anteriores.
- O relatório separa Meta Ads canônico de Shopify com ponte textual verificável; produtos vendidos só são atribuídos com evidência Shopify, sempre com nome + SKU + variante/tamanho quando disponível.
- Registrado no PRD do Mission Control como módulo recorrente aprovado por Lucas, com cadência quarta-feira 10h BRT e entrega por e-mail.
- Produção, VPS/Docker, bancos, campanhas, Shopify/Tiny/Klaviyo/WhatsApp e runtime não foram alterados.

## 2026-05-10 — LK Influencer Audit corrigido: Meta canônico + criativos + produtos

- Gerado relatório read-only corrigido em `reports/lk-influencer-audit-corrected-2026-05-10/audit.md` e `.json`, com imagens dos criativos em `creative_images/`, contact sheet `top_creatives_contact_sheet.png` e versão vertical `top_creatives_contact_sheet_vertical.png`/`.html`.
- A versão vertical registra que criativos como Helena #4/#5/#8 podem compartilhar exatamente o mesmo asset visual, mas ter atribuições diferentes por estarem em anúncios/adsets/campanhas diferentes.
- Correção crítica: compras Meta agora usam uma única action key canônica por anúncio (`offsite_conversion.fb_pixel_purchase` preferencial), evitando triplicar `purchase + omni_purchase + offsite_conversion`.
- Influencers foram descobertos e normalizados por Meta direto (`campaign_name`, `adset_name`, `ad_name`), unificando campanhas repetidas como Silvia Henz/Silvia/variações.
- Produtos vendidos são atribuídos apenas quando existe ponte Shopify textual verificável (cupom, UTM/landing/referrer, note attributes, note ou tags); sem ponte, o relatório mantém o criativo como sinal Meta sem produto vendido atribuído.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-10 — LK Influencer Operational ROAS v0.2

- Criado `reports/lk-influencer-operational-roas-v02-2026-05-10.md` para separar Meta attributed ROAS, Shopify evidence revenue e ROAS operacional provisório por influencer.
- Atualizado `campaign-attribution-dictionary-seed-v0.md`: Silvia Heinz agora tem ROAS operacional provisório 12,93x; Helena Lunardelli 6,34x; Lala Noleto permanece `ambiguous_meta_signal_only` com zero evidência Shopify direta no recorte.
- Próxima ação segura: gerar tabela `influencer → produto/SKU/tamanho → estoque` começando por Silvia/Helena; Lala segue investigação de cupom/UTM/landing/brief real.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-10 — LK team routing matrix v0.1

- Atualizado `areas/lk/equipe/README.md` com matriz inicial de funções, destinatários, revisores e aprovações do LK Operating System.
- Matriz inclui Lucas, Renan, Júlio e Danilo, com roteamento por Daily Sales Brief, Pulso Comercial, Stock Intelligence, Supply & Sourcing, Paid/Influencer, Brand Mix, CRO, SEO, DesignMD, CRM, financeiro/fiscal e loja física.
- Regra preservada: enquanto Lucas não validar canais/cópias, todo output real segue primeiro para Lucas em preview; nenhum cron/envio recorrente deve assumir destinatários.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

Registro das principais mudanças estruturais do Hermes Brain após a adaptação Bruno/OpenClaw para o universo Hermes.

## 2026-05-10 — LK Influencer SKU Stock Matrix real v0.2

- Gerada matriz read-only `influencer → produto/SKU/tamanho → estoque` em `reports/lk-influencer-sku-stock-matrix-readonly-2026-05-10.md` e JSON correspondente.
- Silvia Heinz e Helena Lunardelli foram cruzadas com Shopify por cupom/UTM/landing/note e Tiny somente no depósito `LK | CONTROLE ESTOQUE`.
- Lala Noleto ficou classificada como investigação: há sinal forte em Meta, mas nenhum match Shopify por `lala`/`noleto` em cupom/UTM/landing/note no período; precisa de dicionário canônico de cupom/UTM/brief antes de virar recomendação de estoque.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-10 — LK Campaign Attribution Dictionary seed v0.1

- Criado `areas/lk/sub-areas/trafego-pago/contexto/campaign-attribution-dictionary-seed-v0.md` com a primeira versão preenchida/read-only do dicionário canônico.
- Seed inclui Silvia Heinz, Helena Lunardelli, Lala Noleto, Ju Mesquita, Mariah, Arlindo, Maria Fernanda e campanhas `[PD][FUNDO] ADV+`, `[PD] [FUNDO] RMKT`, `[Pareto] [FUNDO] DABA`, `Pareto.Vendas-Adv [ Geral]` e Jacquemus.
- O documento separa plataforma, evidência Shopify, produto/SKU/tamanho e consequência de estoque; mantém `operational_roas` como não calculável quando custo e receita ainda não estão amarrados por naming/UTM/cupom confiável.
- Próxima ação: confirmar handles/cupons/UTMs oficiais e aprofundar Lala Noleto, que tem sinal Meta forte mas zero evidência Shopify direta encontrada no recorte.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-10 — LK Campaign Attribution Dictionary

- Criada rotina read-only `areas/lk/sub-areas/trafego-pago/rotinas/campaign-attribution-dictionary.md` para mapear campanha/influencer → Meta/Google naming → UTM/cupom/landing → produto/SKU/tamanho → estoque.
- Criado template `areas/lk/sub-areas/trafego-pago/templates/campaign-attribution-record.md` para preencher o dicionário canônico por campanha/influencer.
- Atualizado PRD do LK Operating System para tratar `Meta attributed ROAS by campaign title` como sinal de plataforma até existir dicionário canônico e match Shopify/GA4 confiável.
- Próxima ação: preencher Lala Noleto, Silvia Heinz, Helena Lunardelli e campanhas broad/Advantage+/RMKT com evidência Shopify, GA4, cupom/UTM/landing e consequência de estoque.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-10 — LK Meta campaign-title ROAS read-only

- Gerado relatório read-only `reports/lk-meta-campaign-title-roas-readonly-2026-05-10.md`/`.json` calculando ROAS atribuído do Meta por `campaign_name`/título da campanha.
- O relatório separa `Meta attributed ROAS` por título de campanha de evidência operacional Shopify por `utm_campaign`; matching frouxo foi removido porque confundia campanhas genéricas com UTMs de campanha/influencer.
- Resultado reforça a correção anterior: campanhas broad/Advantage+/RMKT podem mostrar 60–90x no Meta, mas o match estrito Shopify por UTM aparece muito menor ou zerado quando o UTM/naming não bate.
- Próxima ação: criar dicionário `campaign_name Meta → utm_campaign Shopify/GA4 → criativo/influencer/produto esperado` antes de usar ROAS por título como decisão operacional.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-10 — LK ROAS influencer correction + Tiny alias approval preview

- Gerado relatório read-only `reports/lk-roas-influencer-correction-readonly-2026-05-10.md`/`.json` para investigar os ROAS Meta 50–70x de Lala Noleto, Helena Lunardelli e Silvia Heinz.
- Correção central: os 50–70x são `Meta attributed ROAS`, não ROAS operacional da LK; no período 2025-12-01 a 2026-05-10, o valor atribuído pelo Meta para a conta inteira excede a receita web Shopify do período, então não pode ser usado como verdade de receita.
- Site ROAS simples do período foi reconciliado como Shopify web / (Meta + Google via Metricool), separando receita Shopify de valor atribuído por plataforma.
- Gerado preview read-only `reports/lk-sku-tiny-alias-approval-preview-2026-05-10.md` com a tabela de aprovação para alias/correção Tiny dos SKUs priorizados; nenhum write em Tiny/Shopify foi executado.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-10 — LK SKU Shopify ↔ Tiny map preview

- Gerado preview read-only `reports/lk-sku-shopify-tiny-map-preview-2026-05-10.md`/`.json` para os campeões antes marcados como `mapear SKU no Tiny`.
- Incorporada correção de Lucas: tudo que está na Shopify deve existir no Tiny; produtos novos tendem a já estar linkados; divergência relevante tende a estar em produtos antigos/SKU legado ou método de busca insuficiente.
- Segunda busca no Tiny encontrou candidatos para 6/6 SKUs priorizados, todos com confiança alta, reforçando que a causa provável não era ausência no Tiny.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-10 — Correções LK SKU Shopify/Tiny e Meta influencer

- Registrada correção de Lucas: SKU canônico operacional é Shopify; Tiny deve ser aprendido/mapeado/normalizado para Shopify, nunca o contrário por automação.
- Corrigida a leitura Meta influencer do relatório `reports/lk-stock-influencer-audit-readonly-2026-05-10.md`: o recorte anterior de 30 dias subcontava Lala/Helena/Silvia; nova leitura read-only usa janela desde 2025-12-01 e nomes no nível de ad, com aviso de que ROAS de plataforma ainda não é ROAS final da LK.
- Atualizados PRD e template Stock Intelligence para exigir mapa SKU Shopify ↔ Tiny e preview humano antes de qualquer sugestão de correção no Tiny.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-10 — LK Stock Intelligence + Influencer/Product Audit real v0.1

- Gerado o primeiro relatório real agregado/read-only combinando Shopify vendas, Tiny `LK | CONTROLE ESTOQUE`, Brand Mix e auditoria influencer vs produto em `reports/lk-stock-influencer-audit-readonly-2026-05-10.md`.
- A auditoria começou a mapear o match influencer → produto/marca/modelo/tamanho, com exemplos explícitos para Lala Noleto, Silvia Heinz e Helena Lunardelli quando há evidência em Shopify/Meta.
- Registrada próxima ação: criar dicionário canônico de influencers, cupons, UTMs e patterns de campanhas/anúncios; corrigir vínculo SKU Shopify ↔ Tiny nos campeões sem saldo encontrado.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-10 — LK OS: stock, sourcing e influencer intelligence

- Refinado o PRD do LK Operating System com as correções de Lucas sobre busca externa acionada por sinal interno, Monbam, Droper, compra para repor estoque, encomenda BR/US como curadoria humana no pedido Shopify e pronta entrega por variante/tamanho.
- Reforçado que o Stock Intelligence Center deve comparar velocidade de venda, estoque Tiny `LK | CONTROLE ESTOQUE` e lead time para decidir se a compra precisa acontecer antes da ruptura.
- Reforçado o módulo Paid Traffic & Influencer Intelligence: Google Ads via Metricool, Meta Ads direto, Shopify/GA4 para reconciliação, e foco em qual influenciador/campanha move qual produto/marca/modelo/tamanho e consequência de estoque.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-09 — Paid Attribution LK real v0.3

- Salvo no Brain o primeiro relatório real agregado/read-only de atribuição paga/influencers em `reports/lk-paid-attribution-brief-real-2026-05-08-v03.md`.
- Cruzadas fontes read-only: GA4 source/medium/campaign, Shopify web sanitizado com landing/referrer/cupom/produtos e Meta Ads Insights por campanha/adset/ad.
- Atualizado template do Daily Sales Brief para incluir bloco de Pago, Influencers e Conteúdo com confiança de atribuição e produtos/marcas/tamanhos vendidos.
- Atualizada integração Meta Ads com regra de cautela: compras/ROAS da plataforma não são verdade operacional final; reconciliar com Shopify/GA4/UTM/cupom antes de recomendar escala ou pausa.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-09 — Daily Brief LK real v0.2 com GA4

- Salvo no Brain o primeiro Daily Brief real agregado/read-only com GA4 em `reports/lk-daily-sales-brief-real-2026-05-08-ga4-v02.md`.
- Atualizada integração Analytics/GA4/GSC com a service account LK em Doppler por nome de secret, sem valores sensíveis, e com propriedades LK acessíveis.
- Atualizado template do Daily Sales Brief para combinar Shopify como fonte oficial de pedidos/receita/source, Tiny somente `LK | CONTROLE ESTOQUE`, e GA4 para tráfego/canais/campanhas/CRO.
- Registrado no Learning Loop que Lucas aprovou o formato como “ficou bacana”; próxima evolução é atribuição paga/influencers por campanha/UTM/cupom cruzada com produto/marca vendido.
- Produção, VPS/Docker, bancos, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-09 — Exemplos read-only LK Operating System

- Criados exemplos fictícios/read-only para `Daily Sales Brief`, `Stock Intelligence Center` e `Weekly CEO Review` em `areas/lk/rotinas/templates/examples/`.
- Atualizados mapa LK e pendências para indicar que a próxima etapa é validar o formato com Lucas antes de primeira execução com dados reais mascarados.
- Os exemplos separam fato, leitura, recomendação, risco, dados faltantes e aprovação, sem representar venda real nem autorizar ação externa.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-09 — PRD LK Operating System

- Criado `areas/lk/projetos/lk-operating-system-prd.md` com PRD v0.1 aprovado conceitualmente por Lucas para o LK Operating System / LK Chief of Staff.
- Criado `empresa/gestao/hermes-learning-loop.md` como módulo global de aprovações, correções, padrões e anti-padrões para Hermes Brain, LK, Zipper, SPITI e Mission Control.
- Atualizados mapa/projetos LK, roadmap e pendências para indicar implementação faseada por templates/read-only antes de crons ou integrações de escrita.
- Produção, VPS/Docker, bancos, secrets, campanhas, WhatsApp/Klaviyo, Shopify/Tiny/Notion, Google/Meta, n8n, UI, cron e runtime não foram alterados.

## 2026-05-09 — Revisão operacional multiempresa

- Criada rotina `areas/operacoes/rotinas/revisao-operacional-multiempresa.md` para priorização sob demanda de LK, Zipper, SPITI e Operações usando apenas Brain versionado por padrão.
- Gerado `reports/revisao-operacional-multiempresa-2026-05-09.md` como primeira revisão executiva.
- Atualizados índices, roadmap e pendências para registrar uso sob demanda, sem cron recorrente e sem dados vivos/produção por padrão.
- Produção, VPS/Docker, bancos, secrets, campanhas, mensagens externas, UI, cron e runtime não foram alterados.

## 2026-05-09 — Script Retomada de Planos/PRDs

- Criado `scripts/retomada_planos_prds.py` para gerar relatório local/read-only de retomada de planos, PRDs e pendências.
- Gerados `reports/retomada-planos-prds-2026-05-09.md` e `reports/retomada-planos-prds-2026-05-09.json`.
- Atualizada a rotina `areas/operacoes/rotinas/retomada-planos-prds.md` com comando canônico, limites e critérios de uso.
- Avaliação: sem cron semanal por enquanto; usar sob demanda quando Lucas disser “seguir”, “retomar” ou “onde paramos”.
- Produção, VPS/Docker, bancos, secrets, campanhas, mensagens externas, UI, cron e runtime não foram alterados.

## 2026-05-09 — Script Brain Improvement Score

- Criado `scripts/brain_improvement_score.py` como ferramenta local/read-only para gerar relatório executivo do Brain em Markdown e JSON.
- Gerados `reports/brain-improvement-score-2026-05-09-script.md` e `reports/brain-improvement-score-2026-05-09-script.json`, consumindo o health check JSON e arquivos versionados do repo.
- Atualizada rotina `areas/operacoes/rotinas/brain-improvement-score.md` com comando canônico, limites e critérios de uso.
- Atualizados projeto, roadmap e pendências para retirar a avaliação do script da fila ativa.
- Produção, VPS/Docker, bancos, secrets, campanhas, mensagens externas, UI, cron e runtime não foram alterados.

## 2026-05-09 — Teste Material Ingest to PRD

- Testada a rotina `areas/operacoes/rotinas/material-ingest-to-prd.md` em modo leve usando o PRD antigo `areas/operacoes/projetos/mission-control-prd.md`.
- Criado relatório `reports/material-ingest-to-prd-test-2026-05-09.md` com fluxo aplicado, matriz resumida, decisão Hermes-native e lacunas.
- Atualizada a rotina para distinguir modo completo de ZIP/pacote e modo leve de documento único/PRD antigo.
- Atualizados pendências, roadmap, projeto e mapa de Operações.
- Produção, Docker/VPS, bancos, secrets, campanhas, mensagens externas, UI, cron e runtime não foram alterados.

## 2026-05-09 — Rodada G: Health checks versionados do Brain

- Expandido `scripts/brain_health_check.py` com checks de secrets, links/anchors markdown, arquivos estruturais obrigatórios, arquivos por agente, `MAPA.md` por área/subárea, rotinas indexadas e skills canônicas.
- Adicionada saída JSON opcional para relatórios: `--json reports/brain-health-check-YYYY-MM-DD.json`.
- Atualizada rotina `areas/operacoes/rotinas/brain-health-check.md` com critério `FAIL=0` e alvo `WARN=0` para PRs documentais autônomos.
- Gerado `reports/brain-health-check-2026-05-09.json` com `FAIL=0 WARN=0` em todos os checks.
- Rodada G removida da fila ativa de pendências e marcada como concluída no roadmap.
- Produção, Docker/VPS, bancos, secrets, campanhas, mensagens externas e runtime não foram alterados.


## 2026-05-09 — Higiene real de memória e pendências

- Aplicada a rotina `areas/operacoes/rotinas/memory-hygiene-pendencias.md` sobre `empresa/gestao/pendencias.md` e `memories/pending.md`.
- Reclassificadas pendências em ativos, bloqueados, aguardando data/evento, concluídos e arquivados.
- Removida contradição antiga que mantinha Meta Ads como urgente após a consolidação de 2026-04-28 registrar correção em 2026-04-25.
- Criado relatório `reports/memory-hygiene-2026-05-09.md` com fontes, critérios e reclassificação.
- Promovida para decisões permanentes a autorização de Lucas para merges autônomos em PRs documentais/Brain de baixo risco quando checks passarem, preservando aprovação explícita para produção, infra, secrets, banco, ações externas e risco destrutivo.
- Produção, Docker/VPS, bancos, secrets, campanhas, mensagens externas e runtime não foram alterados.

## 2026-05-09 — Guardrails P1 de memória, segurança e entrega

- Criada rotina `areas/operacoes/rotinas/memory-hygiene-pendencias.md` para separar pendências ativas, bloqueadas, aguardando, concluídas, arquivadas, decisões e lições.
- Criada rotina `areas/operacoes/rotinas/security-checkup.md` para revisão de secrets, scopes, prompt injection, integrações, canais, crons, produção e ações sensíveis.
- Criados templates `areas/operacoes/templates/nova-integracao.md`, `areas/operacoes/templates/novo-canal-agente.md` e `areas/operacoes/templates/delivery-summary.md`.
- Atualizados `areas/operacoes/MAPA.md`, `empresa/rotinas/_index.md`, projeto do Hermes Brain Improvement System e roadmap.
- Produção, Docker/VPS, bancos, secrets, campanhas, mensagens externas e runtime não foram alterados.

## 2026-05-09 — Instrumentos executivos Bruno P0

- Criada matriz `areas/operacoes/rotinas/area-skill-subagent-agent-decision.md` para decidir área, rotina, skill, subagent, cron ou agente/canal permanente.
- Criado PRD `areas/operacoes/projetos/mission-control-prd.md` para Mission Control Hermes read-only, separando o uso criativo/performance do protocolo operacional.
- Criado template `areas/operacoes/templates/report-health-executivo.md` para relatórios executivos de health, riscos, evidências e aprovações.
- Criado primeiro relatório manual `reports/brain-improvement-score-2026-05-09.md`, com score geral 88/100.
- Atualizados índices, roadmap e pendências relacionadas a Mission Control.
- Produção, Docker/VPS, bancos, secrets, campanhas, mensagens externas e runtime não foram alterados.

## 2026-05-08 — Hermes Brain Improvement System

- Adicionada rotina `areas/operacoes/rotinas/material-ingest-to-prd.md` para transformar material externo em extração segura, inventário, documentação, matriz de decisão e PRD.
- Adicionados templates `areas/operacoes/templates/matriz-decisao-bruno-hermes.md` e `areas/operacoes/templates/prd-hermes-brain-improvement.md`.
- Adicionadas rotinas `brain-improvement-score.md` e `retomada-planos-prds.md` para avaliação executiva do Brain e retomada de planos pausados.
- Criado projeto `areas/operacoes/projetos/hermes-brain-improvement-system.md` com backlog P0/P1/P2.
- Atualizados `areas/operacoes/MAPA.md`, `empresa/rotinas/_index.md` e `ROADMAP-30-DIAS-HERMES.md`.
- Produção, Docker/VPS, bancos, campanhas, mensagens externas e merge em `main` não foram alterados.

## 2026-05-05 — Hermes Docker atualizado para v0.12.0 com imagem custom

- Confirmado via GitHub API que a release upstream mais recente conhecida é `v2026.4.30` / `Hermes Agent v0.12.0 (2026.4.30)`.
- VPS `lc.vps` agora roda os dois containers Hermes com `hermes-agent-custom:v0.12.0-20260505`.
- Versão verificada nos dois containers via `/opt/hermes/.venv/bin/hermes --version`: `Hermes Agent v0.12.0 (2026.4.30)`, Python `3.13.5`, OpenAI SDK `2.32.0`.
- Corrigido pós-deploy o travamento de tools causado por `terminal.cwd: telegram`; valor correto preservado em `terminal.cwd: /opt/data`.
- Registrados backups/rollback: `docker-compose.yml.bak.20260503_191723`, `docker-compose.yml.pre-v012-20260505T102618Z` e `data/config.yaml.bak-20260505-cwd-telegram`.
- Documentado checklist para próximos updates: preservar Compose/config, validar `terminal.cwd`, permissões de logs/sessions, versão real, gateway Telegram, cron ticker e tool call.
- Segredos não foram documentados; senha root enviada em chat deve ser tratada como exposta e rotacionada depois.

## 2026-05-05 — Hermes Docker: pull/update seguro executado, imagem sem versão nova

- Lucas autorizou reset da senha root da `lc.vps` via Hostinger e backup/update do Hermes Docker.
- Nova senha root foi gerada e salva no Doppler `VPS_ROOT_PASSWORD`, sem documentar valor.
- Backup leve coletado fora do repo: `/opt/data/hermes_bruno_ingest/backups/lc-vps-hermes-20260505T011529Z`.
- Criada rollback tag: `ghcr.io/hostinger/hvps-hermes-agent:preupdate-20260505T011613Z`.
- Executado `docker compose pull` e `docker compose up -d --no-deps` apenas para `hermes-agent` e `hermes-telegram`.
- Digest da imagem Hostinger `latest` permaneceu `sha256:7fc18af3c7a124b00b8853218cf59296861101d65d6af1dc9d7851277829d6b7`; versão segue `Hermes Agent v0.9.0 (2026.4.13)`.
- Confirmado por GitHub API que upstream `NousResearch/hermes-agent` latest segue `v2026.4.30` / `Hermes Agent v0.12.0 (2026.4.30)`; imagem Hostinger não avançou para essa versão no pull.
- Investigação GHCR read-only confirmou tags públicas Hostinger disponíveis (`latest`, `8eb9eb9`, `ba03513` e aliases sha256); `latest` é alias de `8eb9eb9`, digest atual, e `ba03513` é anterior — não há tag pública Hostinger mais nova nesta data.
- Documentado registro completo em `areas/operacoes/rotinas/hermes-runtime-update-attempt-2026-05-05.md`.
- Traefik, n8n, Paperclip, volumes, redes, firewall, Supabase, Vercel, campanhas e mensagens externas não foram alterados.

## 2026-05-05 — Spiti Hub: PR #92 bundle/code splitting mergeado em dev

- Criado e mergeado em `dev` o PR #92: `https://github.com/spiti-auction/spiti-hub/pull/92`.
- Merge commit: `2943614 perf: split route and pdf bundles (#92)`.
- Implementado code splitting de rotas com `React.lazy`/`Suspense` e `manualChunks` para dependências pesadas de PDF/Recharts.
- Warning de chunks Vite acima de 500 kB eliminado sem elevar `chunkSizeWarningLimit`; maiores chunks pós-build ficaram abaixo de 500 kB.
- Verificações locais: `git diff --check` OK, secret scan 0, lint 0 errors/0 warnings, build OK sem warning de chunk grande.
- Revisão independente pré-commit aprovada; sugestões futuras não bloqueantes: ErrorBoundary para falhas de chunk e monitoramento de requests após split granular.
- Produção/`main`, Supabase, Vercel configs, VPS, Docker, campanhas e mensagens externas não foram alterados.

## 2026-05-04 — Spiti Hub: PR #91 mergeado em dev

- Criado e mergeado em `dev` o PR #91: `https://github.com/spiti-auction/spiti-hub/pull/91`.
- Merge commit: `e8d4de4 chore: resolve hook and fast refresh lint warnings (#91)`.
- Warnings de lint reduziram de 8 para 0, mantendo 0 errors.
- Verificações locais: `git diff --check` OK, secret scan 0, lint 0 errors/0 warnings, build OK.
- Registrado aviso Vercel bot: preview/deploy pode falhar porque `@hermes-agent` não é membro do time Vercel da `spiti-auction`; nenhuma alteração em Vercel/team/billing/settings foi feita.
- Produção/`main`, Supabase, Vercel configs, VPS, Docker, campanhas e mensagens externas não foram alterados.

## 2026-05-04 — Spiti Hub: PR #90 mergeado em dev

- Criado e mergeado em `dev` o PR #90: `https://github.com/spiti-auction/spiti-hub/pull/90`.
- Merge commit: `49b5c84 chore: remove unused lint warnings (#90)`.
- Warnings de lint reduziram de 39 para 8, mantendo 0 errors.
- Verificações locais: `git diff --check` OK, secret scan 0, lint 0 errors/8 warnings, build OK.
- Os 8 warnings restantes foram preservados para rodada própria porque envolvem hooks/Fast Refresh.
- Produção/`main`, Supabase, Vercel configs, VPS, Docker, campanhas e mensagens externas não foram alterados.

## 2026-05-04 — Spiti Hub: PR #89 mergeado em dev

- PR #89 (`chore: redact edge function secret examples`) foi squash-mergeado em `dev` do `spiti-auction/spiti-hub`.
- Merge commit: `ae625a2 chore: redact edge function secret examples (#89)`.
- Branch `hermes/spiti-hub-secrets-lint-hardening` removida após merge.
- Clone local sincronizado em `dev...origin/dev`.
- Produção/`main`, Supabase, Vercel configs, VPS, Docker, campanhas e mensagens externas não foram alterados.

## 2026-05-04 — Spiti Hub: PR de hardening aberto

- Clonado `spiti-auction/spiti-hub` via Git usando `GITHUB_SPITI_HUB_TOKEN` sem embutir token no remote.
- Criada branch `hermes/spiti-hub-secrets-lint-hardening` a partir de `dev`.
- Commit no Spiti Hub: `8c8549b chore: redact edge function secret examples`.
- Aberto PR #89 para `dev`: `https://github.com/spiti-auction/spiti-hub/pull/89`.
- Verificações locais: `git diff --check` OK, secret scan 0, lint 0 errors/39 warnings, build OK.
- Nenhum merge ou alteração em produção foi executado.

## 2026-05-04 — Spiti Hub: token salvo no Doppler

- Salvo no Doppler `lc-keys/prd` o secret `GITHUB_SPITI_HUB_TOKEN` para acesso ao repo privado `spiti-auction/spiti-hub`.
- Verificação segura confirmou acesso ao repo com permissões administrativas/push sem imprimir o token.
- Atualizados docs de integração GitHub e contexto SPITI Hub com o nome do secret, sem valor.
- Como o token foi enviado por chat, segue recomendado rotacionar/revogar depois da sequência de PR e substituir no Doppler.

## 2026-05-04 — Spiti Hub: hardening local sem push

- Redigida localmente a cópia de `docs/deploy-edge-functions.md` do Spiti Hub para substituir assignments secret-like de Google OAuth/refresh token por placeholders.
- Rodado `eslint --fix` localmente, reduzindo warnings de lint de 46 para 39, com 0 errors.
- Build local segue OK; warning de bundle grande permanece.
- Secret scan local pós-redação retornou 0 achados nos padrões verificados.
- Nenhum push/PR no Spiti Hub foi feito: token válido para `spiti-auction/spiti-hub` ainda precisa ser colocado em Doppler; PAT colado em chat deve ser rotacionado/revogado.

## 2026-05-04 — Rodada E: inventário GitHub do Spiti Hub

- Confirmado acesso ao repo privado `spiti-auction/spiti-hub`, projeto operacional novo da SPITI.
- Criado `areas/spiti/contexto/spiti-hub-github.md` com inventário inicial, relação com o Hermes Brain, regras de segurança e próximos passos.
- Atualizados `areas/spiti/MAPA.md`, `empresa/integracoes/github.md` e roadmap.
- Verificações locais do Spiti Hub: install OK, lint OK com warnings, build OK.
- Nenhuma alteração foi feita em GitHub remoto, Supabase, Vercel, VPS, Docker, campanhas ou mensagens externas.
- Token GitHub enviado por chat não foi documentado; recomendada migração para Doppler e rotação/revogação depois.

## 2026-05-04 — Rodada D: templates Zipper por subárea

- Criados templates Zipper para consulta read-only de `vendas_tango`, registro pós-contato com colecionador, checklist de feira por fase e briefing de publicação obra/artista.
- Atualizados mapas das subáreas Zipper, mapa principal, índice de rotinas e roadmap.
- Preservadas regras de separação Zipper Vendas vs SPITI, tom Zipper e aprovação Lucas/Osmar antes de contato, negociação, proposta ou publicação externa.
- Fase documental segura: nenhuma consulta/alteração em produção, Docker, VPS, banco, campanhas ou mensagens externas.

## 2026-05-04 — Rodada C: playbooks operacionais LK/Zipper/SPITI

- Criados playbooks LK para comando diário e campanha CRM aprovada.
- Criados playbooks Zipper para abordagem obra/colecionador e execução de feira.
- Criados playbooks SPITI para pregão ao vivo e divergência de lances.
- Atualizados mapas de áreas, índice de rotinas e roadmap.
- Fase documental segura: nenhuma consulta/alteração em produção, Docker, VPS, campanhas ou mensagens externas.

## 2026-05-04 — Diagnóstico read-only do Hermes Gateway

- Executado diagnóstico read-only do Gateway/Telegram na VPS sem restart, kill, update, alteração de env/compose ou mudança Docker/root.
- Criado `areas/operacoes/rotinas/hermes-gateway-readonly-diagnostic-2026-05-04.md` com evidências e classificação H1/H2/H3/H4.
- Atualizados observabilidade, plano de remediação, roadmap e índice de rotinas.
- Conclusão operacional: detector de gateway em Docker foreground provavelmente diverge do processo real; conflito Telegram parece histórico/transitório no momento da coleta.

## 2026-05-04 — Planos seguros para Gateway e update Hermes

Commit: `docs: add Hermes gateway and runtime update plans`

Entregas:

- Criado plano de diagnóstico/correção segura do gateway Telegram, separando hipóteses, evidências, escopo read-only, ações bloqueadas e critérios de sucesso.
- Criado plano de update do runtime Hermes `v0.9.0` → `v0.12.0` com pré-condições, backup, rollback e validações pós-update.
- Atualizado índice de rotinas e roadmap para deixar claro que correção/update exigem aprovação Lucas antes de qualquer alteração em Docker/VPS/root.
- Corrigida orientação antiga de troubleshooting rápido que sugeria restart via `systemctl`; no footprint atual Hermes roda em Docker/Hostinger e restart é ação sensível.

## 2026-05-04 — Observabilidade Hermes runtime/gateway

Commit: `docs: add Hermes runtime observability routine`

Entregas:

- Documentada rotina read-only para observar versão, containers, gateway, cron interno e logs do Hermes na VPS.
- Registrado gap entre runtime Hostinger observado (`Hermes Agent v0.9.0`) e release upstream (`Hermes Agent v0.12.0`, `v2026.4.30`).
- Registrada divergência operacional: processo `hermes gateway run` existe no container Telegram, mas `hermes cron status` reporta gateway não running.
- Registrado warning de conflito de polling Telegram sem aplicar restart, update ou alteração em Docker/VPS/root.
- Atualizados `areas/tecnologia/contexto/hermes-docker-footprint.md`, `areas/operacoes/rotinas/hermes-release-watch.md`, `empresa/rotinas/_index.md` e roadmap.

## 2026-05-04 — Integrações por ferramenta e rotinas seguras

Commit: `docs: deepen integration operating routines`

Entregas:

- Corrigido troubleshooting genérico de Supabase em `TOOLS.md` para apontar nomes específicos por base.
- Validado que os nomes reais de secrets das integrações críticas existem no Doppler, sem imprimir valores.
- Criadas rotinas operacionais para validação de secrets, Shopify read-only, Supabase audit, Evolution/WhatsApp approval, Klaviyo approval, Meta Ads reporting e Hostinger/VPS inventory.
- Atualizados `empresa/integracoes/MAPA.md`, `empresa/rotinas/_index.md` e roadmap com o estado da Rodada B.

## 2026-05-04 — Manual operacional do Brain

Commit: `65a3cfa docs: add Hermes Brain operating manual`

Entregas:

- Criado `START-HERE.md` como manual operacional de entrada.
- Atualizado `README.md` para apontar primeiro para `START-HERE.md`.
- Documentada a ordem de navegação: regras globais → memórias → empresa → áreas → agentes → skills/rotinas → segurança.
- Documentados procedimentos por tipo de tarefa: pergunta de negócio, comunicação externa, automação, skill, bug e credenciais.

## 2026-05-04 — Segurança e permissões por área

Commit: `86d9097 docs: align security permissions with Hermes areas`

Entregas:

- Expandido `seguranca/permissoes.md`.
- Expandido `seguranca/acoes-sensiveis.md`.
- Criado modelo de níveis L0-L5 para ações sensíveis.
- Documentados limites por agente e por negócio.
- Reforçado Doppler `lc-keys/prd` como fonte de verdade de credenciais.
- Reforçada aprovação Lucas para ações externas, produção, dados e credenciais.

## 2026-05-04 — Índices executivos globais

Commit: `9fdaa96 docs: add executive Brain navigation indices`

Entregas:

- Corrigido `README.md` para identificar o repo como Hermes Brain real, não draft.
- Expandido `areas/MAPA.md` com índice executivo de áreas e sub-áreas.
- Expandido `empresa/MAPA.md` com mapa cross-área.
- Criado `empresa/rotinas/_index.md`.
- Criado `empresa/skills/_index.md`.

## 2026-05-04 — Zipper e SPITI operacionalizados

Commit: `6753205 docs: map Zipper and SPITI operating routines`

Entregas:

- Expandido `areas/zipper/MAPA.md`.
- Expandido Zipper em sub-áreas: vendas de obras, colecionadores, feiras e comunicação.
- Criadas rotinas Zipper: consulta de vendas, abordagem de colecionadores e planejamento de feiras.
- Expandido `areas/spiti/MAPA.md`.
- Criadas rotinas SPITI: verificação de lances, alerta de lances e relatório de leilão.
- Reforçada separação Zipper Vendas vs SPITI.
- Reforçada regra SPITI: email é fonte de verdade para lances; meta tag não é lance atual.

## 2026-05-04 — LK CRM, skills e rotinas

Commit: `f08d2b9 docs: map LK CRM routines and skills`

Entregas:

- Expandido `areas/lk/MAPA.md`.
- Expandido `areas/lk/sub-areas/crm/MAPA.md`.
- Criada navegação de área para skills LK cross-sell e leads esfriando.
- Documentadas rotinas LK: RFM semanal, outcomes tracker, consequence tracker e sync log.

## 2026-05-04 — Remediação de secrets versionados

Commit: `bcab06f fix: remove hardcoded secrets from Hermes Brain`

Entregas:

- Redigidos token-like values em docs/memórias.
- Scripts passaram a buscar credenciais por ambiente/Doppler.
- Adicionados erros explícitos quando env vars obrigatórias estão ausentes.
- Scan de secrets retornou `possible_secrets 0` antes do push.

Observação de segurança:

- Tokens que apareceram em chat/log/repo devem ser rotacionados/revogados quando a sequência operacional terminar.

## 2026-05-04 — Padronização de agentes

Commit: `eff6287 docs: standardize Hermes Geral LK and Zipper agent docs`

Entregas:

- Padronizados documentos de agentes Hermes Geral, LK e Zipper.
- Preservadas identidades/regras ricas existentes.
- Adicionados docs de ferramentas, usuário, memória e heartbeat.

## 2026-05-04 — Estrutura Bruno/OpenClaw adaptada ao Hermes

Commit: `fb61b2a docs: adapt Bruno OpenClaw structure for Hermes Brain (#1)`

Entregas:

- Estrutura de áreas, empresa, segurança e agentes aplicada ao repo real.
- `memories/` preservado como memória executiva compacta.
- Adicionada arquitetura compatível com Bruno/OpenClaw, mas filtrada pela lógica Hermes.

## Estado atual

A adaptação estrutural base está aplicada em `main`.

O Brain agora tem:

- manual de entrada;
- README correto;
- índices executivos;
- áreas e sub-áreas por negócio;
- rotinas documentadas;
- skills indexadas;
- agentes padronizados;
- permissões e ações sensíveis;
- scan de secrets limpo na última rodada.
