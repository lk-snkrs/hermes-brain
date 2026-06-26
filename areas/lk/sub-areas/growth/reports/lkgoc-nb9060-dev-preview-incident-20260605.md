# Incident — LKGOC New Balance 9060 DEV preview errado

Data UTC: 2026-06-05T09:48:07Z

## Situação
Lucas reportou que o hero e o guia pós-grid do preview New Balance 9060 estavam errados visualmente e fora do padrão LKGOC/204L.

## Causa raiz
- O agente aplicou um componente simplificado (`lk-goc-9060-*`) em vez de copiar/adaptar literalmente o padrão canônico aprovado da New Balance 204L.
- O agente tratou a existência de copy/evidence local como suficiente para implementação, sem refazer o contrato visual bloco a bloco contra o gold source 204L.
- O QA executado validou presença textual/DOM e ausência de linguagem operacional, mas não validou paridade visual 204L antes de enviar para Lucas.
- Havia um hero 9060 pré-existente no DEV em padrão `lk-next-*`; ele foi aproveitado/retocado indevidamente em vez de ser substituído por clone/adaptação canônica 204L.

## Correção imediata executada
- Removido do DEV o hook/render visível do snippet `lk-goc-new-balance-9060` em `sections/lk-collection.liquid`.
- Removido o desc override 9060 adicionado no DEV.
- Produção/main não foi tocada.

## Regra reforçada
Para LKGOC, não basta “conteúdo correto”. A implementação deve copiar/adaptar o layout aprovado do gold source, incluindo hierarquia, classes, densidade, espaçamento, comportamento mobile/desktop e posição do guia.

## Próxima execução correta
1. Extrair o bloco 204L aprovado real do DEV/produção.
2. Clonar estrutura e CSS com namespace `lk-goc-*`, mantendo compatibilidade onde necessário.
3. Trocar somente conteúdo/links/FAQ/produto.
4. QA visual por comparação lado a lado 204L vs 9060 antes de mandar para Lucas.
5. Só então reenviar approval com botão inline quando disponível.
