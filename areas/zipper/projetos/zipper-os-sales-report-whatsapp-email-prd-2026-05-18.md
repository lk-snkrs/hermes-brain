# PRD — Zipper OS · Report diário de vendas por WhatsApp e e-mail

Data: 2026-05-18  
Owner: Lucas Cimino  
Produto: Zipper OS / Hermes Brain / Mordomo  
Status: PRD v0.1 — pronto para implementação após gate técnico

## 1. Decisão de produto

Criar um **report diário de vendas da Zipper Galeria** dentro do **Zipper OS**, usando sempre o Supabase como fonte de verdade, e entregando de segunda a sexta em dois canais internos:

- WhatsApp: grupo **[ZPR] IA Bot**.
- E-mail: `lucas@zippergaleria.com.br`, `osmar@zippergaleria.com.br`, `fabio@zippergaleria.com.br`.

Este report é uma rotina operacional interna da galeria. Ele não substitui o Mordomo de follow-ups/inbox/drafts: follow-ups, triagem de conversas e rascunhos continuam centralizados no Mordomo. Este PRD cobre apenas **vendas comerciais consolidadas**.

## 2. Objetivo

Todos os dias úteis, entregar para a equipe Zipper uma leitura clara e objetiva das vendas recentes, com foco em:

1. vendas de ontem ou do último período fechado;
2. total vendido;
3. quantidade de pedidos/vendas;
4. artistas vendidos;
5. origem/evento/canal das vendas;
6. principais destaques comerciais;
7. alertas de qualidade de dados;
8. comparação simples com períodos anteriores quando tecnicamente confiável.

O report deve ser curto no WhatsApp e mais completo no e-mail.

## 3. Fonte de verdade

### Supabase Zipper Vendas

- Projeto: `pcstqxpdzibheuopjkas`.
- Tabela: `vendas_tango`.
- Credenciais: Doppler `lc-keys/prd`; nunca salvar nem imprimir valores.

Campos relevantes já mapeados:

- `id`
- `created_at`
- `pedido_id`
- `pedido_data`
- `pedido_origem`
- `pedido_evento`
- `cliente_id`
- `cliente_nome`
- `cliente_bairro`
- `cliente_cidade`
- `cliente_uf`
- `cliente_pais`
- `artista_nome`
- `valor_obra_final`
- `acervo_id`
- `deal_name`
- `email`
- `whatsapp`

Regra central: **nenhum report de venda da Zipper deve usar SPITI, CRM genérico ou conversas como fonte principal de venda realizada. Venda realizada = `vendas_tango`.**

## 4. Escopo do report V1

### WhatsApp — resumo executivo

Formato sugerido:

```text
Zipper OS · Vendas — DD/MM

Ontem:
• Total vendido: R$ X
• Vendas: N
• Ticket médio: R$ X
• Artistas: A, B, C
• Origem/canal: origem 1, origem 2

Destaque:
• [1 insight curto sobre artista, evento, cidade ou ticket]

Qualidade dos dados:
• [OK ou alerta curto: venda sem artista, sem valor, sem origem, etc.]
```

Regras de WhatsApp:

- linguagem objetiva, elegante, sem tom de cobrança;
- sem exposição desnecessária de PII;
- não listar e-mail/WhatsApp de cliente;
- nomes de clientes só se houver decisão explícita posterior; padrão V1 deve agregá-los ou mascará-los;
- máximo recomendado: 8 a 12 linhas.

### E-mail — companion executivo

Assunto sugerido:

`Zipper OS · Report de vendas — DD/MM/YYYY`

Conteúdo sugerido:

1. Cabeçalho: data/período, fonte Supabase, horário de geração.
2. KPIs:
   - total vendido;
   - vendas;
   - ticket médio;
   - artistas distintos;
   - cidades/UFs distintas quando disponível;
   - origem/evento principal.
3. Tabela/resumo por artista:
   - artista;
   - quantidade de vendas;
   - valor total;
   - ticket médio.
4. Origem/evento:
   - `pedido_origem` e `pedido_evento` agregados.
5. Top vendas / destaques sem PII sensível:
   - artista + obra/deal quando disponível + valor;
   - cliente mascarado ou omitido por padrão.
