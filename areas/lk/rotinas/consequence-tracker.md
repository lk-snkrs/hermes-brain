# Rotina — Consequence Tracker LK

## O que roda

Registro de efeitos esperados e observados após ações sugeridas ou executadas pelo Hermes no contexto LK.

Script relacionado:

- `scripts/consequence_tracker.py`

## Quando usar

- Depois de campanha aprovada.
- Depois de alteração operacional relevante.
- Depois de uma recomendação do Hermes produzir impacto mensurável.

## Loop Hermes

```text
ação → resultado esperado → resultado observado → severidade → aprendizado → ajuste de processo
```

## Ferramentas e dados

- Supabase LK `cnjimxglpktznenpbail`.
- Tabela `lk_intel.consequence_log`.

## Credenciais

Buscar em Doppler `lc-keys/prd`; nunca versionar valores.

- `SUPABASE_ACCESS_TOKEN` ou `SUPABASE_MANAGEMENT_TOKEN`.

## Verificação

1. Rodar script via Doppler com `action_id`, esperado e observado.
2. Confirmar retorno de ID inserido.
3. Se severidade for alta, atualizar `memories/lessons.md` ou área LK correspondente.
