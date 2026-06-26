# Elle MVP 1C dry-run report

- Data UTC: 2026-06-09T13:09:56.290717+00:00
- Fixtures: 12
- Intent OK: 12/12
- Labels OK: 12/12
- Risk OK: 12/12
- Handoff OK: 12/12
- Forbidden public actions: 0

## Rows
- evt_001: intents=['saudacao'] labels=['whatsapp-api'] risk=baixo handoff=False actions=['private_note', 'apply_labels']
- evt_002: intents=['pedido'] labels=['pedido', 'whatsapp-api'] risk=medio handoff=False actions=['private_note', 'apply_labels']
- evt_003: intents=['pedido', 'prazo', 'reclamacao'] labels=['pedido', 'whatsapp-api', 'prazo', 'reclamacao', 'humano'] risk=alto handoff=True actions=['private_note', 'apply_labels', 'assign_team']
- evt_004: intents=['estoque'] labels=['estoque', 'whatsapp-api'] risk=medio handoff=False actions=['private_note', 'apply_labels']
- evt_005: intents=['estoque'] labels=['estoque', 'whatsapp-api', 'humano'] risk=alto handoff=True actions=['private_note', 'apply_labels', 'assign_team']
- evt_006: intents=['troca'] labels=['troca', 'whatsapp-api'] risk=medio handoff=False actions=['private_note', 'apply_labels']
- evt_007: intents=['devolucao'] labels=['devolucao', 'humano', 'whatsapp-api'] risk=alto handoff=True actions=['private_note', 'apply_labels', 'assign_team']
- evt_008: intents=['financeiro'] labels=['financeiro', 'humano', 'whatsapp-api'] risk=alto handoff=True actions=['private_note', 'apply_labels', 'assign_team']
- evt_009: intents=['pedido', 'vip'] labels=['pedido', 'whatsapp-api', 'vip'] risk=medio handoff=False actions=['private_note', 'apply_labels']
- evt_010: intents=['encomenda'] labels=['estoque', 'humano', 'whatsapp-api'] risk=alto handoff=True actions=['private_note', 'apply_labels', 'assign_team']
- evt_011: intents=['ambiguo'] labels=['humano', 'whatsapp-api'] risk=alto handoff=True actions=['private_note', 'apply_labels', 'assign_team']
- evt_012: intents=['reclamacao'] labels=['reclamacao', 'humano', 'whatsapp-api'] risk=alto handoff=True actions=['private_note', 'apply_labels', 'assign_team']
