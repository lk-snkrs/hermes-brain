# PRD — Mordomo Hermes: Triagem e Ação sobre E-mails Recebidos

Atualizado: 2026-05-18
Status: v0.1 — proposta inicial para revisão de Lucas
Base de conhecimento relacionada: `../base-conhecimento/mordomo-email-intake-kb-2026-05-18.md`

## 1. Objetivo

Transformar as caixas de e-mail autorizadas de Lucas em uma entrada operacional do Mordomo Hermes, capaz de ler, classificar, resumir, encaminhar para o contexto correto e preparar ações seguras sem misturar empresas nem disparar comunicações externas sem regra aprovada.

O sistema deve reduzir o esforço de Lucas em três frentes:

1. separar o que importa do ruído;
2. transformar e-mails em tarefas, follow-ups, oportunidades comerciais ou decisões;
3. preparar respostas/ações com contexto, mantendo governança e aprovação humana quando necessário.

## 2. Contas inicialmente no escopo

Contas com acesso técnico já verificado:

- `lucascimino@gmail.com` — pessoal/Lucas global.
- `lucas@zippergaleria.com.br` — Zipper e comunicações diretas do Lucas na galeria.
- `lk@lksneakers.com.br` — operação LK Sneakers.
- `spiti@spiti.auction` — operação SPITI Auction.
- `producao@zippergaleria.com.br` — produção/logística Zipper.

Conta ainda não confirmada:

- `zipper@zippergaleria.com.br` — sem token Gmail válido encontrado no Doppler nesta data.

## 3. Princípio central

O Mordomo lê em uma camada global, mas salva e age por contexto.

Cada e-mail deve ser classificado antes de qualquer ação:

- Lucas pessoal/global;
- LK OS;
- Zipper OS;
- SPITI OS;
- Hermes/Infra;
- desconhecido/misto.

A caixa de entrada é uma fonte de sinais, não uma licença para agir externamente.

## 4. Fontes de verdade por contexto

### Zipper OS

- Gmail: `lucas@zippergaleria.com.br`, `producao@zippergaleria.com.br` e futura `zipper@zippergaleria.com.br` se liberada.
- Supabase CRM/Main: contatos, conversas, logs, follow-ups, PDFs de artistas.
- Zipper Vendas/Supabase para vendas reais quando necessário.
- Brain Zipper para regras, PRDs e decisões.

### SPITI OS

- Gmail: `spiti@spiti.auction` e, quando relevante, `lucas@spiti.auction` se houver acesso.
- Spiti Hub/repo e fontes verificadas de leilão.
- Brain SPITI para decisões e rotinas.

### LK OS

- Gmail: `lk@lksneakers.com.br`.
- Shopify/Tiny/GA4/Meta/Google Ads/Metricool conforme skill LK.
- Brain LK para rotinas, relatórios e pendências.

### Lucas pessoal/global

- Gmail: `lucascimino@gmail.com`.
- Calendários e WhatsApp pessoal quando autorizado.
- Brain global/operacional para decisões e follow-ups multiempresa.

## 5. Tipos de e-mail e comportamento esperado

### 5.1 Lead comercial / interessado

Exemplos:

- cliente pedindo obras de artista;
- indicação de arquiteto/colecionador;
- pedido de informações de produto/obra/leilão;
- lead vindo de Tidio/site, formulário ou encaminhamento interno.

Comportamento:

1. identificar empresa;
2. extrair nome, e-mail, telefone/WhatsApp, artista/produto/lote de interesse, origem e intenção;
3. registrar no CRM correto quando houver confiança suficiente;
4. localizar material validado: PDF de artista, catálogo, link de produto, lote ou resposta padrão;
5. preparar resposta;
6. se for fluxo fechado já aprovado, executar; caso contrário, pedir aprovação no Telegram.

Regra Zipper já aprovada:

- lead `ZPR Chatbot` normaliza origem como `Site - Tidio`;
- PDFs de artistas vêm da tabela `artist_pdfs`;
- pós-resposta cordial ao PDF pode ser automático com linguagem de `condições de pagamento`, não `valores`;
- follow-up em 2 dias se não houver nova resposta;
- negociação, reserva, desconto, objeção ou dúvida específica voltam para Lucas.

### 5.2 Pedido operacional / logística

Exemplos:

- coleta/retirada/entrega de obra;
- produção de exposição;
- fornecedor confirmando horário;
- envio de documento;
- pedido de nota, contrato, pagamento ou agendamento.

Comportamento:

1. extrair data, horário, local, pessoas envolvidas e objeto;
2. classificar empresa;
3. criar pendência ou evento apenas quando escopo estiver claro e aprovado pela regra vigente;
4. se envolver movimentação de obra Zipper, usar calendário `lucas@zippergaleria.com.br` e convidar produção/entregas quando aplicável;
5. nunca prometer prazo, preço, desconto ou compromisso novo sem aprovação.

