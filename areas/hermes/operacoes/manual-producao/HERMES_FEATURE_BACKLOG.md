# Hermes Feature Backlog — Fase 2

Gerado em: 2026-05-30T22:02:16+00:00  
Status: **backlog canônico v0.2 / board Kanban real sem execução automática**  
Board planejado: `hermes-lk-improvements`  
Board real criado em 2026-06-03: `hermes-lk-improvements`  
Regra: cards abaixo são **documentais/unassigned** até existir approval packet para execução real. Não acionar dispatcher produtivo por este arquivo.

## Como usar este backlog

- Cada item é um card candidato para Kanban.
- Enquanto não houver worker seguro, manter como documento local.
- Se virar card real, copiar título, objetivo, saída esperada, guardrails e critérios de aceite.
- Atribuição a worker real exige confirmar `dispatch_in_gateway`, lane/toolset, logs, rollback e impacto.

## Card F2-001 — Desenhar board Kanban `hermes-lk-improvements`

Prioridade: P1  
Status: completed/documental em 2026-05-30 — ver `F2_001_KANBAN_BOARD_DESIGN.md`  
Owner lógico: Hermes Geral / governança operacional  
Tipo: local/documental

Objetivo:

- Definir estrutura do board para melhorias Hermes/LK sem acionar execução automática.

Escopo:

- colunas/status esperados;
- convenção de IDs;
- labels de risco;
- critérios para `unassigned`, `ready`, `blocked`, `done`;
- regra de dependência fan-out/fan-in;
- política de comentário/receipt.

Guardrails:

- não atribuir a profile worker ainda;
- não rodar dispatcher produtivo;
- não criar tarefa que faça write externo.

Saída esperada:

- especificação curta do board;
- 3 a 5 cards iniciais prontos para eventual criação;
- approval packet se a próxima etapa envolver Kanban real.

Critério de aceite:

- board design permite auditoria e não depende de conversa Telegram para sobreviver.

## Card F2-002 — Inventariar MCP/DataForSEO existente

Prioridade: P1  
Status: completed/read-only em 2026-05-30 — ver `F2_002_MCP_INVENTORY_AND_CANDIDATES.md`  
Owner lógico: LK Growth/LK Shopify + Hermes Geral  
Tipo: read-only

Objetivo:

- Confirmar onde MCP está configurado, quais servers existem e se DataForSEO está pronto/útil.

Escopo:

- ler configs locais sem imprimir secrets;
- identificar `mcp_servers` por profile;
- registrar command/url sem credenciais;
- documentar sampling, timeout, tool exposure e riscos;
- verificar se a skill/native MCP e SDK estão disponíveis.

Guardrails:

- não adicionar/alterar token;
- não editar config;
- não reiniciar profile;
- não chamar MCP externo com credencial produtiva sem aprovação.

Saída esperada:

- relatório local com matriz `profile -> server -> status -> risco -> próxima ação`;
- whitelist recomendada de tools read-only;
- approval packet se precisar ativar/reiniciar profile.

Critério de aceite:

- Lucas consegue decidir se DataForSEO MCP vale como piloto ou se deve ficar em espera.

## Card F2-003 — Especificar plugin local/read-only “Hermes/LK Capability Status”

Prioridade: P1  
Status: card real criado em 2026-06-03 / `ready` / `assignee=null` / id `t_01156a76`  
Owner lógico: Hermes Geral / runtime observability  
Tipo: design local

Objetivo:

- Definir um plugin próprio que mostre status/capability cards sem writes externos.

Escopo funcional:

- profiles esperados vs live/configurado;
- API/webhook por profile;
- crons e delivery;
- MCPs configurados;
- plugins enabled;
- últimos receipts locais;
- riscos e safe next action.

Guardrails:

- read-only filesystem/local status;
- sem terminal destrutivo;
- sem Docker/VPS/Traefik;
- sem Shopify/Tiny/Crisp/GMC/ads writes;
- sem secrets no output.

Saída esperada:

- mini-PRD do plugin;
- interface dos cards;
- lista de fontes locais permitidas;
- testes mínimos;
- approval packet para implementação/ativação.

Critério de aceite:

- plugin proposto ajuda observabilidade sem virar superfície de ação perigosa.

## Card F2-004 — Classificar exposição Dashboard/API default

Prioridade: P0/P1  
Status: revalidado/concluído em 2026-06-03 — board `hermes-lk-improvements` / id `t_cd3dd451` / `done`; revisão específica do dashboard público registrada no card `t_2302a6a6`; ver `F2_004_DASHBOARD_API_EXPOSURE_CLASSIFICATION.md`, `RECEIPT_F2_004_EXPOSURE_REVALIDATION_20260603.md` e `RECEIPT_F2_DASHBOARD_PUBLIC_AUTH_REVIEW_20260603.md`  
Owner lógico: Hermes Geral / infra safety  
Tipo: read-only

