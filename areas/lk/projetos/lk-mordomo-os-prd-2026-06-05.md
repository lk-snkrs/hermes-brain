# PRD — LK Mordomo OS

Data: 2026-06-05  
Owner: Lucas Cimino  
Contexto: LK Sneakers / Mordomo Hermes / LK OS  
Status: v0.1 criado no Brain, sem execução externa

## 1. Resumo executivo

O **LK Mordomo OS** é a camada de assistente operacional da LK dentro do Hermes. Ele não substitui o LK OS, Mission Control, LK Growth ou os relatórios comerciais; ele funciona como a interface executiva/action-first que observa os sinais da LK, transforma em decisões claras para Lucas/equipe e executa apenas classes seguras já aprovadas.

A diferença central:

- **LK OS**: sistema operacional de dados, rotinas, relatórios e inteligência da LK.
- **LK Growth OS**: SEO/CRO/GEO, conteúdo, coleções, growth e melhorias de superfície.
- **Mission Control**: cockpit visual/kanban/decision inbox.
- **LK Mordomo OS**: secretário operacional e roteador de decisões: lê sinais, prepara respostas, follow-ups, alertas, aprovações e handoffs, mantendo Lucas fora do ruído.

Princípio:

> Telegram de Lucas recebe decisão, exceção ou falha; o resto fica em Brain, relatórios, CRM, Mission Control ou silêncio operacional.

## 2. Razão de existir

A LK tem muitas superfícies: Shopify, loja física/POS, Tiny, Klaviyo, Meta/Pareto, FHITS/influencers, GA4, Google Merchant Center, Search Console, Judge.me, Frenet, WhatsApp, e-mails, relatórios diários/semanais e rotinas de sourcing.

O problema não é só gerar mais relatórios. O problema é decidir:

1. o que exige Lucas agora;
2. o que pode ser resolvido sem Lucas;
3. o que deve virar tarefa para equipe/fornecedor;
4. o que é ruído;
5. o que deve alimentar CRM, recompra, estoque, campanha ou learning loop.

O LK Mordomo OS existe para transformar sinais operacionais em fila clara de ação, com guardrails.

## 3. North Star

> Reduzir a dependência manual de Lucas na operação da LK, mantendo a decisão humana onde há risco comercial, estoque, preço, fornecedor, campanha ou cliente, e automatizando somente leitura, organização, follow-up logístico seguro, roteamento e preparação de decisão.

## 4. Fontes e superfícies conhecidas

### 4.1 Fontes de verdade

- **Shopify**: pedidos, clientes, catálogo, preço atual, produto/variant/SKU, source/canal quando disponível.
- **Tiny / `LK | CONTROLE ESTOQUE`**: verdade operacional de estoque livre/reservado/físico quando sincronizado.
- **Data Spine local / SQLite privado**: espelho operacional/analítico para consultas, auditoria e relatórios, com PII minimizada fora do DB privado.
- **GA4 / Shopify Analytics**: sessões, conversão e funil.
- **GSC / GMC**: busca orgânica, Shopping, feed, reprovações, disponibilidade e problemas de landing.
- **Meta / Google Ads / Metricool**: sinais de plataforma, não receita operacional final.
- **Klaviyo**: listas, campanhas, templates e comunicação online.
- **Judge.me / Rivo / Frenet**: reviews, fidelidade e frete, conforme acesso/rotina.
- **Notion LK**: compras, encomendas e execução humana, quando aprovado.
- **WhatsApp / WACLI / OpenClaw**: camada de grupos internos e possivelmente atendimento, sempre com escopo e guardrails.
- **Brain LK**: decisões, rotinas, PRDs, handoffs e aprendizado.

### 4.2 Superfícies de saída

- Telegram Lucas: decisões/exceções/falhas, não logs.
- Grupos internos LK aprovados: respostas operacionais quando Hermes for mencionado, conforme PRD de WhatsApp LK Team / LK Atendimento.
- Brain LK: fonte canônica de decisões e aprendizados.
- Mission Control: cockpit/kanban/approval manager.
- Relatórios locais: evidência e recibo.
- WhatsApp/e-mail externo: bloqueado salvo aprovação explícita atual ou subfluxo estreito aprovado.

