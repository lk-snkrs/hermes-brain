# LK OS — Auditoria de lacunas contra o PRD inicial

Status: `prd_gap_audit_readonly`
Data: 2026-05-15
Contexto: LK Sneakers / Projeto LK OS
Modo: documentação local/read-only. Nenhuma compra, contato, envio, write produtivo, cron, UI, worker, Shopify/Tiny/Merchant/Klaviyo/Rivo/Judge.me/Meta/Google/n8n/infra foi executado.

## Veredito

Lucas está certo: o backlog pendente anterior ficou estreito demais porque olhou principalmente as frentes recentes — sourcing, GMC, Klaviyo draft, Mission Control e Loyalty — e não reabriu o PRD inicial inteiro.

O PRD v0.1/v0.2 ainda tem lacunas relevantes em módulos estratégicos que não podem sumir do LK OS.

## Lacunas adicionais do PRD que precisam voltar ao backlog

### P1 — Data Quality Layer / modelo operacional por variante

Fonte no PRD: seções 6, 26 e 29.

Falta fechar:

- modelo local canônico por produto/variante/tamanho;
- histórico de preço, estoque, vendas, recomendações, aprovações e eventos;
- estados comerciais por variante: `disponivel`, `reservado`, `sob_encomenda_br`, `sob_encomenda_us`, `em_transito`, `recebido_ja_vendido`, `recebido_livre`, `divergente`;
- regra de estoque livre vs estoque físico vs reservado/encomenda;
- mapeamento completo Shopify SKU ↔ Tiny/aliases;
- status de qualidade antes de qualquer recomendação comercial.

Próximo bloco seguro:

- criar auditoria read-only do modelo local atual e matriz de campos ausentes.

### P1 — Daily Sales Brief 07h e Weekly CEO Review como rotina completa

Fonte no PRD: seções 9, 23 e Fase 8.

Feito parcialmente:

- Daily/Weekly existem como crons/read-only e relatórios iniciais.

Ainda falta:

- estabilizar contrato final do briefing diário com todos os blocos do PRD: vendas, online vs físico, GA4/CRO, produtos/tamanhos, Tiny, encomendas/importações, recompra, pricing signals, ideias e aprovações;
- confirmar se 07h é o horário final ou se o cron ativo divergente é intencional;
- rotina de silêncio/alerta calibrada com critérios finais;
- Weekly CEO Review com módulos de SEO/recompra/mídia/estoque sempre reconciliados.

Próximo bloco seguro:

- auditar crons ativos vs cadência-alvo do PRD e gerar gap report, sem alterar cron.

### P1 — Pulso Comercial 16h

Fonte no PRD: seção 10.

Correção Lucas 2026-05-17: o Pulso Comercial já foi feito como artefato/template/dry-run. Não deve mais aparecer como gap de criação. O gap remanescente é decidir se ele vira rotina real/cron com fonte viva, critérios de silêncio e aprovação de envio.

Escopo pendente:

- sinais do dia em andamento;
- restocks relevantes;
- venda que gera recompra;
- estoque crítico;
- oportunidades por cliente/produto/tamanho;
- alertas para LK Compras;
- política anti-spam: silêncio se não houver ação.

Próximo bloco seguro:

- reconciliar Pulso Comercial existente contra crons/cadência do PRD e preparar proposta de operacionalização, sem criar cron nem enviar mensagem automaticamente.

### P1 — CRO / conversão 0,13% → 0,20%

Fonte no PRD: objetivo 1 e seção 15.

Falta tratar como trilha própria, não só como consequência de GMC/SEO.

Escopo pendente:

- baseline atual Shopify/GA4;
- funil sessões → PDP view → add to cart → checkout → purchase;
- produtos com tráfego alto e baixa venda;
- produtos com add-to-cart e baixa compra;
- diagnóstico mobile/checkout/confiança/PDP/preço/estoque;
- fila de hipóteses e testes aprováveis.

Próximo bloco seguro:

- criar auditoria CRO read-only com Shopify/GA4 e fila P1/P2 de hipóteses.

### P1 — Brand Mix Intelligence

Fonte no PRD: seção 14.

Falta operacionalizar.

Escopo pendente:

- share por receita, unidades, pedidos, canal, campanha/influencer;
- momentum por marca/modelo/tamanho;
- Onitsuka/New Balance/Adidas/Nike e novas marcas;
- separar queda de demanda vs falta de estoque.

Próximo bloco seguro:

- gerar Brand Mix snapshot read-only 30/90/120 dias com Shopify + Tiny.

### P1 — Paid Traffic & Influencer Intelligence completa

