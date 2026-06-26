# LK OS — “Fazer tudo” com escopo limitado

Gerado em: `2026-06-12T11:28:38Z`
Status: `active_rule_verified`

## Decisão

Lucas aprovou na Mesa COO 2026-06-12 a regra: **“Fazer tudo” não é autorização ampla**.

Quando Lucas usa uma frase ampla como `Fazer tudo`, `seguir tudo`, `continuar tudo` ou equivalente depois de um pacote já validado, a autorização fica limitada ao **mesmo escopo seguro já aprovado**.

## Regra operacional

`Fazer tudo` autoriza somente:

- continuar os alvos já pré-validados do mesmo pacote;
- manter os mesmos campos/canais/sistemas do approval anterior;
- preservar as mesmas exclusões, rollback/readback e classe de risco;
- pular automaticamente qualquer alvo ambíguo ou fora do escopo;
- registrar receipt/readback da execução limitada.

`Fazer tudo` **não** autoriza automaticamente:

- novos campos;
- novos tipos de alvo;
- preço, estoque, título, tema, produto ou cliente;
- Tiny write;
- Shopify write fora do campo já aprovado;
- WhatsApp/e-mail/campanha/cliente/fornecedor;
- produção, Docker/VPS/gateway, banco, cron, secrets ou integrações;
- aplicar em alvos ambíguos ou sem evidência suficiente.

Qualquer expansão exige novo approval packet escopado.

## Evidência que originou a regra

No caso LK Stock / Shopify SKU-only de 2026-06-12:

- Lucas aprovou continuar com “Fazer tudo”.
- A execução correta ficou restrita ao escopo anterior: SKU-only a partir de código Tiny seguro.
- Foram aplicados somente alvos com match exato por tamanho e `codigo` Tiny não vazio.
- 7 alvos ambíguos foram mantidos bloqueados.
- Externos fora do pacote: Tiny write `0`; preço/estoque/título/tema/cliente `0`.

## Materialização local

- SQLite local: `local_sql/lk_os_phase5.sqlite`
- Regra: `LK-APPROVAL-BROAD-CONTINUATION-SCOPE-LIMIT-20260612`
- Ledger: `LK-DECISION-FAZER-TUDO-SCOPE-LIMIT-20260612`
- Testes adicionados:
  - `T09-FAZER-TUDO-SKU-ONLY`
  - `T10-FAZER-TUDO-EXPAND-PRICE-STOCK`
  - `T11-SEGUIR-TUDO-CLIENTE-CAMPANHA`

## O que não foi feito

- Nenhum write externo.
- Nenhuma alteração em Shopify, Tiny, GMC, Klaviyo, Meta, WhatsApp, e-mail, clientes, fornecedores, produção, Docker/VPS/gateway, banco externo, cron ou secrets.

## Uso futuro

Antes de executar continuidade ampla, scripts/agentes devem classificar se a frase ampla apenas continua um pacote seguro já aprovado ou se amplia escopo. Se ampliar, a ação correta é **preparar novo approval packet**, não executar.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `LK OS — “Fazer tudo” com escopo limitado` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `LK OS — “Fazer tudo” com escopo limitado` no caminho `areas/lk/rotinas/lk-os-fazer-tudo-scope-limited-approval-guardrail-2026-06-12.md`.
- Owner operacional: LK Operações / LK OS, com governança Hermes Geral e aprovação final Lucas.

### Escopo permitido
- Escopo permitido somente após aprovação explícita: executar apenas os itens, IDs, fluxos, mensagens, campos ou rotinas descritos neste packet, sem ampliar alvo por inferência.
- Pode fazer localmente sem nova aprovação: validação documental, preview, auditoria read-only, receipt e classificação de blockers.

### O que continua bloqueado
- Não pode fazer qualquer execução produtiva, write externo, cron/runtime/gateway, cliente/fornecedor, preço, estoque, campanha, banco ou integração sem approval packet específico.
- Aprovação genérica como `seguir`, `fazer tudo` ou contexto antigo não amplia escopo; novo alvo exige novo approval packet.

### Risco
- Risco principal: transformar preview/packet em autorização ampla e executar ação sensível fora do escopo exato.
- Mitigação: fail-closed, approval textual específica, backup/snapshot quando aplicável, readback e receipt com contagens.

### Verificação / readback
- Verificação obrigatória: receipt local, readback dos artefatos alterados, contagem de itens afetados/bloqueados e confirmação de zero execução externa não aprovada.
- Se houver divergência de identidade, fonte, escopo ou aprovação, bloquear execução e registrar causa sanitizada.

### Opções de aprovação
- Aprovar exatamente o escopo descrito neste packet.
- Aprovar apenas preview/dry-run/read-only.
- Ajustar alvo/limite antes de executar.
- Bloquear execução e manter como histórico/rascunho.

### Secret hygiene
- Usar credenciais somente via Doppler/wrapper seguro quando houver integração; não imprimir tokens, refresh tokens, passwords, service-account JSON, API keys ou connection strings.
- Relatórios e receipts devem manter `values_printed=false` e redigir qualquer valor sensível como `[REDACTED]`.
