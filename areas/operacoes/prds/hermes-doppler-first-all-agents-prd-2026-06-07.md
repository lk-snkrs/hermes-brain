# PRD — Doppler-first para todos os agentes Hermes

Data: 2026-06-07  
Status: **PRD / aprovação antes de implementação**  
Dono: Lucas Cimino  
Executor proposto: Hermes Geral / perfil `hermes-ops-readonly` para auditoria; cada especialista para ativação no próprio runtime  
Escopo: perfis Hermes locais e especialistas em `/opt/data/profiles/*`, perfil default em `/opt/data`, e agentes/subagentes lançados via Hermes/delegation/cron.

## 1. Problema

Os agentes especialistas não têm uma regra uniforme de credenciais. Alguns sabem que devem procurar secrets no Doppler, outros concluem falsamente que uma integração “não está configurada” quando a variável não aparece no `.env` do perfil. Isso gera:

- diagnósticos errados;
- pedidos desnecessários para Lucas reenviar tokens;
- risco de copiar segredo para arquivo local, Brain, skill ou chat;
- workflows quebrados em subagentes/cron porque eles não herdam `DOPPLER_TOKEN` ou não sabem usar o helper;
- baixa autonomia em integrações como GitHub, Vercel, Shopify, Klaviyo, Google, Tiny, WhatsApp, n8n, etc.

## 2. Evidência inicial levantada

Levantamento read-only em 2026-06-07:

- Doppler CLI instalado: `doppler v3.76.0`.
- Token Doppler autorizado já existe fora de repo em:
  - `/opt/data/hermes_bruno_ingest/.secrets/doppler_token`
  - permissões: `0600`.
- Helper existente:
  - `/opt/data/hermes_bruno_ingest/hermes_doppler.sh`
- Mapa não-secreto existente:
  - `/opt/data/hermes_bruno_ingest/doppler_map.md`
- Perfis encontrados em `/opt/data/profiles`:
  - `brain-process`
  - `hermes-ops-readonly`
  - `lc-claude-cli`
  - `lk-analyst-readonly`
  - `lk-collection-optimizer`
  - `lk-content`
  - `lk-content-reviewer`
  - `lk-growth`
  - `lk-ops`
  - `lk-shopify`
  - `lk-trends`
  - `mordomo`
  - `spiti`
- A maioria dos perfis já tem alguma skill Doppler, mas há lacunas ou instruções não uniformes.
- Nenhum perfil deve receber valores de secrets colados em `.env` como solução padrão.

## 3. Objetivo

Criar uma política e runtime de **Doppler-first** para todos os agentes:

> Antes de declarar que uma conexão, API key ou integração está ausente, todo agente deve consultar o mapa/skill Doppler e verificar a existência do secret no Doppler, sem imprimir valores.

## 4. Não objetivos

Este PRD **não** autoriza ainda:

- restart de gateways;
- alterações Docker/VPS/Traefik;
- rotação de secrets;
- escrita em serviços externos;
- cópia de valores de secrets para Brain, skills, `.env`, logs ou chat;
- mudança automática de todos os crons/perfis sem plano de rollback.

Implementação runtime exige aprovação escopada após este PRD.

## 5. Princípios de produto/segurança

1. **Doppler é a fonte de verdade para credenciais.**
2. **Brain e skills guardam nomes, mapas e procedimentos — nunca valores.**
3. **Agentes verificam presença/ausência; valores só entram no processo que precisa executar a chamada.**
4. **Antes de pedir segredo ao Lucas, o agente prova que consultou Doppler ou que o token de acesso ao Doppler está indisponível.**
5. **Subagentes e cron jobs devem receber instrução explícita de Doppler-first no prompt/skill carregado.**
6. **Telegram só recebe alertas acionáveis: erro real, decisão necessária ou conexão faltando; não recebe inventário barulhento de secrets.**
7. **Cada perfil mantém autonomia, mas todos seguem o mesmo contrato mínimo de credenciais.**

## 6. Usuários / atores