Fonte no PRD: seção 18.

Feito parcialmente:

- dicionário influencer/campaign v0.2;
- ponte Meta/Metricool/GA4/Shopify inicial;
- regras de Pareto-compatible e Maicon/Marias;
- correção de governança Lucas 2026-05-17: Pareto cuida de tráfego pago; FHITS cuida de influencers. A camada LK OS deve cruzar sinais, mas preservar essa fronteira operacional.

Ainda falta:

- dicionário canônico vivo entre `campaign_name`, `adset`, `ad_name`, UTM, cupom, landing/referrer, influencer, produto/marca/modelo/SKU/tamanho;
- reconciliação regular de custo pago com receita Shopify compatível;
- consequência de estoque por campanha/influencer;
- leitura por criativo aprovado;
- rotina semanal acionável além do preview inicial;
- visão de Mission Control que mostre Pareto/paid e FHITS/influencers lado a lado, com status, owner e próxima ação segura.

Próximo bloco seguro:

- atualizar attribution dictionary com amostra atual e bucket de lacunas por influencer/campanha.

### P1 — Content & Campaign Production Engine

Fonte no PRD: seção 19.

Falta transformar em motor recorrente.

Escopo pendente:

- gerar copy/estrutura/CTA/briefing visual a partir de sinais reais;
- consultar DesignMD LK antes de conteúdo;
- criar drafts locais para Instagram, Reels, newsletter, WhatsApp, Klaviyo, blog, PDP copy e SEO;
- memória de conteúdo: produzido, canal, aprovação, resultado, aprendizado.

Próximo bloco seguro:

- criar backlog de conteúdo a partir dos sinais P1 já existentes, com previews locais e sem publicação.

### P1 — Trend-to-Product-to-Blog

Fonte no PRD: seção 20.

Falta implementar o fluxo completo.

Escopo pendente:

- sinal de produto/tendência;
- fit com curadoria LK;
- checar LK disponível/sob encomenda;
- checar sourcing aprovado quando necessário;
- calcular preço LK;
- preparar draft de produto + blog + distribuição quando aprovado;
- evitar blog sem produto/link comprável.

Próximo bloco seguro:

- criar router read-only de tendências → produto/blog, usando apenas sinais disponíveis e sem marketplace/write.

### P2 — Shopify Operations

Fonte no PRD: seção 21.

Feito parcialmente:

- SEO title/meta em alguns produtos mediante aprovação;
- padronização SKU em escopos aprovados.

Ainda falta:

- rotina de subir produtos/drafts;
- organizar coleções;
- ordenar coleções: primeiros 8 últimos lançamentos dos últimos 90 dias, depois best sellers, com exceções por estoque livre/encomenda/estratégia/conversão;
- revisar tags, imagens, SEO e PDP;
- localizar/adaptar guia de subida de produto do repositório `LCWATSAP`;
- qualquer tema Shopify exige diff/preview/PR/aprovação.

Próximo bloco seguro:

- gerar auditoria read-only de coleção/PDP/tags/imagens e localizar a fonte LCWATSAP, sem alterações Shopify.

### P2 — SEO / Search Console além do GMC

Fonte no PRD: seção 22.

Feito parcialmente:

- GSC router, SEO/CRO weekly improvement e alguns pacotes title/meta.

Ainda falta:

- rotina evergreen para páginas de coleção, produto, marca/modelo e blog;
- schema quando fizer sentido;
- interlinking;
- backlog de conteúdo SEO conectado a produto comprável;
- separar claramente SEO orgânico de GMC/feed.

Próximo bloco seguro:

- gerar mapa SEO orgânico read-only por oportunidade: produto, coleção, marca/modelo, blog.

### P2 — Online vs loja física / WhatsApp Evolution/wacli

Fonte no PRD: seções 17, 23 e descoberta pendente.

Feito parcialmente:

- contrato wacli/OpenClaw documentado;
- contas `pessoal` e `lk-compras` conectadas no escopo anterior;
- guardrails de envio preservados.

Ainda falta:

- confirmar marcação Shopify de online vs físico;
- confirmar tags/campos de encomenda/importação em pedidos;
- consolidar loja física como canal de relacionamento 1:1 via WhatsApp;
- conectar/validar conta Hermes WhatsApp se Lucas retomar;
- classificador LK Compras v1 local/read-only.

Próximo bloco seguro:

- auditoria read-only de campos Shopify para online/físico/encomenda + revisão local wacli sem envio.

### P2 — Notion LK Compras / Encomendas / Stock

Fonte no PRD: seções 5, 11, 12 e 29.

Feito parcialmente:

- padrão `[LK] Encomenda` e cards de sourcing foram usados em escopo aprovado;
- decisão Júlio/Notion como log foi documentada.

Ainda falta:

- mapear integralmente databases Notion `LK Compras`, `LK Encomendas` e `LK Stock`;
- documentar campos, status, relações e idempotência;
- separar compra real, encomenda, log, pedido e estoque.

Próximo bloco seguro:

- fazer schema map read-only do Notion LK, sem criar/editar cards.

### P2 — Pricing Intelligence completa

Fonte no PRD: seção 13.

Feito parcialmente:

- fórmula de importação corrigida: custo landed sem `×2`; `×2` é markup/ideal;
- preço site LK virou referência primária em sourcing.

Ainda falta:

- custo de trazer por origem/produto/peso/risco;
- arredondamento psicológico LK como sugestão;
- regras de aumento/redução de preço por demanda, estoque, reposição e conversão;
- separar preço de vitrine, custo landed, preço ideal e aprovação de alteração.

Próximo bloco seguro:

- gerar playbook de pricing read-only com parâmetros pendentes e exemplos, sem aplicar preço.

### P2 — Wile ERP / integrações externas pendentes

Fonte no PRD: seções 5 e 29.

Falta mapear:

- papel real do Wile ERP;
- LCWATSAP como fonte de guia/skill de subida;
- Cloudcio quando Lucas enviar link;
- Frenet como fonte auxiliar de frete;
- n8n como orquestração futura apenas após approval flow.

Próximo bloco seguro:

- criar registro de integrações pendentes com status: `mapear`, `sem acesso`, `bloqueado`, `não fonte oficial`.

### P2 — Approval Manager / Learning Loop como produto operacional

Fonte no PRD: seções 24, 25 e 27.

Feito parcialmente:

- ledger e skill updates já existem.

Ainda falta:

- interface/rotina única de aprovações pendentes;
- registrar resultado pós-execução e aprendizado de cada decisão;
- rotina de limpeza de approval packets superseded/no-op;
- status padrão para approved/rejected/needs_data/needs_preview/executed em todas as frentes.

Próximo bloco seguro:

- gerar auditoria do ledger e pacote de aprovação pendente, marcando superseded/no-op/ativo.

### P3 — Crons/cadência alvo completa

Fonte no PRD: seção 23.

Feito parcialmente:

- alguns crons read-only estão ativos.

Ainda falta decidir/implementar com aprovação:

- Daily 07h;
- Pulso 16h;
- SEO/CRO segunda 09h;
- Stock Intelligence segunda 14h;
- Newsletter terça/sexta;
- Content Batch terça 15h;
- Trend-to-Blog quarta 09h;
- CRM/RFM quarta 15h;
- GMC quinta 09h;
- Paid/Influencer quinta 15h;
- Shopify Ops sexta 15h;
- Weekly CEO Review sábado 10h.

Próximo bloco seguro:

- reconciliar cadência-alvo vs crons reais e propor o que fica sob demanda, cron silencioso ou manual.

## Backlog priorizado revisado

### Agora / P1 real

1. Data Quality Layer e modelo operacional por variante.
2. Daily/Weekly briefing completo vs cadência real.
3. Pulso Comercial 16h dry-run.
4. CRO baseline 0,13% → 0,20%.
5. Brand Mix Intelligence.
6. Paid/Influencer attribution dictionary vivo.
7. Content Engine conectado a sinais reais.
8. Trend-to-Product-to-Blog router.
9. Sourcing/Júlio P1 já pronto, mas ainda precisa instrução operacional curta.
10. GMC residual/preço permanece bloqueado pelos gates já conhecidos.

### Depois / P2

1. Shopify Operations e coleções.
2. SEO orgânico/evergreen separado de GMC.
3. Online vs loja física / WhatsApp / encomenda.
4. Notion LK schema map completo.
5. Pricing playbook completo.
6. Integrações pendentes: Wile, LCWATSAP, Cloudcio, Frenet, n8n.
7. Approval Manager/Learning Loop como superfície única.

### Futuro / P3

1. Cadência completa de crons.
2. Mission Control UI/worker/Kanban.
3. Loyalty/Rivo/Judge.me quando Lucas retomar.

## Não executado

- Sem alteração de cron.
- Sem UI/worker/Kanban.
- Sem Shopify/Tiny/Merchant/Klaviyo/Meta/Google/Rivo/Judge.me/Notion write.
- Sem WhatsApp/e-mail/campanha.
- Sem compra, reserva, fornecedor ou cliente.
- Sem marketplace lookup novo.
