# Superpowers OS — digest e encaixe no relatório Hermes 02h30

Data: 2026-06-02
Status: documentado; sem alteração de cron/delivery

## Digest gerado

- Script criado: `/opt/data/hermes_bruno_ingest/hermes-agent-upstream/scripts/superpowers_os_daily_digest.py`.
- Digest local gerado: `/opt/data/home/.hermes/superpowers/digests/2026-06-02.md`.
- Espelho no Brain: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/superpowers-os-digest-2026-06-02.md`.
- Contrato: o script só escreve arquivos locais e imprime o caminho do digest; não envia Telegram.

Resumo do digest de 2026-06-02:

```text
Superpowers OS — resumo diário
Score: 6/100 🔴
Data: 2026-06-02 · Perfil: default

- Eventos avaliados: 47.
- Violações/atenções: 6.
- Sem decisões pendentes.
```

Nota: esse score é baseline observe-only inicial. Não significa bloqueio de runtime; serve para calibração antes de qualquer modo warn/soft-block.

## Cron de memória 02h15 identificado

Cron vivo:

- `job_id`: `f9a1d43caf48`
- Nome: `Hermes memory hygiene watchdog 02h15 BRT`
- Schedule: `15 5 * * *` UTC = 02h15 BRT
- Entrega: `local`
- Tipo: `no_agent=true`
- Script: `/opt/data/scripts/hermes_memory_hygiene_watchdog.py`
- Última execução lida: `2026-06-02T05:15:31.456751+00:00`
- Último status: `ok`
- Erro de entrega: nenhum

O que ele verifica:

- Saturação das memórias `MEMORY.md`/`USER.md` do perfil default e perfis especialistas.
- Possíveis localizadores de secrets em arquivos de memória.
- Se Mem0/Honcho/provider externo parece ativo contra a decisão atual do Lucas.
- Linguagem ativa de reabertura de Mem0 em docs de governança.

Contrato de saída:

- `rc=0` + stdout vazio = OK/silent-OK.
- `rc=0` + stdout com texto = alerta acionável.
- Escreve receipt sanitizado local em `/opt/data/hermes_bruno_ingest/hermes-brain/reports/memory-hygiene/latest.json`.

Último receipt lido:

- Status: `ok`.
- Alertas sanitizados: `0`.
- Mem0/provider externo ativo: não indicado.
- Memória default: `MEMORY.md` ~62,5%; `USER.md` ~83,1%.

## Encaixe recomendado no relatório Hermes 02h30

Relatório Telegram existente:

- `job_id`: `98478b820720`
- Nome: `Relatório Hermes diário 01h + 02h + 02h15 para Lucas`
- Schedule: `30 5 * * *` UTC = 02h30 BRT
- Entrega: `origin`
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain`

Seção curta recomendada para adicionar ao relatório 02h30, sem criar novo cron:

```text
Memória 02h15:
- Watchdog de higiene de memória rodou em silent-OK: status ok, sem alertas, sem Mem0/provider externo ativo.
- Uso atual: MEMORY ~62,5%; USER ~83,1%; sem secrets detectados no receipt.

Superpowers OS:
- Digest observe-only gerado localmente e espelhado no Brain.
- Score baseline: 6/100, 47 eventos avaliados, 6 atenções; sem decisão pendente.
- Próximo passo seguro: calibrar baseline antes de qualquer warn/soft-block.
```

## Decisão/guardrail

Não alterei o cron `98478b820720` nesta execução porque ele entrega em Telegram (`origin`). A recomendação está pronta; aplicar a alteração do prompt/delivery do relatório 02h30 deve ser feito só com aprovação explícita de escopo.
