# PRD — Chatwoot WhatsApp Business API Template Builder

Data: 2026-06-03
Status: `prd_ready_feasibility_positive_no_production_change`
Dono: LK Ops / Atendimento
Sistema alvo: Chatwoot self-hosted `https://chat.lkskrs.online`, conta `1`

## 1. Pergunta do Lucas

Criar um PRD e avaliar se é possível implementar no Chatwoot uma opção para criar template de WhatsApp Business API diretamente pelo Chatwoot.

## 2. Resposta curta

Sim, é possível.

O Chatwoot self-hosted já tem parte da infraestrutura necessária:

- lê/sincroniza templates de WhatsApp Cloud via `business_account_id/message_templates`;
- envia templates via `Channel::Whatsapp` provider `whatsapp_cloud`;
- já possui um serviço específico que cria template de CSAT na Meta (`Whatsapp::CsatTemplateService`), usando `POST /{WABA_ID}/message_templates`;
- já tem controller de CSAT para criar template via inbox.

O que falta é um módulo genérico e seguro para templates, fora do caso específico de CSAT.

## 3. Fontes verificadas

### Meta / WhatsApp Business API

Documentação oficial consultada: `https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/`

Pontos relevantes:

- templates são ativos da WhatsApp Business Account;
- criação via API usa `POST https://graph.facebook.com/vXX.X/{WABA_ID}/message_templates`;
- payload básico: `name`, `category`, `language`, `parameter_format`, `components`;
- categorias: `AUTHENTICATION`, `MARKETING`, `UTILITY`;
- nomes precisam ser minúsculos/alfanuméricos/sublinhados;
- limite informado pela Meta: até 100 templates por WABA por hora;
- variáveis precisam de exemplos;
- template precisa passar por aprovação da Meta antes de uso real.

### Chatwoot observado

Arquivos observados no Chatwoot 4.14.x self-hosted:

- `app/services/whatsapp/providers/whatsapp_cloud_service.rb`
  - `sync_templates` busca templates em `/{business_account_id}/message_templates`.
  - `send_template` envia template via `/{phone_number_id}/messages`.
- `app/services/whatsapp/csat_template_service.rb`
  - já faz `HTTParty.post("#{business_account_path}/message_templates", ...)`.
  - usa token `provider_config['api_key']` e WABA `provider_config['business_account_id']`.
- `app/controllers/api/v1/accounts/inbox_csat_templates_controller.rb`
  - endpoint existente para criar template CSAT em inbox WhatsApp/Twilio WhatsApp.
- `app/services/whatsapp/oneoff_campaign_service.rb`
  - campanhas WhatsApp exigem inbox `Whatsapp`, provider `whatsapp_cloud`, feature `whatsapp_campaign` e `template_params`.

## 4. Problema

Hoje o operador precisa criar templates fora do Chatwoot, normalmente no Gerenciador da Meta/WhatsApp Manager, depois voltar ao Chatwoot e sincronizar/listar templates.

Isso gera atrito:

- atendimento/ops perde contexto;
- difícil padronizar nome/categoria/idioma;
- mais chance de erro em variáveis `{{1}}`/exemplos;
- campanhas no Chatwoot dependem de um template que não nasce no fluxo da campanha;
- recuperação de carrinho fica mais lenta porque o template precisa de ida e volta manual.

## 5. Objetivo do produto

Adicionar ao Chatwoot uma tela/fluxo interno para criar templates WhatsApp Cloud API diretamente da conta/inbox, com validação, preview, envio para aprovação na Meta, status e sincronização automática.

## 6. Não objetivos

Este projeto NÃO deve:

- enviar mensagens para clientes;
- criar campanha automaticamente;
- importar contatos;
- substituir aprovação da Meta;
- permitir free-text em massa fora da janela de 24h;
- prometer que template será aprovado;
- mexer em Tiny/Shopify/estoque;
- habilitar automação de recuperação sem approval separado.

## 7. Usuários

- Lucas / operação LK: cria e aprova copy estratégica.
- Atendimento LK: usa templates aprovados no envio humano/campanha.
- Hermes/Ops: audita consistência, LGPD, nomenclatura e risco.

## 8. Casos de uso iniciais

### UC1 — Criar template de recuperação de carrinho

- Categoria: `MARKETING` ou `UTILITY`, conforme regra/meta/copy final.
- Idioma: `pt_BR`.
- Nome: `lk_carrinho_abandonado_v1`.
- Body com variáveis, ex.: nome, produto, link.
- Botão URL com link dinâmico de recuperação.
- Status inicial esperado: `PENDING`.

### UC2 — Criar template de pedido/envio

- Categoria: `UTILITY`.
- Ex.: confirmação, envio, rastreio, pós-compra.

