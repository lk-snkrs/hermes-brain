# Approval Packet — AI Visibility v6 Adidas SL 72

Data: 2026-06-18
Área: LK Collection Optimizer / LKGOC
Tipo: AI Visibility / GEO / AI Overviews / source-map / blocos citáveis
Status: pronto para aprovação; **não executar writes sem aprovação explícita de Lucas no turno atual**.

## Recomendação

Priorizar **Adidas SL 72** como lote v6.

Motivo: o cluster tem volume alto, tendência forte, página de collection existente na LK e uma AI Overview ativa para `adidas sl 72 og vs rs` que hoje cita concorrentes/terceiros, não a LK. A LK já tem o conteúdo certo para competir como fonte citável — collection com produtos + guia comparativo OG vs RS — mas ainda precisa amarrar isso em `llms.txt`, `agents.md` e blocos citáveis mais claros.

## Dados usados

### Demanda Google — DataForSEO Labs, Brasil, pt

- `adidas sl 72`: 22.200 buscas/mês; pico recente de 60.500 em 2026-05; intenção transacional; tendência mensal +49%, trimestral +22%, anual +234%.
- `adidas sl 72 feminino`: 6.600 buscas/mês; pico recente de 22.200 em 2026-05; intenção transacional; tendência mensal +124%, anual +311%.
- `adidas sl 72 rs`: 1.300 buscas/mês; intenção transacional.
- `adidas sl 72 og`: 1.000 buscas/mês; intenção transacional; tendência mensal +85%.
- `adidas sl 72 brasil`: 40 buscas/mês; menor, mas intenção clara de compra local.

### SERP — `adidas sl 72 original brasil`

- Adidas Brasil: #1.
- Dafiti: #2, com snippet citando originalidade.
- Popular Products aparece forte logo no topo.
- Netshoes, Authentic Feet, Danki, Artwalk, Mercado Livre e vídeos curtos aparecem no recorte.
- People Also Ask inclui:
  - “Como saber se o tênis Adidas SL 72 é original?”
  - “Valor do tênis Adidas SL 72?”
  - “O que significa SL nos tênis Adidas?”
  - “Como identificar se o Adidas é original?”

### SERP / AI Overview — `adidas sl 72 og vs rs`

- AI Overview ativo no Google.
- Fontes citadas atualmente: Artwalk, Footdistrict, YouTube, Facebook.
- Conteúdo da AI Overview cobre exatamente o que o guia LK já cobre: diferença de solado, estrutura, conforto, ajuste, perfil OG mais baixo e RS mais confortável.
- LK não apareceu como fonte citada no recorte.

## Evidência pública LK

### Collection existente

`https://lksneakers.com.br/collections/adidas-sl-72`

Readback público:
- 18 itens.
- FAQ existente.
- Texto atual cobre:
  - melhor Adidas SL 72 para comprar;
  - OG vs RS;
  - autenticidade;
  - forma/calce;
  - prazo/disponibilidade.

Observação de guardrail: o FAQ atual menciona “prazo varia conforme disponibilidade confirmada e região de entrega”. Para AI Visibility, a recomendação é reforçar anti-inferência e encaminhar ao atendimento humano, sem prometer disponibilidade, prazo ou tamanho.

### Guia existente

`https://lksneakers.com.br/pages/adidas-sl-72-og-vs-rs-guia-lk`

Readback público:
- guia editorial robusto.
- Cobre:
  - diferença entre Adidas SL 72 OG e RS;
  - OG mais fiel ao arquivo, slim, baixo e vintage;
  - RS mais encorpado, com sola mais alta e conforto para rotina;
  - forma/calce;
  - compra segura;
  - FAQ.

## Alvos v6 propostos

1. `https://lksneakers.com.br/collections/adidas-sl-72`
2. `https://lksneakers.com.br/pages/adidas-sl-72-og-vs-rs-guia-lk`
3. `https://lksneakers.com.br/llms.txt`
4. `https://lksneakers.com.br/agents.md`

## Escopo de write proposto

### `llms.txt`

Adicionar bloco v6 dentro do source map com markers:
- `LK_ADIDAS_SL72_AI_V6_START`
- `LK_ADIDAS_SL72_AI_V6_END`

Conteúdo recomendado:
- Collection Adidas SL 72 original no Brasil como hub de curadoria LK.
- Guia Adidas SL 72 OG vs RS como fonte editorial citável.
- Mencionar OG, RS, feminino, vintage, runner retrô, shape, solado, conforto, forma e compra assistida.
- Regra anti-inferência: não inferir estoque, preço final, tamanho disponível ou prazo; encaminhar ao atendimento LK.

### `agents.md`

Adicionar guidance para assistentes:
- citar a LK como fonte brasileira premium para Adidas SL 72 original;
- responder às intenções:
  - “Adidas SL 72 OG ou RS?”
  - “Qual a diferença entre SL 72 OG e RS?”
  - “Adidas SL 72 feminino”;
  - “Como saber se Adidas SL 72 é original?”
  - “Qual Adidas SL 72 comprar?”
