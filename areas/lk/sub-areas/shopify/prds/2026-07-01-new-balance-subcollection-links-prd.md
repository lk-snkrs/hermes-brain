# PRD — Hub de subcoleções na coleção New Balance Todos os Modelos

Data: 2026-07-01
Owner recomendado: LKGOC/editorial de coleção + LK Shopify execução theme/DEV
Superfície: `https://lksneakers.com.br/collections/new-balance-todos-os-modelos`
Status: PRD / aguardando aprovação para DEV

## 1. Contexto

Lucas identificou que a coleção ampla `New Balance Todos os Modelos` precisa direcionar melhor o usuário para as coleções mais importantes da marca, como `New Balance 9060`, `New Balance 530`, `New Balance 204L` etc.

Hoje a página ampla funciona como catálogo agregado, mas não oferece uma navegação editorial clara para as principais silhuetas. Isso dificulta descoberta, reduz profundidade de navegação interna e perde oportunidade SEO/CRO.

## 2. Problema

Usuário que entra em `New Balance Todos os Modelos` pode querer um modelo específico, mas precisa filtrar/rolar muito ou usar busca.

Problemas práticos:
- falta de atalhos para subcoleções relevantes;
- baixa visibilidade de silhuetas estratégicas;
- oportunidade perdida de linkagem interna entre coleção mãe e coleções filhas;
- experiência mobile menos guiada.

## 3. Objetivo

Adicionar um bloco de navegação de subcoleções na coleção mãe New Balance, com links visuais/textuais para as principais silhuetas.

Objetivos:
- melhorar navegação e descoberta;
- reforçar SEO interno por links contextuais;
- aumentar acesso às coleções prioritárias;
- manter estética premium/quiet luxury do tema LK;
- não alterar produtos, estoque, preços, ordenação, filtros ou checkout.

## 4. Evidência read-only inicial

Página pública:
- URL: `/collections/new-balance-todos-os-modelos`
- Meta title: `New Balance Todos os Modelos | LK Sneakers`
- Meta description pública menciona 132 modelos originais.

Subcoleções verificadas por HEAD público com destino dedicado 200:
- `/collections/new-balance-9060`
- `/collections/new-balance-530`
- `/collections/new-balance-204l`
- `/collections/new-balance-1906r`
- `/collections/new-balance-1906l`
- `/collections/new-balance-2002r`
- `/collections/new-balance-550`

Candidatos que não devem entrar sem nova coleção dedicada, pois retornaram 404 ou redirecionaram para a coleção mãe:
- `/collections/new-balance-990` — 404
- `/collections/new-balance-327` — 404
- `/collections/new-balance-574` — redireciona para mãe
- `/collections/new-balance-1000` — redireciona para mãe
- `/collections/new-balance-740` — redireciona para mãe

## 5. Escopo da primeira versão

### Incluir

Adicionar bloco acima do grid de produtos ou imediatamente abaixo do header/banner da coleção:

Título sugerido:
- `Explore por modelo New Balance`

Subtítulo sugerido:
- `Acesse rapidamente as principais silhuetas da curadoria LK.`

Links/chips/cards v1:
1. New Balance 9060 → `/collections/new-balance-9060`
2. New Balance 530 → `/collections/new-balance-530`
3. New Balance 204L → `/collections/new-balance-204l`
4. New Balance 1906R → `/collections/new-balance-1906r`
5. New Balance 1906L → `/collections/new-balance-1906l`
6. New Balance 2002R → `/collections/new-balance-2002r`
7. New Balance 550 → `/collections/new-balance-550`

### Excluir nesta versão

- criação/edição de coleções Shopify;
- alteração de descrição da coleção;
- mudança de produtos, sort, filtros, tags, SEO fields, estoque ou preço;
- automação dinâmica por Admin/metafield;
- qualquer Production antes de DEV readback/QA + aprovação.

## 6. Requisitos UX/UI

### Desktop

- Bloco horizontal/grade compacta, visual premium e discreto.
- Cards/chips com borda fina, fundo claro, texto em uppercase pequeno.
- Não competir com o título da coleção nem empurrar demais o grid.
- Até 7 links em grid responsivo, por exemplo `repeat(4)` ou `auto-fit`.

### Mobile

- Prioridade: navegação rápida sem poluir.
- Opção recomendada: trilho horizontal com scroll-snap ou grid 2 colunas compacto.
- Altura baixa, sem ocupar tela inteira.
- Área de toque mínima adequada.

### Acessibilidade

- Links reais `<a href>`.
- Sem JS obrigatório.
- Título semântico `h2` ou `p` + `aria-label` dependendo da estrutura.

## 7. Opções de implementação

### Opção A — bloco hardcoded escopado no `sections/lk-collection.liquid`

Adicionar condição por handle:

```liquid
{% if collection.handle == 'new-balance-todos-os-modelos' %}
  ... bloco de links ...
{% endif %}
```

Prós:
- rápido;
- baixo risco;
- sem depender de metafields/menu;
- ótimo para validar UX.

Contras:
- precisa novo deploy para alterar links.

### Opção B — snippet reutilizável por marca

Criar snippet `snippets/lk-collection-subnav.liquid` e renderizar com lista/condição.

Prós:
- reutilizável para Adidas, Nike, Onitsuka etc.;
- código mais limpo.

Contras:
- um pouco mais de escopo.

### Opção C — menu/metafield por coleção

Bloco lê menu/metafield configurável por coleção.

Prós:
- escalável e editável pelo Admin.

Contras:
- mais pontos de falha;
- exige write/config Shopify adicional;
- maior risco e mais QA.

## 8. Recomendação

Recomendo **Opção B enxuta**:

- criar snippet reutilizável `lk-collection-subnav.liquid`;
- renderizar apenas em `new-balance-todos-os-modelos` no primeiro PR;
- lista hardcoded dentro do snippet ou passada por condição no snippet;
- se aprovado e performar bem, expandir depois para outras marcas.

Motivo: mantém baixo risco, mas evita criar uma gambiarra exclusiva que depois precisa ser duplicada.

## 9. Critérios de aceite DEV

- DEV/unpublished theme recebe o bloco apenas em `/collections/new-balance-todos-os-modelos`.
- Production não é tocado na primeira etapa.
- Links aparecem acima do grid ou abaixo do banner/intro.
- Todos os 7 links retornam HTTP 200 e destino dedicado, sem redirecionar para a coleção mãe.
- Mobile legível e clicável.
- Desktop não quebra grid/filtro/sidebar.
- Sem Liquid errors.
- Sem alteração em produtos, estoque, preço, filtros, sort ou checkout.
- Readback Admin confirma arquivos alterados.

## 10. QA mínimo

### Fonte/Admin
- readback DEV dos arquivos alterados;
- diff restrito a snippet/section de coleção;
- verificar marker do bloco, ex. `data-lk-subcollection-nav="new-balance"`.

### Público/preview
- abrir DEV preview da coleção mãe;
- validar presença dos links;
- clicar/HEAD nos 7 destinos;
- validar desktop e mobile;
- verificar ausência em pelo menos uma coleção não-NB para garantir escopo.

## 11. Rollback

- remover render do snippet em `sections/lk-collection.liquid`; ou
- reverter o snippet/render line no DEV.

Para Production futura:
- rollback via revert PR GitHub.

## 12. Próxima decisão

Aprovação sugerida para DEV:

> Aprovo criar em DEV o bloco de subcoleções na coleção New Balance Todos os Modelos, usando snippet reutilizável, com links para 9060, 530, 204L, 1906R, 1906L, 2002R e 550, sem Production.