- Lucas: quer que agentes encontrem credenciais sem pedir novamente e sem vazar segredos.
- Hermes Geral: orquestrador que roteia tarefas e deve ensinar/lembrar subagentes.
- Perfis especialistas: LK Growth, LK Ops, LK Shopify, LK Trends, LK Content, LKGOC, Mordomo, SPITI, etc.
- Subagentes/delegation: workers efêmeros que precisam receber contexto Doppler-first explicitamente.
- Cron jobs: execuções autônomas sem Lucas presente; devem ser silenciosas quando OK.

## 7. Requisitos funcionais

### RF1 — Skill Doppler comum

Todo perfil Hermes relevante deve ter acesso a uma skill/procedimento `doppler-secrets-operations` ou equivalente local, contendo:

- projeto/config default: `lc-keys/prd`;
- caminho do token autorizado local, quando aplicável;
- comandos seguros para listar nomes, checar existência e rodar processos com env Doppler;
- regra de nunca imprimir valores;
- fallback HTTP quando Doppler CLI não estiver disponível.

### RF2 — Mapa operacional não-secreto

Manter um mapa não-secreto versionável/Brain com:

- domínios de negócio;
- nomes de secrets por integração;
- qual perfil usa qual secret;
- como verificar presença sem valor;
- health checks não sensíveis quando existirem.

Exemplo de grupos:

- Hermes/model providers;
- GitHub/Vercel/infra;
- LK Shopify/Tiny/Google Merchant;
- LK Klaviyo/marketing/analytics;
- WhatsApp/Evolution/n8n;
- SPITI/Hub;
- Google Workspace;
- Metricool/ads/social.

### RF3 — Helper universal seguro

Padronizar helper/scritp, por exemplo:

```text
/opt/data/scripts/hermes_doppler.py
```

Com comandos:

- `names` — imprime apenas nomes;
- `exists SECRET...` — `OK`/`MISSING`, sem valor;
- `get SECRET --exec COMMAND` ou `run COMMAND` — injeta env no processo sem gravar em disco;
- `inventory --profile <name>` — checa só secrets esperados do perfil;
- `doctor` — valida CLI/token/projeto/config sem valores.

O helper deve carregar `DOPPLER_TOKEN` por esta ordem:

1. env atual do processo;
2. arquivo autorizado `/opt/data/hermes_bruno_ingest/.secrets/doppler_token`;
3. falhar com mensagem sanitizada.

### RF4 — Contrato de prompt/AGENTS por perfil

Cada perfil deve receber no seu pacote Brain/skill/AGENTS uma seção padrão:

```text
Credenciais e integrações:
- Antes de declarar que uma credencial está ausente, consulte Doppler lc-keys/prd por nome de secret.
- Use apenas presença/ausência em logs e respostas.
- Não copie secret para Brain, skill, .env, receipt ou Telegram.
- Se o Doppler não estiver acessível, reporte o bloqueio como problema de acesso ao Doppler, não como credencial inexistente.
```

### RF5 — Subagentes/delegation

Quando Hermes Geral delegar uma tarefa que envolva APIs, integrações, repo privado, deploy, email, Shopify, Tiny, Klaviyo, Google, WhatsApp, n8n, etc., o contexto enviado ao subagente deve incluir:

- “Credenciais vivem em Doppler `lc-keys/prd`; verifique nomes/presença sem imprimir valores”; 
- caminho/helper permitido;
- proibição de pedir token ao Lucas antes de verificar Doppler;
- exigência de reportar `values_printed=false`.

### RF6 — Cron jobs

Cron jobs que usam integrações devem:

- chamar o helper ou `doppler run` no script;
- não depender de secrets colados no `.env` do perfil;
- produzir stdout vazio em sucesso silencioso;
- em falha, imprimir só causa sanitizada e ação necessária;
- nunca entregar inventário completo para Telegram.

### RF7 — Diagnóstico obrigatório antes de “não está configurado”

Um agente só pode dizer “integração não configurada” depois de checar:

