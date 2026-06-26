# Receipt — Readback avisar-enc desativado

- Data/hora: 2026-06-18T09:54:56.047432+00:00
- Agente/profile/cron: Hermes Geral / Mesa COO
- Empresa/área: LK Sneakers / Atendimento
- Responsável humano: Hermes
- Pedido original: Lucas indicou que o trigger avisar-enc deve ficar desativado; verificar estado vivo sem write externo.
- Classificação: read-only
- Fontes usadas:
- Chatwoot recovery_settings API GET /api/v1/accounts/1/recovery_settings via Doppler-first; secret values not printed.
- O que foi feito:
- Readback runtime confirmou SHOPIFY_TAG_TRIGGERS como objeto vazio; sem PATCH/PUT/POST.
- Output/artefato:
- Estado desejado já está refletido no runtime: avisar-enc não aparece em SHOPIFY_TAG_TRIGGERS.
- Aprovação: Lucas confirmou direção operacional: deve ficar desativado. Execução feita somente read-only porque não havia write necessário.
- Envio/publicação: Nenhum envio externo.
- Writes externos: 0
- Riscos/bloqueios: Jobs antigos já agendados podem não ser cancelados por mudança de settings; runbook indica que desligar flag impede novos agendamentos mas jobs antigos podem ter comportamento próprio.
- Rollback/mitigação: Não aplicável: nenhum write executado. Se precisar reativar no futuro, exige aprovação escopada e snapshot.
- Próximos passos: Monitorar se novo evento lk_avisa_encomenda/tag avisar-enc aparecer; se aparecer, gerar packet de correção com endpoint/método aprovado.
- Onde foi documentado no Brain: areas/lk/sub-areas/atendimento/receipts/20260618T095455Z-avisar-enc-disabled-readback.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