### UC3 — Ver status de aprovação

- Listar: `PENDING`, `APPROVED`, `REJECTED`, `PAUSED`, etc.
- Mostrar erro/feedback quando a Meta retornar motivo.

## 9. Requisitos funcionais

### RF1 — Listar templates por inbox WhatsApp Cloud

- Tela dentro de Settings > Inboxes > WhatsApp > Templates ou Settings > WhatsApp Templates.
- Buscar do cache `channel.message_templates` e permitir `Sync from Meta`.
- Mostrar nome, idioma, categoria, status, componentes e última sync.

### RF2 — Criar template simples de texto

Campos mínimos:

- Inbox WhatsApp Cloud.
- Nome do template.
- Categoria: `MARKETING`, `UTILITY`, `AUTHENTICATION` (MVP pode restringir a `MARKETING`/`UTILITY`).
- Idioma: default `pt_BR`.
- Parameter format: `positional` no MVP.
- Body text.
- Exemplos de variáveis.
- Footer opcional.
- Botões opcionais.

### RF3 — Validar antes de submeter

Validações:

- nome: minúsculas, números e `_`; máximo 512;
- idioma obrigatório;
- categoria obrigatória;
- body obrigatório;
- se body contém `{{1}}`, `{{2}}`, etc., exigir exemplos na ordem;
- se botão URL contém variável, exigir exemplo;
- bloquear envio se inbox não for `Channel::Whatsapp` com provider `whatsapp_cloud`;
- bloquear se `business_account_id` ou token ausente;
- mostrar aviso LGPD/opt-in para categoria marketing.

### RF4 — Submeter à Meta

Backend cria template via Graph API:

```http
POST /{business_account_id}/message_templates
Authorization: Bearer [REDACTED]
Content-Type: application/json
```

Payload exemplo:

```json
{
  "name": "lk_carrinho_abandonado_v1",
  "category": "MARKETING",
  "language": "pt_BR",
  "parameter_format": "positional",
  "components": [
    {
      "type": "BODY",
      "text": "Oi {{1}}, você deixou {{2}} no carrinho. Posso te ajudar?",
      "example": {
        "body_text": [["Lucas", "Nike Dunk Low"]]
      }
    },
    {
      "type": "BUTTONS",
      "buttons": [
        {
          "type": "URL",
          "text": "Ver carrinho",
          "url": "https://lksneakers.com.br/cart/{{1}}",
          "example": ["abc123"]
        }
      ]
    }
  ]
}
```

### RF5 — Atualizar cache após criação

Depois de sucesso:

- salvar/auditar resposta sem token;
- executar `channel.provider_service.sync_templates` ou marcar sync imediata;
- atualizar `message_templates_last_updated`;
- retornar status `PENDING`.

### RF6 — Auditoria

Registrar internamente:

- usuário Chatwoot que criou;
- inbox;
- nome/template/language/category;
- payload sem secrets;
- resposta Meta redigida;
- data/hora;
- status.

## 10. Requisitos não funcionais

- Nunca expor token Meta no frontend/logs.
- Não fazer envio customer-visible no fluxo de criação.
- Fail-closed: erro de permissão/API não cria campanha nem mensagem.
- Rate limit local: evitar múltiplas submissões duplicadas.
- Compatível com Chatwoot self-hosted 4.14.x.
- Manter patch isolado para facilitar upgrade/rebase.

## 11. Arquitetura proposta

### Backend Rails

Criar serviço genérico:

- `app/services/whatsapp/template_creation_service.rb`

Responsabilidades:

- validar canal WhatsApp Cloud;
- normalizar payload;
- chamar Meta Graph API;
- parsear erro;
- disparar sync.

Criar controller:

- `app/controllers/api/v1/accounts/whatsapp_templates_controller.rb`

Endpoints propostos:

```text
GET  /api/v1/accounts/:account_id/inboxes/:inbox_id/whatsapp_templates
POST /api/v1/accounts/:account_id/inboxes/:inbox_id/whatsapp_templates
GET  /api/v1/accounts/:account_id/inboxes/:inbox_id/whatsapp_templates/:name/status
```

Ou, para encaixar no padrão existente:

```text
resource :whatsapp_templates, controller: 'inbox_whatsapp_templates'
```

### Frontend Vue

MVP pode adicionar botão em `WhatsappTemplates/TemplatesPicker.vue` ou página em Settings/Inboxes:

- `app/javascript/dashboard/components/widgets/conversation/WhatsappTemplates/CreateTemplateModal.vue`
- ou `app/javascript/dashboard/routes/dashboard/settings/inbox/WhatsappTemplateSettings.vue`

Preferência PRD: começar em Settings/Inboxes, não no composer, para reduzir risco de operador criar template durante conversa.

