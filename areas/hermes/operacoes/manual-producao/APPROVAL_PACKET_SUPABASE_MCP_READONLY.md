# Approval Packet — Supabase MCP read-only

Gerado em: 2026-05-30T22:29:07+00:00  
Status: **packet preparado / aguardando aprovação escopada**  
Tipo: MCP read-only externo com credencial/banco.  
Risco: M3 — banco/CRM/cliente sensível.

## Objetivo

Configurar e testar um Supabase MCP **read-only** para uma empresa/projeto específico, começando por schema discovery e uma query pequena, sem mutations e sem expor dados sensíveis no Telegram.

## Escopo sugerido de primeiro piloto

Opção recomendada: **Zipper Vendas read-only** ou **SPITI read-only**.

Motivo:

- Zipper/SPITI têm maior ganho com schema discovery e queries recorrentes.
- LK já tem scripts/skills/Tiny/Shopify mais sensíveis; Supabase LK pode vir depois.

## MCP candidato

- pacote: `@supabase/mcp-server-supabase`
- versão observada: `0.8.1`
- descrição: MCP server for interacting with Supabase

## Secrets disponíveis por nome em Doppler

Foram identificados nomes de secrets relacionados a Supabase, sem valores impressos. Exemplos relevantes:

- `SUPABASE_ZIPPER_URL`
- `SUPABASE_ZIPPER_SERVICE_KEY`
- `SUPABASE_ZIPPER_VENDAS_URL`
- `SUPABASE_ZIPPER_VENDAS_SERVICE_KEY`
- `SUPABASE_SPITI_URL`
- `SUPABASE_SPITI_SERVICE_KEY`
- `SUPABASE_SPITI_CRM_ANON_KEY`
- `SUPABASE_LK_URL`
- `SUPABASE_LK_SERVICE_KEY`

Observação: service keys podem ser amplas demais. Preferir role/token read-only quando disponível. Se só houver service key, usar wrapper/whitelist ou criar credencial restrita antes de expor ao Hermes.

## Profile alvo recomendado

Escolher um:

1. `hermes-ops-readonly` — se o piloto for governança/observabilidade geral.
2. `spiti` — se o piloto for SPITI e o runtime do profile for o dono.
3. profile dedicado futuro, ex.: `zipper-readonly` — se Zipper virar runtime próprio.

Evitar configurar Supabase amplo no `default` enquanto a política ainda está em piloto.

## Tools permitidas no piloto

Somente:

- listar projetos/conexão/schema quando suportado;
- listar tabelas/schema;
- query/select read-only com limite pequeno;
- descrever colunas.

Limites:

- `limit <= 20` em queries de teste;
- não retornar campos sensíveis quando não necessários;
- não cruzar empresas/projetos.

## Tools bloqueadas

- insert/update/delete/upsert;
- SQL arbitrário com DDL/DML;
- chamadas RPC mutáveis;
- gestão de auth/users/storage/secrets;
- export em massa;
- qualquer mutation.

## Config segura esperada

- `sampling.enabled: false`
- timeout: `120` a `180`
- connect_timeout: `60`
- secrets via wrapper Doppler, não em YAML direto
- backup de config antes de editar
- restart apenas do profile alvo, se necessário

## Teste de aceite

1. Backup do `config.yaml` alvo.
2. Configurar MCP com wrapper que busca secret via Doppler sem imprimir valor.
3. Reiniciar apenas profile alvo, se aprovado.
4. Verificar logs sem secrets.
5. Confirmar tool discovery.
6. Executar uma query read-only pequena:
   - exemplo Zipper: listar 5 registros não sensíveis ou schema de uma tabela;
   - exemplo SPITI: listar schema/tabelas ou 5 registros de tabela não sensível.
7. Registrar receipt sanitizado no Brain.
8. Se falhar, rollback: remover MCP do config e reiniciar apenas o profile alvo.

## Rollback

- Restaurar backup do `config.yaml`.
- Reiniciar apenas o profile alvo.
- Verificar que MCP tools desapareceram.
- Não tocar Docker/VPS/Traefik/Main Hermes.

## Frase de aprovação necessária

Para executar runtime/config, Lucas deve aprovar com escopo parecido com:

> Aprovo configurar Supabase MCP read-only no profile `<profile>`, para o projeto `<Zipper/SPITI/LK>`, usando secrets Doppler `<nomes>`, sampling off, sem mutations, com backup de config, restart apenas do profile alvo e rollback restaurando o config anterior.

Sem essa frase, o trabalho fica em documentação e discovery read-only.
