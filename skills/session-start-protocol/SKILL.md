---
name: session-start-protocol
description: Protocolo obrigatório de início de sessão - deve ser executado ANTES de qualquer outra ação
tags: [protocol, session, mandatory]
---

# Session Start Protocol

## REGRA DE OURO
**Hermes Brain é a fonte de verdade.** Se não tá no brain, eu não sei — mesmo que eu ache que sei.

**Lei COO #7: Sempre Corrigir Eternamente.**
- Bug encontrado = fix + prevent + test — no mesmo momento
- Nunca o mesmo erro duas vezes
- Ao fechar sessão: fix hoje → prevention criada? → documentado?

**Tudo que fazemos → documentado no brain.** Ao final de cada sessão:
1. Pending atualizado?
2. Lessons salvas (se houve insight)?
3. Brain sync bidirecional (push local → VPS)?
4. Git push hermes-brain?

---

## REGRA CONTRA COMPRESSÃO DE CONTEXTO (M2.7)

**Contexto压缩 apaga todo o estado da sessão.** O que está no chat morre.

**SOLUÇÃO:** Arquivo `CURRENT_WORK.md` é a âncora de sobrevivência.

```
ANTES de压缩 (eu mesmo preciso fazer):
1. dump do estado → /root/.hermes/CURRENT_WORK.md
2. confirmarbrain atualizado
3. SÓ DEPOIS permitir compressão

A CADA INÍCIO DE SESSÃO:
1. Ler CURRENT_WORK.md PRIMERO (trabalho em andamento)
2. brain + memories (seguir os 7 passos)
3. Verificar se CURRENT_WORK.md tem info que morreu no chat
```

**EU NUNCA devo iniciar resposta sem ter lido CURRENT_WORK.md quando existir.**

---

## Os 7 Passos (exatos, nesta ordem)

1. **Ler `CURRENT_WORK.md`** → se existir, é prioridade (trabalho em andamento)
2. **Ler skill `hermes-brain`** → contexto dos negócios
3. **Ler `MEMORY_INDEX.md`** → mapa navegável (`/root/.hermes/hermes-brain/MEMORY_INDEX.md`)
4. **Verificar pendentes** → `read_file("/root/.hermes/pending.md")`
5. **Verificar crons** → `cronjob list`
6. **Verificar decisions** → `read_file("/root/.hermes/memories/decisions.md")`
7. **Verificar lições** → `read_file("/root/.hermes/memories/lessons.md")`
8. **Perguntar** → "O que vamos fazer hoje?"

## Caminhos Válidos (USAR ESTES)

```
Hermes Brain:
/root/.hermes/hermes-brain/
├── MEMORY_INDEX.md     ← MAPA NAVEGÁVEL (ler primeiro)
├── memories/
│   ├── lk.md           ← LK Sneakers
│   ├── zipper.md        ← Zipper Gallery
│   ├── spiti.md        ← SPITI Auction
│   ├── decisions.md     ← decisões permanentes
│   ├── lessons.md      ← lições aprendidas
│   └── user.md         ← preferências Lucas
├── scripts/            ← scripts operacionais
└── skills/            ← skills ativas

Pendentes:
/root/.hermes/pending.md
```

## Regra de Ouro (NUNCA PULAR)

```
ANTES de qualquer ação nova:
  1. brain → verificar facts
  2. session_search → buscar contexto passado
  3. read_file → confirmar antes de afirmar

DEPOIS de qualquer ação nova:
  1. Isso muda alguma memória? → atualizar brain
  2. Aprendi algo novo? → lessons.md
  3. Tarefa aberta? → pending.md
```

## Ao Final de Cada Sessão (OBRIGATÓRIO — SEMPRE)

**ANTES DE FECHAR — Checklist de 5 minutos:**

1. **Memórias** → se mudou algo: `bash /root/.hermes/scripts/brain_sync.sh`
2. **Git push** → confirmar "main -> main"
3. **Lição aprendida?** → `lessons.md` + `mem0_conclude()`
4. **Pendências novas?** → `pending.md` atualizado
5. **Estado da sessão** → `CURRENT_WORK.md` atualizado

**Se a sessão terminou sem eu fazer o checklist → ERRO de procedimento.**
Patch o skill, não só lembrar.

**Frases que sinalizam que falhei:**
- "pronto", "funciona", "feito" sem o checklist ter sido executado
- Não ter atualizado pending.md ao longo da sessão
- Ter perguntado "posso corrigir?" em vez de ter corrigido primeiro

**Regra aprendida (19/04):** se eu parei pra perguntar em vez de corrigir sozinho → eu falhei. Corrigir primeiro, reportar depois. Sempre.

---

## ERRO CRÍTICO A EVITAR

Se eu pular direto para execução sem ler brain + memories:
- ESTOU FORA DO SCRIPT
- Devo parar e recarregar imediatamente
- "Esqueci de ler o contexto. Um momento."

## Session Log (adicionar ao final de cada sessão)

```markdown
### 2026-04-19 afternoon — COO Audit Completo + Correção Sistêmica

**O que fizemos**
- Auditoria 100% do sistema: 26 crons, 40+ scripts, schema LK Intel
- Identificados 3 problemas reais: Shopify pagination, timezone bugs (3 scripts), Meta token quebrado
- Corrigido: Shopify pagination (page_info + updated_at_min incompatíveis)
- Corrigido: timezone em lk_anomaly_check.py (8x) e lk_anomaly_deepdive.py (8x)
- Corrigido: lk_morning_briefing.py NameError (import datetime/timezone faltando)
- Criado: lk_transactions_full_sync.py + adicionado ao full_sync (6 fontes)
- Criado: skill `lk-data-debug` com padrões de debug de sync LK
- Identificado: schema real — products.is_active NÃO existe (variants.is_active sim)
- Identificado: transactions_full com 7 dias desatualizado — script recriado
- Desabilitados: 3 crons duplicados Monday 9h (Consolidation Weekly agora faz tudo)
- Pausados: Hermes Weekly Memory + Learning Loop (redundantes)

**Lição aprendida**
- NÃO confiar em suposições sobre schema — SEMPRE verificar via API REST
- `/tmp` não é confiável como canonical — 23 scripts com token old lá
- Paginacao Shopify: page_info e updated_at_min são INCOMPATÍVEIS
- Session-start-protocol: a simples existência do CURRENT_WORK.md não impede bugs
- O sistema estava mais quebrado do que eu pensava — precisava de audit completo, não só "fixar o que quebrou"

**Brain atualizado**
- `/root/.hermes/CURRENT_WORK.md` (reescrito)
- `/root/.hermes/hermes-brain/MEMORY_INDEX.md` (reescrito)
- `/root/.hermes/pending.md` (reescrito com status real)
- `/root/.hermes/memories/lessons.md` (atualizado)
- `/root/.hermes/skills/lk/lk-data-debug/SKILL.md` (criado)
```

### YYYY-MM-DD — [tema]

**O que fizemos**
- [tarefas executadas]

**Lição aprendida**
- [o que deu errado ou certo no processo]

**Brain atualizado**
- [quais arquivos foram atualizados]
```
