# Auditoria BRUNO-ATUAL → Hermes Brain

Data: 2026-05-19  
Escopo: material `BRUNO-ATUAL.zip` enviado por Lucas, extraído fora do repositório em `/opt/data/hermes_bruno_ingest/bruno-atual-20260519/` e convertido para textos de análise em `/opt/data/hermes_bruno_ingest/bruno-atual-20260519-analysis/`.  
Tipo de mudança: documentação/auditoria interna. Nenhum dado vivo, credencial, canal externo, campanha, cliente, Docker/VPS ou produção foi alterado.

## Sumário executivo

A versão atualizada do curso do Bruno/OpenClaw está muito mais madura do que um simples conjunto de prompts. Ela ensina uma arquitetura operacional de agente: identidade, workspace, memória, skills, crons, heartbeat, segurança, canais, integrações, multi-agentes e Mission Control.

A conclusão principal é: **Hermes está no caminho certo, e em vários pontos já está acima do padrão básico do OpenClaw**, principalmente em segurança, governança, multiempresa, Doppler, aprovação e separação LK/Zipper/SPITI. O que falta não é “copiar OpenClaw”, e sim fechar alguns gaps Hermes-native: memória quente, auditoria de skills, inventário vivo de crons/canais, normalização dos agentes/documentação legada e reconciliação do status do Mission Control.

Nota geral ponderada: **8,0/10**.

## Material processado

Arquivos relevantes lidos/analisados a partir do pacote extraído:

- `1. LEIA PRIMEIRO (MAPA DO CURSO).docx`
- `3. Changelog (atualizações dos materiais).docx`
- `Materiais Aula/LEIA PRIMEIRO.docx`
- Aulas 0.0, 0.1 e 1–15 em HTML extraído
- Starter kit / LEIA PRIMEIRO
- Templates de agente: `SOUL`, `IDENTITY`, `AGENTS`, `USER`, `MAPA`, `HEARTBEAT`
- Exemplos da Amora
- Cases: Amora, Aurora/Brunner, Chris/Everest, Filippe César, Igor Gouveia
- Referências complementares: onboarding, identidade, workspace, memória, skills, crons, canais, integrações, multi-agente e Mission Control

Artefatos locais fora do Brain:

- ZIP original: `/opt/data/hermes_bruno_ingest/inbox/whatsapp-hermes/2026-05-19/BRUNO-ATUAL.zip`
- Extração: `/opt/data/hermes_bruno_ingest/bruno-atual-20260519/`
- Textos convertidos: `/opt/data/hermes_bruno_ingest/bruno-atual-20260519-analysis/texts/`
- Inventário: `/opt/data/hermes_bruno_ingest/bruno-atual-20260519-analysis/inventory.md`

Regra aplicada: **material bruto de terceiro fica fora do Hermes Brain**. Este relatório salva apenas a auditoria e as decisões de adaptação Hermes-native.

## O que atualizou no curso do Bruno

### 1. Curso virou material para humano e agente

O curso agora é desenhado para que o humano entenda o porquê, mas o agente consiga ler o pacote, criar checklist, configurar workspace e operar os próximos passos. Isso muda a lógica de consumo: o aluno não é só espectador; ele entrega o pacote ao agente e o agente ajuda a implementar.

Adaptação Hermes: criar/fortalecer o padrão “material ingest → análise → matriz Bruno/Hermes → PRD → plano → execução segura”. O Hermes já tem parte disso; o relatório confirma que esse caminho deve ser o padrão oficial.

### 2. Changelog e limpeza estrutural

O changelog registra limpeza forte em 2026-05: remoção de duplicatas, padronização de nomes, sanitização de exemplos, atualização do Starter Kit e melhoria de LEIA PRIMEIRO em várias pastas.

Adaptação Hermes: evitar importar material antigo ou duplicado. Usar sempre inventário, extração limpa, relatório e secret scan antes de versionar qualquer coisa.

### 3. Starter Kit virou eixo operacional

O Starter Kit é o coração prático: README, checklist viva, changelog, skills, templates, prompts, cheatsheets e workspace starter. A ideia principal é o agente transformar material didático em operação.

