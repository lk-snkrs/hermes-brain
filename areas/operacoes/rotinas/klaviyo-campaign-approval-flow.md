# Rotina — Klaviyo Campaign Approval Flow

Objetivo: separar análise/draft de campanhas LK de qualquer envio real pelo Klaviyo.

## Integração

- Doc: `empresa/integracoes/klaviyo.md`.
- Secret: `KLAVIYO_API_KEY`.
- Área principal: LK CRM/ecommerce.

## Permissões

- Read-only: listar métricas, segmentos, flows, campaigns e performance.
- Write: criar draft ou atualizar rascunho exige cuidado e descrição clara.
- External-send: enviar campanha, ativar flow ou disparar email/SMS exige preview e aprovação Lucas.
- Admin/destructive: billing, integrações, suppression list, deletes e permissões exigem aprovação explícita.

## Fluxo recomendado

1. Ler objetivo de negócio e segmento.
2. Consultar métricas/segmentos read-only.
3. Produzir proposta: público, assunto, corpo, oferta, timing e risco.
4. Criar preview textual para Lucas.
5. Aguardar aprovação antes de criar/ativar/disparar.
6. Após envio aprovado, registrar resultado e linkar learning.

## Verificação

- Confirmar que nenhuma ação `send`, `schedule`, `activate` ou equivalente foi executada sem aprovação.
- Registrar fonte dos dados usados para segmentação.
