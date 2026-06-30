# Hermes Reddit benchmark — auditoria de manutenção do sistema

Data: 2026-06-29

## Fonte externa relida

Post Reddit: `My Hermes setup, roast me` — r/hermesagent.

A leitura direta via fetch raw foi bloqueada por `robots.txt`; usei `web_extract`/search disponível e a auditoria local anterior. O conteúdo resumido do post descreve um setup Hermes em Apple Silicon Mac com Docker, SearXNG, Hindsight/pgvector, Bitwarden Lite, hermes-pi/cloud routing, LM Studio fallback, Gitea, Obsidian, Telegram review, perfis ativos (`local-admin`, `coder`, `planner`, `qa-tester`, `repository`) e `hermes-bridge.py` host-side para build/deploy/logs/restart.

## Tese do benchmark

O ponto forte do Reddit não é “ter mais ferramentas”. É ter uma operação mais simples de manter:

`tarefa → planner/coder/QA → logs/status/deploy via bridge → documentação → review humano no Telegram`

O setup Lucas/Cimino é mais seguro e mais governado, mas historicamente era menos ergonômico por excesso de skills, perfis, scripts, crons e decisões técnicas chegando no Telegram.

## Audit — o que fizemos

| Frente | Status | Evidência |
|---|---|---|
| Workcell v1 | Feito | Planner → executor → QA independente → reviewer/receipt virou padrão em tarefas materiais. |
| Skill Surface Diet | Feito | Todos os profiles cobertos, config v30, skills protegidas preservadas, heavy skills compactadas. |
| Recorrência da Skill Diet | Feito | Daily silent-OK read-only, weekly supervised, monthly heavy audit; sem auto-apply/restart por cron. |
| Ops Bridge v1 | Feito v1 | `/opt/data/scripts/hermes_ops_bridge_readonly.py`, stdout-only, sem comandos mutáveis. |
| Webhook runaway fix | Feito | `lk-stock-shopify-sales-os` virou fast-ack + queue + flock + cooldown; 0 órfãos no fechamento. |
| Telegram UX | Parcial/feito operacional | Mais silent-OK e decisão executiva, mas ainda falta consolidar score/contrato em todos os relatórios. |
| Config hygiene | Feito forte | Profiles migrados para v30; status atual sem profiles fora de v30. |
| Cron hygiene | Melhorado | Ops Bridge lê 108 jobs, 90 enabled, 18 paused, 0 enabled non-ok. |

## Estado atual medido

- Ops Bridge status: `profiles_configured=16`, `gateways_running=13`, `profiles_without_v30=[]`.
- API/webhook enabled: apenas `default` PID 1, esperado para Main/local health.
- Cron inventory: `jobs=108`, `enabled=90`, `paused=18`, `non_ok_enabled=0`.
- Skill Surface Diet recurring latest: todos os profiles com `config_version=30`, política ativa, `protected_disabled=[]` no trecho verificado.

## O que ainda não fizemos

| Gap | Por que importa para manutenção | Próximo formato seguro |
|---|---|---|
| Ops Bridge ainda não tem comando `qa` consolidado | Hoje cada tarefa ainda lembra seus próprios gates; manutenção ideal exige um gate único por classe de tarefa. | v1.1 local read-only: `qa --type brain/runtime/script/cron` sem writes. |
| Ops Bridge não tem visão “maintenance score” | Lucas precisa saber se sistema está saudável sem ler logs/crons/receipts. | Score 0–100 local com categorias: runtime, cron, skills, secrets, Telegram noise. |
| Não existe uma tela única card→receipt→runtime | Task OS existe, mas o elo card/owner/receipt/source ainda não está sempre visível. | Relatório local `maintenance-ledger` alimentado por receipts e cron state. |
| Dashboard/cockpit público não foi ativado | Correto por segurança, mas reduz ergonomia comparado ao Reddit. | Manter bloqueado; se quiser, approval packet separado com auth, 401 público e rollback. |
| Docker/VPS/Traefik observability ainda não virou rotina unificada | O post usa bridge host-side para operações. Aqui evitamos por safety, mas falta uma leitura executiva host-level segura. | Read-only host audit packet separado; sem mutação. |
| Medição de latência/contexto antes/depois da Skill Diet é parcial | Fizemos redução estrutural, mas ainda falta provar ganho operacional por métricas contínuas. | Mensurar tokens/latência/skill-load drift semanal. |
| Telegram Executive UX v2 ainda é contrato, não auditor automático | Pode voltar ruído se relatórios crescerem. | Auditor local de mensagens/cron stdout: ação real vs ruído. |

## Priorização recomendada para melhor manutenção

### P0 — manter rodando bem, sem novo risco

1. Usar Ops Bridge manualmente como primeira leitura antes de qualquer frente de manutenção:
   - `status`
   - `cron-inventory`
   - `health`
   - `logs`
2. Adicionar Ops Bridge `qa` v1.1 local/read-only.
3. Adicionar `maintenance score` local/read-only, sem Telegram quando OK.
4. Revisar warnings do Skill Diet recurring e transformar só warnings acionáveis em Telegram.

### P1 — transformar governança em rotina operacional simples

1. Criar ledger local `card/receipt/source/runtime` para as frentes materiais.
2. Padronizar Telegram Executive UX v2 como auditor de formato, não só guideline.
3. Adicionar no Ops Bridge um resumo “o que mudou desde ontem”.

### P2 — só com approval separado

1. Host/Docker/VPS/Traefik read-only bridge.
2. Dashboard/cockpit público ou API externa.
3. Qualquer comando mutável em bridge: restart, deploy, cron update, external write.

## Veredito

Comparado ao Reddit, já corrigimos os dois maiores gargalos de manutenção: superfície de skills e ponte operacional inicial. O próximo salto não é instalar mais stack; é tornar manutenção previsível e menos dependente de contexto humano:

`Ops Bridge status → maintenance score → QA gate → receipt/ledger → Telegram só decisão ou falha atual`.

Se fizermos isso, o Hermes Lucas/Cimino fica mais robusto que o setup Reddit: mantém a ergonomia de uma fábrica solo, mas com guardrails multiempresa, Doppler-first, receipts, rollback e silent-OK.
