# PRD — LK Collection Suggestion

Criado: 2026-06-08 12:35 BRT
Responsável: LK Shopify / Hermes
Status: PRD aprovado conceitualmente por Lucas; **sem execução de tema neste documento**.

## 1. Resumo

O **LK Collection Suggestion** é um módulo da página de busca da LK Sneakers que sugere coleções públicas relevantes quando o cliente pesquisa pelo nome, modelo, marca, cápsula ou colaboração de uma coleção.

Exemplo esperado:

- Busca: `204L`
- Sugestão: `Ver coleção: New Balance 204L · Ver coleção completa →`
- Link: `/collections/new-balance-204l`

A busca continua mostrando produtos normalmente. A sugestão é um atalho editorial/comercial para levar o cliente à coleção mais adequada quando o termo pesquisado tem correspondência forte com uma coleção pública.

## 2. Objetivos

1. Melhorar a navegação de clientes com intenção clara de coleção/modelo.
2. Reduzir fricção entre busca de produto e páginas de coleção.
3. Sugerir a coleção correta mesmo quando a busca de produtos retorna poucos ou nenhum resultado.
4. Manter o visual premium e compacto já aprovado para a busca LK.
5. Cobrir automaticamente todas as coleções públicas elegíveis, com score para priorizar conflitos.

## 3. Não objetivos / fora de escopo

- Não alterar produtos, preços, estoque, disponibilidade ou ordenação de coleções.
- Não alterar Search & Discovery, apps, GMC, ads, Klaviyo, WhatsApp ou campanhas.
- Não substituir a busca de produtos; a sugestão é complementar.
- Não sugerir coleções genéricas que criem ruído, como `Sneakers` ou `Tênis e Sneakers Originais`, quando isso parecer estranho ou pouco útil.
- Não incluir coleções de sistema/merchandising genéricas como `sale`, `lançamentos`, `best sellers`, `roupas`, `apparels` e similares, salvo decisão futura explícita.

## 4. Requisitos funcionais

### 4.1 Quando sugerir

O módulo deve sugerir coleção quando o termo pesquisado corresponder a:

- Nome exato da coleção.
- Modelo exato, especialmente numérico/alfanumérico, por exemplo `204L`, `9060`, `530`.
- Marca + modelo, por exemplo `New Balance 204L`.
- Busca com modelo + cor/atributo, por exemplo `samba verde`, quando houver uma coleção principal segura para o modelo.
- Colaboração/cápsula, quando a coleção pública correspondente existir e for a mais relevante.

### 4.2 Quando sugerir mesmo sem resultado

Se a busca não encontrar produtos, mas existir uma coleção correspondente, a sugestão deve aparecer mesmo assim.

Nesse caso, a sugestão pode funcionar como principal saída útil da página, sem remover a mensagem de busca sem resultados.

### 4.3 Quantidade de sugestões

- Mostrar até **2 ou 3 sugestões**.
- Se houver apenas uma correspondência clara, mostrar uma única sugestão.
- Se houver ambiguidade, ranquear por score e mostrar as melhores.

### 4.4 Conflitos

Quando um termo bater em várias coleções, vence a **coleção principal**.

Exemplo:

- Busca: `samba`
- Possíveis matches:
  - Adidas Samba
  - Adidas Samba OG
  - Adidas Samba Jane
- Resultado esperado: priorizar a coleção principal `Adidas Samba`, salvo score/curadoria indicar outra regra em caso específico.

### 4.5 Termos numéricos / alfanuméricos

Termos de modelo devem ter correspondência exata.

Exemplos:

- `530` → New Balance 530.
- `9060` → New Balance 9060.
- `204L` → New Balance 204L.

Evitar correspondências frouxas que possam sugerir coleção errada.

### 4.6 Todas as coleções públicas

O mapa deve ser gerado automaticamente a partir de **todas as coleções públicas elegíveis**.

Coleções não elegíveis devem ser filtradas por regra, não por esquecimento manual.

## 5. Regras de elegibilidade de coleção

### 5.1 Incluir

