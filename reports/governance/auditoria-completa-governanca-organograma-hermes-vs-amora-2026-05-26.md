# Auditoria completa — Governança e organograma de agentes Hermes/Cimino vs Amora/OpenClaw

Data: 2026-05-26  
Escopo: auditoria local/read-only da estrutura de agentes, Brain, profiles, crons, bots, documentação, segurança e performance.  
Produção/runtime: **nenhuma alteração feita**. Sem restart, sem migração de cron, sem Docker/VPS/Traefik, sem writes externos.

## 1. Resumo executivo

**Nota geral de maturidade: 7,9/10.**

O organograma atual está **conceitualmente correto** para Lucas/Cimino: Hermes Geral atua como COO/orquestrador; especialistas existem por domínio; Brain é fonte de verdade; writes externos e produção exigem aprovação; e há separação crescente entre resposta rápida, trabalho pesado, preview, receipt e handoff.

Comparação franca:

- **Hermes/Cimino é mais seguro e mais adequado para multiempresa** do que copiar a Amora literalmente, porque tem Task Router, approval gates, perfis isolados, bots especializados e fronteiras por empresa.
- **Amora ainda é mais madura como ritual diário vivo**, porque seus arquivos raiz (`SOUL`, `IDENTITY`, `USER`, `AGENTS`, `MAPA`, `HEARTBEAT`) são mais coesos, sua proatividade é mais treinada e o ciclo “ação → registro → memória → skill” é mais orgânico.

Tese central: **não adicionar mais agentes ou prompts por padrão; primeiro fechar o ciclo pedido → router → executor certo → preview/ação segura → receipt → handoff → Brain → skill/rotina.**

## 2. Respostas objetivas

1. **O organograma atual está correto?** Sim, com ajustes: LK Ops, LK Shopify, LK Trends e Zipper precisam aparecer melhor na documentação canônica e no mapa de donos de rotinas.
2. **Está no nível da Amora?** Não totalmente. Está mais forte em segurança multiempresa, mas menos maduro em identidade, heartbeat, continuidade e ritual vivo.
3. **Hermes Geral já é COO?** Parcialmente sim. Ainda executa coisas demais porque rotinas antigas e crons seguem no Main ou Mordomo por conveniência/histórico.
4. **Especialistas têm dono claro?** Growth, Mordomo, SPITI e LK Ops estão claros. LK Shopify/LK Trends existem em runtime, mas precisam de contrato/MAPA canônico mais forte. Zipper ainda é documental/read-only.
5. **Bots/profiles fazem sentido?** Sim para os ativos principais, mas há perfis read-only antigos/auxiliares com função pouco clara que devem ser marcados como arquivo/experimento ou aposentados.
6. **Brain está bem documentado?** Bem melhor que antes, mas com buracos: docs canônicos do organograma ainda não refletem todos os profiles ativos; handoffs/receipts existem mas ainda não são uniformes; há drift entre “documental” e “runtime real”.
7. **Duplicidade/conflito?** Sim: LK Ops em Main/Mordomo, Zipper em Main/Mordomo, Growth com risco de absorver coisas operacionais, Main com watchdogs e rotinas de negócio misturadas.
8. **Rotinas que deveriam mudar de dono?** LK vendas/loja/WhatsApp para LK Ops lógico; Zipper Gmail/vendas/enquiry para Zipper lógico; D+7 Growth devem ser classificados entre decisão Telegram vs relatório local.
9. **Melhorias agora?** Documentar donos, contratos, mapas e receipts; sanear matriz; classificar crons; reduzir ruído; reforçar handoff ledger.
10. **Melhorias com aprovação?** Migrar crons, pausar/remover jobs, criar bot/profile Zipper, reiniciar gateways, alterar env/launchers, expor webhooks/API, writes Tiny/Shopify/Klaviyo/CRM/WhatsApp.

## 3. Principais acertos

