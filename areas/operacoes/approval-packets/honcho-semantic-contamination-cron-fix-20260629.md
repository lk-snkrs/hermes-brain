# Approval packet — corrigir cron Honcho semantic contamination audit — 2026-06-29

Gerado em: 2026-06-29T09:05:58Z

## Pedido / decisão

Lucas clicou **Fazer** na Mesa COO 2026-06-29 para preparar um packet read-only de correção segura do cron Honcho semantic contamination audit.

Escopo autorizado por este clique: **packet/read-only e validação local**.

Não autorizado ainda: alterar cron, criar/substituir script executado automaticamente, Docker/VPS/gateway/restart, mutação/deleção de dados Honcho ou exposição de raw logs/PII/secrets.

## Alvo exato

| Campo | Valor |
|---|---|
| Profile/runtime | `default` |
| Job ID | `ba8ca37bfebd` |
| Nome | `Honcho semantic contamination audit — daily local` |
| Schedule | `40 7 * * *` |
| Delivery | `local` |
| no_agent | `true` |
| Script configurado | `honcho_semantic_contamination_daily.py` |
| Status vivo | `last_status=error` |
| Erro | `Script not found: /opt/data/scripts/honcho_semantic_contamination_daily.py` |
| Script funcional existente | `/opt/data/scripts/honcho_semantic_contamination_auditor.py` |

## Evidência read-only coletada

1. `cronjob list` vivo mostra o job `ba8ca37bfebd` ativo/scheduled com `last_status=error` e script `honcho_semantic_contamination_daily.py`.
2. Output do cron em `/opt/data/cron/output/ba8ca37bfebd/2026-06-29_07-40-05.md` registra:
   - `Status: script failed`
   - `Script not found: /opt/data/scripts/honcho_semantic_contamination_daily.py`
3. Busca local em `/opt/data/scripts` confirma:
   - ausente: `honcho_semantic_contamination_daily.py`
   - presente: `honcho_semantic_contamination_auditor.py`
4. O auditor existente compilou com sucesso:
   - `python3 -m py_compile /opt/data/scripts/honcho_semantic_contamination_auditor.py` → `py_compile_ok`
5. Execução read-only/sanitizada do auditor existente com `--report` retornou:
   - `status=attention`
   - `score=55`
   - `result_count=32`
   - `contamination_ratio=0.75`
   - `values_printed=false`
   - `raw_examples_printed_any=false`

## Diagnóstico

O problema atual é de **target/runtime do cron**, não de provider Honcho indisponível:

- `configured`: job existe e está enabled/scheduled.
- `active`: scheduler executou na janela de 07:40 UTC.
- `functioning`: falha antes de rodar lógica porque o script configurado não existe.
- `protocol_aware`: o auditor existente é sanitizado, não imprime raw excerpts/PII/secrets e trata Honcho como camada auxiliar, não fonte viva.
- `useful`: a lógica existente detecta contaminação semântica residual e classifica como `attention`, mas o cron diário não está publicando/atualizando por apontar para wrapper ausente.

## Opções de correção

### Opção A — recomendada: criar wrapper compatível no target atual

Criar `/opt/data/scripts/honcho_semantic_contamination_daily.py` como wrapper mínimo para chamar o auditor existente com o comportamento pretendido pelo cron diário:

```python
#!/usr/bin/env python3
import runpy
import sys

sys.argv = [
    "/opt/data/scripts/honcho_semantic_contamination_auditor.py",
    "--write-latest",
]
runpy.run_path("/opt/data/scripts/honcho_semantic_contamination_auditor.py", run_name="__main__")
```

**Efeito esperado:** o job existente volta a rodar sem mudar schedule/delivery/job id. Como `--write-latest` não passa `--report`, ele mantém o contrato do auditor: stdout vazio quando `ok/watch`; stdout sanitizado apenas quando `attention/degraded`.

**Vantagens:**
- preserva job id, schedule, delivery e histórico;
- corrige exatamente o `Script not found`;
- evita mexer no registry do cron;
- rollback simples: remover/renomear o wrapper criado.

**Risco/limite:** criação de script sob `/opt/data/scripts` que será executado automaticamente pelo cron; exige aprovação escopada antes de aplicar.

### Opção B — alterar o cron para apontar diretamente para o auditor existente

Atualizar `ba8ca37bfebd` para `script=honcho_semantic_contamination_auditor.py`.

**Não recomendado como primeira opção** porque o cron script field não carrega argumentos; sem wrapper, perderia o `--write-latest` pretendido pelo prompt/rotina, a menos que também se altere o auditor ou a semântica do cron.

### Opção C — pausar o cron

Pausar `ba8ca37bfebd` até redesenhar a rotina.

**Não recomendado** porque remove cobertura diária de contaminação semântica, enquanto já existe auditor funcional e a correção de target é pequena.

## Plano de execução se Lucas aprovar a Opção A

1. Criar backup/pre-state:
   - confirmar que `/opt/data/scripts/honcho_semantic_contamination_daily.py` continua ausente;
   - registrar `cronjob list` do job `ba8ca37bfebd` antes da alteração.
2. Criar wrapper `/opt/data/scripts/honcho_semantic_contamination_daily.py` com permissão executável.
3. Verificar:
   - `python3 -m py_compile /opt/data/scripts/honcho_semantic_contamination_daily.py`
   - executar wrapper manualmente em modo cron e confirmar output sanitizado;
   - confirmar que `/opt/data/state/honcho-semantic-contamination/latest.json` foi atualizado e contém `values_printed=false`.
4. Rodar o job uma vez via scheduler (`cronjob run ba8ca37bfebd`) **somente se essa ação estiver incluída na aprovação**, pois executa a rotina configurada.
5. Readback:
   - `cronjob list` mostra `last_status=ok` depois do run ou depois da próxima janela natural;
   - último output do job não contém raw excerpts/PII/secrets;
   - state latest tem `values_printed=false` e `raw_examples_printed=false` por query.

## Rollback

Se houver comportamento inesperado:

1. Remover o wrapper criado:
   - `rm /opt/data/scripts/honcho_semantic_contamination_daily.py`
2. Confirmar que o cron volta ao estado anterior conhecido (`script not found`) ou, se preferível, pausar o job com aprovação separada.
3. Nenhuma ação de rollback em Honcho DB/provider é necessária porque a correção não deve apagar/mutar mensagens, peers, sessions, conclusions ou embeddings.

## Aprovação solicitada

Aprovar **Opção A — criar wrapper compatível no target atual** para o job `ba8ca37bfebd`, com:

- escopo: criar apenas `/opt/data/scripts/honcho_semantic_contamination_daily.py`, permissões executáveis e validação local/scheduler;
- sem Docker/VPS/gateway/restart;
- sem alteração de schedule/delivery/job id;
- sem deleção/mutação de dados Honcho;
- rollback por remoção do wrapper;
- readback por `py_compile`, execução sanitizada, `latest.json` e `cronjob list`.

## Alternativas de botão/decisão

- **Aprovar Opção A** — criar wrapper e validar.
- **Preferir Opção B** — mudar target do cron, sabendo do problema de argumentos.
- **Pausar cron** — remover alerta/erro agora, aceitando perda de cobertura diária.
- **Não fazer** — manter estado atual e reavaliar depois.
