# Receipt — PRD lk-stock: plano de implementação Gate B

Data UTC: 2026-06-08T17:20:27Z

## Continuação

Lucas mandou seguir após a arquitetura mínima da base local Gate B.

## Alterações feitas

Plano criado:

- `areas/lk/sub-areas/stock/plans/gate-b-base-local-implementation-plan.md`

PRD atualizado para apontar para o plano:

- `areas/lk/sub-areas/stock/PRD.md`

## Conteúdo do plano

O plano detalha a implementação local/offline/dry-run do Gate B em 10 tarefas:

1. criar diretórios operacionais;
2. criar schema SQL versionado;
3. criar módulo de banco local;
4. criar normalizador de eventos;
5. criar ingestão webhook local/dry-run;
6. criar cron diário local/dry-run;
7. implementar cálculo de score;
8. criar comando de consulta A1 sobre base local;
9. criar approval packet para runtime real;
10. rodar verificação final local.

## Guardrail registrado

O plano deixa explícito que implementação local/offline/dry-run não ativa:

- webhook público;
- cron real;
- gateway;
- bot;
- Tiny/Shopify write;
- compra/fornecedor/cliente/campanha.

## Frase de aprovação futura registrada

O plano inclui frase de aprovação para a implementação local:

> Aprovo implementar localmente o Gate B do `lk-stock` em modo offline/dry-run, criando scripts, schema SQLite, fixtures e testes locais, sem ativar webhook público, cron real, gateway, bot ou write externo.

## Writes externos

0.

## Runtime ativado

Nenhum.
