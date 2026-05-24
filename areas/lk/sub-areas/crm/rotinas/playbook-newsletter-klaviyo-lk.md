# Playbook — Newsletter Klaviyo LK

Status: v0.1 consolidado para produção de newsletters LK.
Escopo: brief, copy, design, preview, rascunho Klaviyo, aprovação e pós-envio.
Guardrail: não enviar, agendar ou publicar sem aprovação explícita no fluxo vigente.

## Fontes obrigatórias

1. `areas/lk/design/DESIGN.md` — sistema visual LK.
2. `areas/lk/design/klaviyo-visual-audit.md` — auditoria dos e-mails reais usados como referência.
3. `areas/lk/sub-areas/crm/rotinas/playbook-campanha-crm-aprovada.md` — fluxo de CRM/campanha com aprovação.
4. `areas/lk/sub-areas/crm/rotinas/klaviyo-p1-draft-campaign-2026-05-11.md` — exemplo técnico de rascunho Klaviyo.
5. Fonte viva quando houver produto/catálogo: Shopify, GA4, GSC, Klaviyo e/ou contexto comercial aprovado.

## Direção visual LK

A newsletter deve parecer uma peça editorial de curadoria, não um disparo promocional genérico.

- Conceito: `Less Noise, More Identity`.
- Produto como protagonista cromático; interface neutra.
- Fundo branco/off-white quente, divisórias sutis.
- Header preto com logo branco centralizado.
- Barra de contexto/microcopy uppercase com letter-spacing alto.
- Títulos com serifa editorial: `Cormorant Garamond, Georgia, serif`.
- Corpo/UI com `DM Sans, Arial, sans-serif`.
- CTAs pretos, pequenos, firmes, sem radius evidente.
- Cards sem sombra forte, sem gradiente e sem aparência marketplace.
- Footer preto com slogan: `O que é raro, merece ser encontrado`.
- O slogan deve aparecer no footer, não no header.

## Paleta base

- Preto institucional: `#0A0A0A`.
- Grafite: `#1A1A1A`.
- Paper quente: `#F0ECE8`.
- Paper soft: `#F5F4F2`.
- Branco/surface: `#FFFFFF`.
- Linha clara: `#E8E6E2`.
- Muted: `#8A8580`.
- Bege/acento: `#C8A98A`, `#D4B896`, `#E8D8C4`.

## Estrutura recomendada

1. Header preto com logo LK branco.
2. Context bar: coleção, curadoria ou ocasião.
3. Hero editorial:
   - eyebrow uppercase;
   - título serifado;
   - subtítulo ou frase em itálico/acento;
   - texto curto explicando por que o produto importa.
4. Produto hero ou grid de produtos.
5. Bloco de prova/curadoria:
   - autenticidade;
   - atendimento humano;
   - loja física Jardins quando fizer sentido;
   - troca/frete/parcelamento somente se confirmado.
6. CTA principal preto.
7. CTA secundário textual para explorar coleção ou falar no chat, quando aplicável.
8. Footer preto com slogan.

## Copy e tom

Usar linguagem premium, humana e comercialmente inteligente.

Preferir:

- curadoria;
- intenção;
- originalidade;
- autenticidade;
- raro;
- selecionado;
- mais escolhido;
- explorar;
- ver modelo;
- atendimento humano;
- confirmar no chat.

Evitar:

- megadesconto, imperdível, corre, últimas unidades como pressão agressiva;
- excesso de exclamações;
- linguagem marketplace;
- prometer disponibilidade, prazo, preço ou estoque sem fonte viva/confirmada;
- taxonomias internas como `pronta entrega`, `encomenda` ou `estoque` como narrativa principal pública.

## Checklist antes de montar a peça

- [ ] Produto/coleção definido.
- [ ] Objetivo claro: venda, lançamento, curadoria, reativação, conteúdo ou tráfego.
- [ ] Público/lista/segmento definido.
- [ ] Fonte de dados registrada.
- [ ] Produtos, preços, imagens e links confirmados em fonte viva.
- [ ] Riscos comerciais marcados: estoque, prazo, preço, cupom, segmentação.
- [ ] Métrica de sucesso definida: clique, receita, conversão, resposta, compra ou aprendizado.

## Preview obrigatório

Antes de qualquer Klaviyo write ou envio, gerar um pacote de preview:

```text
Newsletter proposta: ...
Produto/coleção: ...
Objetivo: ...
Segmento/lista: ...
Assunto: ...
Preview text: ...
Hero copy: ...
CTA principal: ...
Links: ...
Imagens/fonte: ...
Risco/ressalva: ...
Métrica de sucesso: ...
Aprovação necessária: revisar / ajustar / aprovar rascunho / aprovar envio
```

Para layout, usar HTML visual ou preview renderizado. Markdown sozinho não aprova direção estética.

## Klaviyo

Fluxo seguro:

1. Criar HTML/customer-facing sem jargão interno.
2. Validar em browser/mobile.
3. Criar ou atualizar template/rascunho Klaviyo somente se autorizado para esta etapa.
4. Manter campanha em `Draft`.
5. Não enviar, não agendar, não ativar flow e não mexer em lista real sem aprovação explícita.
6. Registrar IDs técnicos e nomes, mas não inventar deep link do painel Klaviyo sem testar logado.
7. Antes do envio: confirmar lista, assunto, sender, preview, links, imagens, status `Draft`, `scheduled_at=None`, `send_time=None`.

## Pós-envio

Registrar no Brain:

- data/hora;
- campanha/lista/segmento;
- assunto e preview text;
- link/ID verificado;
- receita, cliques, CTR, conversão, unsub/spam quando disponíveis;
- aprendizados de copy/design/produto;
- próximo teste recomendado.

## Exemplo — Samba Jane

Para uma newsletter do `Adidas Samba Jane`, a lógica esperada é:

- Ângulo: ballerina sneaker / Samba com leitura feminina e curatorial.
- Narrativa: por que a Jane importa agora, como usar, por que a LK selecionou.
- Visual: produto grande, respiro, fundo claro quente, CTA preto.
- CTA: `VER SAMBA JANE` ou `EXPLORAR A CURADORIA`.
- Secundário: `FALAR COM A LK` se for necessário atendimento humano.
- Evitar prometer disponibilidade/tamanho sem checagem viva por variante.
