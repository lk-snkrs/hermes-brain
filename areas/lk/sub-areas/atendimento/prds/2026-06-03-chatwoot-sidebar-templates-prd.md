# PRD — Chatwoot Sidebar “Templates” para WhatsApp/META

Data: 2026-06-03
Área: LK Sneakers / Atendimento / Chatwoot / WhatsApp Cloud API
Status: PRD de aplicação para implementação em branch/customização Chatwoot
Solicitação: criar um novo tópico **Templates** acessível pela sidebar principal do Chatwoot, contendo todos os templates vinculados à conta META/WABA.

## 1. Contexto

A LK já validou que é tecnicamente possível criar templates WhatsApp Business API a partir do Chatwoot, reutilizando as primitivas existentes:

- `Whatsapp::Providers::WhatsappCloudService#sync_templates` já busca templates da Meta/WABA e salva em `channel.message_templates`;
- o serviço CSAT do Chatwoot já cria template via `/{business_account_id}/message_templates`;
- a primeira abordagem planejada era criar um builder em Settings/Inboxes/WhatsApp.

Lucas corrigiu o produto: o acesso não deve ficar escondido dentro de Settings/Inboxes. O operador deve encontrar **Templates** diretamente na sidebar esquerda, no mesmo nível visual de Caixa de Entrada, Conversas, Contatos, Relatórios, Campanhas, Central de Ajuda e Configurações.

Imagem de referência recebida: sidebar atual do Chatwoot LK com itens principais e seção Contatos expandida. O novo item deve aparecer como tópico próprio: **Templates**.

## 2. Problema

Hoje o Chatwoot separa:

- campanhas WhatsApp;
- templates aprovados disponíveis em inbox WhatsApp;
- criação/sync de template no contexto técnico de inbox;
- Meta/WABA como origem real dos templates.

Isso cria atrito operacional:

1. o usuário não sabe onde ver todos os templates;
2. templates ficam associados mentalmente a uma inbox, não à conta Meta/WABA;
3. criação/edição/sync exige navegação técnica;
4. campanhas dependem de templates, mas a gestão de templates não aparece como módulo próprio;
5. atendimento precisa enxergar status Meta: aprovado, pendente, rejeitado, pausado, idioma e categoria.

## 3. Objetivo

Criar um módulo **Templates** na sidebar principal do Chatwoot para a conta LK, exibindo e gerenciando todos os templates WhatsApp vinculados à conta Meta/WABA conectada.

O módulo deve permitir:

- listar templates da Meta/WABA;
- sincronizar templates da Meta para Chatwoot;
- visualizar status, categoria, idioma, componentes e exemplos;
- criar novos templates por builder seguro;
- ver histórico de submissões/auditoria;
- impedir envio/campanha automática;
- preparar uso posterior em campanhas WhatsApp.

## 4. Não objetivos

- Não enviar mensagem WhatsApp a clientes.
- Não criar campanha automaticamente após criação/aprovação de template.
- Não habilitar WhatsApp inbox real se ainda não existir.
- Não prometer aprovação Meta.
- Não permitir templates com promessa de estoque, preço, prazo, reserva, desconto ou condição comercial sem validação humana.
- Não expor tokens Meta/Chatwoot/provider config no frontend, logs ou Brain.

## 5. Usuários

### Admin/gestor LK

Quer criar, revisar e sincronizar templates com Meta.

### Atendimento LK

Quer ver quais templates existem e quais estão aprovados para eventual uso manual/assistido.

### Operador de campanha

Quer filtrar templates por categoria/idioma/status antes de montar campanha WhatsApp.

## 6. Escopo funcional

### 6.1 Sidebar

Adicionar item principal:

- Label: `Templates`
- Ícone sugerido: `i-lucide-file-text`, `i-lucide-message-square-text` ou similar
- Posição recomendada: entre **Campanhas** e **Central de Ajuda**, porque templates alimentam campanhas, mas não são campanhas.
- Rota sugerida: `/app/accounts/:accountId/templates`
- Route name sugerido: `whatsapp_templates_index` ou `templates_index`

Critério visual:

- Deve aparecer como item top-level, não dentro de Contatos/Configurações/Campanhas.
- Deve seguir o padrão de `Sidebar.vue` e `menuItems` do Chatwoot.

### 6.2 Página Templates — visão geral

A tela principal deve conter:

- título: `Templates`
- subtítulo: `Templates WhatsApp vinculados à conta Meta`
- seletor de inbox/WABA quando houver mais de uma inbox WhatsApp Cloud;
- botão `Sincronizar com Meta`;
- botão `Novo template`;
- tabela/lista de templates.

Colunas/campos mínimos:

- Nome
- Status Meta: `APPROVED`, `PENDING`, `REJECTED`, `PAUSED`, `DISABLED` etc.
- Categoria: `MARKETING`, `UTILITY`, `AUTHENTICATION`
- Idioma: ex. `pt_BR`
- Tipo/componentes: `BODY`, `HEADER`, `FOOTER`, `BUTTONS`
- Última sincronização
- Inbox/WABA origem
- Motivo de rejeição quando existir
- Ações: `Ver`, `Duplicar`, `Criar variação`, `Sincronizar status`

