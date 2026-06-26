# LK Content Dashboard — Impeccable Reset

Data: 2026-06-10
Status: discovery/shape, sem código novo ainda
Registro: product UI, dashboard operacional

## Correção recebida de Lucas

O MVP atual está funcional, mas visualmente reprovado. Problemas:

- Sem sidebar, portanto não parece cockpit operacional.
- Hero editorial grande demais, ocupa o primeiro viewport e empurra decisões.
- Cards grandes e genéricos, baixa densidade operacional.
- Hierarquia insuficiente entre decisão, monitoramento, calendário, campanhas, flows e aprendizados.
- Visual “landing estática”, não dashboard de trabalho.
- Falta navegação por domínios: Overview, Campanhas, Calendário, Klaviyo, Flows, Pós-mortems, Brand Guide, Receipts, Settings.
- Falta padrão de estados, empty/loading/error, responsivo e IA/live data boundaries.

## Impeccable workflow aplicado

Documentação oficial lida: https://impeccable.style/docs

Referências locais carregadas:

- `impeccable/SKILL.md`
- `reference/product.md`
- `reference/shape.md`
- `reference/craft.md`
- `reference/mission-control-v12-impeccable-audit-20260517.md`

Regra aplicada agora:

- Antes de codar do zero, rodar `shape`: perguntas de direção, depois brief confirmado.
- Dashboard é product register, não brand landing.
- Detector `npx impeccable detect` será gate técnico, não aprovação visual.
- Redesign precisa mudar topologia, não só tokens.

## Topologia antiga

Landing hero + dois cards grandes.

## Topologia alvo proposta

App shell com sidebar fixa, header compacto e cockpit multi-rota:

1. Overview / Command Center
2. Lucas Queue / Approvals
3. Campanhas
4. Calendário Editorial
5. Klaviyo Monitor
6. Flows & Segments
7. Pós-mortems / Learnings
8. Brand Guide
9. Receipts / Audit Trail
10. Configurações / Guardrails

## Princípios visuais prováveis

- Maison Ledger / editorial product UI.
- Fundo off-white/porcelain, painéis taupe, texto graphite.
- Caramel como ação/seleção, não decoração.
- Sidebar premium com navegação clara.
- Densidade operacional, não hero gigante.
- Decisões e próximos bloqueios aparecem no primeiro viewport.
- Métricas e rotinas abaixo, com drill-down.

## Perguntas pendentes

1. Qual direção visual deve liderar?
2. Qual escopo inicial do rebuild?
3. Quais dados/rotas precisam estar vivos no MVP v1?

## Próximo gate

Aguardar respostas de Lucas antes de implementar código novo.
