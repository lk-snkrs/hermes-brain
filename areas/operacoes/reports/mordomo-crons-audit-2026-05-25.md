# Auditoria dos crons do Mordomo — 2026-05-25

## Veredito atualizado

Aprovado e aplicado localmente nos itens 1–5. A base técnica segue funcionando e a camada de comunicação foi endurecida para não mandar log jogado para Lucas.

O padrão agora é: artefato local completo, Telegram só para decisão/alerta real, com mensagem humana, emoji funcional e negrito HTML.

## Mudanças aplicadas

1. Resumo 17h do WhatsApp/Mordomo
   - Script: `/opt/data/profiles/mordomo/scripts/mordomo_whatsapp_daily_digest.py`.
   - Wrapper: `/opt/data/profiles/mordomo/scripts/mordomo_whatsapp_summary_17.sh`.
   - Agora grava o relatório completo localmente, mas só interrompe Lucas quando há cliente/lead com decisão real.
   - Removeu da mensagem ao Lucas termos internos como status cru, tier, autonomia e classes técnicas.
   - Usa Telegram direto quando possível; stdout fica vazio em sucesso para evitar wrapper do scheduler.

2. Calendário global
   - Script: `/opt/data/profiles/mordomo/scripts/mordomo_calendar_global_watch.py`.
   - Alertas foram convertidos para padrão V3:
     - emoji funcional;
     - negrito HTML;
     - contexto;
     - compromisso/conflito/problema;
     - próximo passo.
   - Continua read-only e silent-OK.
   - Erros são reportados como alerta limpo, sem segredo.

3. Destinos e governança
   - `local` fica para logs, artefatos, ingestões e syncs.
   - Telegram/origin fica reservado para decisão real, alerta urgente, aprovação ou erro.
   - Jobs com Telegram direto mantêm fallback limpo por stdout caso o envio direto falhe.

4. Watchdog do gateway
   - Política documentada no checklist mensal: observar e alertar é permitido; alterar/reiniciar Docker/gateway/Traefik/VPS segue exigindo aprovação explícita com plano e rollback, salvo exceção previamente documentada.

5. Checklist mensal
   - Criado em `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/reports/mordomo-cron-governance-checklist.md`.

## Evolução de produto aplicada — 1 a 5

1. Botões seguros no Telegram
   - Alertas WhatsApp/Decision Inbox agora podem sair com botões funcionais: resolvido, criar/ajustar rascunho, lembrar amanhã e ignorar contato.
   - Callback `mw:*` foi conectado ao gateway Telegram e chama `/opt/data/profiles/mordomo/scripts/mordomo_whatsapp_callback_action.py`.
   - Botões mutam estado local e removem o teclado após uso. Envio externo só ocorre quando Lucas clica explicitamente em botão de envio de sugestão já pré-visualizada.

2. Score de confiança humano
   - Mensagens ao Lucas mostram `Confiança: alta/média/baixa` com explicação curta.
   - Risco técnico A1/A2/A3 fica fora do texto principal ao Lucas.

3. Deduplicação entre superfícies
   - Criado estado `/opt/data/profiles/mordomo/state/mordomo_decision_inbox_dedupe.json`.
   - O digest evita repetir a mesma decisão entre 09h/17h/watchers dentro da janela operacional, preservando alertas críticos após cooldown menor.

4. Painel local de auditoria
   - Criado `/opt/data/profiles/mordomo/scripts/mordomo_decision_dashboard.py`.
   - Output: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/decision-inbox/mordomo-decision-dashboard.md`.
   - Painel pode ser detalhado; Telegram continua limpo.

5. Regras semânticas Zipper mais fortes
   - Perguntas de Pix, pagamento, cor, medida, entrega, reserva, preço e disponibilidade viram decisão humana/baixa confiança.
   - Interesse simples pós-PDF pode virar rascunho, mas sem preço/disponibilidade específica.

## Evidências verificadas

- `py_compile` passou para os scripts principais do Mordomo e para o gateway Telegram alterado.
- Preview do resumo 17h foi gerado sem termos proibidos na saída ao Lucas.
- O relatório local do resumo 17h continua sendo gravado em `decision-inbox/`.
- Testes de regressão executados e aprovados: `test_mordomo_daily_digest.py`, `test_mordomo_callback_learning.py`, `test_mordomo_whatsapp_filters.py`.
- Painel local gerado com sucesso em `decision-inbox/mordomo-decision-dashboard.md`.
- Preview do Calendar V3 foi validado sem termos proibidos.

## Estado dos jobs principais

- WhatsApp watcher global: ativo, every 5m, silent-OK.
- Calendar watcher global: ativo, every 15m, silent-OK com alerta V3.
- CRM local sync: ativo, local-only.
- Decision Inbox 09h: ativo, Telegram direto, alerta só para urgência real.
- Resumo 17h: ativo, Telegram direto só se houver decisão real; artefato local sempre.
- Executor A2: pausado por segurança.

## Risco residual

Baixo-médio.

O risco principal agora não é mais formato, é semântica: se a fila local classificar errado uma conversa como decisão real, o resumo 17h ainda pode alertar. Por isso o checklist mensal exige regressão contra ruído e revisão dos termos proibidos.

## Critério de pronto daqui para frente

Um cron do Mordomo só está pronto se:

- roda sem erro;
- escreve artefato local quando útil;
- fica silencioso quando não há decisão;
- se falar com Lucas, fala em formato V3;
- não inclui log técnico, JSON, job ID ou classe interna;
- não envia nada externo sem aprovação explícita.
