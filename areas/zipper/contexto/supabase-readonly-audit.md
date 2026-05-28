# Zipper Supabase — Auditoria Read-only para PRD

Atualizado: 2026-05-27T23:32:03.499881+00:00

## Escopo e segurança

- Ação executada: leitura read-only via Supabase/PostgREST.
- Credenciais: Doppler `lc-keys/prd`; nenhum valor de secret foi salvo ou impresso.
- Persistência: este relatório contém estrutura, contagens e exemplos não sensíveis. Não contém corpo bruto de mensagens nem dados pessoais brutos.
- Uso: remonte do PRD do Zipper OS com base no que existe de fato na base.

## Projetos auditados

### Zipper Vendas

- Host: `pcstqxpdzibheuopjkas.supabase.co`
- Status: `ok`
- OpenAPI/status: `401`
- Tabelas/recursos analisados: 1

#### `vendas_tango`

- Linhas estimadas: `2108` (status 206, sample 206)
- Colunas detectadas (18): `id, created_at, pedido_id, pedido_data, pedido_origem, pedido_evento, cliente_id, cliente_nome, cliente_bairro, cliente_cidade, cliente_uf, cliente_pais, artista_nome, valor_obra_final, acervo_id, deal_name, email, whatsapp`

- money: `valor_obra_final`
- dates: `created_at, pedido_data`
- sensitive_or_identity: `cliente_id, cliente_nome, cliente_bairro, cliente_cidade, cliente_uf, cliente_pais, artista_nome, deal_name, email`
- other: `id, pedido_id, pedido_origem, pedido_evento, acervo_id, whatsapp`
- Exemplos não sensíveis de formato:
  - `id`: `1422`
  - `created_at`: `2025-08-15T14:19:07.339588+00:00`
  - `pedido_id`: `23923`
  - `pedido_data`: `2023-11-25`
  - `pedido_origem`: `Arquiteto`
  - `pedido_evento`: `Acervo`
  - `valor_obra_final`: `76500`
  - `acervo_id`: `10534`
  - `whatsapp`: `5511`
- Distribuições categóricas amostradas:
  - `pedido_origem`: 

### Zipper CRM/Main

- Host: `rmdugdkantdydivgnimb.supabase.co`
- Status: `ok`
- OpenAPI/status: `200`
- Tabelas/recursos analisados: 36

#### `artist_pdfs`

- Linhas estimadas: `13` (status 200, sample 206)
- Colunas detectadas (6): `id, artist_name, pdf_filename, pdf_base64, created_at, updated_at`

- dates: `created_at, updated_at`
- sensitive_or_identity: `artist_name, pdf_filename`
- other: `id, pdf_base64`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `pdf_base64`: `JVBERi0xLjYNJeLjz9MNCjQ1MCAwIG9iag08PC9GaWx0ZXIvRmxhdGVEZWNvZGUvRmlyc3QgMTQvT...`
  - `created_at`: `2026-05-18T15:45:02.987758+00:00`
  - `updated_at`: `2026-05-18T15:45:02.987758+00:00`

#### `scheduled_sends`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `contacts`

- Linhas estimadas: `1961` (status 206, sample 206)
- Colunas detectadas (12): `id, phone, first_name, last_name, artist_interest, context, tags, notes, pdf_count, email, created_at, updated_at`

- dates: `created_at, updated_at`
- sensitive_or_identity: `phone, first_name, last_name, notes, email`
- other: `id, artist_interest, context, tags, pdf_count`
- Exemplos não sensíveis de formato:
  - `id`: `1854`
  - `artist_interest`: ``
  - `context`: `WhatsApp Pessoal — 19/03/2026`
  - `tags`: `lk`
  - `pdf_count`: `0`
  - `created_at`: `2026-03-19T16:51:59.363707+00:00`
  - `updated_at`: `2026-03-19T16:51:59.363707+00:00`

#### `editorial_notes`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `secretary_log`

- Linhas estimadas: `78` (status 200, sample 206)
- Colunas detectadas (16): `id, created_at, chat_jid, contact_name, last_message, last_message_at, urgency, status, suggested_reply, sent_reply, alerted_at, follow_up_scheduled_at, follow_up_sent_at, artist_detected, is_group, group_name`

- dates: `created_at`
- sensitive_or_identity: `contact_name, last_message, last_message_at, group_name`
- other: `id, chat_jid, urgency, status, suggested_reply, sent_reply, alerted_at, follow_up_scheduled_at, follow_up_sent_at, artist_detected, is_group`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `created_at`: `2026-04-02T14:22:03.676412+00:00`
  - `chat_jid`: `followup_5511981861865@s.whatsapp.net`
  - `urgency`: `normal`
  - `status`: `pending`
  - `suggested_reply`: `Oi 5511981861865, tudo bem? Passando para ver se você conseguiu dar uma olhad...`
  - `alerted_at`: `2026-04-02T14:22:03.627046+00:00`
  - `is_group`: `False`
- Distribuições categóricas amostradas:
  - `status`: pending=77, ignored=1

#### `automation_logs`

- Linhas estimadas: `2614` (status 206, sample 206)
- Colunas detectadas (6): `id, automation_id, status, message, details, executed_at`

- sensitive_or_identity: `message`
- other: `id, automation_id, status, details, executed_at`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `automation_id`: `2`
  - `status`: `success`
  - `executed_at`: `2026-03-11T12:00:17.293+00:00`
  - `details`: `{'pos': {'total': 16499.96, 'orders': 5}, 'web': {'total': 4965.08, 'orders':...`
- Distribuições categóricas amostradas:
  - `status`: 

#### `contents`

- Linhas estimadas: `268` (status 200, sample 206)
- Colunas detectadas (10): `id, platform, external_id, content_type, url, thumbnail_url, caption, published_at, raw_payload, pulled_at`

- other: `id, platform, external_id, content_type, url, thumbnail_url, caption, published_at, raw_payload, pulled_at`
- Exemplos não sensíveis de formato:
  - `id`: `314df701-aef1-4b31-9e97-3a27de251755`
  - `platform`: `mailerlite`
  - `external_id`: `168167512249206689`
  - `content_type`: `newsletter_campaign`
  - `caption`: `Flávia: 4 projetos
Flávia Junqueira em 4 novos projetos`
  - `published_at`: `2025-10-13T21:07:22+00:00`
  - `raw_payload`: `{'id': '168167512249206689', 'can': {'copy': True, 'send': True, 'delete': Tr...`
  - `pulled_at`: `2026-05-27T03:06:05.822+00:00`

#### `spiti_recebimentos`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `exhibitions`

- Linhas estimadas: `20` (status 200, sample 206)
- Colunas detectadas (10): `id, name, slug, start_date, end_date, type, hashtags, description, created_at, updated_at`

- dates: `start_date, end_date, created_at, updated_at`
- sensitive_or_identity: `name`
- other: `id, slug, type, hashtags, description`
- Exemplos não sensíveis de formato:
  - `id`: `4de65622-d053-43b3-9ae4-c68d16789c20`
  - `slug`: `acorda-2026-03`
  - `start_date`: `2026-03-21`
  - `end_date`: `2026-04-30`
  - `type`: `expo`
  - `hashtags`: `[]`
  - `created_at`: `2026-04-29T14:49:48.154556+00:00`
  - `updated_at`: `2026-04-29T14:49:48.154556+00:00`

