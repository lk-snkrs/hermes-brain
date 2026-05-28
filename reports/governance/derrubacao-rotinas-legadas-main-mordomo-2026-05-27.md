# Derrubação prática — rotinas legadas Main/Mordomo

Data/hora: 2026-05-27 11:56 UTC
Escopo: local/documental/read-only. Nenhum runtime, cron, gateway, Docker/VPS, produção, Shopify, Tiny, WhatsApp, e-mail, banco ou secret foi alterado.

## Objetivo

Transformar o scorecard Hermes vs Amora em uma fila curta de limpeza operacional para reduzir herança histórica em Main/Mordomo sem reduzir autonomia dos especialistas.

Regra de desenho: derrubar legado não é deletar tudo. É separar o que fica histórico, o que ganha dono lógico explícito, o que deve migrar para especialista e o que precisa de aprovação técnica antes de mexer em runtime.

## Fila recomendada

### 1. Rotinas LK Ops ainda hospedadas fora do dono ideal

- Estado: há menção explícita de que Main/Mordomo ainda hospedam algumas rotinas LK Ops por histórico.
- Dono alvo: `lk-ops`.
- Ação segura agora: inventariar cada rotina LK operacional que ainda nasce no Main/Mordomo e marcar dono lógico `lk-ops`, mesmo antes de migrar runtime.
- Não fazer sem aprovação: mover cron, mudar delivery, trocar gateway, mexer em Tiny/Shopify ou prometer preço/disponibilidade.
- Critério de pronto: toda rotina LK Ops tem dono lógico, fonte de verdade, local de receipt e motivo se ainda roda no Main/Mordomo.

### 2. Rotinas Zipper no Mordomo por falta de runtime dedicado

- Estado: Zipper permanece documental/read-only; rotinas relacionadas podem passar por Main/Mordomo.
- Dono alvo: Zipper OS documental, com Mordomo apenas como intake/rascunho quando fizer sentido.
- Ação segura agora: separar em três etiquetas: `Zipper documental`, `Mordomo intake` e `bloqueado por comunicação/preço/logística`.
- Não fazer sem aprovação: criar bot/runtime Zipper por simetria, enviar mensagem a cliente/artista, criar proposta, preço, logística ou promessa externa.
- Critério de pronto: cada fluxo Zipper deixa claro se é só leitura/rascunho ou se precisa aprovação humana.

### 3. Perfis auxiliares sem classificação final

- Estado: `brain-process`, `hermes-ops-readonly`, `lk-analyst-readonly` e `lk-content-reviewer` aparecem como auxiliares/read-only/experimentos.
- Dono alvo: Operações Hermes / Brain Process.
- Ação segura agora: classificar cada um como `ativo`, `experimento`, `arquivo` ou `candidato a pausa` com evidência.
- Não fazer sem aprovação: pausar/remover cron ou desativar profile.
- Critério de pronto: nenhum auxiliar fica ambíguo como possível executor de produção.

### 4. SPITI sem política local de crons explicitada

- Estado: SPITI tem runtime próprio, mas política de crons/rituais locais ainda precisa ficar declarada.
- Dono alvo: SPITI.
- Ação segura agora: escrever baseline: `sem crons locais por padrão` ou `crons locais somente após pacote aprovado`, conforme evidência atual.
- Não fazer sem aprovação: criar cron SPITI, mudar cron existente ou integrar Supabase/Itaú/Hub com write.
- Critério de pronto: SPITI não fica parecendo incompleto só porque não tem cron local; isso vira uma escolha documentada.

### 5. Uniformidade de receipts/handoffs em todos os especialistas

- Estado: formato canônico já existe, mas precisa virar hábito transversal.
- Dono alvo: Hermes Geral + todos os especialistas.
- Ação segura agora: apontar os diretórios de receipt/handoff por especialista e criar placeholders ou README mínimo quando faltar local claro.
- Não fazer sem aprovação: exigir microaprovação para cada passo local já aprovado.
- Critério de pronto: qualquer output relevante tem lugar previsível para receipt, e handoff não vira gargalo.

## Ordem sugerida de execução

1. Inventário documental das rotinas LK Ops/Zipper hospedadas no Main/Mordomo.
2. Etiquetagem `dono lógico` vs `runtime atual` vs `cron atual`.
3. Classificação dos perfis auxiliares.
4. Baseline SPITI de cron/ritual local.
5. Normalização de diretórios/READMEs de receipts por especialista.
6. Só depois: pacote de aprovação para qualquer migração real de cron/runtime.

## O que não deve ser derrubado agora

- Main/Hermes Geral como COO/orquestrador central.
- Mordomo como intake pessoal/multiempresa permitido.
- Zipper documental/read-only enquanto não houver gatilho objetivo.
- Rotinas históricas que ainda servem como referência, desde que marcadas como histórico/legado.
- Autonomia dos especialistas dentro do escopo aprovado.

## Próxima ação segura

Executar uma auditoria documental curta para produzir uma matriz:

- rotina;
- empresa/área;
- dono lógico correto;
- runtime atual;
- cron atual, se houver;
- status: manter, marcar legado, migrar depois, ou precisa aprovação;
- risco se mexer agora.

Essa auditoria ainda é local/read-only. Migração real de cron/runtime deve virar approval packet separado.
