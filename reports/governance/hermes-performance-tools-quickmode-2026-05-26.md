# Hermes Performance — Toolsets reduzidos, resposta rápida e Brain FTS

Data: 2026-05-26
Escopo: ajustes locais nos perfis especialistas para reduzir latência percebida no Telegram.

## Pedido de Lucas

Aprovado:
- Reduzir ferramentas por agente.
- Criar modo/resposta rápida por especialista.
- Separar resposta curta de trabalho pesado.
- Usar melhor RAM/cache local da VPS.

Não aprovado nesta fase:
- Redução agressiva de contexto/sessões históricas.

## Diagnóstico antes dos ajustes

A VPS não estava limitada por RAM:
- RAM total observada: 31 GiB.
- RAM disponível observada: 23 GiB.
- CPU: 8 cores.
- Gargalo provável: modelo remoto/API, excesso de ferramentas no prompt, contextos longos e concorrência entre múltiplos gateways.

## Mudanças aplicadas localmente

### 1. Toolsets Telegram reduzidos por especialista

Backups criados com sufixo `.bak-20260526-quick-tools`.

Perfis ajustados:
- `/opt/data/profiles/lk-ops/config.yaml`
- `/opt/data/profiles/mordomo/config.yaml`
- `/opt/data/profiles/lk-trends/config.yaml`
- `/opt/data/profiles/lk-growth/config.yaml`
- `/opt/data/profiles/lk-shopify/config.yaml`
- `/opt/data/profiles/spiti/config.yaml`

A redução foi aplicada em `platform_toolsets.telegram`; `platform_toolsets.cli` foi mantido amplo para manutenção manual.

### 2. Limite de turnos reduzido em especialistas

Objetivo: evitar loops longos em respostas simples e forçar handoff/relatório para trabalhos extensos.

- LK Ops: 40
- Mordomo: 45
- LK Trends: 45
- LK Growth: 60
- LK Shopify: 50
- SPITI: 55

Hermes Geral não foi reduzido nesta fase.

### 3. Política de resposta rápida adicionada aos perfis

Adicionada política em SOUL/AGENTS quando disponível:
- responder simples direto;
- usar ferramentas pesadas só quando mudarem a resposta;
- transformar tarefas longas em relatório/trabalho assíncrono;
- respeitar donos do organograma;
- manter Telegram limpo.

### 4. Brain FTS local criado

Script:
- `/opt/data/scripts/hermes_brain_fts.py`

Índice:
- `/opt/data/cache/hermes-brain-fts/brain_fts.sqlite`

Resultado inicial:
- 1502 documentos Markdown indexados.

Uso:
```bash
/opt/data/scripts/hermes_brain_fts.py --query 'organograma Hermes Amora' --limit 5
```

Esse índice não expõe rede e aproveita cache de página/RAM do Linux para consultas locais mais rápidas ao Brain.

## Verificações

- `hermes config check` passou para todos os perfis ajustados.
- Script FTS passou em lint Python e consulta teste retornou resultados.
- Nenhum restart de gateway/container foi feito nesta etapa.
- Nenhuma alteração em Docker, Traefik, Hostinger, Shopify, Tiny, CRM ou WhatsApp.

## Ativação

As mudanças de config podem exigir restart controlado dos gateways especialistas para entrar 100% em vigor. Recomenda-se reiniciar apenas os especialistas, não o Hermes Geral, para reduzir risco e evitar cortar a conversa principal.

## Rollback

Restaurar backups por profile, exemplo:

```bash
cp /opt/data/profiles/lk-ops/config.yaml.bak-20260526-quick-tools /opt/data/profiles/lk-ops/config.yaml
```

Depois, reiniciar apenas o gateway do profile afetado se ele já tiver sido ativado.