### 6.3 Filtros

Filtros mínimos:

- Status
- Categoria
- Idioma
- Inbox/WABA
- Busca por nome

Filtros úteis para LK:

- `Aprovados`
- `Pendentes`
- `Rejeitados`
- `Marketing`
- `Utility`
- `pt_BR`

### 6.4 Detalhe do template

Ao abrir um template:

- mostrar payload normalizado;
- mostrar texto do BODY com variáveis;
- mostrar exemplos enviados à Meta;
- mostrar botões/URLs;
- mostrar footer/header;
- mostrar histórico de status quando houver ledger local;
- mostrar alerta: “Criar template não envia mensagem para cliente.”

### 6.5 Builder de novo template

MVP deve suportar:

- nome lowercase/underscore;
- categoria;
- idioma;
- BODY text-only;
- variáveis posicionais `{{1}}`, `{{2}}`;
- exemplos obrigatórios para cada variável;
- footer opcional;
- botão URL opcional;
- preview antes de submeter.

Validações:

- nome apenas `[a-z0-9_]`;
- variáveis sequenciais sem gaps;
- toda variável tem exemplo;
- URL com variável exige exemplo;
- categoria obrigatória;
- idioma obrigatório;
- confirmação explícita antes de enviar à Meta.

### 6.6 Auditoria

Criar ledger `whatsapp_template_submissions` ou equivalente.

Campos recomendados:

- `id`
- `account_id`
- `inbox_id`
- `user_id`
- `waba_id` parcial/hashed se necessário
- `template_name`
- `category`
- `language`
- `status`
- `request_payload` sem tokens
- `meta_response` sem tokens
- `meta_template_id`
- `rejected_reason`
- `created_at`
- `updated_at`

## 7. Fonte de verdade

- Meta/WABA é a fonte de verdade dos templates.
- Chatwoot mantém cache local via `channel.message_templates` e/ou ledger.
- O botão `Sincronizar com Meta` deve atualizar o cache a partir da Graph API.
- A listagem deve indicar quando o dado está cacheado e quando foi a última sync.

## 8. API/backend proposto

### Rotas account-level

Como Lucas quer `Templates` como módulo de conta, a UI deve expor rotas account-level, mesmo que internamente precise de inbox/WABA.

Sugerido:

```text
GET  /api/v1/accounts/:account_id/whatsapp_templates
POST /api/v1/accounts/:account_id/whatsapp_templates
POST /api/v1/accounts/:account_id/whatsapp_templates/sync
GET  /api/v1/accounts/:account_id/whatsapp_templates/:id
```

Parâmetros opcionais:

- `inbox_id`
- `status`
- `category`
- `language`
- `q`

### Serviços backend

Reutilizar/generalizar:

- `Whatsapp::TemplatePayloadBuilder`
- `Whatsapp::TemplateCreationService`
- `Whatsapp::TemplateSyncService`
- `Whatsapp::TemplateCatalogService`

### Guardrails backend

- Aceitar apenas inboxes `Channel::Whatsapp` com provider `whatsapp_cloud`.
- Rejeitar inbox API/Shopify/internal-only.
- Nunca retornar `provider_config.api_key`.
- Sanitizar resposta Meta antes de salvar/logar.
- Creation exige permissão de agente/admin apropriada.
- Sync pode ser permitido para admin/agent com permissão de inbox, a definir.

## 9. Frontend proposto

Arquivos prováveis no Chatwoot 4.14.x:

- `app/javascript/dashboard/components-next/sidebar/Sidebar.vue`
  - adicionar item top-level `Templates` em `menuItems`.
- `app/javascript/dashboard/routes/dashboard/...`
  - adicionar rota account-scoped para Templates.
- `app/javascript/dashboard/api/...`
  - criar client API `whatsappTemplates.js` ou estender `inboxes.js` se optar por route inbox-scoped internamente.
- `app/javascript/dashboard/store/modules/...`
  - módulo Vuex/Pinia para templates, se necessário.
- `app/javascript/dashboard/routes/dashboard/templates/pages/TemplatesPage.vue`
  - página principal.
- `.../components/TemplatesTable.vue`
- `.../components/TemplateBuilderDialog.vue`
- `.../components/TemplateDetailDrawer.vue`
- i18n pt_BR/en keys para `SIDEBAR.TEMPLATES` e textos da tela.

## 10. Estados de UI

### Sem inbox WhatsApp Cloud

Mostrar empty state:

> Nenhuma inbox WhatsApp Cloud conectada. Conecte uma inbox WhatsApp para sincronizar templates da Meta.

Não mostrar criação ativa.

### Com inbox WhatsApp Cloud, sem templates

Mostrar:

- CTA `Sincronizar com Meta`
- CTA `Novo template`

