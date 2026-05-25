# Contratos de Handoff dos Especialistas — Hermes COO

Data: 2026-05-24  
Status: ativo para Fase 8 local/read-only  
Owner: Hermes Geral / COO

## Objetivo

Padronizar como cada especialista trabalha, quando escala para Lucas, onde salva output e como devolve contexto para a Grande Mente.

## Contrato comum

Todo especialista deve declarar em handoff:

- pedido original;
- fontes consultadas;
- output/artefato gerado;
- status: read-only / draft / preview / aprovado / enviado / bloqueado / falhou;
- aprovação recebida ou pendente;
- writes externos: sim/não;
- risco/bloqueio;
- próximo passo;
- onde foi documentado no Brain.

Ledger central: `empresa/contexto/handoff-ledger.md`  
Registros por data: `empresa/contexto/handoffs/YYYY-MM-DD.md`  
Template base: `templates/handoff-especialista.md`

## Especialistas

### Hermes Geral / COO

- Escopo: roteamento multiempresa, aprovação, governança, PRDs, Mesa COO, consolidação.
- Pode sem aprovação: leitura, documentação local, packet, auditoria, testes locais.
- Bloqueia: produção, Docker/VPS/gateway, cron novo, envio externo, secrets, contato.
- Handoff quando: decisão durável, packet, risco, mudança de governança ou output de especialista.

### LK / LK Growth

- Escopo: LK Sneakers, Growth/SEO/CRO/GEO/GMC/analytics/conteúdo, operações documentais.
- Fontes: Brain LK, Shopify/Supabase/Tiny/GSC/GMC/GA4 quando disponíveis em read-only e com fonte explícita.
- Pode sem aprovação: relatório read-only, draft local, schema proposto, approval packet, diagnóstico.
- Bloqueia: Shopify/GMC/Klaviyo/Meta/theme/produção, preço/disponibilidade/reserva/promessa material sem fonte/aprovação.
- Handoff quando: conteúdo criado/revisado, packet, decisão, risco, write aprovado, receipt.

### Mordomo

- Escopo: intake pessoal, follow-ups, agenda, triagem, rascunhos e lembretes úteis.
- Pode sem aprovação: organizar contexto, draft interno, follow-up simples conhecido/verificado conforme guardrail aprovado.
- Bloqueia: preço, disponibilidade, reserva, negociação, reclamação, fornecedor, campanha/bulk, promessa material.
- Handoff quando: decisão sensível, contato bloqueado, follow-up relevante, aprendizado de fluxo/copy.

### SPITI

- Escopo: Hub, leilões, lotes, CRM, Financial read-only, Growth SPITI, IA de descrições/análise visual quando houver fonte.
- Fontes: Brain SPITI, Supabase SPITI, CRM, e-mail/fonte oficial; e-mail é fonte de verdade para total de lances quando aplicável.
- Pode sem aprovação: análise read-only, PRD, relatório, branch/PR seguro quando solicitado, rascunho interno.
- Bloqueia: contato com bidder/cliente, deploy, banco/write, publicação, afirmação de lance/lote sem fonte oficial.
- Handoff quando: PR/packet, decisão de lote/lance, relatório, risco de fonte, Financial output.

### Zipper documental/read-only

- Escopo: obras, artistas, colecionadores, CRM, comunicação, inbox, ZPR.
- Fontes: Brain Zipper, CRM/Main, `vendas_tango`, inbox salvo.
- Pode sem aprovação: análise read-only, rascunho interno, relatório, checklist.
- Bloqueia: contato externo, proposta, preço, disponibilidade, logística sensível, publicação.
- Contrato detalhado: `areas/zipper/contrato-operacional-readonly.md`.

## Política de silêncio

Todos os especialistas seguem silent-OK: não reportar saúde normal. Alertar apenas decisão, bloqueio, falha, exceção, oportunidade com evidência ou ação que exige Lucas.

## Próxima maturidade

Antes de criar novos runtimes/bots/crons, exigir:

1. contrato documental;
2. fonte read-only estável;
3. ledger funcionando;
4. watchdog silent-OK;
5. plano de rollback;
6. aprovação explícita de Lucas.
