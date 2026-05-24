# PRD — Hermes nos grupos WhatsApp LK Team e LK Atendimento

Data: 2026-05-17  
Owner: Lucas Cimino  
Produto: LK OS / Hermes Agent / wacli WhatsApp  
Status: aprovado por Lucas e ativado em produção controlada (2026-05-17)  
Escopo ativo: responder perguntas sobre LK quando o Hermes for marcado nos grupos `LK Team` e `LK Atendimento`

## 1. Resumo executivo

Conectar o Hermes à operação interna da LK Sneakers via WhatsApp, usando a instância `wacli`/OpenClaw, para responder perguntas quando alguém marcar o Hermes nos grupos **LK Team** e **LK Atendimento**.

O Hermes atuará como **analista operacional interno da LK OS**: responde dúvidas sobre vendas, produtos mais vendidos, visitas no site, performance comercial, estoque/sinais de produto e outras perguntas sobre LK, sempre consultando fontes reais quando necessário e rotulando a data/fonte da informação.

A V1 deve ser segura: responder apenas quando mencionado, nos grupos aprovados, com linguagem objetiva e premium, sem executar ações externas, campanhas, alterações de sistema, descontos, promessas a clientes ou mutações de dados.

## 2. Contexto

Lucas quer que o Hermes deixe de ser apenas um assistente via Telegram e passe a estar presente nos canais internos da LK, especialmente para reduzir dependência manual de Lucas em perguntas operacionais recorrentes.

Casos esperados:

- “Hermes, quanto vendemos hoje?”
- “Hermes, qual produto mais vendeu ontem?”
- “Hermes, como estão as visitas no site?”
- “Hermes, qual marca está puxando o mês?”
- “Hermes, a loja física vendeu quanto hoje?”
- “Hermes, o que mais saiu na semana?”
- “Hermes, temos algum alerta de produto/estoque?”

## 3. Problema

Hoje, perguntas simples sobre a LK dependem de alguém abrir Shopify, GA4, relatórios, planilhas ou pedir para Lucas/Hermes no Telegram. Isso cria atraso, retrabalho e perda de autonomia da equipe.

Ao mesmo tempo, deixar um agente responder em WhatsApp sem escopo claro pode gerar riscos:

- resposta com dado errado ou desatualizado;
- exposição de dado sensível;
- confusão entre venda real, tráfego, campanha, estoque e hipótese;
- resposta para cliente como se fosse atendimento oficial;
- tomada de decisão comercial sem aprovação;
- excesso de mensagens no grupo.

## 4. Objetivo

Permitir que o Hermes responda perguntas operacionais da LK nos grupos aprovados, quando marcado, com respostas rápidas, úteis, verificáveis e seguras.

Objetivos V1:

1. Monitorar apenas os grupos aprovados: `LK Team` e `LK Atendimento`.
2. Responder apenas quando o Hermes for explicitamente mencionado, marcado ou quando uma mensagem responder diretamente a uma mensagem do Hermes.
3. Responder perguntas sobre LK usando fontes de verdade read-only.
4. Identificar claramente fonte e janela temporal dos dados.
5. Nunca executar ação externa/produtiva sem aprovação explícita de Lucas.
6. Registrar aprendizados duráveis sobre decisões de operação LK na memória/Brain da LK.

## 5. Não objetivos V1

A V1 não deve:

- responder qualquer grupo fora de `LK Team` e `LK Atendimento`;
- monitorar ou responder conversas privadas automaticamente;
- iniciar conversa sem menção;
- enviar campanha, oferta, cupom, desconto ou mensagem para cliente;
- alterar Shopify, Tiny, Supabase, Meta, Google, Klaviyo, site, estoque ou preço;
- prometer disponibilidade, prazo, reserva, troca ou condição comercial a cliente;
- responder perguntas pessoais/sensíveis de clientes;
- expor PII, telefone, e-mail, endereço, CPF, pedido individual ou dados financeiros sensíveis no grupo;
- substituir aprovação de Lucas para decisão estratégica, compra, campanha, desconto, preço ou comunicação externa.