Incluir coleções públicas que sejam úteis como destino de busca, por exemplo:

- Marcas.
- Modelos.
- Linhas/silhuetas.
- Cápsulas.
- Collabs.
- Coleções editoriais específicas com intenção clara.

### 5.2 Excluir por padrão

Excluir coleções genéricas ou de sistema, incluindo:

- Sale / promoção.
- Lançamentos.
- Best sellers.
- Roupas / apparels, salvo futura decisão.
- Sneakers / Tênis e Sneakers Originais, por ser amplo demais e visualmente estranho como sugestão.
- Coleções internas, auxiliares, duplicadas ou sem utilidade como destino de busca.

## 6. Score e aprovação automática de sugestão

Lucas delegou ao Hermes a aprovação operacional dos conflitos, usando score.

O score deve considerar, nesta ordem sugerida:

1. Correspondência exata do termo com alias da coleção.
2. Se a coleção é principal vs subvariação/collab.
3. Vendas da coleção/produtos relacionados.
4. Visitas/interesse em PDPs ou coleção.
5. Tamanho/quantidade de produtos da coleção.
6. Coleção presente em menu/navegação ativa.
7. Penalidade para termos ambíguos ou genéricos.

Em conflitos, sugerir a coleção com maior score. Se a confiança estiver baixa, registrar para revisão em manutenção semanal em vez de forçar sugestão ruim.

## 7. UX / visual

### 7.1 Formato

Manter o formato compacto atual dentro do banner preto da busca.

Copy aprovada:

- Prefixo: `Ver coleção:`
- Nome/link da coleção.
- CTA: `Ver coleção completa →`

### 7.2 Mobile

No mobile, a sugestão deve ficar em **uma linha compacta** quando possível.

Se houver 2 ou 3 sugestões, manter o bloco visualmente leve, sem criar card grande/off-white e sem empurrar agressivamente a grade de produtos para baixo.

### 7.3 Produto continua primeiro

A busca continua sendo product-only e a grade de produtos deve continuar renderizando normalmente.

A sugestão é um atalho, não um redirecionamento automático.

## 8. Dados e geração do mapa

### 8.1 Fontes read-only

Usar fontes read-only para gerar o mapa:

1. Shopify Admin / coleções públicas.
2. Storefront público `/collections.json`, quando útil.
3. Menus ativos, para priorização.
4. Métricas de vendas e visitas disponíveis nos sistemas LK.
5. Títulos/handles de coleções.

### 8.2 Aliases automáticos

Gerar aliases conservadores:

- Título normalizado.
- Handle com hífens convertidos em espaços.
- Handle exato.
- Marca + modelo.
- Modelo exato.
- Abreviações óbvias, por exemplo `New Balance` → `NB`.

### 8.3 Collabs

Collabs entram, mas com cuidado:

- `loewe on running` pode sugerir `Loewe x On Running`.
- `on running` deve priorizar a coleção principal On Running, não uma collab.
- Fragmentos genéricos de colaborador não devem roubar busca ampla.

## 9. Manutenção recorrente

Criar rotina recorrente de manutenção:

- Frequência: toda sexta-feira às 18h BRT.
- Modo padrão: read-only/dry-run.
- Objetivo:
  - detectar novas coleções públicas;
  - atualizar aliases candidatos;
  - revisar conflitos;
  - recalcular score com vendas/visitas;
  - gerar relatório e approval packet quando houver mudança relevante.

Nenhuma atualização de tema deve acontecer automaticamente sem aprovação/fluxo de merge correspondente.

## 10. Plano de implementação

### Fase 1 — PRD e mapa completo local

- Gerar mapa completo de coleções públicas elegíveis.
- Aplicar filtros de exclusão.
- Calcular score.
- Produzir arquivo local de target `sections/lk-search.liquid`.
- Validar static checks.
- Não fazer upload.

### Fase 2 — DEV via GitHub/dev

Lucas definiu que a subida para DEV deve seguir GitHub:

1. Criar branch a partir do source correto.
2. Alterar `sections/lk-search.liquid`.
3. Abrir PR para branch `dev` ou fluxo equivalente do tema DEV.
4. Fazer merge para DEV.
5. Aguardar/sincronizar com tema DEV/unpublished.
6. Validar readback DEV.
7. QA visual/funcional.

Escopo DEV:

- Tema DEV/unpublished.
- Asset `sections/lk-search.liquid`.
- Mapa completo de coleções públicas elegíveis.

### Fase 3 — Merge Production

Depois do DEV aprovado:

1. Criar PR para branch `production`.
2. Seguir padrão normal de merge.
3. Aguardar sync Shopify Production.
4. Readback Production.
5. QA público com cache-buster/no-cache.
6. Registrar receipt e rollback.

Production não deve receber Asset API direto por conveniência.

## 11. Rollback

Rollback completo deve estar previsto.

### DEV

- Reverter PR/commit em `dev`, ou restaurar o asset anterior salvo.
- Confirmar readback DEV.

### Production

- Reverter merge commit via GitHub PR/revert na branch `production`.
- Confirmar readback Production.
- QA público pós-rollback.

Rollback deve remover completamente o LK Collection Suggestion se necessário, não apenas voltar para regra parcial de `9060`.

## 12. QA obrigatório

### 12.1 Queries positivas

Validar que sugerem coleção correta:

- `204L` → New Balance 204L.
- `9060` → New Balance 9060.
- `530` → New Balance 530.
- `Samba` → coleção principal Adidas Samba.
- `Dunk Low` → coleção principal Nike Dunk Low.
- `On Running` → coleção principal On Running.
- `Wales Bonner` → coleção/collab correta.
- `Loewe` / `Loewe On Running` → collab correta sem roubar `On Running`.
- `Jordan 1` → coleção principal correta.
- `Air Max 1` → coleção principal correta.

### 12.2 Queries com cor/atributo

Validar que podem sugerir coleção principal:

- `samba verde`.
- `204L cinza`.
- `dunk low rosa`.

### 12.3 Queries negativas / não sugerir

Validar que não sugerem coleções estranhas/genéricas:

- `sneakers`.
- `roupas`.
- `sale`.
- `lançamentos`.
- termos ambíguos de baixa confiança.

### 12.4 Zero resultados

Validar query que tenha 0 produtos mas match de coleção, garantindo que a sugestão aparece.

### 12.5 Visual

- Desktop: compacto dentro do banner preto.
- Mobile: uma linha compacta quando possível.
- Até 2 ou 3 sugestões sem poluir visual.
- Sem card grande/off-white antigo.
- Product grid preservado.

## 13. Critérios de sucesso

O projeto é considerado bem-sucedido quando:

1. Queries principais mostram a coleção correta.
2. `204L`, `9060`, `530`, `Samba`, `Dunk Low`, `On Running`, `Wales Bonner`, `Loewe`, `Jordan 1` e `Air Max 1` passam no QA.
3. Sugestões aparecem também quando não há resultado de produto, desde que exista coleção correspondente.
4. Não há sugestão estranha para termos genéricos como `sneakers`.
5. O visual está compacto e premium no desktop/mobile.
6. A busca continua product-only e a grade de produtos permanece funcional.
7. DEV passa readback e QA.
8. Production é feito via merge padrão e passa readback/QA público.

## 14. Decisões de Lucas incorporadas

- Cobrir todas as coleções públicas elegíveis.
- Excluir coleções genéricas/sistema como sale, lançamentos, best sellers, roupas e sneakers.
- Sugerir collabs quando seguro.
- Sugerir também com termo + cor/atributo.
- Mostrar até 2 ou 3 sugestões.
- Manter formato compacto dentro do banner preto.
- Prefixo/copy: `Ver coleção:`.
- Busca de produtos continua aparecendo.
- Mostrar sugestão mesmo com zero resultados.
- Gerar automaticamente.
- Hermes aprova conflitos pelo maior score com vendas/visitas.
- Manutenção toda sexta-feira às 18h BRT.
- DEV deve passar por GitHub/dev; Production pelo padrão de merge.
- Rollback completo.