- Task Router e approval gates são mais adequados ao risco de Lucas do que o modelo “super-agente faz tudo”.
- Especialistas ativos existem e foram isolados: Main, Mordomo, LK Growth, LK Ops, LK Trends, LK Shopify, SPITI.
- Toolsets de Telegram foram reduzidos em especialistas, melhorando governança e performance.
- Brain tem volume e estrutura: organograma, matriz, dashboards, contratos LK Ops, gatilhos Zipper, relatórios de governança, receipts e FTS local.
- Zipper não virou runtime por impulso; isso está correto.

## 4. Principais riscos

- **Drift entre runtime e Brain:** organograma canônico antigo ainda menciona só parte dos runtimes ativos.
- **Hermes Geral acumulando execução:** Main ainda abriga crons LK Ops e Zipper documental por histórico.
- **Mordomo amplo demais sem rótulo:** amplo é correto, mas rotinas de negócio dentro dele precisam owner/handoff claro.
- **Profiles especialistas com docs mínimos:** muitos `HERMES_HOME` têm só `SOUL.md`; Amora usa pacote raiz completo.
- **Crons e delivery:** alguns jobs estão no perfil errado ou com ruído potencial; registry Mordomo tem trailing/extra data e precisa saneamento com backup antes de editar.
- **Segurança operacional:** profile secundário deve manter API/webhook desativado; qualquer launcher/env herdado precisa verificação antes de declarar seguro.

## 5. Scorecard por área

### Hermes Geral / COO
- Organograma: 8,5/10
- Documentação: 8,5/10
- Handoffs: 7,5/10
- Crons/rotinas: 7,0/10
- Segurança: 8,8/10
- Performance: 7,0/10
- Clareza de dono: 8,0/10
- Comparação com Amora: 8,0/10
- Status: **correto, mas ainda executa demais**.

### Mordomo
- Organograma: 8,0/10
- Documentação: 7,0/10
- Handoffs: 7,0/10
- Crons/rotinas: 6,5/10
- Segurança: 8,0/10
- Performance: 8,0/10
- Clareza de dono: 7,5/10
- Comparação com Amora: 7,5/10
- Status: **correto como intake amplo; ajustar owner labels e rotinas Zipper/LK**.

### LK Ops / Atendimento
- Organograma: 7,5/10
- Documentação: 8,0/10
- Handoffs: 7,0/10
- Crons/rotinas: 6,5/10
- Segurança: 8,5/10
- Performance: 8,0/10
- Clareza de dono: 7,5/10
- Comparação com Amora: 7,0/10
- Status: **categoria correta; reconciliar crons e docs canônicos**.

### LK Growth
- Organograma: 8,5/10
- Documentação: 8,0/10
- Handoffs: 7,5/10
- Crons/rotinas: 8,0/10
- Segurança: 8,0/10
- Performance: 7,5/10
- Clareza de dono: 8,5/10
- Comparação com Amora: 7,8/10
- Status: **correto; proteger contra virar Ops por conveniência e reduzir ruído D+7**.

### LK Shopify
- Organograma: 7,0/10
- Documentação: 6,5/10
- Handoffs: 6,5/10
- Crons/rotinas: 6,0/10
- Segurança: 8,0/10
- Performance: 7,5/10
- Clareza de dono: 7,0/10
- Comparação com Amora: 6,8/10
- Status: **ajustar documentação; manter writes bloqueados por aprovação, snapshot/readback/rollback**.

### LK Trends
- Organograma: 7,0/10
- Documentação: 6,5/10
- Handoffs: 6,5/10
- Crons/rotinas: 6,0/10
- Segurança: 7,8/10
- Performance: 7,5/10
- Clareza de dono: 6,8/10
- Comparação com Amora: 6,8/10
- Status: **útil, mas precisa contrato claro: pesquisa/tendência/sourcing não pode conflitar com Growth ou Ops**.

### SPITI
- Organograma: 8,0/10
- Documentação: 7,0/10
- Handoffs: 7,0/10
- Crons/rotinas: 5,5/10, por não haver registry local encontrado
- Segurança: 8,8/10
- Performance: 7,5/10
- Clareza de dono: 8,0/10
- Comparação com Amora: 7,0/10
- Status: **correto; faltam crons/rituais próprios ou declaração explícita de que não deve ter**.

