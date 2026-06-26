# Receipt — correção tentativa de imagem no checkout abandonado WhatsApp LK

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp / Meta / n8n

## Input de Lucas

Lucas confirmou recebimento às 07:00 sem imagem e pediu correção.

## Diagnóstico

1. Screenshot confirma mensagem recebida sem header/image, apenas card textual com domínio `lksneakers.com.br`, texto do template e botão `Voltar ao checkout`.
2. `wacli` confirmou mensagens recebidas sem mídia (`media_type` vazio / `has_media=false`).
3. Teste via Crisp com `lk_checkout_abandonado_30min_v3` + `HEADER IMAGE` + `crisp_options.as=text` retornou HTTP 200 / `request_accepted`, mas a entrega visível continuou sem mídia.
4. Teste via Crisp com imagem por `media_id` WhatsApp também retornou `request_accepted`, sem validação de mídia no espelho.
5. Teste direto Meta Cloud API com `lk_checkout_abandonado_30min_v3` e `lk_checkout_abandonado_img_fix_1` retornou erro `#132001 Template name does not exist in pt_BR` para o Phone ID operacional, apesar desses templates aparecerem aprovados na WABA `1478026007140488`.
6. O template `lk_checkout_abandonado_30min_v2` sem imagem foi aceito pelo Phone ID operacional, explicando por que a mensagem sem imagem chegou.

## Correção aplicada

Criado template com imagem também na rota/WABA que o endpoint operacional/Zoppy efetivamente reconhece:

- WABA compatibilidade operacional: `2510782939372375`
- App detectado do token: `ZOPPY`
- Template criado: `lk_checkout_abandonado_img_fix_2`
- ID Meta: `1520904086096395`
- Categoria: `MARKETING`
- Idioma: `pt_BR`
- Status final após polling: `APPROVED`
- Componentes: `HEADER IMAGE`, `BODY`, `BUTTONS`

Workflow n8n atualizado, mantendo inativo:

- Workflow ID: `kWQbmEMuvdipcGjd`
- Status: `active=false`
- Node: `Crisp Send lk_checkout_abandonado_img_fix_2`
- Template no workflow: `lk_checkout_abandonado_img_fix_2`
- Payload mantém `HEADER IMAGE` dinâmico via `{{$json.productImage}}`
- Payload mantém `crisp_options: { "as": "text" }`

## Testes pós-correção

- Crisp `lk_checkout_abandonado_img_fix_2` com imagem por link: HTTP 200 / `request_accepted`, request_id `d54dc413-ccc4-40c5-afe1-6d1fe99dcb4f`.
- Meta direto `lk_checkout_abandonado_img_fix_2` com `media_id`: HTTP 200 / `message_status=accepted`.
- `wacli` após janela curta ainda não mostrou mensagem com mídia (`has_media=false` nas mensagens visíveis). Pode haver retenção/frequency cap/filtragem assíncrona por repetição de marketing template para o mesmo número.

## Estado seguro

- Produção não ativada.
- Workflow continua `active=false`.
- Nenhum cliente impactado.
- Sem cupom/desconto.

## Backup / rollback

Backups brutos salvos em diretório restrito:

- `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-fix-v3-image-as-text-20260520T100811.json`
- `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-fix-img-fix-2-20260520T101657.json`

Rollback: reimportar backup desejado via n8n API/UI e confirmar `active=false`.

## Conclusão operacional

A configuração agora aponta para um template de imagem aprovado no caminho operacional que o Phone ID reconhece. Porém a renderização de imagem ainda não foi confirmada no WhatsApp; não ativar produção até Lucas confirmar recebimento com imagem ou até obter receipt real do provider/Zoppy/Crisp.
