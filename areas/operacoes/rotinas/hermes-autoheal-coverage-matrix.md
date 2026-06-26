# Matriz de Cobertura — Hermes Autoheal

Status: canônica / local-read-only  
Criada em: 2026-06-14  
Contrato pai: `hermes-auto-remediation-contract.md`  
PRD pai: `../prds/hermes-systemwide-auto-remediation-prd-2026-06-14.md`

## Objetivo

Separar claramente três estados que antes ficavam misturados:

1. **Detector existe** — o sistema percebe erro, falha, timeout, drift ou status não OK.
2. **Autoheal permitido** — a correção é A0/A1, local, reversível, secret-free e verificável.
3. **Approval obrigatório** — a correção cruza produção, externo, runtime sensível, secrets, contas, Docker/VPS/Traefik, banco, campanhas, WhatsApp/e-mail ou write API.

Regra curta: detectar problema não implica autorização para corrigir tudo; implica que o sistema deve **corrigir automaticamente quando seguro** ou **gerar approval packet específico quando não for seguro**.

## Matriz executiva

| Superfície | Detector / watchdog | Autoheal automático permitido | Quando virar approval packet | Estado atual |
|---|---|---|---|---|
| Hermes Geral / sessão interativa | Erros de execução, falhas de ferramenta, gaps de contexto, docs inconsistentes | Corrigir docs/skills/rotinas locais, rerodar checks, registrar receipt quando material | Prod/runtime/secrets/externo ou write sensível | Coberto por regra sistêmica e skills centrais |
| Brain Governance | `brain_health_check.py`, `operational_docs_guard.py`, auditorias locais | Corrigir links/docs/MAPAs/índices/receipts/skills quando A0/A1 | Runtime, cron schedule/delivery, Git push se não aprovado, secrets | Coberto e usado nas waves |
| Auto-Remediation Contract audit | `scripts/auto_remediation_contract_audit.py` | Identificar candidatos e adicionar contrato/comentário seguro | Executar scripts produtivos, mexer em secrets ou corrigir integração externa | Coberto; 75 candidatos remanescentes approval-gated |
| Cron registry governance | Auditor cron + metadata `auto_remediation_contract` | Adicionar metadados/contratos sem mudar schedule/delivery/enabled/state | Alterar cron vivo, destino Telegram/local, enabled/state, schedule, script produtivo | Coberto para 6/6 candidatos; crons pendentes 0 |
| No-agent watchdogs locais | Scripts silent-OK com `stdout` vazio em OK | Tratar exceções locais esperadas, retry local, relatório sanitizado, `rc=0` quando recuperado | Gateway/container restart, reconexão de conta, cron mutation, external send | Parcialmente coberto; revisar por superfície quando surgirem falhas |
| Memory OS / Brain OS | Checkers diurnos, scorecards, hygiene watchdogs | Compactação/refresh local, templates, receipts, regression tests locais | Provider externo, profile restart, alteração runtime, secrets | Coberto por skills e rotinas existentes |
| Reminder OS | Ledger/health/watchdog de loops abertos | Registrar/fechar gaps documentais e loops owner-safe | Executar tarefa lembrada, contato externo, produção | Coberto conceitualmente; execução de tarefa segue approval/specialist owner |
| Runtime Truth / profiles | Reconciliadores read-only, status de gateway/profile | Corrigir documentação e reports; preparar diagnóstico sanitizado | Restart gateway, Docker/VPS/Traefik, token, account reconnect | Approval-gated salvo escopo local explicitamente permitido |
| LK Growth endpoints | `LK AI/GEO Endpoints Monitor` | Retry/read-only, JSON sanitizado, alerta acionável de drift | Deploy, publish, Shopify/theme/GMC write, credenciais | Coberto por contrato do cron |
| Mordomo observability | `LC Mordomo OS observability drift monitor` | Evidência local sanitizada, silent-OK saudável | WhatsApp/e-mail/account reconnect, gateway/restart, secrets | Coberto por contrato do cron |
| Gmail/draft engines pausados | Jobs draft-only pausados | Nenhum enquanto pausado; se reativado, draft-only dentro de guardrails | Envio real, reconnect, mudança externa, schedule/delivery | Approval-gated / pausado |
| Scripts produtivos/secret-like remanescentes | Auditor marca `secret_like_pattern_seen_review_redaction` | Nenhuma execução automática; apenas comentário/contrato e análise sanitizada | Qualquer execução, alteração de valor, chamada externa, write API | 75 candidatos em backlog controlado |

## Critérios de autoheal A0/A1

Autoheal pode rodar sem nova pergunta quando todos os itens abaixo são verdadeiros:

- a causa é local e objetiva;
- a correção é reversível;
- não lê/imprime valores de secrets;
- não altera credenciais;
- não altera produção, banco, Docker, VPS, Traefik, gateway ou conta externa;
- não envia mensagem/e-mail/WhatsApp/newsletter/post;
- não muda cron `schedule`, `delivery`, `enabled` ou `state`;
- há verificação clara após a correção;
- OK saudável fica silent-OK, sem Telegram de sucesso rotineiro.

## Critérios de approval packet

Gerar approval packet quando qualquer item abaixo aparecer:

- write externo/produtivo;
- produção, banco, Shopify, Tiny, GMC, Klaviyo, Meta, Supabase, n8n;
- WhatsApp, Gmail/e-mail, newsletter, customer-facing;
- Docker, VPS, SSH, root, Traefik, gateway/restart;
- secrets, tokens, passwords, service accounts, account reconnect;
- cron schedule/delivery/enabled/state;
- execução de script legado/produtivo sem prova de segurança.

Packet mínimo:

```text
Alvo: [sistema/script/job]
Problema detectado: [causa]
Ação proposta: [comando/procedimento]
Escopo máximo: [limites]
Risco: [A2/A3/A4]
Rollback: [como voltar]
Verificação/readback: [como provar]
Valores secretos impressos: false
```

## Cobertura atual verificada em 2026-06-14

- Auditor final: `status=ok`.
- Arquivos varridos: `616`.
- Candidatos file restantes: `75`.
- Candidatos cron restantes: `0`.
- `values_printed=false`.
- Wave 3 tratou 95 candidatos canônicos: 72 com comentário/contrato, 23 com `DEPRECATED / DO NOT RUN`, 95 approval packets sanitizados.
- Restantes são backlog controlado, não prova de falha viva.

## Como usar esta matriz

Quando um relatório ou watchdog disser “problema detectado”:

1. Localizar a superfície na matriz.
2. Se a correção cair em A0/A1, executar e verificar.
3. Se cruzar boundary sensível, parar execução e gerar approval packet.
4. Registrar aprendizado em skill/rotina/receipt quando recorrente ou sistêmico.
5. Alertar Lucas só se houver decisão, exceção, falha atual ou ação necessária.

## Próxima revisão

A reanálise dos 75 candidatos restantes está agendada para 72h após a wave de 2026-06-14. A decisão esperada nessa revisão é uma destas:

- manter backlog sem ação;
- propor uma wave pequena por classe de risco;
- pedir approval escopado para um subconjunto específico;
- converter algum detector em autoheal A0/A1 se houver prova de segurança.
