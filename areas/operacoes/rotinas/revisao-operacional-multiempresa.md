# Revisão Operacional Multiempresa

## Objetivo

Gerar uma leitura executiva curta, acionável e segura da operação de LK Sneakers, Zipper Galeria, SPITI Auction e Operações/Hermes Brain usando apenas fontes versionadas do Brain, salvo quando Lucas pedir dados vivos explicitamente.

Esta rotina existe para responder bem a pedidos como:

- “algo mais a ser feito?”;
- “vamos começar?”;
- “onde devo focar agora?”;
- “me dá um panorama das empresas”.

## Escopo

Inclui:

- prioridades e bloqueios documentados em `empresa/gestao/pendencias.md`;
- memória executiva em `memories/lk.md`, `memories/zipper.md`, `memories/spiti.md`;
- mapas e playbooks em `areas/lk/`, `areas/zipper/`, `areas/spiti/` e `areas/operacoes/`;
- riscos de aprovação, dados vivos necessários e próximos passos seguros.

Não inclui por padrão:

- consultas a Shopify, Supabase, Klaviyo, Meta Ads, Evolution, banco, VPS, Docker, n8n, Paperclip ou APIs externas;
- envio de WhatsApp, email, campanha, post ou contato com cliente/colecionador;
- alteração de infraestrutura, cron, runtime, banco, segredo ou deploy.

## Fontes obrigatórias

1. `empresa/gestao/pendencias.md`.
2. `memories/lk.md`.
3. `memories/zipper.md`.
4. `memories/spiti.md`.
5. `areas/lk/MAPA.md` e playbooks LK relevantes.
6. `areas/zipper/MAPA.md` e playbooks/templates Zipper relevantes.
7. `areas/spiti/MAPA.md` e playbooks/templates SPITI relevantes.
8. `ROADMAP-30-DIAS-HERMES.md`.
9. Relatório mais recente de retomada de planos/PRDs em `reports/` quando existir.

## Passo a passo

1. Confirmar data e worktree limpo/ramo de trabalho.
2. Ler pendências e classificar:
   - ação livre/documental;
   - bloqueada por aprovação Lucas/Osmar;
   - aguardando data/evento;
   - exige dados vivos antes de afirmar.
3. Revisar cada negócio:
   - LK: CRM, campanha, retenção, ecommerce, tráfego e atendimento.
   - Zipper: vendas de obras, colecionadores, feiras e comunicação.
   - SPITI: lances, leilão, Spiti Hub, monitor e evidência.
   - Operações: Brain, integrações, crons, runtime e segurança.
4. Produzir relatório em `reports/revisao-operacional-multiempresa-YYYY-MM-DD.md`.
5. Separar explicitamente:
   - o que pode ser feito agora sem aprovação;
   - o que precisa de dados vivos;
   - o que precisa de aprovação antes de executar;
   - o que não foi tocado.
6. Rodar `brain_health_check.py`, secret scan e `git diff --check` antes de versionar.

## Saída esperada

O relatório deve conter:

- leitura executiva;
- matriz por empresa/área;
- próxima ação recomendada;
- lacunas documentais encontradas;
- itens bloqueados por aprovação;
- itens que exigem dados vivos;
- “não alterado”.

## Critério de qualidade

Uma boa revisão:

- não inventa números atuais;
- não confunde Zipper Vendas com SPITI;
- preserva “silêncio > dado errado” para SPITI;
- separa fato, interpretação e recomendação;
- reduz a próxima ação para uma escolha simples;
- não cria automação, cron ou rotina recorrente sem necessidade real e aprovação.

## Aprovação

Pode ser executada e versionada como documentação/report local.

Requer aprovação explícita antes de:

- consultar ou modificar produção quando não for necessário para a pergunta;
- enviar mensagens, campanhas, posts ou abordagens externas;
- alterar Supabase, Shopify, Klaviyo, Evolution, Meta Ads, n8n, Vercel, VPS, Docker, Traefik, volumes, redes ou cron;
- criar rotina recorrente/cron/Telegram delivery.
