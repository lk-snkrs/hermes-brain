# Zipper Runtime — Gatilhos, Guardrails e Plano de Promoção

Data: 2026-05-26  
Status: planejamento documental; runtime/bot/profile ainda não criado  
Owner lógico: Zipper OS  
Supervisor: Hermes Geral / COO  
Runtimes atuais: Main Hermes e Mordomo conforme rotinas existentes  
Writes externos/runtime: não autorizados por este documento

## Decisão atual

Zipper permanece documental/read-only por padrão, mas já existe volume suficiente para tratar a criação de runtime próprio como possibilidade real, não apenas hipótese distante.

A decisão correta agora é preparar o critério e o pacote de promoção. Não criar bot/profile ainda sem aprovação específica.

## Sinais observados

Rotinas/fluxos Zipper já existentes:

- Gmail style learning refresh.
- Zipper OS vendas 09h WhatsApp/e-mail.
- Zipper Gmail draft engine safe draft-only.
- Zipper direct main e-mail monitor.
- Zipper artist PDFs local-only known-answer ingest.
- ZPR Enquiry Form watcher approval-gated.
- Inbox/documentos salvos em `areas/zipper/inbox/`.

Interpretação:

- O volume já justifica governança própria.
- Ainda não justifica automaticamente runtime próprio se os outputs continuarem baixos, read-only e bem handoffados.
- A promoção deve ser baseada em volume + risco + necessidade de canal, não em “organograma bonito”.

## Gatilho objetivo para criar runtime Zipper

Promover para profile/bot próprio se 2+ critérios abaixo forem verdadeiros por pelo menos 2 semanas:

### Volume

- Mais de 5 interações Zipper relevantes por semana exigindo contexto próprio.
- Mais de 3 outputs materiais por semana: rascunhos, follow-ups, relatórios, análises de venda, listas de obra ou enquiry handling.
- Inbox/e-mail/WhatsApp Zipper começa a competir com Lucas pessoal ou LK no Mordomo.

### Risco de contexto

- Confusão recorrente entre Zipper, SPITI e LK.
- Rascunhos de colecionador/artista/proposta ficam misturados com rotinas pessoais.
- Necessidade de tom cultural/galeria mais consistente do que o Mordomo consegue manter.

### Autonomia operacional

- Equipe Zipper precisa consultar um bot/canal dedicado.
- Rotinas Zipper precisam de cadência própria ou digest próprio.
- Handoffs recorrentes para Osmar, Helo, Biz, Mie, Cibele ou Panda.

### Fontes/integrações

- Uso recorrente de CRM/Main Zipper ou `vendas_tango` em read-only.
- Necessidade de ledger próprio de artistas, obras, colecionadores, feiras, propostas ou comunicação.
- Necessidade de separar logs e receipts por empresa.

### UX

- Lucas sinaliza que Zipper está gerando ruído no Mordomo.
- A equipe precisa de identidade explícita Zipper.
- Há demanda por canal diferente do Telegram principal/Mordomo.

## Guardrails permanentes

Mesmo com runtime próprio, continua bloqueado sem aprovação explícita:

- enviar WhatsApp/e-mail externo;
- contatar colecionador, artista, fornecedor ou parceiro;
- propor preço, desconto, reserva, disponibilidade ou negociação;
- prometer logística, prazo, entrega ou retirada;
- publicar texto/campanha;
- alterar CRM, banco, site, automação ou integração;
- criar cron novo, gateway, bot ou profile sem plano/rollback aprovado.

## O que o runtime Zipper poderia fazer

Permitido sem aprovação adicional, se o runtime for criado futuramente:

- análise read-only;
- rascunho interno;
- classificação de inbox;
- organização de obras/artistas/documentos;
- relatório interno;
- checklist de exposição/feira;
- packet para Lucas/Osmar/equipe aprovar;
- handoff para Hermes Central.

## Pacote mínimo antes de ativação

Antes de criar `/opt/data/profiles/zipper` ou bot dedicado:

1. Escopo do profile.
2. Humano aprovador.
3. Canais autorizados.
4. Fontes permitidas.
5. Lista de crons atuais a manter/migrar.
6. Backups dos registries Main/Mordomo.
7. Rollback de cron/profile/env.
8. `.env` sem herdar API/webhook indevidos.
9. Watchdog silent-OK.
10. Handoff ledger Zipper.
11. Teste read-only de boot.
12. Secret scan de docs/receipts.

## Candidatos a migração futura

Não migrar agora. Apenas candidatos:

- `Zipper Gmail style learning refresh` — Main.
- `Zipper OS vendas 09h WhatsApp/email` — Main.
- `Zipper Gmail draft engine — safe draft-only` — Mordomo.
- `Zipper direct main e-mail monitor — zipper@zippergaleria.com.br` — Mordomo.
- `Zipper artist PDFs local-only known-answer ingest` — Mordomo.
- `ZPR Enquiry Form watcher — approval-gated` — Mordomo.

## Próxima decisão

Antes de runtime, executar por 1 a 2 semanas um acompanhamento simples:

- quantos outputs Zipper relevantes por semana;
- quantos pedem aprovação humana;
- quantos geram handoff;
- quantos causam ruído no Mordomo;
- quantos precisariam de fonte viva/CRM.

Se o critério bater, preparar approval packet para criar runtime Zipper.

## Veredito atual

Vamos provavelmente precisar de runtime Zipper se o volume observado continuar. Mas a ação correta agora é medir, sanear owner dos crons e preparar promoção com rollback — não criar bot imediatamente.
