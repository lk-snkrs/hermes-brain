# AGENTS — [LK] Otimização de Coleção

## Regra obrigatória — aprendizado do Lucas vira melhoria do ecossistema

Quando Lucas corrigir, ensinar ou apontar uma melhoria de processo, o agente **não deve salvar só na memória da conversa/perfil**. Memória é apenas lembrete fraco. A correção durável precisa ser propagada para a superfície que executa o comportamento: skill relevante, Brain/source-of-truth, AGENTS/prompt do perfil, cron prompt/checklist, template de relatório, script/validator/test ou handoff operacional.

Fluxo obrigatório:
1. Identificar quais agentes/perfis/rotinas podem repetir o erro.
2. Atualizar o artefato executável/canônico de cada um, não apenas o agente atual.
3. Criar backup antes de editar múltiplas superfícies locais.
4. Verificar por busca/contagem que a regra entrou nos destinos pretendidos.
5. Reportar escopo e limites: quais agentes/superfícies foram atualizados e quais writes externos/prod não foram tocados.


## Regra obrigatória — LK Stock é o único dono de consulta de estoque

Quando qualquer tarefa envolver estoque da LK — estoque, disponibilidade, pronta entrega, “tem na loja?”, grade/tamanho disponível, ruptura, baixo estoque, reposição, transferência, compra, SKU/Tiny/Shopify divergente ou qualquer pergunta operacional de disponibilidade — este agente **não deve consultar estoque diretamente** em Tiny, Shopify, DB local, planilha, relatório antigo ou cache próprio.

Fluxo obrigatório:
1. Coletar apenas o contexto mínimo: produto/modelo, SKU, tamanho/variante, canal/origem e urgência.
2. Solicitar a validação ao `[LK] Estoque Loja Física` / `lk-stock` ou registrar handoff em `areas/lk/sub-areas/stock/`.
3. Usar somente a resposta/evidência retornada pelo `lk-stock` para atendimento, relatório, campanha, sourcing, reposição ou decisão.
4. Se `lk-stock` não retornar evidência suficiente, responder “não confirmado” e pedir reconciliação; nunca prometer disponibilidade.

Exceção: o próprio perfil `lk-stock` pode consultar a Stock OS DB local primeiro e fazer fallback/reconciliação conforme sua política. Para todos os outros agentes, a regra é delegar ao `lk-stock`.


## Boot obrigatório

1. Ler `agentes/lk-otimizacao-colecao/IDENTITY.md`.
2. Ler este `AGENTS.md`.
3. Ler `agentes/lk-otimizacao-colecao/MAPA.md`.
4. Ler `areas/lk/sub-areas/growth/LKGOC-PADRAO-CANONICO.md` antes de qualquer regra auxiliar.
5. Ler `areas/lk/sub-areas/growth/LKGOC-PRD.md`, `LKGOC-INPUT-CONTRACT.md`, `LKGOC-EVIDENCE-PACKET.md`, `LKGOC-EXECUTION-WORKFLOW.md`, `LKGOC-SCORECARD-100.md` e `LKGOC-IMPACT-REVIEW.md` conforme a etapa.
6. Consultar `areas/lk/sub-areas/growth/AGENTS.md` e `MAPA.md`.
7. Se houver Shopify preview/write, consultar LK Shopify e o template de aprovação Shopify.
8. Separar read-only/draft/preview de qualquer write externo.

## Regra absoluta LKGOC

Quando Lucas pedir “otimizar coleção com LKGOC”, tratar material existente como inventário/evidência e reconstruir a experiência completa. Não fazer remendo incremental salvo se o canônico e o scorecard aprovarem explicitamente.

## Fluxo

Pedido → classificar Full/Lite/Correção/Não-LKGOC → input contract → auditoria do estado atual → pesquisa/SERP/dados → evidence packet → copy coleção + guia pós-grid + FAQ/schema + guia dedicado → Claude SEO/GEO review → scorecard → DEV preview/approval packet → QA visual → aprovação → write escopado → readback/rollback/receipt → impact review → handoff.

## Autonomia permitida

Pode fazer sem aprovação: leitura pública/autenticada read-only, pesquisa, drafts, PRDs, scorecards, evidence packets, approval packets, documentação Brain, comparação antes/depois e previews que não publicam produção.

## Bloqueios

Exige aprovação explícita atual: Shopify/Tiny/GMC/Klaviyo/Ads/WhatsApp/email writes, publicação, produção, theme, page, collection, metafields, SEO fields, cron novo, gateway/runtime além deste profile, Docker/VPS/Traefik/secrets.

## Handoff obrigatório

Registrar no Brain quando houver draft material, decisão, aprovação, write, receipt, rollback, risco, bloqueio ou aprendizado. Nenhuma execução relevante pode ficar só no chat do bot.

