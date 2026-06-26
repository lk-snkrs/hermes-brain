# PRD — Zipper OS / Mordomo Zipper orientado por dados

Data: 2026-05-15  
Owner: Lucas Cimino  
Produto: Hermes Agent / Zipper Galeria  
Status: draft v0.2 — remontado após auditoria read-only do Supabase

## 1. Resumo executivo

O **Zipper OS** é a camada operacional da Zipper Galeria dentro do Brain Hermes/Mordomo Hermes. Ele deve conectar comunicação, relacionamento, feiras, conteúdo, logística e vendas reais usando as fontes de verdade já existentes no Supabase da Zipper.

Após auditoria read-only do Supabase, o desenho deixa de ser genérico e passa a se apoiar nos dados reais disponíveis:

- `vendas_tango`: histórico de vendas reais da galeria.
- `contacts`: base de contatos/relacionamento.
- `conversations`: histórico de mensagens WhatsApp/atendimento.
- `secretary_log`: pendências, urgências, respostas sugeridas e follow-ups.
- `followups`: follow-ups já programados/enviados/cancelados.
- `contents`, `content_metrics`, `content_tags`: conteúdo, newsletters/campanhas e desempenho.
- `artists`, `exhibitions`, `exhibition_artists`: artistas, exposições e vínculos curatoriais.
- `templates`, `messages_log`, `automation_logs`, `sync_runs`, `automations`: camada de automação existente.
- Tabelas `spiti_*` no mesmo projeto compartilhado: devem ser tratadas como **SPITI**, não como Zipper Vendas.

O sistema deve preparar decisões e rascunhos melhores, mas preservar a regra central: **Hermes nunca envia e-mail, WhatsApp, proposta ou contato externo sozinho**.

## 2. Contexto da auditoria Supabase

Auditoria criada em:

`areas/zipper/contexto/supabase-readonly-audit.md`

Script usado:

`/opt/data/scripts/zipper_supabase_readonly_audit.py`

Persistência técnica privada:

`/opt/data/state/zipper_supabase_readonly_audit.json`

Escopo:

- Somente leitura via Supabase/PostgREST.
- Credenciais via Doppler `lc-keys/prd`.
- Nenhum valor de secret foi salvo ou impresso.
- O relatório contém estrutura, contagens e exemplos não sensíveis; não contém dados pessoais brutos.

## 3. Decisão de foco

Enquanto este PRD é implementado:

- **LK OS:** standby operacional.
  - Mantém rotinas existentes e alertas críticos.
  - Sem novas frentes grandes até estabilizar Zipper OS.
- **Zipper OS:** prioridade principal.
- **Brain Hermes:** segue como camada global de memória, roteamento e regras A0-A4.

## 4. Problema

A Zipper já tem dados suficientes para operar com inteligência, mas eles estão fragmentados:

- vendas reais estão em `vendas_tango`;
- relacionamento e contatos estão em `contacts`;
- conversas estão em `conversations`;
- pendências aparecem em `secretary_log` e `followups`;
- conteúdo e métricas estão em `contents`, `content_metrics` e `content_tags`;
- artistas e exposições estão em `artists`, `exhibitions` e `exhibition_artists`;
- SPITI/leilão convive no mesmo ambiente compartilhado, gerando risco de confusão;
- e-mail e WhatsApp têm estilo e contexto próprios, mas envio externo precisa continuar bloqueado.

Sem uma camada operacional, Lucas precisa lembrar manualmente o que responder, quem seguir, que obra/artista consultar, que feira ativar e que dado é confiável.

## 5. Objetivos do produto

O Zipper OS deve:

