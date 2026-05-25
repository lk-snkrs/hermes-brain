# Task Router — Fase 6C Reply Context Routing Fix

Data: 2026-05-24
Status: implementado em disco; exige restart controlado do gateway para ativar no processo vivo

## Problema encontrado

Após ativar o preflight, mensagens enviadas como reply no Telegram podem chegar ao runtime com um envelope de contexto no formato:

```text
[Replying to: "<trecho da mensagem anterior>"]

<instrução atual do Lucas>
```

O Task Router estava classificando o texto completo. Assim, palavras presentes apenas na mensagem citada — por exemplo `spiti`, `lote`, `bidder`, `lk-growth` — podiam contaminar a rota da instrução atual `Seguir`.

## Correção

Arquivo alterado:

- `/opt/hermes/agent/lucas_task_router.py`

Mudança:

- adicionada função `_current_request_text()`;
- antes de classificar, o preflight remove o envelope `[Replying to: ...]` e usa somente a instrução atual;
- também há defesa contra reentrada acidental de bloco interno de preflight, roteando pelo trecho limpo após `Original user request:`.

## Teste RED/GREEN

Arquivo alterado:

- `/opt/hermes/tests/agent/test_lucas_task_router_preflight.py`

Novo caso cobre:

- texto citado contendo SPITI/lote/bidder/Hub;
- instrução atual sendo apenas `Seguir`;
- rota esperada: `general-research-content` / `hermes-geral`, não `spiti-os`.

RED observado:

```text
AssertionError: assert 'spiti-os' == 'general-research-content'
```

GREEN após correção:

```text
1 passed
```

## Verificação final

Comando:

```bash
/opt/hermes/.venv/bin/python -m pytest tests/agent/test_lucas_task_router_preflight.py tests/cron/test_scheduler.py::TestDeliverResultWrapping -q -o 'addopts=' && \
python3 /opt/data/hermes_bruno_ingest/hermes-brain/scripts/test_hermes_task_router.py
```

Resultado:

```text
16 passed, 1 warning
Ran 5 tests
OK
```

Compilação:

```bash
PYTHONPYCACHEPREFIX=/tmp/hermes-pycache /opt/hermes/.venv/bin/python -m py_compile agent/lucas_task_router.py run_agent.py
```

Resultado: exit 0.

Smoke local:

```text
general-research-content hermes-geral executar_aqui
```

## Escopo

Não houve:

- write externo;
- alteração Shopify/GMC/Klaviyo/Meta/WhatsApp;
- mutação de cron registry;
- hard blocker de ferramentas ainda.

## Próximo passo

1. ativar a correção com restart controlado do gateway principal;
2. verificar API/webhook/Telegram;
3. só então avançar para o hard blocker do dispatcher de ferramentas.
