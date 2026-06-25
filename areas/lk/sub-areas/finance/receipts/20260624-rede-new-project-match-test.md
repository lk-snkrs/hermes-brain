# Receipt — Novo projeto REDE salvo e teste de match loja física

- Data/hora: 2026-06-24T20:02:29.176715+00:00
- Agente/profile/cron: lk-finance
- Empresa/área: LK / Finance
- Responsável humano: LK Finance
- Pedido original: Lucas forneceu novo ClientId/ClientSecret REDE e pediu usar para match de vendas da loja física com REDE e saldo Itaú.
- Classificação: infra-sensitive
- Fontes usadas:
- Mensagem Lucas; Doppler lc-keys/prd; REDE Gestão de Vendas sandbox/prod read-only; Shopify POS read-only; Itaú Open Finance read-only.
- O que foi feito:
- Novas credenciais REDE salvas no Doppler como REDE_CLIENT_ID, REDE_CLIENT_SECRET e REDE_AUTH_TYPE=Bearer; smoke REDE sandbox executado; endpoints produtivos de token testados; Shopify POS e Itaú do dia 2026-06-24 exportados sanitizados; conciliation_match gerado localmente.
- Output/artefato:
- REDE sandbox token OK e adjustment-types HTTP 200; REDE sales sandbox HTTP 400 scenario not available; token produtivo HTTP 401 invalid_client. Match local 2026-06-24: Shopify POS 2 pedidos total R$ 4.659,99; Itaú REDE 2 créditos total R$ 8.333,56; 0 matches fechados; 2 pendências NEEDS_REDE_SALE_DETAIL/NO_PIX_BANK_MATCH. values_printed=false.
- Aprovação: Lucas disse Use isso e forneceu as credenciais; escopo aplicado: salvar secret e executar chamadas read-only/smoke. Nenhum write em REDE/Shopify/Itaú.
- Envio/publicação: Não expor ClientId, ClientSecret, token Bearer, headers, PV/CNPJ completos, dados bancários ou PII.
- Writes externos: Write externo apenas Doppler secret update. Chamadas REDE/Shopify/Itaú foram read-only. Nenhum pagamento, transferência, transação, captura, cancelamento, Shopify write ou solicitação de acesso feita.
- Riscos/bloqueios: Credencial nova funciona para token sandbox, mas não para dados reais de loja física; sandbox não disponibiliza cenário de vendas e produção retorna invalid_client. Sem detalhe REDE real, cartões POS seguem pendentes.
- Rollback/mitigação: Restaurar credenciais REDE anteriores no Doppler se necessário; artefatos locais são sanitizados e podem ser removidos.
- Próximos passos: No Portal REDE, habilitar/autorizar acesso produtivo merchant-statement/Gestão de Vendas para o PV da LK ou fornecer coleção/endpoints produtivos corretos; após isso rodar novamente match REDE↔Shopify↔Itaú.
- Onde foi documentado no Brain: Skill lk-finance referência rede-shopify-conciliation atualizada com status do novo projeto.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