Adaptação Hermes: criar um **Hermes Brain Starter Kit** não como cópia do OpenClaw, mas como pacote Hermes-native com:

- LEIA PRIMEIRO do Brain;
- checklist viva de onboarding;
- matriz de decisão Bruno → Hermes;
- templates de agente;
- política de memória;
- política de skills;
- política de crons/heartbeat;
- segurança/Doppler/aprovação;
- rotina de health check e secret scan.

### 4. Tavily virou default de busca no OpenClaw

O curso corrigiu o default de busca: Brave deixou de ser preferido por restrições de free tier e Tavily virou sugestão principal para agentes.

Adaptação Hermes: não copiar o comando OpenClaw; registrar apenas o princípio: search provider deve ser documentado, configurável, auditável, com segredo no cofre e teste dry-run.

### 5. Correção de comandos inexistentes

O curso corrige comando inexistente de `TAVILY_API_KEY` e aponta fluxo correto: `.env`/config → dry-run → apply → reload → audit.

Adaptação Hermes: validação importante. O Hermes deve continuar evitando “comandos inventados”. Toda integração nova precisa de documentação real, dry-run e verificação.

## Aula por aula — leitura e decisão Hermes

### Aulas 0.0 e 0.1 — visão e cases

Bruno ensina que agente não é chat: é funcionário digital com contexto, memória, skills, rotinas, canais e ferramentas. Os cases mostram destino possível, especialmente Amora como Chief of Staff.

Hermes já faz melhor/diferente: possui execução real por ferramentas, memória persistente, `session_search`, skills nativas, cronjobs e integração multiempresa.  
Decisão: **aplicar como modelo mental**, sem copiar stack OpenClaw.

### Aula 1 — ativando agente e canal

Bruno separa credenciais de modelo, OAuth/API e primeiro canal humano, com Telegram como quick win.

Hermes já está Telegram-first e multi-profile.  
Decisão: **adaptar** para onboarding Hermes: canal, identidade, permissões, memória inicial e teste de resposta.

### Aula 2 — CLI/cockpit/doctor

Bruno trata terminal como cockpit operacional: status, doctor, restart, security audit, restore e health check.

Hermes já possui ferramentas e cron/watchdog, mas precisa consolidar cockpit humano em Mission Control e docs.  
Decisão: **aplicar** como padrão: todo agente/projeto deve ter status, health, audit, backup/rollback e verificação.

### Aula 3 — Starter Kit

A aula mais importante para adaptação. O agente lê um zip, cria checklist viva e executa blocos.

Hermes já consegue fazer isso com extração, OCR/DOCX, subagentes e relatórios.  
Decisão: **aplicar fortemente** criando um Starter Kit Hermes-native e mantendo material bruto fora do Brain.

### Aula 4 — Telegram, grupos e tópicos

Telegram é canal default pela API, tópicos e permissionamento. Grupos devem usar menção/allowlist quando necessário.

Hermes já usa Telegram como principal, mas ainda há múltiplos perfis/bots que precisam mapa vivo.  
Decisão: **adaptar** para matriz de canais: DM, grupo, bot, profile, escopo, responsável, regra de silêncio.

### Aula 5 — identidade, SOUL, USER, AGENTS

Bruno ensina que agente sem identidade é chat genérico. Arquivos de identidade precisam nascer de diálogo e evoluir com correções.

Hermes já tem `agentes/hermes-geral`, LK, Zipper e SPITI, mas há gaps em marcas legadas e Mordomo.  
Decisão: **aplicar parcialmente**: fortalecer identidade operacional sem burocratizar.

### Aula 6 — workspace e MAPAs

Bruno usa `MAPA.md` distribuído e pastas com propósito. A ideia transferível é navegação viva, não estrutura literal.

Hermes já tem mapas multiempresa mais ricos que OpenClaw.  
Decisão: **manter Hermes-native**, apenas reforçando archive/higiene e mapas locais atualizados.

### Aula 7 — memória

