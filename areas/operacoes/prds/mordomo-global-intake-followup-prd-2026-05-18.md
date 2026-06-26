# PRD — Mordomo Hermes Global: Intake, Contexto e Follow-ups Autônomos

Atualizado: 2026-05-18
Status: v0.1 — base operacional aprovada conceitualmente por Lucas; implementação por fases

## 1. Decisão de produto

Lucas quer que o Mordomo Hermes funcione como uma secretária/CRM global, não como automações isoladas por fluxo.

O Mordomo deve saber o que acontece no WhatsApp, e-mail e calendário de Lucas, cruzar esse contexto com LK, Zipper, SPITI e assuntos pessoais, manter uma fila própria de pendências/follow-ups e agir de forma inteligente sem depender de Lucas lembrar cada caso.

A regra central é:

> O Mordomo lê globalmente, entende contexto globalmente, mas salva e age no domínio correto.

## 2. Objetivo

Criar uma camada operacional única para:

1. ler sinais de WhatsApp, e-mail e calendário;
2. classificar cada sinal como pessoal, LK, Zipper, SPITI, Hermes/Infra ou desconhecido;
3. detectar eventos, consultas médicas, reuniões, clientes, fornecedores, leads, vendas, entregas e pendências;
4. manter uma fila viva de follow-ups;
5. executar follow-ups seguros sozinho quando o contexto permitir;
6. escalar para Lucas apenas decisões, riscos, exceções ou respostas que exigem julgamento humano;
7. registrar aprendizado em Brain, skills e memória para não repetir correções.

## 3. Escopo inicial

### 3.1 Canais

- WhatsApp pessoal de Lucas via `wacli --account pessoal`.
- Contas de e-mail autorizadas já mapeadas no PRD de e-mail intake.
- Calendários de Lucas e calendários operacionais autorizados.
- Brain local como camada documental.
- Supabase/CRM por empresa quando existir fonte estruturada.

### 3.2 Domínios

- Lucas pessoal: consultas médicas, eventos, compromissos, família, tarefas pessoais.
- Zipper OS: clientes, colecionadores, artistas, PDFs, propostas, obras, disponibilidade, logística, feiras.
- LK OS: clientes, vendas, estoque, campanhas, fornecedores, Júlio, encomendas, recompra, relatórios.
- SPITI OS: clientes, lotes, leilões, lances, consignações, follow-ups.
- Hermes/Infra: alertas técnicos, deploys, crons, automações, tokens, VPS.

## 4. Não escopo / limites

O Mordomo não deve virar um disparador cego.

Mesmo com autonomia de follow-up, continuam bloqueados sem regra aprovada ou validação contextual:

- prometer preço, desconto, reserva, disponibilidade ou prazo sem fonte;
- negociar valores;
- assumir compromisso operacional sensível;
- responder sobre obra/lote/produto sem verificar fonte de verdade;
- enviar campanha, newsletter ou mensagem massiva;
- fazer alterações em Shopify, Tiny, Merchant, Supabase de produção, Vercel, VPS ou Docker;
- expor dados pessoais ou segredos.

## 5. Princípio de autonomia

Lucas corrigiu que follow-up não deve depender de aprovação caso a pendência seja clara e segura.

A autonomia deve ser por classe de risco, não por canal.

### A0 — leitura e classificação

Executar sozinho.

Exemplos:

- ler WhatsApp/e-mail/calendário autorizado;
- classificar contexto;
- detectar pendência;
- criar/atualizar estado local;
- registrar caso no Brain/CRM;
- gerar resumo interno.

### A1 — follow-up interno ou administrativo seguro

Executar sozinho.

Exemplos:

- criar lembrete;
- atualizar fila de follow-up;
- alertar Lucas;
- marcar caso como aguardando resposta;
- criar evento claro de calendário quando data/hora/local forem explícitos e a regra do domínio permitir;
- registrar que um cliente deve ser acompanhado.

### A2 — follow-up externo fechado e seguro

Pode executar sozinho apenas quando houver subfluxo aprovado, texto dentro de limites e sem promessa material.

Exemplos potenciais:

- Zipper: follow-up leve após PDF quando não houve resposta ou houve “vou olhar”, sem preço/disponibilidade/negociação.
- Pessoal: confirmar internamente lembrete de consulta/evento, sem falar com terceiros se houver ambiguidade.
- LK: follow-up operacional interno em grupos/contatos aprovados, quando o conteúdo é pergunta de status simples e não envolve compra/cliente/fornecedor externo sensível.

Toda execução A2 deve gerar log com:

- canal;
- destinatário;
- contexto;
- texto enviado;
- motivo da autonomia;
- link/ID da mensagem;
- próxima verificação.

### A3 — ação com decisão operacional

Preparar sozinho, mas pedir confirmação ou fonte antes de enviar/executar.

Exemplos:

- cliente pediu preço;
- cliente pediu disponibilidade de obra;
- fornecedor pediu confirmação de compra;
- cliente LK pediu troca, desconto ou exceção;
- SPITI pediu informação de lote/lance;
- qualquer promessa comercial.

### A4 — externo sensível, produção, dinheiro, segredo ou infra

Sempre aprovação explícita no turno atual.

## 6. Motor de classificação

Cada item de WhatsApp/e-mail/calendário deve virar um `signal` com campos mínimos:

- `source_channel`: whatsapp / email / calendar / telegram / system;
- `source_account`;
- `contact_id`;
- `contact_name`;
- `business_context`: pessoal / lk / zipper / spiti / hermes / unknown;
- `intent`;
- `risk_level`: A0/A1/A2/A3/A4;
- `summary`;
- `raw_pointer`: ID do e-mail/mensagem/evento, sem despejar conteúdo sensível;
- `detected_at`;
- `due_at`, se houver;
- `next_action`;
- `status`.

## 7. Tipos de intenção

### Pessoal

- consulta médica;
- evento social;
- reunião;
- viagem;
- boleto/pagamento;
- documento;
- família/amigos;
- pendência pessoal.

### Zipper

- lead de artista;
- pedido de PDF;
- interesse em obra;
- pedido de preço/disponibilidade;
- arquiteto/projeto;
- logística de obra;
- feira/evento;
- proposta;
- pós-envio de PDF;
- follow-up de cliente.

### LK

- pedido/cliente;
- estoque/tamanho/SKU;
- campanha;
- fornecedor;
- Júlio/compra;
- logística;
- recompra/RFM;
- relatório;
- problema operacional.

### SPITI

- lote;
- lance;
- consignação;
- bidder;
- leilão;
- documento;
- proposta;
- follow-up comercial.

### Hermes/Infra

- erro de cron;
- deploy;
- token;
- VPS;
- Docker;
- ferramenta;
- automação quebrada.

## 8. Follow-up engine

Follow-up não é template fixo. O Mordomo deve usar o histórico anterior para decidir a próxima ação.

Antes de qualquer follow-up, ler:

1. última mensagem do contato;
2. última mensagem enviada por Lucas/Hermes;
3. histórico recente do canal;
4. Brain/CRM do contato, se existir;
5. calendário ou evento relacionado;
6. fonte de verdade do domínio, se a resposta pedir dado material.

### Estados de follow-up

- `waiting_client`: aguardando cliente.
- `client_replied`: cliente respondeu; precisa interpretar.
- `needs_info`: falta fonte de verdade.
- `needs_lucas_decision`: depende de Lucas.
- `safe_to_followup`: follow-up leve pode ser feito.
- `done`: resolvido.
- `snoozed`: adiado com motivo.

### Regra de estilo

- Zipper: elegante, cultural, sem hard sell.
- LK: direto, premium, operacional, comercial sem parecer barato.
- SPITI: preciso, conservador, sem chutar dados.
- Pessoal: natural, discreto e objetivo.

## 9. Zipper — regra específica já aprendida

Para leads genéricos de artista/obra:

- Não falar da obra específica do site no primeiro contato.
- Não explicar que pode estar vendida.
- Falar das obras disponíveis do/do artista.
- Ajustar gênero: `do artista` para homem, `da artista` para mulher.
- Primeiro contato não pergunta “qual chamou atenção”; só apresenta e envia PDF.
- PDF vai sem caption.
- Follow-up varia pela resposta anterior.
- Se não houve resposta, fallback aprovado:

```text
Olá {{nome}}, tudo bem?

Gostaria de saber se alguma das obras do PDF despertou seu interesse.

Fico à disposição para te passar mais informações.
```

