# Approval packet — Zipper Freshworks org deletion — preservar vs deixar expirar

- Data/hora: 2026-06-27T09:53:30+00:00
- Empresa/área: Zipper / Administração de ferramentas SaaS
- Origem: Mesa COO 2026-06-27, Decisão 2/4, botão `Fazer`
- Escopo aprovado agora: readback local/público e packet com opções; sem login/clique/write externo
- Writes externos executados neste follow-through: 0
- values_printed: false

## Evidência local consolidada

Há **três avisos Freshworks** classificados como `needs-attention`, todos com assunto `Delete your Freshworks Organization?`:

1. `zippergaleria.myfreshworks.com`
   - Recebido/processado: 2026-06-12T06:34:33Z
   - Fonte: `areas/zipper/inbox/email-intake/2026-06-12_freshworks_org_deletion_needs_attention.md`
   - Prazo operacional aproximado se forem 30 dias corridos: **2026-07-12**.

2. `zippergaleria-team.myfreshworks.com`
   - Recebido/processado: 2026-06-21T23:31:13Z
   - Fonte: `areas/zipper/inbox/email-intake/20260621T233113Z-freshworks-needs-attention.md`
   - Prazo operacional aproximado se forem 30 dias corridos: **2026-07-21**.

3. `zippergaleria-org.myfreshworks.com`
   - Recebido/processado: 2026-06-27T03:18:24Z
   - Fonte: `areas/zipper/inbox/email-intake/20260627T031824Z-needs-attention-19f07082857fca1c-freshworks-org-delete.md`
   - Prazo operacional aproximado se forem 30 dias corridos: **2026-07-27**.

Os avisos dizem que não há contas/produtos associados à organização e que a deleção automática remove configurações, usuários, segurança/SSO, logs e dados associados, podendo ser irreversível.

## Readback público/no-login executado

- DNS/HTTP público para `zippergaleria.myfreshworks.com`: responde HTTP 200.
- DNS/HTTP público para `zippergaleria-team.myfreshworks.com`: responde HTTP 200.
- DNS/HTTP público para `zippergaleria-org.myfreshworks.com`: responde HTTP 200.

Interpretação: os subdomínios ainda resolvem/publicam uma superfície Freshworks, mas isso **não prova** que a organização está preservada, usada, paga, exportada ou segura contra deleção. Confirma apenas que o domínio público ainda responde sem login.

## Opções de decisão

### Opção A — Preservar/verificar antes do prazo

- Ação humana: Lucas/Cibele/TI acessar Freshworks pelo canal oficial e confirmar se há dados, usuários, SSO/logs ou produto residual que precisam ser preservados/exportados.
- Hermes pode apoiar depois com checklist/packet de evidência, mas não deve clicar, fazer login, deletar, reativar, responder suporte ou alterar conta sem aprovação escopada.
- Recomendado se houver qualquer chance de histórico/CRM/suporte/logs úteis para Zipper.
- Próximo passo seguro: encaminhar decisão para owner humano com os 3 domínios e prazos acima.

### Opção B — Deixar expirar conscientemente

- Ação humana: marcar que as organizações Freshworks não são mais necessárias e aceitar deleção automática.
- Hermes pode registrar `accepted_to_expire` no Brain/Reminder OS para não repetir alerta como se fosse novo, mantendo fonte e prazo.
- Risco: perda de configurações, usuários, SSO, logs e dados associados.

### Opção C — Criar rotina local de lembrete antes dos prazos

- Ação local: registrar Reminder OS/documental para revisar antes de 2026-07-12, 2026-07-21 e 2026-07-27.
- Não acessa Freshworks e não preserva dados por si só; apenas reduz risco de esquecer.
- Útil se Lucas ainda não souber decidir hoje.

## Recomendação operacional

Recomendação mínima: **Opção A ou C**. Como já há três avisos recorrentes com nomes de organização diferentes, tratar como risco administrativo real até um humano confirmar. Não escolher Opção B por inferência.

## Bloqueios explícitos

- Não clicar em link Freshworks.
- Não fazer login ou recuperação de conta.
- Não deletar/preservar/reativar organização.
- Não enviar e-mail para suporte, Cibele, TI ou terceiros.
- Não criar cron externo nem mudar runtime.
- Não imprimir tokens/secrets; values_printed=false.

## Rollback

Este packet é documental/local. Para rollback, remover este arquivo/receipt/ledger event. Nenhuma ação externa foi executada.
