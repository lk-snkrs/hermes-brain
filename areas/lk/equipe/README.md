# Equipe LK — matriz inicial de funções e roteamento

Status: v0.1 documental/read-only, criada em 2026-05-10. Precisa de validação de Lucas antes de qualquer cron, envio recorrente, grupo, e-mail, WhatsApp, Notion ou automação.

## Objetivo

Definir quem deve receber, revisar ou aprovar cada tipo de relatório e alerta do LK Operating System.

Regra central:

> Enquanto esta matriz não for confirmada, todo output real do LK OS deve ir primeiro para Lucas em modo preview. Nenhum cron/envio recorrente deve assumir destinatários automaticamente.

## Pessoas conhecidas

### Lucas Cimino

- Papel: dono/aprovador final da LK e principal usuário do LK OS.
- Recebe: briefs executivos, decisões de estoque, mídia, CRM, SEO, campanhas, produto, compras, pricing, tecnologia e exceções.
- Aprova obrigatoriamente: campanha, WhatsApp, Klaviyo, compra/recompra, contato externo, Notion produtivo, preço, estoque, Shopify, tema, publicação, mídia paga, cron recorrente, banco/API, n8n e infra.
- Canal default enquanto a matriz não for validada: Telegram DM.

### Renan

- Funções confirmadas: comunicação, conteúdo, newsletter, design e SEO.
- Dono operacional: produção de conteúdo LK, incluindo newsletter, blog, pauta orgânica, copy/visual de campanhas, criativos e materiais de SEO/GEO.
- Recebe/revisa: relatórios de design, conteúdo visual, DesignMD, SEO, blog, organic search, PDP visual, peças Klaviyo/WhatsApp/Instagram quando o assunto for layout/copy/visual.
- Autonomia aprovada por Lucas: Renan pode aprovar e enviar conteúdos/newsletters via Klaviyo no escopo de conteúdo da LK, usando preview, Brain e documentação do que foi feito.
- Fluxo recomendado: trabalhar dentro do `lk-growth`/Growth OS para usar Brain, dados e docs da LK; Renan pode falar direto com o bot LK Growth no Telegram DM, sem necessidade de grupo; registrar pauta, fontes, briefing, versão final, data, canal, aprovação/envio e resultado esperado no Brain antes/depois da publicação.
- Não assumir sem confirmação: vendas, estoque, compras, financeiro, campanha paga, WhatsApp operacional, preço, Shopify/theme/produto ou publicações fora de Klaviyo/conteúdo.
- Contato registrado no Brain: ver `memories/lk.md`; não duplicar dados de contato nesta matriz.

### Júlio

- Funções registradas em `memories/lk.md`: financeiro e fiscal.
- Recebe/revisa: relatórios fiscais/financeiros, divergências de nota, pagamento, conciliação, Tiny/ERP quando o assunto for fiscal/financeiro.
- Não assumir sem confirmação: aprovação comercial, compra de produto, campanha, estoque, SEO, design ou CRM.

### Danilo

- Funções registradas em `memories/lk.md`: vendas e curadoria.
- Recebe/revisa: sinais de venda/curadoria, dúvidas de produto, fit de compra, loja física, oportunidade de produto, demanda por tamanho/modelo e contexto comercial do cliente.
- Não assumir sem confirmação: financeiro/fiscal, design/SEO, alteração de campanha paga, alteração Shopify/Tiny, aprovação final.

## Matriz por módulo/relatório

### Daily Sales Brief 07h

- Objetivo: visão executiva diária de vendas, online/físico, conversão, produtos, estoque, canais e aprovações.
- Destinatário principal v0.1: Lucas.
- Cópias sugeridas após validação:
  - Danilo: bloco de produtos vendidos, loja física, curadoria e oportunidades comerciais.
  - Júlio: somente se houver bloco financeiro/fiscal/conciliação.
  - Renan: somente se houver bloco SEO/conteúdo/design/campanha visual.
- Canal default v0.1: Telegram para Lucas; cópias aguardam validação.
- Frequência sugerida: diário 07h, mas cron ainda não aprovado.
- Aprovação antes de envio externo: sim, se sair do preview para equipe/grupo.

