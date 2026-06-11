# Brain OS — Executive Status

**Atualizado em:** 2026-06-11T13:55:54.899501+00:00
**Audiência:** Lucas / Hermes default / especialistas
**Modo:** status documental, não runtime.

## TL;DR

Brain OS v1 está publicado como camada canônica de hubs. A prioridade agora é maturidade, não mais criar hubs por volume.

## Status por eixo

- **Hubs canônicos:** verde — ondas Brain OS publicadas em `main` via PR #144.
- **Scanner:** verde — `brain-os-v1`, candidatos publicados, sem necessidade imediata de nova onda por volume.
- **Core docs:** em consolidação — docs centrais agora versionados neste diretório.
- **Semântica hub/receipt/backup:** consolidada — ver `MANIFEST_SEMANTICS.md`.
- **Fonte viva externa:** guardrail ativo — documentos não substituem Tiny/Shopify/GMC/Meta/Klaviyo/Chatwoot/Supabase quando a pergunta exige estado atual.
- **Runtime/infra:** intocado — nenhuma mudança Docker/VPS/gateway/cron/API externa neste pacote.

## Como usar

Quando uma pergunta chegar:

1. Identificar área/projeto.
2. Abrir hub canônico do projeto.
3. Ler primeiro `CURRENT_STATE.md` e `DECISIONS_AND_GUARDRAILS.md`.
4. Usar `ARTIFACT_INDEX.md`/`TIMELINE.md` para evidência histórica.
5. Consultar fonte viva se a resposta depender de estado atual.
6. Registrar novo trabalho como receipt/report, e promover a hub só se virar frente recorrente.

## Próximas melhorias recomendadas

1. Melhorar classificação do scanner para diferenciar `hub_manifest`, `receipt_manifest`, `backup_manifest` e `artifact_manifest`.
2. Criar check local que conte hubs vivos sem contar receipts/backups.
3. Adicionar um resumo executivo gerado automaticamente a partir do scanner.
4. Revisar qualidade de hubs existentes por completude, atualidade e fonte viva.

## Fora de escopo deste pacote

- Criar novos crons/watchdogs.
- Reiniciar profiles/gateways.
- Alterar Docker/VPS/Traefik.
- Fazer writes em Shopify/Tiny/GMC/Meta/Klaviyo/Chatwoot/Supabase.
- Habilitar dashboard público.
