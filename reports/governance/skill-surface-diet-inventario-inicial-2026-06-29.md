# Skill Surface Diet — inventário inicial read-only

Data: 2026-06-29T09:43:26Z  
Escopo aprovado: Onda 0/Onda 1 local/read-only/documental.  
Status: inventário inicial; **nenhuma skill foi editada, movida ou deletada**.

## Objetivo

Identificar onde a superfície de skills/toolsets pode estar pesada demais para uso diário, antes de qualquer limpeza.

## Evidência coletada

Fonte: leitura local de `/opt/data/profiles/*/config.yaml` e contagem de `skills/**/SKILL.md` por perfil. Nenhuma credencial lida ou impressa.

| Perfil | Skills | Telegram toolsets | Leitura inicial |
|---|---:|---:|---|
| `lk-collection-optimizer` | 243 | 8 | Muito alto; precisa curadoria por escopo LKGOC. |
| `lk-trends` | 239 | 14 | Muito alto + toolset amplo; candidato forte a dieta. |
| `lk-shopify` | 234 | 10 | Muito alto; manter safety/Shopify, auditar duplicatas. |
| `lk-stock` | 232 | 10 | Muito alto; validar se stock/Tiny/Supabase dominam. |
| `spiti` | 211 | 15 | Alto; revisar se Telegram precisa tantos toolsets. |
| `mordomo` | 201 | 16 | Alto e amplo; perfil chat-centric precisa cuidado para não perder WACLI/CLI. |
| `lk-ops` | 177 | 12 | Alto; toolsets terminal/code_execution justificados por atendimento/ops, mas revisar. |
| `brain-process` | 169 | 2 | Alto, porém Telegram estreito; provável worker/governance surface. |
| `hermes-ops-readonly` | 169 | 2 | Alto, porém Telegram estreito; candidato a shared governance pack. |
| `lk-content-reviewer` | 168 | 2 | Alto para reviewer; provável excesso. |
| `lk-analyst-readonly` | 167 | 2 | Alto, mas read-only; revisar duplicação. |
| `lk-growth` | 159 | 8 | Alto; revisar skills Growth vs LKGOC/Shopify. |
| `lk-content` | 12 | 12 | Skills enxutas; toolset amplo por conteúdo/mídia. |
| `lk-finance` | 9 | 13 | Skills enxutas; toolsets fortes por OCR/local finance. |
| `spiti-atendimento` | 8 | 15 | Skills enxutas; toolset amplo. |
| `lc-claude-cli` | 4 | 8 | Skills enxutas. |

## Achados

1. **Sprawl concentrado em perfis LK/Spiti/Mordomo.** 6 perfis têm 200+ skills.
2. **Alguns profiles worker/reviewer têm muitas skills apesar de Telegram estreito**, o que sugere reuso bruto de repositório de skills em vez de superfície mínima por função.
3. **Perfis com poucas skills podem ter toolsets amplos**, então dieta não é só contagem de skills; precisa cruzar com latência, uso real e risco.
4. **Não há autorização para deletar/editar skills nesta onda.** O próximo passo é classificar.

## Classificação sugerida para a próxima onda

| Classe | Ação futura | Approval |
|---|---|---|
| Core obrigatório | manter e documentar | não para documentação |
| Profile-specific | manter no perfil correto | não para inventário |
| Duplicada/sobreposta | propor consolidação | sim antes de editar/deletar |
| Gigante | mover detalhe para references | sim se skill ativa/crítica |
| Legacy | marcar legacy/DO NOT RUN | geralmente local, mas verificar impacto |
| Não usada | arquivar/remover só após evidência | sim antes de remover |

## Próximo passo recomendado

Criar um relatório de **top 20 skills por profile por uso real** se os logs/sessões permitirem, e só então propor patches pequenos. Não fazer limpeza massiva.

## Não realizado

- Nenhuma skill alterada.
- Nenhum toolset alterado.
- Nenhum profile reiniciado.
- Nenhum cron/gateway/Docker/VPS tocado.
