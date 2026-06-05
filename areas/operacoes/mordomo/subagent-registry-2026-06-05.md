# LC Mordomo OS — Subagent Registry

**Data:** 2026-06-05
**Status:** v0.1
**Fonte:** PRD `areas/operacoes/prds/lcmordomo-os-prd-2026-06-05.md`

## 1. Objetivo

Registrar os subagentes lógicos do LC Mordomo OS, seus escopos, fontes, memória, skills, crons, ferramentas, autonomia e regras de escalonamento.

Subagente lógico não significa necessariamente profile/runtime separado. Na fase inicial, um subagente pode ser:

- contexto + Brain + skill + rotina;
- executor chamado pelo Mordomo Central;
- profile separado apenas quando volume, risco ou isolamento justificarem.

## 2. Regra de promoção

### Nível 0 — Domínio documentado

Existe escopo e Brain, mas sem agente dedicado.

### Nível 1 — Subagente lógico

Existe contrato, skills, rotinas e memória operacional, mas roda via Mordomo Central.

### Nível 2 — Subagente operacional

Tem scripts/crons/rotinas próprias e handoff obrigatório.

### Nível 3 — Profile/runtime separado

Tem profile Hermes próprio, canal/toolsets próprios e isolamento real.

Critério para subir de nível:

- volume recorrente;
- risco operacional;
- necessidade de isolamento de fonte/credenciais;
- necessidade de crons próprios;
- necessidade de handoff/receipts formais.

## 3. Registro inicial

### 3.1 LC Mordomo Central

- **Tipo:** agente principal/orquestrador.
- **Nível:** 2 hoje; candidato a 3 conforme runtime dedicado amadurecer.
- **Interface Lucas:** sim, principal.
- **Escopo:** LC inteira: pessoal, LK, Zipper, SPITI, Hermes/infra, CRM, calendário, inbox, follow-ups.
- **Brain:** `areas/operacoes/`, `areas/operacoes/mordomo/`, PRDs e rotinas globais.
- **Memória:** preferências de Lucas, regras globais, política de autonomia, routing.
- **Skills:** `lucas-chief-of-staff`, `multiempresa-routing-lucas`, `hermes-agent`, skills por domínio.
- **Entrega:** decisão, preview, resumo executivo, blocker, approval packet.
- **Pode:** rotear, documentar, executar A0/A1, acionar A2 aprovado, preparar A3/A4.
- **Não pode:** enviar externo amplo, mexer em produção/infra/secrets/dinheiro sem aprovação.

### 3.2 Pessoal/Calendário

- **Tipo:** subagente lógico.
- **Nível:** 1.
- **Interface Lucas:** via Mordomo Central.
- **Escopo:** agenda, compromissos, lembretes, logística pessoal, tom por contato.
- **Brain:** `areas/operacoes/mordomo/` e futuras notas pessoais seguras.
- **Fontes:** WhatsApp pessoal, calendário, e-mail, screenshots/pastes de Lucas, quando autorizados.
- **Pode:** criar evento claro; registrar lembrete; preparar confirmação; executar follow-up logístico estreito se safe.
- **Escala:** data/hora ambígua, assunto sensível, negociação, dinheiro, conflito de agenda material.

### 3.3 Zipper

- **Tipo:** subagente operacional prioritário.
- **Nível:** 2.
- **Interface Lucas:** via Mordomo Central.
- **Escopo:** leads, PDFs, artistas, colecionadores, CRM de interesse, follow-ups pós-PDF, feiras, propostas.
- **Brain:** `areas/zipper/` + `areas/operacoes/mordomo/` para camada global.
- **Fontes:** Zipper Supabase, `vendas_tango`, CRM/Main, Gmail Zipper, WhatsApp `pessoal`/Zipper conforme fluxo, PDF manifest.
- **Skills:** ZPR PDF send, post-PDF follow-up, artist-interest CRM, negative-fit suppression.
- **Pode:** CRM local, follow-up seguro pós-PDF, ack seguro, supressão budget, drafts.
- **Escala:** preço, disponibilidade, reserva, pagamento, negociação, reclamação, campanha, artista/coletor sensível.

### 3.4 SPITI

- **Tipo:** subagente lógico/operacional planejado.
- **Nível:** 1 → 2.
- **Interface Lucas:** via Mordomo Central.
- **Escopo:** leilões, lotes, lances, Spiti Hub, relatórios, divergências.
- **Brain:** `areas/spiti/`.
- **Fontes:** e-mail/fonte primária de lances, sistema interno validado, site como secundário.
- **Pode:** revisão read-only, relatório, divergência, draft de decisão.
- **Escala:** qualquer afirmação de lance sem fonte primária, contato bidder/cliente, site/deploy/banco.
- **Princípio:** silêncio é melhor que dado errado.

