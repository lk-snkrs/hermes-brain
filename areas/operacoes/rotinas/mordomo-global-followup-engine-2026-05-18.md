# Rotina — Mordomo Global Follow-up Engine

Atualizado: 2026-05-21
Status: v0.3 — follow-up automático de cliente aprovado com Autonomy Registry, Decision Inbox, Contact Profiles e Learning Loop

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

## Known answers v1

A camada de known answers é fonte-grounded e não é uma autorização de envio.

### Escopo atual

- Contexto suportado: Zipper.
- Fonte local estruturada: `/opt/data/zipper_artist_pdfs/manifest.json`.
- Unidade de conhecimento: artista/PDF/seleção comercial validada; não indexar nem depender de nomes/títulos de obras.
- Pode confirmar internamente que existe PDF comercial/seleção validada de um artista.
- Pode anexar ao Decision Packet o status, risco, filename e hash prefix do PDF.

### Limites obrigatórios

- Manifest/PDF de artista **não** é fonte oficial para preço, disponibilidade específica, reserva, pagamento, desconto, dimensão, frete ou condição.
- Perguntas materiais viram `blocked_material_question`, risco A3, `allow_external_send=false`.
- Artista/PDF desconhecido vira `insufficient_source`; não inventar.
- Mesmo quando `answerable_draft`, o resolver retorna draft/preview e `allow_external_send=false`; envio externo continua nas regras de autonomia e aprovação.

### Integração runtime

- Função: `resolve_known_answer(...)` em `/opt/data/profiles/mordomo/scripts/mordomo_whatsapp_global_watch.py`.
- Ingest automático local-only: `/opt/data/profiles/mordomo/scripts/zpr_artist_pdf_local_ingest.py` roda a cada 30 minutos via cron `Zipper artist PDFs local-only known-answer ingest`.
- O ingest automático lê apenas `/opt/data/profiles/mordomo/cache/documents`, copia PDFs comerciais para `/opt/data/zipper_artist_pdfs/` e atualiza o manifest local; não lê Doppler, não chama Supabase e não faz envio externo.
- Casos de obra esgotada/alternativas anexam `known_answer` no metadata do Strategy quando o cliente responde ou traz pergunta material.
- `due_followup_alert(...)` exibe o known answer no alerta para Lucas, sem enviar WhatsApp/e-mail.
- Regressão: `/opt/data/profiles/mordomo/scripts/test_mordomo_whatsapp_filters.py` cobre PDF disponível, pergunta de preço/disponibilidade bloqueada e artista sem fonte.
- Regressão do ingest: `/opt/data/profiles/mordomo/scripts/test_zpr_artist_pdf_local_ingest.py` cobre local-only, dedupe por hash, inferência de artista e zero escrita externa.

## Checkpoint de aprendizado operacional

Toda correção de Lucas sobre o Mordomo deve ser classificada no mesmo ciclo, para não ficar apenas no chat.

### Destinos por tipo de correção

1. **Regra durável de comportamento**
   - Atualizar memória compacta quando for uma preferência ou regra transversal que reduz repetição futura.
   - Atualizar esta rotina ou PRD/KB no Brain quando for regra operacional.
   - Atualizar skill relevante quando a regra precisa orientar execuções futuras.

2. **Regra de empresa ou contexto comercial**
   - Salvar no Brain da empresa correta: Zipper, SPITI, LK ou Operações.
   - Não misturar dados de uma empresa em outra.
   - Se envolver CRM/follow-up, refletir no estado local ou banco correto.

3. **Regra de autonomia**
   - Atualizar `mordomo_autonomy_registry.json` para classe/risco/envio permitido.
   - Atualizar `mordomo_autonomy_policy.json` apenas se o escopo global mudar.
   - Rodar `mordomo_autonomy_policy_audit.py` e exigir `contradictions_count = 0`.

4. **Correção de contato/tom/preferência**
   - Atualizar Contact Profile por hash do contato, nunca dump bruto de JID/conversa.
   - Botões `ignore`/`silence` bloqueiam a classe para aquele contato e removem allowance equivalente.
   - Botão `draft` vira preferência `preview_only`; não autoriza envio.
   - Botão `remind9` vira preferência de pendência humana; não autoriza envio.
   - Uma resposta manual de Lucas é exemplo de tom, não autorização ampla.

5. **Correção de fila/CRM**
   - Atualizar `mordomo_followup_queue.json` e sincronizar SQLite local.
   - Se for Zipper/SPITI/LK com fonte oficial, espelhar no CRM/source-of-truth correto quando a integração estiver aprovada.
   - Sempre preservar status aberto quando a correção indicar que ainda há oportunidade, como obra esgotada que deve oferecer alternativas.

### Checklist obrigatório antes de encerrar uma correção

- [ ] A regra foi classificada: memória, Brain, skill, registry, Contact Profile, CRM/fila ou backlog.
- [ ] Nenhum envio externo foi feito sem aprovação atual, salvo subfluxo estreito já autorizado.
- [ ] Se houve mudança de autonomia, `mordomo_autonomy_policy_audit.py` passou.
- [ ] Se houve mudança em fila/snapshot, `mordomo_mission_control_snapshot.py` foi regenerado.
- [ ] Regressão local cobre o erro, quando aplicável.
- [ ] O plano/backlog registra o que mudou e o que ainda falta.
