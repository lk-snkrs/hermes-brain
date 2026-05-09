# Retomada de planos e PRDs pausados

## Objetivo

Evitar que planos, PRDs, branches e análises longas fiquem perdidos entre sessões. A rotina cria um resumo operacional do que está pendente, o que está bloqueado e qual é a próxima ação segura.

Inspirada no conceito de retomada de wizards do material Bruno/OpenClaw, mas adaptada ao Hermes: `session_search`, Hermes Brain, git, PRs e Telegram.

## Área dona

Operações / Hermes Geral.

## Agenda

Sob demanda quando Lucas disser “seguir”, “retomar”, “onde paramos” ou quando uma rodada longa for interrompida.

Futura agenda possível: semanal, se Lucas quiser briefing automático.

## Fontes

Ler, nesta ordem:

1. contexto ativo da sessão;
2. `todo` da sessão, se existir;
3. `empresa/gestao/pendencias.md`;
4. `memories/pending.md`;
5. `ROADMAP-30-DIAS-HERMES.md`;
6. PRDs locais em `/opt/data/hermes_bruno_ingest/` quando relevantes;
7. `git status`, branches e PRs dos repos envolvidos;
8. `session_search` para trabalhos interrompidos.

## Saída

Resumo curto:

- item/projeto;
- estado atual;
- último artefato/commit/PR;
- bloqueio real;
- próxima ação segura;
- se precisa de aprovação Lucas.

## Fluxo operacional

1. Identificar o projeto ativo ou mais recente.
2. Separar pendência real de histórico já concluído.
3. Verificar arquivos/branches/PRs antes de afirmar status.
4. Se houver vários itens, priorizar:
   - produção quebrada;
   - segurança/secrets;
   - PR aberto bloqueando trabalho;
   - tarefas que Lucas acabou de pedir;
   - melhorias documentais seguras.
5. Executar a próxima ação segura se Lucas já disse “seguir”.
6. Parar para aprovação apenas se o próximo passo for externo, produtivo, destrutivo, credencial, merge, deploy ou envio.

## Doppler keys

Nenhuma por padrão.

Usar Doppler apenas se for necessário verificar PR privado ou push, sem imprimir valores.

## Como verificar sucesso

- Pendência localizada em fonte real.
- Próxima ação executada ou claramente bloqueada.
- Se arquivo foi alterado: health check/secret scan conforme escopo.
- Se PR/branch foi criado: URL/branch/commit registrados.

## Se falhar

- Se não houver contexto suficiente: usar `session_search` antes de perguntar ao Lucas.
- Se repo estiver com alterações locais não relacionadas: usar worktree/branch separada e não misturar diffs.
- Se credencial faltar: documentar o nome do secret necessário, não pedir token em chat.

## Aprovação necessária

Não precisa para retomada, leitura, documentação e PR draft.

Precisa para merge, deploy, produção, Docker/VPS, banco, mensagens externas, credenciais ou qualquer contato com cliente/colecionador/parceiro.
