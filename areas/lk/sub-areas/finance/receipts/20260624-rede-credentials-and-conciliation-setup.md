# Receipt — REDE credentials e setup conciliação loja física

- Data/hora: 2026-06-24T15:05:08.575438+00:00
- Agente/profile/cron: lk-finance
- Empresa/área: LK / Finance
- Responsável humano: LK Finance
- Pedido original: Lucas criou novo projeto REDE e informou que o LK Finance deve fazer match de vendas da loja física com vendas REDE e saldo Itaú.
- Classificação: infra-sensitive
- Fontes usadas:
- Mensagem do Lucas no Telegram; Doppler lc-keys/prd; docs públicas REDE; teste de token sandbox com saída sanitizada.
- O que foi feito:
- Credenciais REDE salvas no Doppler por nomes REDE_CLIENT_ID, REDE_CLIENT_SECRET, REDE_AUTH_TYPE; URLs REDE salvas como REDE_SANDBOX_BASE_URL, REDE_SANDBOX_TOKEN_URL, REDE_PROD_BASE_URL; helper Doppler lk-finance atualizado; skill REDE-Shopify atualizada.
- Output/artefato:
- Inventário lk-finance com 12/12 secrets presentes. Teste de autenticação: sandbox token OK sem imprimir token; endpoints produtivos testados com essas credenciais retornaram 401/403, então produção ainda requer validação/credencial/coleção oficial.
- Aprovação: Lucas forneceu credenciais e instruiu lembrar/wirear para conciliação. Nenhum acesso REDE de Gestão de Acessos foi solicitado sem aprovação separada.
- Envio/publicação: Telegram: reportar apenas nomes de secrets/status; sem ClientId/Secret/token/header/conta/CNPJ.
- Writes externos: Doppler secret write. Nenhum write em REDE, Shopify, banco ou contabilidade.
- Riscos/bloqueios: Credenciais foram coladas no chat; tratar como sensíveis e considerar rotação. Credenciais atuais parecem válidas para sandbox, não confirmadas para produção real.
- Rollback/mitigação: Remover/rotacionar secrets REDE no Doppler; reverter patch do helper/skill se necessário.
- Próximos passos: Para match real: confirmar acesso produtivo REDE/Gestão de Acessos ao PV, ler vendas REDE por data/NSU, ler Shopify/POS read-only, cruzar com Itaú/Open Finance por liquidação.
- Onde foi documentado no Brain: Receipt sanitizado; skill lk-finance references/rede-shopify-conciliation.md; helper Doppler PROFILE_SECRET_MAP.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
