# Hermes Brain rich-memory hygiene receipt — 2026-06-01

## Objetivo

Depois de compactar `MEMORY.md`/`USER.md` dos profiles, revisar os `MEMORY.md` ricos do Brain para evitar que a mesma deriva reapareça dentro das áreas/agentes: estado volátil, localizadores de credenciais, histórico longo ou procedimento que deveria ser regra/skill.

## Escopo

Arquivos auditados: todos os `**/MEMORY.md` dentro de `/opt/data/hermes_bruno_ingest/hermes-brain`.

Total: 14 arquivos.

## Achados

A maior parte dos `MEMORY.md` do Brain já está em formato aceitável: fatos duráveis, ponteiros e guardrails por domínio.

Achados relevantes:

1. `areas/lk/sub-areas/growth/MEMORY.md`
   - Tinha nome de variável de token do bot e aprendizado longo de incidente/rollback.
   - A regra completa já existia em `rules/REGRA-PRODUCTION-GUIAS-COLECOES-LK.md` e receipt próprio.

2. `areas/lk/sub-areas/growth/lk-shopify/MEMORY.md`
   - Tinha item explícito “Token Telegram” em seção de “não salvar aqui”.
   - Não era segredo, mas era melhor usar linguagem genérica.

3. `agentes/hermes-geral/MEMORY.md`
   - Menciona Doppler como fonte de credenciais.
   - Mantido: é política abstrata, não locator/secret.

4. `agentes/mordomo/MEMORY.md`
   - Aponta para inventário documental datado de runtime/canais.
   - Mantido: é ponteiro para documento, não status vivo.

## Mudanças aplicadas

### LK Growth

Arquivo: `areas/lk/sub-areas/growth/MEMORY.md`

- Substituí referência específica a variável de token por regra abstrata: credenciais/tokens ficam fora do Brain e devem ser consultados apenas em fonte segura autorizada.
- Condensei o aprendizado de production/rollback para uma regra curta e ponteiros:
  - `rules/REGRA-PRODUCTION-GUIAS-COLECOES-LK.md`
  - `receipts/2026-06-01-production-guide-layout-rollback-learning.md`

Resultado: o arquivo caiu de ~2.244 chars para ~1.436 chars e ficou mais aderente ao padrão “memória rica curada com ponteiros”.

### LK Shopify

Arquivo: `areas/lk/sub-areas/growth/lk-shopify/MEMORY.md`

- Troquei “Token Telegram” por “Credenciais do bot” na seção de itens que não devem ser salvos.

## Itens mantidos conscientemente

- `Doppler é fonte de credenciais` em `agentes/hermes-geral/MEMORY.md`: guardrail abstrato.
- Ponteiro datado para inventário de runtime em `agentes/mordomo/MEMORY.md`: documento de referência, não status runtime vivo.
- Ponteiro datado para receipt em LK Growth: evidência histórica em arquivo correto.

## Verificação pendente/executada

Após este receipt, rodar:

- Brain health check.
- Secret scan focado nos arquivos alterados.
- Reauditoria dos `**/MEMORY.md` para confirmar que flags restantes são ponteiros/guardrails aceitáveis.

## Não-ações

- Não alterei runtime, gateway, Docker, VPS, Traefik, cron ou provider externo.
- Não movi credenciais.
- Não apaguei histórico ou receipts.
- Não alterei fontes externas.
