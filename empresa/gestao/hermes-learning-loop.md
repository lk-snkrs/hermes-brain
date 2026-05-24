# Hermes Learning Loop — Approval & Correction Intelligence

Status: aprovado conceitualmente por Lucas em 2026-05-09.
Escopo: regra global para Hermes Brain, LK, Zipper, SPITI, Mission Control, agentes, skills, rotinas e PRDs.

## Objetivo

Registrar aprovações, correções, rejeições, decisões, padrões e anti-padrões para que o Hermes aprenda com Lucas e não repita correções já feitas.

Problema a evitar:

```text
Hermes sugere
Lucas corrige
Hermes melhora apenas naquela resposta
Na próxima execução Hermes esquece
Lucas precisa corrigir de novo
```

Comportamento esperado:

```text
Hermes sugere
Lucas aprova/corrige/rejeita
Hermes classifica o feedback
Hermes registra no lugar correto
Hermes atualiza PRD/rotina/skill/memória quando necessário
Próxima execução já nasce melhor
```

## Escopo global

Este loop vale para:

- LK Sneakers;
- Zipper Galeria;
- SPITI Auction;
- Hermes Geral / Lucas Chief of Staff;
- Mission Control;
- agentes e subagentes;
- skills;
- rotinas;
- PRDs;
- reports;
- campanhas/conteúdo;
- aprovações operacionais.

## Regra global de decisão por etapas

Quando um cron, rotina, agente, Mission Control, Mesa COO ou qualquer sistema do Hermes precisar perguntar a Lucas o que fazer, o padrão aprovado é:

- dividir em etapas sequenciais (`1/N`), sem blocão;
- pedir uma decisão por vez;
- usar botões no Telegram quando possível;
- opções padrão: **Fazer**, **Não fazer**, **Agendar para depois**, **Outro / comentar**;
- quando Lucas escolher **Outro**, capturar o comentário escrito como instrução específica do que deve ser feito;
- só avançar para a próxima etapa depois da aprovação/rejeição/agendamento/comentário da etapa atual.

Esta regra vale para decisões de cron e governança em geral, não apenas para a Mesa COO.

## Tipos de feedback

### Aprovação

Lucas aprovou uma direção, formato, raciocínio, copy, report, PRD, arquitetura ou ação preparada.

Registrar:

- o que foi aprovado;
- por que funcionou;
- padrão reutilizável;
- onde aplicar de novo.

### Correção

Lucas corrigiu um erro factual, lógica, nome, fonte, canal, regra, tom ou processo.

Registrar:

- o que Hermes havia entendido/sugerido;
- o que estava errado;
- correção de Lucas;
- nova regra;
- artefatos afetados.

### Rejeição

Lucas rejeitou uma proposta, automação, formato ou direção.

Registrar:

- proposta rejeitada;
- motivo;
- anti-padrão;
- alternativa preferida.

### Padrão aprovado

Algo ficou bom e deve ser repetido.

Registrar:

- artefato;
- características;
- contexto;
- regra de repetição.

### Anti-padrão

Algo ficou ruim ou gerou trabalho desnecessário.

Registrar:

- problema;
- por que é ruim;
- como evitar;
- onde não aplicar.

## Classificação antes de registrar

Todo feedback relevante deve ser classificado como um ou mais:

- preferência pessoal de Lucas;
- regra de negócio;
- regra de execução;
- dado factual;
- decisão permanente;
- anti-padrão;
- melhoria de skill;
- atualização de PRD;
- pendência futura;
- lição aprendida.

## Destino correto

### Memória permanente do agente

Usar quando for compacto, global e recorrente.

Exemplo: “Lucas quer learning loop global para registrar aprovações e correções.”

### Hermes Brain

Usar para regras duráveis e detalhadas.

Destinos:

- `empresa/gestao/hermes-learning-loop.md` — regra global do loop;
- `memories/decisions.md` — decisões permanentes;
- `memories/lessons.md` — lições duráveis;
- `empresa/gestao/pendencias.md` — ações futuras;
- `areas/[empresa]/contexto/lessons.md` — aprendizado por empresa;
- PRDs/projetos afetados.