### 5.3 Financeiro / administrativo

Exemplos:

- boleto, nota fiscal, cobrança, comprovante, pagamento, contrato.

Comportamento:

1. classificar empresa;
2. extrair vencimento, valor, beneficiário, documento e responsável;
3. criar pendência interna;
4. alertar Lucas quando houver vencimento próximo, valor alto, risco ou ambiguidade;
5. nunca pagar, aprovar pagamento, assinar contrato ou enviar dados bancários sem aprovação explícita.

### 5.4 Newsletter, marketing e ruído

Exemplos:

- promoções, plataformas, newsletters, updates genéricos, spam provável.

Comportamento:

1. resumir apenas se houver relevância comercial/estratégica;
2. agrupar por digest quando repetitivo;
3. sugerir unsubscribe/filtro, mas não executar sem aprovação;
4. não criar tarefa para ruído.

### 5.5 Decisões e aprovações

Exemplos:

- alguém aprova orçamento;
- cliente confirma interesse;
- parceiro propõe ação;
- equipe pede decisão de Lucas.

Comportamento:

1. extrair decisão solicitada;
2. montar `Decision Packet` curto para Lucas:
   - contexto;
   - recomendação;
   - risco;
   - ação proposta;
   - payload se houver resposta externa.
3. aguardar aprovação quando envolver ação externa, dinheiro, cliente, fornecedor, campanha, banco de dados ou produção.

## 6. Saídas do sistema

Cada e-mail relevante deve virar uma das saídas abaixo:

- `FYI`: resumo informativo, sem ação.
- `Task`: tarefa interna com dono/contexto/prazo.
- `Follow-up`: lembrete futuro se não houver resposta.
- `Draft`: resposta preparada para aprovação.
- `Auto-reply approved flow`: resposta automática apenas em subfluxo já aprovado.
- `Calendar event`: evento quando dados e regra permitirem.
- `CRM update`: contato/conversa/interesse/follow-up no Supabase correto.
- `Decision Packet`: item para Lucas decidir.
- `Archive/Ignore`: ruído sem valor operacional.

## 7. Autonomia e aprovação

### A0 — leitura e classificação

Autônomo:

- buscar e-mails;
- ler mensagens;
- classificar contexto;
- resumir;
- deduplicar;
- detectar anexos;
- criar relatório local/Brain sem PII sensível.

### A1 — tarefas internas e registros seguros

Autônomo quando claro:

- criar pendência interna;
- registrar CRM com dados necessários;
- registrar follow-up interno;
- atualizar Brain/skill com regra durável sem PII.

### A2 — fluxo fechado aprovado

Autônomo apenas quando a regra já foi explicitamente aprovada por Lucas.

Exemplo atual:

- resposta cordial pós-PDF Zipper com `condições de pagamento` + follow-up em 2 dias.

### A3 — produção/fonte de verdade sensível

Exige preview e, em muitos casos, aprovação:

- alterações em CRM com potencial de impacto comercial;
- calendário com convidados externos;
- mudança de status de negociação;
- arquivamento/filtros automáticos de e-mail;
- marcação como resolvido quando pode ocultar pendência.

### A4 — sempre requer aprovação explícita no turno atual

- enviar e-mail para cliente/fornecedor/parceiro;
- responder WhatsApp externo fora dos subfluxos aprovados;
- enviar proposta, preço, desconto, reserva ou disponibilidade;
- pagar/aprovar financeiro;
- acionar campanha/newsletter;
- alterar produção/site/banco/infra;
- exportar dados pessoais.

## 8. Dados a extrair por e-mail

Campos comuns:

- `source_account` — caixa de e-mail origem.
- `from`, `to`, `cc` — armazenar em fonte segura, não em Brain aberto.
- `subject`.
- `message_id`, `thread_id`.
- `received_at`.
- `business_context`.
- `classification`.
- `urgency`.
- `entities`:
  - pessoas;
  - empresa;
  - artista/produto/lote;
  - telefone/WhatsApp;
  - e-mail;
  - datas;
  - valores;
  - anexos.
- `recommended_action`.
- `approval_required`.
- `next_followup_at`.

## 9. Privacidade e governança

- Brain não deve guardar PII completa quando não necessário.
- PII operacional deve ficar em Supabase/Gmail/WhatsApp autorizados.
- Relatórios abertos usam placeholders ou mascaramento.
- Nunca expor tokens, refresh tokens, senhas, anexos sensíveis ou dados bancários.
- E-mails usados para aprender estilo são exemplos de tom, não autorização de envio.
- Se houver dúvida de empresa/contexto, não misturar: marcar como `unknown/mixed`.

## 10. Inbox do Lucas no Telegram

O resumo diário ou sob demanda deve ser curto e acionável.

Formato sugerido:

