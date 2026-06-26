# Base de Conhecimento — Mordomo Hermes: E-mails Recebidos

Atualizado: 2026-05-18
Status: v0.1 — conhecimento operacional inicial
PRD relacionado: `areas/operacoes/prds/mordomo-email-intake-prd-2026-05-18.md`

## 1. Propósito

Esta base de conhecimento reúne as regras práticas que o Mordomo deve usar ao lidar com e-mails que chegam nas contas autorizadas de Lucas.

Ela não substitui Gmail, Supabase, Brain por empresa nem PRDs. Ela funciona como camada de consulta operacional:

- quais caixas existem;
- como classificar cada e-mail;
- quais sinais extrair;
- quando virar tarefa, CRM, follow-up, digest ou decisão;
- quais ações são automáticas;
- quais ações exigem aprovação explícita.

## 2. Contas de e-mail conhecidas

### Confirmadas com acesso técnico

- `lucascimino@gmail.com`
  - Contexto padrão: Lucas pessoal/global.
  - Pode conter sinais multiempresa.
  - Sempre classificar antes de salvar/agir.

- `lucas@zippergaleria.com.br`
  - Contexto padrão: Zipper OS.
  - Usar para comunicações diretas de Lucas na galeria.
  - Também pode conter agenda, propostas, artistas, colecionadores, ARPA/feiras e logística.

- `producao@zippergaleria.com.br`
  - Contexto padrão: Zipper produção/logística.
  - Sinais típicos: retirada, coleta, entrega, montagem, desmontagem, transporte, calendário expositivo.

- `lk@lksneakers.com.br`
  - Contexto padrão: LK OS.
  - Sinais típicos: cliente, pedido, produto, campanha, financeiro, fornecedor, agência, Shopify/Tiny/CRM.

- `spiti@spiti.auction`
  - Contexto padrão: SPITI OS.
  - Sinais típicos: leilão, lote, consignação, lance, comprador, vendedor, operação de leilão.

### Não confirmada

- `zipper@zippergaleria.com.br`
  - Status: sem token Gmail válido encontrado no Doppler em 2026-05-18.
  - Não usar como fonte automatizada até acesso ser confirmado.

## 3. Regra-mãe de roteamento

Todo e-mail deve passar por roteamento antes de ação:

1. identificar conta de origem;
2. identificar empresa/contexto real;
3. detectar se é misto ou ambíguo;
4. escolher fonte de verdade correta;
5. decidir saída operacional;
6. aplicar guardrail de aprovação.

Nunca assumir que a conta de origem sozinha define o contexto. Exemplo: `lucascimino@gmail.com` pode receber assunto Zipper, LK, SPITI ou pessoal.

## 4. Taxonomia de classificação

### `lead_comercial`

Uso: cliente, arquiteto, colecionador, comprador ou interessado pede informação, catálogo, PDF, disponibilidade, obra, produto ou lote.

Extrair:

- nome;
- e-mail;
- telefone/WhatsApp;
- empresa/origem;
- artista/produto/lote;
- intenção;
- urgência;
- anexos relevantes;
- thread/message id.

Saída padrão:

- Zipper/SPITI/LK CRM update, se claro;
- draft ou Decision Packet;
- fluxo automático apenas se pré-aprovado.

### `operacional_logistica`

Uso: retirada, entrega, coleta, transporte, montagem, desmontagem, envio físico, agenda operacional.

Extrair:

- data;
- horário;
- local;
- pessoa responsável;
- obra/produto/documento envolvido;
- confirmação pendente;
- convidados necessários.

Saída padrão:

- tarefa interna;
- evento de calendário se regra permitir e dados estiverem completos;
- follow-up interno.

Regra Zipper:

- movimentação de obra usa calendário `lucas@zippergaleria.com.br`;
- quando aplicável, envolver produção/entregas;
- não assumir que o local é a Zipper só porque o calendário/categoria é Zipper.

### `financeiro_admin`

