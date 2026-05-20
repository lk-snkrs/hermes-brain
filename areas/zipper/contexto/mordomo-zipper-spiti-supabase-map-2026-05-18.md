# Mordomo Zipper/SPITI — Mapa read-only do Supabase

Atualizado: 2026-05-18T15:23:17.937166+00:00

## Segurança

- Execução read-only via Supabase/PostgREST; nenhum write, migration ou envio externo.
- Credenciais lidas via Doppler; nenhum secret foi salvo ou impresso.
- Relatório sem PII bruta: só estrutura, contagens, campos e recomendações.

## Projetos e fonte de verdade

- Zipper vendas reais: `pcstqxpdzibheuopjkas`, tabela `vendas_tango`.
- CRM/Main/Zipper+SPITI: `rmdugdkantdydivgnimb`, com contatos, conversas, conteúdo, automações e tabelas SPITI.
- Observação: `SUPABASE_ZIPPER_URL` e `SUPABASE_SPITI_URL` apontam para o mesmo host operacional no inventário atual; a separação deve ser lógica por prefixo/tabela, não por suposição de projeto diferente.

## Zipper Vendas

Host: `pcstqxpdzibheuopjkas.supabase.co`

### Zipper vendas reais

- `vendas_tango`
  - Linhas: `2102`; status: ativa
  - Campos: `id, created_at, pedido_id, pedido_data, pedido_origem, pedido_evento, cliente_id, cliente_nome, cliente_bairro, cliente_cidade, cliente_uf, cliente_pais, artista_nome, valor_obra_final, acervo_id, deal_name, email, whatsapp`

## Zipper CRM/Main

Host: `rmdugdkantdydivgnimb.supabase.co`

### Automação/integração

- `automation_logs`
  - Linhas: `2614`; status: ativa
  - Campos: `id, automation_id, status, message, details, executed_at`
- `automations`
  - Linhas: `6`; status: ativa
  - Campos: `id, type, name, config, enabled, created_at, updated_at`
- `sync_runs`
  - Linhas: `48`; status: ativa
  - Campos: `id, source, started_at, finished_at, items_seen, items_new, items_tagged, status, error_message, notes`
- `authorized_emails`
  - Linhas: `4`; status: ativa
  - Campos: `id, email, added_by, added_at`

### CRM/atendimento compartilhado

- `artist_pdfs`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
  - Papel provável: lacuna/futuro módulo; precisa de desenho antes de qualquer write.
- `scheduled_sends`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
  - Papel provável: lacuna/futuro módulo; precisa de desenho antes de qualquer write.
- `contacts`
  - Linhas: `1960`; status: ativa
  - Campos: `id, phone, first_name, last_name, artist_interest, context, tags, notes, pdf_count, email, created_at, updated_at`
- `secretary_log`
  - Linhas: `78`; status: ativa
  - Campos: `id, created_at, chat_jid, contact_name, last_message, last_message_at, urgency, status, suggested_reply, sent_reply, alerted_at, follow_up_scheduled_at, follow_up_sent_at, artist_detected, is_group, group_name`
- `followups`
  - Linhas: `19`; status: ativa
  - Campos: `id, jid, nome, sent_at, followup_at, status, completed_at, created_at`
- `templates`
  - Linhas: `3`; status: ativa
  - Campos: `id, name, body, created_at, updated_at`
- `messages_log`
  - Linhas: `19`; status: ativa
  - Campos: `id, phone, message, template_used, sent_at`
- `sent_contacts`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
  - Papel provável: lacuna/futuro módulo; precisa de desenho antes de qualquer write.
- `conversations`
  - Linhas: `76056`; status: ativa
  - Campos: `id, phone, direction, message, media_type, ack_status, wamid, timestamp`

### Produto/obra futuro ou subutilizado

- `products`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
  - Papel provável: lacuna/futuro módulo; precisa de desenho antes de qualquer write.
- `product_contacts`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
  - Papel provável: lacuna/futuro módulo; precisa de desenho antes de qualquer write.

### SPITI/leilão

- `spiti_recebimentos`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
- `spiti_contacts`
  - Linhas: `507`; status: ativa
  - Campos: `id, tipo, email, nome, whatsapp, telefone, timestamp_original, status, fonte, notas, data_criacao, data_atualizacao`
