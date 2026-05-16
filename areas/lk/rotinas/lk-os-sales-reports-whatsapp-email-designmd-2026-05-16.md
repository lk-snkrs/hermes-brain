# LK OS — Relatórios de venda por WhatsApp + e-mail DesignMD — 2026-05-16

## Origem

Lucas pediu por áudio, após confirmação de STT restaurado, para estruturar os relatórios recorrentes de venda da LK OS. A transcrição usou “relatórios de vergonha”, mas pelo conteúdo o escopo correto é **relatórios de venda**.

## Objetivo

Criar uma camada de reports executivos recorrentes da LK OS que consolide vendas do e-commerce e da loja física, com entrega em dois formatos:

- **WhatsApp:** resumo curto, acionável e legível no celular.
- **E-mail:** versão visual completa usando o padrão **DesignMD / Klaviyo-like** da LK, nunca um HTML genérico.

## Guardrail permanente

Enquanto destinatários, contas de envio e cópia final não estiverem aprovados no turno atual:

- permitido: gerar dados, HTML, preview, arquivos locais, documentação e drafts internos;
- bloqueado: envio real por WhatsApp, envio real por e-mail, criação de campanha, contato com cliente/fornecedor, alteração Shopify/Tiny/Meta/Google/Klaviyo.

A entrega externa só pode ser ativada depois de um preview aprovado por Lucas com canal, destinatários, assunto/copy e cadência.

## Reports solicitados

### LK-SALES-001 — Report da manhã: vendas do dia anterior

- **Horário desejado:** manhã. Padrão proposto: 08:00 BRT, alinhado ao Daily Sales Brief existente.
- **Janela:** dia fechado anterior, 00:00–23:59 BRT.
- **Escopo:** total LK, separando e-commerce e loja física.
- **Conteúdo mínimo:**
  - faturamento total;
  - número de pedidos/vendas;
  - ticket médio;
  - quebra por ponto de venda: online/e-commerce vs loja física/POS;
  - produto mais vendido;
  - marca mais vendida;
  - tamanho/SKU mais vendido quando confiável;
  - cupons/canais relevantes quando disponível;
  - alertas P0/P1: ruptura, SKU sem Tiny, discrepância forte, queda ou outlier;
  - “o que fazer hoje”: 3 decisões ou ações sugeridas.
- **Comparativo semana contra semana:** incluir somente quando a semana anterior estiver fechada ou quando houver janela comparável completa. Não misturar semana parcial com semana fechada sem rotular claramente.

### LK-SALES-002 — Pulso financeiro/comercial das 16h

- **Horário desejado:** 16:00 BRT.
- **Janela:** dia corrente até 16:00 BRT.
- **Formato:** breve, mais operacional.
- **Conteúdo mínimo:**
  - vendido até agora: total, online, loja;
  - quantidade de pedidos/vendas;
  - principais produtos/marcas vendidos;
  - o que ainda não vendeu ou está abaixo do esperado;
  - comparação com média/mesmo horário quando houver baseline confiável;
  - riscos para bater a meta do dia;
  - recomendação curta para equipe/gestão, sem disparar campanha automaticamente.

### LK-SALES-003 — Fechamento loja física 19h30

- **Horário desejado:** 19:30 BRT.
- **Janela:** dia corrente até 19:30 BRT, focado em loja física/POS.
- **Escopo:** somente loja física, separado do e-commerce.
- **Conteúdo mínimo:**
  - faturamento da loja;
  - número de vendas;
  - ticket médio loja;
  - vendedor por venda/faturamento, se a fonte fornecer esse campo com confiança;
  - marcas vendidas;
  - produtos/tamanhos vendidos;
  - itens sem giro relevante;
  - observações para o dia seguinte.

## Fonte de dados proposta

### Já existente / aproveitável