1. Transformar as bases existentes em um painel/rotina operacional para Lucas.
2. Separar Zipper Galeria de SPITI/leilão em toda resposta e consulta.
3. Usar `vendas_tango` como fonte de vendas reais antes de afirmar histórico comercial.
4. Usar `contacts`, `conversations`, `secretary_log` e `followups` para triagem de relacionamento.
5. Usar `contents`, `content_metrics` e `content_tags` para inteligência de comunicação.
6. Usar `artists`, `exhibitions` e `exhibition_artists` para contexto artístico/curatorial.
7. Aprender o estilo de Lucas pelos e-mails enviados/editados, mas apenas para rascunhos.
8. Preparar rascunhos, follow-ups, lembretes e análises com fonte citada.
9. Minimizar exposição de PII em Telegram e documentos.
10. Nunca enviar contato externo sem aprovação explícita de conteúdo + destinatário.

## 6. Não objetivos / fora de escopo V1

O Zipper OS V1 não deve:

- enviar e-mail sozinho;
- enviar WhatsApp sozinho;
- publicar conteúdo sozinho;
- fazer cobrança, proposta, confirmação, preço, prazo, desconto ou reserva sem aprovação;
- escrever em Supabase/CRM como fonte de verdade sem fluxo A3/A4;
- alterar automações existentes;
- usar tabelas SPITI como evidência de vendas reais da Zipper;
- salvar corpo bruto de mensagens/e-mails no Brain;
- expor dados pessoais completos em resumos Telegram.

## 7. Mapa de dados observado

### 7.1 Projeto Zipper Vendas

Host: `pcstqxpdzibheuopjkas.supabase.co`  
Tabela principal: `vendas_tango`  
Linhas estimadas: `2100`

Colunas relevantes:

- Identificação operacional: `id`, `pedido_id`, `acervo_id`.
- Datas: `created_at`, `pedido_data`.
- Origem/canal: `pedido_origem`, `pedido_evento`.
- Cliente/localização: `cliente_id`, `cliente_nome`, `cliente_bairro`, `cliente_cidade`, `cliente_uf`, `cliente_pais`, `email`, `whatsapp`.
- Artista/obra/deal: `artista_nome`, `deal_name`.
- Valor: `valor_obra_final`.

Uso no Zipper OS:

- histórico comercial real;
- ranking por artista;
- vendas por evento/canal/origem;
- ticket médio e total vendido por período;
- suporte para rascunhos comerciais com base em fatos.

Guardrail:

- Contém PII e dados comerciais; resumos devem anonimizar ou reduzir detalhe salvo quando possível.

### 7.2 Projeto Zipper CRM/Main e SPITI compartilhado

Host: `rmdugdkantdydivgnimb.supabase.co`  
Tabelas analisadas: `36`

#### Relacionamento e atendimento

- `contacts` — `1960` contatos.
  - Campos: telefone, nome, interesse em artista, contexto, tags, notas, e-mail, datas.
  - Uso: CRM leve, perfil de contato, histórico de interesse.

- `conversations` — `76056` mensagens.
  - Campos: phone, direction, message, media_type, ack_status, wamid, timestamp.
  - Uso: histórico de conversas e contexto de atendimento.
  - Guardrail: PII/conteúdo sensível; não salvar bruto no Brain.

- `secretary_log` — `78` registros.
  - Campos: chat, contato, última mensagem, urgência, status, resposta sugerida, resposta enviada, follow-up.
  - Uso: backlog atual do Mordomo/secretária; pendências e respostas sugeridas.
  - Observado: status majoritariamente `pending`.

- `followups` — `19` registros.
  - Campos: jid, nome, sent_at, followup_at, status, completed_at.
  - Uso: follow-ups programados/enviados/cancelados.

- `messages_log` — `19` registros.
  - Uso: histórico de mensagens enviadas por automação/campanha; não usar para autorizar envios futuros.

#### Conteúdo e comunicação

- `contents` — `266` itens.
  - Campos: platform, external_id, content_type, url, thumbnail_url, caption, published_at, raw_payload, pulled_at.
  - Observado: inclui campanhas/newsletters MailerLite.

- `content_metrics` — `705` snapshots.
  - Campos: impressions, reach, views, likes, comments, shares, saves, opens, clicks, unsubscribes.
  - Uso: medir performance de conteúdo/newsletters.

