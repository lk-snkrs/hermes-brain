# PRD — Fast lane e model routing por perfil no Hermes v0.16

Data: 2026-06-06T16:40:25Z
Status: PRD/auditoria documental — nenhuma configuração/modelo/runtime alterado
Owner: Hermes Geral / Operações Hermes

## Problema

O ecossistema Hermes tem vários profiles vivos. Usar sempre o lane forte para mensagens simples aumenta latência, custo e risco de timeout. Porém ativar roteamento agressivo pode piorar decisões, especialmente em produção, negócios, código, auditorias e ações sensíveis.

## Objetivo

Criar uma política conservadora de fast lane por perfil:

- respostas simples mais rápidas;
- tarefas profundas seguem no modelo forte;
- fallback real para timeout/provider;
- evidência de runtime antes de chamar ativo.

## Escopo desta fase

Inclui:

- matriz recomendada por perfil;
- regras simples vs profundas;
- critérios de aprovação para ativação futura;
- smoke tests necessários.

Não inclui:

- mudança de `config.yaml`;
- restart de gateways;
- troca de provider/model;
- criação de cron/watchdog;
- mexer em credentials.

## Perfis candidatos

### Mordomo

Fast lane candidato para:

- confirmações simples;
- classificação de inbox;
- follow-up leve;
- respostas administrativas sem bloqueio.

Forçar strong para:

- preço, disponibilidade, negociação, reclamação, fornecedor, bulk, logística sensível, cliente crítico.

### LK Ops/Atendimento

Fast lane candidato para:

- status simples e triagem de atendimento;
- respostas de baixa ambiguidade com fonte clara.

Forçar strong para:

- Tiny/Shopify estoque, promessa a cliente, reclamação, reembolso, logística, bulk, fornecedores.

### LK Shopify

Fast lane candidato para:

- readback simples;
- checklist de QA textual;
- classificação de demanda.

Forçar strong para:

- theme, cart drawer, app, tracking, SEO/metafield write, rollback, produção, diffs, código.

### LK Growth

Fast lane candidato para:

- triagem de pauta;
- resumo de relatório;
- classificação de oportunidade.

Forçar strong para:

- SEO/GEO strategy, conteúdo final, análise competitiva, ads, CRO, decisões comerciais.

### LK Collection Optimizer

Fast lane candidato para:

- triagem de coleção;
- checklist preliminar LKGOC.

Forçar strong para:

- arquitetura de experiência, Guia LK, visual QA, SERP/evidence, Shopify handoff.

### SPITI

Fast lane muito restrito. Usar strong por padrão porque dado errado em leilão/lote/bid é mais caro que latência.

### Hermes Geral

Fast lane candidato só para:

- acknowledgements;
- roteamento simples;
- leitura curta de status não sensível.

Forçar strong para:

- PRD, auditoria, código, runtime, segurança, Brain governance, produção, roteamento multiempresa.

## Regras de roteamento

Fast lane somente se todos forem verdadeiros:

1. pedido é curto e de baixa ambiguidade;
2. não envolve produção, dinheiro, cliente, credencial, deploy, Docker, Traefik, banco, Shopify/Tiny write, campanha ou envio externo;
3. não requer navegar em muitos arquivos/fontes;
4. não requer raciocínio jurídico/financeiro/estratégico;
5. resposta errada tem baixo custo e pode ser corrigida facilmente.

Strong lane se qualquer termo/condição aparecer:

- código, bug, debug, PRD, plano, auditoria, SEO, CRO, deploy, Docker, VPS, Traefik, token, secret, webhook, MCP, OIDC, Shopify, Tiny, Klaviyo, Meta, SPITI, lance, lote, cliente, preço, disponibilidade, reclamação, rollback.

## Fallback policy proposta

- Timeout/non-response deve acionar fallback + cooldown, não só retry infinito.
- Same-provider fallback não conta como proteção contra outage do provider.
- Toda ativação futura precisa log sanitizado confirmando `selected model/lane` e fallback event.

## Smoke tests antes de ativar

Para cada perfil:

1. one-shot simples: classificar demanda leve;
2. one-shot deep: garantir que força strong;
3. timeout/fallback simulado ou teste de provider alternativo;
4. verificar logs sem secrets;
5. confirmar live PID pós-restart se houver restart aprovado;
6. rodada Telegram real apenas no profile afetado.

## Approval packet futuro

Qualquer ativação deve pedir aprovação separada com:

- profiles afetados;
- modelo fast escolhido;
- rollback exato;
- janela de restart;
- smoke tests;
- critério para desligar se a qualidade cair.

## Recomendação

Não ativar todos de uma vez. Piloto recomendado:

1. Mordomo ou LK Ops, se o objetivo for latência de atendimento.
2. LK Shopify, se o objetivo for readback/QA simples.
3. Só depois expandir para Growth/Collection Optimizer.

Status final desta fase: **pronto para approval packet de piloto**, não ativo em runtime.
