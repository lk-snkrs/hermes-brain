# LKGOC Contract Lock — Puma Speedcat

Status: `BLOCKED`
Data: 20260606T165533Z
Responsável: LK Collection Optimizer / LKGOC
Handle: `puma-speedcat`
Ambiente alvo se aprovado: DEV Shopify theme `155065450718` / role `unpublished`

## Decisão executiva

**Não aprovado para DEV write ainda.**

Motivo: falta asset hero lifestyle/on-foot com direito de uso confirmado. Pela regra LKGOC atual, Puma Speedcat não pode ser reconstruída em Shopify usando packshot, PDP, produto isolado ou imagem externa sem licença/autoridade de uso.

## 1. Gold source coleção

- URL/snapshot aprovado: `https://lksneakers.com.br/collections/new-balance-204l`
- Padrão visual esperado: LKGOC/204L, full-width, premium, produto-first, grid antes do guia, guia pós-grid, FAQ em 2 colunas.
- Elementos imutáveis:
  - [x] hero/header escuro no padrão
  - [x] produto-first
  - [x] grid antes do guia
  - [x] guia pós-grid no padrão
  - [x] FAQ/schema único
  - [x] comportamento mobile preservado

## 2. Gold source guia dedicado

- Shell editorial aprovado: padrão premium tipo Moon Shoe/Jacquemus/Nike Mind já referenciado no Brain.
- O guia NÃO pode ser:
  - [x] article simples
  - [x] texto corrido
  - [x] markdown/html cru
  - [x] bloco curto genérico

## 3. Media manifest

### Hero image 1
- URL/fonte: pendente — asset próprio LK, campanha oficial autorizada ou fornecedor com direito de uso.
- Licença/status de uso: `não confirmado`
- Mostra pessoa usando/contexto editorial? `pendente`
- Produto visível? `pendente`
- Não é packshot/PDP/produto isolado? `pendente`
- Decisão: `bloqueada`

### Referências editoriais — não usar como asset final sem aprovação/licença
- Vogue US: referência de posicionamento/street style; imagem apenas como inspiração.
- Vogue Brasil/Globo: referência de tendência/street style; imagem apenas como inspiração.
- Overkill: referência histórica/motorsport; imagem apenas como inspiração.

## 4. Guide pattern manifest

Estrutura prevista para build quando asset for aprovado:

1. Hero full-width lifestyle: pessoa usando Speedcat / street style / motorsport-fashion.
2. Tese LK: perfil baixo, motorsport, camurça/couro, proporção slim.
3. Bloco citável GEO/AI.
4. Referências editoriais: Vogue US, Vogue Brasil, Overkill — texto, não imagens roubadas.
5. Como usar: jeans amplo, alfaiataria relaxada, couro, capri/saia, visual urbano.
6. Cores/materiais: vermelho/preto/clássicos, camurça/couro.
7. Tamanho/ajuste: orientação para confirmar no atendimento humano quando necessário.
8. Seleção LK em grid.
9. FAQ 2 colunas desktop / 1 coluna mobile.
10. FAQPage schema único.

## 5. Acceptance tests pré-build

- [x] `contract_lock_exists`
- [x] `gold_source_collection_locked`
- [x] `gold_source_guide_locked`
- [ ] `hero_has_person_using_product`
- [ ] `hero_not_packshot`
- [x] `guide_matches_gold_source` — especificação travada, ainda sem render final
- [x] `grid_before_guide`
- [x] `faq_unique_schema` — planejado
- [ ] `desktop_mobile_screenshots_exist` — só local/mock permitido
- [ ] `visual_qa_passed` — só após asset aprovado
- [x] `rollback_ready` — DEV-only quando aprovado

## 6. Resultado do Gate

Status permitido: `APPROVED_FOR_DEV_WRITE` ou `BLOCKED`.

**Resultado atual: `BLOCKED`.**

## 7. Ação permitida agora

- Permitido: mock local não-publicado com placeholder claramente marcado como `ASSET PENDENTE`.
- Proibido: write em Shopify DEV/production, publicação, uso de imagem externa como hero sem licença.

## 8. O que preciso do Lucas para destravar

Enviar/aprovar 1 asset hero lifestyle/on-foot da Puma Speedcat com uma destas origens:

1. foto própria/produção LK;
2. asset oficial de campanha com direito de uso confirmado;
3. imagem de fornecedor/parceiro com autorização;
4. aprovação explícita para usar uma imagem externa específica, assumindo o risco/licença.
