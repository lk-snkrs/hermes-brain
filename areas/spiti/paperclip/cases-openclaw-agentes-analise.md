# Análise dos cases OpenClaw para adaptação Hermes/Paperclip/SPITI

> Fonte: ZIP enviado por Lucas em 2026-05-05, extraído localmente em `/opt/data/cache/documents/paperclip_cases_20260505/`.

## LEIA PRIMEIRO — síntese

O pacote se apresenta como exemplos reais de agentes OpenClaw em produção. O objetivo declarado é usar os cases como inspiração concreta, não como receita para copiar literalmente.

Arquivos encontrados no pacote:

- `case-amora.md` — Bruno Okamoto / Pixel Educação: Chief of Staff multi-domínio.
- `case-aurora-brunner.md` — loja tradicional de seminovos: transformação PME com agente operacional.
- `case-igor-gouveia.md` — agência/e-commerce: time multiagente especializado.
- `case-filippe-cesar.md` — empreendedor com 3 empresas: 1 agente por empresa + CoS coordenador.
- `case-chris-everest.md` — outbound híbrido digital + físico.

Observação: Lucas mencionou “3 cases”, mas o ZIP contém 5 cases além do LEIA PRIMEIRO.

A regra principal do próprio material: escolher o arquétipo mais próximo, identificar 1 ideia replicável e adaptar ao contexto. Não copiar tudo.

## Leitura Hermes-native

Para Lucas, o equivalente não é “criar vários agentes porque o case fez”. O equivalente correto é:

1. Hermes Brain continua como fonte de verdade durável.
2. Paperclip pode virar o painel operacional de issues/projetos/agentes.
3. Hermes pode continuar como copiloto externo primeiro; conectar como `hermes_local` depois, se houver volume real.
4. Começar com 1 agente/CoS bem definido e poucas rotinas.
5. Criar skills para tarefas repetitivas que realmente acontecem.
6. Guardrails fortes para ações externas, dados sensíveis e produção.

## Case Amora — aplicação para Lucas

Ideia central: um Chief of Staff único, muito contextual, com skills e rotinas, pode substituir uma proliferação prematura de agentes.

Aplicável para Lucas:

- Criar/fortalecer um “Lucas Chief of Staff” ou “Hermes Geral” para visão multiempresa.
- Para SPITI/Paperclip, começar com `SPITI Chief of Staff`, não com 5 agentes separados.
- Transformar tarefas repetitivas em skills: briefing de leilão, revisão de backlog, auditoria SEO, relatório semanal, triagem de pendências.
- Começar com 2–3 rotinas, não 60+ crons.

Não aplicar agora:

- 60+ crons.
- Muitos canais/agentes.
- Automação externa sem volume/controle.

## Case Filippe César — aplicação para Lucas

Ideia central: multiempresa precisa de separação de contexto e um CoS coordenador. Agentes de empresas diferentes não conversam diretamente; passam pelo CoS.

Muito aplicável para Lucas, porque há LK Sneakers, Zipper Galeria e SPITI Auction.

Arquitetura recomendada:

- CoS geral: Hermes/Lucas Chief of Staff.
- Agente/área LK: e-commerce/CRM/campanhas.
- Agente/área Zipper: vendas de obras/comunicação/colecionadores/feiras.
- Agente/área SPITI: leilão, Spiti Hub, SEO, newsletter, analytics.

Regra crítica:

- Não misturar dados/contexto/credenciais entre empresas.
- SPITI e Zipper têm interseções, mas dados de leilão, Zipper Vendas e CRM devem permanecer separados.

Implementação recomendada:

- No Hermes Brain: manter `areas/lk`, `areas/zipper`, `areas/spiti` e permissões claras.
- No Paperclip: criar Companies separadas apenas se o uso crescer. Inicialmente, usar uma Company SPITI para o projeto atual.

## Case Igor Gouveia — aplicação para Lucas

Ideia central: multiagente especializado faz sentido quando há domínios distintos e volume real.