## 6. Usuários

### Primário

- Equipe LK nos grupos `LK Team` e `LK Atendimento`.

### Secundário

- Lucas, como aprovador e dono da operação.
- Hermes/LK OS, como camada de inteligência operacional.

## 7. Escopo de grupos e conta WhatsApp

### Conta wacli

Conta preferencial:

- `hermes` — número/conta do Hermes para atuar como bot/analista nos grupos LK.

Alternativa apenas se Lucas aprovar explicitamente:

- outra conta LK Business dedicada ao Hermes.

Não usar por padrão:

- `pessoal` — WhatsApp pessoal de Lucas;
- contas Zipper/SPITI;
- `lk-compras`, se o escopo for atendimento/equipe geral e não compras.

### Grupos aprovados V1

- `LK Team`
- `LK Atendimento`

Antes da ativação, o Hermes deve resolver e registrar os IDs/JIDs dos grupos de forma local/sanitizada, sem publicar JIDs completos em Telegram/Brain se não for necessário.

## 8. Gatilhos de resposta

O Hermes só responde quando:

1. A mensagem menciona explicitamente o Hermes: `Hermes`, `@Hermes`, `hermes`, ou alias aprovado.
2. A mensagem é uma resposta/reply a uma mensagem enviada pelo Hermes no grupo.
3. Lucas autoriza manualmente uma resposta específica no Telegram, se a mensagem não tiver menção clara.

O Hermes não deve responder:

- a toda pergunta genérica no grupo;
- a conversa entre membros sem menção;
- a mensagens emocionais/ruído/social;
- a pedidos que não sejam sobre LK;
- a pedidos ambíguos que possam causar ação externa.

## 9. Categorias de perguntas permitidas

### 9.1 Vendas

Pode responder:

- vendas de hoje, ontem, semana, mês;
- total vendido;
- pedidos/vendas;
- ticket médio;
- online vs loja física/POS;
- ranking de vendedores quando houver atribuição POS confiável;
- comparativo com período anterior quando janela for equivalente.

Fonte preferencial:

- Shopify Orders/Admin read-only;
- relatórios LK OS gerados;
- Data Spine local quando disponível.

### 9.2 Produtos e marcas

Pode responder:

- produtos mais vendidos;
- marcas que mais vendem;
- tamanhos/SKUs mais vendidos quando confiáveis;
- share mensal de marcas por receita e BRL;
- itens sem giro relevante;
- alertas de ruptura/baixo estoque quando fonte estiver validada.

Fonte preferencial:

- Shopify/Tiny read-only;
- rotinas LK OS;
- relatórios de vendas LK.

### 9.3 Site e tráfego

Pode responder:

- visitas/sessões do site;
- usuários;
- conversão;
- canais principais;
- páginas/produtos com tráfego relevante;
- queda/subida visível quando dado for confiável.

Fonte preferencial:

- GA4 read-only;
- GSC para busca orgânica;
- Metricool/Meta/Google Ads apenas como contexto, não como faturamento.

### 9.4 Atendimento e operação

Pode responder:

- status agregado de pedidos ou operação, sem PII;
- perguntas internas sobre regras já documentadas da LK;
- orientações operacionais do tipo “onde ver X”, “qual relatório usar”, “qual fonte manda”.

Deve escalar para Lucas:

- reclamação sensível;
- pedido individual de cliente;
- troca/devolução fora do padrão;
- desconto/preço especial;
- conflito de informação;
- pergunta sem fonte de verdade clara.

## 10. Matriz de autonomia

### A0 — Livre / read-only sem resposta externa

- Verificar auth/status wacli.
- Resolver grupos localmente.
- Testar parser em logs locais.
- Consultar dados read-only para preparar resposta.
- Registrar logs sanitizados.

### A1 — Resposta automática permitida nos grupos aprovados, se mencionado