- `spiti_lotes_financeiro`
  - Linhas: `252`; status: ativa
  - Campos: `id, leilao_id, lote, artista, consignante, captacao, valor_base, comissao_consignante_pct`
- `spiti_vendas`
  - Linhas: `151`; status: ativa
  - Campos: `id, leilao_id, lote, artista, titulo, comprador_nome, comprador_cartela, comprador_id, valor_arremate, forma_pagamento, status_pagamento, valor_pago, data_venda, origem, notas, criado_em, atualizado_em, lancado, data_lancamento, num_parcelas, comissao_comprador_pct`
- `spiti_pagamentos_consignante`
  - Linhas: `9`; status: ativa
  - Campos: `id, leilao_id, consignante_nome, lotes_vendidos, valor_total_arremate, total_comissao, valor_a_pagar, valor_pago, status, forma_pagamento, data_pagamento, notas, criado_em`
- `crm_spiti`
  - Linhas: `452`; status: ativa
  - Campos: `id, tipo, email, nome, whatsapp, telefone, timestamp_original, status, fonte, cliente_bairro, cliente_cidade, cliente_uf, data_criacao, data_atualizacao`
- `spiti_custos`
  - Linhas: `48`; status: ativa
  - Campos: `id, leilao_id, categoria, descricao, valor, data, pago, notas, criado_em`
- `spiti_clientes`
  - Linhas: `94`; status: ativa
  - Campos: `id, leilao_id, nome, cpf, endereco, email, telefone, cartela, notas, created_at`
- `spiti_lotes`
  - Linhas: `251`; status: ativa
  - Campos: `id, lote_id, artista, titulo, descricao, tecnica, dimensoes, ano, lance_atual, proximo_lance, status, img_url, url, data_pregao, criado_em, atualizado_em`
- `spiti_parcelas`
  - Linhas: `148`; status: ativa
  - Campos: `id, cobranca_id, numero, valor, forma_pagamento, data_vencimento, data_pagamento, status, notas, criado_em`
- `spiti_todos`
  - Linhas: `1`; status: ativa
  - Campos: `id, leilao_id, titulo, descricao, status, prioridade, responsavel_nome, responsavel_area, origem, referencias, checklist, created_at, updated_at, done_at, created_by, updated_by, responsavel_email`
- `spiti_rsvp`
  - Linhas: `7`; status: ativa
  - Campos: `id, nome, email, whatsapp, cpf, confirmed_at, notified_wpp, notified_email`
- `spiti_parcelas_pagamento`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
- `spiti_cobrancas`
  - Linhas: `108`; status: ativa
  - Campos: `id, leilao_id, comprador_nome, comprador_id, lotes, valor_arremate_total, comissao_total, valor_total, forma_pagamento, num_parcelas, valor_pago, status, lancado, lancado_em, notas, criado_em`

### Zipper conteúdo/artistas/exposições

- `editorial_notes`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
- `contents`
  - Linhas: `266`; status: ativa
  - Campos: `id, platform, external_id, content_type, url, thumbnail_url, caption, published_at, raw_payload, pulled_at`
- `exhibitions`
  - Linhas: `20`; status: ativa
  - Campos: `id, name, slug, start_date, end_date, type, hashtags, description, created_at, updated_at`
- `content_metrics`
  - Linhas: `798`; status: ativa
  - Campos: `id, content_id, snapshot_date, impressions, reach, views, likes, comments, shares, saves, opens, clicks, unsubscribes, raw`
- `exhibition_artists`
  - Linhas: `14`; status: ativa
  - Campos: `exhibition_id, artist_id`
- `artists`
  - Linhas: `36`; status: ativa
  - Campos: `id, name, slug, name_variations, hashtags, instagram_handle, tiktok_handle, youtube_channel_id, photo_url, bio, is_roster, active, created_at, updated_at`
- `content_tags`
  - Linhas: `313`; status: ativa
  - Campos: `id, content_id, entity_type, entity_id, source, matched_text, confirmed_by, confirmed_at, created_at`

## SPITI/CRM compartilhado

Host: `rmdugdkantdydivgnimb.supabase.co`

### Automação/integração

- `automation_logs`
  - Linhas: `2614`; status: ativa
  - Campos: `id, automation_id, status, message, details, executed_at`
