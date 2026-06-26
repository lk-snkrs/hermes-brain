# LK SEO/CRO — Bloco 3 P1 Approval Packets

Data: 2026-05-18
Status: gerado como preview read-only; nenhuma aplicação executada.

## Objetivo

Converter a fila `decision-grade refresh` em packets acionáveis para decisão do Lucas, mantendo separação clara entre:

- SEO fields Shopify (`seo.title` e `seo.description`);
- CRO visível / tema dev;
- estoque/sourcing dependente de Tiny/margem;
- execução externa bloqueada até aprovação explícita.

## Artefatos

- Script: `scripts/lk_seo_cro_approval_packets_from_decision_refresh_20260518.py`
- JSON: `reports/lk-seo-cro-p1-approval-packets-2026-05-18.json`
- Markdown: `reports/lk-seo-cro-p1-approval-packets-2026-05-18.md`
- CSV: `reports/lk-seo-cro-p1-approval-packets-2026-05-18.csv`
- Fonte: `reports/lk-seo-cro-decision-grade-refresh-2026-05-18.json`

## Resultado

- Packets gerados: 8.
- Status: 8 `needs_approval`.
- Public HTML fetch: 8/8 OK.
- `write_allowed_now`: 0.
- Cada packet contém:
  - URL/alvo;
  - evidência comercial GA4/GSC/Shopify live;
  - title/meta/H1 públicos atuais;
  - proposta exata de SEO title/meta com contagem de caracteres;
  - plano de rollback;
  - hipóteses CRO visíveis separadas;
  - frase de aprovação necessária.

## Packets P1 gerados

1. Onitsuka Tiger todos os modelos — SEO title preview: `Onitsuka Tiger Original na LK Sneakers`.
2. New Balance 204L — SEO title preview: `New Balance 204L Original na LK Sneakers`.
3. Air Jordan Travis Scott — SEO title preview: `Air Jordan Travis Scott Original na LK Sneakers`.
4. Lululemon — SEO title preview: `Lululemon Original na LK Sneakers`.
5. Adidas Samba Jane — SEO title preview: `Adidas Samba Jane Original na LK Sneakers`.
6. Onitsuka Tiger Kill Bill PDP — SEO title preview: `Onitsuka Tiger Mexico 66 Kill Bill Amarelo | LK Sneakers`.
7. Onitsuka Tiger Mexico 66 — SEO title preview: `Onitsuka Tiger Mexico 66 Original na LK Sneakers`.
8. Nike Mind 001 — SEO title preview: `Nike Mind 001 Original na LK Sneakers`.

## Frase de aprovação necessária se Lucas quiser aplicar depois

> Aprovo aplicar somente os campos SEO title/meta dos packets listados, sem alterar H1/body/tema/preço/estoque/campanhas, com rollback salvo antes.

A aprovação de SEO fields não aprova CRO visível. CRO visível precisa de dev theme/preview e aprovação separada.

## Guardrails executados

Não foi executado:

- Shopify Admin mutation/write;
- alteração de tema/conteúdo;
- Tiny API/write;
- Merchant/feed write;
- GA4/GSC write;
- WhatsApp/e-mail/campanha;
- contato com fornecedor;
- preço/estoque;
- cron novo.

## Validação

- Script compilou com `py_compile`.
- JSON validado: 8 packets, 8 `needs_approval`, `write_allowed_now=0`, titles <= 60 chars, metas <= 155 chars, rollback presente.
- Secret scan nos arquivos gerados: 0 matches.

## Próximo bloco seguro

Escolha operacional recomendada: preparar **aplicação SEO-field-only** como runner gated, mas ainda não executar. O runner deve:

1. reconsultar Shopify Admin SEO fields por produto/collection antes da aplicação;
2. salvar snapshot rollback exato;
3. aplicar somente `seo.title` e `seo.description` dos packets aprovados;
4. verificar readback Admin e público;
5. registrar receipt/rollback;
6. manter H1/body/tema/preço/estoque/campanhas intocados.

Alternativa: avançar no estoque Tiny em lotes/cooldown antes de qualquer sourcing/estoque.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `LK SEO/CRO — Bloco 3 P1 Approval Packets` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `LK SEO/CRO — Bloco 3 P1 Approval Packets` no caminho `areas/lk/rotinas/lk-seo-cro-p1-approval-packets-2026-05-18.md`.
- Owner operacional: LK Growth / GMC / SEO-CRO, com governança Hermes Geral e aprovação final Lucas.

### Escopo permitido
- Escopo permitido somente após aprovação explícita: executar apenas os itens, IDs, fluxos, mensagens, campos ou rotinas descritos neste packet, sem ampliar alvo por inferência.
- Pode fazer localmente sem nova aprovação: validação documental, preview, auditoria read-only, receipt e classificação de blockers.

### O que continua bloqueado
- Não pode fazer Merchant/Shopify/Tiny/feed/campanha/cliente/fornecedor, preço, estoque, tema, anúncios ou envio externo fora do escopo exato aprovado.
- Aprovação genérica como `seguir`, `fazer tudo` ou contexto antigo não amplia escopo; novo alvo exige novo approval packet.

### Risco
- Risco principal: transformar preview/packet em autorização ampla e executar ação sensível fora do escopo exato.
- Mitigação: fail-closed, approval textual específica, backup/snapshot quando aplicável, readback e receipt com contagens.

### Verificação / readback
- Verificação obrigatória: readback da fonte afetada quando aplicável, comparação com preview/CSV/JSON, contagem de aplicados/bloqueados/divergentes e receipt com `values_printed=false`.
- Se houver divergência de identidade, fonte, escopo ou aprovação, bloquear execução e registrar causa sanitizada.

### Opções de aprovação
- Aprovar exatamente o escopo descrito neste packet.
- Aprovar apenas preview/dry-run/read-only.
- Ajustar alvo/limite antes de executar.
- Bloquear execução e manter como histórico/rascunho.

### Secret hygiene
- Usar credenciais somente via Doppler/wrapper seguro quando houver integração; não imprimir tokens, refresh tokens, passwords, service-account JSON, API keys ou connection strings.
- Relatórios e receipts devem manter `values_printed=false` e redigir qualquer valor sensível como `[REDACTED]`.
