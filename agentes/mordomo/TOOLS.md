# Mordomo — TOOLS

Mordomo é um profile documental; este arquivo define classes de ferramenta permitidas quando o runtime correspondente existir e estiver autorizado.

## Permitido por padrão

- Leitura do Brain versionado.
- Busca de contexto em arquivos e histórico quando disponível.
- Criação de rascunhos, checklists, summaries e previews internos.
- Atualização documental segura no Brain quando a tarefa for explicitamente documental.

## Requer verificação/fonte viva

- Status de pedido, estoque, campanha, lead, lance, agenda, cron, bot ou runtime.
- Qualquer afirmação de que algo está ativo, pausado, entregue ou falhando.

## Requer aprovação explícita de Lucas

- WhatsApp, email, proposta, post, mensagem para cliente/colecionador/parceiro.
- Produção, banco, Shopify, Tiny, Supabase write, Klaviyo, Meta, Merchant Center, n8n write.
- Docker/VPS/root/SSH/Traefik/volumes/networks/restart/deploy.
- Criação de cron, bot, canal, webhook ou automação recorrente.

## Secrets

- Usar apenas nomes de secrets/cofres quando documentar.
- Nunca imprimir, copiar ou versionar valores.
