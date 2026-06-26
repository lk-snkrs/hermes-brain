# Handoff — Chatwoot Sidebar Templates

Data UTC: 2026-06-03T18:25:13Z
Área: LK Sneakers / Atendimento / Chatwoot / WhatsApp Cloud API
Workspace: `/opt/data/lk-chatwoot-prod-source`
Branch: `lk/whatsapp-template-builder`

## Solicitação

Criar novo tópico **Templates** acessível via sidebar principal do Chatwoot, com todos os templates vinculados à conta Meta/WABA.

## Implementado localmente

- Novo item top-level `Templates` na sidebar, posicionado após `Campanhas` e antes de `Central de Ajuda`.
- Nova rota frontend: `/app/accounts/:accountId/templates`.
- Nova página `TemplatesPage.vue` com:
  - listagem de inboxes WhatsApp Cloud;
  - contagem de templates carregados;
  - listagem agrupada por inbox;
  - nome, status, categoria, idioma e componentes;
  - botão de recarregar;
  - botão de sincronizar com Meta;
  - formulário para submeter novo template para aprovação na Meta usando endpoints já adicionados no MVP anterior.
- Traduções adicionadas em `en/settings.json` e `pt/settings.json`.

## Arquivos alterados/criados

- `app/javascript/dashboard/components-next/sidebar/Sidebar.vue`
- `app/javascript/dashboard/routes/dashboard/dashboard.routes.js`
- `app/javascript/dashboard/routes/dashboard/templates/templates.routes.js`
- `app/javascript/dashboard/routes/dashboard/templates/TemplatesPage.vue`
- `app/javascript/dashboard/i18n/locale/en/settings.json`
- `app/javascript/dashboard/i18n/locale/pt/settings.json`

## Verificação executada

Dependências JS foram instaladas temporariamente via `corepack pnpm install` para viabilizar verificação local.

Comandos executados:

```bash
corepack pnpm exec eslint app/javascript/dashboard/routes/dashboard/templates/TemplatesPage.vue app/javascript/dashboard/routes/dashboard/templates/templates.routes.js app/javascript/dashboard/routes/dashboard/dashboard.routes.js app/javascript/dashboard/components-next/sidebar/Sidebar.vue
```

Resultado: exit code 0.

```bash
corepack pnpm exec vite build
```

Resultado: exit code 0; build concluído em aproximadamente 3m08s. Apenas warnings esperados de chunk size grande foram emitidos.

Após build, artefatos gerados em `public/vite` foram removidos/revertidos para não poluir a branch. `node_modules` temporário também foi removido.

## Guardrails / não feito

- Nenhum deploy de produção.
- Nenhuma chamada live para Meta feita por esta implementação.
- Nenhum template real criado neste passo.
- Nenhum envio WhatsApp.
- Nenhuma campanha.
- Nenhuma alteração Shopify/Tiny.

## Próximo passo recomendado

Preparar commit da branch local e, se aprovado, abrir PR/deploy controlado. Antes de produção, confirmar se criação de template via UI deve ficar habilitada para todos administradores ou atrás de feature flag/permissão LK específica.
