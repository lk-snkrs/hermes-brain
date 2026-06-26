# Hermes v0.17 — Onda 1 executada (local/read-only/documental)

Data: 2026-06-22
Responsável: Hermes Geral/default
Status: Onda 1 iniciada e materialmente executada sem mudanças sensíveis.

## Interpretação da ordem do Lucas

Lucas pediu: “Siga pela onda 1? Depois o 3 depois o 5 depois o 1 em ordem”.

Interpretação aplicada com segurança:

1. Executar **Onda 1** agora, pois é local/read-only/documental.
2. Preparar **Onda 3** como approval packet de canais novos, sem ativar canais.
3. Preparar **Onda 5** como approval packet de fleet/infra avançada, sem mexer em infra.
4. Tratar o último “1” como revisão/fechamento da Onda 1 após os packets, salvo correção de Lucas.

## Evidência runtime coletada

Run dir principal:

- `/opt/data/backups/hermes-v017-wave1-20260622T114043Z/wave1_runtime_evidence.log`

Run dir Doppler candidate:

- `/opt/data/backups/hermes-v017-wave1-20260622T114046Z-doppler/doppler_presence.log`

Resultados:

- Hermes ativo: `Hermes Agent v0.17.0 (2026.6.19)`.
- Curator: `ENABLED`, `consolidate: off`, prune-only/LLM merge opt-in.
- Dashboard real process count: `0`; não há dashboard real rodando/exposto agora.
- MCP catalog/list:
  - Disponíveis no catálogo: `linear`, `n8n`.
  - Custom/enabled: `dataforseo`, `fetch`, `metricool_readonly`, `sequential_thinking`, `time`.
- Doppler candidate presence:
  - `XAI_API_KEY`: presente.
  - `LINEAR_API_KEY`: presente.
  - `N8N_API_TOKEN`: presente.
  - Photon/Raft/SimpleX/WhatsApp Cloud/Dashboard password candidates testados: ausentes sob esses nomes.
- `values_printed=false`.

## Onda 1 — itens adotados

### 1. Governança e documentação

- PRD principal já criada: `areas/operacoes/prds/hermes-v017-adocao-completa-20260622.md`.
- Skill reference já criada: `lucas-runtime-operations/references/hermes-v017-complete-adoption-20260622.md`.
- Este relatório registra a execução da Onda 1 e a sequência solicitada por Lucas.

### 2. Curator v0.17

- Validado que o curator está ativo e `consolidate: off`.
- Decisão: manter como padrão; LLM consolidation só via aprovação/execução explícita.

### 3. Dashboard local-only readiness

- Confirmado por status estrito que não há processo real de dashboard rodando.
- Decisão: dashboard fica pronto para avaliação local-only, mas não será exposto publicamente sem approval packet.

### 4. MCP catalog readiness

- Catalog/list read-only executado.
- `linear` e `n8n` aparecem como disponíveis, mas instalação/uso com write/OAuth fica bloqueado para aprovação escopada.

### 5. Background subagents

- Padrão adotado: usar `delegate_task(background=true)` para pesquisa/build longo que não exige interação e não executa side effects externos sem aprovação.
- Não foi disparado teste desnecessário em Telegram para evitar ruído; o recurso está disponível no runtime/ferramentas.

### 6. Image-to-image/editing

- Padrão adotado: usar como preview criativo local/visual; publicação em Shopify/Klaviyo/Ads/site exige aprovação separada.

### 7. xAI/Grok readiness inicial

- `XAI_API_KEY` existe no Doppler, mas nenhum modelo default foi alterado.
- Próximo passo seguro: smoke read-only em Onda 4 ou approval específico se Lucas priorizar.

## Não-ações confirmadas

- Não mexeu em Docker/VPS/Traefik.
- Não reiniciou gateway.
- Não expôs dashboard/API publicamente.
- Não ativou WhatsApp Cloud, Photon/iMessage, Raft ou SimpleX.
- Não instalou MCP novo.
- Não criou cron novo.
- Não trocou modelo default.
- Não imprimiu secrets.

## Próximos conforme ordem solicitada

1. Onda 3: preparar pacote de aprovação para canais novos.
2. Onda 5: preparar pacote de aprovação para fleet/infra avançada.
3. Voltar à Onda 1 para fechamento/revisão, caso Lucas confirme que o último “1” era intencional.

`values_printed=false`
