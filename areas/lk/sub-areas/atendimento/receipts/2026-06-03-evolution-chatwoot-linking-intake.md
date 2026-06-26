# Intake — Evolution API Railway + Chatwoot

Data: 2026-06-03

## Pedido
Lucas perguntou se o Hermes LK Ops tem acesso à Evolution API hospedada no Railway e se consegue linkar Evolution API + Chatwoot sozinho.

## Verificação read-only feita
- `doppler` CLI não está instalado neste runtime.
- Helper local `/opt/data/hermes_bruno_ingest/hermes_doppler.sh` existe, mas depende do Doppler CLI e não conseguiu listar nomes.
- `railway` CLI não está instalado.
- Não há variáveis de ambiente visíveis com nomes `CHATWOOT`, `EVOLUTION` ou `RAILWAY`.

## Status
Sem acesso direto confirmado neste runtime para Railway/Evolution/Chatwoot via credenciais já carregadas.

## Guardrails
- Integração Evolution API ↔ Chatwoot é mudança externa/produção/WhatsApp: requer aprovação explícita de Lucas com escopo.
- Não imprimir nem salvar tokens/chaves em receipts ou chat.

## Próximos dados necessários
- URL/base da Evolution API no Railway.
- API key/token da Evolution API ou secret name no Doppler.
- Domínio do Chatwoot, account_id e user API access token ou secret name no Doppler.
- Nome/instância do WhatsApp a conectar.
- Confirmação do escopo: criar inbox, configurar webhook/integração, testar inbound apenas, sem envio ativo automático.
