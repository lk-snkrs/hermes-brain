# F2-001 — Kanban board design: `hermes-lk-improvements`

Gerado em: 2026-05-30T22:20:43+00:00  
Status: **concluído; board real criado em modo seguro em 2026-06-03**  
Escopo original: desenhar o board Kanban da Fase 2 sem criar board real, sem criar cards reais, sem atribuir workers e sem acionar dispatcher produtivo. Atualização 2026-06-03: Lucas aprovou “seguir”; o board real foi criado com cards iniciais **sem assignee**, mantendo bloqueio contra worker/dispatcher produtivo.

## 1. Decisão executiva

O board planejado será:

- slug: `hermes-lk-improvements`
- nome humano: **Hermes/LK Improvements**
- finalidade: melhorias duráveis de plataforma Hermes/LK que precisam sobreviver restart, ter trilha auditável e poder passar por review antes de qualquer runtime/write externo.

Não usar este board para:

- atendimento imediato;
- pedido simples de uma resposta;
- write externo direto;
- deploy, Docker, Traefik, VPS, secret ou webhook sem approval packet;
- tarefas que deveriam ir para LK Growth/Ops/Shopify/SPITI/Mordomo como atendimento normal.

## 2. Evidência de contexto atual

Checagem read-only mostrou:

- boards existentes:
  - `default` — vazio;
  - `lk-growth-ops` — board ativo histórico com tarefas `done=9`, `ready=6`.
- board atual do CLI: `lk-growth-ops`.
- assignees conhecidos em disco incluem: `brain-process`, `hermes-ops-readonly`, `lk-analyst-readonly`, `lk-content-reviewer`, `lk-growth`, `lk-ops`, `lk-shopify`, `lk-trends`, `mordomo`, `spiti`.

Implicação: já existe uso Kanban histórico; a Fase 2 deve criar uma frente separada para melhorias de plataforma, sem misturar com `lk-growth-ops`.

## 3. Estados/colunas operacionais

Usar os estados nativos do Hermes Kanban com interpretação local:

- `triage`
  - ideia bruta ou melhoria ainda ambígua;
  - não executável;
  - precisa ser especificada antes de `ready`.

- `todo`
  - especificada, mas aguardando dependência, janela, aprovação ou priorização;
  - não deve ser executada automaticamente.

- `ready`
  - pronta para execução **apenas se** tiver assignee seguro;
  - em Fase 2, card `ready` ainda pode ficar sem assignee para evitar execução.

- `running`
  - worker real reivindicou a tarefa;
  - só permitido após approval packet quando houver dispatcher/worker envolvido.

- `blocked`
  - depende de decisão do Lucas, credencial, aprovação, dado externo, ou risco não resolvido.

- `scheduled`
  - aguardando tempo/janela explícita;
  - não usar como substituto de cron sem aprovação.

- `done`
  - saída entregue e verificada;
  - deve ter summary, evidência e link/arquivo de receipt.

- `archived`
  - histórico encerrado; nunca apagar só para “limpar”.

## 4. Convenção de IDs e títulos

Usar IDs humanos na camada documental:

- `F2-KB-001` — Kanban board setup/spec
- `F2-MCP-001` — MCP/DataForSEO inventory
- `F2-PLG-001` — plugin local/read-only spec
- `F2-API-001` — Dashboard/API exposure classification
- `F2-DLV-001` — deliverable mode/receipts policy

Quando virar card real, o Hermes Kanban gerará IDs técnicos `t_<hex>`. O corpo do card deve incluir o ID humano no topo para rastreabilidade.

Formato de título:

```text
[F2][<frente>][<risk>] verbo + objeto claro
```

Exemplos:

- `[F2][KANBAN][A1] Specify hermes-lk-improvements board`
- `[F2][MCP][A1] Inventory DataForSEO MCP config read-only`
- `[F2][PLUGIN][A2] Draft capability-status plugin mini-PRD`

## 5. Labels de risco

