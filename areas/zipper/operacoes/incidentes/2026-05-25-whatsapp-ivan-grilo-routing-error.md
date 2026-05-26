# Incidente — envio WhatsApp Ivan Grilo pelo canal errado

Data: 2026-05-25  
Contexto: Zipper / Ivan Grilo / colecionadoras  
Status: correção registrada  
Writes externos já ocorridos: sim, para uma destinatária; não repetir sem rota correta

## O que aconteceu

Lucas aprovou seguir com o fluxo de WhatsApp para contatos que demonstraram interesse em obras de Ivan Grilo e deveriam receber mensagem introdutória + PDF de obras disponíveis.

A execução técnica foi feita diretamente pelo Hermes Geral usando a conta WhatsApp `zipper` via `wacli`.

## Por que foi errado

Mesmo que o assunto fosse Zipper, Lucas corrigiu que todo contato com cliente/colecionador da Zipper deve sair pelo WhatsApp pessoal dele, via fluxo Mordomo/Lucas pessoal, não pelo WhatsApp `zipper`.

Hermes Geral deveria ter orquestrado e roteado para Mordomo/Zipper-client-contact em vez de executar diretamente pelo canal `zipper`.

## Correção operacional

Para próximos casos de Zipper/Ivan Grilo/colecionadores:

1. Classificar como Zipper OS, mas execução de contato externo deve usar o fluxo Mordomo/Lucas pessoal.
2. Usar `wacli --account pessoal` para contato com cliente/colecionador da Zipper, salvo autorização explícita de outro canal.
3. Hermes Geral fica como orquestrador/approval controller, não executor direto por conveniência.
4. Gerar receipt/handoff com destinatário sanitizado, mensagem, anexo/fonte e resultado.
5. Nunca usar `wacli --account zipper` para outreach de cliente/colecionador por padrão.

## Guardrail mantido

- Envio externo continua exigindo aprovação explícita de Lucas com escopo/conteúdo claros.
- Preço/disponibilidade não devem ser inventados fora do PDF/fonte aprovada.
- Erros de entrega devem ser reportados sem expor dados sensíveis desnecessários.

## Ação imediata

A correção foi registrada nas skills `multiempresa-routing-lucas` e `wacli-whatsapp-cli` para prevenir repetição do erro.
