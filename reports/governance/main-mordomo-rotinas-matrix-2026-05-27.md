# Matriz read-only — rotinas Main/Mordomo vs dono lógico

Data/hora: 2026-05-27 11:56 UTC  
Escopo: local/documental/read-only. Nenhum runtime, cron, gateway, Docker/VPS, produção, Shopify, Tiny, WhatsApp, e-mail, banco ou secret foi alterado.

## Objetivo

Mapear o que hoje aparece hospedado em Main/Mordomo, separar dono lógico de runtime atual e indicar o estado correto de cada fluxo antes de qualquer migração real.

## Regra de leitura

- **Manter** = está coerente e não pede migração agora.
- **Marcar legado** = permanece histórico, mas deve ficar explicitamente rotulado para não virar verdade de runtime.
- **Migrar depois** = o dono lógico já é claro, mas a troca de runtime/cron depende de pacote de aprovação.
- **Aprovação necessária** = qualquer write externo, restart, cron, Docker/VPS, produção, contato externo ou mudança de superfície sensível.

## Matriz curta

### 1) Hermes Geral / Main central

- **Dono lógico:** Hermes COO / Governança central.
- **Runtime atual:** `/opt/data`.
- **Situação:** **manter**.
- **Por quê:** é a camada central de coordenação, Brain, Mesa COO, approval packets, watchdogs e governança.
- **Observação:** o problema não é o Main existir; é o Main ainda carregar rotinas históricas que já têm dono lógico mais específico.

### 2) Mordomo / Lucas pessoal

- **Dono lógico:** Lucas pessoal / intake.
- **Runtime atual:** `/opt/data/profiles/mordomo`.
- **Situação:** **manter com ajustes**.
- **Por quê:** o Mordomo é apropriado para agenda, follow-up permitido, inbox e rascunhos pessoais.
- **O que precisa ficar explícito:** qualquer fluxo Zipper/LK que ainda esteja aqui por histórico deve ser tratado como legado até migração documentada.

### 3) LK Ops operacionais ainda espalhadas

- **Dono lógico:** LK Ops / Atendimento.
- **Runtime atual:** Main e, em alguns casos, Mordomo por histórico.
- **Situação:** **migrar depois**.
- **Exemplos de rotas históricas:** daily sales, weekly CEO review, pulso comercial, close de loja e partes de WhatsApp operacional.
- **Por quê:** o dono lógico já está claro, mas o runtime ainda não está plenamente alinhado.
- **Ação segura agora:** inventário linha a linha, sem mexer em cron/runtime ainda.

### 4) Zipper com rotas legadas no Main/Mordomo

- **Dono lógico:** Zipper OS.
- **Runtime atual:** Main/Mordomo, sem runtime dedicado consolidado.
- **Situação:** **marcar legado**.
- **Por quê:** Zipper hoje é documental/read-only; o espaço de execução ainda não justifica um runtime próprio por simetria.
- **O que pode existir:** CRM/Main, vendas_tango, rascunhos internos e análise de obras/artistas/colecionadores.
- **O que não pode virar padrão:** proposta, preço, logística, contato externo ou promessa material sem aprovação explícita.

### 5) LK WhatsApp / respostas operacionais

- **Dono lógico:** depende do canal e risco; em geral LK Ops/Mordomo.
- **Runtime atual:** Mordomo e legado histórico de Main.
- **Situação:** **migrar depois**.
- **Por quê:** mensagens simples podem ficar no Mordomo, mas respostas operacionais sensíveis precisam ficar claramente atribuídas ao dono correto.
- **Ação segura agora:** classificar caso a caso antes de mover qualquer automação.

### 6) SPITI sem cron local consolidado

- **Dono lógico:** SPITI OS.
- **Runtime atual:** `/opt/data/profiles/spiti`.
- **Situação:** **manter / declarar escolha**.
- **Por quê:** a ausência de cron local consolidado não é falha por si só; pode ser uma decisão documentada.
- **Ação segura agora:** explicitar se a política é “sem crons locais por padrão” ou “crons só com pacote aprovado”.

### 7) Perfis auxiliares read-only

- **Dono lógico:** Hermes Governança.
- **Perfis observados:** `brain-process`, `hermes-ops-readonly`, `lk-analyst-readonly`, `lk-content-reviewer`.
- **Situação:** **marcar legado / classificar**.
- **Por quê:** ainda precisam ser rotulados como ativo, experimento, arquivo ou candidato a pausa.
- **Ação segura agora:** nenhuma pausa/remoção sem classificação e sem pacote apropriado.

## Síntese executiva

O quadro atual é estruturalmente bom, mas ainda tem três bolsões de herança:

1. **LK Ops** ainda com rotas em Main/Mordomo.
2. **Zipper** ainda documental/read-only com superfícies históricas em Main/Mordomo.
3. **Mordomo** ainda hospedando fluxos híbridos que precisam de dono lógico explícito.

Isso não pede ruptura. Pede **higienização por identidade**:

- dono lógico claro;
- runtime atual explícito;
- histórico marcado;
- migração só com approval packet quando houver mudança real.

## Próxima ação segura

Produzir, na sequência, um inventário detalhado com as colunas:

- rotina;
- dono lógico;
- runtime atual;
- cron atual;
- status (`manter`, `marcar legado`, `migrar depois`, `aprovação necessária`);
- risco se mexer agora.

Esse inventário ainda é read-only. A migração vem depois, em pacote separado.
