# Approval packet — Crocs Relâmpago McQueen collection schema/FAQ lite

- Criado UTC: 2026-06-22T17:21:57.363778+00:00
- Modo: read-only packet; writes externos até aqui: 0; values_printed=false.
- Objetivo: melhorar citabilidade/schema da collection `/collections/crocs-relampago-mcqueen` sem mexer no PDP Crocs McQueen já trabalhado.

## Anti-retrabalho

- PDP já trabalhado em Package A: `/products/crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho`.
- Este packet **não altera o PDP**.
- A collection `/collections/crocs-relampago-mcqueen` não aparece como trabalhada em Package A/B; tem updatedAt `2026-06-19T15:42:18Z`, mas descrição curta e sem FAQ/schema.
- Por catálogo raso: `productsCount=1`, usar abordagem lite/defensiva, sem prometer disponibilidade.

## Evidência pública da collection

- HTTP 200.
- Canonical: `https://lksneakers.com.br/collections/crocs-relampago-mcqueen`.
- H1: `Crocs Relâmpago McQueen`.
- `CollectionPage=1`.
- `BreadcrumbList=1`.
- `FAQPage=0`.
- `Liquid error=false`.
- Description admin: `210` caracteres; sem FAQ.

## Demanda

GSC 28d recente:
- `crocs relampago mcqueen`: 18.267 impressões, 41 cliques, CTR 0,22%, posição 8,76.
- `crocs mcqueen`: 18.025 impressões, 42 cliques, CTR 0,23%, posição 8,87.
- `crocs do relâmpago mcqueen`: 13.341 impressões, 23 cliques, CTR 0,17%, posição 6,88.

DataForSEO Brasil/pt:
- `crocs mcqueen`: SV 49.500/mês; intenção transacional.
- `crocs relampago mcqueen`: SV 33.100/mês; maio 40.500; tendência mensal +49%; intenção transacional.
- `crocs do relâmpago mcqueen`: SV 14.800/mês; YoY +124%; intenção transacional.

## Proposta de escopo

Aplicar apenas na **collection**:

1. Intro curta citável.
2. FAQ lite com 3–4 perguntas.
3. FAQPage JSON-LD único, se o tema não gerar automaticamente.
4. Não alterar preço, estoque, disponibilidade, PDP, tema global, GMC ou ads.

## Draft de copy segura

### Intro

`Crocs Relâmpago McQueen reúne a leitura colecionável do Classic Clog inspirado em Lightning McQueen, com visual vermelho, detalhes gráficos e apelo forte para fãs de Cars e cultura sneaker. Na LK, a curadoria prioriza originalidade, atendimento humano e orientação para escolher tamanho e detalhes do modelo antes da compra.`

### FAQ sugerido

1. **O Crocs Relâmpago McQueen é original na LK?**  
   Sim. A LK trabalha com curadoria de produtos originais e atendimento humano para orientar detalhes do modelo.

2. **Qual é o modelo do Crocs Relâmpago McQueen?**  
   A versão mais buscada é o Crocs Classic Clog inspirado em Lightning McQueen, com estética vermelha e elementos gráficos da personagem.

3. **Como escolher o tamanho do Crocs Relâmpago McQueen?**  
   A escolha deve considerar a forma do Classic Clog e a preferência de ajuste. A equipe LK pode orientar a melhor numeração antes da decisão.

4. **Por que o Crocs McQueen é tão procurado?**  
   O modelo combina nostalgia, colaboração licenciada, visual reconhecível e perfil colecionável, por isso costuma concentrar alta demanda.

## Impacto esperado

- Melhorar parsing de Google/LLM para a collection.
- Capturar intenção transacional sem retrabalhar o PDP.
- Evitar promessas públicas de disponibilidade.

## Risco

- Médio por catálogo raso: collection tem 1 produto. O copy precisa ser factual e não inflar variedade.
- Baixo técnico se limitado a collection description + schema escopado.

## Rollback

- Backup de `descriptionHtml` + SEO antes do write.
- Restaurar collection via Admin API se necessário.
- QA público: HTTP 200, H1=1, FAQPage=1, sem termos proibidos.

## Aprovação necessária

Write em Shopify production collection exige aprovação explícita.

Frase segura:

> aprovado Crocs McQueen collection FAQ lite