- `automations`
  - Linhas: `6`; status: ativa
  - Campos: `id, type, name, config, enabled, created_at, updated_at`
- `sync_runs`
  - Linhas: `48`; status: ativa
  - Campos: `id, source, started_at, finished_at, items_seen, items_new, items_tagged, status, error_message, notes`
- `authorized_emails`
  - Linhas: `4`; status: ativa
  - Campos: `id, email, added_by, added_at`

### CRM/atendimento compartilhado

- `artist_pdfs`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
  - Papel provável: lacuna/futuro módulo; precisa de desenho antes de qualquer write.
- `scheduled_sends`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
  - Papel provável: lacuna/futuro módulo; precisa de desenho antes de qualquer write.
- `contacts`
  - Linhas: `1960`; status: ativa
  - Campos: `id, phone, first_name, last_name, artist_interest, context, tags, notes, pdf_count, email, created_at, updated_at`
- `secretary_log`
  - Linhas: `78`; status: ativa
  - Campos: `id, created_at, chat_jid, contact_name, last_message, last_message_at, urgency, status, suggested_reply, sent_reply, alerted_at, follow_up_scheduled_at, follow_up_sent_at, artist_detected, is_group, group_name`
- `followups`
  - Linhas: `19`; status: ativa
  - Campos: `id, jid, nome, sent_at, followup_at, status, completed_at, created_at`
- `templates`
  - Linhas: `3`; status: ativa
  - Campos: `id, name, body, created_at, updated_at`
- `messages_log`
  - Linhas: `19`; status: ativa
  - Campos: `id, phone, message, template_used, sent_at`
- `sent_contacts`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
  - Papel provável: lacuna/futuro módulo; precisa de desenho antes de qualquer write.
- `conversations`
  - Linhas: `76056`; status: ativa
  - Campos: `id, phone, direction, message, media_type, ack_status, wamid, timestamp`

### Produto/obra futuro ou subutilizado

- `products`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
  - Papel provável: lacuna/futuro módulo; precisa de desenho antes de qualquer write.
- `product_contacts`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
  - Papel provável: lacuna/futuro módulo; precisa de desenho antes de qualquer write.

### SPITI/leilão

- `spiti_recebimentos`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
- `spiti_contacts`
  - Linhas: `507`; status: ativa
  - Campos: `id, tipo, email, nome, whatsapp, telefone, timestamp_original, status, fonte, notas, data_criacao, data_atualizacao`
- `spiti_lotes_financeiro`
  - Linhas: `252`; status: ativa
  - Campos: `id, leilao_id, lote, artista, consignante, captacao, valor_base, comissao_consignante_pct`
- `spiti_vendas`
  - Linhas: `151`; status: ativa
  - Campos: `id, leilao_id, lote, artista, titulo, comprador_nome, comprador_cartela, comprador_id, valor_arremate, forma_pagamento, status_pagamento, valor_pago, data_venda, origem, notas, criado_em, atualizado_em, lancado, data_lancamento, num_parcelas, comissao_comprador_pct`
- `spiti_pagamentos_consignante`
  - Linhas: `9`; status: ativa
  - Campos: `id, leilao_id, consignante_nome, lotes_vendidos, valor_total_arremate, total_comissao, valor_a_pagar, valor_pago, status, forma_pagamento, data_pagamento, notas, criado_em`
- `crm_spiti`
  - Linhas: `452`; status: ativa
  - Campos: `id, tipo, email, nome, whatsapp, telefone, timestamp_original, status, fonte, cliente_bairro, cliente_cidade, cliente_uf, data_criacao, data_atualizacao`
- `spiti_custos`
  - Linhas: `48`; status: ativa
  - Campos: `id, leilao_id, categoria, descricao, valor, data, pago, notas, criado_em`
- `spiti_clientes`
  - Linhas: `94`; status: ativa
  - Campos: `id, leilao_id, nome, cpf, endereco, email, telefone, cartela, notas, created_at`
- `spiti_lotes`
  - Linhas: `251`; status: ativa
  - Campos: `id, lote_id, artista, titulo, descricao, tecnica, dimensoes, ano, lance_atual, proximo_lance, status, img_url, url, data_pregao, criado_em, atualizado_em`
