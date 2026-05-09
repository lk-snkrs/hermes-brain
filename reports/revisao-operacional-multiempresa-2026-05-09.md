# Revisão operacional multiempresa — 2026-05-09

## Leitura executiva

Há uma melhoria clara e segura a fazer agora: transformar a pergunta “o que fazer a seguir?” em uma revisão operacional multiempresa padronizada, usando só o Brain versionado.

A fila ativa documentada está pequena. O único item ativo global é completar subdocs de integrações não recorrentes apenas quando virarem fluxo real. Isso, sozinho, não justifica abrir integrações aleatórias agora. Melhor movimento: criar uma rotina de revisão executiva multiempresa e deixar este primeiro relatório como referência de uso.

## Próxima ação recomendada

Começar por revisão documental e operacional, não por produção:

1. Criar rotina `revisao-operacional-multiempresa.md` em Operações.
2. Registrar este primeiro relatório em `reports/`.
3. Usar a revisão para decidir, em cada nova conversa, se o próximo passo é LK, Zipper, SPITI ou Operações.
4. Só consultar dados vivos quando a pergunta exigir número atual.
5. Só executar campanha, contato externo, deploy, banco ou infra após aprovação explícita.

## Matriz por área

### LK Sneakers

- Estado no Brain: bem estruturado para CRM, cross-sell, briefing, ecommerce, tráfego e atendimento.
- Oportunidade real documentada: retenção/segunda compra, cross-sell Jason Markk e segmento NB 9060 dormente.
- Próxima ação segura: preparar diagnóstico ou preview quando Lucas pedir foco em LK; antes de afirmar número atual, consultar fonte viva.
- Precisa aprovação antes de executar: qualquer Klaviyo, WhatsApp, campanha, post, público, alteração Shopify/Supabase/Meta ou contato externo.
- Lacuna útil: templates de preview de campanha/RFM/cross-sell ainda aparecem como pendência futura no roadmap, mas só valem se Lucas for ativar campanha ou rotina CRM concreta.

### Zipper Galeria

- Estado no Brain: bem mapeado por vendas de obras, colecionadores, feiras e comunicação; já existem templates por subárea.
- Regra crítica: Zipper Vendas (`pcstqxpdzibheuopjkas`, `vendas_tango`) não é SPITI/leilão.
- Próxima ação segura: usar templates existentes para análise ou briefing quando houver obra, artista, feira ou colecionador específico.
- Precisa aprovação antes de executar: contato com colecionador, negociação, proposta, publicação externa ou decisão de curadoria.
- Lacuna útil: nenhuma urgência documental nova; o ganho agora depende de demanda concreta com obra/feira/colecionador.

### SPITI Auction

- Estado no Brain: regras de fonte e playbooks críticos estão bem documentados.
- Regra crítica: email é fonte de verdade de lances; site mostra destaques; meta tag é preço base; silêncio é melhor que dado errado.
- Próxima ação segura: aguardar novo leilão ou demanda operacional; para Spiti Hub, trabalhar via PR para `dev` quando for código.
- Precisa aprovação antes de executar: mensagem para grupo/cliente, deploy, Supabase, Vercel, monitor, n8n, leilão ou produção.
- Lacuna útil: sem ação imediata até evento/leilão ou tarefa específica no Spiti Hub.

### Operações / Hermes Brain

- Estado no Brain: melhoria contínua está madura: health check, score, material ingest, retomada de planos e agora revisão multiempresa.
- Oportunidade real: consolidar esta revisão como rotina business-readable, sem cron.
- Próxima ação segura: versionar rotina e relatório; validar com health check e secret scan.
- Precisa aprovação antes de executar: cron recorrente, Mission Control visual, runtime Hermes, Docker/VPS, gateway, secrets, banco ou ações externas.

## Itens bloqueados por aprovação

Permanecem bloqueados, sem mudança nesta revisão:

- rotação de senha root da `lc.vps`, se desejada;
- decidir permanência/remoção de chave SSH dedicada;
- correção ativa do alerta/divergência Gateway Hermes;
- Mission Control visual ou cron recorrente;
- qualquer contato externo/campanha/mensagem em massa.

## Itens que exigem dados vivos antes de afirmar

- faturamento, pedidos, ticket, estoque, retenção ou segmentos atuais da LK;
- vendas reais, origem de pedido ou histórico comercial atual da Zipper;
- lance atual, total de lances, status de lote, monitor ou divergência SPITI;
- versão/estado real de runtime, container, cron, n8n, deploy ou VPS.

## Decisão operacional desta revisão

Criar a rotina de revisão operacional multiempresa e manter uso sob demanda. Não criar cron. Não consultar produção. Não acionar campanha. Não tocar infra.

## Não alterado

- Nenhum cron foi criado, pausado ou alterado.
- Nenhum dado vivo foi consultado.
- Nenhuma UI/Mission Control visual foi criada.
- Nenhum serviço de produção, VPS, Docker, Traefik, volume ou rede foi tocado.
- Nenhum banco, API, secret, campanha, WhatsApp, email, post ou contato externo foi tocado.
