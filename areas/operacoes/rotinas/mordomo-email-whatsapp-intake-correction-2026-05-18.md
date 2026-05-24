# Mordomo — correção de intake e respostas (e-mail + WhatsApp pessoal Lucas)

Data: 2026-05-18

## Problema identificado

No caso Felipe / Flávia Junqueira, Lucas viu resposta/estado no celular antes do Mordomo conseguir enxergar no espelho local do `wacli`. Isso torna o fluxo inseguro: o Mordomo não pode depender de Lucas mandar print para saber se houve resposta.

Correção conceitual de Lucas: o WhatsApp usado para Zipper não é “WhatsApp da Zipper”; é o WhatsApp pessoal de Lucas Cimino, que cuida de várias frentes, inclusive Zipper. A relação comercial da Zipper é pessoal e o envio pelo WhatsApp de Lucas aumenta credibilidade. Internamente o Mordomo deve classificar/salvar como Zipper OS quando o assunto for Zipper, mas a superfície de conversa é Lucas pessoal.

## Correção operacional

### WhatsApp

1. Manter um watcher recorrente para conversas comerciais ativas.
2. Rodar `wacli --account pessoal sync --once` de forma periódica e limitada.
3. Ler mensagens novas nas conversas em follow-up.
4. Quando houver inbound novo:
   - alertar Lucas no Telegram;
   - incluir lead/contexto/mensagem;
   - preparar a próxima resposta, mas não enviar sem aprovação, salvo subfluxo fechado já aprovado.
5. Manter estado de mensagens vistas para não repetir alertas.

Watcher criado:

- Script: `/opt/data/profiles/mordomo/scripts/zipper_whatsapp_response_watch.py`
- Cron: `Lucas personal WhatsApp — Zipper lead watcher` / job `6f4c913082db`
- Frequência: a cada 5 minutos
- Modo: `no_agent`, silencioso quando não houver resposta nova

Conversas inicialmente monitoradas:

- Felipe — Flávia Junqueira
- Anna Campos — Flávia Junqueira

### E-mail

Próxima etapa do mesmo padrão, preferindo evento/webhook em vez de polling quando possível. Lucas sugeriu usar n8n para isso; tecnicamente faz sentido.

1. Preferir evento/webhook: Gmail/Google Workspace ou n8n detecta novo e-mail/label/thread e chama endpoint do Hermes.
2. Hermes recebe payload, classifica por domínio: pessoal, Zipper, SPITI, LK, infra.
3. Para Zipper: extrair artista/obra/lead/canal, registrar no CRM/Brain e gerar draft/resposta.
4. Enviar automaticamente apenas em fluxos fechados aprovados; caso contrário, pedir aprovação no Telegram.
5. Usar polling apenas como fallback/monitor de saúde quando webhook/n8n falhar.

## Guardrails

- Nenhuma resposta externa automática sem escopo aprovado.
- PDF/catálogo Zipper por WhatsApp deve ir sem caption e sem texto salvo aprovação.
- Negociação, reserva, desconto, disponibilidade sensível e reclamação sempre sobem para Lucas.
- Estado do watcher deve ser persistido para evitar alertas duplicados.