Permitido após aprovação deste PRD e implementação validada:

- responder perguntas objetivas sobre LK com dados agregados;
- citar fonte e janela temporal;
- responder “não consigo confirmar agora” quando a fonte falhar;
- orientar qual relatório/fonte consultar.

### A2 — Resposta com cuidado / pode responder, mas deve ser conservador

- análises comparativas incompletas;
- rankings com amostra pequena;
- alertas de estoque com divergência Tiny/Shopify;
- performance de vendedor quando atribuição estiver parcial;
- tráfego/site quando a janela do GA4 ainda estiver sujeita a atraso.

Resposta deve incluir ressalva de confiabilidade.

### A3 — Preparar e pedir aprovação a Lucas

- resposta que envolve cliente específico;
- recomendações comerciais fortes;
- sugestão de campanha;
- desconto/cupom/preço;
- decisão de compra/reposição;
- qualquer resposta que possa comprometer margem, relação com cliente ou reputação.

### A4 — Bloqueado

- enviar WhatsApp para cliente/fornecedor fora dos grupos aprovados;
- responder como atendimento oficial a cliente externo;
- alterar estoque/preço/produto/pedido;
- criar campanha ou disparo;
- expor dados pessoais;
- prometer reserva, entrega, troca, desconto ou disponibilidade;
- responder sobre Zipper/SPITI/pessoal em grupo LK.

## 11. Fontes de verdade e hierarquia

### Faturamento/vendas

1. Shopify Orders/Admin read-only.
2. Data Spine/relatórios LK OS derivados do Shopify.
3. Tiny apenas para sanity de SKU/estoque, não como fonte primária de faturamento.

### Loja física/POS

1. Shopify POS/source/tags quando confiáveis.
2. Campo de vendedor/staff somente se validado.
3. Se não houver atribuição confiável, responder total da loja e informar que vendedor está indisponível ou parcial.

### Estoque/produtos

1. Para perguntas de disponibilidade por produto/SKU/tamanho no WhatsApp, a V1 usa Tiny read-only como fonte primária operacional: `produtos.pesquisa`, `produto.obter` para variações e `produto.obter.estoque`.
2. O depósito oficial para responder “tem/não tem” é `LK | CONTROLE ESTOQUE`.
3. Se houver saldo em `LK FISCAL`, consignação, encomendas ou outro depósito, mas zero em `LK | CONTROLE ESTOQUE`, responder como **não disponível no Controle Estoque** e citar o saldo externo como pendente de validação operacional; não prometer ao cliente.
4. Exemplos cobertos: `Tem New Balance 9060 Moonbeam tamanho 38?`, `Tem U9060WHT 38?`, `Quais New Balance 9060 tem no 38?`.
5. Shopify + Tiny reconciliados continuam preferíveis para decisões comerciais amplas; se divergirem, explicitar divergência e não afirmar disponibilidade sem checagem.

### Site/tráfego

1. GA4 para tráfego/conversão.
2. GSC para orgânico/search.
3. Meta/Google Ads/Metricool para contexto de mídia, não para receita real.

## 12. Padrão de resposta no WhatsApp

Resposta deve ser curta, útil e com fonte.

Formato recomendado:

```text
Hermes · LK OS

[Resposta direta em 1–3 linhas]

Janela: [hoje até HHh / ontem / mês até hoje]
Fonte: [Shopify / GA4 / relatório LK OS]
Obs.: [ressalva curta se houver]
```

Exemplo — vendas:

```text
Hermes · LK OS

Hoje até 16h, a LK vendeu R$ X em Y pedidos. Loja física: R$ A. Online: R$ B. Ticket médio: R$ Z.

Janela: hoje até 16h BRT
Fonte: Shopify read-only
```

Exemplo — sem confirmação:

```text
Hermes · LK OS

Não vou cravar esse número agora: a fonte de visitas ainda não respondeu/está atrasada. Posso confirmar pelo GA4 e retorno quando tiver dado confiável.

Fonte esperada: GA4
```