Uso: boleto, nota fiscal, cobrança, recibo, contrato, pagamento, reembolso, dados bancários.

Extrair:

- valor;
- vencimento;
- beneficiário;
- empresa/contexto;
- documento/anexo;
- risco de atraso;
- ação solicitada.

Saída padrão:

- Decision Packet ou tarefa interna;
- nunca pagar, aprovar, assinar ou enviar dados bancários sem aprovação explícita.

### `decisao_lucas`

Uso: e-mail pede decisão, aprovação, sim/não, orçamento, posicionamento, resposta comercial, confirmação.

Extrair:

- pergunta exata;
- contexto;
- deadline;
- opções;
- recomendação Hermes;
- payload sugerido se houver resposta externa.

Saída padrão:

- Decision Packet para Telegram.

### `newsletter_ruido`

Uso: newsletter, plataforma, promoção, spam, update genérico, relatório automático sem decisão.

Extrair:

- origem;
- tema;
- se há oportunidade real;
- se deve ser ignorado ou virar digest.

Saída padrão:

- ignorar/arquivar logicamente;
- digest agrupado;
- sugerir filtro/unsubscribe, sem executar sem aprovação.

### `documento_anexo`

Uso: e-mail cujo valor principal é um anexo ou documento.

Extrair:

- tipo de documento;
- nome do arquivo;
- quem enviou;
- a qual empresa/contexto pertence;
- ação pedida;
- sensibilidade/PII.

Saída padrão:

- salvar em fonte correta se permitido;
- registrar referência segura;
- não expor conteúdo sensível em Brain aberto.

### `desconhecido_misto`

Uso: contexto incerto, empresas misturadas, conteúdo ambíguo, risco de resposta errada.

Saída padrão:

- não agir externamente;
- pedir decisão ou classificar como pendente de roteamento.

## 5. Saídas operacionais padronizadas

### `FYI`

Resumo informativo sem ação.

Critério:

- não exige Lucas;
- não exige resposta;
- pode ser útil para digest.

### `Task`

Tarefa interna.

Campos mínimos:

- contexto;
- ação;
- dono sugerido;
- prazo se houver;
- fonte `message_id/thread_id`;
- risco.

### `Follow-up`

Lembrete futuro condicionado.

Campos mínimos:

- canal/thread;
- última mensagem relevante;
- data de follow-up;
- condição de disparo;
- texto/payload se for automático aprovado;
- parada se houver resposta.

### `Draft`

Resposta preparada, mas não enviada.

Uso:

- e-mail externo;
- WhatsApp externo;
- cliente, fornecedor, artista, parceiro, comprador, vendedor.

### `Decision Packet`

Pacote curto para Lucas aprovar/decidir.

Formato:

```text
Contexto: [empresa]
Origem: [conta/thread]
Resumo: [1-3 linhas]
Recomendação: [ação]
Risco: [baixo/médio/alto]
Payload: [se houver resposta]
Aprovação necessária: [sim/não]
```

### `CRM update`

Registro estruturado no Supabase correto.

Campos esperados:

- contato;
- origem;
- contexto;
- intenção/interesse;
- canal;
- thread/message id;
- próximo passo;
- status.

### `Calendar event`

Evento a criar ou propor.

Campos mínimos:

- título;
- data;
- início/fim;
- local;
- participantes;
- empresa/contexto;
- fonte;
- aprovação/regra usada.

### `Archive/Ignore`

Ruído sem ação.

Não apagar e-mail no MVP. Apenas classificar como ignorável no relatório/estado local.

## 6. Guardrails de aprovação

### Autônomo

- ler e-mails autorizados;
- resumir;
- classificar;
- extrair entidades;
- detectar anexos;
- gerar relatório local;
- criar KB/Brain docs sem PII sensível;
- preparar drafts/previews;
- registrar CRM quando a regra estiver clara e a escrita for de baixo risco.

### Aprovado apenas em subfluxos fechados

