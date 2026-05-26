# Critérios — quando Zipper deve ganhar profile próprio

Status: critério documental; runtime dedicado ainda não aprovado  
Owner documental: Zipper OS  
Supervisor: Hermes Geral / COO  
Executor técnico atual: Hermes Geral/Mordomo, conforme rota  
Writes externos/runtime: não

## Decisão atual

Zipper permanece dentro do contrato documental/read-only e, operacionalmente, parte dos fluxos segue pelo Mordomo quando envolve inbox, WhatsApp, e-mail ou follow-up.

Criar um profile próprio Zipper só faz sentido se houver sinal claro de volume, risco, autonomia ou separação de contexto suficiente para justificar novo runtime/bot/cron.

## Estado atual observado

- Há agente documental Zipper em `agentes/zipper/`.
- Há área operacional em `areas/zipper/`.
- Existem crons/rotinas Zipper distribuídos entre Main e Mordomo.
- Contato externo, colecionadores, curadoria, negociação e comunicação continuam approval-gated.
- Grupo `[ZPR] IA Bot` deve responder com fontes Zipper read-only quando Hermes for marcado; não é Telegram.

## Manter no Mordomo/Hermes Geral quando

- O fluxo é baixo volume ou eventual.
- O output é rascunho interno, análise, classificação ou intake.
- O risco principal é triagem pessoal/inbox/follow-up.
- A resposta pode ser resolvida com Brain + fontes Zipper read-only.
- Não há necessidade de identidade conversacional separada.
- Não há entrega recorrente de alto valor que exija canal próprio.

## Promover para profile próprio quando 2+ critérios forem verdadeiros por pelo menos 2 semanas

### Volume

- Mais de 5 interações Zipper relevantes por semana exigindo contexto próprio.
- Mais de 3 outputs materiais por semana: rascunhos de colecionador, reports, listas de obra, follow-ups ou análises de venda.
- Inbox/WhatsApp/e-mail Zipper começa a competir com Lucas pessoal ou LK no Mordomo.

### Risco de contexto

- Confusão recorrente entre Zipper, SPITI e LK.
- Necessidade de preservar tom cultural/galeria sem contaminar Mordomo pessoal.
- Decisões ou rascunhos sensíveis de colecionador/obra ficam misturados com rotinas pessoais.

### Autonomia operacional

- Rotinas Zipper passam a precisar de cadência própria.
- Equipe Zipper precisa consultar um bot/canal dedicado.
- Há necessidade de handoffs próprios frequentes para Osmar, Helo, Biz, Mie, Cibele ou Panda.

### Integrações/fonte

- Uso recorrente de `vendas_tango` ou CRM/Main Zipper como fonte read-only.
- Necessidade de ledger próprio para artistas, obras, colecionadores, feiras ou comunicação.
- Necessidade de separar logs/receipts por empresa para auditoria.

### UX

- Lucas sinaliza que Zipper está gerando ruído no Mordomo.
- Mensagens Zipper precisam de canal próprio para equipe.
- Há necessidade de bot com identidade explícita Zipper.

## O que profile próprio permitiria

- `HERMES_HOME=/opt/data/profiles/zipper` isolado.
- Bot/canal Zipper dedicado, se aprovado.
- Cron registry próprio para rotinas Zipper.
- Memória/skills/contexto separados.
- Watchdog próprio silent-OK.
- Handoff obrigatório para Hermes Central.

## O que continua bloqueado mesmo com profile próprio

- Contatar colecionadores sem aprovação.
- Enviar WhatsApp/e-mail externo sem aprovação.
- Tomar decisão de curadoria, preço ou negociação.
- Afirmar desempenho de obra/artista sem consultar fonte real.
- Misturar dados SPITI ou LK.
- Criar gateway, bot, cron ou profile runtime sem aprovação explícita.

## Pacote mínimo antes de criar runtime

Se a promoção for aprovada no futuro, preparar antes:

1. Escopo do profile e canais autorizados.
2. Lista de crons a migrar/criar.
3. Backups dos registries afetados.
4. Plano de rollback.
5. Secret/env checklist sem imprimir valores.
6. Watchdog silent-OK.
7. Handoff/receipt template.
8. Teste read-only de boot e fontes.

## Veredito atual

Não criar profile Zipper agora. Manter como documental/read-only sob Mordomo/Hermes Geral e reavaliar quando houver volume, risco ou demanda de canal próprio.