- `spiti_parcelas`
  - Linhas: `148`; status: ativa
  - Campos: `id, cobranca_id, numero, valor, forma_pagamento, data_vencimento, data_pagamento, status, notas, criado_em`
- `spiti_todos`
  - Linhas: `1`; status: ativa
  - Campos: `id, leilao_id, titulo, descricao, status, prioridade, responsavel_nome, responsavel_area, origem, referencias, checklist, created_at, updated_at, done_at, created_by, updated_by, responsavel_email`
- `spiti_rsvp`
  - Linhas: `7`; status: ativa
  - Campos: `id, nome, email, whatsapp, cpf, confirmed_at, notified_wpp, notified_email`
- `spiti_parcelas_pagamento`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
- `spiti_cobrancas`
  - Linhas: `108`; status: ativa
  - Campos: `id, leilao_id, comprador_nome, comprador_id, lotes, valor_arremate_total, comissao_total, valor_total, forma_pagamento, num_parcelas, valor_pago, status, lancado, lancado_em, notas, criado_em`

### Zipper conteúdo/artistas/exposições

- `editorial_notes`
  - Linhas: `0`; status: vazia/subutilizada
  - Campos: `não expostos no sample; provável tabela vazia ou sem permissões de sample`
- `contents`
  - Linhas: `266`; status: ativa
  - Campos: `id, platform, external_id, content_type, url, thumbnail_url, caption, published_at, raw_payload, pulled_at`
- `exhibitions`
  - Linhas: `20`; status: ativa
  - Campos: `id, name, slug, start_date, end_date, type, hashtags, description, created_at, updated_at`
- `content_metrics`
  - Linhas: `798`; status: ativa
  - Campos: `id, content_id, snapshot_date, impressions, reach, views, likes, comments, shares, saves, opens, clicks, unsubscribes, raw`
- `exhibition_artists`
  - Linhas: `14`; status: ativa
  - Campos: `exhibition_id, artist_id`
- `artists`
  - Linhas: `36`; status: ativa
  - Campos: `id, name, slug, name_variations, hashtags, instagram_handle, tiktok_handle, youtube_channel_id, photo_url, bio, is_roster, active, created_at, updated_at`
- `content_tags`
  - Linhas: `313`; status: ativa
  - Campos: `id, content_id, entity_type, entity_id, source, matched_text, confirmed_by, confirmed_at, created_at`

## Cobertura por necessidade do Mordomo

- Contatos: `contacts`, `spiti_contacts`, `crm_spiti`, `spiti_clientes`.
- Conversas/atendimento: `conversations`, `secretary_log`, `messages_log`, `followups`.
- Vendas Zipper: `vendas_tango`.
- Vendas/financeiro SPITI: `spiti_vendas`, `spiti_cobrancas`, `spiti_parcelas`, `spiti_lotes_financeiro`, `spiti_pagamentos_consignante`.
- Artistas/exposições/conteúdo: `artists`, `exhibitions`, `exhibition_artists`, `contents`, `content_tags`, `content_metrics`.
- PDFs/propostas/envios: `artist_pdfs`, `scheduled_sends`, `sent_contacts` existem, mas estão vazias/subutilizadas; hoje o histórico real fica disperso entre `conversations`, `messages_log`, `secretary_log` e o fluxo externo do `!enviar`.
- Automações: `automations`, `automation_logs`, `sync_runs`.

## Lacunas mínimas antes de automação

1. View read-only `artist_interest_signals`: unir vendas, contatos, conversas e tags por artista com score e exclusões.
2. View/tabela controlada `proposal_events`: registrar proposta/PDF enviado, artista, fonte do PDF, status e follow-up; hoje não há trilha suficiente por artista.
3. Cadastro validado de PDFs por artista/obra: preencher/desenhar `artist_pdfs` antes de qualquer envio automático.
4. Campo/estrutura de sinal negativo (`negative_fit_reason`, `blocked_until` ou equivalente) para bloquear desfit sem depender só de busca textual.
5. Regras de minimização: Telegram recebe contatos mascarados/resumos; qualquer PII bruta fica na fonte de verdade.

## Próximo passo recomendado

Usar o protótipo read-only de busca por artista como base das views acima; não criar CRM paralelo.
