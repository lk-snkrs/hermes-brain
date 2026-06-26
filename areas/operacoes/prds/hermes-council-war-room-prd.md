# PRD — Hermes Council / War Room Decision Layer

Data: 2026-05-13
Owner: Lucas Cimino
Sistema: Hermes Agent / Hermes Brain / LK-Zipper-SPITI operations
Status: Draft operacional v1

## 1. Contexto

Lucas quer avaliar se faz sentido implementar uma habilidade/metodologia de “council / war room / debate / pressure-test” no Hermes para decisões importantes de LK, Zipper, SPITI e do próprio Hermes.

Fonte: conversa Telegram em 2026-05-13 sobre uma metodologia de council acionável por frases como:

- `council this`
- `run the council`
- `war room this`
- `pressure-test this`
- `debate this`

Relação com o operating model do Lucas: Hermes deve funcionar como COO. Um COO útil não só executa: ele estrutura decisão, antecipa risco, separa tese de evidência, força contraditório e transforma a decisão em ação segura.

## 2. Problema

Hoje decisões estratégicas podem ficar lineares demais:

1. Lucas traz uma ideia ou pergunta.
2. Hermes responde com uma recomendação única.
3. O contraditório, riscos, trade-offs e critérios de decisão ficam implícitos.
4. Quando a decisão envolve várias empresas, canais, risco de marca, dinheiro, produção ou cliente, a resposta pode ser útil mas não suficientemente “COO-grade”.

O problema não é falta de inteligência do modelo; é falta de um ritual explícito para decisões de alto impacto.

## 3. Objetivo

Criar uma camada operacional chamada **Hermes Council** para acionar um debate estruturado, com papéis fixos, evidências, riscos, recomendação final e próximos passos com guardrails.

Objetivo principal: melhorar a qualidade de decisões antes de ações importantes, sem transformar todo pedido simples em burocracia.

## 4. Não objetivos

Nesta fase, o Council não deve:

- virar um SaaS ou interface visual nova;
- instalar dependência externa sem lacuna comprovada;
- executar writes automaticamente;
- aprovar produção, Docker, banco, Merchant, Shopify, campanha, cliente, WhatsApp ou dinheiro por conta própria;
- substituir Lucas em decisões A3/A4;
- rodar em toda tarefa por padrão;
- gerar “teatro de agentes” com personas genéricas e sem evidência.

## 5. Usuários

- **Lucas:** toma decisões melhores e mais rápidas sem precisar pedir manualmente “pense nos riscos”.
- **Hermes Geral:** ganha um modo de raciocínio estruturado para decisões de alto impacto.
- **LK Sneakers:** usa Council para growth, GMC/SEO, CRM, compras, pricing, campanhas, operação e reputação.
- **Zipper Galeria:** usa Council para posicionamento cultural, vendas, comunicação e curadoria.
- **SPITI Auction:** usa Council para risco, CRM, comunicação e processos onde silêncio é melhor que dado errado.
- **Futuro mantenedor:** entende quando acionar Council, quais papéis existem e quais saídas são obrigatórias.

## 6. Decisão Hermes-native

### O que a metodologia ensina

Usar múltiplos pontos de vista para pressão decisória:

- defensor da tese;
- cético/risk officer;
- operador/COO;
- cliente/mercado;
- financeiro;
- jurídico/reputação quando relevante;
- síntese final.

### O que Hermes já faz diferente

Hermes já tem:

- `delegate_task` para subagentes paralelos;
- skills por domínio;
- memória e Brain;
- cron e background;
- guardrails A0–A4 do Lucas;
- PRDs, relatórios e approval packets.

### Decisão

**Adaptar como skill + ritual + templates**, não como novo produto externo nesta fase.

Por quê:

- entrega valor imediato;
- não adiciona risco de infra;
- combina com o Hermes COO Routing Layer;
- permite evoluir depois para subagentes reais quando necessário.

## 7. Princípios de produto

1. **Council é para decisão, não para toda execução.**
2. **Evidência antes de opinião.** Quando houver fonte consultável, Hermes deve buscar; quando não houver, marcar como hipótese.
3. **Contraditório obrigatório.** Toda recomendação precisa passar por uma crítica forte.
4. **Guardrails vencem entusiasmo.** A saída deve dizer o que pode ser feito agora e o que exige aprovação.
5. **Telegram-first.** O resumo precisa caber no contexto do Lucas, com decisão e próximos passos claros.
6. **Sem teatro.** Personas só entram se melhorarem decisão; nada de debate longo sem conclusão operacional.

## 8. Quando acionar

### Acionar automaticamente ou sugerir acionar quando

