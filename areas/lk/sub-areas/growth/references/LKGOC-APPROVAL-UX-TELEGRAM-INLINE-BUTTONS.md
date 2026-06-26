# LKGOC — Approval UX no Telegram com botões inline

Registrado: 2026-06-05T09:31:08Z
Origem: feedback Lucas no LKGOC New Balance 9060 Full.

## Regra

Quando o agente precisar de aprovação de Lucas para etapa LKGOC/Shopify/theme/produção, **não deve pedir para Lucas escrever manualmente “aprovo” como caminho principal**.

Preferir enviar aprovação com **botões inline** no Telegram, quando a plataforma/ferramenta do profile permitir.

## Padrão de botões

- `✅ Aprovar DEV preview`
- `🔎 Ver pacote`
- `⛔ Segurar`

Para produção:

- `✅ Aprovar merge DEV → Production`
- `↩️ Rollback / não publicar`
- `🔎 Ver evidências`

## Fallback

Se o runtime/canal atual não permitir botões inline, declarar isso brevemente e aceitar aprovação textual escopada, mas registrar que o ideal é inline.

## Aplicação

Vale para:

- approval packet LKGOC;
- Shopify DEV preview;
- merge DEV → Production;
- alterações de tema;
- SEO fields/descrições públicas;
- GMC/feed/campanhas/Klaviyo quando houver approval.

## Não fazer

- Não encerrar a execução pedindo “me escreva aprovo” se botões inline estiverem disponíveis.
- Não usar botão genérico sem escopo. O botão precisa explicitar o que está sendo aprovado.