## 13. Tom de voz

- Premium, direto, útil.
- Sem “coach”, sem euforia, sem emoji excessivo.
- Comercial, mas não vendedor barato.
- Nunca inventar número.
- Separar fato, interpretação e recomendação quando houver análise.
- Se a pergunta for de atendimento externo, ser prudente e escalar.

## 14. Privacidade e dados sensíveis

O Hermes pode responder dados agregados da operação, mas não deve publicar no grupo:

- nome/telefone/e-mail/endereço de cliente;
- CPF/documento;
- dados de pagamento;
- detalhes de pedido individual;
- print bruto de conversa;
- IDs internos desnecessários;
- tokens, URLs privadas, chaves ou secrets;
- JIDs completos dos grupos/contatos.

Para pergunta sobre pedido/cliente específico, o Hermes deve responder internamente algo como:

```text
Posso ajudar, mas não vou expor dados do cliente no grupo. Me mandem o identificador internamente no canal correto ou peçam ao Lucas para autorizar a consulta específica.
```

## 15. Arquitetura proposta

### Componentes

1. **wacli listener/poller**
   - Conta: `hermes`.
   - Escopo: grupos aprovados.
   - Detecta novas mensagens e menções.

2. **Router LK OS**
   - Classifica pergunta: vendas, produto, marca, site, estoque, atendimento, outra.
   - Bloqueia fora de escopo.

3. **Data fetchers read-only**
   - Shopify/Tiny/GA4/GSC/relatórios locais, conforme pergunta.
   - Timeout curto e fallback conservador.

4. **Response composer**
   - Gera resposta curta em padrão LK.
   - Inclui janela/fonte/ressalva.

5. **Send guard**
   - Só envia se: grupo aprovado + menção + categoria permitida + sem PII + sem ação externa proibida.
   - Log sanitizado.

6. **Audit log local**
   - Registra hash da mensagem, grupo lógico, categoria, resposta enviada, fonte, timestamp e status.
   - Não versionar mensagens brutas no Brain.

## 16. Estado e logs

Persistir localmente, fora do Brain público:

- último timestamp processado por grupo;
- IDs/hash de mensagens respondidas para evitar duplicidade;
- categoria classificada;
- resposta enviada;
- fonte usada;
- erros/falhas.

Não persistir no Brain:

- conteúdo bruto de conversas;
- PII de clientes;
- JIDs completos se não necessário;
- tokens/secrets.

No Brain, registrar apenas:

- PRD;
- rotina operacional;
- decisões aprovadas;
- guardrails;
- aprendizados duráveis sem PII.

## 17. Fases de implementação

### Fase 0 — Aprovação do PRD

Lucas aprova, ajusta ou bloqueia este escopo.

### Fase 1 — Descoberta read-only

- Verificar conta `hermes` no wacli.
- Se não estiver conectada, preparar QR/pairing para Lucas conectar.
- Listar grupos localmente e identificar `LK Team` e `LK Atendimento`.
- Não ler conteúdo em escala ainda; apenas metadata mínima para resolver grupo.

### Fase 2 — Dry-run sem envio

- Ler mensagens novas dos grupos aprovados em janela curta.
- Detectar menções ao Hermes.
- Classificar perguntas.
- Gerar resposta candidata, mas enviar para Lucas no Telegram como preview.
- Nenhuma resposta no WhatsApp.

### Fase 3 — Piloto interno com envio automático limitado

Após Lucas aprovar dry-run:

- ativar resposta automática apenas para A1/A2;
- grupos: `LK Team` e `LK Atendimento`;
- gatilho: menção explícita;
- horário inicial sugerido: comercial, 08h–20h BRT;
- limite de rate: máximo 1 resposta por thread/mensagem e cooldown por grupo.

### Fase 4 — Expansão controlada

Somente após 7 dias sem incidente:

- ajustar categorias;
- ampliar horários, se fizer sentido;
- adicionar comandos internos como `Hermes resumo de hoje`, `Hermes top produtos`, `Hermes visitas do site`;
- considerar respostas mais analíticas, ainda sem ações externas.

## 18. Critérios de aceite

Antes de ativar envio automático:

- [ ] Lucas aprovou este PRD.
- [ ] Conta wacli `hermes` autenticada e verificada.
- [ ] IDs dos grupos aprovados resolvidos localmente.
- [ ] Dry-run demonstrou detecção correta de menções.
- [ ] Dry-run gerou respostas com fonte e janela temporal.
- [ ] Teste bloqueou PII e pedidos fora de escopo.
- [ ] Teste bloqueou ações A3/A4.
- [ ] Log local sanitizado criado.
- [ ] Health/secret scan do Brain passou se houver alteração no repo.
- [ ] Lucas aprovou início do piloto com envio automático limitado.

## 19. Métricas de sucesso

- Tempo médio de resposta a perguntas internas.
- % de respostas com fonte e janela claras.
- Nº de escalonamentos corretos para Lucas.
- Nº de bloqueios corretos de pedidos fora de escopo.
- Incidentes de dado errado/PII/envio indevido: meta zero.
- Feedback qualitativo da equipe LK.

## 20. Riscos e mitigação

### Risco: dado errado no grupo

Mitigação: sempre buscar fonte read-only, incluir janela/fonte, responder “não consigo confirmar” quando houver falha.

### Risco: Hermes responder conversa sem ser chamado

Mitigação: gatilho por menção/reply; cooldown e deduplicação.

### Risco: PII ou pedido individual exposto

Mitigação: filtro de PII, regra de dados agregados, bloqueio de pedido/cliente específico.

### Risco: ação comercial sem aprovação

Mitigação: matriz A0–A4; descontos/campanhas/preços especiais sempre A3/A4.

### Risco: grupo errado

Mitigação: allowlist por JID resolvido localmente; nomes de grupo não bastam se houver duplicatas.

### Risco: spam

Mitigação: só por menção, cooldown, respostas curtas, horário controlado no piloto.

## 21. Decisões aprovadas por Lucas

Lucas aprovou em 2026-05-17:

1. Usar a conta WhatsApp `hermes`.
2. Ativar nos grupos `[LK] Team` e `LK | Atendimento Online`.
3. Responder automaticamente quando mencionado ou quando responderem uma mensagem do Hermes.
4. Dados agregados de vendas/site e consultas de estoque por produto/tamanho estão liberados para esses grupos.
5. Estoque deve aprender os padrões: `New Balance 9060 Moonbeam tamanho 38`, `U9060WHT 38`, `Quais New Balance 9060 tem no 38?`, usando Tiny e depósito `LK | CONTROLE ESTOQUE`.

## 22. Aprovação realizada

Aprovação registrada no chat Telegram: “Eu aprovo que já responda, pode fazer tudo e executar”.

## 23. Status

- Status atual: `ativo_piloto_controlado`.
- Implementação: `/opt/data/scripts/lk_hermes_whatsapp_responder.py`.
- Watchdog: cron `LK WhatsApp Hermes responder watchdog` (`71b2636add5d`) via `/opt/data/scripts/lk_hermes_whatsapp_watchdog.sh`.
- Wacli: conta `hermes`, sync com webhook local `127.0.0.1:8787/wacli`.
- Grupos ativos: `[LK] Team` e `LK | Atendimento Online`.
- Ação externa executada: mensagens de ativação enviadas aos dois grupos aprovados.
- Guardrail ativo: sem escrita em Tiny/Shopify/Meta/Google/Klaviyo; sem cliente/fornecedor; sem PII; sem promessa de disponibilidade se saldo não estiver no `LK | CONTROLE ESTOQUE`.
- Próxima ação segura: monitorar logs sanitizados e corrigir parser conforme perguntas reais da equipe.
