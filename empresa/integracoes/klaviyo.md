# Integração — Klaviyo

## Escopo

Klaviyo gerencia email marketing/CRM da LK, listas, segmentos e campanhas.

## Secrets Doppler

- `KLAVIYO_API_KEY`

## Read-only

- Consultar perfis, listas, segmentos, métricas agregadas, campanhas e eventos.
- Analisar performance de públicos e hipóteses de CRM.

## Write

- Criar segmentos, tags/propriedades e drafts quando a intenção estiver documentada.
- Atualizar perfis em lote exige escopo pequeno e verificação.

## External-send

- Enviar campanha, flow, email, SMS ou qualquer comunicação para clientes exige preview Lucas, assunto, público, amostra e horário.

## Admin/destructive

- Alterar flows ativos, listas centrais, consentimento, integrações, API keys ou deletes exige aprovação explícita e rollback.

## Regra

- Nunca sacrificar reputação de envio; começar por consulta/draft/preview.

## Escala de permissões

- Read-only: consultar metadados, status, listas, métricas e registros sem alterar dados.
- Write: criar/atualizar dados internos, tags, notas, segmentos ou configurações não destrutivas.
- External-send: enviar mensagem, email, campanha, notificação ou contato com cliente/lead/parceiro. Exige preview e aprovação de Lucas.
- Admin/destructive: apagar dados, alterar credenciais, webhooks, domínios, billing, permissões, deploys, containers, produção ou integrações críticas. Exige aprovação explícita, plano de backup e rollback.

Regra de secrets: este arquivo lista apenas nomes de secrets no Doppler `lc-keys/prd`; valores reais nunca entram no GitHub.