#### `spiti_contacts`

- Linhas estimadas: `507` (status 200, sample 206)
- Colunas detectadas (12): `id, tipo, email, nome, whatsapp, telefone, timestamp_original, status, fonte, notas, data_criacao, data_atualizacao`

- dates: `timestamp_original, data_criacao, data_atualizacao`
- sensitive_or_identity: `email, nome, telefone`
- other: `id, tipo, whatsapp, status, fonte, notas`
- Exemplos não sensíveis de formato:
  - `id`: `2`
  - `tipo`: `comprador`
  - `status`: `respondido`
  - `fonte`: `compradores-confirmados.csv`
  - `data_criacao`: `2026-03-17T11:24:06.201236`
  - `data_atualizacao`: `2026-03-17T11:24:06.201236`
- Distribuições categóricas amostradas:
  - `tipo`: comprador=441, lead_whatsapp=43, collector=21, teste_service=1, teste=1
  - `status`: respondido=505, novo=2

#### `content_metrics`

- Linhas estimadas: `831` (status 200, sample 206)
- Colunas detectadas (14): `id, content_id, snapshot_date, impressions, reach, views, likes, comments, shares, saves, opens, clicks, unsubscribes, raw`

- dates: `snapshot_date`
- other: `id, content_id, impressions, reach, views, likes, comments, shares, saves, opens, clicks, unsubscribes, raw`
- Exemplos não sensíveis de formato:
  - `id`: `d77b2c55-c91b-44d9-9ca7-dccd197d0cb7`
  - `content_id`: `5f9f1e4f-b0f7-40e8-b442-0972e21f11af`
  - `snapshot_date`: `2026-04-30`
  - `opens`: `7794`
  - `clicks`: `115`
  - `unsubscribes`: `18`
  - `raw`: `{'sent': 22299, 'open_rate': {'float': 0.34952240010763, 'string': '34.95%'},...`

#### `followups`

- Linhas estimadas: `20` (status 200, sample 206)
- Colunas detectadas (8): `id, jid, nome, sent_at, followup_at, status, completed_at, created_at`

- dates: `created_at`
- sensitive_or_identity: `nome`
- other: `id, jid, sent_at, followup_at, status, completed_at`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `jid`: `31611593450@c.us`
  - `sent_at`: `2026-02-24T13:31:53.053+00:00`
  - `followup_at`: `2026-02-27T13:31:53.053+00:00`
  - `status`: `sent`
  - `completed_at`: `2026-02-27T13:31:53.65+00:00`
  - `created_at`: `2026-02-24T13:31:53.108289+00:00`
- Distribuições categóricas amostradas:
  - `status`: sent=16, cancelled=3, pending=1

#### `exhibition_artists`

- Linhas estimadas: `14` (status 200, sample 206)
- Colunas detectadas (2): `exhibition_id, artist_id`

- other: `exhibition_id, artist_id`
- Exemplos não sensíveis de formato:
  - `exhibition_id`: `4de65622-d053-43b3-9ae4-c68d16789c20`
  - `artist_id`: `5556e3a5-6e9a-4e62-9197-a90d9bd16e27`

#### `spiti_lotes_financeiro`

- Linhas estimadas: `252` (status 200, sample 206)
- Colunas detectadas (8): `id, leilao_id, lote, artista, consignante, captacao, valor_base, comissao_consignante_pct`

- money: `valor_base`
- other: `id, leilao_id, lote, artista, consignante, captacao, comissao_consignante_pct`
- Exemplos não sensíveis de formato:
  - `id`: `218`
  - `leilao_id`: `spiti9`
  - `lote`: `1`
  - `artista`: `Antônio Poteiro`
  - `consignante`: `Alysson Rodrigues`
  - `captacao`: `Alysson Rodrigues`
  - `valor_base`: `3500.0`
  - `comissao_consignante_pct`: `10.0`
- Distribuições categóricas amostradas:
  - `artista`: Emiliano Di Cavalcanti=9, Assume Vivid Astro Focus (AVAF)=6, Alfredo Volpi=5, Eric Doeringer=5, Chico da Silva=4, Jandyra Waters=4, Manabu Mabe=4, Antônio Poteiro=3, Emmanuel Nassar=3, Arthur Luiz Piza=3

#### `templates`

- Linhas estimadas: `3` (status 200, sample 200)
- Colunas detectadas (5): `id, name, body, created_at, updated_at`

- dates: `created_at, updated_at`
- sensitive_or_identity: `name`
- other: `id, body`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `body`: `[{"type":"text","content":"Olá {nome}, tudo bem?\n\nFico feliz com seu contat...`
  - `created_at`: `2026-02-20T19:11:48.477+00:00`
  - `updated_at`: `2026-02-20T19:11:48.478+00:00`

#### `spiti_vendas`

- Linhas estimadas: `151` (status 200, sample 206)
- Colunas detectadas (21): `id, leilao_id, lote, artista, titulo, comprador_nome, comprador_cartela, comprador_id, valor_arremate, forma_pagamento, status_pagamento, valor_pago, data_venda, origem, notas, criado_em, atualizado_em, lancado, data_lancamento, num_parcelas, comissao_comprador_pct`

- money: `valor_arremate, valor_pago, data_venda`
- dates: `data_lancamento`
- sensitive_or_identity: `comprador_nome`
- other: `id, leilao_id, lote, artista, titulo, comprador_cartela, comprador_id, forma_pagamento, status_pagamento, origem, notas, criado_em, atualizado_em, lancado, num_parcelas, comissao_comprador_pct`
- Exemplos não sensíveis de formato:
  - `id`: `345`
  - `leilao_id`: `spiti9`
  - `lote`: `76`
  - `artista`: `Ana Maria Tavares`
  - `valor_arremate`: `95000.0`
  - `status_pagamento`: `pendente`
  - `valor_pago`: `0.0`
  - `data_venda`: `2026-04-27`
  - `origem`: `pos-leilao`
  - `notas`: ``
  - `criado_em`: `2026-04-27T21:37:09.615502+00:00`
  - `atualizado_em`: `2026-04-27T21:37:09.615502+00:00`
  - `lancado`: `True`
  - `num_parcelas`: `1`
  - `comissao_comprador_pct`: `0`
  - `comprador_id`: `15`
- Distribuições categóricas amostradas:
  - `artista`: Emiliano Di Cavalcanti=7, Alfredo Volpi=5, Emanoel Araujo=3, Yutaka Toyota=3, Tomie Ohtake=3, Antônio Dias=3, Manabu Mabe=3, Paulo Pasta=3, Wega Nery=3, Ana Maria Tavares=2
  - `forma_pagamento`: 
  - `origem`: leiloesbr=137, pos-leilao=14

#### `spiti_pagamentos_consignante`

- Linhas estimadas: `9` (status 200, sample 206)
- Colunas detectadas (13): `id, leilao_id, consignante_nome, lotes_vendidos, valor_total_arremate, total_comissao, valor_a_pagar, valor_pago, status, forma_pagamento, data_pagamento, notas, criado_em`