## 5. Módulos do LK Mordomo OS

### 5.1 Decision Inbox LK

Fila única com itens que realmente precisam de decisão.

Campos mínimos:

- contexto: vendas, estoque, atendimento, campanha, growth, sourcing, logística, infraestrutura;
- contato/canal quando aplicável;
- o que aconteceu;
- por que importa;
- risco;
- recomendação;
- texto/ação sugerida;
- aprovação necessária;
- fonte consultada;
- prazo.

Regra de UX: não mandar dumps técnicos ou bullets genéricos. Cada alerta precisa ser um pacote acionável.

### 5.2 Signal Router

Classifica sinais em:

- `silent_log`: registrar localmente, sem Lucas;
- `receipt`: informar ação concluída, se relevante;
- `digest`: consolidar em resumo diário/17h/23h;
- `decision`: pedir decisão clara;
- `approval_packet`: preview exato antes de write/envio;
- `technical_failure`: falha real, curta e com impacto;
- `blocked_sensitive`: preço, estoque, campanha, fornecedor, cliente, desconto, reclamação, alteração de sistema.

### 5.3 Atendimento interno LK

Escopo aprovado/conhecido: Hermes nos grupos `LK Team` e `LK Atendimento`, respondendo quando mencionado, com dados agregados e fonte/janela temporal.

Pode responder:

- quanto vendeu hoje/ontem/semana/mês;
- produto/marca/tamanho mais vendido;
- visitas/conversão quando fonte estiver disponível;
- alerta agregado de estoque;
- onde consultar um dado ou relatório;
- explicação de fonte: Shopify vs Tiny vs GA4 vs Meta.

Não pode responder ou executar:

- desconto, preço especial, promessa a cliente, reserva, troca sensível, campanha, publicação, alteração Shopify/Tiny/Klaviyo/Meta/Google, compra, contato fornecedor.

### 5.4 Follow-ups e logística segura

Classes candidatas para autonomia estreita:

- confirmar compromisso logístico já conhecido com fornecedor/prestador validado;
- lembrar equipe sobre pendência operacional sem negociação;
- follow-up interno sobre tarefa prometida quando a obrigação está clara;
- reportar exceção de pedido/entrega quando há bloqueador real.

Bloquear sempre:

- preço, desconto, compra, prazo novo, promessa a cliente, reclamação, disponibilidade, estoque não verificado, negociação ou decisão de fornecedor.

### 5.5 CRM/RFM/Recompra

O Mordomo deve transformar sinais em oportunidades estruturadas, não em campanhas automáticas.

Exemplos:

- cliente comprou um modelo/marca e pode recomprar;
- cliente ficou sem tamanho/produto e deve entrar em fila de restock;
- cliente de alto valor sem recompra em janela relevante;
- oportunidade para Klaviyo segmentada;
- oportunidade para WhatsApp 1:1, mas apenas como preview/approval packet.

Saídas:

- segmento sugerido;
- motivo;
- fonte;
- risco de abordagem;
- copy prévia;
- canal recomendado;
- approval gate.

### 5.6 Stock/Sourcing Assistant

Transforma sinais de estoque em decisão para Lucas/Júlio.

Regras já aprendidas:

- Shopify é venda/catálogo/SKU canônico.
- Tiny é estoque oficial.
- Estoque Shopify sozinho não autoriza ação comercial.
- Reposição precisa produto + SKU + tamanho + fonte + confiança.
- Preço médio vendido não é campo decisório primário de sourcing.
- Campos relevantes: preço Droper, preço StockX/GOAT USD, custo produto BRL, preço site LK, margem, rota recomendada, prioridade.
- Hermes não compra, não reserva, não paga e não contata fornecedor.

Saída ideal:

- P1 comprar primeiro;
- P2 comprar se orçamento permitir;
- P3 monitorar preço;
- P4 não comprar agora;
- decisão/manual para Júlio/Lucas.

### 5.7 Campaign & Growth Gate

O Mordomo não cria campanha sozinho; ele monta decisão.

Separações obrigatórias:

