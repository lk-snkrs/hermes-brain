# Auditoria + PRD leve — Superpowers no dia a dia

Data: 2026-06-02
Contexto: Lucas relatou ganho claro de performance ao usar Superpowers e pediu para usar “para tudo”.
Escopo: adoção operacional segura no Hermes Brain, Hermes Geral e agentes especialistas, sem mexer em runtime, Docker, VPS, gateway, crons ou integrações externas.

## Veredito executivo

Superpowers deve virar o **modo operacional padrão** do ecossistema, mas com intensidade variável.

A decisão correta não é rodar um ritual pesado para qualquer mensagem. A decisão correta é usar Superpowers como disciplina universal de trabalho:

- entender intenção antes de executar;
- rotear para o contexto/agente certo;
- escolher a skill/procedimento correto;
- separar risco baixo de risco alto;
- verificar antes de concluir;
- transformar repetição em sistema, skill, rotina ou artifact.

## O que já estava integrado

1. Skill `superpowers` instalada e disponível.
2. Regra já registrada: todo PRD/documento de requisitos/spec/plano de produto passa por Superpowers.
3. `AGENTS.md` global do Brain já continha a regra PRD → Superpowers.
4. Os `AGENTS.md` dos agentes/especialistas documentais já tinham recebido a regra PRD → Superpowers.
5. `hermes-agent` já documentava a adaptação `mechovation/superpowers-hermes` e a correção de UX do `/superpowers`.
6. Skills derivadas já existem para o fluxo Superpowers: `brainstorming`, `writing-plans`, `executing-plans`, `verification-before-completion`, `dispatching-parallel-agents`, `receiving-code-review`, `finishing-a-development-branch`, `using-git-worktrees`, `writing-skills`.

## Lacunas encontradas

1. A regra estava forte para PRD, mas não estava explícita como modo operacional diário.
2. Faltava distinção entre Superpowers micro, leve e completo; sem isso, “usar para tudo” poderia virar burocracia.
3. Faltava propagar a regra para especialistas de forma não ambígua: LK, Mordomo, SPITI, Zipper, Hermes Geral e subáreas LK.
4. Faltava um artifact canônico para explicar quando usar cada intensidade.
5. Risco de excesso: longas perguntas de design para tarefas simples, mais ruído no Telegram e approval loops.

## Proposta de adoção

### Nível 0 — Micro-Superpowers

Usar em tarefas óbvias/curtas.

Checklist interno, sem expor ritual ao Lucas:

1. Qual é a intenção?
2. Qual é o contexto/empresa?
3. Existe risco ou fonte viva necessária?
4. Qual ação segura resolve?
5. Como verifico rapidamente?

Exemplos:

- responder dúvida simples;
- ajustar memória curta;
- procurar um arquivo específico;
- checar status read-only;
- resumir um relatório já existente.

### Nível 1 — Light Superpowers

Usar no trabalho normal do dia a dia.

Fluxo:

1. Carregar skill relevante.
2. Consultar Brain/histórico/fonte se necessário.
3. Roteamento: Hermes Geral vs especialista.
4. Declarar suposição/risco só quando importa.
5. Executar.
6. Verificar.
7. Salvar aprendizado se for durável.

Exemplos:

- auditoria local;
- relatório executivo;
- ajuste de documentação;
- continuidade de rotina;
- triagem de erro;
- handoff para especialista.

### Nível 2 — Full Superpowers

Usar sempre que houver PRD, auditoria pesada, código, multi-etapas, produção/external-write-adjacent, decisão estratégica, recorrência, cross-empresa ou risco.

Fluxo:

1. `superpowers` como wrapper.
2. Skill derivada correta:
   - descoberta/design: `brainstorming`;
   - plano: `writing-plans`;
   - execução: `executing-plans`;
   - verificação: `verification-before-completion`;
   - paralelismo: `dispatching-parallel-agents`;
   - skills: `writing-skills`;
   - PR/branch: skills GitHub/desenvolvimento correspondentes.
3. Skill de domínio/empresa.
4. Artifact reutilizável no Brain quando o output for recorrente ou estratégico.
5. Critérios de aceite, riscos, evidência e próxima decisão.

## Regras de UX

- Não transformar Superpowers em texto visível desnecessário.
- Telegram deve continuar limpo: decisão, exceção, resultado ou pergunta objetiva.
- Não fazer approval loop: se a ação é local/read-only/documental, executar; se é externa/produção/sensível, criar approval packet.
- Para tarefas triviais, usar o raciocínio Superpowers sem narrar tudo.
- Para tarefas complexas, explicitar o plano e checkpoints.

## Ações executadas nesta adoção

1. Memória do usuário atualizada: Superpowers como modo padrão para PRDs e trabalho não-trivial/recorrente, com versão leve no dia a dia.
2. Skill `superpowers` atualizada:
   - trigger ampliado para uso diário;
   - adicionado modelo Micro / Light / Full.
3. `AGENTS.md` global atualizado com seção “Superpowers no dia a dia”.
4. Regra propagada para AGENTS dos agentes e subáreas documentais:
   - Hermes Geral;
   - LC Claude CLI;
   - LK;
   - Mordomo;
   - SPITI;
   - Zipper;
   - LK Atendimento;
   - LK CRM;
   - LK Ecommerce;
   - LK Growth;
   - LK Growth / LK Shopify;
   - LK Shopify;
   - LK Tráfego Pago;
   - LK Trends.

## Política final

Superpowers passa a ser o **sistema operacional de trabalho**:

- micro para o simples;
- leve para o dia a dia;
- completo para PRDs, decisões, auditorias, código, risco e recorrência.

A métrica de sucesso não é “parecer que usamos Superpowers”. A métrica é:

- menos retrabalho;
- menos execução no contexto errado;
- mais verificação;
- mais aprendizado reutilizável;
- menos ruído para Lucas;
- decisões melhores e mais rápidas.

## Próximos passos recomendados

1. Na próxima semana, observar quais tarefas ainda foram resolvidas “no improviso” e converter em skill/rotina.
2. Adicionar um checklist curto de Superpowers aos relatórios diários de aprendizado apenas quando houver melhoria real, não como ruído.
3. Se o uso continuar melhorando performance, avaliar um pequeno “Superpowers score” nos handoffs internos: `micro`, `light` ou `full`, só em artifacts do Brain, não no Telegram.
