# Task Router técnico v1 — 2026-05-24

## Escopo

Implementação local/read-only da Fase 5 do Task Router Hermes para converter pedidos de Lucas em metadados de rota, executor, risco e aprovação.

Não houve alteração de runtime/gateway/Docker/crons nem writes externos.

## Arquivos criados

- `scripts/hermes_task_router.py`
- `scripts/test_hermes_task_router.py`

## Arquivo atualizado

- `empresa/contexto/task-router-hermes.md`

## Contrato CLI

```bash
python3 scripts/hermes_task_router.py "faz uma source page da LK para New Balance 530 e publica no Shopify"
```

Retorna JSON com:

- `route_id`
- `context`
- `task_type`
- `orchestrator`
- `executor`
- `runtime_profile`
- `action`
- `output_path`
- `allowed_without_approval`
- `requires_approval`
- `handoff_required`
- `rationale`

## Rotas cobertas na v1

1. `lk-growth-content`
   - Executor: `lk-growth`
   - Runtime: `/opt/data/profiles/lk-growth`
   - Bloqueia/packet para Shopify/GMC/Klaviyo/Meta/produção.

2. `mordomo-personal-intake`
   - Executor: `mordomo`
   - Runtime: `/opt/data/profiles/mordomo`
   - Bloqueia preço, disponibilidade, reserva, negociação, reclamação, fornecedor/compra, campanha/bulk e promessa material.

3. `spiti-os`
   - Executor: `spiti`
   - Runtime: `/opt/data/profiles/spiti`
   - Bloqueia/packet para bidder/cliente, banco/write, deploy, publicação e lote/lance sem fonte oficial.

4. `zipper-os-readonly-comm-crm`
   - Executor: `zipper-documental-readonly`
   - Runtime dedicado: `None` por enquanto.
   - Bloqueia contato externo, proposta, preço e logística sensível.

5. `hermes-ops-brain-governance`
   - Executor: `hermes-geral`
   - Runtime: `/opt/data`
   - Permite documentação/auditoria local; packet para cron novo, restart, Docker/VPS/Traefik/secrets.

6. `general-research-content`
   - Fallback quando nenhum dono especialista claro é detectado.

## TDD / verificação

Teste escrito antes do script e verificado como RED por ausência do arquivo.

GREEN:

```text
python3 scripts/test_hermes_task_router.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.248s

OK
```

## Limitações assumidas

- Classificador é heurístico, não LLM.
- Ainda não intercepta automaticamente mensagens Telegram/gateway.
- Ainda não migra tarefa para outro profile sozinho.
- Ainda não grava handoff automaticamente.
- Ainda não altera crons por dono.

Essas limitações são intencionais para manter a primeira Fase 5 sem risco de produção.

## Próximo degrau recomendado

Fase 5B, com approval separado se mexer em runtime:

1. Rodar `hermes_task_router.py` como preflight em rotinas/cron/Mesa COO ou no agente principal.
2. Anexar `route_id`, `executor` e `action` ao contexto da tarefa.
3. Quando `executor != hermes-geral`, impedir o Hermes Geral de produzir output final por conveniência.
4. Criar handoff mínimo automático quando um especialista devolver output.
5. Adicionar testes para prompts reais de Lucas em regressão contínua.

## Segurança

- Sem secrets no script/test/report.
- Sem API externa.
- Sem mutation runtime.
- Sem envio externo.
- Sem restart.
