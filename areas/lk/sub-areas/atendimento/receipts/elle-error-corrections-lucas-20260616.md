# Elle — correções aprovadas por Lucas sobre erros da auditoria

Data: 2026-06-16
Perfil: lk-ops
Classificação: produção local Elle/Chatwoot; sem impressão de segredos

## Pedido
Lucas aprovou corrigir os erros apontados na auditoria das últimas 24h com as seguintes regras:

1. Corrigir prioridade de contexto para não responder catálogo quando o histórico recente é pedido/prazo/entrega/rastreio.
2. Pergunta de originalidade/autenticidade deve responder apenas: “Sim, trabalhamos apenas com produtos originais.”
3. Comparação/diferença entre produtos deve transferir para Larissa.
4. Não existe desconto no Pix; cupom ELLE5 dá 5% tanto no Pix quanto no cartão de crédito.
5. Corrigir repetição/reintrodução.
6. Em respostas de produto/site, manter transparência de que a Elle é uma IA em treinamento enquanto ainda erra muito.
7. Elle deve sempre tentar responder a dúvida da pessoa diretamente; evitar copy condicional tipo “se for sobre boleto/pagamento, chamo a Larissa...”.

## Ações executadas

- Patch aplicado em `/app/app.py` do container `elle-chatwoot`.
- Backup do app anterior salvo em `/opt/data/backups/elle-chatwoot/20260616T183936Z/app.py.before`.
- Imagem anterior tagueada como rollback: `elle-chatwoot-elle-chatwoot:rollback-20260616T183936Z`.
- Container validado com `python -m py_compile /app/app.py` antes do restart.
- Container reiniciado para carregar o patch.
- Container commitado na imagem usada pelo serviço: `elle-chatwoot-elle-chatwoot:latest`.

## Verificação sanitizada

Health interno após restart retornou OK:

- ok: true
- dry_run: false
- write_enabled: true
- kill_switch: false
- public_reply_enabled: true
- ai_enabled: true
- ai_provider: openrouter
- debounce_enabled: true
- observer_enabled: true

Testes locais de classificação, sem envio externo:

- “Esse tênis é original?” → `institutional`, sem handoff, resposta exata: “Sim, trabalhamos apenas com produtos originais.”
- “qual a diferença entre o nb 9060 preto e branco?” → `human_handoff`, transfere para Larissa.
- “tem desconto no pix? posso usar cupom?” → `coupon`, resposta: não tem desconto no Pix; ELLE5 dá 5% no Pix e cartão de crédito.
- Histórico recente de pedido + link de produto → não responde catálogo; pede número do pedido ou transfere conforme contexto.

## Não feito

- Nenhum segredo impresso.
- Nenhuma alteração em Shopify, Tiny, Meta, Klaviyo ou estoque.
- Nenhum retry de mensagem antiga.