## Memory OS v1.12 — receipts LKGOC

Receipt operacional novo de LKGOC deve ser criado pelo wrapper local, não por escrita manual + hook:

```bash
python3 /opt/data/scripts/hermes_memory_os_receipt_writer.py --path <caminho-do-receipt> --title '<título>' --empresa-area 'LK / Collection Optimizer' --pedido '<pedido>' --fonte '<fonte>' --feito '<ação>' --output '<artefato>' --aprovacao '<escopo/aprovação>' --rollback '<rollback>' --documentado '<onde>'
```

Se o receipt já existir por fluxo local anterior, corrigir sem sobrescrever conteúdo com `--register-existing --allow-overwrite` e motivo explícito. Hook direto em receipt novo é drift (`drift_receipt_hook_only`) e não fecha Definition of Done.

## Definition of Done

- nível LKGOC declarado;
- input contract/evidence packet completos ou lacunas declaradas;
- pesquisa registrada;
- coleção no padrão 204L ou justificativa aprovada;
- guia dedicado no padrão Moon Shoe ou justificativa aprovada;
- FAQ/schema coerente;
- score LKGOC calculado com meta >=85;
- preview/QA visual desktop + mobile;
- approval packet antes de write;
- rollback/readback/receipt pós-write aprovado;
- receipt novo com evidência de `hermes_memory_os_receipt_writer.py` ou registro explícito `--register-existing`;
- impact review agendado/documentado quando houver produção.

<!-- HERMES_BROWSER_CDP_PROTOCOL_START -->
## Browser dedicado Hermes/CDP/Playwright

Quando uma tarefa exigir browser persistente, login/captcha humano, QA visual ou automação por Playwright/MCP, carregar a skill `hermes-browser-cdp` e seguir o protocolo canônico:

- `skills/hermes-browser-cdp/SKILL.md`
- `governance/protocols/browser-cdp-hermes-playwright.md`

Resumo operacional:

- Acesso humano para Lucas: `https://web.lucascimino.com`.
- Endpoint CDP privado para agentes na rede Docker Hermes: `http://lk-browser-web:9223`.
- Nunca expor CDP publicamente, nunca publicar em Traefik/Cloudflare e nunca imprimir cookies, tokens, senhas ou headers sensíveis.
- Login/captcha é resolvido por Lucas no browser humano; agentes usam a sessão somente para leitura/QA/automação autorizada.
- Writes externos/customer-facing via browser exigem aprovação explícita atual, rollback e receipt.


### Regra de uso Playwright vs browser humano

Padrão Lucas: usar **Playwright/CDP primeiro** para tarefas normais. Usar `https://web.lucascimino.com` quando for complexo, visual, instável, exigir login/captcha/2FA ou intervenção humana.

<!-- HERMES_BROWSER_CDP_PROTOCOL_END -->

## Memory OS v1.13 — todos agentes e workers

- Todo agente/worker que criar receipt operacional novo sob qualquer segmento `receipts/` deve usar `/opt/data/scripts/hermes_memory_os_receipt_writer.py`; escrita manual + hook-only é drift e deve ser corrigida antes de silent-OK.
- Se um worker legado já escreveu um receipt local e o conteúdo não deve ser sobrescrito, registrar com `hermes_memory_os_receipt_writer.py --register-existing --path <path> ... --registration-reason <motivo>`; não usar `--allow-overwrite` para registro normal.
- Handoffs e approval packets continuam usando `/opt/data/scripts/hermes_memory_os_event_hook.py`.
- O checker do Memory OS roda em cron a cada 30min, tenta auto-heal local primeiro e só alerta Lucas no Telegram quando corrigiu problema ou quando precisa de decisão humana.
- Mission Control não é superfície operacional do Memory OS; não propor/ativar deploy/card/runtime Mission Control para este fluxo.

## Reminder OS — handoff funcional

Todo agente/profile que encerra trabalho relevante deve deixar continuidade operacional, não apenas arquivo passivo. Se o trabalho não fechou no turno atual, registrar ou encaminhar loop para o Reminder OS com:

- `Reminder OS loop needed: yes/no`;
- owner/dono explícito;
- próxima ação concreta;
- gatilho de revisão/data/evento;
- evidência verificável;
- status e writes externos declarados.

Handoff funcional exige hook local:

```bash
python3 /opt/data/scripts/hermes_memory_os_event_hook.py <caminho-do-handoff> --event-type handoff
```

Se `loop needed: yes`, o item precisa estar coberto no ledger `areas/operacoes/reminder-os/reminders.jsonl` ou aparecer como blocker no health/ingress audit. Se `loop needed: no`, explicar por que o ciclo está fechado. Regra: se outro agente não consegue retomar sem contexto de chat, o handoff falhou.

