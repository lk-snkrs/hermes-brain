# Receipt — Chatwoot PÓS VENDA LK FLAGSHIP

Data: 2026-06-10
Área: LK / Atendimento / Chatwoot / Pós-venda POS

## Pedido aprovado por Lucas

Criar no Chatwoot a camada **PÓS VENDA LK FLAGSHIP** com label/sidebar, inbox/API interno se necessário, e registrar pedidos POS elegíveis como conversas/notas privadas.

Guardrail aprovado: **não enviar mensagem ao cliente por Chatwoot ainda**.

## Implementação local

Repo Chatwoot: `/opt/data/chatwoot-v4.14.1-build`

Fluxo de branches executado:

1. Branch feature criada: `lk/post-sale-flagship-chatwoot`
2. Commit feature: `de5d874 feat(lk): add post-sale flagship sidebar`
3. Merge em `dev`: `6f575c4 merge: post-sale flagship into dev`
4. Merge em `production`: `60a0fb6 merge: promote post-sale flagship to production`
5. Merge também no branch produtivo local existente `lk/whatsapp-template-builder-prod`: `daa5d32 merge: promote post-sale flagship to lk production`

Arquivos Chatwoot alterados:

- `app/javascript/dashboard/components-next/sidebar/Sidebar.vue`
- `app/javascript/dashboard/i18n/locale/en/settings.json`
- `app/javascript/dashboard/i18n/locale/pt_BR/settings.json`

Detalhe: o texto visível no sidebar é **PÓS VENDA LK FLAGSHIP**; a label interna usada na rota é `pos-venda-lk-flagship`, porque a API de labels do Chatwoot rejeitou título com espaços/acentos/maiúsculas como inválido.

## Script operacional interno

Script criado/ajustado:

- `/opt/data/scripts/lk_pos_postsale_chatwoot_layer.py`

Função:

- garantir inbox/API interno `LK Pós Venda Flagship`;
- garantir labels `pos-venda-lk-flagship`, `pos`, `shopify-pos`, `sem-envio-chatwoot`;
- criar/reusar contatos;
- criar conversas/tickets;
- adicionar nota privada com dados do pedido POS;
- aplicar labels;
- salvar estado local de idempotência.

Guardrails do script:

- mensagens ao cliente pelo Chatwoot: `0`;
- writes Shopify: `0`;
- writes Tiny: `0`;
- estoque/pronta entrega não consultado nem prometido; permanece com `lk-stock`/Tiny.

## Execução Chatwoot apply

Comando executado:

`/opt/hermes/.venv/bin/python /opt/data/scripts/lk_pos_postsale_chatwoot_layer.py --apply --days 2 --limit 10`

Resultado:

- inbox: `LK Pós Venda Flagship` / id `4` / `Channel::Api`
- labels ausentes antes do apply final: `[]`
- jobs POS elegíveis: `10`
- conversas/notas internas criadas: `10`
- mensagens ao cliente pelo Chatwoot: `0`

Pedidos registrados:

- `#147718` → conversa `500`
- `#147719` → conversa `501`
- `#147720` → conversa `502`
- `#147727` → conversa `503`
- `#147731` → conversa `504`
- `#147732` → conversa `505`
- `#147734` → conversa `506`
- `#147742` → conversa `507`
- `#147743` → conversa `508`
- `#147746` → conversa `509`

Relatório apply:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/reports/lk_pos_postsale_chatwoot_layer_20260610T154557Z_apply.json`

Readback pós-apply:

- inbox encontrada: `LK Pós Venda Flagship` id `4`
- jobs já processados: `10`
- novas escritas no readback: `0`
- mensagens ao cliente pelo Chatwoot: `0`

## Verificações

Verificação de sintaxe do script:

- `python3 -m py_compile /opt/data/scripts/lk_pos_postsale_chatwoot_layer.py` → OK

Verificação frontend direcionada em feature/dev/production/prod local:

- `pnpm exec eslint app/javascript/dashboard/components-next/sidebar/Sidebar.vue app/javascript/dashboard/i18n/locale/en/settings.json app/javascript/dashboard/i18n/locale/pt_BR/settings.json` → exit 0
- `TZ=UTC pnpm exec vitest --run --no-cache --no-coverage app/javascript/dashboard/components-next/sidebar/specs/SidebarGroupLeaf.spec.js` → `1 passed`, `4 tests passed`

Observação: tentativa inicial de lint/teste via script `pnpm eslint`/`pnpm test` acionou escopo amplo; houve timeout do teste amplo, então a verificação final válida foi a direcionada acima. Ambiente precisou de `pnpm` via `/opt/data/home/.local/bin`; Node atual `v22.12.0` emitiu warning porque o package pede Node `24.x`.

## Pedido #147746 — pós-compra 30min

Verificador final retornou:

- pedido: `#147746`
- status: `pending_delivery_confirmation`
- `send_executed`: `true`
- `external_write_executed`: `true`
- Evolution HTTP: `201`
- Evolution status: `PENDING`
- `message_id_present`: `true`

Conclusão: o envio pós-compra saiu pela Evolution/API e ficou aguardando confirmação de entrega/leitura. Não houve erro de envio no momento da checagem.
