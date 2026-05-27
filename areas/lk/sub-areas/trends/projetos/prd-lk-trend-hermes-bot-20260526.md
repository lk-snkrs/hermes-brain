# PRD — LK Trend Hermes Bot

Status: profile local preparado; ativação Telegram pendente de token/bot dedicado.
Data: 2026-05-26.

## Problema

A LK precisa de um especialista separado para monitorar tendências de sneakers/fashion e transformar sinais dispersos em oportunidades priorizadas, sem misturar esse trabalho com Hermes Geral, LK Growth ou LK Shopify.

## Objetivo

Criar o LK Trend como agente especialista para detectar produtos, modelos e colorways que estão ganhando tração fora do Brasil e transformar esses sinais em decisões comerciais seguras para LK Sneakers.

Prioridade operacional:

1. detectar produtos/modelos/colorways bombando fora do Brasil;
2. validar sinal internacional via StockX, GOAT, KicksDev, Hypebeast, Highsnobiety, Vogue e social quando relevante;
3. checar se o sinal ainda não está saturado no Brasil via Droper, busca BR e concorrência local;
4. cruzar com fit LK, lacuna de catálogo, margem provável e possibilidade de sourcing;
5. classificar como watchlist, sourcing para Júlio, catálogo-preview, conteúdo posterior ou ignorar por evidência fraca.

SEO, conteúdo, source page e PDP copy são camadas posteriores, usadas apenas quando a oportunidade virar publicação/produto/catálogo e houver pedido explícito ou handoff adequado.

Criar o LK Trend como agente especialista para:

- pesquisar tendências internacionais e brasileiras;
- cruzar sinais externos com venda/estoque/catálogo da LK;
- gerar relatório semanal;
- manter fila de oportunidades;
- preparar previews internos de conteúdo somente como etapa posterior;
- preparar pacotes de sourcing quando houver demanda/ruptura validada;
- acionar LK Growth ou LK Shopify apenas por handoff seguro.

## Escopo v1

### Incluído

- Relatório semanal read-only.
- Fila de oportunidades em Markdown/JSON.
- Score 0–100.
- Separação obrigatória: conteúdo vs compra/reposição vs catálogo-preview.
- Pesquisa web e mercado.
- Consulta a Brain e bases locais read-only.
- Handoff limpo para LK Growth/LK Shopify.

### Fora do escopo v1

- Cron automático.
- Publicação.
- Criação/edição de Shopify.
- Contato fornecedor.
- Compra/reserva.
- Campanha/WhatsApp/email/Klaviyo.
- Promessa a cliente.

## Fontes desejadas

- KicksDev / StockX / GOAT para sinal internacional e preço/referência quando aplicável.
- Droper para validação BR e sourcing local.
- Vogue, Hypebeast, Highsnobiety e web recente para contexto cultural.
- Reddit/TikTok/social quando disponível como sinal qualitativo.
- Shopify/Tiny/GA4/GSC/CRM/atendimento em modo read-only.

## Score

- Demanda interna LK: 25
- Sinal externo/tendência: 20
- Fit com LK: 20
- Estado comercial/catálogo/estoque: 20
- Evidência/confiança: 15

## Saídas Telegram

Sempre limpas:

- sem wrappers;
- sem JSON bruto;
- sem job ID;
- sem config boilerplate;
- uma decisão por vez.

Exemplo:

> Decisão 1/1: aprovar preview interno dos 3 P1 de conteúdo desta semana?

## Runtime

- Profile: `/opt/data/profiles/lk-trends`
- Brain: `areas/lk/sub-areas/trends/`
- Gateway: não iniciar até existir token dedicado e aprovação de ativação.
- API/webhook no profile: desativados para evitar conflito com Hermes Geral.

## Critério de pronto — preparação local

- Profile local criado.
- Token herdado removido/zerado.
- API/webhook desativados.
- SOUL do profile escrito.
- Brain package criado.
- MAPA LK atualizado.
- Secret scan sem vazamento.

## Critério de pronto — ativação Telegram futura

- Token dedicado configurado sem exposição.
- Gateway do profile iniciado.
- Processo verificado por HERMES_HOME.
- Teste de ida/volta Telegram.
- Receipt de ativação criado.
- Watchdog silent-OK configurado se aprovado.
