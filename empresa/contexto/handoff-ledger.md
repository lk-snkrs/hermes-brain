# Handoff Ledger — Hermes COO

Data de criação: 2026-05-24  
Owner: Hermes Geral / COO  
Status: ativo para registros locais/read-only

## Objetivo

Manter um ponto único para registrar handoffs relevantes entre Hermes Geral, especialistas, rotinas e Brain.

O ledger não substitui arquivos de trabalho de cada área. Ele aponta para eles e garante que a Grande Mente saiba o que aconteceu, onde está o output e qual decisão falta.

## Quando registrar

Registrar quando houver pelo menos um dos itens abaixo:

- decisão durável;
- output de especialista;
- approval packet;
- risco ou bloqueio A3/A4;
- write externo aprovado e executado;
- rollback/receipt;
- aprendizado que precisa virar Brain/skill/rotina;
- relatório de rotina com exceção relevante.

Não registrar ruído operacional sem decisão, sucesso silencioso, checks saudáveis ou progresso temporário de chat.

## Caminho recomendado

- Ledger central por data: `empresa/contexto/handoffs/YYYY-MM-DD.md`
- Output de domínio: manter no caminho da área, por exemplo:
  - `areas/lk/sub-areas/growth/`
  - `areas/zipper/inbox/` ou `areas/zipper/relatorios/`
  - `areas/spiti/`
  - `agentes/mordomo/`
- Template base: `templates/handoff-especialista.md`

## Formato mínimo

```markdown
## HH:MM — [Área] Título curto

- Agente/profile:
- Pedido original:
- Status: draft / read-only / preview / aprovado / enviado / bloqueado / falhou
- Fontes/evidências:
- Output/artefato:
- Aprovação: sim/não — escopo
- Writes externos: sim/não
- Risco/bloqueio:
- Próximo passo:
```

## Regras

1. Nunca incluir secrets, tokens, chaves ou dumps brutos de banco/API.
2. Não registrar promessa de preço, disponibilidade, reserva, logística externa, contato ou publicação sem fonte/approval.
3. Se o handoff envolve produção ou cliente, incluir rollback/receipt ou dizer explicitamente que não houve write.
4. Se a ação foi só local/read-only, declarar `Writes externos: não`.
5. Se for recurring/silent-OK, registrar apenas exceção, falha ou decisão necessária.

## Relação com Task Router

- `executar_aqui`: registrar só se a decisão for durável ou se houver artefato relevante.
- `delegar_especialista`: registrar handoff obrigatório quando houver output material.
- `preparar_approval_packet`: registrar o packet e o bloqueio.
- `bloquear_por_aprovacao`: registrar apenas se houver risco recorrente ou decisão pendente.
- `perguntar_clarificacao`: não registrar salvo se virar decisão durável.
