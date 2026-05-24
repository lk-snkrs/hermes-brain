# Template — Receipt Operacional Hermes Brain

Use para toda execução relevante feita por Hermes Central, profile especialista, cron, webhook ou integração. O receipt é a ponte entre execução e Brain; sem receipt, a execução não é fonte durável.

```md
# Receipt — <empresa/área> — <ação> — <YYYY-MM-DD>

- Data/hora:
- Agente/profile/cron:
- Empresa/área:
- Responsável humano:
- Pedido original:
- Classificação: read-only | local-write | external-write | customer-facing | infra-sensitive
- Fontes usadas:
- O que foi feito:
- Output/artefato:
- Aprovação:
- Envio/publicação:
- Writes externos:
- Riscos/bloqueios:
- Rollback/mitigação:
- Próximos passos:
- Onde foi documentado no Brain:
- Source confidence: runtime-verificado | fonte-primária | fonte-secundária | inferido | não-verificado
```

## Regra

- Ações externas, customer-facing, infra, campanha, preço, disponibilidade, reserva, negociação e fornecedor exigem aprovação ou fonte/escopo previamente autorizados.
- Receipts devem ficar na área que executou: `areas/<empresa>/.../receipts/` ou `areas/operacoes/receipts/`.
- Reports brutos podem ficar locais; receipts curados são artefatos de governança.
