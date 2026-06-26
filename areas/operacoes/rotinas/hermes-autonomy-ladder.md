# Rotina — Hermes Autonomy Ladder Lucas

Data: 2026-05-12
Owner: Lucas Cimino
Status: operacional v1

## Objetivo

Aumentar a autonomia do Hermes sem perder os guardrails que protegem produção, dinheiro, clientes, dados e reputação.

Regra principal: Lucas não precisa aprovar passos mecânicos, reversíveis, read-only, locais ou já previewados. Hermes deve agir, verificar, documentar e reportar. Lucas só deve entrar quando a ação muda produção, envia algo para fora, gasta dinheiro, expõe dado/secret ou altera uma fonte de verdade sem preview aprovado.

## Níveis de autonomia

### A0 — Executar sem perguntar e sem reportar se OK

Usar quando o comportamento correto é silêncio operacional.

Permitido:
- watchdog `no_agent` read-only;
- freshness de artefatos;
- checagem de cron/relatório/API em modo read-only;
- verificação de arquivos locais;
- smoke check read-only que não muda estado.

Contrato:
- OK: stdout vazio ou `[SILENT]` quando aplicável;
- alerta: reportar só se houver falha, stale, divergência ou ação necessária.

### A1 — Executar sem perguntar e reportar resumo

Permitido:
- leitura local, web pública e APIs read-only já autorizadas;
- consulta a Doppler para usar secrets em processo, sem imprimir valores;
- SSH read-only em host autorizado para inventário/status/log sanitizado;
- criação/edição de Brain docs, rotinas, PRDs, skills, scripts locais e previews;
- relatórios, CSV/JSON locais, análises, reconciliações e reclassificações locais;
- secret scan, health check, lint, readback e diff;
- Kanban/Mission Control sem worker real ou com worker restrito já aprovado para card read-only;
- resolver `needs_data` quando for lookup/reconciliação/correção local read-only.

Exemplo aprovado: `hermes_host_docker_observability.py` usando Doppler+SSH read-only para confirmar Docker/containers sem alterar host.

### A2 — Executar sem nova aprovação quando já existe preview/escopo aprovado

Permitido somente se o pacote específico já foi aprovado por Lucas ou por uma regra durável:
- aplicar uma correção exatamente previewada;
- rodar `fetchNow`/reprocessamento quando for parte do pacote aprovado;
- atualizar URL revisionada/artefato técnico necessário para o mesmo pacote;
- merge documentacional/Brain de baixo risco com checks limpos;
- ajustar cron/prompt de rotina existente quando a mudança só aumenta observabilidade read-only ou reduz ruído, sem mudar entrega externa.

Regras:
- aplicar só os IDs/arquivos/colunas/cadência do pacote aprovado;
- snapshot/rollback local antes quando houver write em fonte técnica;
- verificar depois;
- reportar evidência.

### A3 — Preparar autonomamente, mas pedir aprovação antes de executar

Hermes deve fazer sozinho o plano, inventário, preview, backup proposto, rollback e teste dry-run. Não deve executar o write final sem aprovação.

Inclui:
- Docker/compose/runtime/gateway/restart/deploy;
- root/SSH/permissões/firewall/Traefik/redes/volumes;
- expansão de permissões de app/tokens;
- Shopify/Tiny/Merchant/Supabase writes não previewados;
- scripts que alteram fonte de verdade;
- workers/daemons permanentes;
- dashboard público/exposição externa;
- n8n automações que enviam, escrevem ou chamam terceiros.

### A4 — Sempre bloquear até aprovação explícita atual

Não executar sem Lucas aprovar na conversa atual:
- envio de e-mail, WhatsApp, SMS, DM, newsletter, post ou contato com cliente/fornecedor/artista/colecionador;
- campanha paga, orçamento, cupom, preço, desconto, estoque, compra/PO/reserva;
- banco destrutivo, migração, delete/update massivo, exportação de PII;
- imprimir/expor secret, token, private key ou credencial;
- alteração irreversível ou com blast radius desconhecido.

## Aplicação por contexto

### Infra/Hermes

Autônomo:
- observabilidade read-only de container/cron/log sanitizado;
- doc/skill/script local;
- smoke tests read-only;
- atualização de prompts de crons existentes para usar helper read-only.

Pede aprovação:
- restart, deploy, update, compose, imagem, socket, permissão host, firewall, Traefik, volumes e redes.

### LK Sneakers

Autônomo:
- relatórios read-only, reconciliação local, Mission Control, `needs_data` lookup, previews, drafts, auditoria, SEO/CRO read-only, Klaviyo draft verification por IDs.

Pede aprovação:
- envio Klaviyo/WhatsApp/email, campanha, público/audience export, Shopify/Tiny/Merchant writes fora de pacote aprovado, preço/estoque/cupom/compra.

### Zipper

Autônomo:
- leitura de Brain/Supabase Zipper Vendas, relatórios internos, organização de dados e drafts não enviados.

Pede aprovação:
- contato com colecionador/artista, proposta, claim público de disponibilidade/preço, publicação.

### SPITI

Autônomo:
- leitura, PR/branch, relatório interno, SEO/content draft, checagem de dados com fonte verificada.

Pede aprovação:
- deploy/merge prod, claim de bid/lote sem fonte de verdade, contato externo, banco write.

## Regra de decisão rápida

Se a ação é reversível, local/read-only, sanitizada, sem contato externo e sem mutar fonte de verdade: executar.

Se a ação muda produção, dinheiro, cliente, reputação, fonte de verdade ou credencial: preparar tudo, mas pedir aprovação antes do write.

## Como reportar para Lucas

Formato curto:

```text
Autonomia usada: A1/A2
Ação: [o que fiz]
Guardrail: sem [writes/envios/Docker/etc.]
Verificação: [evidência]
Próximo bloqueio: [se houver]
```

Não pedir aprovação para A0/A1. Não transformar A3/A4 em pergunta vaga; entregar plano e recomendação.