Bruno separa memória de boot, sessão, semântica, daily notes, `hot.md`, compactação e reset.

Hermes tem memória persistente, session search e Brain, mas falta um `hot/current` mais canônico e dailies/higiene mais visíveis.  
Decisão: **aplicar** como gap principal.

### Aula 8 — skills

Prompt resolve uma vez; skill resolve mil vezes. Skills devem ter gatilho, passos, output e verificação.

Hermes já tem skills nativas e regra repetição→sistema.  
Decisão: **aplicar** com auditoria de skills: status, owner, último uso/revisão, risco e depreciação.

### Aula 9 — crons e heartbeat

Skill = o quê. Cron = quando. Heartbeat = respiração/proatividade. Silêncio é feature.

Hermes já tem cronjobs e política silent-OK, mas precisa inventário vivo e reconciliação entre rotina documentada e cron ativo.  
Decisão: **aplicar** com matriz viva de crons/canais e kill criteria.

### Aula 10 — segurança

Secrets em cofre, escopo mínimo, prompt injection, canais públicos, recovery e auditoria.

Hermes está muito forte aqui: Doppler, aprovação A4, secret scan, não imprimir secrets, limites de Docker/VPS.  
Decisão: **manter e reforçar**; não relaxar para copiar autonomia OpenClaw.

### Aulas 11 e 12 — canais e integrações

Canais são onde o agente fala; integrações são em cima do que ele opera. Cada nova conexão precisa escopo, auth, teste e monitoramento.

Hermes já separa WhatsApp, Telegram, Google, Shopify, Supabase, Klaviyo, Meta, VPS e GitHub com permissões.  
Decisão: **adaptar** criando/atualizando matriz única de canais e integrações.

### Aula 13 — multi-agentes

Bruno recomenda começar com 1 agente forte. Subagente é pontual; agente paralelo só com domínio contínuo.

Hermes está alinhado: Grande Mente central, agentes documentais e runtime profiles separados.  
Decisão: **manter** e evitar sprawl. LK/Zipper/SPITI devem crescer por Chief of Staff + skills/rotinas antes de especialistas demais.

### Aula 14 — Mission Control

Bruno trata Mission Control como fase avançada: template, auditoria, PRD, execução em chunks, iteração por Telegram.

Hermes já tem Mission Control em evolução, mas precisa reconciliação documental entre versões/legado/ativo e status real.  
Decisão: **aplicar como protocolo**, não apenas UI: Mission Control deve mostrar estado, aprovações, receipts, rollback e bloqueios.

### Aula 15 — fechamento

O curso fecha dizendo que o produto real é modelo mental + prática diária + memória + automações.

Hermes está alinhado.  
Decisão: **manter filosofia de aprendizado contínuo**: correções de Lucas viram Brain/skills/rotinas.

## Lições dos cases

### Amora

Amora é o benchmark de maturidade: Chief of Staff central, tom próprio, memória, crons, skills, inbox e múltiplos canais. Mas é destino, não ponto de partida.

Aplicar no Hermes:

- fortalecer Hermes Geral como CoS/Grande Mente;
- manter `hot/current` central;
- proatividade com poucos checks úteis;
- transformar repetição em skill;
- Text/Telegram → Brain quando decisão durável.

Não aplicar literalmente:

- 60+ crons;
- envio externo automático;
- múltiplos canais sem volume;
- contexto privado em grupos;
- broad ownership que mistura LK/Zipper/SPITI.

### Filippe César

Case mais parecido com Lucas: múltiplas empresas com um Chief of Staff coordenador.  
Aplicação: Hermes Geral coordena; LK, Zipper e SPITI são áreas/agentes com isolamento; comunicação entre domínios passa por roteamento central.

### Aurora/Brunner

Mostra que PME tradicional ganha com automação de dor real.  
Aplicação: para LK, Zipper e SPITI, começar por problemas operacionais concretos, não por arquitetura bonita.

### Igor e Chris

São inspiração para estágios mais avançados: multi-agentes especializados e outbound/provas de valor.  
Aplicação: adiar até haver maturidade, dados confiáveis e aprovação de risco.