- money: `valor_total_arremate, total_comissao, valor_a_pagar, valor_pago`
- dates: `data_pagamento`
- sensitive_or_identity: `consignante_nome`
- other: `id, leilao_id, lotes_vendidos, status, forma_pagamento, notas, criado_em`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `leilao_id`: `spiti9`
  - `lotes_vendidos`: `[85]`
  - `valor_total_arremate`: `29000.0`
  - `total_comissao`: `5800.0`
  - `valor_a_pagar`: `23200.0`
  - `valor_pago`: `23200.0`
  - `status`: `pago`
  - `forma_pagamento`: `PIX`
  - `data_pagamento`: `2026-04-13`
  - `notas`: `2026-04-13: R$ 23.200 PIX`
  - `criado_em`: `2026-04-13T18:03:47.200797+00:00`
- Distribuições categóricas amostradas:
  - `status`: pago=8, parcial=1
  - `forma_pagamento`: PIX=9

#### `products`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `crm_spiti`

- Linhas estimadas: `452` (status 200, sample 206)
- Colunas detectadas (14): `id, tipo, email, nome, whatsapp, telefone, timestamp_original, status, fonte, cliente_bairro, cliente_cidade, cliente_uf, data_criacao, data_atualizacao`

- dates: `timestamp_original, data_criacao, data_atualizacao`
- sensitive_or_identity: `email, nome, telefone, cliente_bairro, cliente_cidade, cliente_uf`
- other: `id, tipo, whatsapp, status, fonte`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `tipo`: `comprador`
  - `status`: `ativo`
  - `fonte`: `compradores-confirmados.csv`
  - `data_criacao`: `2026-03-17T11:49:10.267249`
  - `data_atualizacao`: `2026-03-17T11:49:10.267249`
- Distribuições categóricas amostradas:
  - `tipo`: comprador=441, prospect=8, lead_whatsapp=3
  - `status`: ativo=441, catalogo_enviado=8, respondido=3

#### `spiti_custos`

- Linhas estimadas: `54` (status 200, sample 206)
- Colunas detectadas (9): `id, leilao_id, categoria, descricao, valor, data, pago, notas, criado_em`

- money: `valor`
- dates: `data`
- other: `id, leilao_id, categoria, descricao, pago, notas, criado_em`
- Exemplos não sensíveis de formato:
  - `id`: `70`
  - `leilao_id`: `spiti9`
  - `categoria`: `Marketing`
  - `descricao`: `Facebook`
  - `valor`: `2.29`
  - `data`: `2026-04-24`
  - `pago`: `True`
  - `notas`: ``
  - `criado_em`: `2026-04-24T13:29:01.493239+00:00`
- Distribuições categóricas amostradas:
  - `categoria`: Produção=11, Marketing=8, Alimentação=7, Freelance=6, Geral=5, Estrutura=5, Reembolso=4, Outros=3, Comissão=3, Segurança=2

#### `spiti_clientes`

- Linhas estimadas: `94` (status 200, sample 206)
- Colunas detectadas (10): `id, leilao_id, nome, cpf, endereco, email, telefone, cartela, notas, created_at`

- dates: `created_at`
- sensitive_or_identity: `nome, cpf, endereco, email, telefone`
- other: `id, leilao_id, cartela, notas`
- Exemplos não sensíveis de formato:
  - `id`: `10`
  - `leilao_id`: `spiti9`
  - `created_at`: `2026-04-16T09:51:45.328259+00:00`

#### `spiti_lotes`

- Linhas estimadas: `251` (status 200, sample 206)
- Colunas detectadas (16): `id, lote_id, artista, titulo, descricao, tecnica, dimensoes, ano, lance_atual, proximo_lance, status, img_url, url, data_pregao, criado_em, atualizado_em`

- dates: `data_pregao`
- other: `id, lote_id, artista, titulo, descricao, tecnica, dimensoes, ano, lance_atual, proximo_lance, status, img_url, url, criado_em, atualizado_em`
- Exemplos não sensíveis de formato:
  - `id`: `23`
  - `lote_id`: `29723823`
  - `artista`: `Wega Nery`
  - `titulo`: `Futuro sonhado`
  - `descricao`: `Lote 117`
  - `tecnica`: `Ãleo sobre tela`
  - `dimensoes`: `92 x 64 cm`
  - `ano`: `1990`
  - `lance_atual`: `9000.0`
  - `proximo_lance`: `9500`
  - `status`: `com_lance`
  - `img_url`: `https://d1o6h00a1h5k7q.cloudfront.net/imagens/img_m/60396/29723823.jpg`
  - `url`: `https://www.spiti.art/peca.asp?ID=29723823`
  - `data_pregao`: `01/04/2026`
  - `criado_em`: `2026-03-20T20:52:08.327802`
  - `atualizado_em`: `2026-04-01T01:50:11.148718`
- Distribuições categóricas amostradas:
  - `artista`: Emiliano Di Cavalcanti=9, Assume Vivid Astro Focus (AVAF)=6, Alfredo Volpi=5, Eric Doeringer=5, Emanoel Araujo=5, Mira Schendel=4, Chico da Silva=4, Jandyra Waters=4, Manabu Mabe=4, Wega Nery=3
  - `ano`: s/d=45, 1986=7, 2011=7, 1970=6, 1987=6, 1996=6, 1988=5, 1967=5, 2007=5, 1985=5
  - `status`: com_lance=142, sem_lance=109

#### `product_contacts`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `messages_log`

- Linhas estimadas: `24` (status 200, sample 206)
- Colunas detectadas (5): `id, phone, message, template_used, sent_at`

- sensitive_or_identity: `phone, message`
- other: `id, template_used, sent_at`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `template_used`: `bulk`
  - `sent_at`: `2026-02-16T01:58:54.627+00:00`

#### `spiti_parcelas`

- Linhas estimadas: `148` (status 200, sample 206)
- Colunas detectadas (10): `id, cobranca_id, numero, valor, forma_pagamento, data_vencimento, data_pagamento, status, notas, criado_em`

- money: `valor`
- dates: `data_vencimento, data_pagamento`
- other: `id, cobranca_id, numero, forma_pagamento, status, notas, criado_em`
- Exemplos não sensíveis de formato:
  - `id`: `80`
  - `cobranca_id`: `79`
  - `numero`: `1`
  - `valor`: `19800.0`
  - `forma_pagamento`: `DINHEIRO`
  - `data_vencimento`: `2026-04-02`
  - `data_pagamento`: `2026-04-02`
  - `status`: `pago`
  - `criado_em`: `2026-04-02T17:41:53.006962+00:00`
- Distribuições categóricas amostradas:
  - `forma_pagamento`: PIX=142, DINHEIRO=5, CHEQUE=1
  - `status`: pago=129, pendente=19

#### `spiti_todos`

- Linhas estimadas: `1` (status 200, sample 200)
- Colunas detectadas (17): `id, leilao_id, titulo, descricao, status, prioridade, responsavel_nome, responsavel_area, origem, referencias, checklist, created_at, updated_at, done_at, created_by, updated_by, responsavel_email`

