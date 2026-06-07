# LK Content — Checklist Técnico-Operacional de Implementação

> **Para Hermes:** usar este checklist após aprovação escopada de runtime. Este documento não autoriza token, gateway, crons reais nem writes externos por si só.

Status: plano documental aprovado para orientar execução futura
Data: 2026-06-07
PRD fonte: `../prd/lk-content-prd-20260607.md`
Perfil alvo: `lk-content`
Bot alvo: `@hermes_lk_producaodeconteudo_bot`

---

## Objetivo

Implementar o agente **LK Content** como perfil Hermes isolado para operar conteúdo premium, Klaviyo, calendário, pesquisa, criativos e aprendizado contínuo da LK Sneakers.

## Arquitetura resumida

- Perfil Hermes isolado: `/opt/data/profiles/lk-content`.
- Brain canônico: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/`.
- Telegram dedicado: `@hermes_lk_producaodeconteudo_bot`.
- API Server e Webhook desativados por padrão.
- Klaviyo/Calendar/Shopify/Tiny/web/creative por credenciais escopadas.
- Envio Klaviyo/ativação de flow só com dupla confirmação no Telegram.

---

## Gate 0 — Pré-condições e aprovação

- [ ] Lucas aprovou este checklist técnico.
- [ ] Lucas aprovou explicitamente a ativação runtime do perfil `lk-content`.
- [ ] Token do bot está disponível em canal seguro ou será rotacionado no BotFather.
- [ ] Nenhum token será escrito no Brain, PRD, receipts ou logs.
- [ ] Escopo aprovado cobre apenas perfil `lk-content`, sem Docker/VPS/Traefik/Main Hermes.
- [ ] Rollback definido: parar gateway `lk-content`, remover/renomear `.env` sensível, restaurar backup de config se necessário.

## Gate 1 — Criar perfil Hermes isolado

- [ ] Verificar perfis existentes: `hermes profile list`.
- [ ] Criar perfil: `hermes profile create lk-content`.
- [ ] Confirmar diretório: `/opt/data/profiles/lk-content`.
- [ ] Backupar config inicial do perfil.
- [ ] Garantir que o perfil não herdou token Telegram do default.
- [ ] Garantir `API_SERVER_ENABLED=false`.
- [ ] Limpar/desativar `API_SERVER_KEY`, `API_SERVER_PORT`, `API_SERVER_HOST` se herdados.
- [ ] Garantir `WEBHOOK_ENABLED=false`.
- [ ] Limpar/desativar `WEBHOOK_PORT`, `WEBHOOK_SECRET` se herdados.

## Gate 2 — Configurar identidade e toolsets

- [ ] Instalar/copiar skills relevantes para o perfil ou habilitar acesso às skills necessárias.
- [ ] Configurar toolsets Telegram mínimos para operação do LK Content:
  - skills;
  - memory/session context conforme perfil;
  - web/search;
  - file/Brain;
  - messaging/Telegram;
  - cronjob quando crons forem aprovados;
  - MCP/APIs necessárias quando configuradas.
- [ ] Evitar terminal amplo em Telegram se não for necessário para operação cotidiana.
- [ ] Manter CLI/manutenção com ferramentas mais amplas se necessário.

## Gate 3 — Bot Telegram

- [ ] Validar `getMe` sem imprimir token.
- [ ] Confirmar username esperado: `hermes_lk_producaodeconteudo_bot`.
- [ ] Gravar token apenas em `/opt/data/profiles/lk-content/.env` com permissão restrita.
- [ ] Autorizar Lucas.
- [ ] Autorizar Renan.
- [ ] Enviar probe curto para Lucas.
- [ ] Enviar probe curto para Renan.
- [ ] Confirmar inbound+response nos logs do perfil.

## Gate 4 — Brain package

- [ ] Criar pacote `agentes/lk-content/`.
- [ ] Criar/validar `IDENTITY.md`.
- [ ] Criar/validar `SOUL.md`.
- [ ] Criar/validar `AGENTS.md`.
- [ ] Criar/validar `USER.md`.
- [ ] Criar/validar `MEMORY.md`.
- [ ] Criar/validar `TOOLS.md`.
- [ ] Criar/validar `HEARTBEAT.md`.
- [ ] Criar/validar `MAPA.md`.
- [ ] Atualizar `areas/lk/sub-areas/content/MAPA.md`.

## Gate 5 — Klaviyo

- [ ] Criar/obter credenciais Klaviyo com escopo mínimo necessário.
- [ ] Validar leitura de campanhas, listas, segmentos, flows e métricas.
- [ ] Criar draft de campanha teste em ambiente/escopo seguro.
- [ ] Criar/editar template teste.
- [ ] Criar/editar segmento teste.
- [ ] Auditar flow teste sem ativar.
- [ ] Validar que envio/agendamento/ativação exigem dupla confirmação Telegram.
- [ ] Validar bloqueio de deleção sem aprovação específica.
- [ ] Registrar receipt sanitizado.

## Gate 6 — Google Calendar

- [ ] Confirmar acesso ao calendário/conta `lk@lksneakers.com.br`.
- [ ] Criar evento teste `LK Content Smoke Test`.
- [ ] Atualizar evento teste.
- [ ] Validar que não mexe em calendários pessoais/fora do escopo.
- [ ] Validar política de não apagar sem confirmação.
- [ ] Registrar receipt sanitizado.

## Gate 7 — Shopify/Tiny

- [ ] Validar Tiny leitura apenas.
- [ ] Validar Shopify leitura.
- [ ] Validar escrita Shopify apenas com aprovação:
  - tags;
  - metafields de marketing;
  - coleções de campanha.
- [ ] Validar bloqueio para preço, estoque, tema live, descrição principal e publicação/despublicação sem aprovação específica.
- [ ] Registrar receipt sanitizado.

## Gate 8 — Pesquisa, LK Growth e LK Trends

- [ ] Definir protocolo de consulta sob demanda ao LK Growth.
- [ ] Definir protocolo de relatório periódico do LK Growth.
- [ ] Definir protocolo de consulta sob demanda ao LK Trends.
- [ ] Definir protocolo de relatório periódico do LK Trends.
- [ ] Criar template de pedido de inteligência.
- [ ] Criar template de resposta/handoff.

## Gate 9 — Brand/Content Guide vivo

- [ ] Criar estrutura `brand-guide/`.
- [ ] Rodar auditoria inicial de newsletters antigas, Instagram/TikTok, site/Shopify/produtos e referências aprovadas.
- [ ] Criar guia principal.
- [ ] Criar módulos de voz, visual, newsletter, social, produtos, Klaviyo e segmentação.
- [ ] Criar changelog.
- [ ] Criar exemplos aprovados/reprovados.
- [ ] Definir confiança dos aprendizados.

## Gate 10 — Crons próprios

- [ ] Criar cron calendário mensal dia 1.
- [ ] Criar cron planejamento semanal segunda.
- [ ] Criar mecanismo de pós-mortem 48h após envio.
- [ ] Criar alertas de oportunidade/risco.
- [ ] Garantir Telegram anti-ruído: só decisões, entregas planejadas, riscos e alertas acionáveis.
- [ ] Registrar rollback para cada cron.

## Gate 11 — Smoke de campanha ponta a ponta

- [ ] Gerar pesquisa para uma campanha fictícia/segura.
- [ ] Montar estratégia.
- [ ] Selecionar produtos por score sem estoque.
- [ ] Criar copy premium.
- [ ] Criar variações A/B.
- [ ] Criar UTMs.
- [ ] Criar checklist compliance.
- [ ] Criar draft Klaviyo.
- [ ] Criar evento Calendar.
- [ ] Entregar pacote completo no Telegram.
- [ ] Validar aprovação de copy separada de criativo.
- [ ] Validar dupla confirmação para envio/ativação, sem executar envio real se não aprovado.

## Gate 12 — Verificação final

- [ ] Gateway `lk-content` rodando com `HERMES_HOME=/opt/data/profiles/lk-content`.
- [ ] API/webhook desativados no processo vivo.
- [ ] Logs sem token/secrets.
- [ ] Lucas round-trip OK.
- [ ] Renan round-trip OK.
- [ ] Klaviyo smoke OK.
- [ ] Google Calendar smoke OK.
- [ ] Shopify/Tiny guardrails OK.
- [ ] Secret scan dos artifacts OK.
- [ ] Receipt final salvo em `receipts/`.

---

## Comandos de referência — não executar sem aprovação de runtime

```bash
HERMES_HOME=/opt/data /opt/data/hermes-0.15.1-venv/bin/hermes profile create lk-content
HERMES_HOME=/opt/data/profiles/lk-content /opt/data/hermes-0.15.1-venv/bin/hermes config path
HERMES_HOME=/opt/data/profiles/lk-content /opt/data/hermes-0.15.1-venv/bin/hermes gateway run
```

> Observação: ajustar o binário Hermes ao runtime real antes da execução. Validar versão/caminho no momento da implementação.

---

## Critério de pronto

Só considerar implementação completa quando houver evidência real de:

- perfil criado;
- bot validado;
- Lucas e Renan respondidos;
- Klaviyo testado;
- Calendar testado;
- Brain package instalado;
- crons criados e verificados;
- envio/ativação bloqueados por dupla confirmação;
- receipts sanitizados;
- secret scan limpo.