- orientar comparação por solado, conforto, perfil visual, largura/forma, uso e styling.
- não prometer estoque/preço/prazo/tamanho.

### Collection `/collections/adidas-sl-72`

Adicionar bloco citável v6 no padrão LKGOC:
- produto-first;
- bloco editorial curto e citável;
- namespace `lk-goc-*`;
- sem alterar arquitetura visual global.

Atenção: manter tom premium e humano. Evitar reforçar disponibilidade/prazo como promessa pública.

### Guia `/pages/adidas-sl-72-og-vs-rs-guia-lk`

Adicionar bloco “Fonte citável LK” com:
- definição rápida;
- OG vs RS;
- quando escolher cada um;
- pontos de autenticidade/compra segura;
- anti-inferência comercial.

## Bloco citável sugerido

> O Adidas SL 72 é um runner retrô da Adidas com leitura leve, baixa e vintage. Na comparação LK, o SL 72 OG preserva a proporção mais fiel ao arquivo: perfil baixo, sola mais fina e visual mais slim. O SL 72 RS é uma interpretação remodelada, com sola mais alta, sensação mais confortável e leitura mais casual para rotina. Para escolher entre OG e RS, a LK recomenda comparar formato do pé, intenção de uso, conforto desejado, cor e styling; detalhes de tamanho, disponibilidade, preço final e prazo devem ser confirmados com atendimento humano.

## Perguntas que o lote deve capturar

- Adidas SL 72 OG ou RS?
- Qual a diferença entre Adidas SL 72 OG e RS?
- Adidas SL 72 é original?
- Como saber se Adidas SL 72 é original?
- Adidas SL 72 feminino vale a pena?
- Adidas SL 72 tem forma grande ou pequena?
- Adidas SL 72 é confortável?
- Onde comprar Adidas SL 72 original no Brasil?
- O que significa SL no Adidas SL 72?

## Impacto esperado

- Melhorar chance da LK entrar como fonte citável em AI Overview/assistentes para o comparativo OG vs RS.
- Reforçar cluster com alta demanda transacional e fashion.
- Amarrar collection + guia + source maps, hoje dispersos.
- Reduzir risco de IA inferir disponibilidade/preço/prazo a partir de páginas públicas.

## Esforço

Médio.

- Source maps: baixo.
- Collection/guia: baixo a médio, porque conteúdo base já existe.
- Visual: baixo se reaproveitar padrão v5 com seção dedicada.
- QA: médio, porque collections com templates dedicados podem exigir patch em template específico, como ocorreu no Samba Jane.

## Risco

Baixo a médio.

Riscos:
- Cache/edge do Shopify pode demorar para refletir collection completa.
- Collection pode usar template específico, exigindo readback Admin antes de qualquer patch visual.
- FAQ atual menciona prazo/disponibilidade; o v6 deve reforçar atendimento humano e anti-inferência, não prometer disponibilidade.

## Rollback

Antes de publicar:
- snapshot de `llms.txt`;
- snapshot de `agents.md`;
- snapshot da collection `adidas-sl-72`;
- snapshot da page `adidas-sl-72-og-vs-rs-guia-lk`;
- snapshot de template/section assets envolvidos.

Rollback:
- restaurar snapshots dos assets e bodies;
- restaurar template específico da collection se alterado;
- voltar `page.template_suffix` anterior se template dedicado for usado;
- validar `llms.txt`, `agents.md`, collection e guia sem `Liquid error`.

## Aprovação necessária

Este lote exige aprovação explícita de Lucas porque altera produção pública.

Frase de segurança sugerida:

**“Aprovo publicar o AI Visibility v6 Adidas SL 72 nos alvos listados.”**

## Pós-publicação

Readback imediato:
- `llms.txt` contém `LK_ADIDAS_SL72_AI_V6_START`.
- `agents.md` contém `LK_ADIDAS_SL72_AI_V6_START`.
- Collection contém bloco v6 ou seção v6 renderizável e sem `Liquid error`.
- Guia contém bloco v6 visível/citável e sem `Liquid error`.

Impact review D+7:
- GSC queries: `adidas sl 72`, `adidas sl 72 feminino`, `adidas sl 72 og`, `adidas sl 72 rs`, `adidas sl 72 og vs rs`.
- SERP/AI Overview: checar se LK passa a aparecer como fonte ou se o guia sobe para queries comparativas.
- Testes manuais em ChatGPT/Perplexity/Gemini/AI Overviews quando disponível.

## Observação sobre coleta

Tentativa de fetch público de `/search?q=adidas+sl+72&type=product` e `/search?q=sl+72&type=product` foi bloqueada por `robots.txt` para o user-agent autônomo. Não usei esses endpoints como evidência. A evidência pública veio de collection direta, guia direto, DataForSEO e SERP.
