# Receipt — Solicitação REDE merchant-statement criada/confirmada

- Data/hora: 2026-06-24T20:32:34.637657+00:00
- Agente/profile/cron: lk-finance
- Empresa/área: LK / Finance
- Responsável humano: LK Finance
- Pedido original: Lucas aprovou criar solicitação REDE merchant-statement read-only para habilitar match da loja física com REDE e Itaú.
- Classificação: infra-sensitive
- Fontes usadas:
- REDE Gestão de Acessos sandbox API; Doppler lc-keys/prd; scripts rede_access_request.py e rede_client.py.
- O que foi feito:
- Executado POST de solicitação merchant-statement com permissão de leitura; API retornou 409 indicando solicitação já enviada anteriormente com requestId; consulta GET do requestId retornou HTTP 200 com feature MERCHANT-STATEMENT, permission LEITURA, status APROVADO.
- Output/artefato:
- RequestId e35ff829-d3dd-4fca-a7c2-e7be5fb30e6d; status APROVADO; requestType TOTAL; permission LEITURA; created/update 2026-06-24 20:32:05. Teste subsequente de sales com PV LK no sandbox ainda retornou HTTP 400 scenario not available in sandbox. values_printed=false.
- Aprovação: Lucas escreveu Pode criar. Escopo executado: criar/confirmar solicitação read-only merchant-statement; sem pagamentos, transações, capturas ou cancelamentos.
- Envio/publicação: Não expor ClientSecret, token Bearer, headers, PV/CNPJ completos, dados bancários ou PII.
- Writes externos: Write externo REDE Gestão de Acessos POST executado; resposta indicou conflito por solicitação existente, não duplicada. Readback GET executado.
- Riscos/bloqueios: A aprovação observada é no ambiente/base sandbox atualmente configurado; dados reais da loja física ainda não apareceram, pois sales com PV LK segue indisponível no sandbox. Produção ainda precisa endpoint/credencial produtiva válida ou confirmação de que o Portal Rede vinculou o projeto produtivo.
- Rollback/mitigação: Se necessário, cancelar solicitação pendente via PUT cancel; porém status APROVADO não é pendente, então rollback operacional passa por Portal REDE/suporte. Nenhum dado de venda alterado.
- Próximos passos: Verificar no Portal REDE se o acesso merchant-statement do projeto/PV está ativo em produção; obter base/token produtivo correto e rodar match REDE↔Shopify↔Itaú novamente.
- Onde foi documentado no Brain: Receipt criado; manter referência de que solicitação read-only existe/aprovada mas sandbox não entrega dados reais da LK.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