- Pareto = tráfego pago/ads.
- FHITS = influencers.
- LK Growth = SEO/CRO/GEO/conteúdo/coleções.
- Lucas = decisão final quando houver write, campanha, preço, orçamento ou marca.

Para campanhas:

- validar fonte de segmento;
- separar WhatsApp, Klaviyo, Meta, Shopify e conteúdo;
- gerar preview e risco;
- bloquear envio até aprovação explícita.

### 5.8 Pulso Comercial e Briefs

Rotinas conhecidas:

- Daily Sales Brief;
- Weekly CEO Review;
- Pulso Comercial 16h;
- relatório 09h dia anterior;
- fechamento loja física 19h30;
- GMC review;
- catalog badges sync;
- LK WhatsApp Hermes responder watchdog;
- Tiny stock local DB fullsync/event refresh, conforme estado vivo.

O Mordomo deve:

- reconciliar cron vivo antes de afirmar status;
- não duplicar cron antigo;
- separar sucesso silencioso de exceção;
- não mandar recibo técnico de sucesso ao Lucas;
- transformar P0/P1 em action surface quando necessário.

### 5.9 Data Quality Guardian

Responsável por impedir decisão com dado ruim.

Flags exemplos:

- `needs_tiny_stock_truth`;
- `blocked_missing_sku`;
- `needs_sku_alias_review`;
- `ready_basic_variant_layer`;
- `divergent_shopify_tiny`;
- `stale_snapshot`;
- `platform_signal_only`;
- `missing_source_of_truth`.

Regra: se a fonte estiver stale, dizer que é validação de formato, não status vivo.

### 5.10 Learning Loop

Toda correção recorrente de Lucas vira:

- Brain doc na área LK/Operações;
- patch de skill quando operacional;
- teste/fixture quando houver script;
- ajuste de alerta para não repetir ruído;
- regra de aprovação/autonomia quando aplicável.

## 6. Matriz de autonomia

### A0 — Livre

- Ler Brain/relatórios locais.
- Consultar fonte read-only.
- Criar relatório interno.
- Criar/atualizar Brain doc.
- Rodar health check/local audit.
- Preparar preview/approval packet.

### A1 — Autonomia segura

- Silenciar ruído óbvio.
- Consolidar digest.
- Responder em grupos internos aprovados quando mencionado, com dado agregado e fonte, se o PRD do grupo estiver ativo.
- Confirmar follow-up logístico neutro com contato validado, se a classe estiver aprovada e sem negociação.
- Atualizar filas locais/CRM interno.

### A2 — Cuidado, mas pode preparar

- Recomendações de estoque/recompra.
- Segmentos de CRM/Klaviyo.
- Sugestões de campanha/conteúdo.
- Drafts internos para equipe.
- Recomendações de sourcing.

### A3 — Aprovação obrigatória

- WhatsApp/e-mail a cliente/fornecedor.
- Campanha Klaviyo/Meta/WhatsApp.
- Desconto/preço/condição.
- Compra/reposição/fornecedor.
- Alteração Shopify/Tiny/GMC/Merchant/Notion/n8n.
- Publicação de tema/cópia em produção.
- Exportação de audiência.

### A4 — Bloqueio até plano explícito

- Produção/infra/deploy sem rollback.
- Apagar dados.
- Expor segredos.
- Mudança massiva de catálogo/preço/estoque.
- Automação nova de envio externo sem kill switch/cadência/preview.

## 7. Estado conhecido hoje

### Já existe / parcialmente existe

- PRD LK OS e plano mestre de implementação.
- Data Spine read-only iniciado.
- Data Quality Layer local materializado com tabelas derivadas.
- Daily Sales Brief e Weekly CEO Review.
- Pulso Comercial 16h como contrato/template já criado, próximo trabalho é operacionalizar/reconciliar, não inventar do zero.
- Stock/Sourcing decision fields e fila de execução Júlio.
- Separação Pareto/FHITS registrada.
- Growth OS ativo com SEO/CRO/GEO e coleções.
- Mission Control como superfície canônica planejada/ativa.
- Hermes nos grupos LK Team/LK Atendimento aprovado em escopo controlado.
- Inventário de crons/agentes com LK OS ativo e LK Growth separado.

### Gaps principais