### Skills

Atualizar quando o feedback muda um procedimento repetível.

Regra:

> Se Lucas corrigiu algo que vai se repetir, não basta responder “ok”. Atualizar Brain, skill, PRD ou memória conforme o caso.

## Template de registro

```text
Feedback ID:
Data:
Área: LK / Zipper / SPITI / Hermes Global / Operações
Artefato:
Tipo: aprovação / correção / rejeição / padrão / anti-padrão / decisão
Resumo:
Antes:
Depois:
Regra aprendida:
Onde aplicar:
Precisa atualizar skill? sim/não
Precisa atualizar PRD? sim/não
Precisa atualizar memória? sim/não
Status:
```

## Exemplos

### LK — correção de compra

```text
Tipo: correção
Antes: Hermes entendeu que pedido de compra iria para Nox.
Depois: destino correto é Notion da LK.
Regra aprendida: recompra aprovada deve criar item no Notion LK, não Nox.
Onde aplicar: LK Operating System, Stock Intelligence Center, Approval Manager.
```

### LK — padrão aprovado

```text
Tipo: padrão aprovado
Padrão: Trend-to-Product-to-Blog.
Regra aprendida: tendência só vira conteúdo forte quando existe produto comprável/sob encomenda com link LK.
Onde aplicar: SEO, Shopify, conteúdo, newsletter, campanhas.
```

### Zipper — tom comercial

```text
Tipo: padrão aprovado
Regra aprendida: abordagem de colecionador deve ser sofisticada, cultural, leve e sem hard sell.
Onde aplicar: Zipper colecionadores, comunicação e vendas de obras.
```

### SPITI — hierarquia de fonte

```text
Tipo: decisão/regra factual
Regra aprendida: email é fonte principal para lances; site pode ser parcial; silêncio é melhor que dado errado.
Onde aplicar: SPITI relatórios, alertas e divergências.
```

### LK — Daily Brief real com GA4

```text
Tipo: padrão aprovado / avanço operacional
Artefato: Daily Sales Brief LK real read-only v0.2 com GA4.
Feedback Lucas: “perfeito, seguir, ficou bacana”.
Regra aprendida: o briefing diário deve combinar Shopify como fonte oficial de pedidos/receita/source, Tiny somente `LK | CONTROLE ESTOQUE` para estoque, e GA4 para sessões/canais/campanhas/CRO, sempre sem PII/secrets e sem ação externa automática.
Onde aplicar: Daily Sales Brief 07h, Pulso Comercial, CRO, Paid Traffic & Influencer Intelligence, Brand Mix Intelligence e Stock Intelligence Center.
Próximo refinamento: cruzar campanhas/influencers/UTMs/cupons com produtos e marcas vendidos no Shopify.
```

### LK — atribuição paga e influencers v0.3

```text
Tipo: avanço operacional / regra de execução
Artefato: LK Paid Attribution Brief real read-only v0.3.
Regra aprendida: performance de influencers/campanhas deve cruzar Meta Ads Insights, GA4 source/medium/campaign e Shopify landing/referrer/cupom/produtos vendidos antes de qualquer recomendação.
Anti-padrão: tratar ROAS/compras do Meta como verdade operacional final ou escalar orçamento por ROAS extremo com gasto muito baixo.
Onde aplicar: Daily Sales Brief 07h, Pulso Comercial, Paid Traffic & Influencer Intelligence, CRO e recomendações de criativo/campanha.
Próximo refinamento: padronizar UTM/cupom por influencer e criar confiança da atribuição: alta/média/baixa.
```

## Regra anti-perda em contexto compactado

Feedback crítico de Lucas em 2026-05-20: decisões aprovadas em chat, especialmente copy/tom/fluxo de contato com cliente, não podem depender da memória temporária da conversa. Compressão/compaction pode preservar o resumo geral e ainda perder o texto exato aprovado ou a razão da aprovação.