Esse fallback não é fixo universal; só serve para silêncio/não resposta substantiva.

## 10. Observabilidade e alertas

O Mordomo deve ser silencioso quando nada exige ação.

Alertar Lucas quando:

- há decisão real;
- há risco;
- há oportunidade quente;
- houve falha de automação;
- um follow-up autônomo foi enviado e merece ciência;
- uma mensagem é ambígua e pode mudar a resposta;
- uma fonte de verdade está indisponível.

Não alertar Lucas apenas para dizer “nada novo”.

## 11. Arquitetura v1

### 11.1 Watchers

- WhatsApp global watcher: varre chats recentes e grupos relevantes do WhatsApp pessoal; classifica sinais por contexto.
- E-mail intake watcher: usa o PRD de e-mail já existente.
- Calendar watcher: identifica eventos novos, conflitos e pendências.
- Follow-up scheduler: controla `due_at`, estados e próxima ação.

### 11.2 Estado local

Enquanto Supabase/CRM global não estiver completo, manter estado local em arquivos JSON/SQLite restritos:

- signals;
- contacts;
- followups;
- sent_actions;
- pending_decisions;
- tone_profiles.

### 11.3 Brain

Registrar decisões e padrões duráveis em:

- `areas/operacoes/` para regras globais;
- `areas/zipper/` para Zipper;
- `areas/lk/` para LK;
- `areas/spiti/` para SPITI;
- skills correspondentes quando houver procedimento repetível.

## 12. Implementação por fases

### Fase 1 — Unificar PRD e regras

Critério de conclusão:

- este PRD salvo;
- skills atualizadas;
- memória atualizada;
- guardrails de follow-up explícitos.

### Fase 2 — WhatsApp global read-only

Critério de conclusão:

- watcher lê chats recentes do WhatsApp pessoal;
- não depende de allowlist;
- classifica sinais em pessoal/LK/Zipper/SPITI/Hermes/unknown;
- não envia nada;
- stdout silencioso quando não há ação.

### Fase 3 — Fila global de follow-ups

Critério de conclusão:

- follow-ups viram registros estruturados;
- cada registro tem dono/contexto/due_at/status/risk;
- há relatório Telegram apenas para ações/decisões;
- casos Zipper existentes migrados.

### Fase 4 — Execução autônoma A1/A2

Critério de conclusão:

- regras fechadas por domínio;
- logs de envio;
- kill switch;
- dry-run antes de ativar;
- primeiro subfluxo aprovado: Zipper pós-PDF sem resposta.

Status atual: modo seguro implementado parcialmente. O watcher global já controla vencimento de follow-up e gera rascunho contextual quando algo vence. O envio externo automático ainda fica bloqueado até existir executor A2 com validação de histórico recente, kill switch e log de envio.

### Fase 5 — Integração com CRM/Supabase

Critério de conclusão:

- contatos/followups salvos na base correta por empresa;
- Brain vira camada de decisão/conhecimento, não banco principal;
- histórico recuperável por contato.

## 13. Próximos passos recomendados

1. Transformar o atual watcher Zipper em `mordomo_whatsapp_global_watch.py`.
   - Conclusão: script varre WhatsApp pessoal inteiro e classifica sinais sem enviar.
2. Criar `mordomo_followup_queue.json` ou SQLite local.
   - Conclusão: cada pendência tem estado, vencimento e risco.
3. Migrar follow-ups Zipper atuais para a fila global.
   - Conclusão: nenhum cron solto por lead sem aparecer na fila.
4. Rodar 24h em dry-run/silent mode.
   - Conclusão: relatório só de sinais acionáveis, sem spam.
5. Ativar primeiro subfluxo A2 fechado.
   - Conclusão: follow-up Zipper pós-PDF sem resposta pode ser enviado sozinho com log, salvo se houver pedido de preço/disponibilidade/negociação.

## 14. Métrica de sucesso

O sistema está funcionando quando:

- Lucas não precisa lembrar o Mordomo de follow-ups óbvios;
- mensagens importantes não ficam invisíveis;
- cada sinal cai no contexto correto;
- o Mordomo sabe quando agir, quando preparar e quando escalar;
- Lucas recebe menos ruído e mais decisões claras;
- nenhuma mensagem externa sensível é enviada sem regra ou contexto suficiente.