1. skill/mapa do perfil;
2. nomes esperados no mapa Doppler;
3. acesso ao Doppler CLI/token;
4. presença/ausência do secret no Doppler;
5. se o problema é env injection/runtime, e não falta do secret.

## 8. Requisitos não funcionais

- Segurança: zero vazamento de valores em logs, Brain, Telegram, Git ou skill.
- Portabilidade: funcionar em perfis diferentes e subagentes efêmeros.
- Auditabilidade: cada mudança deve ter receipt sanitizado.
- Silêncio operacional: inventários OK não alertam Lucas.
- Rollback: cada perfil alterado deve ter backup antes de patch.
- Compatibilidade: não quebrar envs já existentes; Doppler-first não significa apagar `.env` atual sem migração separada.

## 9. Abordagens consideradas

### A — Copiar `DOPPLER_TOKEN` para todos os `.env` de perfis

Vantagem:
- simples para runtime.

Desvantagem:
- aumenta superfície de segredo;
- espalha credencial sensível;
- pode conflitar com a regra de não replicar valores;
- precisa higienização/rollback por perfil.

Veredito: **não recomendado como padrão**.

### B — Manter token central e ensinar todos os agentes a usar helper central

Vantagem:
- menor superfície de segredo;
- Doppler segue fonte de verdade;
- scripts e subagentes podem acessar quando autorizados;
- fácil auditar sem valores.

Desvantagem:
- alguns runtimes podem precisar de PATH/env para localizar helper;
- exige patch de skills/AGENTS e prompts de delegation.

Veredito: **recomendado**.

### C — Injetar todos os secrets via `doppler run` no launcher de cada gateway

Vantagem:
- runtime “nasce” com env completo.

Desvantagem:
- todos os secrets ficam disponíveis para o processo inteiro;
- risco de excesso de privilégio;
- restart de gateways necessário;
- mais sensível operacionalmente.

Veredito: útil para perfis específicos, mas não como primeira fase universal.

## 10. Recomendação

Implementar em fases, começando por **B — token central + helper + skill/AGENTS + contrato de subagentes**, sem restart/runtime mutation inicial.

## 11. Fases propostas

### Fase 0 — Aprovação e congelamento de escopo

- Lucas aprova este PRD.
- Escopo inicial: documentação/skills/helpers locais e inventário read-only.
- Bloqueado: restart gateway, Docker/VPS, rotação, escrita externa.

### Fase 1 — Auditoria read-only por perfil

Para cada perfil:

- verificar presença de skill Doppler;
- verificar se AGENTS/MAPA/TOOLS mencionam Doppler-first;
- listar integrações esperadas por nome de secret;
- checar se cron/script falha por “Doppler token missing”.

Saída:

- matriz `perfil → status Doppler-first`;
- lacunas por perfil;
- nenhum valor impresso.

### Fase 2 — Helper universal

- Criar/normalizar helper em `/opt/data/scripts/hermes_doppler.py` ou equivalente.
- Testar:
  - `doctor`;
  - `names`;
  - `exists` com secrets conhecidos;
  - falha sanitizada quando token indisponível.
- Garantir `values_printed=false`.

### Fase 3 — Skill/AGENTS padrão em todos os perfis

- Patch nos perfis relevantes para incluir seção Doppler-first.
- Não copiar valores de secrets.
- Instalar/replicar apenas procedimento, helper path e mapa de nomes.

### Fase 4 — Delegation e cron prompts

- Atualizar prompt/handoff padrão de Hermes Geral para subagentes.
- Atualizar skills de perfis que geram subagentes.
- Atualizar scripts cron críticos para usar helper quando precisarem de integração.

### Fase 5 — Runtime opcional por perfil

Somente com aprovação separada:

- decidir quais perfis precisam de `DOPPLER_TOKEN` no env runtime ou launcher;
- backup do `.env`/launcher;
- patch mínimo;
- restart só do perfil afetado;
- verificação `/proc/<pid>/environ` sem imprimir token;
- health check e receipt.

