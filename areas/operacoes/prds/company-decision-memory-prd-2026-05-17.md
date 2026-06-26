# PRD — Memória de Decisões por Empresa

Data: 2026-05-17  
Status: Aprovado como regra operacional de documentação  
Origem: correção do Lucas após ajustes no relatório LK OS de vendas/WhatsApp/newsletter

## 1. Contexto

Durante a evolução dos relatórios da LK Sneakers, várias decisões de produto/operação foram tomadas em conversa: ordem do relatório, presença de vendedores, share de marcas, subject/preheader e separação do fechamento de loja física. Parte dessas decisões já existia no Brain, mas parte foi registrada apenas depois da cobrança do Lucas.

Lucas corrigiu a regra esperada: **toda decisão tomada sobre uma empresa deve ser salva na memória operacional daquela empresa**, não apenas ficar no histórico do chat ou em um relatório pontual.

## 2. Problema

O histórico da conversa não é uma fonte de verdade operacional suficiente. Se uma decisão fica só no Telegram, em um cron response ou em um arquivo gerado, o Hermes pode:

- repetir perguntas já decididas;
- desfazer uma preferência operacional em execuções futuras;
- tratar uma correção como caso isolado, não como regra;
- misturar decisões entre LK, Zipper, SPITI e Lucas pessoal;
- perder continuidade quando outro agente/subagente assumir a tarefa.

## 3. Objetivo

Criar uma regra de documentação permanente: **decisões empresariais viram memória viva da empresa correspondente**, com referência cruzada quando a decisão também afetar governança global, rotinas ou skills.

## 4. Não objetivos

Nesta fase, este PRD não autoriza:

- envio externo por WhatsApp/e-mail/campanha;
- alteração de dados em Shopify, Supabase, Meta, Google, Klaviyo ou Tiny;
- deploy, restart, Docker, VPS ou automação produtiva;
- criação automática de decisão sem evidência no chat/fonte;
- guardar secrets, dados sensíveis desnecessários ou dados pessoais brutos.

## 5. Usuários

- **Lucas:** ganha continuidade; não precisa repetir decisões já tomadas.
- **Hermes Geral / COO:** sabe onde registrar e recuperar decisões.
- **LK OS, Zipper OS, SPITI OS:** mantêm memória própria por empresa.
- **Operações/Governança:** define quando uma decisão também muda skill, rotina, PRD ou guardrail global.
- **Subagentes futuros:** recebem contexto estável sem depender do chat original.

## 6. Decisão Hermes-native

- O que Lucas definiu: toda decisão sobre empresas deve ser documentada na memória delas.
- O que Hermes já faz: possui Brain versionado, skills, memória persistente, áreas por empresa e rotinas.
- Decisão: **aplicar como protocolo permanente**.
- Por quê: decisões empresariais têm valor operacional e precisam sobreviver ao turno atual.

## 7. Escopo da regra

Uma decisão deve ser registrada quando ela definir ou alterar qualquer um destes pontos:

1. **Produto/relatório/rotina:** formato, ordem, frequência, audiência, canal, campos obrigatórios.
2. **Tom e comunicação:** estilo de marca, linguagem permitida/proibida, nível de sofisticação, hard-sell ou não.
3. **Dados e fontes de verdade:** qual sistema manda, filtros, exceções, fallback, leitura vs escrita.
4. **Aprovações/autonomia:** o que pode rodar sozinho, o que exige aprovação do Lucas, o que é bloqueado.
5. **Comercial/operacional:** pricing, sourcing, estoque, CRM, logística, atendimento, pós-venda.
6. **Governança entre empresas:** regras que impedem mistura de dados, tom, clientes, credenciais ou contexto.

## 8. Requisitos funcionais

### RF1 — Classificar a empresa antes de registrar

Toda decisão deve ser roteada para uma destas camadas:

- `areas/lk/` — LK OS / LK Sneakers;
- `areas/zipper/` — Zipper OS / Zipper Galeria;
- `areas/spiti/` — SPITI OS / SPITI Auction;
- `empresa/` — regra cross-empresa ou arquitetura global da Grande Mente;
- `areas/operacoes/` — rotina, cron, Brain hygiene ou workflow Hermes;
- `areas/governanca/` ou `seguranca/` — aprovação, risco, permissão, autonomia;
- `areas/tecnologia/` — infra, integração, scripts, deploy, APIs.

### RF2 — Registrar no artefato vivo certo

A decisão deve ir para o local que será consultado no futuro, não apenas para `reports/`.

Regra prática:

- decisão específica de empresa → `areas/<empresa>/...`;
- regra operacional recorrente → rotina em `areas/operacoes/rotinas/`;
- padrão usado por agente → skill correspondente em `skills/`;
- regra global/cross-empresa → `empresa/` e, se necessário, `areas/governanca/`;
- evidência temporária → `reports/`, apontando para o artefato vivo.

### RF3 — Atualizar skills quando a decisão muda execução

Se a decisão muda como o Hermes deve agir, a skill correspondente deve ser atualizada no mesmo ciclo.

Exemplos:

- decisão de relatório LK → `lk-operational-intelligence` e/ou `lk-report-delivery`;
- decisão de roteamento multiempresa → `multiempresa-routing-lucas`;
- decisão sobre aprovação/envio externo → skill/rotina de governança apropriada;
- decisão sobre Shopify LK → skill LK Shopify aplicável.

