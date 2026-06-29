# Política CLI/MCP-first para integrações Hermes

Status: vigente
Data: 2026-06-27
Owner: Hermes Geral / Brain Governance

## Decisão

Lucas corrigiu/definiu que os agentes Hermes devem usar **CLI oficial ou wrapper Hermes-Doppler-first primeiro**, **MCP segundo** quando a CLI/wrapper não cobrir melhor o caso, e **não API direta/raw** como primeira opção.

## Ordem obrigatória de escolha

1. **CLI oficial ou wrapper Hermes/Doppler-first**
   - Usar CLIs oficiais ou wrappers locais já governados, por exemplo `hermes-cli-run`, `gws`, `ntn`, `gh`, `vercel`, `shopify`, `himalaya`, `wacli`, conforme skill/rotina.
   - Seguir Doppler-first para credenciais e nunca imprimir valores.

2. **MCP nativo/read-only quando CLI/wrapper não for o melhor caminho**
   - Usar ferramentas `mcp_*` expostas no perfil quando cobrem o caso melhor que CLI/wrapper ou quando a integração só está disponível por MCP.
   - Preferir wrappers MCP read-only para métricas, SEO, conteúdo, analytics, brands, tempo e fetch quando forem a camada governada disponível.

3. **API direta/raw somente como exceção**
   - Só usar `curl`/HTTP/raw SDK/API quando não houver CLI/wrapper nem MCP adequado, ou quando a API for a única fonte viva necessária.
   - Declarar no receipt/resposta: por que CLI/MCP não serviu, escopo, método, se é read-only ou write, e evidência sanitizada.
   - Para qualquer write externo/API mutável: exigir aprovação escopada, payload claro, backup/rollback/readback e verificação.

## Regras para agentes, subagentes e crons

- Antes de chamar API direta, verificar se existe CLI oficial/wrapper Hermes e depois MCP adequado para aquela integração.
- Subagentes e cron prompts devem receber a mesma regra quando a tarefa envolve integrações.
- Se uma integração só existe via API hoje e ela será recorrente, criar backlog/packet para CLI/wrapper ou MCP antes de automatizar.
- Não copiar secrets para `.env`, Brain, receipts ou logs; reportar apenas presença/ausência/status (`values_printed=false`).

## Exemplos práticos

- SEO/SERP/keyword: DataForSEO MCP antes de API DataForSEO raw.
- Metricool: `metricool_readonly` MCP antes de API raw.
- GitHub/Vercel/Notion/Google Workspace/Shopify/Klaviyo/Supabase: `hermes-cli-run <cli>` ou CLI governada antes de HTTP raw.
- E-mail: Himalaya/Google Workspace CLI antes de Gmail API raw.
- WhatsApp: WACLI/wrapper governado antes de endpoint raw.

## Guardrail

`Fonte viva` não significa automaticamente `API direta`. Em Hermes, fonte viva deve ser acessada pela camada mais governada disponível: CLI/wrapper → MCP → API direta excepcional.


## Central Integration Auth Broker — complemento 2026-06-28

Para integrações com auth compartilhada entre profiles/agentes, a política CLI/MCP-first deve passar pelo broker central quando disponível:

```bash
/opt/data/home/.local/bin/hermes-cli-run <cli> <args...>
```

Regras adicionais:

- Agents, subagents e crons não devem executar login/OAuth interativo individual (`shopify login`, `shopify store auth`, `hermes mcp login`) sem approval de reauth/control plane.
- O broker central bloqueia login/auth interativo e mutations Shopify por padrão; mutations exigem `--allow-mutations` + referência de aprovação (`--approval` ou `HERMES_INTEGRATION_APPROVAL`) + rollback/readback.
- Secrets continuam Doppler-first e process-scoped; não copiar `.env`, `auth.json`, `mcp-tokens` ou cache OAuth entre profiles.
- Fallback legado (`shopify-admin-graphql` ou raw HTTP) é incidente aprovado/documentado, não alternativa normal silenciosa.

## Verificação

Em trabalhos materiais com integração, receipts devem mencionar `integration_access_path` ou equivalente: `mcp`, `cli`, `wrapper`, ou `raw_api_exception`.

values_printed=false
