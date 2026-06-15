# LK SEO/CRO — aprovação do roteador comercial

Data: 2026-05-18 13:39 UTC
Empresa: LK Sneakers
Sistema: Hermes Brain / LK OS
Status: aprovado por Lucas para internalizar como regra operacional e próximo bloco de implementação.

## Decisão aprovada

Lucas aprovou a recomendação de corrigir o módulo semanal LK SEO/CRO para deixar de priorizar páginas por HTML público e passar a priorizar por lógica comercial.

A regra aprovada é:

> LK SEO/CRO deve começar por vendas, visitas/sessões, conversão, receita, estoque/disponibilidade, margem/comercialidade, GSC impressões/cliques/CTR/posição e risco real de Merchant/feed. Auditoria pública/HTML entra depois, apenas como diagnóstico das páginas comercialmente relevantes.

## O que fica salvo no Hermes Brain

1. Fonte de verdade operacional:
   - `areas/lk/rotinas/lk-seo-cro-commercial-router-approval-2026-05-18.md` — este registro de aprovação.
   - `reports/lk-seo-cro-weekly-2026-05-18-correction-commercial.md` — emenda comercial do relatório ruim.
   - `reports/lk-seo-cro-weekly-2026-05-18-correction-commercial.json` — payload estruturado da emenda.

2. Código/roteador read-only:
   - `scripts/lk_seo_cro_commercial_router_20260518.py` — roteador comercial read-only que roda GSC + GA4/PDP low-conversion e gera a emenda.

3. Governança recorrente:
   - skill `lk-seo-weekly-improvement` atualizada com a correção.
   - cron `15777e3416dc` atualizado para exigir o roteador comercial antes de qualquer ranking por HTML.

## O que entra no LK OS

Este bloco entra no LK OS como evolução da **Fase 6 — SEO, Search Console e Merchant Center**:

- `SEO/CRO Commercial Opportunity Router` como módulo oficial de priorização;
- public HTML/Claude SEO rebaixado para camada diagnóstica;
- ranking semanal só pode ser emitido quando houver evidência comercial suficiente;
- se faltar vendas/visitas/conversão/GSC, o relatório deve sair como `incompleto / não decision-grade`;
- recomendações de PDP/collection devem ter evidência comercial + diagnóstico SEO/CRO + aprovação necessária.

## Próximo bloco aprovado para execução interna

Implementar o join comercial único por `URL / handle / SKU`, sem writes externos:

- Shopify vendas/pedidos/receita;
- GA4 sessões/conversão/compras/receita por página;
- GSC impressões/cliques/CTR/posição por página/query;
- GMC issues por item/SKU quando houver match;
- estoque/disponibilidade;
- margem/comercialidade quando disponível;
- HTML/SEO audit apenas das páginas vencedoras.

Output esperado:

- `reports/lk-seo-cro-commercial-opportunity-router-YYYY-MM-DD.json`
- `reports/lk-seo-cro-commercial-opportunity-router-YYYY-MM-DD.md`
- fila P1/P2/P3 com evidência comercial, risco, esforço, approval status e `writes_allowed_now: 0`.

## Execução do Bloco 1 — 2026-05-18

Implementado e executado read-only em:

- `scripts/lk_seo_cro_commercial_opportunity_router_20260518.py`
- `reports/lk-seo-cro-commercial-opportunity-router-2026-05-18.json`
- `reports/lk-seo-cro-commercial-opportunity-router-2026-05-18.md`
- `reports/lk-seo-cro-commercial-opportunity-router-2026-05-18.csv`

Resultado:

- 52 URLs avaliadas.
- 13 P1, 6 P2, 21 P3, 12 data-gap.
- Join feito com GA4, GSC, Shopify/local spine, Tiny parcial, GMC disponível e HTML público apenas diagnóstico.
- `writes_allowed_now: 0`.

Limitações registradas:

- Shopify/local spine de pedidos termina em 2026-04-16; vendas recentes precisam de refresh por linha de item/handle.
- Tiny snapshot está `partial_api_rate_limited`; estoque precisa ser rechecado antes de qualquer write.
- Collections ainda usam match por tokens; próximo passo é membership exato Shopify.
- Margem/custo confiável ainda não entrou no score.

## Guardrails

Livre sem nova aprovação:

- leitura read-only de Shopify/GA4/GSC/GMC/Tiny quando credenciais já existirem;
- criação de scripts locais;
- geração de relatórios/JSON no Brain;
- previews de title/meta/CRO;
- atualização de skill/rotina/cron read-only.

Ainda exige aprovação explícita de Lucas com payload + alvo + rollback:

- alterar Shopify SEO fields;
- alterar tema/dev theme ou conteúdo visível;
- alterar feed/GMC;
- enviar e-mail/WhatsApp/Telegram/campanha;
- criar automação com write externo.

## Critério de pronto do próximo bloco

- Roteador gera fila com dados comerciais cruzados.
- Top 5 não contém páginas sem venda/visita/demanda/estoque/valor estratégico.
- Itens excluídos aparecem claramente com motivo.
- Relatório semanal novo usa a fila comercial como base.
- LK OS implementation control aponta este módulo como regra oficial da Fase 6.
- Mission Control pode consumir o artifact como snapshot read-only depois.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `LK SEO/CRO — aprovação do roteador comercial` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `LK SEO/CRO — aprovação do roteador comercial` no caminho `areas/lk/rotinas/lk-seo-cro-commercial-router-approval-2026-05-18.md`.
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