- dates: `created_at, updated_at, created_by, updated_by`
- sensitive_or_identity: `responsavel_nome, responsavel_email`
- other: `id, leilao_id, titulo, descricao, status, prioridade, responsavel_area, origem, referencias, checklist, done_at`
- Exemplos não sensíveis de formato:
  - `id`: `spiti9-reconciliacao-lotes-27-91-consignantes`
  - `leilao_id`: `spiti9`
  - `titulo`: `Reconciliar lotes 27/91 e grade de pagamentos a consignantes — SPITI 9`
  - `descricao`: `Confirmar o split do residual de R$ 40.000 entre os lotes 27 e 91, corrigir/c...`
  - `status`: `pending`
  - `prioridade`: `alta`
  - `responsavel_area`: `Produtora SPITI`
  - `origem`: `Cobrança 113 / PRD Claw`
  - `referencias`: `{'prd': 'empresa/prds/2026-04-28-spiti-financial-reconciliacao-lotes-consigna...`
  - `checklist`: `[{'done': False, 'label': 'Revisar cobrança 113 na origem operacional/finance...`
  - `created_at`: `2026-04-28T22:22:00+00:00`
  - `updated_at`: `2026-04-28T23:37:07.900328+00:00`
- Distribuições categóricas amostradas:
  - `status`: pending=1
  - `origem`: Cobrança 113 / PRD Claw=1

#### `automations`

- Linhas estimadas: `6` (status 200, sample 206)
- Colunas detectadas (7): `id, type, name, config, enabled, created_at, updated_at`

- dates: `created_at, updated_at`
- sensitive_or_identity: `name`
- other: `id, type, config, enabled`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `type`: `google_calendar_daily`
  - `config`: `{'timezone': 'America/Sao_Paulo', 'calendar_id': 'primary', 'notify_time': '0...`
  - `enabled`: `False`
  - `created_at`: `2026-03-11T00:41:29.26839+00:00`
  - `updated_at`: `2026-03-11T00:41:29.26839+00:00`

#### `sync_runs`

- Linhas estimadas: `50` (status 200, sample 206)
- Colunas detectadas (10): `id, source, started_at, finished_at, items_seen, items_new, items_tagged, status, error_message, notes`

- sensitive_or_identity: `error_message, notes`
- other: `id, source, started_at, finished_at, items_seen, items_new, items_tagged, status`
- Exemplos não sensíveis de formato:
  - `id`: `baeb8544-11b3-4299-90eb-c633b775a8c1`
  - `source`: `api:mailerlite`
  - `started_at`: `2026-04-30T13:10:30.799402+00:00`
  - `finished_at`: `2026-04-30T13:10:58.991+00:00`
  - `items_seen`: `29`
  - `items_new`: `29`
  - `items_tagged`: `9`
  - `status`: `success`
- Distribuições categóricas amostradas:
  - `status`: success=50

#### `artists`

- Linhas estimadas: `36` (status 200, sample 206)
- Colunas detectadas (14): `id, name, slug, name_variations, hashtags, instagram_handle, tiktok_handle, youtube_channel_id, photo_url, bio, is_roster, active, created_at, updated_at`

- dates: `created_at, updated_at`
- sensitive_or_identity: `name, name_variations`
- other: `id, slug, hashtags, instagram_handle, tiktok_handle, youtube_channel_id, photo_url, bio, is_roster, active`
- Exemplos não sensíveis de formato:
  - `id`: `2cd426de-d617-4982-bc80-7c61d05cdb42`
  - `slug`: `adriana-duque`
  - `hashtags`: `[]`
  - `is_roster`: `True`
  - `active`: `True`
  - `created_at`: `2026-04-29T14:49:46.837837+00:00`
  - `updated_at`: `2026-04-30T13:43:40.995638+00:00`

#### `spiti_rsvp`

- Linhas estimadas: `7` (status 200, sample 206)
- Colunas detectadas (8): `id, nome, email, whatsapp, cpf, confirmed_at, notified_wpp, notified_email`

- sensitive_or_identity: `nome, email, cpf, notified_email`
- other: `id, whatsapp, confirmed_at, notified_wpp`
- Exemplos não sensíveis de formato:
  - `id`: `2`
  - `whatsapp`: `(55) 11991-2033`
  - `confirmed_at`: `2026-03-30T17:53:19.72+00:00`
  - `notified_wpp`: `True`

#### `spiti_parcelas_pagamento`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `content_tags`

- Linhas estimadas: `315` (status 200, sample 206)
- Colunas detectadas (9): `id, content_id, entity_type, entity_id, source, matched_text, confirmed_by, confirmed_at, created_at`

- dates: `created_at`
- other: `id, content_id, entity_type, entity_id, source, matched_text, confirmed_by, confirmed_at`
- Exemplos não sensíveis de formato:
  - `id`: `e4292e51-d0d2-43cf-843a-7b68765752df`
  - `content_id`: `828b9064-cceb-4cda-b5a9-4fd57900e9cb`
  - `entity_type`: `exhibition`
  - `entity_id`: `ffe9b130-5dbe-4347-915a-9a22d6a0aaf1`
  - `source`: `auto`
  - `matched_text`: `SP-Arte`
  - `created_at`: `2026-04-30T15:13:07.070464+00:00`

#### `sent_contacts`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `spiti_cobrancas`

- Linhas estimadas: `108` (status 200, sample 206)
- Colunas detectadas (16): `id, leilao_id, comprador_nome, comprador_id, lotes, valor_arremate_total, comissao_total, valor_total, forma_pagamento, num_parcelas, valor_pago, status, lancado, lancado_em, notas, criado_em`

- money: `valor_arremate_total, comissao_total, valor_total, valor_pago`
- sensitive_or_identity: `comprador_nome`
- other: `id, leilao_id, comprador_id, lotes, forma_pagamento, num_parcelas, status, lancado, lancado_em, notas, criado_em`
- Exemplos não sensíveis de formato:
  - `id`: `79`
  - `leilao_id`: `spiti9`
  - `lotes`: `[16, 28]`
  - `valor_arremate_total`: `18000.0`
  - `comissao_total`: `1800.0`
  - `valor_total`: `19800.0`
  - `forma_pagamento`: `DINHEIRO`
  - `num_parcelas`: `1`
  - `valor_pago`: `19800.0`
  - `status`: `pago`
  - `lancado`: `True`
  - `lancado_em`: `2026-04-02T17:41:52.501+00:00`
  - `notas`: ``
  - `criado_em`: `2026-04-02T17:41:52.750226+00:00`
- Distribuições categóricas amostradas:
  - `forma_pagamento`: PIX=81, PIX, PIX=11, PIX, PIX, PIX=7, PIX, PIX, PIX, PIX=3, DINHEIRO=2, DINHEIRO, PIX=1, PIX, CHEQUE=1, PIX, DINHEIRO, PIX, PIX=1, PIX, DINHEIRO=1
  - `status`: pago=96, parcial=12

#### `authorized_emails`

- Linhas estimadas: `4` (status 200, sample 200)
- Colunas detectadas (4): `id, email, added_by, added_at`

- sensitive_or_identity: `email`
- other: `id, added_by, added_at`
- Exemplos não sensíveis de formato:
  - `id`: `dae89d03-cd62-435f-8124-1a2ac5fd3568`
  - `added_by`: `system`
  - `added_at`: `2026-04-29T14:48:51.363539+00:00`

