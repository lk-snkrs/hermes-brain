# Google Workspace 2FA — action packet sem mudança admin — 2026-06-17T14:38:36Z

## Situação
Alerta do Google Workspace informa **7 usuários sem verificação em duas etapas**. Isso é risco real de conta comprometida por roubo de senha.

## Ação segura preparada
- Revisão no Admin Console em modo leitura.
- Identificar os 7 usuários/grupos afetados.
- Priorizar contas admin e contas com acesso financeiro/CRM.
- Só depois de aprovação: ativar/obrigar 2FA com janela curta de exceção.


## Probe read-only de credencial
- Smoke Google Workspace: OK, token recebido, HTTP 200, `values_printed=false`.
- Admin Reports API para listar 2FA: bloqueada por escopo insuficiente, HTTP 403.
- Interpretação: credencial existe no Doppler e autentica; o runtime atual não tem escopo Admin Reports para listar os 7 usuários por API sem novo OAuth/escopo admin. A alternativa segura hoje é revisão manual/read-only no Admin Console ou aprovação de nova credencial/escopo.

## Approval packet para executar mudança
Se você aprovar depois, o escopo deve ser:
- Target: Google Workspace Zipper.
- Mudança: exigir 2FA para usuários pendentes, começando por admins/alto risco.
- Rollback: remover enforcement temporariamente para usuário bloqueado, se necessário.
- Verificação: Admin Console mostrando 2SV enforced/enrolled e zero usuários críticos pendentes.

## Limites desta execução
- Admin changes: 0
- Sends executados: 0
- External writes: nenhum
- Secrets: nenhum valor impresso
- values_printed=false

Fonte local: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/zipper/inbox/email-intake/2026-06-17_124253Z_needs_attention_19ed594bc007a7c6.yaml`