### Zipper
- Organograma: 6,8/10
- Documentação: 7,5/10
- Handoffs: 6,5/10
- Crons/rotinas: 6,0/10
- Segurança: 8,0/10
- Performance: 7,0/10
- Clareza de dono: 6,5/10
- Comparação com Amora: 6,8/10
- Status: **documental/read-only correto por enquanto; criar runtime só se volume/risco/canal justificar**.

### Brain Process / Brain
- Organograma: 8,0/10
- Documentação: 8,5/10
- Handoffs: 7,5/10
- Crons/rotinas: 8,0/10
- Segurança: 8,0/10
- Performance: 8,0/10 com FTS local
- Clareza de dono: 7,5/10
- Comparação com Amora: 8,0/10
- Status: **bem estruturado, mas precisa menos drift e mais ledger sistemático**.

## 6. Matriz de agentes

### Hermes Geral / Main
- Função: COO/orquestrador, Brain, governança, approval gates, Mesa COO, watchdogs centrais.
- Dono lógico: Lucas / Hermes COO.
- Escopo permitido: análise, documentação, roteamento, approval packets, coordenação, governança, local/read-only.
- Ferramentas necessárias: file, terminal, cronjob, session_search, memory, skills, web/browser quando pesquisa/QA, messaging com cuidado.
- Ferramentas excessivas: nenhuma por padrão no Main, mas deve evitar usar poder amplo para executar tarefa de especialista.
- Rotinas/crons: 20 jobs no Main; misto de governança, LK Ops e Zipper documental.
- Status: **correto; ajustar distribuição lógica e handoff**.

### Mordomo
- Função: intake pessoal, follow-ups, agenda, decisão pessoal, triagem WhatsApp/multiempresa.
- Dono lógico: Lucas pessoal.
- Escopo permitido: rascunhos, organização, follow-ups simples conhecidos/verificados, alerta de pendência.
- Ferramentas necessárias: clarify, file, memory, messaging, session_search, skills, todo.
- Ferramentas excessivas: evitar terminal/web pesados no Telegram se não necessários.
- Rotinas/crons: 13 parseáveis; registry com extra data; contém Zipper e LK WhatsApp que precisam classificação.
- Status: **ajustar, não encolher artificialmente**.

### LK Ops / Atendimento
- Função: atendimento, loja, vendas operacionais, estoque, preço, disponibilidade, Tiny/Shopify operacional.
- Dono lógico: LK Ops/Comercial.
- Escopo permitido: read-only, diagnóstico, rascunho interno, resolução SKU/tamanho, relatórios comerciais.
- Ferramentas necessárias: file, session_search, memory, skills, terminal limitado, clarify.
- Ferramentas excessivas: browser/cron/delegation/messaging externo por padrão.
- Rotinas/crons: LK sales brief, weekly CEO review, pulso comercial, store close, WhatsApp reply flows.
- Status: **correto como categoria/runtime; reconciliar crons e docs canônicos**.

### LK Growth
- Função: SEO, GEO, CRO, GMC, analytics, conteúdo, source pages, impacto D+7.
- Dono lógico: LK Growth.
- Escopo permitido: leitura, relatórios, drafts, schema/brief/preview, approval packets.
- Ferramentas necessárias: web/browser/vision, file, terminal, skills, session_search, memory, todo.
- Ferramentas excessivas: messaging externo, cronjob/delegation no Telegram se não necessário.
- Rotinas/crons: 19-21 jobs conforme registry/auditoria; maioria coerente.
- Status: **correto; reduzir ruído e impedir mistura com Ops**.