Regra operacional:

- Se Lucas aprovar uma mensagem, sequência, tom, oferta, condição, cadência ou fluxo que possa ser enviado para cliente/lead/fornecedor/coletor, registrar imediatamente em artefato durável antes de continuar.
- O registro precisa guardar: texto aprovado ou path do artefato, contexto, canal, destinatário/segmento, status de aprovação, limites de uso, tom aprovado, data e próxima ação permitida.
- Para CRM/carrinho abandonado/Klaviyo/WhatsApp/e-mail, usar um ledger ou arquivo de campanha/fluxo no Brain; não confiar em “foi aprovado acima no chat”.
- Se a conversa for compactada ou retomada depois, consultar o ledger/Brain antes de continuar o fluxo.
- Se não houver registro durável, tratar como aprovação não comprovada: reconstruir preview e pedir confirmação antes de envio externo.

Template mínimo:

```text
Decision ID:
Data:
Área/empresa:
Fluxo/campanha:
Canal:
Segmento/destinatário:
Copy aprovada:
Tom aprovado:
O que Lucas aprovou exatamente:
Limites/guardrails:
Pode enviar agora? sim/não — aprovação atual necessária se externo
Artefato/path:
Status:
```

## Approval UX recomendada

Todo preview operacional deveria permitir, mesmo que manualmente no início:

- aprovar;
- aprovar com ajustes;
- rejeitar;
- registrar como padrão;
- registrar como anti-padrão.

## Verificação

Ao final de uma tarefa complexa, checar:

- houve aprovação ou correção durável?
- alguma skill precisa mudar?
- algum PRD/projeto precisa mudar?
- alguma memória compacta precisa mudar?
- alguma pendência deve ser criada?

## Limites

- Não registrar dados sensíveis, tokens, senhas ou informações pessoais desnecessárias.
- Não transformar log de sessão inteiro em memória permanente.
- Não registrar feedback trivial que não melhora execução futura.
- Não sobrescrever regra de negócio sem evidência ou aprovação explícita.

### Global/Zipper — `/background` não autoriza envio externo

```text
Feedback ID: GLOBAL-EXTERNAL-SEND-20260515-01
Data: 2026-05-15
Área: Global / Zipper / LK OS Approval Manager
Tipo: correção / anti-padrão / regra de execução
Resumo: Lucas corrigiu que uma execução em `/background` enviou e-mail automaticamente para Paulo/Zipper; o correto era gerar um draft.
Antes: Hermes interpretou execução/background como autorização suficiente para enviar a resposta.
Depois: background, seguir ou aprovação ampla de trabalho geram apenas draft/preview para contatos externos.
Regra aprendida: e-mail/WhatsApp/cliente/coletor/fornecedor/campanha só sai com aprovação atual explícita do payload e destinatário nomeado. Se houver erro, preparar mitigação como draft e pedir aprovação antes de novo envio.
Onde aplicar: Google Workspace/Gmail, Mordomo WhatsApp, Zipper atendimento, LK CRM/Klaviyo/WhatsApp, SPITI contatos, Mission Control Approval Manager.
Precisa atualizar skill? sim — google-workspace, multiempresa-routing-lucas, lucas-chief-of-staff.
Precisa atualizar PRD? sim — LK OS Approval Manager + Learning Loop.
Precisa atualizar memória? sim.
Status: registrado_e_skills_patchadas
```

## 2026-05-15 — LK OS Approval Manager v1

Tipo: padrão aprovado + regra de execução.

Lucas aprovou finalizar o Approval Manager como parte do LK OS. O padrão correto é: regras-mestre + ledger auditável + router de aprovação + testes de regressão + superfície no Mission Control. Políticas soltas em Markdown não bastam quando a regra precisa governar ações futuras.

Artefato: `areas/lk/rotinas/lk-os-approval-manager-v1-2026-05-15.md`.
