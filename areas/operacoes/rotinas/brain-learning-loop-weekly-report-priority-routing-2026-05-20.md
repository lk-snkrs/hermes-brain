# Brain Learning Loop — Relatório semanal + roteamento de prioridade

Data: 2026-05-20
Status: ativo para o cron das 02h e rotina semanal.

## Objetivo

Transformar o Learning Loop diário das 02h em um ciclo de aprendizagem mais gerenciável para Lucas:

1. **Diário às 02h BRT:** roda silencioso por padrão, audita o sistema e registra aprendizado local no Brain.
2. **Semanal:** consolida os aprendizados reais da semana em um relatório executivo curto para Lucas.
3. **Prioridade ativa:** evita espalhar energia entre LK, Mission Control, Zipper, SPITI e Mordomo; escolhe foco por evidência recente.

## Contrato diário

O cron `f5a23dd6a1bd` é o Learning/Intelligence Loop principal.

Ele deve:

- usar o fechamento das 23h como insumo;
- validar estado vivo antes de concluir;
- gerar relatório local em `reports/hermes-continuous-improvement/YYYY-MM-DD.md`;
- atualizar Brain/skills/CHANGELOG quando houver aprendizado durável;
- manter Telegram silencioso em sucesso normal;
- avisar Lucas só por exceção, decisão necessária ou oportunidade material.

## Relatório semanal

O relatório semanal deve responder:

- O que o Hermes aprendeu esta semana?
- Quais correções de Lucas viraram guardrails/skills/docs?
- Quais erros ou alertas se repetiram?
- Quais mecanismos melhoraram?
- Quais prioridades mudaram?
- O que precisa de decisão de Lucas?
- Qual é o próximo melhor passo?

Formato desejado para Telegram:

- curto;
- executivo;
- sem logs crus;
- sem segredos;
- com links/caminhos dos artefatos locais quando úteis;
- decisões pendentes devem vir inline, não apenas como arquivo local.

Artefato local esperado:

- `reports/hermes-learning-weekly/YYYY-WW.md` ou nome equivalente com intervalo de datas.

## Roteamento de prioridade ativa

O Learning Loop deve classificar o foco da semana/dia usando evidência, não memória estática.

### Fontes de evidência, em ordem

1. Pedidos explícitos recentes de Lucas nas conversas.
2. Tarefas em andamento no contexto atual/sessões recentes.
3. Relatório das 23h e relatório das 02h anterior.
4. Artefatos Brain recentes: PRDs, reports, changelog, rotinas atualizadas.
5. Crons/watchdogs com alertas ou falhas recentes.
6. Memória/perfil apenas como baseline, nunca como verdade final.

### Saída obrigatória da seção de prioridade

Todo relatório diário/semanal deve registrar:

- **Foco principal:** uma área só, salvo emergência real.
- **Por que:** 2–4 evidências.
- **Modo das outras áreas:** manutenção, monitoramento, aguardando Lucas, ou bloqueado.
- **Risco de dispersão:** baixo/médio/alto.
- **Próxima ação segura:** uma ação concreta, sem write externo por padrão.

### Rubrica

- **P0 foco do dia:** pedido explícito recente + trabalho em andamento + impacto operacional.
- **P1 manutenção ativa:** rotina recorrente saudável com alertas úteis ou oportunidade clara.
- **P2 monitoramento:** sem pedido recente, sem alerta crítico, manter watchdogs.
- **Blocked/approval:** precisa de write externo, Docker/runtime, fonte de verdade, cliente, dinheiro, campanha, fornecedor, banco ou segredo.

## Limites

Mesmo quando a prioridade for clara, o Learning Loop não deve executar automaticamente:

- Docker/runtime/gateway/host/Traefik/network changes;
- Shopify/GMC/Ads/source-of-truth writes;
- envio a cliente/fornecedor/e-mail/WhatsApp/Telegram externo;
- compras/reservas/negociação;
- segredo/config sensível;
- ação destrutiva.

Nesses casos, produzir decision brief com scope, payload, risco, rollback e recomendação.