## Auditoria do Hermes Brain atual

### Notas por dimensão

- Segurança: **9/10**
  - Forte em Doppler, approval gates, secret scan e limites A4.
  - Gap: alguns documentos operacionais antigos ainda merecem saneamento de comandos/placeholders.

- Segundo cérebro / Brain: **9/10**
  - Forte em Brain GitHub como fonte de verdade, `memories/`, áreas, empresa, agentes, rotinas e reports.
  - Gap: ainda há legado histórico e nomenclatura antiga em partes do repositório.

- Identidade / agentes: **8/10**
  - Hermes Geral, LK, Zipper e SPITI têm estrutura documental.
  - Gap: LK/Zipper têm marcas legadas; Mordomo existe como runtime/profile, mas precisa documentação completa.

- Workspace / mapas: **8/10**
  - Estrutura multiempresa é melhor que a estrutura OpenClaw genérica.
  - Gap: regra de archive/higiene e mapas locais pode ficar mais explícita.

- Memória: **7/10**
  - Boa arquitetura conceitual, com memory tool, session_search e Brain.
  - Gap: falta camada quente canônica tipo `hot.md`, dailies/últimas 48h e rotina clara de higiene.

- Skills: **7/10**
  - Skills existem e a regra repetição→sistema está correta.
  - Gap: precisa auditoria de uso, owner, risco, última revisão e promoção de rotinas maduras para skills.

- Crons / heartbeats: **8/10**
  - Forte em silent-OK, aprovação antes de cron novo e distinção rotina vs cron ativo.
  - Gap: precisa inventário vivo consolidado de crons/bots/profiles e status real.

- Integrações / canais: **8/10**
  - Forte em Doppler, read-only por padrão e separação por negócio.
  - Gap: falta matriz única atualizada com canal, escopo, bot/profile, allowlist, status e responsável.

- Multi-agentes: **7/10**
  - Bom modelo Grande Mente → áreas/profiles, sem sprawl.
  - Gap: documentar melhor Mordomo e consolidar health/custo/status por profile.

- Mission Control: **7,5/10**
  - Produto avançou: Work Kernel, preview, approvals, runner simulado e receipts.
  - Gap: reconciliar documentação histórica do Mission Control para deixar claro o que é ativo, legado, benchmark e próxima camada.

- Governança / aprovação: **9/10**
  - Excelente: preview-first, A4 para externo/prod/secrets/destrutivo, rollback/receipts.
  - Gap: ledger único de aprovações/decisões por data/área/risco/status.

Nota geral ponderada: **8,0/10**.

## O que estamos fazendo certo

1. **Hermes não está copiando OpenClaw cegamente.** Está adaptando para Lucas, LK, Zipper, SPITI e infraestrutura real.
2. **Segurança e aprovação estão acima do básico.** O curso fala em cofre/scope; Hermes já tem Doppler, A4, read-only, preview e secret scan.
3. **Grande Mente está correta.** O modelo “agente não é o cérebro; agente lê/escreve no Brain” está internalizado.
4. **Multiempresa está melhor que o padrão genérico.** Há separação real de LK/Zipper/SPITI e guardrails contra mistura.
5. **Mission Control evoluiu com a filosofia certa.** Preview-first, receipts, rollback e zero writes externos automáticos são a versão Hermes-native da Aula 14.
6. **Learning loop está presente.** Correções de Lucas viram memória, skill, Brain e rotina quando são duráveis.

## O que falta melhorar

### P0 — próximos ajustes mais importantes

1. **Criar/normalizar camada de contexto quente**
   - Equivalente Hermes de `hot.md`.
   - Deve mostrar prioridades, bloqueios, decisões recentes, próximos eventos e riscos por Lucas/LK/Zipper/SPITI/Hermes.

2. **Inventário vivo de crons, bots e profiles**
   - Um lugar único: profile, bot, canal, destino, cadência, status, último check, silent contract, kill criteria.
   - Separar claramente documentação de execução real.

3. **Auditoria de skills**
   - Status, owner, risco, gatilho, última revisão, última execução, se está canônica ou obsoleta.