- Consolidar LK Mordomo OS como camada única de decisão/action inbox.
- Reconciliar crons vivos vs documentação antiga antes de prometer cobertura.
- Melhorar fonte viva Tiny/stock truth e freshness.
- Transformar P0/P1 de relatórios em action packets consistentes.
- Unificar CRM/RFM/recompra com aprovação de canal.
- Deixar Mission Control refletindo filas reais, não só cards estáticos.
- Definir quais alertas vão Telegram, digest, local ou grupo LK.
- Criar testes/fixtures para false positives de WhatsApp interno LK.

## 8. MVP proposto

### MVP 1 — LK Mordomo Command Center local

Entregáveis:

1. `lk_mordomo_os_state.json` ou tabela local equivalente com filas: decisions, approvals, followups, blocked, receipts.
2. Router de sinais LK com saída padronizada.
3. Digest curto para Lucas apenas com decisões/exceções.
4. Relatório local completo para auditoria.
5. Brain doc atualizado automaticamente por decisões duráveis.

### MVP 2 — Decision Inbox LK

Entregáveis:

1. Action packets com campos padronizados.
2. Deduplicação de alertas vindos de crons diferentes.
3. Botões/ações: Aprovar preview, Rascunhar, Ignorar, Lembrar, Silenciar fonte.
4. Aprendizado por resposta de Lucas.

### MVP 3 — CRM/Recompra Mordomo

Entregáveis:

1. Lista de oportunidades RFM/recompra com fonte e risco.
2. Preview de Klaviyo/WhatsApp/e-mail sem envio.
3. Supressões/guardrails por cliente/canal.
4. Feedback loop de outcomes.

### MVP 4 — LK Internal WhatsApp Assistant

Entregáveis:

1. Respostas seguras nos grupos aprovados quando mencionado.
2. Fonte/janela em toda resposta.
3. Fail-closed para dado incerto.
4. Supressão de grupos/logística ruidosa.

### MVP 5 — Mission Control bridge

Entregáveis:

1. Dashboard de filas reais.
2. Botões de aprovação conectados ao Approval Manager.
3. Estado visível: feito, pendente, bloqueado, aprovado, aguardando fonte.
4. Sem external write por padrão.

## 9. Critérios de aceite

O LK Mordomo OS está funcionando quando:

- Lucas recebe menos ruído e mais decisões claras.
- Todo alerta tem recomendação e próximo passo.
- Nenhum envio externo ocorre sem aprovação ou classe estreita aprovada.
- Toda ação sensível tem fonte, preview, risco e rollback quando aplicável.
- Toda correção recorrente vira Brain/skill/fixture.
- Relatórios e crons não duplicam alertas.
- Dados stale são rotulados como stale.
- Shopify/Tiny/GA4/Meta/Klaviyo não são confundidos entre si.
- Pareto/FHITS/Growth/LK operação não são misturados.

## 10. Próximo bloco seguro

Criar uma primeira versão local do **LK Mordomo Decision Inbox** sem envio externo e sem write produtivo:

1. ler inventário de crons LK e últimos reports;
2. normalizar sinais em action packets;
3. gerar um relatório local com 3 seções: decisões Lucas, tarefas equipe, silêncio/receipts;
4. não enviar WhatsApp/e-mail/campanha;
5. entregar para Lucas um preview curto e ajustar a taxonomia.

## 11. Não ações executadas agora

Este documento não:

- criou cron;
- enviou WhatsApp/e-mail;
- alterou Shopify/Tiny/Klaviyo/Meta/Google/Notion;
- consultou ou expôs segredo;
- implantou Mission Control;
- ativou nova automação externa.

## 12. Referências consultadas

- `areas/lk/projetos/lk-operating-system-prd.md`
- `areas/lk/projetos/lk-os-implementation-control.md`
- `areas/lk/projetos/lk-whatsapp-hermes-team-atendimento-prd-2026-05-17.md`
- `areas/MAPA.md`
- `areas/operacoes/inventarios/crons-agentes-profiles.md`
- Skill `multiempresa-routing-lucas`
- Skill `lk-operational-intelligence`
- Skill `superpowers`
- Skill `writing-plans`
