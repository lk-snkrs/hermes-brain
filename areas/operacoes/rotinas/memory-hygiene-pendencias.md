# Higiene de memória e pendências

## Objetivo

Manter o sistema de memória do Hermes Brain limpo, acionável e auditável, separando o que é ativo, bloqueado, histórico, decisão, lição e contexto vivo.

Esta rotina existe para evitar dois problemas: pendência eterna que nunca vira ação e memória inchada que mistura regra durável com log de sessão.

## Área dona

Operações / Hermes Geral.

## Agenda

Sob demanda após rodadas grandes, antes de retomar planos antigos, ou mensalmente se Lucas quiser uma rotina fixa.

Não é cron confirmado. Se virar cron, documentar o job real e a entrega em Telegram.

## Fontes

Ler, nesta ordem:

1. `START-HERE.md` para o fluxo de navegação.
2. `empresa/gestao/memory-system.md` para camadas de memória.
3. `empresa/gestao/pendencias.md`.
4. `memories/pending.md`.
5. `memories/decisions.md`.
6. `memories/lessons.md`.
7. `ROADMAP-30-DIAS-HERMES.md`.
8. `CHANGELOG.md`.
9. `session_search` quando a pendência depender de histórico não documentado.
10. `git status`, branches e PRs quando houver trabalho em repo.

## Classificação obrigatória

Cada item revisado precisa cair em uma destas classes:

- **Ativo**: próxima ação clara e segura existe agora.
- **Bloqueado**: depende de aprovação Lucas, credencial, acesso, dado vivo, agenda externa ou decisão de negócio.
- **Aguardando data/evento**: depende de leilão, campanha, feira, cron, release ou reunião futura.
- **Concluído**: já virou commit, PR, rotina, decisão ou entrega verificável.
- **Arquivar**: informação histórica sem próxima ação.
- **Promover para decisão**: saiu de pendência e virou regra permanente.
- **Promover para lição**: aprendizado reutilizável que deve entrar em `memories/lessons.md` ou skill.

## Fluxo operacional

1. Coletar pendências das fontes acima.
2. Remover duplicatas óbvias, preservando o registro mais rico.
3. Para cada item, preencher:
   - título curto;
   - negócio/área: Global, LK, Zipper, SPITI, Operações, Tecnologia, Governança;
   - status: ativo, bloqueado, aguardando, concluído, arquivado;
   - próxima ação segura;
   - aprovação necessária, se houver;
   - evidência: arquivo, commit, PR, rotina, relatório ou sessão.
4. Atualizar `empresa/gestao/pendencias.md` com o estado executivo.
5. Atualizar `memories/pending.md` somente para pendências globais compactas que precisam aparecer no boot mental.
6. Se algo virou regra, mover para `memories/decisions.md` e referenciar no changelog/roadmap se for relevante.
7. Se algo virou aprendizado operacional, mover para `memories/lessons.md` ou para uma skill.
8. Não apagar histórico útil; mover para seção de arquivados/concluídos com data.

## Regras de higiene

- Memória durável não é log de execução.
- `memories/` deve ser compacto e executivo.
- Detalhe operacional vive em `empresa/`, `areas/`, `agentes/`, `skills/` e `reports/`.
- Tokens, dumps, dados pessoais e credenciais nunca entram em memória ou docs.
- “Rotina documentada” não significa cron ativo.
- Se não há fonte verificável, marcar `[a confirmar]` em vez de inventar.

## Template de saída

```md
# Higiene de memória e pendências — YYYY-MM-DD

## Ativos
- [ ] Item — próxima ação — dono/área — evidência

## Bloqueados
- [ ] Item — bloqueio — aprovação/acesso necessário

## Aguardando data/evento
- [ ] Item — evento gatilho — data se houver

## Concluídos nesta revisão
- Item — evidência: commit/PR/arquivo

## Arquivados
- Item — motivo

## Promovidos para decisões/lições
- Decisão/lição — destino
```

## Como verificar sucesso

- `empresa/gestao/pendencias.md` e `memories/pending.md` não se contradizem.
- Itens concluídos têm evidência.
- Itens bloqueados dizem exatamente o bloqueio.
- Nenhum valor secreto foi registrado.
- Se houve alteração no Brain: rodar `python3 scripts/brain_health_check.py` e secret scan.

## Aprovação necessária

Não precisa para leitura, organização e documentação.

Precisa para deletar informação sensível sem backup, alterar produção, mexer em secrets, executar contatos externos, mudar crons, fazer deploy, alterar banco ou mergear PR fora da autorização documental de baixo risco.