#### `conversations`

- Linhas estimadas: `76056` (status 206, sample 206)
- Colunas detectadas (8): `id, phone, direction, message, media_type, ack_status, wamid, timestamp`

- dates: `media_type, timestamp`
- sensitive_or_identity: `phone, message`
- other: `id, direction, ack_status, wamid`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `direction`: `in`
  - `ack_status`: `1`
  - `wamid`: `false_5511949914664@c.us_3EB08852BCD378BF14F774`
  - `timestamp`: `2026-03-09T20:04:22.682+00:00`

### SPITI/CRM compartilhado

- Host: `rmdugdkantdydivgnimb.supabase.co`
- Status: `ok`
- OpenAPI/status: `200`
- Tabelas/recursos analisados: 36

#### `artist_pdfs`

- Linhas estimadas: `13` (status 200, sample 206)
- Colunas detectadas (6): `id, artist_name, pdf_filename, pdf_base64, created_at, updated_at`

- dates: `created_at, updated_at`
- sensitive_or_identity: `artist_name, pdf_filename`
- other: `id, pdf_base64`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `pdf_base64`: `JVBERi0xLjYNJeLjz9MNCjQ1MCAwIG9iag08PC9GaWx0ZXIvRmxhdGVEZWNvZGUvRmlyc3QgMTQvT...`
  - `created_at`: `2026-05-18T15:45:02.987758+00:00`
  - `updated_at`: `2026-05-18T15:45:02.987758+00:00`

#### `scheduled_sends`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `contacts`

- Linhas estimadas: `1961` (status 206, sample 206)
- Colunas detectadas (12): `id, phone, first_name, last_name, artist_interest, context, tags, notes, pdf_count, email, created_at, updated_at`

- dates: `created_at, updated_at`
- sensitive_or_identity: `phone, first_name, last_name, notes, email`
- other: `id, artist_interest, context, tags, pdf_count`
- Exemplos não sensíveis de formato:
  - `id`: `1854`
  - `artist_interest`: ``
  - `context`: `WhatsApp Pessoal — 19/03/2026`
  - `tags`: `lk`
  - `pdf_count`: `0`
  - `created_at`: `2026-03-19T16:51:59.363707+00:00`
  - `updated_at`: `2026-03-19T16:51:59.363707+00:00`

#### `editorial_notes`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `secretary_log`

- Linhas estimadas: `78` (status 200, sample 206)
- Colunas detectadas (16): `id, created_at, chat_jid, contact_name, last_message, last_message_at, urgency, status, suggested_reply, sent_reply, alerted_at, follow_up_scheduled_at, follow_up_sent_at, artist_detected, is_group, group_name`

- dates: `created_at`
- sensitive_or_identity: `contact_name, last_message, last_message_at, group_name`
- other: `id, chat_jid, urgency, status, suggested_reply, sent_reply, alerted_at, follow_up_scheduled_at, follow_up_sent_at, artist_detected, is_group`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `created_at`: `2026-04-02T14:22:03.676412+00:00`
  - `chat_jid`: `followup_5511981861865@s.whatsapp.net`
  - `urgency`: `normal`
  - `status`: `pending`
  - `suggested_reply`: `Oi 5511981861865, tudo bem? Passando para ver se você conseguiu dar uma olhad...`
  - `alerted_at`: `2026-04-02T14:22:03.627046+00:00`
  - `is_group`: `False`
- Distribuições categóricas amostradas:
  - `status`: pending=77, ignored=1

#### `automation_logs`

- Linhas estimadas: `2614` (status 206, sample 206)
- Colunas detectadas (6): `id, automation_id, status, message, details, executed_at`

- sensitive_or_identity: `message`
- other: `id, automation_id, status, details, executed_at`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `automation_id`: `2`
  - `status`: `success`
  - `executed_at`: `2026-03-11T12:00:17.293+00:00`
  - `details`: `{'pos': {'total': 16499.96, 'orders': 5}, 'web': {'total': 4965.08, 'orders':...`
- Distribuições categóricas amostradas:
  - `status`: 

#### `contents`

- Linhas estimadas: `268` (status 200, sample 206)
- Colunas detectadas (10): `id, platform, external_id, content_type, url, thumbnail_url, caption, published_at, raw_payload, pulled_at`

- other: `id, platform, external_id, content_type, url, thumbnail_url, caption, published_at, raw_payload, pulled_at`
- Exemplos não sensíveis de formato:
  - `id`: `314df701-aef1-4b31-9e97-3a27de251755`
  - `platform`: `mailerlite`
  - `external_id`: `168167512249206689`
  - `content_type`: `newsletter_campaign`
  - `caption`: `Flávia: 4 projetos
Flávia Junqueira em 4 novos projetos`
  - `published_at`: `2025-10-13T21:07:22+00:00`
  - `raw_payload`: `{'id': '168167512249206689', 'can': {'copy': True, 'send': True, 'delete': Tr...`
  - `pulled_at`: `2026-05-27T03:06:05.822+00:00`

#### `spiti_recebimentos`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `exhibitions`

- Linhas estimadas: `20` (status 200, sample 206)
- Colunas detectadas (10): `id, name, slug, start_date, end_date, type, hashtags, description, created_at, updated_at`

- dates: `start_date, end_date, created_at, updated_at`
- sensitive_or_identity: `name`
- other: `id, slug, type, hashtags, description`
- Exemplos não sensíveis de formato:
  - `id`: `4de65622-d053-43b3-9ae4-c68d16789c20`
  - `slug`: `acorda-2026-03`
  - `start_date`: `2026-03-21`
  - `end_date`: `2026-04-30`
  - `type`: `expo`
  - `hashtags`: `[]`
  - `created_at`: `2026-04-29T14:49:48.154556+00:00`
  - `updated_at`: `2026-04-29T14:49:48.154556+00:00`

#### `spiti_contacts`

- Linhas estimadas: `507` (status 200, sample 206)
- Colunas detectadas (12): `id, tipo, email, nome, whatsapp, telefone, timestamp_original, status, fonte, notas, data_criacao, data_atualizacao`

- dates: `timestamp_original, data_criacao, data_atualizacao`
- sensitive_or_identity: `email, nome, telefone`
- other: `id, tipo, whatsapp, status, fonte, notas`
- Exemplos não sensíveis de formato:
  - `id`: `2`
  - `tipo`: `comprador`
  - `status`: `respondido`
  - `fonte`: `compradores-confirmados.csv`
  - `data_criacao`: `2026-03-17T11:24:06.201236`
  - `data_atualizacao`: `2026-03-17T11:24:06.201236`
- Distribuições categóricas amostradas:
  - `tipo`: comprador=441, lead_whatsapp=43, collector=21, teste_service=1, teste=1
  - `status`: respondido=505, novo=2

#### `content_metrics`

- Linhas estimadas: `831` (status 200, sample 206)
- Colunas detectadas (14): `id, content_id, snapshot_date, impressions, reach, views, likes, comments, shares, saves, opens, clicks, unsubscribes, raw`

