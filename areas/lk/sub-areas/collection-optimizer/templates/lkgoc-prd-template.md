# PRD — LKGOC Zero-Base Superpowers v2

Data UTC: 20260606T180811Z
Owner: LK Collection Optimizer
Aprovador: Lucas Cimino
Status: **DRAFT — Aguardando respostas de Lucas**

## 1. Problema

O LKGOC falhou porque o processo aceitou entregas tecnicamente válidas, mas visualmente divergentes do padrão aprovado.

O erro não foi apenas da Puma Speedcat. Foi de sistema:

- o QA técnico substituiu o QA visual;
- o padrão New Balance 204L foi tratado como inspiração, não como contrato;
- não havia PRD obrigatório antes da execução;
- não havia gate de perguntas antes de rebuild;
- o veto da Skill Superpowers não estava conectado a um artefato de decisão claro;
- o PASS era possível sem side-by-side visual.

## 2. Objetivo

Refazer o LKGOC do zero como sistema operacional de coleção, usando a Skill Superpowers, com gates que impeçam novo erro.

O novo LKGOC deve produzir coleções que pareçam pertencer exatamente à mesma família visual do Gold Source 204L.

## 3. Gold Source inegociável

Gold Source visual: `https://lksneakers.com.br/collections/new-balance-204l`

O Gold Source é **contrato**, não inspiração.

Toda coleção LKGOC deve ser uma adaptação mínima do shell 204L:

- mesma hierarquia visual;
- mesmo peso editorial;
- mesma lógica hero → grid → guia;
- mesma densidade do guia;
- mesmo padrão de FAQ;
- mesma sofisticação premium/minimalista;
- sem layout novo sem aprovação explícita.

## 4. Escopo v2

### Inclui

- PRD obrigatório antes de qualquer rebuild.
- Perguntas obrigatórias respondidas por Lucas ou marcadas como default aprovado.
- Contract Lock por coleção.
- Media Manifest com fontes editoriais principais.
- DEV build apenas em tema `role: unpublished`.
- QA técnico + QA visual lado a lado 204L vs coleção.
- Worker/Superpowers veto documentado.
- Receipt com rollback e evidências.
- Approval packet separado para Production.

### Não inclui sem aprovação explícita

- Write em Production/main.
- Merge DEV → Production.
- Mudança de preço, estoque, desconto ou disponibilidade pública.
- Nova arquitetura visual fora do 204L.
- Novo design system.
- Envio externo/customer-facing.

## 5. Tema e arquitetura técnica

### DEV

Tema DEV atual: `155065450718` / `lk-new-theme/dev` / `role: unpublished`.

Antes de qualquer write:

- verificar via Shopify Admin API que `role == unpublished`;
- se `role == main`, abortar.

### Production

Tema Production atual conhecido: `155065417950` / `lk-new-theme/production` / `role: main`.

Regra: **Production é proibido sem aprovação explícita de Lucas.**

### Componente

Fonte única:

- `snippets/lk-goc-collection.liquid`

Permitido:

- branches por `collection.handle`, desde que sejam adaptação mínima do shell 204L.

Proibido:

- snippets paralelos por coleção;
- layout próprio por coleção;
- duplicação que gere drift visual;
- declarar PASS só por estar no componente único.

## 6. Fluxo obrigatório por coleção

### Gate -2 — PRD

Antes de qualquer rebuild:

- PRD aprovado ou confirmado por Lucas;
- perguntas respondidas;
- coleção alvo definida;
- Gold Source confirmado;
- critérios de aceitação congelados.

### Gate -1 — Contract Lock

Criar Contract Lock da coleção:

- handle;
- objetivo comercial;
- mídias candidatas;
- fontes editoriais;
- riscos;
- rollback;
- status DEV allowed / Production blocked.

### Gate 0 — Superpowers Workers

Acionar/verificar, mesmo que localmente, os papéis:

- Visual Fidelity Worker;
- Editorial/Merchandising Worker;
- Technical Shopify Worker;
- QA/Regression Worker;
- Approval/Rollback Worker.

Cada worker pode vetar PASS.

### Gate 1 — Gold Source Extraction

Extrair/confirmar shell 204L:

- screenshot 204L desktop/mobile;
- DOM/section markers;
- estrutura de hero;
- estrutura de guia;
- FAQ;
- ritmo visual.

### Gate 2 — Build DEV

Construir apenas no DEV/unpublished.

### Gate 3 — QA Técnico

- sem Liquid error;
- assets DEV carregando;
- grid preservado;
- guide após grid;
- FAQPage schema quando aplicável;
- mobile/desktop renderizados;
- readback Admin API.

### Gate 4 — QA Visual 204L

Obrigatório:

- screenshot 204L;
- screenshot coleção alvo;
- side-by-side desktop;
- side-by-side mobile;
- avaliação de equivalência visual.

Status possível:

- `PASS_204L_VISUAL_CONTRACT`
- `FAIL_VISUAL_CONTRACT_204L`

Sem esse gate, o QA final é inválido.

### Gate 5 — Receipt

Salvar:

- arquivos alterados;
- snapshots rollback;
- media manifest;
- screenshots;
- checks JSON;
- worker verdicts;
- Production guard.

### Gate 6 — Approval Packet

Somente se todos os gates passarem:

- impacto;
- risco;
- rollback;
- screenshots;
- preview;
- pedido claro de aprovação para merge.

## 7. Critérios de aceite finais

Uma coleção LKGOC só passa se:

- foi construída no DEV/unpublished;
- não tocou Production;
- usa o componente único;
- mantém o shell 204L;
- tem side-by-side aprovado;
- tem veto Superpowers resolvido;
- tem rollback;
- tem receipt;
- Lucas aprova antes de Production.

## 8. Critérios de reprovação automática

- QA técnico sem side-by-side visual.
- Build visualmente diferente do 204L.
- Hero editorial bonito, mas fora do shell.
- Guia simplificado.
- FAQ fora do padrão.
- Mudança estrutural não aprovada.
- Write em `role: main`.
- Falta de PRD/Contract Lock.
- Falta de respostas às perguntas bloqueantes.

## 9. Rollback padrão

Todo build deve salvar snapshots antes do write:

- `snippets/lk-goc-collection.liquid.before`
- `sections/lk-collection.liquid.before` se alterada
- qualquer asset adicional alterado

Rollback em DEV:

1. validar tema `role: unpublished`;
2. restaurar snapshots;
3. readback;
4. screenshot após rollback;
5. receipt.

Production rollback só existe se houve merge aprovado previamente.

## 10. Primeira execução após PRD

Recomendação: refazer **Puma Speedcat** do zero como piloto, porque ela é o caso de falha.

Mas só após Lucas responder as perguntas do briefing.