### LK Shopify
- Função: Shopify operacional/preview, produto/upload, integração e superfície de publicação.
- Dono lógico: LK Shopify, supervisionado por Hermes Geral/LK Ops conforme risco.
- Escopo permitido: diagnóstico, preview, read-only, approval packet.
- Ferramentas necessárias: file, terminal limitado, web, skills, session_search, memory, clarify.
- Ferramentas excessivas: writes diretos, API/webhook sem aprovação, messaging externo.
- Rotinas/crons: não consolidado como registry próprio claro nesta auditoria.
- Status: **ajustar documentação e boundaries**.

### LK Trends
- Função: tendências, pesquisa, sourcing intelligence, sinais de mercado.
- Dono lógico: LK Trends/Sourcing/Growth-adjacent.
- Escopo permitido: pesquisa, análise, rascunhos, relatórios, comparação read-only.
- Ferramentas necessárias: web/browser, file, terminal limitado, skills, memory, session_search.
- Ferramentas excessivas: produção, Shopify/Tiny writes, cron/messaging externo.
- Rotinas/crons: não consolidado como registry próprio claro nesta auditoria.
- Status: **ajustar escopo para não conflitar com Growth/Ops**.

### SPITI
- Função: Hub SPITI, obras, leilões, clientes, CRM/admin, descrição e análise com fonte verificável.
- Dono lógico: SPITI OS.
- Escopo permitido: read-only, drafts, análise, fonte verificada, tagging/embedding/matching interno sem contato externo.
- Ferramentas necessárias: web/browser/vision, file, terminal limitado, memory, session_search, skills.
- Ferramentas excessivas: writes, contatos externos, financeiro/sync sem aprovação.
- Rotinas/crons: registry local não encontrado.
- Status: **correto; documentar ausência/intenção de crons próprios**.

### Zipper
- Função: galeria, CRM/Main, vendas, artistas, colecionadores, enquiries e textos institucionais.
- Dono lógico: Zipper OS.
- Escopo permitido: documental/read-only, rascunhos internos, análises, ingest local de PDFs/known answers.
- Ferramentas necessárias: file, session_search, web quando pesquisa pública, memory/skills.
- Ferramentas excessivas: bot/runtime próprio sem gatilho, WhatsApp/e-mail externo, CRM writes.
- Rotinas/crons: Gmail style learning, vendas 09h, e-mail monitor, enquiry watcher espalhados entre Main/Mordomo.
- Status: **ajustar; não criar runtime ainda sem gatilhos comprovados**.

### Brain Process e profiles read-only auxiliares
- Função: suporte documental, leitura, análise, experimentos ou manutenção.
- Dono lógico: Hermes Geral / Governança.
- Escopo permitido: local/read-only.
- Ferramentas necessárias: skills/file/search conforme caso.
- Ferramentas excessivas: qualquer produção/runtime público se não houver função clara.
- Status: **marcar como ativo, arquivo ou aposentar; hoje há ambiguidade**.

## 7. Matriz de problemas

### 1 — Organograma canônico desatualizado frente ao runtime real
- Evidência: organograma ainda descreve parte dos especialistas como documentais enquanto runtime atual inclui LK Ops, LK Shopify e LK Trends.
- Impacto: futuros agentes podem rotear para o lugar errado.
- Risco: médio.
- Correção: atualizar organograma com “documental vs runtime real vs dono lógico”.
- Aprovação: pode ser feito local/read-only.

### 2 — Main Hermes ainda abriga rotinas de negócio
- Evidência: Main contém rotinas LK Daily Sales, Weekly CEO Review, Pulso Comercial, loja física e Zipper vendas.
- Impacto: Hermes Geral vira executor por conveniência.
- Risco: médio.
- Correção: manter temporariamente, mas rotular dono lógico e preparar migração futura.
- Aprovação: documentação agora; migração de cron exige aprovação.

### 3 — Mordomo mistura rotinas pessoais com Zipper/LK WhatsApp
- Evidência: auditoria de cron owner registrou rotinas Zipper/LK WhatsApp no Mordomo e extra data no registry.
- Impacto: risco de contexto cruzado e ruído.
- Risco: médio/alto se houver contato externo.
- Correção: classificar job a job, registrar handoff e só depois migrar/pausar.
- Aprovação: classificação local ok; editar registry/migrar exige aprovação.

