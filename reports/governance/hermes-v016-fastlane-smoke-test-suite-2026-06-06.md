# Smoke Test Suite — Fast lane / model routing Hermes v0.16

Data: 2026-06-06
Card: `t_171bd02c` — `[R2] Preparar smoke test de fast lane/model routing`
Status: suite documental/local; nenhum modelo, provider, config ou gateway alterado
Owner: Hermes Geral / Operações Hermes
Fonte: `reports/governance/hermes-v016-fastlane-model-routing-prd-2026-06-06.md`

## Objetivo

Preparar uma suite mínima para validar, em fase futura, se o roteamento fast lane é conservador:

- pedidos simples vão para fast lane;
- pedidos profundos/sensíveis continuam no strong lane;
- timeout/non-response gera fallback/cooldown real;
- logs comprovam lane/model selecionado sem secrets;
- runtime só é chamado ativo após restart e evidência de PID/log.

## Regra geral esperada

Fast lane somente se todos forem verdadeiros:

1. pedido curto;
2. baixa ambiguidade;
3. sem produção, dinheiro, cliente, credencial, deploy, Docker, Traefik, banco, Shopify/Tiny write, campanha ou envio externo;
4. não exige muitos arquivos/fontes;
5. erro tem baixo custo e correção fácil.

Strong lane se houver qualquer termo/condição sensível:

- código, bug, debug, PRD, plano, auditoria, SEO, CRO, deploy, Docker, VPS, Traefik, token, secret, webhook, MCP, OIDC, Shopify, Tiny, Klaviyo, Meta, SPITI, lance, lote, cliente, preço, disponibilidade, reclamação, rollback.

## Casos por perfil

### Hermes Geral

Fast candidato:

- “ok, registre que vou ver depois”
- “qual o próximo card pendente?” quando for só leitura curta do board

Strong obrigatório:

- “prepare PRD de mudança no gateway”
- “debugue fallback de provider”
- “mude dashboard/OIDC/Traefik”

Critério: qualquer runtime, segurança, Brain governance ou multiempresa força strong.

### Mordomo

Fast candidato:

- “marque como follow-up simples”
- “resuma esse recado em uma frase”

Strong obrigatório:

- preço, disponibilidade, reserva, negociação, reclamação, fornecedor, bulk, logística, cliente crítico.

Critério: atendimento com impacto externo ou promessa a terceiros força strong.

### LK Ops/Atendimento

Fast candidato:

- classificação de atendimento leve;
- resposta de baixa ambiguidade com fonte já anexada.

Strong obrigatório:

- Tiny/Shopify estoque;
- promessa a cliente;
- reclamação/reembolso/logística;
- bulk/fornecedor.

Critério: qualquer risco de informação operacional errada força strong.

### LK Shopify

Fast candidato:

- readback simples;
- checklist textual de QA sem tocar tema;
- classificação de demanda.

Strong obrigatório:

- theme/cart drawer/app/tracking;
- SEO/metafield write;
- produção, diffs, código, rollback.

Critério: qualquer alteração de loja, tema ou código força strong.

### LK Growth

Fast candidato:

- triagem de pauta;
- resumo curto de relatório já produzido;
- classificação de oportunidade.

Strong obrigatório:

- SEO/GEO strategy;
- conteúdo final;
- análise competitiva;
- ads/CRO/decisão comercial.

Critério: estratégia e publicação final ficam no strong lane.

### LK Collection Optimizer

Fast candidato:

- triagem preliminar de coleção;
- checklist LKGOC sem decisão final.

Strong obrigatório:

- arquitetura de experiência;
- Guia LK;
- visual QA;
- SERP/evidence;
- Shopify handoff.

Critério: qualquer reconstrução de coleção ou handoff comercial força strong.

### SPITI

Fast candidato:

- praticamente nenhum, exceto ack/roteamento administrativo.

Strong obrigatório:

- lote, leilão, bid, valor, oportunidade, análise, risco, publicação, cliente.

Critério: strong por padrão.

## Testes mínimos antes de ativação real

Para cada perfil candidato:

1. **Simple route test**
   - Input: uma solicitação curta e não sensível.
   - Esperado: fast lane selecionado.
   - Evidência: log sanitizado `selected_lane=fast` ou equivalente.

2. **Deep/sensitive route test**
   - Input: solicitação com termo sensível do perfil.
   - Esperado: strong lane selecionado.
   - Evidência: log sanitizado `selected_lane=strong`.

3. **Boundary test**
   - Input: curto, mas contendo risco escondido; ex.: “só confirma disponibilidade para cliente”.
   - Esperado: strong lane.

4. **Fallback test**
   - Input: simulação de timeout/non-response.
   - Esperado: fallback + cooldown, não retry infinito.
   - Evidência: evento sanitizado de fallback.

5. **Post-restart runtime proof**
   - Confirmar PID do profile afetado.
   - Confirmar `HERMES_HOME` correto em `/proc`.
   - Confirmar log pós-restart com configuração ativa.

6. **Telegram round-trip limitado**
   - Só no profile aprovado.
   - Um teste simples e um teste deep.
   - Sem usar clientes reais nem dados sensíveis.

## Critérios de reprovação

- Fast lane responde tarefa que deveria ser strong.
- Log não mostra lane/model selecionado.
- Timeout vira retry indefinido sem fallback/cooldown.
- Same-provider fallback é tratado como proteção contra outage total.
- Config foi alterada mas processo vivo não foi reiniciado/verificado.
- Telegram recebe logs técnicos ou wrappers.

## Próximo approval necessário

Ativação real exige novo packet contendo:

- profiles afetados;
- modelo fast escolhido;
- mudança exata em config/env/código;
- rollback;
- janela de restart;
- testes acima;
- critério para desligar fast lane se qualidade cair.

## Resultado

Card `t_171bd02c` pode ser considerado concluído no escopo aprovado: suite de smoke tests pronta, sem ativação runtime.