```text
E-mails importantes — hoje

1. Zipper — Lead / Adriana Duque
   Origem: Site - Tidio / e-mail encaminhado
   Ação: draft pronto + PDF encontrado
   Precisa: aprovação para envio

2. LK — Financeiro
   Vencimento: amanhã
   Ação: revisar boleto
   Precisa: decisão Lucas

3. SPITI — Operação leilão
   Ação: FYI, sem resposta necessária
```

Para itens que exigem decisão:

```text
Decisão necessária
Contexto: Zipper
Resumo: cliente pediu condições de pagamento de obra X.
Recomendação: responder com condições padrão, sem desconto.
Payload: [texto]
Aprovar? Responda: “Aprovado item 1”
```

## 11. Rotinas propostas

### 11.1 Varredura contínua leve

- Frequência: a definir.
- Função: detectar e-mails urgentes/leads novos.
- Contrato: silencioso se nada relevante.

### 11.2 Digest diário

- Horário sugerido: fim da manhã ou fim do dia.
- Função: agrupar o que precisa de Lucas.
- Saída: Telegram.

### 11.3 Follow-up automático

- Aplicável quando um fluxo aprovado criou um follow-up.
- Antes de enviar, verificar se houve resposta no thread/canal.
- Se houve resposta, não enviar; classificar e reportar se necessário.

## 12. MVP recomendado

### Fase 1 — Read-only triage

Objetivo: ler e classificar e-mails sem enviar nada.

Escopo:

- `lucas@zippergaleria.com.br`
- `lk@lksneakers.com.br`
- `spiti@spiti.auction`
- `lucascimino@gmail.com`

Entregável:

- script read-only de triagem;
- relatório com 20 e-mails recentes por conta;
- classificação por empresa/tipo/urgência;
- falsos positivos identificados.

Critério de conclusão:

- Lucas valida que a classificação está útil e sem misturar empresas.

### Fase 2 — Decision Inbox

Objetivo: transformar e-mails relevantes em itens acionáveis.

Entregável:

- formato de Decision Packet;
- preview de respostas;
- pendências e follow-ups internos;
- zero envio externo.

Critério de conclusão:

- Lucas consegue aprovar/rejeitar itens pelo Telegram com comandos simples.

### Fase 3 — CRM/follow-up por empresa

Objetivo: salvar dados estruturados nos Supabases corretos.

Entregável:

- Zipper: contatos/conversas/followups/artist interest.
- SPITI: contatos/lotes/interesses/leilão quando fonte for clara.
- LK: pedidos, clientes, suporte, financeiro, oportunidades.

Critério de conclusão:

- cada e-mail relevante tem rastro: origem, classificação, ação, status.

### Fase 4 — Automações fechadas

Objetivo: automatizar somente casos aprovados e seguros.

Primeiros candidatos:

- Zipper pós-PDF cordial;
- follow-up se não houve resposta;
- confirmação interna de recebimento de documento;
- digest de ruído/marketing.

Critério de conclusão:

- automação tem regra, rollback, logs e parada fácil.

## 13. Fora do escopo por enquanto

- Responder automaticamente qualquer e-mail genérico.
- Criar campanhas/newsletters.
- Negociar preço, desconto, reserva ou disponibilidade.
- Pagar boletos ou aprovar contratos.
- Apagar e-mails ou aplicar filtros permanentes.
- Usar `zipper@zippergaleria.com.br` até acesso ser confirmado.

## 14. Riscos principais

1. Misturar empresas e responder com contexto errado.
2. Transformar e-mail em envio externo sem aprovação.
3. Salvar PII demais no Brain.
4. Classificar spam/newsletter como oportunidade.
5. Perder urgência operacional escondida em thread longa.
6. Assumir preço/disponibilidade sem fonte validada.

Mitigações:

- roteamento obrigatório por empresa;
- aprovação A4 para externo;
- mascaramento de PII;
- read-only no MVP;
- logging por `message_id`/`thread_id`;
- fonte de verdade por contexto.

## 15. Próximos passos recomendados

1. Lucas aprovar ou corrigir este PRD v0.1.
2. Rodar uma auditoria read-only dos últimos e-mails de cada conta autorizada.
3. Produzir uma amostra de triagem com 10–20 itens reais mascarados.
4. Ajustar classificadores e regras de urgência.
5. Definir quais subfluxos podem ser automáticos e quais ficam sempre approval-gated.
6. Implementar digest/Decision Inbox piloto.

## 16. Decisões pendentes para Lucas

1. O digest deve ser diário, sob demanda ou ambos?
2. Qual horário ideal para digest?
3. Devemos começar por Zipper, LK ou todos read-only em paralelo?
4. Financeiro deve aparecer no mesmo digest ou em bloco separado?
5. Podemos registrar automaticamente contatos/leads claros em Supabase, ou primeiro só preview?
6. Quais labels/pastas do Gmail devem ser ignoradas no MVP?
