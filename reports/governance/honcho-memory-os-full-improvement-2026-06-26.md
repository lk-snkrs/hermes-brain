# Honcho / Memory OS — melhoria completa governada — 2026-06-26

## Pedido

Lucas pediu: “Melhorar tudo”.

Escopo executado:

1. Mapear ponto real de ingestão Honcho no runtime Hermes.
2. Implementar filtro/classificador sanitizado para impedir nova promoção de eventos operacionais/PII ao peer `lucas`.
3. Implementar utility scoring Honcho/Brain.
4. Exportar candidatos de limpeza histórica de forma sanitizada/read-only.
5. Integrar novos sinais ao Memory OS maintenance audit.

## Veredito

Melhoria local/governada executada. Não houve deleção Honcho, external write, Docker/VPS/Traefik, secret/env write ou restart de gateway.

Estado final:

| Gate | Resultado |
|---|---|
| Honcho technical quality | `ok`, score `92/100` |
| Honcho semantic | `attention`, score `55/100`, contamination ratio `0.75` |
| Honcho utility score | `attention`, score `80/100` |
| Ingestion filter unit test | passed, 4/4 cases |
| Cleanup candidate export | `attention`, 92 candidates, raw content not printed |
| Cleanup safe to delete now | `false` |
| Memory hygiene | `ok` |
| Boot memories >80% | `0` from previous cycle |

## 1) Runtime ingestion mapping

Ponto real de persistência encontrado:

```text
/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/plugins/memory/honcho/session.py
HonchoSessionManager._flush_session()
```

Esse método transforma mensagens locais não sincronizadas em `peer.message(...)` e chama:

```python
honcho_session.add_messages(honcho_messages)
```

## 2) Filtro/classificador Honcho

Patch aplicado em:

```text
/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/plugins/memory/honcho/session.py
```

Backup:

```text
/opt/data/backups/honcho-ingestion-filter/<timestamp>/session.py.before
```

Comportamento novo:

- mensagens de preferência/decisão/política do Lucas continuam elegíveis para Honcho;
- payloads/logs de Shopify/pedido/cliente/webhook/endereço/e-mail/telefone são bloqueados da persistência no Honcho;
- mensagem bloqueada é marcada como sincronizada localmente para não entrar em retry infinito;
- ledger sanitizado registra apenas tags/contagens/hash de sessão, nunca conteúdo bruto.

Ledger sanitizado:

```text
/opt/data/state/honcho-ingestion-filter/events.jsonl
```

Unit test executado:

```text
filter_unit=passed
cases=4
```

Casos cobertos:

- preferência durável → persiste;
- pedido Shopify com contato/endereço → bloqueia;
- decisão/aprovação de política → persiste;
- payload de cliente/telefone/endereço → bloqueia.

## 3) Utility scoring Honcho

Script criado:

```text
/opt/data/scripts/honcho_memory_utility_scorer.py
```

Saídas:

```text
/opt/data/state/honcho-utility/latest.json
reports/memory-hygiene/honcho-utility-latest.json
```

Resultado atual:

```text
status=attention
utility_score=80
technical_score=92
semantic_score=55
contamination_ratio=0.75
memory_hygiene_status=ok
filter_active=true
blockers=[]
```

Interpretação:

- Honcho está tecnicamente saudável;
- filtro novo melhora ingestão futura;
- histórico contaminado ainda puxa utility para `attention`.

## 4) Cleanup candidate export

Script criado:

```text
/opt/data/scripts/honcho_cleanup_candidate_export.py
```

Saídas:

```text
/opt/data/state/honcho-cleanup-candidates/latest.json
reports/memory-hygiene/honcho-cleanup-candidates-latest.json
```

Resultado atual:

```text
candidate_count=92
raw_content_printed=false
safe_to_delete_now=false
```

Motivo para não deletar agora:

- há hashes/candidatos;
- mas não há confirmação de granularidade segura de delete por mensagem + rollback snapshot;
- deleção por heurística seria perigosa.

## 5) Maintenance audit integrado

Atualizado:

```text
/opt/data/scripts/hermes_memory_os_maintenance_audit.py
```

Agora inclui:

- Honcho quality;
- Honcho semantic contamination;
- Honcho utility score;
- status do filtro de ingestão;
- quantidade de candidatos de cleanup;
- flag `cleanup_safe_to_delete_now`.

## Non-actions

- Não deletei memória Honcho.
- Não alterei Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/database.
- Não mexi em Docker/VPS/Traefik/secrets/env.
- Não reiniciei gateway/runtime.
- Não imprimi PII, payloads, emails, endereços, tokens ou secrets.

## Limite importante

O patch no arquivo do plugin entra em efeito para processos que carregarem esse código após restart/import novo. O gateway já em execução pode precisar de restart controlado para ativar o filtro no runtime vivo.

Como este pedido não incluiu restart explícito, não reiniciei gateway/Docker.

## Próximo passo recomendado

Se Lucas aprovar restart controlado:

1. backup já existe;
2. reiniciar apenas gateway/profile necessário;
3. enviar uma amostra sintética/no-op ou observar próximo evento real;
4. verificar `honcho-ingestion-filter/events.jsonl` com `raw_content_logged=false`;
5. rodar utility/semantic novamente após alguns ciclos.

Para limpeza histórica:

- só executar com provider rollback/snapshot e confirmação de operação por IDs;
- nunca deletar por heurística cega.
