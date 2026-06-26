# Integração — Judge.me Reviews

Status: `mapped_pending_readonly_inventory`
Área: LK Sneakers / Customer Trust & Loyalty / Reviews
Última atualização: 2026-05-13

## Papel no LK OS

Judge.me deve entrar como fonte de prova social e confiança para PDP/CRO, CRM/Klaviyo, atendimento/reputação e ranking de produtos.

## Fonte de dados

- `fact_judgeme_review`: dados confirmados pelo Judge.me, como rating, texto/status da review, produto associado e timestamps.
- `derived_review_cro`: cruzamentos Shopify/GA4/Judge.me para priorizar PDPs, produtos campeões sem review e prova social.
- `manual_approval`: decisão humana de responder, remover, moderar ou usar review em comunicação.

## Regras confirmadas por Lucas

- Reviews publicam automaticamente.
- Lucas deleta reviews ruins manualmente.
- Lucas responde pessoalmente reviews negativas.
- Review request deveria sair pelo Klaviyo, mas Lucas suspeita que não está bem configurado.
- Reviews devem alimentar todas as frentes, por fase:
  1. PDP/CRO;
  2. CRM/Klaviyo;
  3. atendimento/reputação;
  4. ranking de produtos.

## Credenciais / nomes seguros

Verificação Doppler `lc-keys/prd` em 2026-05-13, sem imprimir valores:

- `JUDGEME_API_TOKEN` — existe.
- `JUDGEME_PRIVATE_TOKEN` — existe.
- Relacionados para auditoria de review request: `KLAVIYO_API_KEY`, `KLAVIYO_CONNECTION_ID`, `KLAVIYO_PUBLIC_KEY` — existem.

Não registrar valores neste arquivo.

## Inventário read-only necessário

1. Confirmar shop domain/identificação usada pelo Judge.me.
2. Listar endpoints disponíveis para reviews, products, review requests e settings sem puxar PII desnecessária.
3. Snapshot agregado:
   - total de reviews;
   - rating médio;
   - reviews recentes;
   - reviews 1–3 estrelas;
   - produtos sem reviews;
   - produtos campeões com pouca prova social;
   - produtos com rating forte para destacar.
4. Auditar se review request atual é Judge.me nativo, Klaviyo, Shopify ou combinação.
5. Verificar risco de duplicidade de solicitações se Judge.me e Klaviyo estiverem ativos ao mesmo tempo.

## Guardrails

Sem aprovação explícita de Lucas, Hermes não deve:

- responder review;
- publicar/despublicar review;
- deletar/moderar review;
- alterar template de review request;
- disparar e-mail/SMS/WhatsApp;
- alterar widget/tema Shopify;
- escrever em Judge.me/Klaviyo/Shopify/Notion/Supabase.

## Primeiros artefatos seguros

- Diagnóstico read-only de reviews.
- Fila de PDPs sem prova social suficiente.
- Fila interna de reviews negativas/recentes para atendimento humano, sem resposta automática.
- Preview de review request premium via Klaviyo, sem envio.
