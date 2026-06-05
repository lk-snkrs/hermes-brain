# LKGOC — padrão de envio de screenshots no QA

Registrado em: 20260604T181834Z
Origem: pedido do Lucas no Telegram — "Me manda o screenshot aqui sempre, anote como padrão".

## Padrão operacional
Sempre que for feito QA visual de LKGOC/tema Shopify/collections com screenshot gerado localmente:

- enviar o screenshot no próprio Telegram usando `MEDIA:/caminho/absoluto/do/arquivo`;
- não apenas informar o caminho local;
- manter no resumo curto: página, viewport, tema/preview e produção intocada;
- se houver desktop e mobile, enviar ambos quando relevantes;
- se screenshot não existir ou falhar, avisar explicitamente e regenerar antes de finalizar quando possível.

## Guardrail
Continua obrigatório: DEV/unpublished → QA visual/readback → approval Lucas → merge/promoção para Production. Produção não deve ser alterada para gerar screenshot.
