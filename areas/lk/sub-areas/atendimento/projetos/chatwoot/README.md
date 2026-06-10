# Projeto Canônico — Chatwoot / Elle / LK Atendimento

Status: **pasta canônica local/documental ativa**
Criado em: `2026-06-10T18:33:50Z`
Dono lógico: `LK Ops / Atendimento`
Área Brain: `areas/lk/sub-areas/atendimento/projetos/chatwoot/`

## Objetivo

Centralizar, dentro do Brain, tudo que foi feito pelo agente **LK Atendimento** no projeto Chatwoot/Elle/WhatsApp/Shopify/POS, sem apagar os artefatos históricos existentes.

Esta pasta é o **hub canônico de leitura**. Os PRDs, receipts, scripts, reports e approval packets originais continuam em seus diretórios de origem e são indexados aqui.

## Escopo coberto

- Elle / cérebro de atendimento conectado ao Chatwoot.
- Chatwoot + WhatsApp Business API / Evolution API.
- Integração Shopify → Chatwoot: contatos, pedidos, eventos e contexto.
- Sidebar/labels/templates do Chatwoot para operações LK.
- Pós-venda POS / **PÓS VENDA LK FLAGSHIP**.
- Copiloto interno no Chatwoot.
- Diagnósticos read-only de Cloud, inbox, data services e migração.
- Guardrails de atendimento: não prometer preço/estoque/reserva/prazo sem fonte viva e aprovação quando sensível.

## Estado executivo atual

- Total de artefatos Chatwoot inventariados em LK Atendimento: **77**.
- Já rastreados pelo Git local do Brain: **56**.
- Ainda locais/untracked no Brain: **21**.
- Estado POS/Chatwoot: `processed_orders=10; updated_at_utc=2026-06-10T15:45:57.370898+00:00; guardrail=internal Chatwoot records only; no customer-visible Chatwoot messages`.
- Guardrail central preservado: **Chatwoot pode conter registros/notas internas; mensagem visível ao cliente continua bloqueada sem aprovação escopada.**

## Arquivos canônicos nesta pasta

- `CURRENT_STATE.md` — leitura rápida do estado atual e do que já foi feito.
- `DECISIONS_AND_GUARDRAILS.md` — decisões, limites e approval gates.
- `ARTIFACT_INDEX.md` — índice humano completo por categoria.
- `TIMELINE.md` — linha do tempo operacional por data/frente.
- `NEXT_STEPS.md` — próximos passos recomendados e pendências.
- `manifest.json` — inventário estruturado de todos os artefatos encontrados.

## Regra de uso

Antes de qualquer nova ação em Chatwoot/Elle/LK Atendimento:

1. Ler `CURRENT_STATE.md`.
2. Confirmar se a ação é local/read-only ou external-write.
3. Se envolver Chatwoot/Shopify/WhatsApp/Evolution/API/runtime/cliente, exigir fonte viva + aprovação escopada + snapshot/readback/receipt.
4. Registrar novo receipt usando `/opt/data/scripts/hermes_memory_os_receipt_writer.py`.

## Status GitHub

Esta pasta canônica foi commitada e pushada para o repositório `lk-snkrs/hermes-brain`.

- Branch: `consolidation/brain-filesystem-git-hygiene-20260516`
- Commit inicial do hub: `7d3566a3a7c091d50494aeddcf042fb0d19bd8b7`

## O que esta consolidação NÃO fez

- Não moveu nem apagou arquivos históricos.
- Não alterou Chatwoot, Shopify, WhatsApp, Evolution, Docker, VPS, gateway, cron ou runtime.
- Não copiou secrets para esta pasta.