- `content_tags` — `313` tags.
  - Campos: content_id, entity_type, entity_id, source, matched_text, confirmed_by.
  - Uso: mapear conteúdo a artista/exposição/entidade.

- `templates` — `3` modelos.
  - Uso: base de mensagens; devem ser tratados como material para rascunho, não envio.

#### Artistas e exposições

- `artists` — `36` artistas.
  - Campos: name, slug, name_variations, hashtags, redes, photo_url, bio, is_roster, active.
  - Uso: roster, bio, variações de nome, ligação com conteúdo.

- `exhibitions` — `20` exposições.
  - Campos: name, slug, start_date, end_date, type, hashtags, description.
  - Uso: calendário/arquivo expositivo, contexto cultural.

- `exhibition_artists` — `14` vínculos.
  - Uso: ligação exposição-artista.

#### Automação e saúde operacional

- `automations` — `6` automações.
- `automation_logs` — `2614` logs.
- `sync_runs` — `42` execuções de sync.
- `authorized_emails` — `4` e-mails autorizados.

Uso:

- observabilidade e diagnóstico;
- não alterar sem aprovação A3/A4.

#### SPITI no projeto compartilhado

Tabelas como `spiti_lotes`, `spiti_vendas`, `spiti_cobrancas`, `spiti_clientes`, `spiti_contacts`, `crm_spiti`, `spiti_parcelas`, `spiti_custos`, `spiti_pagamentos_consignante`, `spiti_todos` existem no mesmo ambiente.

Regra:

- São contexto SPITI/leilão.
- Nunca usar como fonte de vendas reais da Zipper Galeria.
- Podem ajudar quando a tarefa for explicitamente SPITI, mas devem ser roteadas fora do Zipper OS comercial.

## 8. Arquitetura funcional do Zipper OS

### 8.1 Camada de dados

Responsável por consultas read-only e normalização:

- `vendas_tango`: vendas reais.
- `contacts`: contatos/perfis.
- `conversations`: histórico bruto, com minimização.
- `secretary_log` + `followups`: pendências e follow-ups.
- `contents` + `content_metrics` + `content_tags`: inteligência de comunicação.
- `artists` + `exhibitions`: contexto artístico.

### 8.2 Camada de classificação

Classifica cada sinal em:

- Comercial/Vendas.
- Colecionador/Relacionamento.
- Comunicação/Conteúdo.
- Feiras/Eventos.
- Logística de obra.
- Financeiro/RH.
- SPITI/leilão — roteado para SPITI OS.
- Indefinido — pede contexto antes de agir.

### 8.3 Camada de ação segura

Produz apenas:

- resumos;
- análises;
- rascunhos;
- lembretes;
- propostas de agenda;
- checklists;
- recomendações com fonte.

Ações externas ficam bloqueadas até aprovação explícita.

### 8.4 Camada de estilo

Usa:

- `areas/zipper/email-style-profile.md`;
- e-mails enviados/editados por Lucas;
- respostas aprovadas no Telegram;
- feedback de Lucas.

Uso permitido:

- melhorar rascunhos.

Uso proibido:

- enviar sozinho.

## 9. Módulos do produto

### 9.1 Inbox Zipper assistida

Fontes:

- Gmail `lucas@zippergaleria.com.br`.
- `contacts`.
- `conversations`.
- `secretary_log`.
- `followups`.

Funcionalidades:

- listar pendências acionáveis;
- identificar urgência;
- sugerir próximo passo;
- preparar rascunho no tom Zipper;
- salvar draft quando Lucas pedir;
- atualizar perfil de tom após Lucas editar/enviar.

Critérios de aceite:

- toda sugestão vem com fonte;
- nenhuma mensagem externa é enviada;
- PII minimizada nos resumos;
- separa resposta sugerida de fato verificado.

### 9.2 Comercial / Vendas reais

Fonte principal:

- `vendas_tango`.

