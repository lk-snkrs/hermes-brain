# PRD — Mission Control Hermes read-only

## 1. Contexto

A aula 14 do Bruno/OpenClaw apresenta Mission Control como cockpit acima da observabilidade nativa: dashboard, status, auditoria, PRD/build/iteração e comandos claros.

No Hermes Brain já existia uma pendência explícita para separar dois significados de “Mission Control”:

1. formato de criativo/performance citado na imersão;
2. protocolo operacional de inventário + health check citado em análises de maturidade.

Este PRD adapta o conceito para Hermes sem copiar OpenClaw literalmente.

## 2. Problema

Lucas opera várias frentes ao mesmo tempo: LK, Zipper, SPITI, Hermes Brain, Spiti Hub, integrações, crons, runtime e aprovações. O Brain tem documentação rica, mas ainda falta uma camada executiva única que responda rapidamente:

- o que está saudável;
- o que está pendente;
- o que exige decisão do Lucas;
- o que é risco;
- o que mudou recentemente;
- onde estão as evidências.

Sem isso, o custo cognitivo de navegar o Brain cresce conforme o sistema fica mais completo.

## 3. Objetivo

Criar um Mission Control Hermes **read-only**, primeiro como relatório Markdown/Telegram, depois possivelmente como UI, para consolidar status operacional sem executar ações destrutivas ou externas.

## 4. Não objetivos

- Não criar app visual nesta fase.
- Não criar botões de ação destrutiva.
- Não alterar VPS, Docker, Traefik, volumes, redes ou deploy.
- Não consultar/mutar banco sem necessidade e autorização.
- Não enviar WhatsApp/email/campanha/post.
- Não expor segredos.
- Não substituir o Hermes Brain; Mission Control é vista executiva, não fonte de verdade.

## 5. Usuários

- Lucas: decisor executivo.
- Hermes Geral: gera relatório, verifica evidências e recomenda próximos passos.
- Agentes/áreas: fornecem contexto por domínio.

## 6. Escopo MVP read-only

O MVP deve gerar um relatório com:

1. **Status do Brain**
   - health check;
   - secret scan;
   - links/índices;
   - docs de agentes.

2. **Status de operações**
   - rotinas documentadas;
   - crons reais quando verificados;
   - pendências abertas;
   - PRs/branches relevantes.

3. **Status por negócio**
   - LK;
   - Zipper;
   - SPITI;
   - Operações/Infra.

4. **Aprovações necessárias**
   - ações externas;
   - produção/infra;
   - banco/secrets;
   - merge de risco;
   - campanhas/contatos.

5. **Riscos e alertas**
   - tokens expirados ou pendentes sem imprimir valores;
   - runtime divergente;
   - monitor não confirmado;
   - dados/fonte de verdade ausentes.

6. **Próximas ações seguras**
   - correções documentais;
   - PRs de baixo risco;
   - investigações read-only;
   - decisões que Lucas precisa tomar.

## 7. Dois blocos do conceito “Mission Control”

### 7.1 Mission Control criativo/performance

Uso: marketing, criativos, mídia paga, campanhas e aprendizado.

Versão Hermes-native:

```text
hipótese
→ criativo/campanha em preview
→ dados reais
→ learning
→ próxima hipótese
```

Aplicação provável:

- LK tráfego/CRM;
- Zipper comunicação/feiras;
- SPITI conteúdo/leilão, com cautela.

Guardrail: nenhum anúncio, campanha, post, mensagem ou orçamento é alterado sem aprovação Lucas.

### 7.2 Mission Control operacional

Uso: status do sistema, Brain, integrações, crons, PRs, riscos e aprovações.

Versão Hermes-native:

```text
Brain + rotinas + integrações + crons + PRs + pendências
→ relatório executivo read-only
→ recomendações
→ aprovação antes de qualquer ação sensível
```

Este é o foco do MVP.

## 8. Fontes de dados permitidas no MVP

- `scripts/brain_health_check.py`.
- Secret scan local sem valores.
- `CHANGELOG.md`.
- `ROADMAP-30-DIAS-HERMES.md`.
- `empresa/gestao/pendencias.md`.
- `memories/pending.md`.
- `empresa/rotinas/_index.md`.
- `areas/*/MAPA.md`.
- Rotinas em `areas/operacoes/rotinas/`.
- Git local/GitHub PRs quando credencial segura estiver disponível.
- Cronjob list do Hermes quando a tarefa for local e segura.

Fontes com cuidado/aprovação:

- VPS/Docker/Hostinger: read-only apenas.
- Supabase/Shopify/APIs: read-only e só quando necessário.
- Emails/WhatsApp/canais externos: somente leitura explícita e sem envio.

## 9. Requisitos funcionais

### RF1 — Relatório executivo

Gerar relatório com status, riscos, pendências, evidências e próximos passos.

### RF2 — Separar fato/interpretação/recomendação

Cada item deve distinguir:

- fato verificado;
- interpretação;
- recomendação;
- aprovação necessária.

### RF3 — Evidência obrigatória

Toda afirmação de saúde ou falha deve apontar para:

- comando/check executado;
- arquivo consultado;
- timestamp;
- PR/commit quando aplicável.

### RF4 — Classificação de risco

Cada recomendação deve ser classificada:

- L0/L1: leitura/documentação;
- L2: branch/PR documental;
- L3: código/integração não produtiva;
- L4: produção/dados/externo;
- L5: destrutivo/admin.

### RF5 — Bloqueio de ações sensíveis

O Mission Control não executa diretamente ações L4/L5. Ele prepara preview/plano e pede aprovação.

## 10. Requisitos não funcionais

- Português por padrão.
- Sem segredos.
- Curto o suficiente para Telegram.
- Detalhado o bastante para auditoria no Brain.
- Reprodutível.
- Seguro por padrão.
- Compatível com evolução futura para UI.

## 11. Formato inicial de output

```md
# Mission Control Hermes — YYYY-MM-DD

## Status geral

## LK

## Zipper

## SPITI

## Operações / Brain / Runtime

## Aprovações pendentes

## Riscos

## Próximas ações seguras

## Evidências
```

## 12. Fases

### Fase 0 — PRD documental

Status: este documento.

### Fase 1 — Relatório Markdown manual

Usar template de report executivo e Brain Improvement Score para gerar um primeiro Mission Control manual.

### Fase 2 — Script/gerador opcional

Automatizar coleta local segura quando o padrão estabilizar.

### Fase 3 — Cron sob aprovação

Enviar briefing em cadência aprovada por Lucas.

### Fase 4 — UI read-only

Somente se Markdown/Telegram provar valor. Sem botões destrutivos no MVP.

## 13. Riscos

- Virar dashboard bonito sem fonte confiável.
- Misturar status documentado com execução real.
- Expor segredos por excesso de coleta.
- Criar botões perigosos cedo demais.
- Automatizar antes de estabilizar formato.

## 14. Critérios de pronto do MVP

- Primeiro relatório manual gerado.
- Health check e secret scan executados.
- Pendências e aprovações separadas.
- Nenhuma ação externa/produtiva executada.
- Lucas consegue decidir próximos passos em menos tempo.

## 15. Decisão Hermes-native

Aplicar o conceito, mas começar como relatório/protocolo read-only. UI e automação ficam para depois. O Mission Control deve ser uma vista executiva do Brain, não um segundo Brain nem um painel com poderes perigosos.