Usar labels no corpo do card, mesmo se a versão atual do Kanban não tiver labels nativos suficientes.

- `A0` — leitura/documentação local sem segredo e sem runtime.
- `A1` — inspeção read-only de runtime/config/logs, sem restart e sem secret value.
- `A2` — edição local de docs/scripts/skills, sem runtime ativo.
- `A3` — runtime local/profile/gateway/config/cron/plugin/MCP; exige approval packet.
- `A4` — Docker/VPS/Traefik/secrets/write externo/produção; exige aprovação explícita forte, backup e rollback.

Regra: Fase 2 só executa automaticamente `A0/A1` e, quando necessário, `A2` local. `A3/A4` viram approval packet.

## 6. Template de card

```markdown
Human ID: F2-XXX-000
Risk: A0/A1/A2/A3/A4
Owner lógico: <Hermes Geral | LK Growth | LK Shopify | Ops | etc.>
Assignee real: <unassigned até aprovação>
Status inicial: triage/todo/ready

## Objetivo
- ...

## Escopo permitido
- ...

## Fora de escopo / bloqueado
- ...

## Fontes/evidências necessárias
- ...

## Saída esperada
- arquivo/relatório/receipt/approval packet

## Critério de aceite
- ...

## Verificação obrigatória
- brain_health_check quando tocar Brain
- secret scan direcionado
- comando read-only específico, quando aplicável

## Rollback
- para docs: patch reversível/checkpoint/git diff
- para runtime: approval packet separado
```

## 7. Fan-out/fan-in padrão

Usar dependências parent→child para trabalho paralelo:

### Padrão Fase 2 inicial

- `F2-API-001` — classificar API/webhook/dashboard exposure — **done**
- `F2-KB-001` — especificar board Kanban — **este documento**
- `F2-MCP-001` — inventariar MCP/DataForSEO — pode rodar em paralelo com plugin spec
- `F2-PLG-001` — plugin local/read-only mini-PRD — pode rodar em paralelo com MCP inventory
- `F2-DLV-001` — deliverable mode policy — pode rodar em paralelo
- `F2-PILOT-001` — escolher piloto real pequeno — depende de MCP/plugin/Kanban specs

### Regra

Filhos que dependem de evidência dos pais devem ficar `todo` ou `blocked` até os pais estarem `done` com summary verificável.

## 8. Assignee policy

### Estado inicial

Todos os cards produtivos de `hermes-lk-improvements` começam **unassigned**.

### Assignees candidatos para piloto read-only

- `hermes-ops-readonly`
  - inspeção local/runtime/documental;
  - sem writes externos;
  - bom primeiro worker se precisar testar execução.

- `brain-process`
  - organização do Brain e documentação;
  - deve ficar restrito a docs/rotinas/relatórios.

- `lk-analyst-readonly`
  - análise comercial/dados read-only;
  - não usar para runtime Hermes.

- `lk-content-reviewer`
  - revisão de conteúdo/output;
  - bom para review, não para execução.

### Bloqueio

Não atribuir inicialmente a:

- `lk-shopify`, `lk-ops`, `lk-growth`, `lk-trends`, `mordomo`, `spiti` para tarefas de Fase 2 de plataforma, salvo se a tarefa for claramente do domínio deles;
- qualquer profile com terminal/write externo amplo sem approval packet.

## 9. Dispatcher safety

Ponto crítico: configs inspecionadas anteriormente indicam `kanban.dispatch_in_gateway=true` em default/LK profiles. Portanto:

- criar card sem assignee é seguro como planejamento;
- atribuir card `ready` a profile real pode disparar execução;
- `dispatch --dry-run` deve ser preferido antes de qualquer dispatch real;
- worker real só depois de approval packet com:
  - board;
  - task id;
  - assignee;
  - toolset esperado;
  - comando previsto;
  - rollback/reclaim;
  - logs a verificar.

## 10. Comentários e receipts