- dates: `snapshot_date`
- other: `id, content_id, impressions, reach, views, likes, comments, shares, saves, opens, clicks, unsubscribes, raw`
- Exemplos não sensíveis de formato:
  - `id`: `d77b2c55-c91b-44d9-9ca7-dccd197d0cb7`
  - `content_id`: `5f9f1e4f-b0f7-40e8-b442-0972e21f11af`
  - `snapshot_date`: `2026-04-30`
  - `opens`: `7794`
  - `clicks`: `115`
  - `unsubscribes`: `18`
  - `raw`: `{'sent': 22299, 'open_rate': {'float': 0.34952240010763, 'string': '34.95%'},...`

#### `followups`

- Linhas estimadas: `20` (status 200, sample 206)
- Colunas detectadas (8): `id, jid, nome, sent_at, followup_at, status, completed_at, created_at`

- dates: `created_at`
- sensitive_or_identity: `nome`
- other: `id, jid, sent_at, followup_at, status, completed_at`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `jid`: `31611593450@c.us`
  - `sent_at`: `2026-02-24T13:31:53.053+00:00`
  - `followup_at`: `2026-02-27T13:31:53.053+00:00`
  - `status`: `sent`
  - `completed_at`: `2026-02-27T13:31:53.65+00:00`
  - `created_at`: `2026-02-24T13:31:53.108289+00:00`
- Distribuições categóricas amostradas:
  - `status`: sent=16, cancelled=3, pending=1

#### `exhibition_artists`

- Linhas estimadas: `14` (status 200, sample 206)
- Colunas detectadas (2): `exhibition_id, artist_id`

- other: `exhibition_id, artist_id`
- Exemplos não sensíveis de formato:
  - `exhibition_id`: `4de65622-d053-43b3-9ae4-c68d16789c20`
  - `artist_id`: `5556e3a5-6e9a-4e62-9197-a90d9bd16e27`

#### `spiti_lotes_financeiro`

- Linhas estimadas: `252` (status 200, sample 206)
- Colunas detectadas (8): `id, leilao_id, lote, artista, consignante, captacao, valor_base, comissao_consignante_pct`

- money: `valor_base`
- other: `id, leilao_id, lote, artista, consignante, captacao, comissao_consignante_pct`
- Exemplos não sensíveis de formato:
  - `id`: `218`
  - `leilao_id`: `spiti9`
  - `lote`: `1`
  - `artista`: `Antônio Poteiro`
  - `consignante`: `Alysson Rodrigues`
  - `captacao`: `Alysson Rodrigues`
  - `valor_base`: `3500.0`
  - `comissao_consignante_pct`: `10.0`
- Distribuições categóricas amostradas:
  - `artista`: Emiliano Di Cavalcanti=9, Assume Vivid Astro Focus (AVAF)=6, Alfredo Volpi=5, Eric Doeringer=5, Chico da Silva=4, Jandyra Waters=4, Manabu Mabe=4, Antônio Poteiro=3, Emmanuel Nassar=3, Arthur Luiz Piza=3

#### `templates`

- Linhas estimadas: `3` (status 200, sample 200)
- Colunas detectadas (5): `id, name, body, created_at, updated_at`

- dates: `created_at, updated_at`
- sensitive_or_identity: `name`
- other: `id, body`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `body`: `[{"type":"text","content":"Olá {nome}, tudo bem?\n\nFico feliz com seu contat...`
  - `created_at`: `2026-02-20T19:11:48.477+00:00`
  - `updated_at`: `2026-02-20T19:11:48.478+00:00`

#### `spiti_vendas`

- Linhas estimadas: `151` (status 200, sample 206)
- Colunas detectadas (21): `id, leilao_id, lote, artista, titulo, comprador_nome, comprador_cartela, comprador_id, valor_arremate, forma_pagamento, status_pagamento, valor_pago, data_venda, origem, notas, criado_em, atualizado_em, lancado, data_lancamento, num_parcelas, comissao_comprador_pct`

- money: `valor_arremate, valor_pago, data_venda`
- dates: `data_lancamento`
- sensitive_or_identity: `comprador_nome`
- other: `id, leilao_id, lote, artista, titulo, comprador_cartela, comprador_id, forma_pagamento, status_pagamento, origem, notas, criado_em, atualizado_em, lancado, num_parcelas, comissao_comprador_pct`
- Exemplos não sensíveis de formato:
  - `id`: `345`
  - `leilao_id`: `spiti9`
  - `lote`: `76`
  - `artista`: `Ana Maria Tavares`
  - `valor_arremate`: `95000.0`
  - `status_pagamento`: `pendente`
  - `valor_pago`: `0.0`
  - `data_venda`: `2026-04-27`
  - `origem`: `pos-leilao`
  - `notas`: ``
  - `criado_em`: `2026-04-27T21:37:09.615502+00:00`
  - `atualizado_em`: `2026-04-27T21:37:09.615502+00:00`
  - `lancado`: `True`
  - `num_parcelas`: `1`
  - `comissao_comprador_pct`: `0`
  - `comprador_id`: `15`
- Distribuições categóricas amostradas:
  - `artista`: Emiliano Di Cavalcanti=7, Alfredo Volpi=5, Emanoel Araujo=3, Yutaka Toyota=3, Tomie Ohtake=3, Antônio Dias=3, Manabu Mabe=3, Paulo Pasta=3, Wega Nery=3, Ana Maria Tavares=2
  - `forma_pagamento`: 
  - `origem`: leiloesbr=137, pos-leilao=14

#### `spiti_pagamentos_consignante`

- Linhas estimadas: `9` (status 200, sample 206)
- Colunas detectadas (13): `id, leilao_id, consignante_nome, lotes_vendidos, valor_total_arremate, total_comissao, valor_a_pagar, valor_pago, status, forma_pagamento, data_pagamento, notas, criado_em`

- money: `valor_total_arremate, total_comissao, valor_a_pagar, valor_pago`
- dates: `data_pagamento`
- sensitive_or_identity: `consignante_nome`
- other: `id, leilao_id, lotes_vendidos, status, forma_pagamento, notas, criado_em`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `leilao_id`: `spiti9`
  - `lotes_vendidos`: `[85]`
  - `valor_total_arremate`: `29000.0`
  - `total_comissao`: `5800.0`
  - `valor_a_pagar`: `23200.0`
  - `valor_pago`: `23200.0`
  - `status`: `pago`
  - `forma_pagamento`: `PIX`
  - `data_pagamento`: `2026-04-13`
  - `notas`: `2026-04-13: R$ 23.200 PIX`
  - `criado_em`: `2026-04-13T18:03:47.200797+00:00`
- Distribuições categóricas amostradas:
  - `status`: pago=8, parcial=1
  - `forma_pagamento`: PIX=9

#### `products`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `crm_spiti`

- Linhas estimadas: `452` (status 200, sample 206)
- Colunas detectadas (14): `id, tipo, email, nome, whatsapp, telefone, timestamp_original, status, fonte, cliente_bairro, cliente_cidade, cliente_uf, data_criacao, data_atualizacao`

