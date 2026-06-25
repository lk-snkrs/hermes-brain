# Receipt — e.Rede identifier recheck e teste read-only

- Data/hora: 2026-06-24T19:48:24.441456+00:00
- Agente/profile/cron: lk-finance
- Empresa/área: LK / Finance
- Responsável humano: LK Finance
- Pedido original: Lucas corrigiu que já havia enviado API e identifier; revalidar histórico antes de pedir dado novamente.
- Classificação: infra-sensitive
- Fontes usadas:
- Histórico local/skill/cache; Doppler lc-keys/prd; e.Rede read-only wrapper; documentação pública e.Rede.
- O que foi feito:
- Identificador histórico tratado como PV/companyNumber e salvo no Doppler como REDE_EREDE_PV; helper Doppler atualizado para carregar REDE_EREDE_PV; e.Rede smoke local reexecutado; GET read-only com reference inexistente testado sem transação.
- Output/artefato:
- Secrets REDE_EREDE_TOKEN, REDE_EREDE_PV, REDE_EREDE_SANDBOX_BASE_URL e REDE_EREDE_COLLECTION_URL presentes. Smoke local pv_present=true. GET read-only retornou HTTP 401 com mensagem sanitizada Affiliation invalid parameter format/size. values_printed=false.
- Aprovação: Lucas pediu explicitamente usar as informações já enviadas; escopo limitado a secret/config e leitura GET sem transação.
- Envio/publicação: Telegram não deve exibir token, PV, Basic header, TID real, cartão, documento ou dados bancários.
- Writes externos: Write externo apenas Doppler secret REDE_EREDE_PV. Nenhum write em e.Rede/REDE transacional, Shopify, banco ou contabilidade.
- Riscos/bloqueios: e.Rede ainda não está funcionando para consulta; provável mismatch de PV/token/ambiente ou token não é par Basic e.Rede. Não declarar integração e.Rede 100% enquanto HTTP 401 persistir.
- Rollback/mitigação: Remover/rotacionar REDE_EREDE_PV no Doppler se o identifier estiver errado; manter token seguro ou rotacionar se exposto.
- Próximos passos: Confirmar no Portal Rede se o token é de e.Rede Basic e qual afiliação/PV exata associada, ou seguir conciliação de loja física por REDE Gestão de Vendas/merchant-statement.
- Onde foi documentado no Brain: Referência rede-shopify-conciliation atualizada com pitfall e status do teste.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