6. Qualidade de dados:
   - vendas sem `valor_obra_final`;
   - vendas sem `artista_nome`;
   - vendas sem `pedido_data`;
   - vendas duplicadas por `pedido_id` se detectadas.
7. Rodapé:
   - `Fonte: Supabase Zipper Vendas / vendas_tango`;
   - `Gerado por Zipper OS`;
   - receipt interno com hash/ID de execução, sem secrets.

## 5. Janela de análise

V1 padrão:

- Segunda a sexta.
- Horário sugerido: **09:00 BRT**, alinhado ao modelo de report diário.
- Período principal: **ontem** (`pedido_data` do dia anterior em America/Sao_Paulo).

Regras de final de semana/segunda-feira:

- Opção A — recomendada: segunda-feira reporta sexta, sábado e domingo separados em blocos.
- Opção B — alternativa: segunda-feira reporta apenas domingo/ontem, mas isso perde visão do fim de semana.

Decisão recomendada para implementação: **segunda-feira consolidar o fim de semana**, com blocos:

- Sexta;
- Sábado;
- Domingo;
- Total do fim de semana.

## 6. Destinos de entrega

### WhatsApp

- Grupo: **[ZPR] IA Bot**.
- Implementação deve descobrir e fixar o JID do grupo via `wacli`, sem hardcode por nome solto.
- Conta WhatsApp: usar a conta operacional que estiver autenticada para Zipper/Hermes conforme decisão técnica; confirmar no gate antes de ativar.
- Guardrail: antes de criar o cron definitivo, validar `auth status`, grupo correto e dry-run da mensagem.

### E-mail

Destinatários V1:

- `lucas@zippergaleria.com.br`
- `osmar@zippergaleria.com.br`
- `fabio@zippergaleria.com.br`

Conta remetente preferencial:

- credencial Zipper/Lucas disponível em Doppler, validada por Gmail API ou mecanismo já usado para reports.

Guardrail:

- verificar MIME/HTML após envio;
- verificar assunto, destinatários, marker do report e ausência de padrões de secret;
- registrar message_id/thread_id no receipt local.

## 7. Segurança e governança

Este report é uma exceção operacional interna autorizada por PRD para entrega recorrente a canais internos definidos. Ainda assim, a implementação deve respeitar:

- sem envio para clientes, artistas, fornecedores ou colecionadores;
- sem rascunhos de follow-up;
- sem proposta comercial;
- sem preço/disponibilidade individual fora do que já consta como venda realizada;
- sem writes em Supabase;
- sem alteração em CRM;
- sem exposição de secrets;
- sem dados pessoais brutos no WhatsApp;
- e-mail pode ter mais detalhe comercial, mas deve evitar e-mail/telefone/WhatsApp de cliente no V1.

Qualquer ampliação de destinatário, mudança de grupo ou inclusão de PII bruta exige novo gate explícito.

## 8. Arquitetura técnica proposta

### Componentes

1. **Generator read-only**
   - Script: `zipper_sales_report_generator.py`.
   - Lê Supabase `vendas_tango` via PostgREST.
   - Produz payload JSON com KPIs, mensagens e paths de artefatos.
   - Não envia nada.

2. **Renderer**
   - Gera:
     - texto WhatsApp;
     - HTML de e-mail;
     - JSON de evidência;
     - opcional markdown local.

3. **Delivery layer aprovado**
   - Script: `zipper_sales_report_external_delivery.py`.
   - Valida destinos fixos.
   - Envia WhatsApp para o JID aprovado.
   - Envia e-mail para os três destinatários aprovados.
   - Verifica entrega e MIME.
   - Registra receipt.

4. **Watchdog/cron wrapper**
   - Script: `zipper_weekday_sales_report_watchdog.py`.
   - Roda de segunda a sexta.
   - Em sucesso, pode ficar silencioso para Telegram/origem ou emitir apenas receipt curto conforme configuração.
   - Em falha, alerta com erro sanitizado.

### Estado local

Diretório sugerido:

`/opt/data/hermes_bruno_ingest/local_sql/zipper_sales_report/`

Arquivos:

- `state.json` — última execução, hash de período, controle anti-duplicidade.
- `receipts.jsonl` — receipts sanitizados de envio.
- `artifacts/YYYY-MM-DD/` — HTML, texto e JSON do report.