- dates: `timestamp_original, data_criacao, data_atualizacao`
- sensitive_or_identity: `email, nome, telefone, cliente_bairro, cliente_cidade, cliente_uf`
- other: `id, tipo, whatsapp, status, fonte`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `tipo`: `comprador`
  - `status`: `ativo`
  - `fonte`: `compradores-confirmados.csv`
  - `data_criacao`: `2026-03-17T11:49:10.267249`
  - `data_atualizacao`: `2026-03-17T11:49:10.267249`
- Distribuições categóricas amostradas:
  - `tipo`: comprador=441, prospect=8, lead_whatsapp=3
  - `status`: ativo=441, catalogo_enviado=8, respondido=3

#### `spiti_custos`

- Linhas estimadas: `54` (status 200, sample 206)
- Colunas detectadas (9): `id, leilao_id, categoria, descricao, valor, data, pago, notas, criado_em`

- money: `valor`
- dates: `data`
- other: `id, leilao_id, categoria, descricao, pago, notas, criado_em`
- Exemplos não sensíveis de formato:
  - `id`: `70`
  - `leilao_id`: `spiti9`
  - `categoria`: `Marketing`
  - `descricao`: `Facebook`
  - `valor`: `2.29`
  - `data`: `2026-04-24`
  - `pago`: `True`
  - `notas`: ``
  - `criado_em`: `2026-04-24T13:29:01.493239+00:00`
- Distribuições categóricas amostradas:
  - `categoria`: Produção=11, Marketing=8, Alimentação=7, Freelance=6, Geral=5, Estrutura=5, Reembolso=4, Outros=3, Comissão=3, Segurança=2

#### `spiti_clientes`

- Linhas estimadas: `94` (status 200, sample 206)
- Colunas detectadas (10): `id, leilao_id, nome, cpf, endereco, email, telefone, cartela, notas, created_at`

- dates: `created_at`
- sensitive_or_identity: `nome, cpf, endereco, email, telefone`
- other: `id, leilao_id, cartela, notas`
- Exemplos não sensíveis de formato:
  - `id`: `10`
  - `leilao_id`: `spiti9`
  - `created_at`: `2026-04-16T09:51:45.328259+00:00`

#### `spiti_lotes`

- Linhas estimadas: `251` (status 200, sample 206)
- Colunas detectadas (16): `id, lote_id, artista, titulo, descricao, tecnica, dimensoes, ano, lance_atual, proximo_lance, status, img_url, url, data_pregao, criado_em, atualizado_em`

- dates: `data_pregao`
- other: `id, lote_id, artista, titulo, descricao, tecnica, dimensoes, ano, lance_atual, proximo_lance, status, img_url, url, criado_em, atualizado_em`
- Exemplos não sensíveis de formato:
  - `id`: `23`
  - `lote_id`: `29723823`
  - `artista`: `Wega Nery`
  - `titulo`: `Futuro sonhado`
  - `descricao`: `Lote 117`
  - `tecnica`: `Ãleo sobre tela`
  - `dimensoes`: `92 x 64 cm`
  - `ano`: `1990`
  - `lance_atual`: `9000.0`
  - `proximo_lance`: `9500`
  - `status`: `com_lance`
  - `img_url`: `https://d1o6h00a1h5k7q.cloudfront.net/imagens/img_m/60396/29723823.jpg`
  - `url`: `https://www.spiti.art/peca.asp?ID=29723823`
  - `data_pregao`: `01/04/2026`
  - `criado_em`: `2026-03-20T20:52:08.327802`
  - `atualizado_em`: `2026-04-01T01:50:11.148718`
- Distribuições categóricas amostradas:
  - `artista`: Emiliano Di Cavalcanti=9, Assume Vivid Astro Focus (AVAF)=6, Alfredo Volpi=5, Eric Doeringer=5, Emanoel Araujo=5, Mira Schendel=4, Chico da Silva=4, Jandyra Waters=4, Manabu Mabe=4, Wega Nery=3
  - `ano`: s/d=45, 1986=7, 2011=7, 1970=6, 1987=6, 1996=6, 1988=5, 1967=5, 2007=5, 1985=5
  - `status`: com_lance=142, sem_lance=109

#### `product_contacts`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `messages_log`

- Linhas estimadas: `24` (status 200, sample 206)
- Colunas detectadas (5): `id, phone, message, template_used, sent_at`

- sensitive_or_identity: `phone, message`
- other: `id, template_used, sent_at`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `template_used`: `bulk`
  - `sent_at`: `2026-02-16T01:58:54.627+00:00`

#### `spiti_parcelas`

- Linhas estimadas: `148` (status 200, sample 206)
- Colunas detectadas (10): `id, cobranca_id, numero, valor, forma_pagamento, data_vencimento, data_pagamento, status, notas, criado_em`

- money: `valor`
- dates: `data_vencimento, data_pagamento`
- other: `id, cobranca_id, numero, forma_pagamento, status, notas, criado_em`
- Exemplos não sensíveis de formato:
  - `id`: `80`
  - `cobranca_id`: `79`
  - `numero`: `1`
  - `valor`: `19800.0`
  - `forma_pagamento`: `DINHEIRO`
  - `data_vencimento`: `2026-04-02`
  - `data_pagamento`: `2026-04-02`
  - `status`: `pago`
  - `criado_em`: `2026-04-02T17:41:53.006962+00:00`
- Distribuições categóricas amostradas:
  - `forma_pagamento`: PIX=142, DINHEIRO=5, CHEQUE=1
  - `status`: pago=129, pendente=19

#### `spiti_todos`

- Linhas estimadas: `1` (status 200, sample 200)
- Colunas detectadas (17): `id, leilao_id, titulo, descricao, status, prioridade, responsavel_nome, responsavel_area, origem, referencias, checklist, created_at, updated_at, done_at, created_by, updated_by, responsavel_email`

- dates: `created_at, updated_at, created_by, updated_by`
- sensitive_or_identity: `responsavel_nome, responsavel_email`
- other: `id, leilao_id, titulo, descricao, status, prioridade, responsavel_area, origem, referencias, checklist, done_at`
- Exemplos não sensíveis de formato:
  - `id`: `spiti9-reconciliacao-lotes-27-91-consignantes`
  - `leilao_id`: `spiti9`
  - `titulo`: `Reconciliar lotes 27/91 e grade de pagamentos a consignantes — SPITI 9`
  - `descricao`: `Confirmar o split do residual de R$ 40.000 entre os lotes 27 e 91, corrigir/c...`
  - `status`: `pending`
  - `prioridade`: `alta`
  - `responsavel_area`: `Produtora SPITI`
  - `origem`: `Cobrança 113 / PRD Claw`
  - `referencias`: `{'prd': 'empresa/prds/2026-04-28-spiti-financial-reconciliacao-lotes-consigna...`
  - `checklist`: `[{'done': False, 'label': 'Revisar cobrança 113 na origem operacional/finance...`
  - `created_at`: `2026-04-28T22:22:00+00:00`
  - `updated_at`: `2026-04-28T23:37:07.900328+00:00`
- Distribuições categóricas amostradas:
  - `status`: pending=1
  - `origem`: Cobrança 113 / PRD Claw=1

#### `automations`

- Linhas estimadas: `6` (status 200, sample 206)
- Colunas detectadas (7): `id, type, name, config, enabled, created_at, updated_at`

