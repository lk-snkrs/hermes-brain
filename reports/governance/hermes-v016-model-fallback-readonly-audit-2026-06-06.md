# Hermes v0.16 — Auditoria read-only de modelos e fallbacks

Data: 2026-06-06
Escopo: read-only/local/documental. Nenhum modelo default foi alterado.

## Evidência coletada

- Runtime: `Hermes Agent v0.16.0 (2026.6.5)`.
- Config: version `27 ✓`.
- Default profile:
  - provider: `openai-codex`;
  - model default: `gpt-5.5`;
  - delegation: `openai-codex` / `gpt-5.5`;
  - fallback providers presentes: `true`.
- Perfis especialistas principais (`lk-shopify`, `lk-trends`, `spiti`, `mordomo`, `lk-ops`, `lk-growth`, `lk-collection-optimizer`): majoritariamente `openai-codex` + `gpt-5.5` com fallback configurado.
- Exceção relevante:
  - `lc-claude-cli` usa `lc-claude-cli-proxy` / `claude-opus-4` e não mostrou fallback providers no resumo read-only.
- `hermes model --help` confirma o novo fluxo interativo/model picker com refresh de catálogo, mas não foi executado interativamente para não alterar configuração.

## Interpretação v0.16

A v0.16 melhora model picker, catálogo, agrupamento de providers e recuperação de modelo. No nosso ecossistema, o ganho não deve ser “trocar modelos agora”, e sim criar uma política segura de seleção.

## Política recomendada

### 1. Strong/default lane

Manter `gpt-5.5` como default para:

- decisões críticas;
- produção externa;
- Docker/Traefik/gateway;
- Shopify/GMC/Ads/email/clientes/fornecedores/dinheiro;
- debug complexo;
- escrita de código;
- auditorias com risco;
- tarefas multiempresa.

### 2. Fast/triage lane — preparar, não ativar ainda

Validar depois um modelo mais rápido/barato para:

- respostas simples;
- classificação de intenção;
- rascunhos curtos;
- busca leve;
- triagem de inbox.

Critério antes de ativar:

- smoke test por perfil;
- fallback para strong lane;
- log/receipt;
- rollback simples;
- não aplicar em ações A3/A4.

### 3. Fallback lane

Fallback deve ser entendido como resiliência, não permissão para degradar qualidade silenciosamente.

Regras:

- timeout/nonresponse deve gerar evento sanitizado e fallback quando apropriado;
- fallback não deve executar writes externos sem revalidar escopo;
- mesma-provider fallback não substitui provider-outage fallback;
- se perfil usa proxy específico (`lc-claude-cli`), tratar como caso especial antes de produção.

## Recomendações por prioridade

### P0

- Não trocar default de perfis vivos sem approval packet.
- Preservar `gpt-5.5` para deep/critical.

### P1

- Criar smoke test read-only para catálogo/modelos por profile.
- Definir candidatos a fast lane por profile.
- Verificar se `lc-claude-cli` precisa fallback documentado ou se é propositalmente isolado.

### A3/A4

Exige aprovação antes de:

- alterar `model.default`;
- alterar `delegation.model`;
- ativar router automático;
- mudar fallback provider em runtime vivo;
- reiniciar gateways para ativar modelo.

## Decisão desta rodada

Nenhuma troca aplicada. Resultado é uma política e backlog seguro para adoção do model picker v0.16.
