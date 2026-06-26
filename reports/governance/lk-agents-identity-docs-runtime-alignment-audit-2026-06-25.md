# Audit — LK agents identity/docs/runtime alignment (2026-06-25)

Generated at: `2026-06-25T18:02:05.877890+00:00`

## Pedido

Lucas apontou erro no agente `[LK] Otimização de Coleções`: documentação canônica parecia correta, mas o runtime/SOUL carregado se apresentava como `LK Growth OS`. Lucas pediu verificar se quase todos os agentes LK estão com SOUL/MAPA/MEMORY/documentação desalinhados.

## Veredito

**Lucas está certo sobre o problema do `lk-collection-optimizer`.**

O profile runtime real em `/opt/data/profiles/lk-collection-optimizer` tem uma contaminação crítica no `SOUL.md`:

```text
# LK Growth OS — Hermes Specialist
Você é o agente especialista de Growth da LK Sneakers...
```

Isso é errado para `[LK] Otimização de Coleções`. O correto é uma SOUL primária de Collection Optimizer/LKGOC, não Growth.

## Achados principais

### 1. LKGOC / Collection Optimizer

| Camada | Status | Evidência |
|---|---:|---|
| Runtime profile real | ✅ existe | `/opt/data/profiles/lk-collection-optimizer` |
| SOUL principal | ❌ contaminado | heading `LK Growth OS — Hermes Specialist` |
| AGENTS guardrails | ✅ existe | regras Task OS, Stock, Shopify, Memory OS |
| Skill local LKGOC | ✅ existe | `skills/lk-superpowers-collection-optimizer/SKILL.md` |
| MAPA local profile root | ❌ ausente | `/opt/data/profiles/lk-collection-optimizer/MAPA.md` não existe |
| MEMORY profile root | ❌ ausente no runtime real | `/opt/data/profiles/lk-collection-optimizer/MEMORY.md` não existe |
| Smoke CLI de identidade | ⚠️ resposta correta, processo abortou | saída declarou LKGOC corretamente, mas `hermes chat` encerrou com exit 134/core dump |

Interpretação: a skill local e AGENTS compensam parte do erro, mas a identidade base do SOUL está errada. Isso explica a resposta que Lucas recebeu: o agente pode oscilar entre LKGOC e Growth dependendo da ordem/contexto carregado.

### 2. Caminho alternativo `/opt/data/home/.hermes/profiles`

Existe material parcial em:

```text
/opt/data/home/.hermes/profiles/lk-collection-optimizer/MEMORY.md
/opt/data/home/.hermes/profiles/lk-growth/MEMORY.md
```

Mas esses diretórios **não têm `config.yaml`**, `SOUL.md`, `AGENTS.md` ou skills. Portanto, parecem ser **stubs/legado**, não os profiles runtime vivos. Usar esse caminho como evidência de runtime leva a diagnóstico incompleto.

### 3. Outros profiles LK

Resumo estático dos profiles LK reais em `/opt/data/profiles`:

| Profile | SOUL heading | MAPA root | MEMORY root | Skill específica | Observação |
|---|---|---:|---:|---:|---|
| `lk-growth` | LK Growth OS | não | não | sim | identidade coerente, falta pacote root completo |
| `lk-shopify` | LK Shopify Hermes | não | não | sim | identidade coerente, falta pacote root completo |
| `lk-collection-optimizer` | **LK Growth OS** | não | não | sim | **contaminação crítica** |
| `lk-stock` | [LK] Estoque Loja Física | não | sim | sim | identidade coerente, falta MAPA root |
| `lk-trends` | LK Trend OS | não | não | sim | identidade coerente, falta pacote root completo |
| `lk-finance` | LK Finance | não | não | sim | identidade coerente, falta pacote root completo |
| `lk-content` | LK Content | sim | sim | sim | pacote mais completo |
| `lk-ops` | LK Ops Hermes Bot | não | não | não detectada por nome | precisa revisão de skill específica |
| `lk-analyst-readonly` | LK Analyst Readonly | não | não | não detectada por nome | support profile; pacote mínimo |
| `lk-content-reviewer` | LK Content Reviewer | não | não | não detectada por nome | support profile; pacote mínimo |

## Root cause provável

A criação/propagação histórica dos profiles LK reutilizou/copilou partes do pacote `lk-growth` como base. Em alguns agentes isso ficou só como referências cruzadas aceitáveis; no `lk-collection-optimizer`, a identidade primária do `SOUL.md` ficou de Growth.

Além disso, várias camadas foram evoluídas separadamente:

- Brain canonical docs;
- profile-local `SOUL.md`;
- profile-local `AGENTS.md`;
- profile-local skills;
- profile root `MAPA.md`/`MEMORY.md`;
- Honcho/contexto de sessão;
- stubs legados em `/opt/data/home/.hermes/profiles`.

Isso cria drift.

## Risco operacional

- LKGOC pode responder como Growth/SEO amplo em vez de Collection Optimizer.
- Um agente pode puxar contexto de estoque/Shopify/Growth como dono, em vez de handoff.
- Suporte profiles sem MAPA/MEMORY podem depender demais de skill genérica e Honcho, aumentando ruído.
- Smoke CLI mostrou resposta correta, mas exit 134/core dump no final; precisa investigação separada se recorrente.

## Não executado

- Não alterei SOUL/AGENTS/MAPA/MEMORY de nenhum profile.
- Não reiniciei gateways.
- Não migrei cron.
- Não toquei em secrets, Docker, VPS, Traefik, Shopify, Tiny, Klaviyo, GMC ou produção.

## Próximo bloco recomendado

Executar um pacote de realinhamento documental/runtime para os LK agents, em ordem segura:

1. Backup de `SOUL.md`, `AGENTS.md`, `MEMORY.md`, `MAPA.md`, skill-local dos 10 profiles LK.
2. Corrigir primeiro `lk-collection-optimizer/SOUL.md` para Collection Optimizer puro.
3. Criar/normalizar `MAPA.md` e `MEMORY.md` root mínimos para cada profile LK, sem duplicar docs longos.
4. Garantir que cada profile tenha uma skill/local pointer específica ou justificar como support profile.
5. Criar smoke harness de identidade: cada profile deve responder quem é, escopo, donos de handoff e ações bloqueadas.
6. Rodar smoke read-only em todos os profiles LK.
7. Só depois considerar restart dos gateways LK.

## Conclusão

O problema não é “quase todos estão Growth”, mas Lucas acertou o padrão: há **drift real entre Brain, SOUL, MAPA, MEMORY e skills**. O caso mais grave confirmado é `lk-collection-optimizer`. A correção deve ser feita como pacote controlado, não patch avulso.
