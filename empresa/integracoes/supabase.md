# Integração — Supabase

## Escopo

Supabase guarda bases analíticas e operacionais de LK, Zipper Vendas e SPITI/Zipper CRM. Separar rigorosamente cada projeto.

## Projetos e secrets Doppler

### LK Sneakers

- Project ID: `cnjimxglpktznenpbail`
- Secrets: `SUPABASE_LK_URL`, `SUPABASE_LK_SERVICE_KEY`
- Uso: clientes, pedidos, analytics, RFM e rotinas LK.

### Zipper Vendas

- Project ID: `pcstqxpdzibheuopjkas`
- Secrets: `SUPABASE_ZIPPER_VENDAS_URL`, `SUPABASE_ZIPPER_VENDAS_SERVICE_KEY`
- Uso: vendas reais de obras, especialmente `vendas_tango`.

### SPITI / Zipper CRM

- Project ID: `rmdugdkantdydivgnimb`
- Secrets: `SUPABASE_SPITI_URL`, `SUPABASE_SPITI_SERVICE_KEY`
- Uso: SPITI Auction, lances, contatos e CRM associado. Email continua fonte de verdade para totais de lance.

## Read-only

- Consultar tabelas com `select`, filtros e limites.
- Gerar relatórios, validações, segmentações e auditorias de consistência.
- Conferir schemas e contagens.

## Write

- Inserir logs, resultados de rotina, classificações internas e campos derivados quando o processo estiver documentado.
- Atualizações em registros de cliente/lance/venda só com fonte clara e escopo pequeno.

## External-send

- Supabase não deve enviar mensagens diretamente; se dados forem usados para WhatsApp/email/campanhas, a etapa de envio exige preview Lucas.

## Admin/destructive

- Migrations, RLS, service keys, policies, deletes, truncates, schema changes, funções, webhooks e alterações em produção exigem aprovação explícita + backup/rollback.

## Regras críticas

- Não misturar Zipper Vendas (`pcstqxpdzibheuopjkas`) com SPITI/Zipper CRM (`rmdugdkantdydivgnimb`).
- Para SPITI, silêncio > dado errado; confirmar email antes de afirmar total de lance.

## Escala de permissões

- Read-only: consultar metadados, status, listas, métricas e registros sem alterar dados.
- Write: criar/atualizar dados internos, tags, notas, segmentos ou configurações não destrutivas.
- External-send: enviar mensagem, email, campanha, notificação ou contato com cliente/lead/parceiro. Exige preview e aprovação de Lucas.
- Admin/destructive: apagar dados, alterar credenciais, webhooks, domínios, billing, permissões, deploys, containers, produção ou integrações críticas. Exige aprovação explícita, plano de backup e rollback.

Regra de secrets: este arquivo lista apenas nomes de secrets no Doppler `lc-keys/prd`; valores reais nunca entram no GitHub.