### RF4 — Registrar em formato de decisão, não só narrativa

Cada decisão salva deve conter, quando possível:

- data;
- empresa/área;
- decisão;
- motivo/contexto;
- fonte/evidência;
- impacto operacional;
- guardrails/aprovações;
- arquivos/skills atualizados;
- próxima revisão, se houver.

### RF5 — Separar fato, decisão e interpretação

O registro deve distinguir:

- **Fato:** o que foi dito, medido ou observado.
- **Decisão:** o que Lucas aprovou/corrigiu/definiu.
- **Interpretação:** como o Hermes aplicará isso.
- **Pendência:** o que ainda precisa de confirmação.

### RF6 — Exemplo obrigatório: relatório LK

As decisões do relatório LK devem estar na memória da LK, incluindo:

- relatório 19h30 é exclusivo loja física/POS;
- relatório deve mostrar dia/período primeiro e mês depois;
- vendedores devem aparecer no contexto diário/período e mensal quando houver atribuição POS;
- share de marcas mensal deve mostrar % de receita e valor BRL;
- categorias/marcas estranhas devem ser agrupadas em `Outras marcas`;
- e-mail/newsletter deve gerar subject, preheader e preheader oculto no HTML;
- decisões/next steps estratégicos vão para Lucas no Telegram, não para grupos/externos sem aprovação.

## 9. Requisitos não funcionais

- Português por padrão.
- Não salvar secrets, tokens ou valores sensíveis.
- Não salvar dados pessoais brutos desnecessários.
- Não criar “memória” a partir de suposição; registrar pressuposto como pendência.
- Preferir memória operacional compacta e consultável a logs longos.
- Evitar duplicação: uma decisão viva deve ter um local canônico e referências cruzadas.
- Se o Brain for alterado, rodar validação/secret scan disponível antes de PR/merge.

## 10. Guardrails e aprovações

Permitido sem nova aprovação, quando a decisão já foi dita/corrigida por Lucas no turno:

- documentação local no Brain;
- atualização de skill para refletir a decisão;
- criação de PRD/rotina/registro de decisão;
- referência cruzada em mapas/índices.

Bloqueado sem aprovação explícita adicional:

- envio externo;
- campanha;
- mutação de banco/API produtiva;
- alteração de preço/estoque/produto;
- deploy/restart/infra;
- compartilhar dados sensíveis fora do Brain.

## 11. Arquitetura de arquivos proposta

### Camada global

- `empresa/contexto/organograma-operacional-hermes-brain.md` — regra de roteamento e hierarquia.
- `empresa/decisoes/` — decisões cross-empresa ou de governança global.
- `areas/operacoes/prds/company-decision-memory-prd-2026-05-17.md` — este PRD.
- `areas/operacoes/rotinas/company-decision-memory.md` — rotina executável futura.

### Camada por empresa

- `areas/lk/` — decisões LK OS.
- `areas/zipper/` — decisões Zipper OS.
- `areas/spiti/` — decisões SPITI OS.

Cada empresa deve ter ou passar a ter um artefato de decisões/memória operacional, por exemplo:

- `areas/lk/decisoes/` ou seção equivalente no mapa/rotina LK;
- `areas/zipper/decisoes/` ou seção equivalente;
- `areas/spiti/decisoes/` ou seção equivalente.

A nomenclatura exata pode seguir a estrutura existente de cada área, mas o princípio é obrigatório: **decisão empresarial fica dentro da memória da empresa**.

## 12. Fluxo operacional

1. Identificar que Lucas tomou/corrigiu/aprovou uma decisão.
2. Classificar a empresa/área afetada.
3. Separar fato, decisão, interpretação e pendência.
4. Atualizar o artefato vivo da empresa.
5. Atualizar skill/rotina se a decisão muda comportamento futuro.
6. Se for regra cross-empresa, registrar também em `empresa/` ou governança.
7. Verificar que não há secrets/dados sensíveis indevidos.
8. Responder ao Lucas com: onde foi salvo, o que mudou, e se algo ficou pendente.

## 13. Critérios de pronto

- [ ] PRD salvo no Brain.
- [ ] Regra refletida no roteamento multiempresa ou rotina operacional.
- [ ] Exemplo LK registrado/endereçado em skill ou memória operacional LK.
- [ ] Índice de Operações atualizado.
- [ ] Nenhuma ação externa executada.
- [ ] Nenhum secret salvo.

## 14. Riscos

- Registrar demais e poluir a memória com detalhes transitórios.
- Registrar de menos e perder decisões importantes.
- Duplicar decisões em locais divergentes.
- Confundir relatório/evidência com fonte de verdade operacional.
- Registrar decisões de uma empresa na área errada.

Mitigação: manter decisões compactas, canônicas e por empresa; usar `reports/` só como evidência; atualizar skills quando houver mudança de comportamento.

## 15. Próximos passos recomendados

1. Criar rotina `company-decision-memory.md` com checklist operacional.
2. Atualizar `multiempresa-routing-lucas` com a regra explícita.
3. Garantir que LK OS tenha um registro claro para decisões dos relatórios de vendas.
4. Estender a mesma convenção para Zipper OS e SPITI OS quando novas decisões surgirem.
