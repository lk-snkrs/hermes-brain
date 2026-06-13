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