### Templates pendentes

Mostrar status visual amarelo e texto:

> Aguardando aprovação da Meta.

### Templates rejeitados

Mostrar motivo de rejeição se disponível e CTA `Duplicar e corrigir`.

### Erro de permissão Meta

Mostrar:

> Token Meta sem permissão para gerenciar templates. Verifique `whatsapp_business_management`.

Sem exibir token.

## 11. Permissões

Sugestão MVP:

- Admin: listar, sincronizar, criar template.
- Agent: listar e ver detalhes.
- Custom roles: futura permissão `manage_whatsapp_templates`.

Criação de template é write externo Meta/WABA e deve exigir confirmação.

## 12. Segurança e compliance LK

- Criar template não envia mensagem, mas cria ativo de produção na Meta.
- Mensagens/campanhas continuam bloqueadas sem aprovação separada.
- UI deve mostrar aviso para categorias Marketing/Utility.
- Templates de carrinho/recuperação devem evitar promessas comerciais/estoque.
- Tiny continua fonte de estoque; templates não podem prometer disponibilidade.
- Não registrar tokens nem números sensíveis em logs/Brain.

## 13. Métricas de sucesso

- Item `Templates` aparece na sidebar principal.
- Lista carrega todos os templates vinculados à WABA/Meta conectada.
- Sync Meta atualiza status sem expor segredo.
- Builder cria template válido em ambiente aprovado.
- Templates pendentes/aprovados/rejeitados são distinguíveis.
- Nenhum envio WhatsApp é disparado pelo módulo.
- Testes de payload builder, service, controller e UI passam.

## 14. MVP recomendado

### MVP A — Catálogo read-only na sidebar

- Criar rota/sidebar `Templates`.
- Listar templates cacheados de `channel.message_templates`.
- Botão `Sincronizar com Meta` para inbox WhatsApp Cloud.
- Empty state se não houver inbox WhatsApp Cloud.
- Sem criação Meta ainda.

### MVP B — Builder com submissão Meta

- Form text-only.
- Validações.
- Confirmação explícita.
- POST Meta.
- Ledger/auditoria.
- Sync pós-criação.

### MVP C — Operação avançada

- Duplicar template.
- Histórico de rejeição.
- Variações por idioma.
- Integração com campanhas.
- Permissão granular.

## 15. Critérios de aceite MVP A

1. Sidebar mostra `Templates` como tópico principal.
2. Clique abre `/app/accounts/:accountId/templates`.
3. Tela lista templates vinculados às inboxes WhatsApp Cloud da conta.
4. Tela mostra nome/status/categoria/idioma/componentes.
5. Sync chama Meta via backend e atualiza cache.
6. Sem inbox WhatsApp Cloud, mostra empty state correto.
7. Nenhum token aparece no payload do frontend.
8. Nenhuma mensagem/campanha é criada/enviada.
9. Testes frontend/backend passam.

## 16. Critérios de aceite MVP B

1. Admin consegue abrir `Novo template`.
2. Builder valida nome, categoria, idioma, BODY e exemplos.
3. Preview aparece antes da submissão.
4. Confirmação explícita informa que será criado ativo na Meta.
5. Backend chama `/{WABA_ID}/message_templates` com token server-side.
6. Resultado salva ledger sem segredo.
7. Sync atualiza lista e mostra `PENDING`/`APPROVED`/`REJECTED`.
8. Nenhuma mensagem é enviada a cliente.

## 17. Riscos

- Chatwoot sem inbox WhatsApp Cloud real: módulo só mostra empty state.
- Token Meta sem `whatsapp_business_management`: criação/sync falha.
- Cache `channel.message_templates` pode estar por inbox, mas Lucas quer visão account-level; precisa agregação por todas as inboxes WhatsApp Cloud da conta.
- Meta pode rejeitar templates por conteúdo/categoria.
- Customização precisa de build/deploy Chatwoot; produção exige backup/rollback e aprovação separada.

## 18. Decisões abertas

1. Posição exata na sidebar: recomendado entre `Campanhas` e `Central de Ajuda`.
2. Nome técnico da rota: `templates_index` ou `whatsapp_templates_index`.
3. MVP inicial será read-only catálogo + sync ou já builder com criação Meta?
4. Permissão: só admin cria ou agentes também podem criar rascunho?
5. Ledger obrigatório no MVP A ou apenas no MVP B?
6. Devemos esconder `Templates` quando não houver WhatsApp Cloud inbox ou mostrar com empty state?

## 19. Recomendação final

Implementar em duas etapas:

1. **MVP A primeiro:** sidebar + catálogo + sync + empty state. Isso resolve a navegação e a visibilidade dos templates vinculados à Meta sem risco de criar ativos externos.
2. **MVP B depois:** builder + submissão Meta + ledger + confirmação explícita.

Essa separação mantém o produto seguro: o módulo aparece onde o operador espera, mas criação Meta e mensagens continuam separadas por gates de aprovação.
