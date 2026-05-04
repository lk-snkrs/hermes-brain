# Integração — GitHub

## Escopo

GitHub hospeda o Hermes Brain (`lk-snkrs/hermes-brain`) como fonte de verdade versionada.

## Secrets Doppler

- `GITHUB_TOKEN`


## Repositórios privados relevantes observados

- `lk-snkrs/hermes-brain` — fonte de verdade operacional/documental do Hermes Brain.
- `spiti-auction/spiti-hub` — sistema operacional unificado da SPITI, privado; acesso confirmado em 2026-05-04 com token separado fornecido por Lucas. Não gravar token em remote/arquivo; mover segredo para Doppler antes de uso recorrente.

## Read-only

- Ler arquivos, histórico, issues, PRs, releases e diffs.
- Verificar status de branches e commits.

## Write

- Criar commits e push em `main` para docs/guardrails quando dentro do fluxo aprovado.
- Preferir PR para mudanças estruturais grandes; commits diretos pequenos são aceitáveis no fluxo atual do Brain se verificados.

## External-send

- Comentários públicos em issues/PRs ou abertura de PR externo devem ser tratados como ação externa; usar bom senso e informar Lucas quando relevante.

## Admin/destructive

- Alterar settings do repo, secrets/actions, permissões, deletar branches importantes, force-push ou tornar público/privado exige aprovação explícita.

## Verificação obrigatória

- Rodar `python3 scripts/brain_health_check.py`.
- Rodar secret scan com resultado `possible_secrets 0`.
- Usar Doppler para token; não gravar token no remote/arquivo.

## Escala de permissões

- Read-only: consultar metadados, status, listas, métricas e registros sem alterar dados.
- Write: criar/atualizar dados internos, tags, notas, segmentos ou configurações não destrutivas.
- External-send: enviar mensagem, email, campanha, notificação ou contato com cliente/lead/parceiro. Exige preview e aprovação de Lucas.
- Admin/destructive: apagar dados, alterar credenciais, webhooks, domínios, billing, permissões, deploys, containers, produção ou integrações críticas. Exige aprovação explícita, plano de backup e rollback.

Regra de secrets: este arquivo lista apenas nomes de secrets no Doppler `lc-keys/prd`; valores reais nunca entram no GitHub.