### 4 — LK Ops/Atendimento ainda parcialmente implícito
- Evidência: contrato/MAPA existem, mas organograma/matriz principal ainda precisam refletir runtime/bot ativo e crons relacionados.
- Impacto: Growth ou Main podem absorver atendimento/estoque por conveniência.
- Risco: alto em preço/disponibilidade/reserva.
- Correção: promover LK Ops no organograma como dono lógico formal.
- Aprovação: doc local ok; writes/cron/runtime não.

### 5 — LK Shopify/LK Trends têm runtime, mas documentação raiz fraca
- Evidência: profiles existem com `SOUL.md` e config, mas sem pacote Amora-style completo observado no `HERMES_HOME`.
- Impacto: especialistas dependem de histórico/chat/memória.
- Risco: médio.
- Correção: criar/atualizar `IDENTITY`, `AGENTS`, `MAPA`, `TOOLS`, `HEARTBEAT` ou equivalentes Brain.
- Aprovação: doc local ok.

### 6 — SPITI sem registry de cron local
- Evidência: `/opt/data/profiles/spiti/cron/jobs.json` não encontrado.
- Impacto: pode ser escolha correta, mas hoje não está explicitamente declarado.
- Risco: baixo/médio.
- Correção: documentar “sem crons próprios por decisão” ou criar plano de rituais futuros.
- Aprovação: doc local ok; criar cron exige aprovação.

### 7 — Handoffs/receipts não uniformes
- Evidência: existem reports e receipts, mas auditorias anteriores repetem gap de consistência.
- Impacto: perda de continuidade pós-compactação.
- Risco: médio.
- Correção: ledger único de handoffs por materialidade.
- Aprovação: local/read-only.

### 8 — Guardrail read-only às vezes fica grosseiro demais
- Evidência: referências indicam que cron list pode ser bloqueado por preflight e exigir terminal read-only como alternativa.
- Impacto: auditoria operacional fica mais difícil.
- Risco: médio.
- Correção: distinguir hard-block de writes vs allowlist de inspeção read-only.
- Aprovação: patch runtime/gateway exige aprovação; documentação/test spec pode ser local.

### 9 — Performance parcialmente ativada, mas launcher/env pode sobrescrever
- Evidência: relatório de performance registrou risco de `HERMES_MAX_ITERATIONS=90` herdado.
- Impacto: especialistas podem continuar pesados apesar do config.
- Risco: médio.
- Correção: verificar live logs/env e ajustar launcher com override explícito.
- Aprovação: verificação read-only ok; restart/launcher change exige aprovação.

### 10 — Risco de vazamento de metadado técnico no Telegram
- Evidência: histórico de wrappers/preflight/job IDs exigiu skills específicas de clean UX.
- Impacto: experiência ruim e confusão decisória.
- Risco: alto para confiança.
- Correção: manter regra de Telegram limpo e testar entregas reais com botões nativos.
- Aprovação: testes/docs ok; patch gateway/restart exige aprovação.

## 8. Plano de melhoria

### Fazer agora — local/read-only

1. Atualizar organograma canônico com profiles ativos e status documental/runtime.
2. Criar matriz única `agente → dono → profile → bot → área Brain → cron registry → status`.
3. Completar docs de LK Shopify e LK Trends.
4. Registrar SPITI: “sem crons próprios por escolha” ou “crons pendentes”.
5. Classificar jobs D+7 Growth entre decisão Telegram, relatório local e receipt silencioso.
6. Criar checklist simples de handoff/receipt obrigatório.
7. Rodar auditoria read-only recorrente: profiles vivos, cron registry, docs canônicos, secret scan.
8. Marcar profiles auxiliares read-only como: ativo, experimento, arquivo ou candidato a pausa.

### Fazer com aprovação explícita

