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