- Zipper pós-PDF: resposta cordial usando `condições de pagamento`, nunca `valores`, e follow-up em 2 dias se não houver resposta.

### Sempre aprovação explícita no turno atual

- enviar e-mail externo;
- enviar WhatsApp externo fora de subfluxo fechado;
- responder cliente/fornecedor/artista/coletor/parceiro;
- afirmar preço, disponibilidade, desconto, reserva ou condição nova;
- aprovar pagamento/contrato;
- apagar e-mails/filtros permanentes;
- exportar PII;
- alterar produção/site/infra/banco.

## 7. Regras por empresa

### Zipper

Tom:

- sofisticado;
- cultural;
- leve;
- sem hard sell.

Sinais relevantes:

- artista;
- obra;
- PDF/catálogo;
- colecionador;
- arquiteto;
- feira/ARPA;
- produção/logística;
- proposta e condições de pagamento.

Fonte de verdade:

- Supabase Zipper/CRM para contato/conversa/follow-up;
- `artist_pdfs` para PDFs comerciais;
- Zipper Vendas para venda real;
- Brain Zipper para regras/PRDs.

Regras já aprendidas:

- `ZPR Chatbot` normaliza como `Site - Tidio`;
- sobrenome vem literalmente da resposta “Qual seu sobrenome?”;
- valores já estão no PDF, então pós-envio fala em `condições de pagamento`;
- resposta cordial pós-PDF pode ser automática;
- negociação/reserva/desconto/objeção volta para Lucas.

### SPITI

Tom:

- preciso;
- só afirmar com fonte;
- silêncio é melhor que dado errado.

Sinais relevantes:

- lote;
- lance;
- consignação;
- comprador/vendedor;
- leilão;
- documentação.

Fonte de verdade:

- e-mail/thread operacional;
- Spiti Hub quando aplicável;
- Brain SPITI.

Regra:

- não inferir lance/status de leilão sem fonte verificada.

### LK

Tom:

- premium;
- comercial/analítico;
- nada “barato”.

Sinais relevantes:

- pedido;
- produto/SKU/tamanho;
- cliente;
- financeiro;
- fornecedor;
- agência;
- campanha;
- estoque;
- CRM.

Fonte de verdade:

- Shopify para pedido/venda;
- Tiny para estoque operacional;
- GA4/Meta/Google/Metricool para marketing;
- Brain LK para rotinas e pendências.

Regra:

- enviar campanhas, descontos, contato com cliente/fornecedor e alterações em Shopify/Tiny/Klaviyo sempre exigem aprovação.

### Lucas pessoal/global

Sinais relevantes:

- agenda;
- pessoal;
- multiempresa;
- decisões;
- compromissos;
- documentos;
- pessoas-chave.

Regra:

- classificar antes de salvar;
- se misto, não forçar empresa errada.

## 8. Campos para base estruturada futura

Modelo lógico sugerido para uma futura tabela `email_intake_events`:

```text
id
source_account
provider
message_id
thread_id
received_at
from_masked
to_masked
subject
business_context
classification
urgency
summary
entities_json
attachments_json
recommended_output
approval_required
status
next_action_at
created_at
updated_at
```

Modelo lógico para `email_decision_packets`:

```text
id
email_event_id
business_context
decision_question
recommendation
risk_level
payload_preview
approval_state
approved_by
approved_at
execution_result
created_at
updated_at
```

Modelo lógico para `email_followups`:

```text
id
email_event_id
business_context
channel
condition
scheduled_for
payload_preview
auto_send_allowed
status
last_checked_at
executed_at
```

## 9. Exemplos de interpretação

### Exemplo A — Lead Zipper por encaminhamento

E-mail encaminha contato de arquiteta interessada em artista.

Classificação:

- contexto: Zipper;
- tipo: `lead_comercial`;
- saída: CRM update + draft/Decision Packet;
- aprovação: necessária se for responder externamente.

### Exemplo B — E-mail Tidio/ZPR Chatbot