- dates: `created_at, updated_at`
- sensitive_or_identity: `name`
- other: `id, type, config, enabled`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `type`: `google_calendar_daily`
  - `config`: `{'timezone': 'America/Sao_Paulo', 'calendar_id': 'primary', 'notify_time': '0...`
  - `enabled`: `False`
  - `created_at`: `2026-03-11T00:41:29.26839+00:00`
  - `updated_at`: `2026-03-11T00:41:29.26839+00:00`

#### `sync_runs`

- Linhas estimadas: `50` (status 200, sample 206)
- Colunas detectadas (10): `id, source, started_at, finished_at, items_seen, items_new, items_tagged, status, error_message, notes`

- sensitive_or_identity: `error_message, notes`
- other: `id, source, started_at, finished_at, items_seen, items_new, items_tagged, status`
- Exemplos não sensíveis de formato:
  - `id`: `baeb8544-11b3-4299-90eb-c633b775a8c1`
  - `source`: `api:mailerlite`
  - `started_at`: `2026-04-30T13:10:30.799402+00:00`
  - `finished_at`: `2026-04-30T13:10:58.991+00:00`
  - `items_seen`: `29`
  - `items_new`: `29`
  - `items_tagged`: `9`
  - `status`: `success`
- Distribuições categóricas amostradas:
  - `status`: success=50

#### `artists`

- Linhas estimadas: `36` (status 200, sample 206)
- Colunas detectadas (14): `id, name, slug, name_variations, hashtags, instagram_handle, tiktok_handle, youtube_channel_id, photo_url, bio, is_roster, active, created_at, updated_at`

- dates: `created_at, updated_at`
- sensitive_or_identity: `name, name_variations`
- other: `id, slug, hashtags, instagram_handle, tiktok_handle, youtube_channel_id, photo_url, bio, is_roster, active`
- Exemplos não sensíveis de formato:
  - `id`: `2cd426de-d617-4982-bc80-7c61d05cdb42`
  - `slug`: `adriana-duque`
  - `hashtags`: `[]`
  - `is_roster`: `True`
  - `active`: `True`
  - `created_at`: `2026-04-29T14:49:46.837837+00:00`
  - `updated_at`: `2026-04-30T13:43:40.995638+00:00`

#### `spiti_rsvp`

- Linhas estimadas: `7` (status 200, sample 206)
- Colunas detectadas (8): `id, nome, email, whatsapp, cpf, confirmed_at, notified_wpp, notified_email`

- sensitive_or_identity: `nome, email, cpf, notified_email`
- other: `id, whatsapp, confirmed_at, notified_wpp`
- Exemplos não sensíveis de formato:
  - `id`: `2`
  - `whatsapp`: `(55) 11991-2033`
  - `confirmed_at`: `2026-03-30T17:53:19.72+00:00`
  - `notified_wpp`: `True`

#### `spiti_parcelas_pagamento`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `content_tags`

- Linhas estimadas: `315` (status 200, sample 206)
- Colunas detectadas (9): `id, content_id, entity_type, entity_id, source, matched_text, confirmed_by, confirmed_at, created_at`

- dates: `created_at`
- other: `id, content_id, entity_type, entity_id, source, matched_text, confirmed_by, confirmed_at`
- Exemplos não sensíveis de formato:
  - `id`: `e4292e51-d0d2-43cf-843a-7b68765752df`
  - `content_id`: `828b9064-cceb-4cda-b5a9-4fd57900e9cb`
  - `entity_type`: `exhibition`
  - `entity_id`: `ffe9b130-5dbe-4347-915a-9a22d6a0aaf1`
  - `source`: `auto`
  - `matched_text`: `SP-Arte`
  - `created_at`: `2026-04-30T15:13:07.070464+00:00`

#### `sent_contacts`

- Linhas estimadas: `0` (status 200, sample 200)
- Colunas detectadas (0): ``


#### `spiti_cobrancas`

- Linhas estimadas: `108` (status 200, sample 206)
- Colunas detectadas (16): `id, leilao_id, comprador_nome, comprador_id, lotes, valor_arremate_total, comissao_total, valor_total, forma_pagamento, num_parcelas, valor_pago, status, lancado, lancado_em, notas, criado_em`

- money: `valor_arremate_total, comissao_total, valor_total, valor_pago`
- sensitive_or_identity: `comprador_nome`
- other: `id, leilao_id, comprador_id, lotes, forma_pagamento, num_parcelas, status, lancado, lancado_em, notas, criado_em`
- Exemplos não sensíveis de formato:
  - `id`: `79`
  - `leilao_id`: `spiti9`
  - `lotes`: `[16, 28]`
  - `valor_arremate_total`: `18000.0`
  - `comissao_total`: `1800.0`
  - `valor_total`: `19800.0`
  - `forma_pagamento`: `DINHEIRO`
  - `num_parcelas`: `1`
  - `valor_pago`: `19800.0`
  - `status`: `pago`
  - `lancado`: `True`
  - `lancado_em`: `2026-04-02T17:41:52.501+00:00`
  - `notas`: ``
  - `criado_em`: `2026-04-02T17:41:52.750226+00:00`
- Distribuições categóricas amostradas:
  - `forma_pagamento`: PIX=81, PIX, PIX=11, PIX, PIX, PIX=7, PIX, PIX, PIX, PIX=3, DINHEIRO=2, DINHEIRO, PIX=1, PIX, CHEQUE=1, PIX, DINHEIRO, PIX, PIX=1, PIX, DINHEIRO=1
  - `status`: pago=96, parcial=12

#### `authorized_emails`

- Linhas estimadas: `4` (status 200, sample 200)
- Colunas detectadas (4): `id, email, added_by, added_at`

- sensitive_or_identity: `email`
- other: `id, added_by, added_at`
- Exemplos não sensíveis de formato:
  - `id`: `dae89d03-cd62-435f-8124-1a2ac5fd3568`
  - `added_by`: `system`
  - `added_at`: `2026-04-29T14:48:51.363539+00:00`

#### `conversations`

- Linhas estimadas: `76056` (status 206, sample 206)
- Colunas detectadas (8): `id, phone, direction, message, media_type, ack_status, wamid, timestamp`

- dates: `media_type, timestamp`
- sensitive_or_identity: `phone, message`
- other: `id, direction, ack_status, wamid`
- Exemplos não sensíveis de formato:
  - `id`: `1`
  - `direction`: `in`
  - `ack_status`: `1`
  - `wamid`: `false_5511949914664@c.us_3EB08852BCD378BF14F774`
  - `timestamp`: `2026-03-09T20:04:22.682+00:00`

## Implicações para o PRD

- O Zipper OS deve tratar Supabase como fonte read-only inicial e só escrever em fonte de verdade após fluxo A3/A4 com aprovação explícita.
- `vendas_tango` deve ser o núcleo do módulo Comercial/Vendas quando disponível, com consultas por artista, canal/origem, período e ticket.
- Campos sensíveis/de identidade devem ser minimizados nos resumos; Telegram deve receber apenas o necessário para decisão.
- O PRD precisa separar camada de dados reais (vendas) da camada de comunicação (e-mail/WhatsApp/rascunhos) e da camada de logística/calendário.
