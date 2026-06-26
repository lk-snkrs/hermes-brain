# Audit — Task OS, LK OS e roteamento real dos agentes (2026-06-25)

Generated at: `2026-06-25T17:56:59.283284+00:00`

## Pergunta auditada

> Tudo vai rodar dentro do LK OS?

## Veredito

**Não literalmente — e isso é correto.**

O modelo seguro é:

1. **Hermes Task OS** é a camada universal de governança para todos os agentes: tarefa rastreável, handoff, receipt, aprovação e evidência.
2. **LK OS** é a camada operacional da LK Sneakers. Todo trabalho **da LK** deve ser roteado para LK OS / especialistas LK, não para Zipper, SPITI, Mordomo ou default por conveniência.
3. Zipper, SPITI, Mordomo e governança Hermes continuam fora do LK OS, mas dentro do Task OS universal.

Portanto, a resposta curta é: **todo trabalho LK deve passar pelo LK OS; nem todo Hermes deve rodar dentro do LK OS.**

## Evidência — profiles e política Task OS

| Escopo | Profiles | AGENTS Task OS | SOUL Task OS | Identidade LK |
|---|---:|---:|---:|---:|
| LK | 10 | 10/10 | 10/10 | 10/10 |
| Global/outros | 7 | 7/7 | 7/7 | não deve ser LK |

### Profiles LK cobertos

- `lk-analyst-readonly` — AGENTS=1, SOUL=1, LK identity=sim
- `lk-collection-optimizer` — AGENTS=1, SOUL=1, LK identity=sim
- `lk-content` — AGENTS=1, SOUL=1, LK identity=sim
- `lk-content-reviewer` — AGENTS=1, SOUL=1, LK identity=sim
- `lk-finance` — AGENTS=1, SOUL=1, LK identity=sim
- `lk-growth` — AGENTS=1, SOUL=1, LK identity=sim
- `lk-ops` — AGENTS=1, SOUL=1, LK identity=sim
- `lk-shopify` — AGENTS=1, SOUL=1, LK identity=sim
- `lk-stock` — AGENTS=1, SOUL=1, LK identity=sim
- `lk-trends` — AGENTS=1, SOUL=1, LK identity=sim

## Evidência — gateways vivos

Gateways Hermes vivos detectados: **12**.

| Profile | API | Webhook |
|---|---:|---:|
| `default` | `true` | `true` |
| `lk-collection-optimizer` | `false` | `false` |
| `lk-content` | `false` | `false` |
| `lk-finance` | `false` | `false` |
| `lk-growth` | `false` | `false` |
| `lk-ops` | `false` | `false` |
| `lk-shopify` | `false` | `false` |
| `lk-stock` | `false` | `false` |
| `lk-trends` | `false` | `false` |
| `mordomo` | `false` | `false` |
| `spiti` | `false` | `false` |
| `spiti-atendimento` | `false` | `false` |

## Evidência — crons e automações LK

LK-related cron jobs encontrados: **54**.

Distribuição por scheduler/registry:

| Registry | Total LK jobs | Ativos |
|---|---:|---:|
| `default` | 19 | 17 |
| `lk-content` | 5 | 4 |
| `lk-growth` | 11 | 8 |
| `lk-ops` | 9 | 7 |
| `lk-shopify` | 2 | 2 |
| `lk-stock` | 4 | 4 |
| `lk-trends` | 2 | 1 |
| `mordomo` | 2 | 2 |

### Finding principal

Ainda existem **19 LK-related jobs no scheduler `default`**. Isso não significa que eles estejam errados, mas significa que **nem tudo que é LK está fisicamente dentro dos profiles `lk-*`** hoje.

Classificação:

- Jobs agent-driven com `workdir=/opt/data/hermes_bruno_ingest/hermes-brain`: aceitáveis como governança central/Brain/Mesa COO, desde que roteiem LK para LK OS quando há execução operacional.
- Jobs `no_agent=true`/scripts: não “sabem” Task OS como LLM; precisam ter contrato script-level: fonte, silent-OK, receipt/handoff, e delegação/roteamento para profile LK quando houver decisão operacional.
- Jobs LK operacionais recorrentes no `default`: candidatos a migração gradual para scheduler/profile LK correspondente, mas isso é mudança de cron/runtime e precisa de approval packet separado.

Default LK jobs detectados:

| Job | Ativo | no_agent | Script/workdir | Classificação |
|---|---:|---:|---|---|
| `LC Hermes daily intelligence loop — systemwide audit + self-improvement` | True | None | `hermes_daily_intelligence_preflight.py` | governança Brain/Mesa |
| `LK Daily Sales Brief read-only mandatory delivery` | True | True | `lk_daily_sales_brief_watchdog.py` | script no-agent LK |
| `LK Weekly CEO Review read-only mandatory delivery` | True | True | `lk_weekly_ceo_review_watchdog.py` | script no-agent LK |
| `LK Pulso Comercial 16h read-only delivery` | True | True | `lk_financial_pulse_16h_watchdog.py` | script no-agent LK |
| `LK 09h previous-day sales report external delivery` | True | True | `lk_previous_day_09h_sales_report_watchdog.py` | script no-agent LK |
| `LK 19h30 physical store close external delivery` | True | True | `lk_store_close_1930_watchdog.py` | script no-agent LK |
| `LK Growth Telegram gateway watchdog` | False | True | `lk_growth_gateway_watchdog.sh` | script no-agent LK |
| `Mesa COO diária Telegram` | True | False | `/opt/data/hermes_bruno_ingest/hermes-brain` | governança Brain/Mesa |
| `Hermes Brain Fechamento Ágil 01h + Brain Sync` | True | False | `/opt/data/hermes_bruno_ingest/hermes-brain` | governança Brain/Mesa |
| `Lucas Brain weekly Learning Loop report` | True | False | `/opt/data/hermes_bruno_ingest/hermes-brain` | governança Brain/Mesa |
| `Hermes Brain Runtime Truth Reconciler` | True | False | `/opt/data/hermes_bruno_ingest/hermes-brain` | governança Brain/Mesa |
| `Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram` | True | False | `/opt/data/hermes_bruno_ingest/hermes-brain` | governança Brain/Mesa |
| `LK Weekly Collection Sort Rule B` | True | True | `lk_weekly_collection_sort_ruleB_apply_recurring.sh` | script no-agent LK |
| `LK Weekly Catalog Badges BEST SELLER sync` | True | True | `lk_catalog_badges_weekly_sync.sh` | script no-agent LK |
| `LK specialist Telegram gateway watchdog` | False | True | `lk_specialist_gateways_watchdog.py` | script no-agent LK |
| `Hermes all Telegram gateways watchdog` | True | True | `hermes_all_gateway_watchdog.py` | script no-agent LK |
| `LK Tiny stock local DB daily fullsync` | True | True | `lk_tiny_stock_fullsync_watchdog.py` | script no-agent LK |
| `LK POS pós-compra WhatsApp auto-worker` | True | True | `lk_pos_postpurchase_auto_worker_once.py` | script no-agent LK |
| `LK POS Shopify→fila reconciliador` | True | True | `lk_pos_postpurchase_shopify_reconciler_cron.sh` | script no-agent LK |

## Kanban Task OS

Status board `hermes-task-os`:

```json
{
  "status_counts": [
    {
      "status": "archived",
      "count": 16
    },
    {
      "status": "blocked",
      "count": 3
    },
    {
      "status": "done",
      "count": 5
    }
  ],
  "open_items": [
    {
      "id": "t_6fbf8d6c",
      "title": "Backlog seguro — capability-status plugin mini-PRD",
      "status": "blocked",
      "assignee": null
    },
    {
      "id": "t_6e404c9e",
      "title": "Backlog seguro — política deliverable mode e receipts",
      "status": "blocked",
      "assignee": null
    },
    {
      "id": "t_8d2cea05",
      "title": "Backlog seguro — revalidar LK Growth antigo antes de execução",
      "status": "blocked",
      "assignee": null
    }
  ]
}
```

## Decisão operacional recomendada

Não transformar LK OS em “container universal” de tudo. O desenho correto é:

```text
Hermes Task OS = camada universal de tarefas/receipts/aprovação
LK OS = domínio operacional da LK Sneakers
Zipper OS = domínio Zipper
SPITI OS = domínio SPITI
Mordomo = pessoal/inbox/follow-up
Hermes/Infra = runtime, Brain, gateway, cron, secrets, governança
```

## Lacunas reais encontradas

1. **LK jobs ainda no scheduler default:** 19 encontrados, 17 ativos.
2. **Scripts no-agent não absorvem AGENTS/SOUL:** eles precisam de contrato próprio no script ou wrapper; Task OS para scripts é por output/receipt/handoff, não por prompt.
3. **Governança central pode conter LK:** Mesa COO/Brain daily podem ler LK, mas não devem executar operacional LK por conveniência; devem rotear para LK OS/especialistas.

## Não executado

- Nenhum cron migrado.
- Nenhum scheduler alterado.
- Nenhum Docker/VPS/Traefik/secrets/deploy alterado.
- Nenhum write externo.

## Próximo bloco seguro

Criar um approval packet de migração gradual dos LK cron jobs do `default` para os profiles LK corretos, começando por `no_agent` script jobs, com:

- inventário job-by-job;
- dono LK correto (`lk-stock`, `lk-ops`, `lk-content`, `lk-growth`, `lk-shopify`, etc.);
- plano de pausa/criação/rollback;
- dry-run por job;
- verificação de entrega silent-OK/Telegram;
- janela de ativação.

## Conclusão

**Task OS universal está coberto. LK OS está coberto para os agentes LK. Mas nem toda automação LK roda fisicamente dentro dos profiles LK hoje.**

A arquitetura correta é federada: global Task OS + roteamento por OS de domínio. Para LK, a próxima melhoria é migrar/normalizar cron/script ownership para LK OS sem quebrar rotinas existentes.
