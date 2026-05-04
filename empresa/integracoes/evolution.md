# Integração — Evolution API / WhatsApp

## Escopo

Evolution API opera instâncias WhatsApp usadas por LK, Zipper, SPITI e Lucas. WhatsApp é canal externo sensível.

## Secrets Doppler

- `EVOLUTION_API_URL`
- `EVOLUTION_API_KEY`

## Instâncias documentadas

- Clo: LK + pessoal.
- SPITI: recepção/uso SPITI.
- Pessoal: Lucas pessoal.
- ZipperGaleria: Zipper Galeria.

## Read-only

- Listar instâncias e status de conexão.
- Conferir webhooks, filas e saúde da API sem ler conteúdo sensível além do necessário.

## Write

- Ajustes técnicos não destrutivos em metadados/labels apenas quando documentados.

## External-send

- Enviar WhatsApp, disparos, follow-ups, mensagens para leads/clientes/coletadores exige preview e aprovação explícita de Lucas.
- Para envios em lote, incluir amostra, público, volume, janela, opt-out e plano de parada.

## Admin/destructive

- Recriar instância, alterar webhook, resetar sessão, desconectar número, trocar API key ou mexer em infraestrutura exige aprovação e rollback.

## Observações

- Links em caption de imagem não são clicáveis; enviar URL como texto separado quando aprovado.
- Respeitar limites e reputação do número.

## Escala de permissões

- Read-only: consultar metadados, status, listas, métricas e registros sem alterar dados.
- Write: criar/atualizar dados internos, tags, notas, segmentos ou configurações não destrutivas.
- External-send: enviar mensagem, email, campanha, notificação ou contato com cliente/lead/parceiro. Exige preview e aprovação de Lucas.
- Admin/destructive: apagar dados, alterar credenciais, webhooks, domínios, billing, permissões, deploys, containers, produção ou integrações críticas. Exige aprovação explícita, plano de backup e rollback.

Regra de secrets: este arquivo lista apenas nomes de secrets no Doppler `lc-keys/prd`; valores reais nunca entram no GitHub.