### Pulso Comercial 16h

- Objetivo: sinais de curto prazo, oportunidades do dia, gargalos, produtos com tração e ações sugeridas.
- Destinatário principal v0.1: Lucas.
- Cópias sugeridas após validação: Danilo para leitura comercial/loja/curadoria; Renan se houver conteúdo/campanha; Júlio apenas se houver fiscal/financeiro.
- Canal default v0.1: Telegram Lucas.
- Frequência sugerida: diário 16h, mas cron ainda não aprovado.
- Aprovação: qualquer ação externa derivada exige Lucas.

### Stock Intelligence Center

- Objetivo: prever ruptura, compra antes de acabar, estoque alto/lento, lead time e sourcing por sinal interno.
- Destinatário principal v0.1: Lucas.
- Revisor sugerido: Danilo para curadoria/produto/fit de compra.
- Cópia condicional: Júlio quando envolver Tiny/ERP/fiscal ou preço de compra; Renan quando a recomendação for conteúdo/campanha para desovar ou acelerar produto.
- Canal default v0.1: Telegram Lucas.
- Destino operacional aprovado futuramente: grupo de compras/Monbam/Droper/WhatsApp somente depois de preview e aprovação.
- Aprovação: compra, recompra, contato com fornecedor/revendedor, mensagem em grupo e Notion produtivo exigem Lucas.

### Supply & Sourcing

- Objetivo: transformar sinal interno de venda/ruptura/restock em checagem de fonte Brasil/fora/pessoa/revendedor.
- Destinatário principal v0.1: Lucas.
- Revisor sugerido: Danilo.
- Cópia condicional: Júlio se houver risco fiscal/financeiro; Renan se virar pauta de conteúdo.
- Canal default: preview Telegram Lucas.
- Ação bloqueada sem aprovação: comprar, reservar, mandar WhatsApp, acionar Monbam/grupo, contatar revendedor, criar Notion produtivo.

### Paid Traffic & Influencer Intelligence

- Objetivo: cruzar Meta/Google/GA4/Shopify/UTM/cupom/produto/tamanho/estoque para entender qual influencer/campanha vendeu qual produto.
- Destinatário principal v0.1: Lucas.
- Revisor sugerido: Renan quando envolver criativo/copy/design/SEO/conteúdo; Danilo quando envolver produto/curadoria/estoque; Júlio somente quando envolver custo/financeiro.
- Canal default: Telegram Lucas.
- Aprovação: qualquer alteração de verba, campanha, criativo publicado, público, orçamento ou mensagem externa exige Lucas.

### Brand Mix Intelligence

- Objetivo: share over time por marca/modelo, tendência, concentração e impacto de estoque/campanha.
- Destinatário principal v0.1: Lucas.
- Cópias sugeridas: Danilo para curadoria/compras; Renan quando virar conteúdo/SEO/campanha; Júlio apenas se houver leitura financeira/fiscal.
- Canal default: Telegram Lucas.
- Aprovação: compra, mudança de mix, campanha ou sourcing real exigem Lucas.

### CRO / Conversão Shopify Analytics

- Objetivo: aumentar conversão online de 0,13% para 0,20%.
- Destinatário principal v0.1: Lucas.
- Revisor sugerido: Renan para design/SEO/PDP/conteúdo visual; Danilo se hipótese envolver produto/preço/curadoria; Júlio apenas se houver impacto financeiro/fiscal.
- Canal default: Telegram Lucas + HTML visual quando for layout/PDP.
- Aprovação: alteração Shopify, tema, preço, PDP publicado, app, checkout, campanha ou experimento em produção exige Lucas.

### SEO / Blog / Organic Search / GSC

- Objetivo: crescimento orgânico, páginas, blog, busca e conteúdo com DesignMD LK.
- Destinatário principal sugerido: Renan.
- Aprovador final: Lucas.
- Cópia: Lucas sempre em decisões estratégicas; Danilo se pauta depender de curadoria/produto; Júlio não entra por padrão.
- Canal default: preview para Lucas; após validação, Renan pode receber relatório operacional.
- Aprovação: publicar blog, alterar página/produto/SEO em Shopify, disparar conteúdo ou briefing externo exige Lucas.

