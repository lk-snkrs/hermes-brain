# Audit — Registro de Aprovações, Copy e Memória Operacional

Data: 2026-05-20  
Escopo: Hermes Brain / LK CRM / rotinas de registro de decisões aprovadas  
Base conceitual: Bruno/OpenClaw — agente não é o cérebro; agente lê e escreve no cérebro. Decisão aprovada deve virar memória operacional navegável, não ficar só no chat.

## Veredito

Parcialmente bom, mas ainda não estava 100% limpo.

A estrutura certa já existia: decisão viva, protocolo anti-perda pós-compactação, skill atualizada e regra global no learning loop. O problema era de navegação e consistência: a decisão canônica de copy existia, mas o playbook antigo ainda carregava uma copy diferente como “aprovada”, e o novo protocolo não estava indexado no índice de rotinas.

## O que estava certo

- A decisão canônica de checkout abandonado foi salva em `areas/lk/sub-areas/crm/decisions/2026-05-20-checkout-abandonado-copy-canonica.md`.
- O Brain já tinha a rotina geral `areas/operacoes/rotinas/company-decision-memory.md` dizendo que decisão de empresa precisa ir para memória viva da empresa/área.
- O arquivo `empresa/gestao/memory-system.md` já separa corretamente memory tool, session_search, Hermes Brain, `memories/`, `empresa/areas` e dados vivos.
- O protocolo anti-perda pós-compactação existe em `areas/operacoes/rotinas/protocolo-registro-decisoes-aprovadas-contexto-compactado.md`.

## Gaps encontrados

1. `protocolo-registro-decisoes-aprovadas-contexto-compactado.md` não estava no índice `empresa/rotinas/_index.md`.
2. O `MAPA.md` de LK CRM não apontava para a pasta `decisions/`, então o próximo agente poderia ler só o playbook e não a decisão viva.
3. O playbook de WhatsApp checkout abandonado tinha uma seção chamada “Copy aprovada” com texto anterior/diferente da decisão canônica.
4. A regra Bruno/OpenClaw correta ainda precisa ficar cada vez mais operacional: decisão → artefato vivo → índice/MAPA → skill/rotina → verificação. Só criar arquivo não basta.

## Melhorias aplicadas neste audit

- Indexei o protocolo anti-perda no índice global de rotinas.
- Adicionei seção “Decisões vivas” no `areas/lk/sub-areas/crm/MAPA.md` apontando para a decisão canônica.
- Atualizei o playbook de WhatsApp checkout abandonado para dizer que a decisão viva prevalece em caso de conflito.
- Alinhei T1/30min e T2/24h do playbook com a copy canônica aprovada por Lucas.

## Recomendação Bruno-native

O padrão daqui para frente deve ser:

```text
aprovação/correção do Lucas
→ registrar decisão viva na área certa
→ atualizar playbook/skill que pode contradizer a decisão
→ atualizar MAPA/índice para navegabilidade
→ rodar health check/secret scan
→ deixar versionável pelo Brain Sync seguro
```

Isso é mais importante do que “lembrar” no chat. O agente é transitório; o Brain é a fonte operacional.

## Próximas melhorias recomendadas

- Criar um template padrão de decisão customer-facing em `areas/operacoes/templates/` para copy/tom/fluxo aprovado.
- Adicionar um check leve no health check para alertar quando existir `decisions/` sem link no `MAPA.md` da área.
- Criar uma fila/ledger específico para aprovações de CRM customer-facing, separando `approved_copy`, `approved_flow`, `needs_current_send_approval` e `executed_verified`.

## Não alterado

- Nenhum envio externo.
- Nenhum template Meta/Crisp/n8n alterado em produção.
- Nenhum Docker/VPS/cron/runtime alterado.
- Nenhum secret lido ou exposto.