1. Migrar crons entre Main, Mordomo, LK Ops, LK Growth ou futuro Zipper.
2. Corrigir/sanear registry Mordomo com backup, se for necessário editar.
3. Reiniciar gateways para ativar ajustes de launcher/env/max iterations.
4. Criar bot/profile/runtime Zipper.
5. Alterar delivery de jobs Telegram/origin/local.
6. Alterar API/webhook em qualquer profile secundário.
7. Qualquer write em Tiny, Shopify, CRM, Klaviyo, WhatsApp, SPITI Hub, Zipper CRM/Main ou infra.

### Fazer depois

1. Dashboard executivo de coerência operacional com tendência semanal.
2. Métrica de false positive/false negative do Task Router.
3. Meta-auditoria mensal estilo Amora: “o que virou rotina, o que virou skill, o que ainda está no chat”.
4. Score de maturidade por especialista com bloqueios abertos.
5. Zipper runtime só se gatilhos de volume/risco/canal forem atingidos por 2 semanas.

### Não fazer

1. Não criar agente novo só para deixar organograma bonito.
2. Não copiar os 60+ crons da Amora.
3. Não transformar Growth em Ops.
4. Não transformar Mordomo em executor de negócio sensível.
5. Não permitir writes externos sem snapshot, preview, aprovação, readback, receipt e rollback.
6. Não expor wrappers, job IDs, JSON de roteamento ou detalhes técnicos no Telegram.

## 9. Checklist final

### Certo
- Modelo COO/orquestrador central.
- Separação entre Main e especialistas.
- Brain como fonte de verdade.
- Approval boundaries para produção/externo.
- Tiny como verdade de estoque e Shopify como superfície/gatilho.
- Silent-OK como padrão para rotinas saudáveis.
- Toolsets especialistas reduzidos para performance.
- Zipper não virou runtime por impulso.

### Parcialmente certo
- Handoff/receipt: existe, mas precisa consistência obrigatória.
- Crons: rodam, mas donos lógicos ainda misturados.
- Profiles: existem, mas alguns têm pacote documental incompleto.
- Telegram UX: regra está clara, mas precisa validação real contínua.
- Performance: config melhorou, mas ativação depende de env/launcher/logs.

### Errado/frágil
- Docs canônicos não refletem todos os profiles ativos.
- Main/Mordomo ainda carregam rotinas de negócio sem owner suficientemente explícito.
- Mordomo registry com extra data/trailing issue é risco de manutenção.
- LK Shopify e LK Trends têm escopo menos maduro do que Growth/Ops.
- Perfis auxiliares read-only sem função clara geram dívida cognitiva.

### Falta para nível Amora/Bruno
1. Pacote de identidade completo por agente.
2. Heartbeats menos teóricos e mais treinados: poucos checks, silent-OK, critérios objetivos de interrupção.
3. Handoff ledger consistente.
4. Rotinas com dono lógico e runtime coerente.
5. Skills criadas/consolidadas a partir de repetição real, não prompt gigante.
6. Auditoria periódica de drift entre docs, runtime, crons e Telegram UX.

## 10. Evidências read-only usadas

- Amora/OpenClaw: `LEIA-PRIMEIRO`, `SOUL`, `IDENTITY`, `USER`, `AGENTS`, `MAPA`, `HEARTBEAT` sanitizados.
- Hermes Brain: organograma, matriz de roteamento, Task Router, relatórios de auditoria vs Amora, dashboard de coerência, contratos LK Ops e gatilhos Zipper.
- Runtime local: profiles em `/opt/data` e `/opt/data/profiles/*`; configs parseados; registries de cron locais; processos gateway por `HERMES_HOME`.
- Performance: relatório de toolset/quick mode e FTS local.

## 11. Próxima decisão recomendada

**Fazer primeiro o pacote local/read-only de alinhamento documental, sem mexer em runtime:**

1. Atualizar organograma canônico com profiles ativos e status documental/runtime.
2. Criar matriz única `agente → dono → profile → bot → área Brain → cron registry → status`.
3. Completar docs de LK Shopify e LK Trends.
4. Registrar handoff/receipt desta auditoria.
5. Só depois decidir se aprova migração de cron, restart/launcher ou runtime Zipper.