### 3.5 LK

- **Tipo:** subagente lógico planejado.
- **Nível:** 1.
- **Interface Lucas:** via Mordomo Central.
- **Escopo:** Shopify, Tiny, CRM, recompra, estoque, campanhas, SEO, analytics, influenciadores.
- **Brain:** `areas/lk/`.
- **Fontes:** Shopify, Tiny `LK | CONTROLE ESTOQUE`, GA4, Meta/Google como sinais, Brain LK.
- **Pode:** análises read-only, relatórios, drafts, reconciliação local.
- **Escala:** preço, estoque, Shopify/Tiny writes, Klaviyo/WhatsApp/e-mail, campanhas, orçamento, fornecedor/cliente.

### 3.6 Hermes/Infra

- **Tipo:** subagente operacional/governança técnica.
- **Nível:** 2.
- **Interface Lucas:** via Mordomo Central.
- **Escopo:** Hermes Agent, crons, gateway, skills, scripts, Brain health, logs, runtime.
- **Brain:** `areas/operacoes/`, `areas/hermes/`.
- **Fontes:** config/logs/cron list/scripts, sem imprimir secrets.
- **Pode:** read-only observability, docs, skill patch, self-heal local de automação segura.
- **Escala:** restart, Docker, VPS, Traefik, deploy, secrets, banco, produção.

### 3.7 CRM/Relacionamentos

- **Tipo:** subagente lógico transversal.
- **Nível:** 1.
- **Interface Lucas:** via Mordomo Central.
- **Escopo:** visão global de pessoas, contexto, tom, pendências e relacionamento.
- **Brain:** `areas/operacoes/mordomo/` + áreas empresariais corretas.
- **Fonte:** CRM local, WhatsApp/e-mail/calendário autorizados, Supabase por empresa.
- **Pode:** dedupe, profile, tom, pendência, routing.
- **Escala:** dado sensível, mistura multiempresa, export PII, contato externo.

### 3.8 Governança/Qualidade

- **Tipo:** subagente auditor.
- **Nível:** 1 → 2.
- **Interface Lucas:** só por exceção/resumo.
- **Escopo:** auditar crons, skills, ruído, handoffs, memória, fontes, separação multiempresa.
- **Brain:** `areas/operacoes/rotinas/`, reports de governança.
- **Pode:** auditoria local/read-only, relatórios, abrir melhoria documental, sugerir skill.
- **Escala:** falha crítica, risco de envio externo indevido, dados misturados, produção/infra.

## 4. Regras universais de subagente

1. Subagente não fala com Lucas sem passar pelo Mordomo Central, salvo configuração explícita futura.
2. Subagente não guarda decisão só em chat.
3. Subagente deve devolver handoff quando houver output material.
4. Subagente deve usar fonte de verdade do próprio domínio.
5. Subagente não pode ampliar autonomia por inferência.
6. Subagente não pode imprimir secrets.
7. Subagente deve classificar risco A0-A4.
8. Subagente deve ser silencioso quando não há decisão.
9. Subagente não carrega “tudo” por padrão: usa contexto mínimo, índice/MAPA, busca sob demanda, skills e fonte viva apenas quando a tarefa exigir.
10. Subagente deve manter handoff compacto: decisão, fonte, status, próximos passos e blockers, nunca histórico bruto inteiro.

### 4.1 Context Budget obrigatório

Antes de promover um subagente para rotina recorrente, cron ou runtime/profile separado, registrar:

- **Boot mínimo:** identidade, escopo, permissões, bloqueios e skill principal.
- **Índices:** `MAPA.md`, registry, rotina e PRD que localizam o contexto rico.
- **Fontes sob demanda:** Brain, session_search, SQLite/API/fonte viva e skills que podem ser consultados quando necessário.
- **Critério de leitura:** quais sinais justificam carregar arquivos grandes, histórico de sessão ou dados vivos.
- **Handoff/compactação:** formato mínimo para devolver resultado ao Mordomo Central e ao Brain sem despejar histórico inteiro.

## 5. Próxima revisão

Revisar depois de:

- SOUL aprovado;
- primeiro MVP Zipper formalizado;
- auditoria dos crons atuais;
- definição se algum subagente vira profile/runtime separado.
