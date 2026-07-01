# Approval Packet — reparar acesso GitHub para logs do `lucascimino/lk-ops`

- Data: 2026-07-01
- Área: Hermes / LK Ops / GitHub Actions
- Pedido: corrigir falhas recebidas por e-mail dos workflows do repo `lucascimino/lk-ops`
- Workflows afetados por screenshot:
  - `Theme and Platform Health Weekly` / job `health` / branch `main` / commit `ca1f2a8`
  - `Content and SEO Strategy Biweekly` / job `strategy` / branch `main` / commit `ca1f2a8`
- Classificação: A2 auth/access repair, read-only até acesso ser restaurado
- `values_printed=false`

## Problema atual

Hermes não consegue ler os logs/annotations dos GitHub Actions do repo `lucascimino/lk-ops`.

Evidência sanitizada:

| Superfície | Resultado |
|---|---|
| `GITHUB_TOKEN` | autentica como `lk-snkrs`, mas `lucascimino/lk-ops` retorna 404 / repo inacessível |
| `GITHUB_TOKEN_LUCASCIMINO` | existe no Doppler, mas GitHub retorna HTTP 401 Bad credentials |
| Local checkout | não há checkout utilizável de `lk-ops` em `/opt/data` |
| Logs dos runs | indisponíveis até corrigir acesso |

## Objetivo da correção

Restaurar acesso read-only suficiente para:

```bash
gh run list --repo lucascimino/lk-ops --commit ca1f2a8 --json databaseId,name,conclusion,status,url
gh run view <run-id> --repo lucascimino/lk-ops --log-failed
```

Sem fazer writes GitHub, rerun, workflow dispatch, commit, push, deploy ou mudança de produção.

## Opção recomendada A — renovar `GITHUB_TOKEN_LUCASCIMINO`

Lucas gera um PAT fine-grained ou classic token com acesso ao repo `lucascimino/lk-ops` e permissões mínimas:

- Repository access: `lucascimino/lk-ops`
- Contents: Read-only
- Actions: Read-only
- Metadata: Read-only

Depois, Hermes atualiza no Doppler `lc-keys/prd` o secret:

- `GITHUB_TOKEN_LUCASCIMINO`

Verificação pós-update:

- `gh api user` OK
- `gh repo view lucascimino/lk-ops` OK
- `gh run list --repo lucascimino/lk-ops --workflow ...` OK
- `values_printed=false`

Rollback:

- restaurar valor anterior do secret se houver backup seguro/gerenciado; ou
- revogar o novo token no GitHub se comportamento inesperado.

## Opção B — dar acesso ao token/conta `lk-snkrs`

Conceder ao token/conta `lk-snkrs` acesso ao repo `lucascimino/lk-ops` com permissões read-only para Actions/Contents.

Vantagem: não altera secret; usa broker atual.

Risco: amplia acesso do token operacional `lk-snkrs`.

## Opção C — Lucas envia logs/URLs

Lucas envia o link dos runs ou copia logs/annotations dos jobs `health` e `strategy`.

Vantagem: sem mudança de credencial.

Limite: Hermes consegue diagnosticar esse incidente, mas o problema recorrente de acesso permanece.

## Guardrails

- Não imprimir token, preview, OAuth code/state, secret ou header.
- Não copiar credencial para `.env`, Brain, receipt, skill, chat ou logs.
- Usar Doppler `lc-keys/prd` como fonte de verdade.
- Qualquer update de secret só com aprovação explícita e valor fornecido/armazenado de forma segura.
- Sem GitHub write, rerun, commit, push, workflow dispatch, deploy, Docker/VPS/Traefik.

## Próximo passo operacional após aprovação

1. Restaurar acesso por uma das opções acima.
2. Coletar logs falhos dos dois workflows.
3. Identificar causa raiz do commit `ca1f2a8`.
4. Corrigir via PR ou packet separado, conforme a causa.
5. Verificar Actions/readback.
6. Registrar receipt final.
