# AI Visibility v2 — Onitsuka Tiger audit

Data UTC: 20260618T145226Z
Área: LK Collection Optimizer / LKGOC
Status: read-only audit + approval packet preparado. **Nenhum write em produção executado nesta etapa.**
Claude SEO: aplicado.
Decision-grade: não. Falta GSC/GA4 por URL e métrica LLM mentions continua bloqueada por plano/acesso.

## Escopo auditado

- Hub Onitsuka Tiger: `/collections/onitsuka-tiger-todos-os-modelos` e alias público `/collections/onitsuka-tiger`
- Collection Mexico 66: `/collections/onitsuka-tiger-mexico-66`
- Guia geral: `/pages/onitsuka-tiger-original-brasil-guia-lk`
- Guia Mexico 66: `/pages/guia-onitsuka-tiger-mexico-66`
- Subclusters via Shopify/API/read-only:
  - Mexico 66 Sabot: `/collections/onitsuka-tiger-mexico-66-sabot`
  - Mexico 66 Metallic Series: `/collections/onitsuka-tiger-mexico-66-metallic-series`
  - Mexico 66 Slip-On: `/collections/onitsuka-tiger-mexico-66-slip-on`
  - Mexico 66 Fringe: `/collections/onitsuka-tiger-mexico-66-fringe`
  - Astroboy, Versace, California 78 EX, Mexico Mid, Otiger Court, Moage CO, Tsunahiki Slip-On, TGRS, Exposed.

## Demanda Google Brasil — DataForSEO

- `onitsuka tiger`: 33.100/mês; tendência anual +83%; intent transactional.
- `onitsuka tiger mexico 66`: 8.100/mês; tendência anual +83%; intent transactional.
- `onitsuka tiger brasil`: 1.300/mês; intent transactional.
- `mexico 66`: 880/mês; intent informational.
- `onitsuka tiger kill bill`: 720/mês; intent transactional.
- `onitsuka tiger feminino`: 480/mês; intent transactional.
- `onitsuka tiger prata`: 110/mês.
- `onitsuka tiger mexico 66 sd`: 90/mês; tendência anual +425%.
- `onitsuka tiger original`: 90/mês.
- `onitsuka tiger slip on`: 30/mês.
- `mexico 66 sabot`: 30/mês.

## Diagnóstico

### O que já está forte

- O source map AI já contém Onitsuka Tiger geral, guia geral, Mexico 66 e guia Mexico 66.
- Hub e Mexico 66 já têm conteúdo editorial forte, FAQ e linguagem de curadoria.
- Guia Mexico 66 já tem “Bloco citável LK”, tabela de versões e FAQ: é o gold source atual do cluster.
- A taxonomia de produto é rica: Sabot, Slip-On, Metallic, Fringe e collabs existem como collections separadas.

### Lacunas de AI Visibility

- Hub Onitsuka e collection Mexico 66 não expõem “Bloco citável LK” de forma explícita no conteúdo simplificado.
- Guia geral Onitsuka é bom, mas falta um parágrafo canônico curto para IA citar sem depender de muitos trechos.
- `llms.txt` e `agents.md` ainda não apontam diretamente para Sabot, Slip-On e Metallic Series, embora esses subclusters existam e sejam úteis para respostas comparativas.
- `onitsuka-tiger-mexico-66-sd` retorna 404; SD deve continuar como subversão dentro do hub/guia ou exige decisão de criar collection canônica separada.
- Algumas metas de subcollections ainda estão genéricas (“Exclusivo”, “100% originais”, “10x sem juros”) e menos úteis para AI Search.

## Priorização recomendada

### P0 — publicar no v2

1. Inserir bloco citável no hub Onitsuka Tiger.
2. Inserir bloco citável na collection Mexico 66.
3. Inserir bloco citável no guia geral Onitsuka.
4. Atualizar `llms.txt` e `agents.md` com subclusters:
   - Mexico 66 Sabot
   - Mexico 66 Metallic Series
   - Mexico 66 Slip-On
   - Guia Mexico 66 como fonte principal de comparação.

### P1 — próximo lote

1. Blocos citáveis e metas mais descritivas para:
   - Sabot
   - Metallic Series
   - Slip-On
   - Fringe
2. Revisar schema/FAQ dos subclusters.

### Decisão pendente

- Criar ou não uma collection canônica `onitsuka-tiger-mexico-66-sd`.
- Recomendação: **não criar agora**. Manter SD como parte do hub/guia até GSC mostrar demanda suficiente, porque o volume explícito ainda é menor, apesar da tendência forte.

## Risco

Baixo, se publicado como bloco editorial e source map.
Risco principal: over-fragmentation de Onitsuka se criarmos páginas finas demais para SD/Slip-On/Metallic sem conteúdo/produtos suficientes.

## Approval packet

Arquivo preparado:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/approval-packets/20260618T145226Z-ai-visibility-v2-onitsuka-tiger-approval-packet.md`
