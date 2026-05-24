# Zipper Mordomo — Integração Tidio para leads do site

Atualizado: 2026-05-18

## Objetivo

Automatizar a ingestão dos leads que hoje Lucas cola manualmente como blocos `!enviar`, lendo diretamente conversas/contatos do Tidio quando possível.

## Fonte

Lucas confirmou que grande parte dos leads da Zipper vem do Tidio. No fluxo comercial do Mordomo, a origem normalizada desses leads deve ser:

- `Site - Tidio`

Manter também a origem raw quando disponível, por exemplo:

- `Flow: ZPR Chatbot | ZPRALL`
- IDs/propriedades de contato/conversa do Tidio

## Documentação Tidio verificada

Docs: `https://developers.tidio.com/`

OpenAPI:

- Endpoints de `Contacts`.
- Endpoint de `Conversations / Get contact messages`.
- Autenticação por dois headers:
  - `X-Tidio-Openapi-Client-Id` — começa com `ci_`.
  - `X-Tidio-Openapi-Client-Secret` — começa com `cs_`.
- API keys são geradas no painel Tidio em `Developer > OpenAPI`.
- Acesso ao OpenAPI exige usuário owner/admin e plano Plus/Premium para endpoints além de produtos/Lyro.

Webhooks:

- Configuração em `Settings > Developer > Webhooks`.
- Exige plano Plus/Premium.
- Melhor caminho para automação em tempo real: novo contato/mensagem/evento dispara endpoint Hermes.

## Tentativa de acesso ao painel

Lucas forneceu credencial do painel Tidio por Telegram. Por segurança:

- a senha não foi repetida nem persistida em Brain;
- não foi salva em Doppler nesta etapa;
- recomenda-se rotação posterior porque foi compartilhada em chat.

Resultado técnico:

- Login pelo browser Hermes abriu a tela Tidio.
- Ao submeter login, a página informou: `Your browser is blocking the reCAPTCHA script`.
- Navegação direta para `app.tidio.com/login` retornou `HTTP 403` no ambiente browser atual.
- Portanto, não foi possível gerar API key no painel a partir deste ambiente.

## Caminho recomendado

### Caminho A — Lucas gera API key no painel

1. Entrar no Tidio manualmente.
2. Ir em `Developer > OpenAPI`.
3. Gerar par de chaves.
4. Salvar em Doppler `lc-keys/prd` como:
   - `TIDIO_ZIPPER_CLIENT_ID`
   - `TIDIO_ZIPPER_CLIENT_SECRET`
5. Hermes testa em modo read-only:
   - listar contatos recentes;
   - puxar mensagens de contato;
   - comparar com blocos `!enviar` conhecidos.

### Caminho B — Lucas configura Webhook

1. Criar endpoint Hermes público/seguro para receber eventos Tidio.
2. No Tidio: `Settings > Developer > Webhooks`.
3. Criar stack apontando para endpoint Hermes.
4. Habilitar eventos de contato/mensagem/conversa relevantes.
5. Hermes valida assinatura do webhook, persiste evento bruto em área segura e normaliza para Supabase.

## Fluxo alvo

1. Tidio recebe lead do site.
2. Hermes ingere conversa/contato via API ou webhook.
3. Extrai artista, nome, sobrenome, email, WhatsApp, intenção.
4. Origem normalizada: `Site - Tidio`.
5. Verifica PDF validado em `artist_pdfs`.
6. Aplica guardrails: negativo/desfit, artista ambígua, PDF ausente.
7. Para fluxo aprovado, envia WhatsApp + e-mail e registra em CRM.
8. Pós-resposta cordial: subfluxo automático aprovado, falando apenas em `condições de pagamento`.
9. Follow-up em 2 dias se não houver resposta relevante.

## Guardrails

- Não enviar mensagens externas fora dos subfluxos explicitamente aprovados.
- Não armazenar PII no Brain; PII pertence a Supabase/Tidio/Gmail/WhatsApp autorizados.
- Não salvar senha de painel em arquivos locais/Brain.
- Preferir API key dedicada em Doppler em vez de senha de usuário.
- Se houver negociação, desconto, reserva, objeção de preço/desfit ou pergunta específica sobre obra, enviar para Lucas aprovar.
