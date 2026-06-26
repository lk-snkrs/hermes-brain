# LK Growth OS — Bloco 3 Brain Doc: Autenticidade Hub e decisões GEO

Data: 2026-05-22 19:45 UTC
Status: documentação Brain local concluída; sem writes externos adicionais nesta etapa.

## Estado atual

A página `https://lksneakers.com.br/pages/autenticidade` está live com layout hub longo, premium e visualmente aprovado por Lucas.

Elementos validados em produção:
- H1 editorial: `Tênis original começa antes da compra.`
- H2s de processo, compra segura, páginas-fonte e FAQ.
- Cards/pilares de autenticação.
- Links para guias relacionados.
- JSON-LD detectado no DOM: `Organization`, `WebPage`, `FAQPage`.
- Layout visual aprovado pelo usuário como `MUITO bom`.

## Decisões tomadas

### 1. Hub de Autenticidade é ativo canônico de GEO

A página deve ser tratada como página central para:
- autenticidade LK;
- compra segura de sneakers originais no Brasil;
- links para guias específicos de modelos e marcas;
- reforço de entity mapping no futuro `llms.txt`.

### 2. O próximo gargalo não é layout; é fonte específica por intenção

O gap competitivo principal não é mais criar uma página bonita. É criar páginas que respondam intenções específicas:
- Air Jordan Travis Scott original;
- New Balance 204L original;
- Adidas SL 72 OG vs RS;
- Onitsuka Tiger Mexico 66 original;
- Yeezy original;
- Lululemon original/importado.

### 3. Linguagem de negócio correta

Correção durável de Lucas:
- LK é `boutique premium` ou `loja especializada`.
- `Curadoria` não deve definir tecnicamente o modelo de negócio.
- Pode aparecer apenas como ideia de seleção/olhar especializado, quando não substitui a definição da loja.
- LK não deve ser posicionada como marketplace, operação de legit-check ou loja que precisa provar autenticidade por vídeo.
- Originalidade/autenticidade é premissa, não tema central da narrativa comercial.
- Concorrentes principais para análise futura: Juicy Sneakers, Hype Concept e PalmTree48.
- Droper é marketplace e não concorrente direto de boutique; Vox não existe mais; 90sneakers não é referência conhecida.

### 4. Guardrail público de disponibilidade

Manter regra já existente:
- não transformar `estoque`, `pronta entrega` ou `encomenda` em taxonomia pública;
- disponibilidade/prazo ficam no atendimento/chat quando necessário;
- copy deve falar em autenticidade, seleção, atendimento humano e confirmação de detalhes.

## Issue aberto encontrado no Bloco 2

Apesar da intenção de corrigir a terminologia, inspeção DOM live encontrou:
- `curadoria_count`: 11
- `boutique_count`: 0 no texto visível
- `FAQPage`: presente
- `Organization.description`: já usa `Sneaker boutique premium em Sao Paulo`

Isso significa que o schema está alinhado, mas o conteúdo visível ainda precisa de micro-hotfix.

Micro-hotfix proposto, pendente de aprovação atual:
- `A LK Sneakers é uma curadoria...` → `A LK Sneakers é uma boutique premium...`
- `entrar na curadoria` → `entrar na seleção LK`
- `Curadoria é confiança antes de ser compra.` → `Autenticidade é confiança antes da compra.`
- revisar usos contextuais de `curadoria humana` para `seleção humana` / `atendimento humano`.

## Relatórios relacionados

- Baseline anterior: `areas/lk/sub-areas/growth/reports/2026-05-22-geo-ai-search-baseline-p1.md`
- Bloco 2 gap analysis: `areas/lk/sub-areas/growth/reports/2026-05-22-geo-bloco2-gap-analysis-authenticidade.md`

## Próxima fila recomendada

1. Aprovação do micro-hotfix de terminologia na página Autenticidade.
2. Draft do guia `Air Jordan Travis Scott original no Brasil`.
3. Draft do guia `New Balance 204L original no Brasil`.
4. Outline do comparativo `Adidas SL 72 OG vs RS`.
5. Depois dos guias live: atualizar `llms.txt` e rodar D+7 AI Search/GSC review.

## Approval boundaries

Sem aprovação:
- briefs;
- drafts locais;
- relatórios Brain;
- schema proposal;
- gap analysis;
- outlines.

Com aprovação explícita atual:
- editar página Shopify production;
- publicar novo guia/page/blog;
- alterar `llms.txt` público;
- alterar theme production;
- mexer em campanhas, Klaviyo, Merchant Center ou qualquer canal externo.
