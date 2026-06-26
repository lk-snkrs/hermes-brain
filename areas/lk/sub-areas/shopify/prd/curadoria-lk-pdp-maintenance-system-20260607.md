# PRD — Sistema de manutenção recorrente da Curadoria LK PDP

Data: 2026-06-07
Área: LK Shopify / Curadoria LK PDP
Status: Proposta operacional read-only; sem write externo executado

## Problema

Os blocos de Curadoria LK PDP hoje são grupos estáticos de produtos relacionados. Isso resolve a primeira camada de CRO/editorial, mas cria risco de envelhecimento:

- best sellers mudam;
- estoque e disponibilidade mudam;
- novos drops entram;
- produtos podem sair de linha, esgotar ou ficar menos relevantes;
- algumas imagens podem mudar ou virar placeholder;
- clusters podem perder coerência comercial com o tempo.

Sem uma rotina de revisão, a Curadoria pode continuar tecnicamente correta, mas comercialmente velha.

## Objetivo

Transformar a Curadoria LK PDP em uma rotina semi-automatizada de manutenção, com análise read-only recorrente, score comercial/editorial, approval packet e execução apenas após aprovação explícita.

## Princípios

1. Não atualizar em tempo real no storefront.
2. Não deixar a lista fixa indefinidamente.
3. Usar automação para detectar oportunidades e riscos.
4. Manter revisão humana/editorial antes de qualquer mudança.
5. Preservar o fluxo seguro: read-only → packet → DEV aprovado → QA → Production aprovado → readback/receipt/rollback.
6. Separar sinais comerciais de regras visuais/editoriais.

## Fontes de sinal

### Shopify / catálogo

- produto ativo/publicado;
- handle público 200;
- imagem válida e sem placeholder;
- coleção/modelo/silhueta;
- vendor/brand;
- tags e metacampos úteis;
- preço e disponibilidade visível no storefront.

### Comercial / demanda

- vendas recentes por produto/modelo;
- best sellers por família/coleção;
- visitas de PDP / interesse GA4 quando disponível;
- produtos novos relevantes;
- prioridade comercial definida pela LK;
- margem ou giro, se disponível em fonte segura;
- estoque real: Tiny continua sendo a verdade operacional de estoque quando necessário.

### Editorial / UX

- mesma silhueta/modelo antes de mesma marca genérica;
- collab/cápsula separada de linha regular;
- produto atual sempre excluído dos cards;
- labels curtos e legíveis no mobile;
- evitar mistura fraca só para completar 5 cards;
- evitar kids/TD quando o grupo é adulto;
- evitar placeholders como `TenisMoldeLK`.

## Score sugerido

Cada candidato recebe uma pontuação explicável:

- + mesma silhueta/modelo;
- + mesma cápsula/collab quando o grupo for de collab;
- + mesma marca quando fizer sentido;
- + disponível/publicado;
- + imagem pública válida;
- + vendas recentes fortes;
- + tráfego/interesse de PDP;
- + produto novo e relevante;
- + prioridade comercial LK;
- - esgotado ou sem disponibilidade visível;
- - placeholder/imagem ruim;
- - handle público 404/redirect/home;
- - duplicado no grupo;
- - produto atual vazando no próprio bloco;
- - mistura semântica fraca.

## Cadência proposta

### Semanal

Para clusters de alto giro e famílias com muitos SKUs:

- Samba/Gazelle;
- Dunk/Jordan;
- New Balance 530/9060/1906;
- On Running;
- Asics relevantes;
- grupos com best sellers mudando rápido.

### Quinzenal

Para famílias médias ou com reposições frequentes.

### Mensal

Para grupos editoriais mais estáveis:

- collabs raras;
- cápsulas limitadas;
- produtos premium de menor giro;
- grupos com pouca renovação.

### Sob demanda

Quando houver:

- drop novo;
- grande reposição;
- produto estratégico;
- reclamação visual/comercial;
- produto esgotado aparecendo em bloco importante.

## Relatório recorrente — formato padrão

Cada rodada deve entregar um relatório com:

1. Blocos analisados.
2. Estado atual de cada bloco.
3. Problemas encontrados:
   - produto esgotado;
   - imagem inválida/placeholder;
   - handle público inválido;
   - card duplicado;
   - menos de 5 alternativas seguras;
   - mistura semântica fraca;
   - bloco não renderizando publicamente.
4. Produtos novos candidatos.
5. Proposta de troca por bloco:
   - manter;
   - remover;
   - adicionar;
   - substituir;
   - aguardar.
6. Motivo de cada troca.
7. Risco e rollback.
8. Decisão pedida ao Lucas.

## Semáforo por bloco

- Verde: bloco atual segue coerente, público e comercialmente aceitável.
- Amarelo: bloco funciona, mas tem oportunidade de melhorar ranking/novidades.
- Vermelho: bloco tem problema operacional ou comercial relevante e precisa de correção.
- Cinza: dados insuficientes; precisa de fonte comercial/estoque ou revisão manual.

## Execução segura

### Etapa 1 — Scan read-only

- Parsear grupos já publicados/DEV;
- validar handles e imagens;
- cruzar com catálogo/disponibilidade;
- cruzar com sinais comerciais disponíveis;
- gerar score e justificativas.

### Etapa 2 — Approval packet

Gerar pacote com:

- antes/depois por grupo;
- cards adicionados/removidos;
- motivo de cada troca;
- risco;
- QA planejado;
- rollback;
- aprovação pedida para DEV.

### Etapa 3 — DEV somente após aprovação

- aplicar em tema DEV/unpublished;
- readback Asset API;
- QA estático;
- preview público quando possível;
- receipt.

### Etapa 4 — Production somente após aprovação separada

- merge para Production via GitHub PR;
- deploy/readback Shopify;
- QA público multi-round;
- receipt e rollback.

## Critérios de bloqueio

Não propor ou não aplicar candidato se:

- público 404/redirect/home;
- imagem placeholder ou inválida;
- produto atual aparece no próprio bloco;
- grupo teria menos de 5 alternativas seguras, salvo se Lucas aprovar bloco menor;
- mistura regular/collab enfraquece a experiência;
- há conflito com estoque/availability;
- fonte comercial está incompleta para uma decisão de best seller.

## Recomendação inicial

Criar uma rotina de revisão semanal read-only da Curadoria LK PDP, começando por:

1. grupos recém-publicados e com edge/cache ainda estabilizando;
2. clusters de maior giro;
3. grupos com muitos SKUs e maior risco de envelhecer;
4. oportunidades de novos drops.

A primeira entrega deve ser um relatório piloto, sem write externo, para calibrar pesos e critérios antes de automatizar qualquer cron.

## Próxima decisão sugerida

Aprovar apenas a criação do primeiro relatório piloto read-only de manutenção da Curadoria LK PDP.

Escopo do piloto:

- mapear todos os blocos atuais;
- validar handles/imagens/disponibilidade pública;
- classificar verde/amarelo/vermelho/cinza;
- sugerir trocas prioritárias;
- não executar nenhum DEV/Production write.
