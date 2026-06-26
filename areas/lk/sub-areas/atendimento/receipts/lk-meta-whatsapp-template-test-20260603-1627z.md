# LK Meta WhatsApp — template real de teste

Data: 2026-06-03 16:27 UTC
Status: `submitted_to_meta_pending_review`

## Aprovação

Lucas aprovou explicitamente: criar 1 template real de teste na Meta para aprovação, sem enviar WhatsApp.

## Descoberta operacional

- Chatwoot produção customizado está online, mas ainda não há inbox `Channel::Whatsapp` configurado no Chatwoot.
- Inboxes Chatwoot encontrados no momento: apenas `Channel::Api` (`Shopify Carrinho Abandonado`).
- Portanto, a criação foi feita diretamente via Meta Graph API usando credencial autorizada em Doppler, não pela UI do Chatwoot.
- Nenhum secret/token foi registrado no Brain ou resposta.

## WABA usado

- Business: `LK Sneakers & Streetwear` (`343191257771041`)
- WABA escolhido: `1478026007140488` — `LK Sneakers & Apparels`
- Motivo: WABA aprovado, associado ao número storefront `+55 11 94956-5000` e já contém templates LK de carrinho/checkout aprovados.

## Template criado

- Nome: `lk_teste_chatwoot_builder_20260603`
- Categoria: `MARKETING`
- Idioma: `pt_BR`
- Meta Template ID: `1930178777664845`
- Status Meta: `PENDING`
- Rejected reason: `NONE`

Body submetido:

```text
Oi {{1}}, este é um teste interno da LK Sneakers para validar a criação de template no WhatsApp Business. Nenhuma ação é necessária.
```

Exemplo de variável:

```text
Lucas
```

Footer:

```text
LK Sneakers
```

## Segurança / não feito

- Nenhuma mensagem WhatsApp foi enviada.
- Nenhuma campanha foi criada.
- Nenhuma feature flag Chatwoot foi alterada.
- Nenhum contato foi importado.
- Nenhum token/secret foi exposto.

## Próximo passo

Aguardar revisão da Meta. Quando o status virar `APPROVED`, o template poderá ser usado em teste interno controlado, se Lucas aprovar explicitamente o envio para 1 número interno.