- decisão afeta dinheiro, marca, cliente, campanha, estoque, produto, preço, reputação, infra ou estratégia;
- há trade-off real entre velocidade e risco;
- Lucas pergunta “faz sentido?”, “qual caminho?”, “vamos implementar?”, “vale a pena?”;
- existem várias áreas envolvidas: LK + Hermes, LK + WhatsApp, Zipper + CRM, SPITI + comunicação;
- uma ação parece reversível tecnicamente, mas tem risco comercial.

### Não acionar quando

- resposta factual simples;
- cálculo/consulta direta;
- correção pequena já aprovada;
- rotina operacional já documentada;
- tarefa A0/A1 de baixo risco sem decisão real.

## 9. Modos do Council

### 9.1 Quick Council

Uso: decisão média, resposta no próprio chat.

Papéis mínimos:

- **Proponente:** melhor argumento a favor.
- **Cético:** melhor argumento contra.
- **COO:** execução, dependências e guardrails.
- **Síntese:** decisão recomendada.

Saída: 5–10 bullets + recomendação.

### 9.2 War Room

Uso: decisão de alto impacto ou com risco A3/A4.

Papéis:

- **CEO/estratégia:** alinhamento com objetivo maior.
- **COO/operação:** caminho executável, dependências, reversibilidade.
- **CFO/unit economics:** margem, custo, upside/downside.
- **Customer/brand:** impacto na percepção do cliente/colecionador.
- **Risk/legal/reputation:** riscos, compliance, dano potencial.
- **Data/evidence:** o que é fato, sinal, hipótese e desconhecido.
- **Red team:** como isso pode dar errado.
- **Decider synthesis:** recomendação final e aprovação necessária.

Saída: decisão estruturada + pacote de aprovação se houver write/externo.

### 9.3 Pressure Test

Uso: Lucas já tem uma tese e quer saber se aguenta.

Saída:

- tese em uma frase;
- premissas;
- premissas frágeis;
- cenários de falha;
- sinais que validariam/refutariam;
- recomendação: seguir / piloto / adiar / rejeitar.

### 9.4 Debate

Uso: duas ou mais opções claras.

Saída:

- critérios de decisão;
- score qualitativo por opção;
- melhor caso de cada opção;
- pior caso de cada opção;
- recomendação e plano de reversão.

## 10. Requisitos funcionais

- **RF1 — Trigger textual:** reconhecer frases como `council this`, `run the council`, `war room this`, `pressure-test this`, `debate this`, e equivalentes em português como `faz um conselho`, `debate isso`, `testa essa tese`, `war room`.
- **RF2 — Seleção de modo:** escolher Quick Council, War Room, Pressure Test ou Debate com base em risco/complexidade.
- **RF3 — Contexto empresarial:** rotear papéis e guardrails conforme LK, Zipper, SPITI, Hermes ou multiempresa.
- **RF4 — Evidência:** buscar dados/fonte quando necessário e seguro; marcar `fato`, `sinal`, `hipótese`, `desconhecido`.
- **RF5 — Red team obrigatório:** incluir crítica forte antes da recomendação.
- **RF6 — Saída operacional:** terminar com recomendação, próximos passos e nível de aprovação A0–A4.
- **RF7 — Approval packet:** se a recomendação exigir ação produtiva, incluir escopo inline para Lucas aprovar, não apenas caminho de arquivo.
- **RF8 — Persistência:** decisões relevantes viram Brain doc/memória/skill quando duráveis.
- **RF9 — Subagentes opcionais:** para War Room pesado, usar `delegate_task` com papéis independentes, mas só quando a complexidade justificar.

## 11. Requisitos não funcionais

- Português por padrão para Lucas.
- Resposta executiva e direta no Telegram.
- Sem inventar dados.
- Segredos via Doppler; nunca valores em docs.
- Sem PII em Telegram quando envolver clientes.
- Separar fato, interpretação e recomendação.
- Guardrails A0–A4 sempre explícitos.
- `possible_secrets 0` antes de commit/PR quando houver alteração no Brain.
- Health check do Brain passando quando o repo for alterado.

## 12. Guardrails e aprovações

Ações permitidas nesta fase sem nova aprovação:

- criar PRD local no Brain;
- criar skill/metodologia local;
- criar templates de saída;
- testar com exemplos simulados;
- abrir PR documental/de baixo risco, se o fluxo do repo exigir.

Ações bloqueadas sem aprovação específica:

- alterar gateway/produção/Docker/Traefik/VPS;
- instalar dependência externa;
- criar cron ou automação que acione Council sozinho;
- enviar WhatsApp/e-mail/campanha/post;
- escrever em Shopify, Merchant, Supabase, Tiny, Klaviyo, Meta/Google;
- expor secrets;
- tomar decisão A3/A4 sem Lucas.

