# Receipt — Chatwoot label creation for Giselia without admin

Data/hora UTC: 2026-06-12 20:17–20:25
Operador: Hermes LK Ops
Sistema: Chatwoot LK (`chat.lkskrs.online`)
Usuária: Giselia — `atendimento@lksneakers.com.br`

## Pedido

Lucas pediu corrigir porque a Giselia, usando `atendimento@lksneakers.com.br`, não conseguia criar tags/labels no Chatwoot.

URL citada:

- `https://chat.lkskrs.online/app/accounts/1/settings/labels/list`

Lucas escolheu a alternativa:

- criar workaround/alternativa sem transformar Giselia em admin.

## Diagnóstico

Inspeção read-only mostrou:

- Giselia existe na conta LK Sneakers.
- Role atual: `agent`.
- `administrator?`: `false`.
- Chatwoot upstream usa `LabelPolicy#create?` hardcoded para `administrator?`.
- A rota frontend `/settings/labels` também restringia a página a `administrator`.

Conclusão: não havia permissão granular nativa só para tags nesta instalação.

## Solução aplicada

Foi aplicado patch escopado para permitir que **somente** a Giselia crie labels/tags na conta LK Sneakers, sem virar admin.

### Backend

Arquivo no container/imagem:

- `/app/app/policies/label_policy.rb`

Mudança:

- `create?` agora permite:
  - admin normal; ou
  - usuário com e-mail `atendimento@lksneakers.com.br` na conta `1`.

Mantido bloqueado:

- `destroy?` continua somente admin.
- `update?` continua somente admin.
- demais agentes não receberam permissão ampla.

### Frontend

Arquivos no container/imagem:

- `/app/app/javascript/dashboard/routes/dashboard/settings/labels/labels.routes.js`
- `/app/public/packs/vite/assets/dashboard-*.js`

Mudança:

- rota `labels_wrapper` / `labels_list` passou a aceitar `agent` no frontend, permitindo que a Giselia abra a página de labels.
- O controle real de criação continua no backend policy, escopado por e-mail/conta.

## Persistência

Para evitar perder o patch no próximo recreate simples:

- foi criado commit de imagem Docker a partir do container patchado;
- imagem ativa: `lk-chatwoot:v2-recovery19-giselia-labels-20260612`;
- `/opt/chatwoot/docker-compose.yaml` atualizado para usar essa imagem.

## Backup

Backup criado em:

- `/opt/chatwoot/backups/giselia-labels-20260612T201752Z/`

Inclui:

- `label_policy.rb`
- `dashboard.js`
- `docker-compose.yaml`

## Restart/recreate

Executado:

- `docker compose up -d --no-deps rails`

Observação:

- houve 502 temporário enquanto o Rails subia;
- depois voltou `HTTP 200`.

## Verificação

Container ativo:

```text
chatwoot-rails-1 | lk-chatwoot:v2-recovery19-giselia-labels-20260612 | Up
```

HTTP página labels:

```text
https://chat.lkskrs.online/app/accounts/1/settings/labels/list -> 200
```

Policy check:

```json
{
  "role": "agent",
  "admin": false,
  "can_create_label": true,
  "can_delete_label": false
}
```

Frontend asset:

```text
labels_list_agent=true
labels_wrapper_agent=true
```

## Rollback

Se precisar reverter:

1. Editar `/opt/chatwoot/docker-compose.yaml` e voltar imagem para:
   - `lk-chatwoot:v2-recovery19`
2. Recriar Rails:
   - `cd /opt/chatwoot && timeout 180 docker compose up -d --no-deps rails`
3. Confirmar:
   - `curl -fsS -o /dev/null -w "%{http_code}\n" https://chat.lkskrs.online/app/accounts/1/settings/labels/list`

Rollback mais fino:

- restaurar arquivos de `/opt/chatwoot/backups/giselia-labels-20260612T201752Z/` para o container/imagem.

## Notas operacionais

- Giselia continua sem admin.
- Ela deve atualizar a página / limpar cache se a UI antiga continuar aparecendo.
- Como o patch mexe em asset compilado e policy de app, upgrades futuros do Chatwoot podem sobrescrever essa exceção; se houver upgrade, revalidar `LabelPolicy` e rota `labels_list`.
- Não foram impressos secrets. `values_printed=false`.