### DesignMD / PDP / Visual / Klaviyo visual

- Objetivo: manter consistência estética da LK em PDP, newsletter, WhatsApp visual, Instagram e previews.
- Destinatário principal sugerido: Renan.
- Aprovador final: Lucas.
- Formato obrigatório: HTML visual para aprovação de layout, não só Markdown.
- Aprovação: nenhum layout vira cliente/Shopify/Klaviyo/WhatsApp sem Lucas.

### CRM / RFM / Recompra / Klaviyo / WhatsApp

- Objetivo: aumentar recompra em 50%, usando janela de 90 dias, clientes recorrentes e receita recorrente.
- Destinatário principal v0.1: Lucas.
- Cópias sugeridas: Renan quando envolver copy/layout; Danilo quando envolver abordagem 1:1/loja/produto; Júlio apenas se houver fiscal/financeiro.
- Canal default: preview Telegram Lucas.
- Aprovação: segmentação pode ser preparada read-only; envio Klaviyo/WhatsApp/campanha/fluxo exige Lucas.

### Financeiro / Fiscal / Tiny/ERP sensível

- Objetivo: tratar conciliação, fiscal, preço de compra, nota, Tiny/ERP financeiro e divergências.
- Destinatário/revisor sugerido: Júlio.
- Aprovador final: Lucas quando impactar decisão comercial, compra, preço, margem, sistema ou banco.
- Canal default: preview Lucas; Júlio após validação.
- Aprovação: qualquer write no Tiny/ERP/banco/Notion produtivo exige Lucas.

### Loja física / Atendimento / WhatsApp 1:1

- Objetivo: inteligência de atendimento, loja física, cliente e oportunidade 1:1.
- Destinatário principal v0.1: Lucas.
- Revisor sugerido: Danilo quando envolver venda/curadoria/cliente.
- Canal default: preview Lucas.
- Aprovação: contato com cliente, mensagem WhatsApp, resposta em nome da LK ou criação de rotina Evolution/n8n exige Lucas.

## Matriz de aprovação por ação

- Relatório read-only para Lucas: permitido.
- Relatório para outro membro da equipe: exige validação desta matriz por Lucas antes do primeiro envio recorrente.
- Draft interno de design/SEO/copy: Renan pode revisar depois que Lucas validar o roteamento.
- Draft de produto/curadoria/compra: Danilo pode revisar depois que Lucas validar o roteamento.
- Fiscal/financeiro/Tiny sensível: Júlio pode revisar depois que Lucas validar o roteamento.
- Campanha, WhatsApp, Klaviyo, Shopify, preço, estoque, compra, fornecedor, Notion produtivo, n8n, Meta/Google, banco/API, cron ou infra: Lucas aprova antes de executar.

## Campos obrigatórios para futuros envios

Todo relatório que for roteado para alguém deve registrar:

- nome do relatório;
- objetivo;
- destinatário principal;
- cópias;
- canal;
- frequência;
- sensibilidade dos dados;
- se contém PII;
- ação esperada do destinatário;
- aprovação necessária;
- data/hora de envio;
- evidência/fonte dos dados.

## Próximas perguntas para Lucas

1. Confirmar se Danilo deve ser o revisor operacional de compras/curadoria/loja física.
2. Confirmar se Júlio deve receber apenas financeiro/fiscal/Tiny sensível ou também relatórios de estoque.
3. Confirmar se Renan deve receber tráfego pago/influencer além de design/SEO.
4. Confirmar canais por pessoa: Telegram, WhatsApp, e-mail, Notion ou outro.
5. Confirmar se existe grupo oficial para `LK Team`/compras e qual nome deve ser usado nos documentos.

## O que esta matriz não faz

- Não cria cron.
- Não envia mensagem para equipe.
- Não cria grupo, Notion, automação, campanha ou fluxo.
- Não consulta dados produtivos.
- Não altera Shopify, Tiny, Klaviyo, WhatsApp, Google, Meta, Notion, n8n, banco, VPS ou Docker.
