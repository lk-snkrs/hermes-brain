# Report — Customer-facing Decision Template + Health Check Guard

Data: 2026-05-20  
Escopo: Hermes Brain / Operações / decisões customer-facing

## Objetivo

Transformar a melhoria recomendada no audit em mecanismo operacional: não basta registrar uma decisão; ela precisa ter formato padrão e precisa aparecer no `MAPA.md` da área para o próximo agente encontrar.

## Entregas

1. Template padrão criado:
   - `areas/operacoes/templates/decisao-customer-facing.md`

2. Navegação atualizada:
   - `areas/operacoes/MAPA.md`

3. Health check ampliado:
   - `scripts/brain_health_check.py`
   - novo check `decisions_index`
   - alerta quando uma pasta `areas/**/decisions/*.md` existe mas não está navegável a partir do `MAPA.md` local da área/subárea.

4. Rotina documentada:
   - `areas/operacoes/rotinas/brain-health-check.md`

## Regra operacional criada

Toda decisão customer-facing aprovada/corrigida por Lucas deve registrar:

- texto exato aprovado;
- canal;
- segmento/público;
- status de aprovação;
- tom aprovado;
- fluxo/cadência;
- guardrails;
- próxima ação permitida;
- o que ainda exige aprovação atual.

## Não alterado

- Nenhum envio externo.
- Nenhum template Meta/Crisp/n8n em produção.
- Nenhum cron/runtime/Docker/VPS.
- Nenhum banco/API/cliente.

## Critério de verificação

- `python3 -m py_compile scripts/brain_health_check.py`
- `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-05-20-customer-facing-decision-guard.json`
- `git diff --check`
- scan de secrets em arquivos alterados/untracked