### Modelo de dados

MVP pode não criar tabela nova: usar cache existente `channel.message_templates` + auditoria Rails logs.

Versão mais robusta pode criar tabela:

- `whatsapp_template_submissions`
  - account_id
  - inbox_id
  - user_id
  - template_name
  - language
  - category
  - status
  - request_payload_jsonb redigido
  - response_payload_jsonb redigido
  - meta_template_id
  - timestamps

Recomendação: criar tabela para auditoria, porque isso é produção/customer-messaging adjacent.

## 12. Segurança e compliance

- Categoria `MARKETING` exige aviso explícito: só usar com consentimento/opt-in e opt-out respeitado.
- Não permitir criar template com promessa de estoque, prazo ou desconto sem aprovação humana.
- Para recuperação de carrinho, template deve ser genérico e não prometer disponibilidade.
- Templates rejeitados devem ficar visíveis como rejeitados, não reaproveitados automaticamente.
- O fluxo deve exigir permissão de admin/agent com acesso a inbox.

## 13. Critérios de aceite

### Aceite técnico

- Com uma inbox WhatsApp Cloud válida, usuário admin consegue criar um template simples `pt_BR`.
- Resposta da Meta aparece como `PENDING`/id/nome sem token.
- Sync traz o template para `channel.message_templates`.
- Template aprovado aparece no seletor de WhatsApp templates já existente.
- Erros de Meta aparecem legíveis.
- Tests Rails cobrem validação, sucesso e erro.
- Nenhuma mensagem é enviada durante criação.

### Aceite operacional LK

- O operador consegue criar `lk_carrinho_abandonado_v1` sem sair do Chatwoot.
- O template fica pendente/aprovado/rejeitado rastreável.
- Campanha só pode usar template aprovado.
- Nenhum envio acontece sem aprovação separada.

## 14. Plano de implementação sugerido

### Fase 0 — Preparação segura

1. Fazer fork/branch do Chatwoot custom LK.
2. Confirmar versão/base do container atual.
3. Garantir rollback: imagem atual + compose atual + backup DB antes de deploy.
4. Não mexer em produção no primeiro ciclo.

### Fase 1 — Backend API

1. Criar testes para `Whatsapp::TemplateCreationService`.
2. Implementar validador de inbox/provider.
3. Implementar builder de payload `BODY` + exemplos.
4. Implementar chamada Graph API com token redigido.
5. Implementar parser de erro.
6. Implementar controller e routes.
7. Adicionar policy/autorização.

### Fase 2 — UI mínima

1. Adicionar página/modal de criação em Settings > Inbox > WhatsApp Templates.
2. Campos: name/category/language/body/examples/footer/buttons.
3. Preview do payload e preview humano.
4. Submit + status.
5. Botão `Sync templates` após sucesso.

### Fase 3 — Auditoria

1. Criar tabela `whatsapp_template_submissions`.
2. Persistir submission sem secrets.
3. Exibir histórico básico.

### Fase 4 — LK Recovery templates

1. Criar rascunhos de templates aprováveis.
2. Submeter 1 template controlado.
3. Aguardar aprovação Meta.
4. Só depois habilitar uso em campanha/teste interno.

## 15. Riscos

- Token atual da inbox pode não ter permissão `whatsapp_business_management`; nesse caso consegue enviar/sync ou não dependendo do token, mas criação pode falhar.
- Meta pode rejeitar templates de marketing/carrinho por copy inadequada.
- Patch direto no Chatwoot pode dificultar upgrades; ideal manter branch/fork ou adaptar como contribuição upstream.
- Criar template é seguro comparado a enviar mensagem, mas ainda é uma alteração externa na Meta; exige aprovação antes de produção.

## 16. Veredito de viabilidade

Viável e relativamente direto.

O caminho mais seguro é reaproveitar o que já existe no Chatwoot:

- `Whatsapp::CsatTemplateService` como referência de POST para Meta;
- `WhatsappCloudService#sync_templates` para atualizar cache;
- seletor de templates WhatsApp existente para usar templates aprovados.

O MVP técnico é de tamanho moderado: backend Rails + pequena UI Vue + testes + auditoria.

## 17. Próxima decisão necessária

Antes de implementar, decidir:

1. Implementar como patch/fork do Chatwoot LK self-hosted ou criar primeiro uma ferramenta externa leve no Recovery OS/Hermes que cria templates e depois sincroniza Chatwoot?
2. Começar por backend-only API + uso interno Hermes ou já construir UI dentro do Chatwoot?
3. Qual primeiro template LK será submetido? Recomendo começar com um template utilitário/pós-compra ou um marketing de carrinho com copy conservadora.
