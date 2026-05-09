# Brain Improvement Score

## Objetivo

Criar uma avaliação executiva e repetível da saúde do Hermes Brain depois de cada rodada de melhoria, pacote externo ou reorganização relevante.

O score não substitui o `scripts/brain_health_check.py`. Ele traduz checks técnicos e operacionais em um diagnóstico legível para Lucas: o que está bom, o que está frágil, o que deve virar próxima rodada e o que exige aprovação.

## Área dona

Operações / Hermes Geral.

## Agenda

Sob demanda após rodadas grandes de documentação/PRD/PR. Pode virar rotina mensal se houver volume.

## Skill/script executado

- `python3 scripts/brain_health_check.py` para validação técnica.
- Secret scan whole-repo.
- Leitura dos índices principais do Brain.
- Futuro script opcional: `scripts/brain_improvement_score.py`.

## Dimensões do score

Cada dimensão vai de 0 a 100. Enquanto não houver script, usar avaliação manual documentada.

### 1. Identidade e agentes

Verifica se agentes têm docs úteis e não apenas stubs:

- `SOUL.md`;
- `AGENTS.md`;
- `TOOLS.md`;
- `USER.md`;
- `MEMORY.md`;
- `HEARTBEAT.md`.

### 2. MAPAs e navegação

Verifica se a pessoa/agente consegue navegar sem adivinhar:

- `START-HERE.md`;
- `README.md`;
- `areas/MAPA.md`;
- `empresa/MAPA.md`;
- MAPAs de áreas/subáreas.

### 3. Rotinas e crons

Verifica separação entre rotina documentada e execução real:

- docs em `areas/*/rotinas/`;
- `empresa/rotinas/_index.md`;
- inventário de crons/VPS/Hermes quando necessário;
- status real não inventado.

### 4. Skills e procedimentos

Verifica se workflows recorrentes viraram skill/rotina e se não há duplicação perigosa:

- `skills/` canônicas;
- skills navegacionais em áreas;
- templates em `empresa/skills/_templates/` ou `areas/*/templates/`;
- instruções de verificação.

### 5. Segurança, secrets e aprovações

Verifica:

- `seguranca/permissoes.md`;
- `seguranca/acoes-sensiveis.md`;
- secret scan `possible_secrets 0`;
- nomes de secrets permitidos, valores proibidos;
- produção/VPS/Docker protegidos.

### 6. Integrações

Verifica docs por ferramenta e rotinas operacionais:

- Supabase;
- Shopify;
- Klaviyo;
- Evolution;
- Meta/Analytics;
- GitHub;
- Hostinger/VPS;
- Telegram;
- n8n.

### 7. Roadmap, changelog e pendências

Verifica se a história do Brain está rastreável:

- `ROADMAP-30-DIAS-HERMES.md`;
- `CHANGELOG.md`;
- `empresa/gestao/pendencias.md`;
- `memories/pending.md` quando relevante.

### 8. Links, arquivos e consistência

Verifica links relativos, arquivos obrigatórios e referências quebradas usando health check.

## Template de output

```md
# Brain Improvement Score — YYYY-MM-DD

Score geral: __/100

## Resultado por dimensão

- Identidade/agentes: __/100 — motivo
- MAPAs/navegação: __/100 — motivo
- Rotinas/crons: __/100 — motivo
- Skills/procedimentos: __/100 — motivo
- Segurança/secrets: __/100 — motivo
- Integrações: __/100 — motivo
- Roadmap/changelog/pendências: __/100 — motivo
- Links/consistência: __/100 — motivo

## Correções seguras recomendadas

## Itens que exigem aprovação Lucas

## Evidências

- Health check:
- Secret scan:
- Diff/commit/PR:
```

## Doppler keys

Nenhuma por padrão. Se uma checagem exigir integração privada, consultar apenas nomes de secrets e nunca imprimir valores.

## Como verificar sucesso

- Health check executado.
- Secret scan executado.
- Score e recomendações salvos em Markdown quando a avaliação for formal.
- Nenhuma ação externa/produtiva executada.

## Se falhar

Se a avaliação achar problemas críticos, separar:

- correções documentais seguras;
- correções técnicas que podem ir para PR;
- correções produtivas que exigem aprovação.

## Aprovação necessária

Não precisa para avaliação e documentação.

Precisa para mudanças em produção, secrets, deploy, merge, banco, mensagens externas ou infraestrutura.
