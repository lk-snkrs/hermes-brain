# Receipt — Coleção Itaú/REDE Sandbox Gestão-Vendas revisada

- Data/hora: 2026-06-24T20:17:45.519747+00:00
- Agente/profile/cron: lk-finance
- Empresa/área: LK / Finance
- Responsável humano: LK Finance
- Pedido original: Lucas enviou SandboxGestao-Vendas.postman_collection.json e readme do Itaú/REDE perguntando se por ali dá para habilitar o match de loja física.
- Classificação: infra-sensitive
- Fontes usadas:
- Arquivo enviado doc_1f2d8efaff8c_SandboxGestao-Vendas.postman_collection.json; readme enviado; Doppler lc-keys/prd; REDE sandbox read-only.
- O que foi feito:
- Coleção parseada; variáveis e endpoints classificados; 28 GET read-only identificados; endpoints centrais testados com credenciais atuais e PV LK em sandbox; nenhum endpoint de habilitação encontrado na coleção.
- Output/artefato:
- Coleção Sandbox Gestão-Vendas contém 1 POST de token e 28 GET para vendas/parcelas/pagamentos/débitos/recebíveis. Com PV LK em sandbox, sales/installments/payments/credit-orders/receivables/charges retornaram HTTP 400 scenario not available in sandbox. values_printed=false.
- Aprovação: Sem aprovação para criar solicitação de acesso; somente leitura/teste e análise local.
- Envio/publicação: Não expor ClientId, ClientSecret, access_token, Bearer, PV/CNPJ completos, dados bancários ou PII.
- Writes externos: Nenhum write externo. Apenas chamadas REDE GET/read-only e atualização de skill/receipt local.
- Riscos/bloqueios: Coleção não habilita merchant-statement; para dados reais é necessária solicitação via Gestão de Acessos/Portal REDE e aprovação do PV.
- Rollback/mitigação: Remover artefato sanitizado de teste e patch de skill se a interpretação da coleção mudar.
- Próximos passos: Se Lucas aprovar explicitamente, criar solicitação read-only merchant-statement requestType=I permissions=R; depois Lucas precisa aceitar no Portal Rede do PV.
- Onde foi documentado no Brain: Skill lk-finance referência rede-shopify-conciliation atualizada.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
