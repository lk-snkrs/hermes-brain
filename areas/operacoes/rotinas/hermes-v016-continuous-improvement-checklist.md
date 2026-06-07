# Checklist recorrente — Hermes v0.16 Continuous Improvement

Criado em: 2026-06-06
Escopo padrão: local/read-only/documental, salvo aprovação explícita.

## Objetivo

Transformar releases Hermes em melhorias reais de uso, segurança, governança e autonomia, sem gerar ruído no Telegram e sem mutar produção sem plano.

## Cadência sugerida

- Pós-release: obrigatório.
- Semanal: melhoria contínua.
- Pós-incidente: reavaliar guardrails e receipts.

## Checklist P0 — sempre

1. **Release truth**
   - Capturar release oficial GitHub.
   - Confirmar versão runtime viva com `hermes --version`.
   - Confirmar config version com `hermes config check`.

2. **Dashboard/API safety**
   - `/` anônimo redireciona para `/login`.
   - `/api/config` anônimo retorna `401`.
   - API local `/health` retorna `ok`.
   - API bruta não está exposta publicamente sem aprovação.

3. **Telegram clean UX**
   - Sem wrappers técnicos.
   - Sem JSON/job_id/preflight metadata.
   - Telegram só alertas acionáveis, decisões e resumos desejados.

4. **Brain/receipts**
   - Brain Health `FAIL=0/WARN=0`.
   - Secret scan targeted nos artefatos tocados.
   - Receipt salvo para qualquer mudança material.

5. **Adoption matrix**
   - Classificar cada novidade como:
     - já adotado;
     - P0 hábito agora;
     - P1 melhoria segura;
     - P2 futuro;
     - A3/A4 aprovação necessária;
     - irrelevante.

## Checklist P1 — melhoria contínua

1. **Skills/toolsets**
   - Auditar skills pesadas ou redundantes.
   - Separar Telegram leve de CLI/manutenção ampla.
   - Preservar skills críticas de Lucas contra pruning automático sem receipt.

2. **Modelos/fallbacks**
   - Verificar catálogo/model picker.
   - Não trocar default sem smoke/rollback.
   - Separar fast lane de deep work quando houver evidência.

3. **Sessões/contexto**
   - Usar `session_search` antes de pedir Lucas repetir.
   - Usar `/undo` quando a direção ficou errada.
   - Salvar aprendizados como skills/Brain, não inflar memória curta.

4. **Especialistas**
   - Garantir contratos claros por perfil.
   - Registrar handoff/receipt em tarefas multiempresa.
   - Não deixar Hermes Geral assumir ownership de LK/Shopify/SPITI quando há especialista.

5. **Micro-aulas**
   - Ensinar uma feature prática por digest/semana quando relevante.
   - Rotação inicial v0.16:
     - `/undo`;
     - Dashboard admin;
     - model picker;
     - skills/curator;
     - sessions/search.

## Checklist A3/A4 — pedir aprovação

Pedir aprovação com escopo, risco, rollback e verificação antes de:

- Docker/Traefik/gateway restart/swap.
- Credentials/secrets/OAuth.
- Webhooks públicos.
- Channels/messaging platform changes.
- MCP com permissões sensíveis.
- API pública.
- Model default/fallback de perfis vivos.
- Kanban workers com impacto externo.
- Shopify/Ads/GMC/email/clientes/fornecedores/dinheiro.

## Resultado esperado

Um ciclo de melhoria só está completo quando existe:

- evidência da release/runtime;
- classificação de adoção;
- mudança segura executada ou deferida;
- receipt/Brain doc;
- verificação;
- explicação curta para Lucas do que muda no uso diário.
