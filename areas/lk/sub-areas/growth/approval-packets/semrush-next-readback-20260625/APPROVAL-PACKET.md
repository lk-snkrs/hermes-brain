# Approval Packet — SEMrush next clusters readback — 2026-06-25

Status: **readback profundo concluído; nenhum write externo executado**.

Evidências:
- Shopify Admin read-only: `work/semrush-next-readback-20260625/shopify-admin-readback.json`
- Histórico/receipts: `work/semrush-next-readback-20260625/history-hits.txt`
- Public readback: `work/semrush-next-readback-20260625/public-readback.json`
- SERP/DataForSEO mobile BR/PT: consultado para `asics gel 1130`, `adidas gazelle feminino`, `nike shox tl`, `new balance 2002r`.

---

## Resumo executivo

Depois de NB530, Adidas Campus 00s e Adidas SL 72 publicados, a próxima melhor continuação SEMrush é **Adidas Gazelle feminino / Adidas Gazelle**.

Motivo: tem demanda alta, superfície pública real com 30 itens, não tem guia editorial LK nem FAQPage schema e a SERP favorece páginas de categoria/listagem. É o melhor equilíbrio entre impacto, prontidão de superfície e risco baixo.

---

## Ranking recomendado

| Prioridade | Cluster | Volume SEMrush | Superfície LK | Estado atual | Recomendação |
|---|---:|---:|---|---|---|
| P1 | Adidas Gazelle feminino / Gazelle | 12.100 + cauda | `/collections/adidas-gazelle` e `/collections/adidas-gazelle-feminino`, 30 itens | Sem guia LK; FAQPage 0; sem Liquid error | Preparar dev/preview guia/FAQ/schema |
| P2 | ASICS Gel 1130 | 12.100 | Produtos ativos existem; collection específica `/collections/asics-gel-1130` dá 404; superfície atual é `/collections/asics-todos-os-modelos`, 13 itens | Sem guia LK; FAQPage 0; conteúdo público tem termos operacionais antigos | Primeiro resolver superfície/canonical; depois guia |
| P3 | Nike Shox TL | 9.900 | Produtos ativos existem; collection `/collections/nike-shox-tl` dá 404 | Sem collection clara; risco de intenção errada se atacar sem superfície | Handoff/validação de collection antes de Growth write |
| P4 | New Balance 2002R | 8.100 | `/collections/new-balance-2002r`, 2 itens | Já tem guia LK e FAQPage 1 | Não mexer agora; apenas GSC/impact review ou catálogo se ampliar superfície |

---

## 1) Adidas Gazelle feminino — P1 recomendado agora

### Demanda
- `adidas gazelle feminino` — volume 12.100.
- Cauda SERP: `adidas gazelle feminino branco`, `adidas gazelle feminino gucci`, `adidas gazelle feminino prata`, `adidas gazelle feminino promoção`.

### Superfície LK
- `/collections/adidas-gazelle` — 30 itens.
- `/collections/adidas-gazelle-feminino` — 30 itens, aparentemente mesma superfície pública.
- Public QA: 200, sem Liquid error.
- FAQPage schema: 0.
- Guia editorial LK: não detectado.

### SERP intent
SERP dominada por Adidas oficial, Popular Products/Shopping, Dafiti, Netshoes, Authentic Feet, Zattini, Artwalk e Loja Virus. Intenção é claramente categoria/listagem + escolha feminina/styling.

PAA principais:
- “Qual a diferença entre Adidas Gazelle e Samba?”
- “O que significa Adidas Gazelle?”
- “Qual o tênis mais confortável da adidas?”
- “Qual o valor do Adidas Gazelle?”

### Diagnóstico
Melhor continuação. A LK tem coleção com volume visual suficiente e gap claro de guia/FAQ/schema. A ação é semelhante a Campus/SL72, com baixo risco se limitada a snippet condicional em dev.

### Próximo passo seguro
Preparar dev/preview de guia/FAQ/schema para `adidas-gazelle` e/ou rota feminina, cobrindo:
- Gazelle feminino;
- Gazelle Indoor vs OG/Bold;
- diferença Gazelle vs Samba;
- cores branco/prata/rosa/verde/bege;
- conforto e forma;
- autenticidade;
- styling feminino.

---

## 2) ASICS Gel 1130 — P2, mas com pré-requisito

### Demanda
- `asics gel 1130` — volume 12.100.
- Cauda: `asics gel 1130 feminino`, `masculino`, `preto`, `branco`, `prata`, `bege`.

### Superfície LK
- Produtos ativos Gel-1130 encontrados.
- Collection específica `/collections/asics-gel-1130`: 404.
- Superfície pública existente: `/collections/asics-todos-os-modelos`, 13 itens.
- Public QA: sem Liquid error.
- FAQPage schema: 0.
- Guia editorial LK: não detectado.

### Atenção de guardrail
A descrição pública atual da coleção Asics ainda contém termos operacionais antigos como `encomenda` e `entrega rápida`. Não corrigi nesta etapa porque a aprovação foi read-only. Recomendo tratar isso antes/ao preparar qualquer copy nova.

### Diagnóstico
Tem demanda e produto, mas falta superfície específica/canonical para `Gel 1130`. Se atacarmos a coleção geral Asics, diluímos intenção; se criarmos/ativarmos collection específica, entra no escopo LK Shopify/tema e precisa cuidado.

---

## 3) Nike Shox TL — P3, precisa superfície

### Demanda
- `nike shox tl` — volume 9.900.
- Cauda: `nike shox tl black`, `original`, `zip`, `nova`, `feminino`, `branco`, `prata`, `masculino`.

### Superfície LK
- Produtos ativos Shox TL encontrados.
- Collection `/collections/nike-shox-tl`: 404.
- Nenhuma collection clara retornou no Admin search.

### Diagnóstico
Melhor que Shox R4 porque produto existe, mas ainda não é seguro para Growth sem uma collection/hub correta. Precisa handoff/validação de superfície antes.

---

## 4) New Balance 2002R — não mexer agora

### Demanda
- `new balance 2002r` — volume 8.100.

### Superfície LK
- `/collections/new-balance-2002r` — 2 itens.
- Public QA: 200, sem Liquid error.
- Guia editorial LK: detectado.
- FAQPage schema: 1.

### Diagnóstico
Já foi trabalhado. Com apenas 2 itens e guia/schema existente, não é o melhor próximo write. Melhor acompanhar GSC ou ampliar catálogo/superfície antes de nova otimização.

---

# Aprovação recomendada — próximo passo

`Aprovo preparar em dev/preview o guia/FAQ/schema da coleção Adidas Gazelle, focado em Adidas Gazelle feminino, Gazelle Indoor/OG/Bold, diferença Gazelle vs Samba, cores, conforto, forma e autenticidade, sem publicar em produção, sem alterar SEO title/meta, descrição da coleção, produtos, preço, estoque, ordenação, GMC, campanhas, Klaviyo ou checkout, com rollback e QA público do preview.`

# Alternativa se quiser atacar ASICS antes

`Aprovo fazer apenas diagnóstico de superfície/canonical para ASICS Gel 1130, verificando se devemos usar a coleção geral Asics, criar/ativar uma collection específica ou preparar packet para LK Shopify, sem write externo.`