## 9. Anti-duplicidade

A rotina deve evitar reenvio acidental:

- chave de idempotência: `report_type + period_start + period_end + recipients_hash + whatsapp_group_jid`;
- se a chave já foi enviada com sucesso, não reenviar automaticamente;
- permitir `--force` apenas manualmente;
- se WhatsApp enviar e e-mail falhar, receipt deve marcar estado parcial e permitir retry somente do canal faltante.

## 10. Critérios de aceite

### Dados

- Consulta Supabase read-only passa sem gravar nada.
- Período calculado em timezone America/Sao_Paulo.
- Total vendido bate com soma de `valor_obra_final` das linhas filtradas.
- Vendas contam pedidos/linhas de forma documentada; se houver ambiguidade entre `pedido_id` e linha, reportar a métrica explicitamente.
- Linhas com valor nulo/zero são tratadas como alerta de qualidade, não somadas silenciosamente como venda plena.

### WhatsApp

- Grupo `[ZPR] IA Bot` identificado e validado.
- Mensagem curta, elegante e sem PII bruta.
- Envio retorna message_id/receipt.
- Não envia nada para contatos individuais.

### E-mail

- Enviado para os três destinatários exatos.
- Assunto correto.
- HTML renderizável e também parte texto/plain.
- Verificação pós-envio confirma destinatários, assunto, marker e zero secret-pattern hits.

### Cron

- Agendado segunda a sexta.
- Sem reenvio duplicado para o mesmo período.
- Falhas alertam Telegram/origem com stack sanitizado.
- Sucesso pode registrar localmente e, se necessário, mandar recibo curto apenas para Lucas.

## 11. Cron proposto

Horário sugerido:

`0 9 * * 1-5`

Prompt/job:

- Nome: `Zipper OS vendas 09h WhatsApp/email`
- Tipo: script-only ou delivery wrapper com logs sanitizados.
- Entrega de erro: Telegram/origem.
- Entrega externa: feita pelo script para WhatsApp/email aprovados.

## 12. Roadmap

### V1 — Report diário de vendas

- Supabase read-only.
- WhatsApp resumo executivo.
- E-mail HTML companion.
- Receipts e anti-duplicidade.
- Cron dias úteis.

### V1.1 — Comparativos

- D-1 vs média dos últimos 7/30 dias.
- Semana corrente vs semana anterior.
- Mês corrente vs mês anterior.
- Ranking por artista no mês.

### V1.2 — Integração Mordomo

- Se o report identificar queda, oportunidade ou venda relevante, criar sinal interno para Mordomo.
- Não criar follow-up externo automaticamente.
- Não criar draft externo sem gate explícito.

### V2 — Intelligence comercial

- Segmentos por artista/colecionador com PII minimizada.
- Conexão com conteúdo/exposições quando relevante.
- Recomendações internas de próximos contatos, sempre preview-first.

## 13. Fora de escopo

- Cobrança ou financeiro detalhado.
- Envio para clientes/colecionadores/artistas.
- Propostas comerciais.
- Follow-ups de relacionamento.
- Escrita em Supabase/CRM.
- Uso de tabelas SPITI como vendas Zipper.
- Alterar automações existentes sem aprovação.

## 14. Próximo passo de implementação

1. Fazer dry-run read-only em `vendas_tango` para os últimos 7 dias e gerar amostra local sem envio.
2. Descobrir JID do grupo `[ZPR] IA Bot` via wacli e validar conta WhatsApp autenticada.
3. Implementar generator com testes unitários de período, agregação, PII minimization e idempotência.
4. Implementar delivery layer com `--dry-run` e `--send` separado.
5. Rodar envio manual controlado de teste para o grupo/e-mails definidos, se Lucas aprovar o gate de implementação.
6. Só depois criar cron `0 9 * * 1-5`.

## 15. Decisão pendente antes de implementar

Antes de ativar o cron, confirmar:

1. horário exato: manter 09:00 BRT?
2. segunda-feira deve consolidar sexta-sábado-domingo?
3. pode omitir nomes de clientes no WhatsApp e manter e-mail também sem contato bruto no V1?
4. qual conta WhatsApp será usada para enviar ao grupo `[ZPR] IA Bot`?
