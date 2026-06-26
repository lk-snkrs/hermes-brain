# LK Shopify — token recebido, ativação bloqueada pelo runtime guardrail

Data: 2026-05-26
Status: runtime_guardrail_blocked_secret_profile_activation

## Pedido limpo

Lucas pediu concluir a ativação do `@LKShopify_HermesBot` usando o token recém-enviado.

## Importante

O token foi tratado como segredo. Não deve ser copiado para docs, logs, relatórios ou respostas.

## Tentativa de execução

Foram tentadas as etapas aprovadas:

1. Gravar o token apenas no `.env` do profile `/opt/data/profiles/lk-shopify`.
2. Manter API server e webhook desativados no profile.
3. Validar o bot com `getMe` sem imprimir o token.
4. Salvar o segredo no Doppler como `TELEGRAM_LK_SHOPIFY_BOT_TOKEN`.
5. Subir gateway isolado do profile.

## Resultado

O runtime guardrail bloqueou terminal/execute_code para ações de secrets/profile activation nesta rota, apesar da aprovação textual do Lucas.

Nada foi executado após o bloqueio:

- token não foi gravado no `.env`;
- token não foi gravado no Doppler;
- gateway não foi iniciado;
- main Hermes não foi alterado;
- Shopify/GMC/Klaviyo/ads não foram tocados.

## Estado preservado

- Profile `lk-shopify` existe, preparado e parado.
- Main Hermes continua preservado.
- LK Growth continua preservado.

## Próximo passo

Executar a ativação a partir de um runtime/canal sem bloqueio de secrets/profile operations, ou ajustar o guardrail para reconhecer aprovação explícita contendo `Fazer` + token + escopo limitado.
