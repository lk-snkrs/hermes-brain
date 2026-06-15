# PRD — Hermes Nightly Operations Audit OS

Status: aprovado por Lucas em 2026-06-14  
Classificação: runtime/cron autorizado neste escopo  
Owner: Hermes Geral / Operações  
Fonte viva: cron registries + `/proc` runtime snapshot + artifacts Brain  

## Objetivo

Criar uma camada noturna transversal para auditar todos os OS, agentes, scripts e crons do Hermes antes do relatório executivo diário. A camada deve responder diariamente:

- o que está saudável;
- o que está ruim;
- o que piorou/melhorou;
- o que pode ser corrigido automaticamente;
- o que exige aprovação de Lucas;
- quais achados devem entrar no digest das 03h.

## Decisão de Lucas

Lucas aprovou executar as fases 1 a 4, deixar rodando, mexer em runtime/cron dentro deste escopo, executar a auditoria às 02h30 BRT e mover o digest diário para 03h BRT.

Emenda operacional 2026-06-15: Lucas aprovou Bloco A e Bloco B após reavaliação da madrugada. A cadeia ativa passa a ser Brain OS silent-OK health/scanner às 02h25 BRT (`deliver=local`), LK Shopify Sales OS reconcile às 02h40 BRT, Nightly Operations Audit OS às 02h50 BRT (`deliver=local`) e digest executivo às 03h BRT (`deliver=origin`). Reminder OS permanece autorizado a enviar Telegram/origin sempre que houver loop aberto acionável.

## Escopo aprovado

- Criar PRD e matriz no Brain.
- Implementar script local de auditoria.
- Gerar artifacts JSON/Markdown diários.
- Permitir autoheal A0/A1 local, reversível e sanitizado.
- Criar cron no-agent às 02h30 BRT.
- Alterar o cron do digest diário para 03h BRT.
- Atualizar o prompt/contexto do digest para ler o artifact da auditoria.

## Fora de escopo mesmo com esta aprovação

- Docker/VPS/Traefik/host mutation.
- Restart de gateway/profile.
- Mudança de secrets/credenciais.
- Envio externo de WhatsApp/email.
- Writes em Shopify, Tiny, Supabase, GMC, Klaviyo, Meta, Ads, bancos ou fontes de verdade.
- Operações destrutivas.

Esses itens seguem exigindo aprovação escopada própria com rollback.

## Cadência

- 02h30 BRT: `Hermes Nightly Operations Audit OS` roda em `no_agent=true`, `deliver=local`, com silent-OK.
- 03h00 BRT: digest executivo obrigatório no Telegram lê o artifact da auditoria junto com 01h/02h/02h15.

## Inputs

- `/opt/data/cron/jobs.json`.
- `/opt/data/profiles/*/cron/jobs.json`.
- `/proc/*/environ` + `/proc/*/cmdline`, sanitizado, apenas para `HERMES_HOME`/presença booleana.
- scripts em `/opt/data/scripts/` e `/opt/data/profiles/<profile>/scripts/`.
- artifacts de reports do Brain quando disponíveis.

## Outputs

- `reports/nightly-ops-audit/YYYY-MM-DD.json`.
- `reports/nightly-ops-audit/YYYY-MM-DD.md`.
- `reports/nightly-ops-audit/latest.json`.
- `reports/nightly-ops-audit/latest.md`.

## Contrato silent-OK

- `rc=0` + stdout vazio: auditoria saudável ou apenas watchlist sem ação imediata.
- `rc=0` + stdout: achado acionável para o digest/operador.
- `rc!=0`: falha do script/auditor, não achado operacional esperado.

## Autoheal A0/A1 permitido

Permitido automaticamente:

- criar diretório local de reports;
- atualizar ponteiros `latest.*`;
- escrever artifacts sanitizados;
- classificar achados e recomendar ação;
- futuramente, com contrato/teste, corrigir metadados documentais locais, receipts ou índices.

Bloqueado sem pacote separado:

- alterar schedules/delivery/enabled de crons;
- reiniciar runtime;
- tocar secrets;
- enviar externo;
- mexer em sistemas produtivos.

## Critérios de saúde

- Cron registries legíveis.
- Jobs ativos com scripts resolvíveis.
- Jobs ativos sem `last_status` non-ok atual.
- Jobs frequentes com `deliver=origin/telegram` entram em watchlist de ruído, não incidente automático.
- `last_status=None` em jobs futuros/novos entra como watch, salvo evidência de atraso.
- Runtime profile snapshot não imprime secrets.
- Digest das 03h inclui status da auditoria.

## Rollback

- Remover ou pausar o cron `Hermes Nightly Operations Audit OS`.
- Restaurar `/opt/data/cron/jobs.json` do backup em `/opt/data/backups/cron-nightly-ops-audit-20260614/` se necessário.
- Remarcar digest para `30 5 * * *` UTC se Lucas quiser voltar para 02h30 BRT.
- Remover instrução do prompt/contexto do digest se o artifact deixar de existir.

## Verificação obrigatória

- `py_compile` do script.
- execução manual do script com `--autoheal --json-only`.
- execução manual em modo cron/silent-OK.
- cron list após criar/remarcar.
- Brain health.
- operational docs guard.
- focused secret scan nos arquivos criados/modificados.
- `git diff --check`.

values_printed: false
