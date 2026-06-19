# Approval Packet — Zipper Google Workspace 2FA / Admin Reports read-only — 2026-06-18

Status: preparado, não executado em Admin Console.  
Target Workspace: `zippergaleria.com.br`.  
Admin changes: 0.  
External writes: 0.  
Sends executed: 0.  
values_printed=false.

## Contexto

O Fechamento Ágil 2026-06-17 registrou alerta do Google Workspace Zipper: **7 usuários sem 2FA**. A fonte indica que o alerta pertence à Zipper (`lucas@zippergaleria.com.br` / domínio `zippergaleria.com.br`), não LK.

## Prova read-only já feita

- Smoke Google Workspace: OK / HTTP 200 / `values_printed=false`.
- Credenciais Google em Doppler existem e algumas refresham com sucesso.
- Probe de escopo para Admin Reports/Directory: credenciais atuais **não têm** `admin.reports.usage.readonly` nem `admin.directory.user.readonly`.
- Admin Reports 2FA retornou HTTP 403 nas credenciais testadas; interpretar como **escopo/admin-read insuficiente**, não como ausência do alerta.

## Bloqueio atual

Não é seguro/enforceable listar usuários ou aplicar 2FA por API com o token atual. O próximo passo seguro é autorização OAuth read-only com conta Super Admin do Workspace Zipper.

## Próxima ação segura aprovada por este packet

1. Abrir URL OAuth gerada localmente para escopos read-only:
   - `admin.reports.usage.readonly`
   - `admin.directory.user.readonly`
2. Usar `lucas@zippergaleria.com.br` se for Super Admin; se não, usar outro Super Admin do domínio `zippergaleria.com.br`.
3. Colar de volta o redirect completo `http://localhost:1/?code=...&state=...`.
4. Hermes troca o code em processo local, lê somente status 2FA e gera contagem/lista operacional local.

Pending OAuth state: `gws2fa_3rejL4GbZA4XVNvN0U9Q2g`.  
Pending verifier file: `/opt/data/tmp/google_workspace_zipper_admin_read_pending_gws2fa_3rejL4GbZA4XVNvN0U9Q2g.json`.

## Fora do escopo sem nova aprovação

- Enforce de 2FA.
- Alterar Organization Units / políticas.
- Bloquear/desbloquear usuários.
- Notificar usuários por e-mail/WhatsApp.
- Criar/revogar credenciais permanentes em Doppler.

## Plano após read-only

- Se usuário sem 2FA for admin/high-risk: gerar packet de enforcement por ordem de risco.
- Se forem contas comuns: gerar checklist para Admin Console com rollback de lockout.
- Verificação pós-mudança somente depois de aprovação de enforcement: Admin Console + Admin Reports readback.

## Rollback

Nenhum rollback necessário agora: nenhuma mudança externa foi feita. Para enforcement futuro, rollback mínimo é remover enforcement temporariamente para usuário bloqueado ou mover usuário para OU de exceção temporária, sempre com aprovação e prazo.

## Auth URL

```text
https://accounts.google.com/o/oauth2/v2/auth?client_id=797436119355-kdjqqvips3oea32h94nq4f97l7r4ank6.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A1&response_type=code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fadmin.reports.usage.readonly+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fadmin.directory.user.readonly&access_type=offline&prompt=consent&state=gws2fa_3rejL4GbZA4XVNvN0U9Q2g&code_challenge=iAj5BdO825f-BuQTwNu8gFh566PfYQkB8Kf4EkpqKgU&code_challenge_method=S256&include_granted_scopes=true
```