## 13. Arquitetura / arquivos

### Fase v0 — Brain + skill local

Criar/alterar:

- `areas/operacoes/prds/hermes-council-war-room-prd.md`
- skill nova: `hermes-council` em categoria operacional/produtividade, com:
  - quando usar;
  - modos;
  - templates;
  - exemplos LK/Zipper/SPITI/Hermes;
  - guardrails A0–A4.

### Fase v1 — Integração ao COO Routing Layer

Atualizar:

- `areas/operacoes/prds/hermes-coo-routing-layer-prd.md`
- skill/rotina de roteamento COO, se existir, para dizer quando Council entra antes de execução.

### Fase v2 — Subagentes reais, se necessário

Adicionar templates para `delegate_task`:

- red team;
- financial/operator;
- customer/brand;
- legal/risk;
- synthesis.

Somente usar em decisões complexas, não por padrão.

## 14. Plano de implementação

### Fase 0 — PRD

- Criar este PRD.
- Revisar com Lucas.
- Definir se v0 será skill apenas ou skill + alteração no routing layer.

### Fase 1 — Skill v0

- Criar skill `hermes-council`.
- Incluir template Quick Council.
- Incluir template War Room.
- Incluir template Pressure Test.
- Incluir template Debate.
- Incluir exemplos por empresa.

### Fase 2 — Teste controlado

Testar com 3 casos simulados:

1. LK: decisão sobre ampliar piloto de títulos GMC.
2. Zipper: decisão sobre comunicação de lote/artista.
3. Hermes: decisão sobre instalar ou não ferramenta externa.

Critério: a saída precisa gerar decisão melhor que uma resposta normal, sem ficar longa demais.

### Fase 3 — Integração leve

- Atualizar COO Routing Layer para citar Council como rito antes de A3/A4 ou decisões estratégicas.
- Se aprovado, criar frase operacional: “Quando Lucas disser `war room`, carregar skill `hermes-council` e executar o modo War Room.”

### Fase 4 — Evolução futura

- Avaliar subagentes reais para War Room longo.
- Avaliar cron/rotina apenas para revisão estratégica agendada, nunca para decisões produtivas autônomas.

## 15. Critérios de pronto

- [ ] PRD criado.
- [ ] Skill `hermes-council` criada.
- [ ] Templates utilizáveis no Telegram.
- [ ] Exemplos por empresa incluídos.
- [ ] Guardrails A0–A4 explícitos.
- [ ] Teste com 3 casos simulados documentado.
- [ ] Health check Brain OK, se disponível.
- [ ] Secret scan sem achados.
- [ ] Diff revisado.
- [ ] Nenhuma ação externa/produtiva executada.

## 16. Riscos

- Virar burocracia e atrasar decisões simples.
- Gerar personas artificiais sem evidência.
- Aumentar confiança em recomendação errada se os papéis concordarem superficialmente.
- Confundir “Council recomendou” com “Lucas aprovou”.
- Rodar subagentes demais e gastar contexto/tempo sem necessidade.
- Ser usado para justificar ação A3/A4 sem approval packet.

Mitigação: Council sempre termina com nível de risco, evidência, incerteza e aprovação necessária.

## 17. Decisões de Lucas — 2026-05-13

Lucas aprovou a calibragem v1:

1. **Nome oficial:** Hermes Council.
2. **Acionamento:** Hermes deve adicionar/acionar automaticamente quando for relevante, especialmente decisões estratégicas, A3/A4, alto impacto, risco de marca, dinheiro, cliente, produção, infraestrutura, dados ou trade-off real.
3. **Formato Telegram:** aceita a recomendação inicial — resumo executivo curto por padrão; relatório completo apenas quando for War Room ou quando a complexidade justificar.
4. **Papéis fixos:** aprovado — COO/operação, CFO/unit economics, Cliente/Marca, Red Team e Síntese/decisor.
5. **LK Sneakers:** aprovado — sempre separar visão **premium brand** de visão **performance/ROI** em decisões relevantes da LK.

## 18. Recomendação inicial

Implementação v0 concluída e calibrada conforme decisão de Lucas, sem mexer em produção.

Escopo executado:

- PRD criado;
- skill `hermes-council` criada;
- templates incluídos;
- defaults de acionamento e papéis definidos;
- sem dependências externas permanentes;
- sem alteração em gateway/Docker;
- sem cron novo;
- sem ação externa/produtiva.

Próximo passo recomendado:

- Integrar o Hermes Council ao COO Routing Layer como rito automático antes de decisões relevantes/A3/A4 e em perguntas do tipo “faz sentido?”, “vale a pena?”, “vamos implementar?”, mantendo respostas curtas quando bastar.
