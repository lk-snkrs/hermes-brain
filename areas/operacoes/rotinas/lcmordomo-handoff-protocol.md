# Rotina — LC Mordomo OS Handoff Protocol

**Data:** 2026-06-05
**Status:** v0.1
**Escopo:** handoff entre LC Mordomo Central e subagentes lógicos/operacionais.

## 1. Objetivo

Impedir que subagentes virem ilhas de contexto. Todo trabalho material feito por um subagente deve voltar para o LC Mordomo Central como receipt/handoff estruturado.

## 2. Quando handoff é obrigatório

Handoff obrigatório quando houver:

- decisão ou recomendação;
- contato/cliente/lead afetado;
- follow-up criado, executado, bloqueado ou adiado;
- CRM atualizado;
- e-mail/WhatsApp/draft/previews;
- falha de cron/script/API;
- mudança em Brain/skill/rotina;
- qualquer A2 executado;
- qualquer A3/A4 bloqueado;
- descoberta de fonte de verdade;
- correção aprendida com Lucas;
- risco de mistura multiempresa.

Handoff não é necessário para leituras triviais sem efeito ou checks silenciosos OK sem output material.

## 3. Formato mínimo

```markdown
## Handoff — [Subagente] — YYYY-MM-DD HH:MM

**Domínio:** pessoal | Zipper | SPITI | LK | Hermes/Infra | CRM | Governança
**Objetivo:**
**Fonte(s):**
**Risco:** A0 | A1 | A2 | A3 | A4
**Ação realizada:**
**Resultado:**
**Pendência:**
**Precisa Lucas?:** sim/não
**Por quê:**
**Registro durável:** caminho/CRM/state/skill
**Próxima ação recomendada:**
```

## 4. Handoff para Lucas

O handoff interno não deve ser enviado bruto para Lucas.

O LC Mordomo Central deve converter para um destes formatos:

- silencioso;
- recibo curto;
- digest;
- urgente;
- aprovação;
- erro.

## 5. Regras de qualidade

Um handoff bom responde:

1. O que aconteceu?
2. Por que importa?
3. Qual fonte sustenta?
4. O que foi feito?
5. O que falta?
6. Lucas precisa decidir algo?
7. Onde ficou registrado?

## 6. Anti-padrões

Não usar:

- logs crus;
- JSON sem síntese;
- “verificar depois” sem dono;
- “needs attention” sem ação;
- status técnico sem impacto;
- receipts de sucesso enviados ao Lucas sem necessidade;
- duplicação de mensagem externa já enviada.

## 7. Storage sugerido

- Handoffs materiais diários: `areas/operacoes/reports/handoffs/YYYY-MM-DD.md`
- Handoffs de empresa: área da empresa correspondente.
- Receipts operacionais novos: preferir `/opt/data/scripts/hermes_memory_os_receipt_writer.py` para salvar o receipt e chamar hook em uma única operação local.
- Handoff/approval packet criado manualmente: executar `/opt/data/scripts/hermes_memory_os_event_hook.py <caminho-do-artefato>` após salvar.
- Correções de procedimento: skill/reference.
- Decisões aprovadas: decision ledger/Brain da empresa.
- Follow-ups: CRM/follow-up queue.

## 8. LK/Evolution operational knowledge

Quando o assunto for LK Evolution API, confirmação de entrega WhatsApp, `lk-evolution-delivery-reconciliation`, `matched=0`, `updated=0`, `delivery_updates` ou POS thank-you ledger, carregar/consultar:

- `areas/operacoes/rotinas/lcmordomo-lk-evolution-delivery-reconciliation-runbook-2026-06-06.md`
- skill do perfil Mordomo: `lk-evolution-webhook-operations`

Regra: LC Mordomo entende e roteia o problema, mas não executa envio WhatsApp LK, alteração Evolution, deploy Vercel, restart gateway ou mutação de ledger sem aprovação explícita e escopo atual de Lucas. LK Ops é dono operacional; Tiny segue fonte de verdade de estoque/disponibilidade/preço.

## 9. Verificação

Antes de fechar uma tarefa com subagente:

- há handoff se houve output material?
- a fonte foi marcada?
- o risco A0-A4 foi marcado?
- o registro durável existe?
- Lucas só será interrompido se necessário?
- receipt/handoff material acionou wrapper/hook Memory OS e ficou silencioso quando verde?