Aplicável parcialmente para SPITI, mas só depois do CoS amadurecer.

Possíveis agentes futuros no Paperclip/SPITI:

- Estrategista/Growth: direção de SEO, conteúdo e campanhas.
- Criativo: copies, artes, ângulos e briefing visual.
- Técnico: Spiti Hub, GitHub, PRs, bugs, tracking.
- CRM/Newsletter: MailerLite/Klaviyo, segmentação, calendário editorial.
- Analytics: GA/GSC/Search Console, relatórios, oportunidades.

Não criar todos no dia 1. Primeiro validar volume com um CoS e projetos/issues.

## Case Aurora — aplicação para Lucas

Ideia central: começar por uma dor operacional real e criar skills específicas de domínio.

Aplicável para SPITI:

- Começar por dores concretas, não por arquitetura bonita.
- Exemplos de skills específicas SPITI:
  - `verificar-lances-spiti`
  - `briefing-lote-spiti`
  - `auditar-spiti-hub`
  - `gerar-post-seo-leilao`
  - `relatorio-pos-leilao`
  - `triagem-divergencia-lances`

Cuidado:

- SPITI lida com dados sensíveis e lances. “Silêncio > dado errado.”
- Não automatizar atendimento externo sem validação e aprovação.

## Case Chris Everest — aplicação para Lucas

Ideia central: outbound/prova de valor personalizada pode ser mais poderoso que campanha genérica.

Aplicável para SPITI/Zipper com muita cautela:

- Em vez de postcard físico, adaptar para prova de valor digital curatorial:
  - landing/dossiê personalizado para consignadores potenciais;
  - relatório de visibilidade para artistas/colecionadores;
  - proposta visual de lote/leilão;
  - peça editorial personalizada para relacionamento.

Não aplicar direto:

- scraping agressivo;
- contato automático com colecionadores/artistas;
- envio físico/emails sem aprovação.

Potencial futuro:

- “SPITI Consignment Intelligence”: identificar potenciais consignadores/lotes, montar dossiês e rascunhos de abordagem para aprovação humana.

## Decisão recomendada

Implementar, mas em fases:

### Fase 1 — Agora

- Usar Paperclip como painel operacional SPITI.
- Criar 1 agente: `SPITI Chief of Staff`.
- Criar projetos iniciais: Spiti Hub, SEO/Content, Newsletter/CRM, Criativos, Analytics, Future Site.
- Criar backlog de 15–25 issues.
- Criar guardrails de aprovação.

### Fase 2 — Após 1–2 semanas de uso real

- Identificar tarefas repetidas.
- Transformar em skills Hermes/Paperclip.
- Criar 2–3 rotinas leves:
  - revisão semanal SPITI;
  - auditoria SEO semanal;
  - triagem de backlog/bugs Spiti Hub.

### Fase 3 — Só com volume comprovado

- Separar agentes especializados.
- Conectar Hermes via `hermes_local` se Paperclip precisar executar tarefas usando memória, repo local e skills Hermes.
- Criar integração API/webhook com aprovações.

## Primeiros 5 passos práticos

1. Finalizar a criação da Company SPITI no Paperclip.
2. Criar o `SPITI Chief of Staff` com a task inicial já redigida.
3. Pedir para ele gerar plano de 30 dias + backlog.
4. Eu reviso o output dele e converto em estrutura real do Hermes Brain/Paperclip.
5. Depois escolhemos 1 skill operacional para implementar primeiro.

## Conclusão

Sim, os cases são implementáveis para Lucas, mas o melhor caminho é a lógica dos cases, não a cópia da arquitetura. Para o momento atual, o case mais importante é uma combinação de:

- Amora: 1 CoS forte antes de multiagente.
- Filippe: separação multiempresa com CoS coordenador.
- Aurora: começar por dor real e skill específica.

Igor e Chris são úteis como visão futura, depois que houver volume e maturidade.
