# Rotina — Mordomo Global Follow-up Engine

Atualizado: 2026-05-19
Status: v0.2 — follow-up automático de cliente aprovado e ativado com guardrails

## Decisão operacional

Lucas quer que o Mordomo seja responsável pela fila de follow-ups sem depender de Lucas lembrar. Follow-up não deve ser template fixo; deve variar pelo histórico e pela resposta anterior.

Decisão de Lucas por voz em 2026-05-19: **follow-ups de clientes podem ser feitos automaticamente pelo Mordomo**, sem pedir aprovação caso a conversa já tenha contexto claro e o follow-up não envolva preço, disponibilidade, reserva, negociação, reclamação, compra/fornecedor, campanha/bulk ou promessa material. Depois que o cliente responder, o Mordomo também pode responder automaticamente quando a resposta for conhecida e verificável por fonte/documento confiável.

## Implementação atual

Script ativo:

- `/opt/data/profiles/mordomo/scripts/mordomo_whatsapp_global_watch.py`
- Wrapper cron: `/opt/data/scripts/mordomo_whatsapp_global_watch.sh`
- Política/kill switch: `/opt/data/profiles/mordomo/config/mordomo_autonomy_policy.json`

Estado local:

- `/opt/data/profiles/mordomo/state/mordomo_whatsapp_global_watch.json`
- `/opt/data/profiles/mordomo/state/mordomo_followup_queue.json`

Cron ativo:

- `Mordomo global WhatsApp follow-up autopilot`
- Job ID: `cca00bf0a682`
- Frequência: `every 5m`
- Modo: `no_agent`

## Comportamento

A cada execução, o Mordomo:

1. sincroniza o WhatsApp pessoal de Lucas;
2. varre chats recentes;
3. classifica sinais em `pessoal`, `zipper`, `lk`, `spiti`, `hermes` ou `unknown`;
4. registra sinais relevantes na fila;
5. mantém follow-ups estruturados;
6. quando um follow-up vence, lê o histórico recente;
7. se estiver dentro da allowlist e sem bloqueios, envia o follow-up automaticamente;
8. registra receipt local em `sent_actions` e avisa o Telegram;
9. se houver bloqueio, gera alerta/rascunho contextual;
10. fica silencioso quando não há sinal acionável.

## Política de envio externo

A fila é autônoma para detectar, registrar, decidir risco e executar follow-up de cliente. O envio externo automático está habilitado para subfluxos fechados com:

- intenção allowlisted;
- regra de bloqueio por preço/disponibilidade/reserva/negociação/reclamação/promessa;
- histórico recente verificado antes de envio;
- dedupe por follow-up;
- log de mensagem enviada;
- kill switch em `mordomo_autonomy_policy.json`;
- fonte de verdade definida quando houver dado material.

Quando o subfluxo não passar nos guardrails, o motor prepara rascunho e alerta Lucas/Hermes, mas não envia.

## Subfluxo candidato — Zipper pós-PDF sem resposta

Condição:

- contexto `zipper`;
- intenção `post_pdf_followup`;
- status `waiting_client` / `safe_to_followup`;
- `due_at` vencido;
- sem nova resposta substantiva do cliente pedindo preço, disponibilidade, condição, reserva ou negociação.

Rascunho fallback aprovado para silêncio:

```text
Olá {{nome}}, tudo bem?

Gostaria de saber se alguma das obras do PDF despertou seu interesse.

Fico à disposição para te passar mais informações.
```

Bloqueios para auto-envio:

- cliente pediu preço;
- cliente pediu disponibilidade;
- cliente citou obra específica;
- cliente negociou condição/pagamento;
- cliente pediu reserva;
- cliente é arquiteto/projeto e o histórico pede abordagem específica;
- há resposta nova ainda não interpretada.

## Respostas quando o cliente responde

Autorizado: o Mordomo pode responder automaticamente perguntas simples quando a resposta estiver conhecida/verificada. Exemplos seguros:

- reenviar PDF/catálogo correto já mapeado;
- confirmar informação factual presente no histórico/documento aprovado;
- orientar próximo passo neutro sem prometer preço, reserva, disponibilidade ou prazo.

Bloqueios continuam automáticos para preço, disponibilidade, reserva, negociação, reclamação, pagamento, promessa operacional, SPITI lote/lance sem fonte oficial, fornecedor/compra e campanhas/bulk.

## Próxima melhoria

Expandir a camada de `known answers` para consultar PDFs/propostas/artistas/obras por fonte estruturada antes de responder automaticamente. Até essa camada estar completa, respostas automáticas ficam restritas ao que o runtime consegue verificar com segurança no histórico/política; casos materiais viram bloqueio com rascunho.