- Shopify Admin Orders: vendas online e POS quando registradas como `source_name`/tags de POS.
- Tiny ERP: sanity de estoque e SKUs vendidos.
- GA4/GSC/Meta/Metricool: sinais contextuais para reports maiores, não fonte primária de faturamento.
- Scripts existentes:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_os_daily_sales_brief_20260511.py`
  - `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_os_weekly_ceo_review_20260511.py`
  - `/opt/data/scripts/lk_daily_sales_brief_watchdog.py`
  - `/opt/data/scripts/lk_weekly_ceo_review_watchdog.py`

### Gap a validar antes de ativar 19h30

O pedido “vendedor vendeu quanto” depende de fonte confiável de vendedor/colaborador no POS. O script atual de Shopify não busca campos de staff/vendedor; ele só classifica online vs POS por `source_name`/tags. Próximo passo seguro é investigar read-only se os pedidos POS expõem:

- staff/user/cashier via Shopify Admin API;
- tags/metafields com vendedor;
- app/POS note attributes;
- Tiny/Nuvem/loja como fonte alternativa.

Sem esse campo, o report 19h30 deve mostrar loja física total e marcar vendedor como `needs_data`, não inventar atribuição.

## Padrão de saída

### WhatsApp

- Curto, sem tabela pesada.
- Máximo recomendado: 12–18 linhas.
- Começar com status: `🟢`, `🟡` ou `🔴`.
- Sempre separar `Total LK`, `Online` e `Loja` quando aplicável.
- Nunca incluir PII de cliente.

### E-mail DesignMD / Klaviyo-like

- Usar `areas/lk/design/DESIGN.md` como contrato visual.
- HTML de e-mail deve ser table-based, CSS inline, sem CSS externo, sem `file://`, sem tokens em URL.
- Visual precisa parecer LK/Klaviyo, não dashboard genérico.
- Antes de produção, enviar preview/teste para Lucas e validar renderização real no Gmail/mobile.
- Assunto sugerido:
  - Manhã: `LK OS — Vendas de ontem — DD/MM`
  - Pulso 16h: `LK OS — Pulso comercial 16h — DD/MM`
  - Loja 19h30: `LK OS — Fechamento loja — DD/MM`

## Cadências e canais propostos

- 08:00 BRT — WhatsApp + e-mail, diário.
- 16:00 BRT — WhatsApp + e-mail curto, diário.
- 19:30 BRT — WhatsApp + e-mail, diário, focado loja física.
- Segunda 09:00 BRT — bloco semana contra semana dentro do report semanal ou anexo ao report da manhã.

## Relação com automações existentes

Já existem crons de Daily e Weekly obrigatórios entregues no Telegram/origin:

- `LK Daily Sales Brief read-only mandatory delivery` — 08:00 BRT.
- `LK Weekly CEO Review read-only mandatory delivery` — segunda 09:00 BRT.

Estes crons **não são ainda** WhatsApp/e-mail DesignMD. Eles devem ser tratados como base de dados/roteiro, não como a entrega final solicitada.

## Plano seguro de implementação

### Fase 1 — Read-only/protótipo local

1. Reusar funções de Shopify/Tiny dos scripts Daily/Weekly.
2. Criar gerador único para `morning`, `pulse_16h`, `store_1930`.
3. Produzir três artefatos por report:
   - JSON canônico;
   - texto WhatsApp preview;
   - HTML e-mail DesignMD preview.
4. Rodar secret scan e validação de MIME/HTML local.
5. Não enviar nada externo.

### Fase 2 — Validação de fonte POS/vendedor

1. Consultar pedidos POS read-only com campos adicionais seguros.
2. Verificar se `vendedor` existe de forma confiável.
3. Se não existir, documentar alternativa ou campo necessário no POS/loja.

### Fase 3 — Aprovação visual e de destinatários

Lucas aprova:

- destinatários de WhatsApp;
- destinatários de e-mail;
- conta remetente;
- assunto/copy;
- visual HTML no Gmail/mobile;
- se WhatsApp será resumo simples ou arquivo/link.

### Fase 4 — Ativação cron

Somente após aprovação explícita:

- criar crons `no_agent` com stdout silencioso/alerta apropriado;
- primeiro rodar por 3 dias em modo preview para Telegram/origin;
- depois liberar entrega externa se Lucas aprovar novamente a versão final.

## Riscos

- **Envio externo sem aprovação:** mitigado por preview-only até aprovação atual.
- **Atribuição errada de vendedor:** bloquear campo como `needs_data` até fonte POS confiável.
- **E-mail renderizar como dashboard genérico:** usar DesignMD real da LK e validar no cliente de e-mail.
- **Semana parcial enviesada:** rotular comparativos; só comparar janelas equivalentes.
- **Duplicar report Daily existente:** consolidar Daily antigo como base e não criar redundância sem mapear sobreposição.

## Próxima execução recomendada

1. Construir protótipo local dos três reports sem envio.
2. Investigar vendedor/POS read-only.
3. Gerar um preview real de hoje/ontem para Lucas aprovar formato.
4. Só depois pedir aprovação para WhatsApp/e-mail real.

## Status

- Documento criado: 2026-05-16.
- Estado: `design_aprovado_por_intenção`, `execução_externa_bloqueada`, `protótipo_local_próximo`.
- Ação externa executada: nenhuma.
