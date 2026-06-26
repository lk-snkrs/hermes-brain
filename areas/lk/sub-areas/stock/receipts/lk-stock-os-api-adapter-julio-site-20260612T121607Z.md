# Receipt — API adapter Stock OS para site do Júlio

- Data/hora: 2026-06-12T12:16:31.635255+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK/Stock
- Responsável humano: Hermes lk-stock
- Pedido original: Fazer opção A: API/adapter read-only para o site do Júlio consumir nossa Stock OS DB em vez da database dele/Tiny direto.
- Classificação: local-write
- Fontes usadas:
- Stock OS pointer lk_stock_os_current_pointer.json; SQLite current_local_stock; testes unittest; smoke HTTP local
- O que foi feito:
- Criado adapter dependency-free lk_stock_api_adapter.py com /health e /lookup; criado teste TDD test_stock_api_adapter.py; criado guia de integração para Júlio; smoke CLI e HTTP validaram contrato confirmado/não_confirmado.
- Output/artefato:
- areas/lk/sub-areas/stock/scripts/lk_stock_api_adapter.py; areas/lk/sub-areas/stock/evaluation/test_stock_api_adapter.py; areas/lk/sub-areas/stock/references/lk-stock-os-api-adapter-julio-site-20260612.md
- Aprovação: Aprovado por Lucas ao escolher Fazer o A. Sem deploy público/runtime produtivo ainda.
- Envio/publicação: Telegram resumo para Lucas; nenhum contato externo com Júlio executado.
- Writes externos: 0
- Riscos/bloqueios: Serviço ainda local; para uso pelo site precisa definir hospedagem/rede/token. public_availability_safe e availability_claim_allowed permanecem 0.
- Rollback/mitigação: Parar processo HTTP se estiver rodando; remover/ignorar adapter e voltar a consultar via CLI lk_stock_lookup_current.py; nenhum sistema externo foi alterado.
- Próximos passos: Receber repo/ambiente do site do Júlio ou decidir onde hospedar o adapter; configurar token interno e trocar fonte do site para /api/lk-stock/lookup.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/references/lk-stock-os-api-adapter-julio-site-20260612.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