Objetivo:

- Saber se API/webhook/dashboard atuais estão apenas locais/seguros ou expostos de forma que exige correção.

Escopo:

- inspecionar configuração local e processos;
- confirmar bind host/port;
- distinguir `0.0.0.0` dentro de container vs exposição pública real;
- checar se há Traefik/firewall/port publishing relevante somente por leitura.

Guardrails:

- não alterar Docker/compose/Traefik/firewall;
- não reiniciar gateway;
- não imprimir API key;
- se risco real aparecer, emitir approval packet separado.

Saída esperada:

- classificação: local-only / host-local / publicly reachable / unknown;
- evidências redigidas;
- ação recomendada.

Resultado 2026-06-03:

- API default: host-local via publish `127.0.0.1:8642`, com API key exigida.
- Webhook default: público via Traefik/Cloudflare, com subscriptions LK Shopify `Deliver: log`.
- Dashboard: público separado via Traefik em hostname Hermes Agent Dashboard; revisão específica encontrou docs/OpenAPI públicos, token de sessão injetado no HTML e acesso read-only sensível com token da própria página. Uso operacional fica bloqueado até mitigação/isolamento.

Critério de aceite:

- nenhuma decisão de cockpit/dashboard acontece sem saber o blast radius.

## Card F2-005 — Padronizar deliverable mode e receipts

Prioridade: P1  
Status: card real criado em 2026-06-03 / `ready` / `assignee=null` / id `t_fe598ba5`  
Owner lógico: Hermes Geral / UX Telegram  
Tipo: local/documental

Objetivo:

- Definir quando uma entrega deve ser Telegram texto, `MEDIA:`, arquivo local, relatório em Brain ou receipt silencioso.

Escopo:

- regra para relatórios executivos;
- regra para anexos nativos;
- regra para jobs silent-OK;
- regra para approval/rollback receipts;
- exemplos bons/ruins.

Guardrails:

- não alterar crons existentes;
- não mudar delivery target sem aprovação;
- respeitar preferência de Lucas: Telegram só decisão/exceção/falha/relatório desejado.

Saída esperada:

- seção curta adicionável ao manual;
- template de receipt enxuto.

Critério de aceite:

- reduz ruído e evita “caminho interno sem arquivo entregue” quando o produto é um artefato.

## Card F2-006 — Definir política MCP de negócio

Prioridade: P2 depois do inventário  
Status: completed/documental em 2026-05-30 — ver `F2_006_BUSINESS_MCP_POLICY.md`  
Owner lógico: Hermes Geral + dono da área  
Tipo: policy

Objetivo:

- Criar política para MCPs de negócio: DataForSEO, banco/Open Finance, Crisp/Hugo, GitHub, Shopify/Tiny etc.

Guardrails:

- read-only/list/get primeiro;
- tokens em Doppler/secret manager;
- sampling off salvo necessidade explícita;
- writes externos com approval por payload.

Saída esperada:

- política curta por classe de MCP;
- checklist de ativação.

## Card F2-007 — Preparar piloto real pequeno

Prioridade: P2 depois de F2-001/F2-002/F2-003  
Status: pilot-executed/read-only em 2026-05-30 — ver `F2_007_DATAFORSEO_MCP_PILOT_RECEIPT.md`; Supabase packet preparado em `APPROVAL_PACKET_SUPABASE_MCP_READONLY.md`; card Kanban para escolher próximo piloto criado em 2026-06-03 / `ready` / `assignee=null` / id `t_45b92440`  
Owner lógico: Hermes Geral + LK Growth/LK Shopify/LK Trends  
Tipo: approval packet / piloto MCP pequeno

Objetivo:

- Escolher **um** piloto real: Kanban read-only, MCP DataForSEO read-only ou plugin local/read-only.

Critério para escolher:

- menor risco;
- valor claro em menos de 1 dia;
- rollback simples;
- sem write externo;
- verificação objetiva.

Saída esperada:

- approval packet com comandos, arquivos, rollback e verificação.

## Ordem recomendada dos cards

1. F2-004 — classificar API/dashboard antes de cockpit.
2. F2-001 — desenhar Kanban board.
3. F2-002 — inventariar MCP/DataForSEO.
4. F2-003 — especificar plugin local/read-only.
5. F2-005 — padronizar deliverables.
6. F2-006 — política MCP após inventário.
7. F2-007 — piloto real pequeno, só com aprovação.
