# LK Sourcing v11 — Pacote P1 para aprovação de compra manual

Generated: `2026-05-15T01:21:46.887735+00:00`

- Itens P1: 4
- Custo estimado total: R$ 4.465,92
- Valor site LK: R$ 11.199,96
- Lucro bruto estimado: R$ 6.734,04
- Margem combinada: 60.1%

## Itens P1
### #1 — Tênis New Balance 204L Arid Timberwolf Bege — BR 37
- SKU: `U204LMMC-4`
- Rota: Importar
- Preço Droper: R$ 1.999,90
- StockX/GOAT: US$ 109.00
- Custo: R$ 1.077,80
- Site LK: R$ 2.799,99
- Margem: 61.5%
- Estado: Aguardando decisão manual do Júlio/Lucas

### #2 — Tênis New Balance 204L Arid Timberwolf Bege — BR 39
- SKU: `U204LMMC-6`
- Rota: Importar
- Preço Droper: R$ 2.380,00
- StockX/GOAT: US$ 109.00
- Custo: R$ 1.077,80
- Site LK: R$ 2.799,99
- Margem: 61.5%
- Estado: Aguardando decisão manual do Júlio/Lucas

### #3 — Tênis New Balance 204L Arid Timberwolf Bege — BR 38
- SKU: `U204LMMC-5`
- Rota: Importar
- Preço Droper: R$ 1.999,90
- StockX/GOAT: US$ 115.00
- Custo: R$ 1.108,74
- Site LK: R$ 2.799,99
- Margem: 60.4%
- Estado: Aguardando decisão manual do Júlio/Lucas

### #4 — Tênis New Balance 204L Arid Timberwolf Bege — BR 40
- SKU: `U204LMMC-7`
- Rota: Importar
- Preço Droper: R$ 2.380,00
- StockX/GOAT: US$ 133.00
- Custo: R$ 1.201,57
- Site LK: R$ 2.799,99
- Margem: 57.1%
- Estado: Aguardando decisão manual do Júlio/Lucas

## Texto de aprovação sugerido
Aprovo o lote P1 para o Júlio conferir disponibilidade e executar compra manual dos 4 itens, mantendo Hermes sem compra, contato, pagamento ou reserva automática.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `LK Sourcing v11 — Pacote P1 para aprovação de compra manual` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `LK Sourcing v11 — Pacote P1 para aprovação de compra manual` no caminho `areas/lk/rotinas/mission-control-sourcing-p1-approval-packet-v11-2026-05-15.md`.
- Owner operacional: LK Sourcing / LK Operações, com governança Hermes Geral e aprovação final Lucas.

### Escopo permitido
- Escopo permitido somente após aprovação explícita: executar apenas os itens, IDs, fluxos, mensagens, campos ou rotinas descritos neste packet, sem ampliar alvo por inferência.
- Pode fazer localmente sem nova aprovação: validação documental, preview, auditoria read-only, receipt e classificação de blockers.

### O que continua bloqueado
- Não pode fazer contato com fornecedor, cotação enviada, compra, reserva, negociação, pagamento, mensagem externa ou alteração de preço/estoque sem approval packet específico.
- Aprovação genérica como `seguir`, `fazer tudo` ou contexto antigo não amplia escopo; novo alvo exige novo approval packet.

### Risco
- Risco principal: transformar preview/packet em autorização ampla e executar ação sensível fora do escopo exato.
- Mitigação: fail-closed, approval textual específica, backup/snapshot quando aplicável, readback e receipt com contagens.

### Rollback
- Rollback obrigatório: reverter somente a alteração aprovada usando backup/snapshot/artefato anterior quando aplicável; se a ação foi apenas preview/read-only, rollback é manter sem execução e registrar o bloqueio.
- Qualquer rollback que toque sistema externo exige o mesmo escopo aprovado, readback e receipt.

### Verificação / readback
- Verificação obrigatória: receipt local, conferência de itens/SKUs/fornecedores pretendidos, confirmação de zero contato externo não aprovado e readback do artefato de decisão.
- Se houver divergência de identidade, fonte, escopo ou aprovação, bloquear execução e registrar causa sanitizada.

### Opções de aprovação
- Aprovar exatamente o escopo descrito neste packet.
- Aprovar apenas preview/dry-run/read-only.
- Ajustar alvo/limite antes de executar.
- Bloquear execução e manter como histórico/rascunho.

### Secret hygiene
- Usar credenciais somente via Doppler/wrapper seguro quando houver integração; não imprimir tokens, refresh tokens, passwords, service-account JSON, API keys ou connection strings.
- Relatórios e receipts devem manter `values_printed=false` e redigir qualquer valor sensível como `[REDACTED]`.
