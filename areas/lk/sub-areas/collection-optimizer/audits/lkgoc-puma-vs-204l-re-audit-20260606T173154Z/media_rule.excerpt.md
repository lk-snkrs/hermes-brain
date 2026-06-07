# REGRA — LKGOC mídia, DEV write e Production merge

Registrado em: 20260606T165914Z
Fonte: correção direta de Lucas Cimino.

## 1. Imagens principais: veículos de moda como fonte obrigatória

Para LKGOC, o agente deve **sempre buscar e retirar as imagens principais dos principais veículos de moda/editoriais** quando forem relevantes para a coleção, incluindo exemplos como:

- Vogue;
- Vogue Brasil / Globo;
- Highsnobiety;
- Hypebeast;
- GQ / Esquire / Elle / Harper's Bazaar quando aplicável;
- campanhas/editoriais oficiais de marca quando forem a melhor referência visual.

Interpretação operacional:

- Para hero e módulos editoriais, priorizar imagem principal editorial/lifestyle desses veículos, não packshot.
- Imagem de produto isolado, PDP ou packshot não é padrão LKGOC para hero.
- Registrar fonte/URL no receipt e no media manifest.
- Se houver múltiplas opções, escolher a imagem com maior força editorial: pessoa usando, street style, contexto de moda, campanha ou atmosfera aspiracional.

## 2. Shopify write: sempre DEV, sem pedir autorização

Todo write operacional do LKGOC em Shopify deve ser feito **sempre no tema DEV/unpublished**.

- Write em DEV/unpublished é permitido por padrão.
- Não precisa pedir autorização de Lucas para escrever, testar, ajustar, criar preview, fazer QA, readback ou rollback em DEV.
- Antes de escrever, verificar por API que o tema alvo tem `role: unpublished`.
- Se o tema alvo for `role: main`, abortar imediatamente.

## 3. Production é extremamente proibido

É **extremamente proibido** fazer write direto no tema Production/main.

Proibido sem aprovação explícita de Lucas:

- editar asset em tema `role: main`;
- publicar template/section/snippet direto em production;
- merge/promover DEV para Production;
- qualquer alteração customer-facing fora do fluxo de aprovação.

A única coisa que Lucas aprova é:

- **merge/promoção para tema Production/main** depois do QA e approval packet.

## 4. Fluxo canônico atualizado

1. Pesquisar referências editoriais e imagens principais nos veículos de moda relevantes.
2. Criar media manifest com URL/fonte das imagens usadas.
3. Verificar tema DEV por API: `role: unpublished`.
4. Fazer write em DEV sem pedir autorização.
5. Gerar preview DEV.
6. Rodar QA visual/editorial/mobile/desktop/readback.
7. Preparar approval packet para Lucas.
8. Somente após aprovação explícita, fazer merge/promoção para Production.
9. Nunca fazer write direto no tema Production.

## 5. Correção sobre regras antigas

Qualquer documentação anterior que diga que:

- imagem de Vogue/veículos editoriais só pode ser inspiração e não asset;
- falta de autorização de imagem bloqueia DEV;
- Contract Lock bloqueia write em DEV;
- o agente deve pedir autorização para write em DEV;

está **obsoleta** e deve ser interpretada pela regra atual:

- imagens principais de veículos de moda devem ser buscadas/usadas no LKGOC;
- DEV write é liberado;
- Production/main é proibido sem merge aprovado por Lucas.
