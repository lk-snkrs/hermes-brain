# Integração — Analytics / GA4 / GSC

## Escopo

Analytics cobre GA4, Google Search Console e métricas de tráfego/performance usadas por LK e Zipper.

## Secrets / IDs Doppler

- `GA4_LK_PROPERTY_ID`
- `GA4_ZIPPER_PROPERTY_ID`
- credenciais Google/Workspace quando documentadas no Doppler.

## Read-only

- Consultar sessões, eventos, conversões, origem/mídia, landing pages, termos e tendências.
- Gerar relatórios comparativos e insights sem alterar propriedades.

## Write

- Criar notas internas no Brain e relatórios.
- Alterar configuração de GA4/GSC não é write rotineiro; tratar como admin.

## External-send

- Relatórios enviados a terceiros ou clientes externos exigem revisão.

## Admin/destructive

- Alterar propriedades, permissões, tags, conversões, data streams, Search Console ou GTM exige aprovação explícita.

## Regra

- Não inventar métricas; se não consultar fonte viva, marcar como hipótese/pendência.

## Escala de permissões

- Read-only: consultar metadados, status, listas, métricas e registros sem alterar dados.
- Write: criar/atualizar dados internos, tags, notas, segmentos ou configurações não destrutivas.
- External-send: enviar mensagem, email, campanha, notificação ou contato com cliente/lead/parceiro. Exige preview e aprovação de Lucas.
- Admin/destructive: apagar dados, alterar credenciais, webhooks, domínios, billing, permissões, deploys, containers, produção ou integrações críticas. Exige aprovação explícita, plano de backup e rollback.

Regra de secrets: este arquivo lista apenas nomes de secrets no Doppler `lc-keys/prd`; valores reais nunca entram no GitHub.
