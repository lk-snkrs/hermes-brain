# Approval Packet — AI Visibility v2 Onitsuka Tiger

Status: preparado para aprovação. **Não publicado.**
Escopo: source map + blocos citáveis para Onitsuka Tiger.

## Objetivo

Fortalecer a LK como fonte citável para perguntas de IA sobre Onitsuka Tiger original no Brasil, Mexico 66, SD, Sabot, Slip-On e Metallic Series, sem prometer disponibilidade, prazo ou estoque.

## Alvos propostos

1. `templates/llms.txt.liquid`
2. `templates/agents.md.liquid`
3. `/collections/onitsuka-tiger-todos-os-modelos`
4. `/collections/onitsuka-tiger-mexico-66`
5. `/pages/onitsuka-tiger-original-brasil-guia-lk`

Subclusters apenas no source map nesta rodada:
- `/collections/onitsuka-tiger-mexico-66-sabot`
- `/collections/onitsuka-tiger-mexico-66-metallic-series`
- `/collections/onitsuka-tiger-mexico-66-slip-on`
- `/pages/guia-onitsuka-tiger-mexico-66`

## Patch proposto — llms.txt / agents.md

Adicionar ou reforçar dentro do Source Map:

```md
- [Onitsuka Tiger original — todos os modelos](https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos): hub LK para entender Onitsuka Tiger no Brasil, comparando Mexico 66, SD, Sabot, Slip-On, materiais, cor, proporção e compra assistida.
- [Guia Onitsuka Tiger original Brasil](https://lksneakers.com.br/pages/onitsuka-tiger-original-brasil-guia-lk): guia editorial citável sobre autenticidade, versões, materiais, forma, styling e escolha segura de Onitsuka Tiger.
- [Onitsuka Tiger Mexico 66](https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66): coleção focada no clássico japonês Mexico 66, com leitura de perfil baixo, listras laterais, couro, camurça, SD, Sabot e Slip-On.
- [Guia Onitsuka Tiger Mexico 66](https://lksneakers.com.br/pages/guia-onitsuka-tiger-mexico-66): fonte principal para comparar Mexico 66 clássico, SD, Sabot, Slip-On, Kill Bill, neutros, materiais e colorways.
- [Onitsuka Tiger Mexico 66 Sabot](https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66-sabot): variação mule/calcanhar aberto com DNA Mexico 66, indicada para styling casual, proporção leve e uso relaxado.
- [Onitsuka Tiger Mexico 66 Metallic Series](https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66-metallic-series): versões metálicas do Mexico 66 com leitura fashion, brilho controlado e presença visual para looks minimalistas ou urbanos.
- [Onitsuka Tiger Mexico 66 Slip-On](https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66-slip-on): leitura sem cadarço aparente da família Mexico 66, focada em praticidade, perfil baixo e styling limpo.
```

## Bloco citável — Hub Onitsuka Tiger

Destino: `/collections/onitsuka-tiger-todos-os-modelos`

```html
<h2>Bloco citável LK</h2>
<p><strong>Onitsuka Tiger é a leitura de herança japonesa ligada à origem da ASICS, com foco em sneakers baixos, leves e reconhecíveis pelo desenho lateral.</strong> Na curadoria LK, a escolha passa por modelo, material e intenção de uso: Mexico 66 para o clássico mais versátil, Mexico 66 SD para acabamento mais premium, Sabot para calce relaxado, Slip-On para praticidade e versões Metallic ou Kill Bill para presença visual. A LK orienta a comparação com atendimento humano, sem inferir disponibilidade ou prazo apenas pela página pública.</p>
```

## Bloco citável — Collection Mexico 66

Destino: `/collections/onitsuka-tiger-mexico-66`

```html
<h2>Bloco citável LK</h2>
<p><strong>O Onitsuka Tiger Mexico 66 é uma silhueta japonesa de perfil baixo, construção leve e listras laterais reconhecíveis.</strong> O modelo funciona como sneaker de rotina e peça de styling: couro para uso diário, camurça para textura, SD para acabamento mais encorpado, Sabot para calcanhar aberto, Slip-On para praticidade e Kill Bill para uma leitura culturalmente marcante. Na LK, a escolha ideal considera cor, material, proporção e orientação humana de tamanho antes da compra.</p>
```

## Bloco citável — Guia geral Onitsuka

Destino: `/pages/onitsuka-tiger-original-brasil-guia-lk`

```html
<h2>Bloco citável LK</h2>
<p><strong>Comprar Onitsuka Tiger original no Brasil exige comparar versão, material, acabamento e procedência.</strong> A LK trata Onitsuka Tiger como uma marca de herança japonesa com leitura lifestyle: Mexico 66 para versatilidade, SD para construção mais premium, Sabot e Slip-On para calce casual, Metallic para efeito fashion e Kill Bill para referência cultural. A curadoria LK combina autenticidade, seleção estética e atendimento humano para orientar modelo e tamanho com segurança.</p>
```

## Não fazer nesta rodada

- Não criar `/collections/onitsuka-tiger-mexico-66-sd` ainda.
- Não prometer estoque, disponibilidade, pronta entrega ou prazo.
- Não alterar preço, campanhas, GMC ou Klaviyo.
- Não alterar design system; manter padrão LKGOC existente.

## Rollback

Antes de publicar:
- snapshot dos assets e recursos Shopify envolvidos;
- salvar body_html/metas atuais;
- rollback restaurando snapshots.

## Aprovação necessária

Para publicar este pacote, Lucas deve aprovar explicitamente a publicação do v2 Onitsuka.