Funcionalidades:

- total vendido por período;
- vendas por artista;
- vendas por canal/origem/evento;
- ticket médio;
- últimas vendas por artista ou perfil;
- insumo para abordagem de colecionador.

Critérios de aceite:

- qualquer afirmação comercial cita período e fonte;
- não mistura SPITI;
- não expõe cliente completo quando não necessário.

### 9.3 Colecionadores / Relacionamento

Fontes:

- `contacts`;
- `conversations`;
- `secretary_log`;
- `followups`;
- `vendas_tango` quando houver histórico de compra.

Funcionalidades:

- detectar oportunidades de follow-up;
- identificar interesses em artistas;
- sugerir abordagens leves;
- lembrar Lucas antes/depois de feiras;
- aprender formalidade por contato.

Critérios de aceite:

- rascunho sem hard sell;
- não promete preço/obra/reserva;
- envio só após aprovação explícita.

### 9.4 Feiras / Eventos

Fontes:

- `exhibitions`;
- `contents` e `content_tags`;
- conversas/e-mails com menção a ARPA, SP-Arte, ArtRio, Farol Santander;
- calendário Zipper.

Funcionalidades:

- pipeline de pessoas que mencionaram feira;
- rascunhos de convite/reencontro;
- checklist operacional;
- leitura de conteúdo já publicado para reuso.

Critérios de aceite:

- não envia convite sozinho;
- não confirma presença externamente;
- usa tom cultural e elegante.

### 9.5 Comunicação / Conteúdo

Fontes:

- `contents`;
- `content_metrics`;
- `content_tags`;
- `artists`;
- `exhibitions`.

Funcionalidades:

- entender o que performou em newsletter/conteúdo;
- mapear conteúdo por artista/exposição;
- sugerir temas ou reaproveitamentos;
- apoiar briefing para Biz/Helo/Mie.

Critérios de aceite:

- não publicar sozinho;
- não inventar facts artísticos;
- separar métrica real de leitura qualitativa.

### 9.6 Artistas / Exposições

Fontes:

- `artists`;
- `exhibitions`;
- `exhibition_artists`;
- `content_tags`;
- `vendas_tango` para histórico comercial.

Funcionalidades:

- contexto de artista;
- relação com exposições;
- conteúdos associados;
- histórico de vendas quando necessário;
- preparação de rascunhos e briefings.

Critérios de aceite:

- não inferir representação/roster sem campo `is_roster` ou confirmação;
- usar variações de nome para matching;
- citar fonte e data.

### 9.7 Logística de obras

Fontes:

- e-mail/WhatsApp;
- calendário `lucas@zippergaleria.com.br`;
- contexto de conversas.

Funcionalidades:

- extrair data, hora e local;
- identificar coleta/retirada/entrega/movimentação;
- propor/criar evento conforme regra aprovada;
- convidar `producao@zippergaleria.com.br` e `entregas@zippergaleria.com.br` quando aplicável.

Critérios de aceite:

- não assumir local físico por etiqueta “Zipper”;
- se faltar data/hora/local, vira pendência para Lucas;
- não contata motorista/artista/cliente sozinho.

## 10. Matriz de autonomia A0-A4

### A0/A1 — pode executar sem perguntar

- Ler Brain Hermes e arquivos locais.
- Consultar Supabase em modo read-only.
- Consultar Gmail Zipper em read-only para contexto/aprendizado.
- Atualizar relatórios locais agregados sem PII bruta.
- Classificar mensagens/sinais.
- Gerar resumo interno/Telegram com minimização.
- Atualizar perfil de escrita agregado.

### A2 — pode preparar e pedir aprovação

- Rascunho de e-mail/WhatsApp.
- Follow-up de feira.
- Sugestão de abordagem comercial.
- Briefing de conteúdo.
- Proposta de evento quando informação estiver incompleta.
- Relatório comercial baseado em `vendas_tango`.

### A3 — exige plano, rollback e aprovação específica

