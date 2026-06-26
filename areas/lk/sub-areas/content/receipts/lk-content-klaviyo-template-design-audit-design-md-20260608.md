# Receipt — Klaviyo template/design audit + design.md

Data: 2026-06-08
Perfil: lk-content
Escopo: auditoria read-only de templates/campaigns Klaviyo para fundamentar o `design.md` do agente Produção de Conteúdo.

## Status

Status: OK

## Evidência

- Script criado/ajustado: `/opt/data/profiles/lk-content/scripts/klaviyo_template_design_audit.py`
- Output OK: `/opt/data/profiles/lk-content/cron/output/8fe6fcf6626f/2026-06-08_10-48-39.md`
- Design guide criado: `/opt/data/profiles/lk-content/brand-guide/design.md`

## Resultado do audit

- Templates lidos: 10
- Campaigns email recentes lidas: 20
- Endpoints: templates HTTP 200; campaigns email HTTP 200
- Editor type observado: CODE em 10/10 templates
- HTML presente: 10/10 templates
- Templates com sinal de produto: 10/10
- Templates com sinal de desconto: 4/10
- Média estimada: 3,4 imagens e 6,8 links por template

## Guardrails

- Writes externos realizados: 0
- Draft/template/campaign criado ou editado: não
- Envio/agendamento/ativação realizada: não
- PII retornado: false
- Secrets impressos: false

## Decisão incorporada no design.md

- Base visual: preto/off-white/taupe, editorial premium.
- Estrutura: hero editorial, curadoria/produto, contexto, atendimento humano e footer limpo.
- Desconto: exceção comercial, não linguagem base.
- Próximo gate: preview local da newsletter; qualquer write Klaviyo exige aprovação explícita atual.
