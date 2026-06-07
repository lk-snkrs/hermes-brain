# Rotina — Hermes v0.16 Contexto, sessões e prompt-size

Criado em: 2026-06-06
Escopo padrão: read-only/local/manual. Não ativa cron nem muda configuração.

## Objetivo

Usar as melhorias v0.16 de sessões, contexto e diagnóstico para reduzir lentidão, compressão ruim e perda de nuance em conversas longas.

## Evidência inicial

Snapshot read-only de 2026-06-06:

- `hermes sessions stats`:
  - total sessions: `1240`;
  - total messages: `90950`;
  - database size: `1579.8 MB`.
- `hermes sessions --help` confirma `sessions optimize`:
  - merge de FTS5 segments;
  - `VACUUM`;
  - descrito como sem mudança de dados.
- `hermes prompt-size --help` disponível:
  - roda offline;
  - reporta orçamento fixo do prompt para sessão nova;
  - aceita `--platform` e `--json`.

## Quando usar

Rodar esta rotina quando houver:

- Telegram lento sem causa clara;
- compressão frequente;
- erro de contexto ou fallback de compressão;
- sessão longa com muitas mudanças de assunto;
- especialista demorando por excesso de tools/skills/contexto;
- antes de propor mudança de modelo, restart ou VPS.

## Passos read-only

1. Verificar versão/config:

```bash
hermes --version
hermes config check
```

2. Medir prompt fixo por plataforma:

```bash
hermes prompt-size --platform telegram --json
hermes prompt-size --platform cli --json
```

3. Medir session store:

```bash
hermes sessions stats
```

4. Se a sessão atual estiver grande demais:

- usar `/undo` para corrigir direção recente;
- usar `/new` para nova fase;
- usar `session_search` para recuperar fatos antigos;
- promover decisões duráveis para Brain/skills;
- evitar carregar skills desnecessárias.

## Manutenção manual possível

`hermes sessions optimize` existe e é descrito como sem mudança de dados, mas ainda deve ser tratado como manutenção local com cuidado porque executa `VACUUM` no banco de sessões.

Antes de executar:

- garantir backup/snapshot se o banco for crítico;
- executar em janela sem carga alta;
- registrar receipt;
- verificar `sessions stats` antes/depois.

Não ativar como cron sem aprovação separada.

## Política operacional

- Problema de lentidão primeiro: medir contexto/sessões/toolsets/model logs.
- Não presumir que é RAM/VPS.
- Não resolver com restart antes de evidência.
- Não trocar modelo default por sensação de lentidão sem smoke/fallback/rollback.
- Telegram deve continuar limpo; diagnósticos detalhados ficam no Brain/local.

## Resultado esperado

Esta rotina transforma as melhorias v0.16 em disciplina prática:

- sessões menores;
- contexto mais limpo;
- compressão menos arriscada;
- menos ruído no Telegram;
- melhor decisão antes de mexer em runtime.