- Escrever em Supabase, CRM, planilhas oficiais ou automações.
- Alterar labels/estado em Gmail/WhatsApp além de draft solicitado.
- Criar automações recorrentes com escrita.
- Alterar calendário compartilhado em massa.

### A4 — sempre exige aprovação explícita atual

- Enviar e-mail.
- Enviar WhatsApp.
- Contatar colecionador, artista, fornecedor, instituição ou parceiro.
- Confirmar presença/agenda externamente.
- Prometer preço, disponibilidade, reserva, desconto, obra, prazo ou entrega.
- Publicar conteúdo externo.
- Cobrança, pagamento, proposta comercial ou negociação.

## 11. Fluxos principais V1

### 11.1 Briefing diário Zipper

Entrada:

- `secretary_log` pending;
- `followups` pendentes;
- novos e-mails relevantes;
- conversas recentes classificadas como Zipper;
- conteúdo/campanhas recentes se houver mudança relevante.

Saída:

- lista curta para Lucas no Telegram ou relatório local;
- itens agrupados por: urgente, responder, follow-up, logística, feira, comercial, comunicar equipe.

Regras:

- sem corpo bruto extenso;
- sem envio externo;
- cada item com fonte.

### 11.2 Rascunho de resposta a contato

1. Identificar contato e contexto.
2. Verificar histórico em `contacts` e, se necessário, `conversations`.
3. Se envolver obra/venda/artista, consultar `vendas_tango`, `artists` e/ou `exhibitions`.
4. Produzir rascunho curto no tom Lucas/Zipper.
5. Salvar draft apenas se Lucas pedir ou mandar preparar draft.
6. Enviar somente se Lucas aprovar destinatário + texto explicitamente.

### 11.3 Consulta comercial por artista/obra

1. Verificar se é Zipper e não SPITI.
2. Consultar `vendas_tango` por artista/obra/período.
3. Reportar totais, quantidade, ticket médio e ressalvas.
4. Preparar recomendação ou rascunho sem prometer disponibilidade.

### 11.4 Conteúdo e performance

1. Consultar `contents` por período/plataforma.
2. Juntar com `content_metrics`.
3. Usar `content_tags` para artista/exposição quando houver.
4. Sugerir pauta, reuso ou briefing.
5. Não publicar nem disparar campanha.

### 11.5 Feira / ARPA

1. Detectar menção em e-mail/WhatsApp/conversa.
2. Classificar contato e histórico.
3. Preparar follow-up sofisticado e sem hard sell.
4. Sugerir lembrete ou draft.
5. Aguardar aprovação.

### 11.6 Logística de obra

1. Detectar termos: retirada, coleta, entrega, movimentação, acervo, ateliê.
2. Extrair data, hora, local e participantes.
3. Se completo e dentro do escopo aprovado, criar/propor evento no calendário Zipper.
4. Incluir produção/entregas quando for movimentação de obra.
5. Se incompleto, criar pendência para Lucas.

## 12. Privacidade e governança

- Não salvar corpo bruto de e-mails/WhatsApps no Brain.
- Relatórios devem reduzir PII.
- Secrets via Doppler, nunca impressos.
- Supabase V1 é read-only por padrão.
- Toda resposta com dado deve dizer fonte e período quando aplicável.
- SPITI é separado por roteamento; Zipper Vendas é `vendas_tango`.
- Envio externo só com aprovação explícita no Telegram com conteúdo e destinatário.

## 13. Métricas de sucesso

### Segurança

- 0 envios externos sem aprovação.
- 0 confusões Zipper vs SPITI.
- 0 secrets ou PII bruta em relatórios.
- 0 escritas em Supabase sem aprovação A3/A4.

### Operação

- Redução de pendências `secretary_log` pending.
- Follow-ups rastreados sem esquecimento.
- Mais respostas prontas em draft.
- Menos tempo para responder demandas Zipper.

### Comercial

