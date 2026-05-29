# Padrão canônico — bloco guia pós-grid em coleções LK

Status: aprovado visualmente por Lucas em 2026-05-28.
Referência inicial: coleção `new-balance-204l`.
Screenshot aprovado: `/opt/data/profiles/lk-growth/image_cache/img_0be4cb12599f.jpg`.

## Uso

Este é o padrão visual preferencial para coleções product-first da LK que precisam de suporte editorial, FAQ e CTA para guia completo sem empurrar os produtos para baixo.

Aplicar especialmente em coleções de modelo, marca/collab ou curadoria com busca e dúvidas recorrentes.

## Estrutura visual aprovada

1. Produtos primeiro.
2. Depois do grid/listagem, inserir um bloco editorial com fundo off-white/claro e borda sutil.
3. Topo do bloco:
   - kicker pequeno em caixa alta: `GUIA EDITORIAL LK` ou equivalente aprovado;
   - H2 serifado grande, editorial e comercial;
   - parágrafo introdutório curto, objetivo e citável.
4. Card interno branco em duas colunas no desktop:
   - esquerda: `Como escolher...` com bullets/linhas de orientação comercial;
   - direita: `Perguntas frequentes` com accordion;
   - divisor vertical sutil entre colunas;
   - os títulos das duas colunas devem estar alinhados pela mesma linha superior.
5. Rodapé do bloco:
   - nota/helper clara à esquerda;
   - CTA preto à direita: `ABRIR GUIA COMPLETO` quando houver página de guia.

## Regras de layout desktop

- Container amplo, alinhado ao grid/ritmo da coleção.
- Card branco com padding generoso.
- Grid real de duas colunas; não apenas card alargado.
- FAQ deve começar na mesma altura do título da coluna esquerda.
- Separação do FAQ por `border-left`, não `border-top`, em desktop.
- Evitar qualquer faixa superior, margem ou padding que empurre o FAQ para baixo.

CSS de referência conceitual:

```css
@media (min-width: 990px) {
  .lk-guide-standard-card--wide {
    display: grid;
    grid-template-columns: minmax(380px, .88fr) minmax(520px, 1.12fr);
    grid-template-rows: auto 1fr;
    align-items: start;
  }

  .lk-guide-standard-card--wide > h3 {
    grid-column: 1 / 2;
    grid-row: 1;
    margin: 0;
  }

  .lk-guide-standard-card--wide > ul {
    grid-column: 1 / 2;
    grid-row: 2;
  }

  .lk-guide-standard-faq {
    grid-column: 2 / 3;
    grid-row: 1 / span 2;
    align-self: start;
    margin-top: 0;
    padding-top: 0;
    border-top: 0;
    border-left: 1px solid #e2dbd0;
  }

  .lk-guide-standard-faq h3 {
    margin: 0 0 12px;
  }
}
```

## Regras mobile

- Manter coleção product-first.
- Bloco deve comprimir bem: uma coluna, FAQ abaixo da orientação, espaçamento menor.
- Não deixar o guia dominar antes do produto.

## Copy e tom

- Premium, minimalista, humano e comercialmente útil.
- Evitar taxonomia operacional pública de estoque/encomenda/pronta entrega.
- Usar curadoria, autenticidade, orientação humana e compra segura como linguagem de confiança.
- O texto deve ajudar decisão de compra: cor, material, proporção, intenção de uso, autenticidade e atendimento.

## FAQ/schema

- Se o FAQ entra neste bloco, remover/desativar FAQ legado separado na mesma coleção para evitar duplicação visual e duplicação de schema.
- Gerar/atualizar `FAQPage` JSON-LD apenas uma vez por coleção.

## Verificação obrigatória

Antes de considerar aplicado:

- Browser desktop: títulos `Como escolher...` e `Perguntas frequentes` com diferença de topo `0px` ou visualmente indistinguível.
- Computed CSS do FAQ em desktop:
  - `margin-top: 0px`;
  - `padding-top: 0px`;
  - `border-top: 0px`;
  - `grid-row: 1 / span 2`;
  - `align-self: start`.
- Screenshot visual aprovado/compartilhável.
- Verificar cascata de CSS: estilos em `layout/theme.liquid` podem sobrescrever a seção depois do `content_for_layout`.
- Registrar rollback/receipt se houver write em produção.

## Rollback

- Reverter o asset da seção/tema usando backup/receipt anterior.
- Se houver hotfix runtime no `layout/theme.liquid`, remover o `<style>` correspondente após consolidar o CSS no asset canônico.