## 12. Critérios de aceite

Um perfil passa quando:

- tem instrução Doppler-first no seu pacote/skill;
- consegue rodar diagnóstico sanitized sem valores;
- sabe diferenciar:
  - secret inexistente;
  - Doppler inacessível;
  - env runtime não injetado;
  - integração realmente sem configuração;
- nenhum teste/scan encontra valor de secret em Brain/skill/repo;
- cron OK fica silencioso;
- falhas geram alerta acionável, não inventário bruto.

Critérios globais:

- 100% dos perfis listados auditados;
- matriz de status salva em Brain;
- helper universal testado;
- pelo menos 3 integrações reais verificadas por presença/health não sensível;
- Brain health check passa;
- secret scan focado passa;
- nenhum gateway reiniciado sem aprovação explícita.

## 13. Matriz inicial de perfis

Perfis locais prioritários:

- `default` — orquestrador.
- `mordomo` — follow-ups e WhatsApp pessoal.
- `lk-growth` — Growth/SEO/CRO/analytics.
- `lk-ops` — atendimento/operação LK.
- `lk-shopify` — Shopify/LK commerce.
- `lk-trends` — tendências/inteligência.
- `lk-content` — conteúdo/Klaviyo/calendário.
- `lk-content-reviewer` — revisão conteúdo.
- `lk-collection-optimizer` — LKGOC.
- `lk-analyst-readonly` — leitura analítica.
- `spiti` — SPITI/Hub.
- `brain-process` — Brain governance/processamento.
- `hermes-ops-readonly` — auditoria operacional.
- `lc-claude-cli` — agente/CLI auxiliar.

## 14. Riscos e mitigação

Risco: token Doppler central vira ponto único de falha.  
Mitigação: `doctor` sanitizado, alerta acionável, sem concluir “secret ausente” quando o problema é acesso Doppler.

Risco: helper imprime valor por bug.  
Mitigação: testes explícitos, grep/scan em outputs, comandos `exists`/`names` separados de `get/run`.

Risco: perfis com excesso de privilégio.  
Mitigação: na fase 1/2, só nomes e presença; `doppler run` por comando específico, não env global irrestrito.

Risco: Telegram poluído por inventários.  
Mitigação: inventários salvos local/Brain; Telegram só exceções e decisões.

Risco: subagente sem terminal ou sem acesso ao helper.  
Mitigação: contexto deve exigir que ele reporte “não executei” se não tiver ferramenta, sem fabricar resultado.

## 15. Rollback

Para documentação/skills:

- manter backups ou diffs de cada arquivo alterado;
- reverter patch por perfil se a instrução ficar errada.

Para helper:

- preservar versão anterior;
- `mv hermes_doppler.py.bak hermes_doppler.py`.

Para runtime/env/restart, se aprovado em fase posterior:

- backup de `.env` e launcher;
- restart só do perfil afetado;
- rollback restaura arquivo e reinicia mesmo perfil;
- verificar processos por `HERMES_HOME`.

## 16. Perguntas em aberto para aprovação

1. O escopo inicial deve cobrir **todos** os perfis listados ou começar por P0 (`default`, `mordomo`, `lk-growth`, `lk-ops`, `lk-shopify`, `lk-content`, `spiti`)?
2. Você quer que a Fase 1/2 seja só documentação/helper, ou já autoriza patch local de skills/AGENTS dos perfis sem restart?
3. Para runtime, prefere manter token central via helper ou, em perfis críticos, injetar `DOPPLER_TOKEN` no launcher do perfil?

## 17. Pedido de aprovação

Aprovação sugerida para começar sem risco externo:

> Aprovo Fase 1 e Fase 2 do PRD Doppler-first: auditoria read-only de todos os perfis e criação/validação do helper universal, sem restart, sem Docker/VPS, sem copiar valores de secrets, sem escrita externa.

Após isso, Hermes deve entregar a matriz de lacunas e um pacote de implementação da Fase 3 por perfil.
