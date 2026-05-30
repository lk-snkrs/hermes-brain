# Rotina — Data Boundaries e Resumos Autorizados

## Objetivo

Formalizar duas regras aprendidas no ciclo Pixel AI Hub/Brainzinho:

1. **Hermes Brain/Git guarda conhecimento estável**: decisões, contexto, processos, rotinas, PRDs, templates, permissões e aprendizados.
2. **Dados vivos ficam nas fontes vivas**: bancos, APIs, dashboards, sistemas de pedido, estoque, campanha, WhatsApp, e-mail, GitHub/runtime e logs.

A rotina também define o padrão **hub-and-spoke multiempresa**: agentes/áreas de LK, Zipper e SPITI produzem artefatos executivos autorizados para o Hermes Geral/Mission Control, em vez de compartilhar o cérebro inteiro, banco inteiro ou histórico bruto por conveniência.

## Quando usar

Usar antes de:

- escrever número operacional no Brain;
- transformar consulta de banco/API em relatório versionado;
- criar painel ou card de Mission Control;
- consolidar aprendizado de LK, Zipper ou SPITI no contexto global;
- passar informação de um agente/especialista para o Hermes Geral;
- desenhar integração entre agentes, subagentes, crons, bots ou sistemas multiempresa.

## Regra 1 — Git/Markdown para conhecimento; API/banco para dado vivo

O Brain pode guardar:

- definição de fonte de verdade;
- query/endpoint/caminho usado para consultar;
- regras de interpretação;
- decisões tomadas;
- aprendizados permanentes;
- templates e checklists;
- reports datados quando forem snapshots explícitos, com `generated_at`, fonte e ressalvas.

O Brain **não** deve virar banco paralelo de:

- pedidos, clientes, estoque, margem, faturamento, CAC, ROAS, lances, campanhas, preço atual ou status operacional contínuo;
- dumps de tabelas, listas completas de clientes, dados pessoais ou dados financeiros sensíveis;
- respostas brutas de APIs, WhatsApp/e-mail ou logs extensos.

Quando houver número ou status atual, usar a fórmula:

```text
Fato verificado na fonte viva → interpretação → recomendação → aprovação/ação necessária
```

E declarar a fonte:

```text
Fonte viva: Shopify / Tiny / Supabase / GA4 / GSC / Meta / Metricool / Klaviyo / WhatsApp / e-mail / GitHub / runtime / outro
Gerado em: YYYY-MM-DD HH:MM TZ
Limite: snapshot datado; não substitui consulta atual
```

## Regra 2 — Hub-and-spoke multiempresa

O Hermes Geral é o hub/orquestrador. LK, Zipper e SPITI são spokes com contexto, fontes, permissões e riscos próprios.

### Permitido por padrão

- O agente/área especialista prepara **resumo executivo autorizado** para o Hermes Geral.
- O Hermes Geral usa o resumo para priorização, decisão, aprovação e roteamento.
- Mission Control mostra síntese, status, decisão pendente, risco e link para fonte/artefato — não dados brutos sensíveis.
- Aprendizados reutilizáveis sobem para `empresa/`, `seguranca/`, `skills/` ou `areas/operacoes/` quando forem gerais.

### Não permitido por conveniência

- Agente de uma empresa ler banco/CRM/WhatsApp bruto de outra sem escopo explícito.
- Misturar Supabase LK, Zipper Vendas e SPITI/Zipper CRM no mesmo relatório sem justificar fonte, finalidade e limite.
- Copiar lista bruta de cliente/colecionador/pedido/lance para `memories/` ou docs globais.
- Fazer Mission Control depender de dump sensível quando bastaria um indicador ou resumo.
- Usar o Brain como atalho para evitar consultar fonte viva.

## Template de resumo autorizado

```md
# Resumo autorizado — [empresa/área] — YYYY-MM-DD

- Dono: LK / Zipper / SPITI / Operações / Tecnologia / Governança
- Fonte viva consultada: [sistema/tabela/API/log]
- Snapshot gerado em: [data/hora/TZ]
- Escopo autorizado: [o que pode ser compartilhado com Hermes Geral/Mission Control]
- Dados omitidos: [PII, cliente, valor sensível, logs brutos, credenciais]

## Fatos
- [fato verificado, sem extrapolação]

## Interpretação
- [leitura executiva]

## Recomendação
- [próxima ação segura]

## Aprovação necessária
- [sim/não; escopo exato]

## Limites
- Snapshot datado; não substitui nova consulta à fonte viva.
```

## Aplicação por empresa

### LK Sneakers

- Fonte viva de vendas/clientes/catálogo: Shopify e/ou camada analítica aprovada.
- Fonte viva de estoque: Tiny `LK controle de stock`; Shopify stock é sinal secundário e pode ser inconsistente.
- Meta/Metricool/GA4/GSC/GMC/Klaviyo são sinais próprios; não misturar métrica de mídia com venda sem ponte documentada.
- Relatórios globais devem esconder PII e separar `fact_shopify`, `fact_tiny`, `fact_ga4`, `fact_meta` e recomendação.

### Zipper Galeria

- Zipper Vendas real: Supabase `pcstqxpdzibheuopjkas`, tabela `vendas_tango`.
- SPITI/Zipper CRM: Supabase `rmdugdkantdydivgnimb`, apenas quando o escopo for CRM/leilão/relacionamento compatível.
- Nunca afirmar performance de artista/obra sem consultar histórico correto.
- Resumo ao Hermes Geral deve separar vendas reais, relacionamento, feira, comunicação e aprovação Lucas/Osmar.

### SPITI Auction

- Email é fonte de verdade para total de lances quando houver divergência.
- Site pode mostrar destaques; meta tag é preço base, não lance atual.
- Resumo global deve trazer confiança, fonte e ressalva; silêncio é melhor que dado errado.

## Mission Control

Mission Control deve exibir:

- síntese executiva;
- status de decisão;
- risco e aprovação necessária;
- timestamp da fonte;
- link para report/artefato autorizado.

Mission Control não deve exibir por padrão:

- dumps de clientes/colecionadores/pedidos/lances;
- tokens, logs extensos ou credenciais;
- dados brutos de uma empresa para outra;
- número operacional sem timestamp/fonte.

## Verificação

Antes de concluir uma mudança que use esta rotina:

1. A fonte viva foi declarada?
2. O Brain recebeu só conhecimento/snapshot datado, não banco paralelo?
3. O resumo autorizado omitiu PII e dados sensíveis desnecessários?
4. LK, Zipper e SPITI continuam separados?
5. Mission Control recebeu síntese, não dump bruto?
6. A ação externa/produção/banco/infra continua bloqueada sem aprovação?

## Não mudanças

Esta rotina não cria cron, bot, agente novo, integração nova, painel runtime ou automação. É uma regra documental/governança para orientar relatórios, Mission Control e handoffs entre agentes.