- Toda afirmação comercial baseada em `vendas_tango`.
- Relatórios por artista/canal/período disponíveis sob demanda.
- Follow-ups de feira mais consistentes.

### Comunicação

- Conteúdo avaliado por performance real.
- Briefings mais conectados a artistas/exposições.
- Rascunhos cada vez mais próximos ao estilo do Lucas.

## 14. MVP remontado após Supabase

### Fase 1 — Fundação de dados e PRD

Status: iniciada.

- Auditoria read-only Supabase concluída.
- PRD remontado com mapa real de tabelas.
- Perfil de escrita de e-mail Zipper iniciado.
- Regra draft-only reforçada.

### Fase 2 — Briefing diário Zipper read-only

Construir rotina que leia:

- `secretary_log` pending;
- `followups` não concluídos;
- `contacts` alterados recentemente;
- e-mails Zipper relevantes;
- eventos/logística quando detectável.

Saída:

- resumo Telegram curto ou local;
- nenhum envio externo.

### Fase 3 — Comercial `vendas_tango`

Construir consultas seguras:

- vendas por artista;
- vendas por período;
- vendas por origem/evento;
- ticket médio;
- top artistas/canais;
- base para rascunhos comerciais.

### Fase 4 — Inbox + drafts

Construir assistente que:

- identifica e-mails acionáveis;
- cruza contato/histórico;
- prepara draft;
- deduplica drafts já criados;
- nunca envia.

### Fase 5 — Conteúdo e feiras

Construir inteligência sobre:

- conteúdos publicados;
- métricas de newsletter/social;
- tags por artista/exposição;
- oportunidades ARPA/SP-Arte/ArtRio;
- rascunhos de follow-up.

### Fase 6 — Escrita controlada opcional

Só após aprovação específica:

- registrar decisões em CRM;
- marcar pendência como resolvida;
- atualizar follow-up;
- nunca contato externo automático.

## 15. Backlog inicial priorizado

### P0 — Segurança e roteamento

- Criar helper read-only canônico para Supabase Zipper.
- Validar separação Zipper Vendas vs SPITI em toda consulta.
- Criar política de minimização de PII nos outputs.

### P1 — Briefing operacional

- Ler `secretary_log` pending.
- Ler `followups` pendentes.
- Agrupar por urgência/status.
- Gerar resumo diário Zipper.

### P1 — Comercial real

- Query por artista em `vendas_tango`.
- Query por período/origem/evento.
- Relatório compacto para decisão.

### P2 — Inbox assistida

- Cruzar e-mail com contato/histórico.
- Gerar draft seguro.
- Aprender após edição/envio do Lucas.

### P2 — Comunicação

- Relatório de conteúdo e métricas.
- Tags por artista/exposição.
- Sugestões de pauta.

### P3 — Escrita em sistemas

- Atualizar status de pendência.
- Registrar follow-up aprovado.
- Criar visão operacional futura.

## 16. Questões abertas para Lucas

1. O briefing Zipper deve chegar no Telegram todo dia ou só quando houver pendência relevante?
2. Você quer que eu priorize primeiro `secretary_log`/followups ou `vendas_tango` comercial?
3. O Zipper OS deve considerar `contacts.tags = lk` como contaminação a limpar/ignorar, ou há razão operacional para tags misturadas?
4. Quem pode aprovar ações externas além de você: Osmar, Biz, Panda ou ninguém nesta fase?
5. Podemos criar uma rotina read-only diária do Supabase Zipper, ou prefere rodar sob demanda no começo?

## 17. Próximo passo recomendado

Começar por **Briefing diário Zipper read-only** porque os dados já mostram um backlog operacional claro:

- `secretary_log`: 78 registros, quase todos `pending`.
- `followups`: 19 registros.
- `conversations`: 76k mensagens, mas precisa minimização e classificação.
- `contacts`: 1.960 contatos.

Depois, construir o módulo **Comercial `vendas_tango`**, que dá base objetiva para qualquer resposta sobre artista, obra, origem e histórico de venda.