4. **Reconciliar Mission Control**
   - Um documento único dizendo: versão ativa em produção, versões históricas, benchmark TenacitOS/OpenClaw, próximos módulos e invariantes de segurança.

5. **Documentar Mordomo como agente/profile completo**
   - SOUL/IDENTITY/AGENTS/TOOLS/USER/MEMORY/HEARTBEAT ou equivalente Hermes.
   - Limites explícitos: pode ler/intake; não envia externo sem aprovação atual.

### P1 — melhorias estruturais

1. Matriz única de canais e integrações.
2. Regra de archive/higiene mensal mais explícita.
3. Ledger de aprovações/decisões com risco e rollback.
4. Starter Kit Hermes-native para onboarding de novos projetos/agentes.
5. Template de fechamento de fase com: entregue, verificado, não alterado, decisão, lição, próximo passo.

### P2 — futuro

1. Multi-agentes especialistas apenas após volume real.
2. Mission Control com snapshots read-only vivos por fonte.
3. Automação com execução real somente após payload, destino, aprovação explícita e rollback.
4. Relatórios visuais/painéis quando o fluxo textual já estiver confiável.

## Recomendações de adaptação para o ecossistema Hermes

### 1. Criar o “Hermes Brain Starter Kit”

Um pacote operacional próprio do Hermes para qualquer novo domínio/projeto. Deve conter:

- `LEIA PRIMEIRO` Hermes;
- checklist viva;
- template de PRD;
- matriz Bruno → Hermes;
- templates de identidade/agente;
- política de memória;
- política de skill;
- política de cron/heartbeat;
- segurança/Doppler/aprovação;
- comandos de verificação;
- relatório de fechamento.

### 2. Criar camada `hot/current` do Hermes

Formato recomendado:

- Lucas pessoal: prioridades e pendências quentes;
- LK: status/gaps comerciais e dados vivos necessários;
- Zipper: inbox/follow-ups/feiras/artistas;
- SPITI: leilões/lances/riscos;
- Hermes/Infra: crons, gateway, releases, incidentes;
- decisões recentes;
- bloqueios;
- próxima ação segura.

### 3. Criar auditoria periódica de skills

Campos mínimos:

- skill;
- área;
- gatilho;
- owner;
- risco;
- última revisão;
- última execução conhecida;
- status: ativa, draft, obsoleta, substituir, consolidar;
- gaps/verificação.

### 4. Criar inventário vivo runtime/profile/canal

Campos mínimos:

- profile/runtime;
- bot/canal;
- owner;
- propósito;
- fonte de verdade;
- permissões;
- cron/watchdog associado;
- estado atual;
- último check;
- regra de silêncio;
- ação bloqueada sem Lucas.

### 5. Reconciliar Mission Control

Documento único deve responder:

- Qual commit/marker está em produção.
- Quais módulos estão feitos.
- O que é preview/simulação/read-only.
- Quais ações continuam bloqueadas.
- Qual é o próximo bloco seguro.
- Como se valida antes/depois de deploy.

## Decisão final

- **Aplicar:** Starter Kit Hermes-native, contexto quente, skill audit, inventário vivo, matriz de canais, reconciliação Mission Control, documentação Mordomo.
- **Adaptar:** SOUL/IDENTITY/AGENTS/USER/MAPA/HEARTBEAT como camadas Hermes, não como cópia literal de OpenClaw.
- **Adiar:** multi-agentes especialistas, crons numerosos, canais adicionais e execução externa real.
- **Não aplicar literalmente:** comandos OpenClaw, caminhos OpenClaw, 60+ crons da Amora, envio externo automático, multi-canal sem volume, dashboard como primeiro passo.

## Verificação desta auditoria

- Material bruto ficou fora do Brain.
- Nenhuma credencial foi copiada.
- Nenhuma ação externa foi executada.
- Nenhum runtime, VPS, Docker, banco, campanha, WhatsApp, e-mail ou produção foi alterado.
- Este relatório é documentação interna para orientar próximas fases do Hermes Brain.