Todo card real deve receber comentários nestes marcos:

1. `scope-confirmed` — escopo e bloqueios claros.
2. `evidence-collected` — fontes lidas e comandos read-only usados.
3. `output-written` — arquivo/relatório gerado.
4. `verification-passed` ou `verification-failed` — com comando e resultado.
5. `handoff` — se outro profile/worker precisa continuar.

Receipts técnicos ficam no Brain/arquivo local. Telegram recebe apenas resumo executivo, decisão ou exceção.

## 11. Cards iniciais prontos para eventual criação real

Atualização 2026-06-03:

- Board real: `hermes-lk-improvements`.
- Receipt: `RECEIPT_FASE2_KANBAN_BOARD_LIVE_20260603.md`.
- Setup card concluído: `t_49098f9f`.
- Cards concluídos: `t_49098f9f`, `t_cd3dd451`, `t_2302a6a6`.
- Cards prontos sem assignee: `t_01156a76`, `t_fe598ba5`, `t_45b92440`.
- Nenhum worker real atribuído; nenhum dispatch produtivo executado.
- Revalidação F2-004 atualizou a classificação: API default segue host-local; webhook default segue público; há dashboard público separado que exige revisão de autenticação/exposição antes de cockpit operacional. Receipt: `RECEIPT_F2_004_EXPOSURE_REVALIDATION_20260603.md`.
- Revisão específica do dashboard público (`t_2302a6a6`) encontrou token de sessão injetado em HTML público, OpenAPI/docs públicos e endpoints sensíveis acessíveis com o token da própria página. Receipt: `RECEIPT_F2_DASHBOARD_PUBLIC_AUTH_REVIEW_20260603.md`. Cockpit/plugin operacional segue bloqueado até mitigação/isolamento.

### F2-KB-001 — Specify `hermes-lk-improvements` board

Risk: A0/A2  
Assignee inicial: unassigned  
Saída: este documento + README/backlog atualizados.  
Status documental: done.

### F2-MCP-001 — Inventory DataForSEO MCP config read-only

Risk: A1  
Assignee inicial: unassigned ou `hermes-ops-readonly` após aprovação de piloto.  
Saída: `F2_002_MCP_DATAFORSEO_INVENTORY.md`.  
Bloqueios: não chamar MCP externo com credencial produtiva sem aprovação; não imprimir secrets.

### F2-PLG-001 — Draft capability-status plugin mini-PRD

Risk: A0/A2  
Assignee inicial: unassigned.  
Saída: `F2_003_CAPABILITY_STATUS_PLUGIN_PRD.md`.  
Bloqueios: implementação/ativação de plugin exige approval packet.

### F2-DLV-001 — Define deliverable mode policy

Risk: A0/A2  
Assignee inicial: unassigned.  
Saída: seção curta no manual + template de receipt.  
Bloqueios: não alterar crons/deliveries existentes.

### F2-PILOT-001 — Select first real pilot

Risk: A2/A3 dependendo da escolha  
Assignee inicial: unassigned.  
Dependências: F2-MCP-001, F2-PLG-001 e F2-DLV-001.  
Saída: approval packet específico para um piloto real.

## 12. Approval packet mínimo para criar board real

Antes de executar `hermes kanban boards create` ou criar cards reais, pedir aprovação com:

- board slug: `hermes-lk-improvements`;
- confirmação de que cards serão criados `unassigned`;
- comando exato;
- rollback: arquivar/remover board se criado errado, sem apagar histórico de outro board;
- verificação: `hermes kanban boards list`, `hermes kanban --board hermes-lk-improvements stats`;
- garantia: sem dispatcher manual e sem worker assignment.

## 13. Status final do F2-001

F2-001 está concluído como design documental.

Próxima ação segura:

- seguir para **F2-002 — MCP/DataForSEO inventory read-only**, ou
- transformar este design em board real **somente com aprovação explícita**, criando cards unassigned e sem dispatcher/assignee.