E-mail ou bloco contém respostas do fluxo Tidio.

Classificação:

- contexto: Zipper;
- origem normalizada: `Site - Tidio`;
- tipo: `lead_comercial`;
- ação: localizar PDF, preparar envio, registrar contato;
- envio: exige aprovação se ainda não estiver dentro de fluxo fechado.

### Exemplo C — Cliente agradece PDF

Cliente responde agradecendo/confirmando recebimento.

Classificação:

- contexto: Zipper;
- tipo: continuidade pós-envio;
- ação automática aprovada: responder curto mencionando condições de pagamento e agendar follow-up em 2 dias;
- bloqueio: se pedir desconto/reserva/disponibilidade, volta para Lucas.

### Exemplo D — Boleto LK

E-mail contém cobrança ou boleto.

Classificação:

- contexto: LK;
- tipo: `financeiro_admin`;
- ação: extrair vencimento/valor/beneficiário e criar Decision Packet;
- aprovação: obrigatória para pagar/aprovar.

### Exemplo E — Lote SPITI

E-mail menciona lance/lote/documentação.

Classificação:

- contexto: SPITI;
- tipo: lead/operacional leilão;
- ação: resumir, verificar fonte, montar decisão;
- regra: não afirmar status sem fonte verificada.

## 10. Calibração inicial da auditoria read-only

Auditoria inicial salva em `areas/operacoes/reports/mordomo-email-intake-readonly-audit-2026-05-18.md`.

Aprendizados de classificação:

- E-mails da Tidio com assunto como `Tidio [N novas mensagens] ...` não devem cair como newsletter/ruído. Devem ser `lead_comercial` ou `operacional_logistica` conforme conteúdo do chat, com origem `Site - Tidio`, porque podem conter leads reais.
- E-mails automáticos de TikTok/Instagram/social dizendo que a Zipper publicou algo são `FYI/marketing_social`, não logística, mesmo quando mencionam exposição/montagem.
- Recibos Meta/Google/ads são `financeiro_admin/marketing_spend`, mas não devem ser roteados para Zipper apenas porque o texto contém palavra artística; confirmar conta/anunciante antes de classificar empresa.
- Newsletters de varejo, Substack, fundos, Serasa, Porto/seguro e similares são `newsletter_ruido` por padrão, mesmo quando contêm palavras como pedido, proposta, conserto ou orçamento.
- E-mail de cliente/WhatsApp encaminhado por equipe Zipper com obra/artista/problema em obra deve ser `lead_comercial` ou `pos_venda_cliente`, não simples FYI.
- E-mail de leilão recebido em conta Zipper pode ser SPITI ou mercado/concorrente; marcar como `desconhecido_misto` se não houver vínculo claro com operação SPITI.

Novas subclasses sugeridas:

- `marketing_social_fyi` — posts/avisos automáticos de redes sociais.
- `marketing_spend_financeiro` — recibos e cobranças de Meta/Google/plataformas.
- `pos_venda_cliente` — cliente relata problema, mofo, dano, troca, reclamação ou pós-venda.

## 11. Rotina de atualização da KB

Atualizar esta base quando:

- Lucas corrigir classificação, tom ou ação;
- novo tipo de e-mail aparecer 2+ vezes;
- uma automação fechada for aprovada;
- uma conta nova for conectada;
- um falso positivo/falso negativo relevante for identificado;
- uma regra de aprovação mudar.

Não salvar:

- senhas;
- tokens;
- refresh tokens;
- PII completa desnecessária;
- dados bancários;
- conteúdo integral de e-mails sensíveis.

## 12. Próximo uso prático

Antes de implementar automação, usar esta KB para auditar e-mails recentes em modo read-only:

1. buscar amostra por conta;
2. classificar com esta taxonomia;
3. gerar relatório mascarado;
4. Lucas corrige os erros;
5. atualizar KB/skill;
6. só depois criar rotina ou automação.
