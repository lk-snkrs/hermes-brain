# Receipt — Elle Chatwoot product_clear guard for Antonio Gabriel conversation

- Data/hora: 2026-06-15 12:09 BRT
- Escopo: LK WhatsApp / Chatwoot conversation `#1937`, contato Antonio Gabriel, telefone sanitizado `***2212`.
- Tipo: correção emergencial de atendimento/Elle.

## Evidência lida

Conversa `#1937` no Chatwoot mostrou sequência rápida:

1. Cliente perguntou disponibilidade/tamanho do Onitsuka Tiger Mexico 66 Kill Bill amarelo, tamanho 36.
2. Elle respondeu como `product_clear` em poucos segundos, orientando selecionar numeração/finalizar pelo site.
3. Cliente perguntou loja física.
4. Elle fez handoff Larissa/estoque.
5. Depois houve resposta humana, e Elle ficou bloqueada por `human_takeover_lock` como esperado.

Logs da Elle confirmaram:

- `message_id=41585`: `category=product_clear`, `handoff=false`, `public_reply=200`.
- `message_id=41590`: `category=product_clear`, `handoff=false`, `public_reply=200`.
- `message_id=41593`: `category=stock_handoff`, `handoff=true`, `public_reply=200`, assignment para Giselia.

## Causa operacional

- O motor público estava liberando `product_clear` para perguntas de produto/tamanho com contexto ainda em formação.
- A resposta saía muito rápido em sequência multi-mensagem.
- Embora o handoff de loja física tenha funcionado depois, a conversa já tinha recebido respostas automáticas repetidas e com fricção comercial.

## Correção aplicada

Patch emergencial em `/app/app.py` do container `elle-chatwoot`:

- Pausar resposta pública de `product_clear`.
- Manter observação/labels/handoff humano ativo.
- Converter `product_clear` para `handoff=true`, `reply=''`, bloqueio `product_clear_public_reply_paused_context_guard`.
- Não alterar `stock_handoff`: perguntas de loja física/pronta entrega continuam podendo receber o texto Larissa e abrir/atribuir humano.

## Backup / rollback

- Backup host: `/opt/data/backups/elle-chatwoot-product-guard-*/app.py.before` e `app.py.after`.
- Backup container/mount: `/data/backups/product-guard-20260615/app.py.before`.
- Rollback: copiar `app.py.before` de volta para `/app/app.py` no container e reiniciar `elle-chatwoot`.

## Verificação

- `python -m py_compile` OK antes e depois do copy para o container.
- Container `elle-chatwoot` reiniciado e ficou `Up`.
- Health readback: `ok=true`, `dry_run=false`, `write_enabled=true`, `kill_switch=false`, `public_reply_enabled=true`, `ai_enabled=true`, `observer_enabled=true`; valores sensíveis não impressos.
- Smoke sintético pós-patch:
  - Produto/tamanho: `category=product_clear`, `handoff=true`, `reply_allowed=false`, bloqueio `product_clear_public_reply_paused_context_guard`.
  - Loja física: `category=stock_handoff`, `handoff=true`, `reply_allowed=true` com copy Larissa.

## Não feito

- Não consultei estoque/Tiny/Shopify para disponibilidade; isso segue sendo dono do `lk-stock`.
- Não mandei mensagem corretiva ao cliente.
- Não alterei Chatwoot/Tiny/Shopify além do runtime do container Elle.

## Próximo ajuste recomendado

Implementar versão definitiva com debounce/fila curta e uso obrigatório de janela de conversa antes de qualquer resposta pública de produto, para voltar a liberar `product_clear` com segurança.
