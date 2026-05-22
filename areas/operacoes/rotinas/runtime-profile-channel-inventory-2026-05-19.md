# Inventário runtime / profile / canal — Hermes

Data: 2026-05-19  
Tipo: documentação P0 segura após auditoria BRUNO-ATUAL  
Escopo: matriz única para registrar profiles, bots, canais, destinos, cadência, status, contrato de silêncio e kill criteria.  
Ação executada nesta rodada: documentação somente. Nenhum cron, bot, canal, Docker, VPS, API, banco ou envio externo foi alterado.

## Princípio

Rotina documentada não prova execução ativa. Antes de dizer que algo roda, verificar a fonte real do runtime no ambiente autorizado e registrar evidência com timestamp.

## Status desta versão

- Este arquivo é o lugar canônico para consolidar o inventário.
- As linhas abaixo começaram como inventário documental inicial, derivado do Brain versionado e da auditoria BRUNO-ATUAL.
- Atualização live parcial em 2026-05-19: `cronjob list` verificado no runtime Hermes; jobs relevantes reconciliados abaixo.
- Campos `status runtime` marcados como `não verificado nesta rodada` ainda exigem checagem live antes de qualquer afirmação operacional.

## Matriz inicial

| Profile / agente | Canal / bot | Destino | Escopo | Cadência | Status runtime | Silent contract | Kill criteria | Fonte documental |
|---|---|---|---|---|---|---|---|---|
| Hermes Geral | Telegram | Lucas / interface principal | Chief of Staff, roteamento multiempresa, Brain, aprovações, Mesa COO | Sob demanda + Mesa diária 08h30 BRT | ativo parcial: cron `749ee30b51eb` Mesa COO diária Telegram; `f5a23dd6a1bd` Brain daily intelligence loop ativo | Não interromper sem utilidade; pedir aprovação para externo/prod | Erro de contexto, risco de segredo, envio externo sem aprovação | `agentes/hermes-geral/`, `AGENTS.md`, `areas/operacoes/rotinas/mesa-coo-diaria-telegram-2026-05-19.md` |
| LK | Telegram / Hermes | Lucas / operação LK | Ecommerce, CRM, Growth, SEO/CRO, Shopify/Tiny/GA4/GSC/GMC read-only quando permitido | Sob demanda + rotinas documentadas | ativo parcial: LK Daily Sales, Weekly CEO, 16h, 09h, 19h30 e watchdogs; alguns SEO/GMC pausados | Alertar só quando houver decisão/bloqueio/entrega obrigatória | Dado sem fonte viva, mistura com Zipper/SPITI, write sem aprovação | `agentes/lk/`, `areas/lk/` |
| Zipper | Telegram / Hermes | Lucas / operação Zipper | Galeria, vendas de obras, artistas, colecionadores, comunicação | Sob demanda + rotina de vendas 09h | ativo parcial: cron `357d40a5863e` Zipper OS vendas 09h WhatsApp/email ativo | Sem contato externo automático; rascunho antes de mensagem | Tom inadequado, lead/colecionador sem aprovação, fonte de venda não confirmada | `agentes/zipper/`, `areas/zipper/` |
| SPITI | Telegram / Hermes | Lucas / operação SPITI | Leilão, lotes, lances, CRM SPITI | Sob demanda + rotinas documentadas | não verificado nesta rodada | Silêncio é melhor que dado errado | Divergência de lance/lote sem evidência, resposta durante pregão sem fonte | `agentes/spiti/`, `areas/spiti/` |
| Mordomo | Telegram/WhatsApp pessoal | Lucas / atendimento interno e triagem | Concierge operacional, intake, follow-up, organização de pedidos e canais | Scan 15min + resumo 17h + watchdog | ativo parcial: crons `051f05ce17c1`, `4ced266825f0`, `ac0b440e2643` ativos | Não enviar nada externo; só organizar/rascunhar até aprovação | Confundir com Hermes Geral, agir fora do escopo, contato sem aprovação | `agentes/mordomo/` |
| Brain Sync | Script/rotina | Repositório Brain | Sync/versionamento e higiene do Brain | Conforme rotina; confirmar live | não verificado nesta rodada | Reportar falha relevante; sucesso silencioso quando esperado | Divergência de branch, conflito, segredo em diff | `skills/brain-sync/`, `areas/operacoes/rotinas/brain-sync.md` |
| Brain Health Check | Script local | Reports do Brain | Validação de estrutura/links/secrets/skills/rotinas | Sob demanda nesta rodada | executado localmente na verificação desta branch | Só reportar falhas/warnings | FAIL/WARN relevante ou segredo | `scripts/brain_health_check.py` |
| LK Daily/Weekly/GMC/SEO rotinas | Cron/no_agent quando aprovado | Reports internos LK | Relatórios e guards read-only | Ver docs por rotina; confirmar live | não verificado nesta rodada | Entregas obrigatórias conforme docs; sem spam | Falha de fonte, dado stale, write externo, envio sem aprovação | `empresa/rotinas/_index.md`, `areas/lk/rotinas/` |

## Campos obrigatórios para novas linhas

- `profile/agente`: nome humano e diretório de docs quando existir.
- `canal/bot`: Telegram, WhatsApp, email, n8n, cron, no_agent, script, webhook etc.
- `destino`: quem recebe ou onde aparece.
- `escopo`: o que pode fazer.
- `cadência`: sob demanda, diária, semanal, evento, manual.
- `status runtime`: ativo, pausado, draft, não criado, não verificado, falhando; sempre com evidência quando live.
- `silent contract`: quando deve ficar quieto e quando deve avisar.
- `kill criteria`: condições de desligar/pausar.
- `fonte documental`: arquivo do Brain que sustenta a linha.

## Procedimento para atualização live

1. Obter aprovação se a checagem exigir Docker/VPS/root/runtime/API sensível.
2. Rodar apenas leitura: cron list, status de bot/profile, health endpoint, logs necessários, sem restart/deploy/write.
3. Registrar timestamp, comando/fonte, resultado resumido e limitações.
4. Nunca copiar tokens, chat IDs sensíveis privados, headers ou valores de secrets.
5. Se descobrir runtime ativo sem documentação, criar rotina/doc antes de ampliar escopo.

## Ponte Mission Control

Mission Control deve consumir esta matriz como fonte documental, mas a reconciliação detalhada do repo/UI/runtime fica fora desta rodada. Ponte criada em `areas/operacoes/projetos/mission-control-reconciliation-pointer-2026-05-19.md`.
