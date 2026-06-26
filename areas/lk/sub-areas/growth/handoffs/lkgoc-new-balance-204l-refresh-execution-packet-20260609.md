# Handoff — LKGOC New Balance 204L refresh — execução item 3 — 2026-06-09

Status: **handoff local / preview-only / sem write externo**  
Criado em: 2026-06-09 14:15 UTC  
Origem: LK Growth  
Destino: **[LK] Otimização de Coleção**

## URL

`https://lksneakers.com.br/collections/new-balance-204l`

## Evidência verificada

- GSC atual: **11.078 impressões / 59 cliques / CTR 0,53% / posição 9,3** em queries posição 4–15.
- Query principal `new balance 204l` caiu:
  - antes: **91 cliques / 18.427 impressões / CTR 0,49% / posição 8,0**;
  - atual: **18 cliques / 7.318 impressões / CTR 0,25% / posição 10,3**;
  - delta: **-73 cliques / -11.109 impressões / piora +2,3 posições**.
- GA4 orgânico: **231 sessões / engagement 71,0%**.
- URL Inspection: indexada, canonical OK, mobile crawl OK.
- Fetch público: collection já contém guia editorial, FAQ e orientação humana.
- DataForSEO `new balance 204l`: volume Brasil **9.900**, intenção **transactional**, competição paid **high**; pico recente em 2026-03/04 acima de **40k** buscas/mês.
- DataForSEO `new balance 204l brasil`: volume **320**, intenção principal **informational** com componente transactional.
- SERP mobile: New Balance oficial domina top orgânico e popular products; SERP mistura PDPs oficiais, imagens, vídeos curtos e blog editorial. People also search inclui `new balance 204l brasil`, `feminino`, `branco`, `sea salt`, `é confortável`, `marrom`, `masculino`, `cinza`, `off white`.

## Hipótese

A queda pode ter componente de ciclo de lançamento, mas há oportunidade de refresh porque:

- a query ainda tem volume alto;
- a página da LK está indexada e tecnicamente saudável;
- SERP exige tanto produto quanto orientação editorial;
- os modifiers de busca indicam dúvidas de cor, gênero, conforto, Brasil e variações.

## Brief para o owner LKGOC

Preparar preview dev-first sem reinventar o padrão 204L aprovado:

1. Refresh de bloco citável com foco em `New Balance 204L original no Brasil`.
2. FAQ por dúvidas reais:
   - O que é New Balance 204L?
   - New Balance 204L é confortável?
   - Qual cor escolher: Sea Salt, Mushroom, Timberwolf, Silver Metallic, Black Magnet?
   - New Balance 204L é feminino, masculino ou unissex?
   - Como comparar tamanho com outros New Balance?
3. Módulo de orientação de colorways baseado em intenção de uso, sem prometer disponibilidade.
4. Revalidar se a coleção e/ou guia devem ser reforçados em `llms.txt`/`agents.md` — `agents.md` já contém 204L; `llms.txt` precisa revisão de cobertura.
5. D+7/D+14 impact review após qualquer produção aprovada.

## Métrica esperada

- CTR query principal sair de **0,25%** para alvo inicial **>0,50%**.
- Posição média voltar para faixa **<8**.
- Recuperar cliques/impressões orgânicos da collection.
- Separar efeito de sazonalidade vs melhoria de snippet/landing.

## Risco e rollback

- Risco: médio; página já tem padrão LKGOC, então o maior risco é mexer demais em estrutura aprovada.
- Regra: manter padrão visual/estrutura, ajustar conteúdo por evidência.
- Rollback: snapshot de collection/source/theme/SEO/FAQ/schema.
- Produção só com aprovação explícita de Lucas após preview.

## Approval surface

> Lucas, aprova [LK] Otimização de Coleção preparar preview dev-first de refresh New Balance 204L, mantendo o padrão aprovado e sem produção?
