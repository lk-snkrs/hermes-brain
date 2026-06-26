# Template — Approval Ledger Entry

Use quando Lucas aprovar, corrigir ou delimitar autonomia para qualquer ação sensível.

```md
# Approval — <tema> — <YYYY-MM-DD>

- Data/hora:
- Aprovador:
- Canal da aprovação:
- Empresa/área:
- Escopo autorizado:
- Escopo explicitamente não autorizado:
- Validade/expiração:
- Nível de autonomia: A0 bloqueado | A1 read-only | A2 local-write | A3 externo gated | A4 externo autorizado
- Risco:
- Fontes/evidências:
- Ação permitida:
- Critério de parada:
- Rollback:
- Onde aplicar: rotina | skill | memória | cron | profile | Mission Control
- Onde foi persistido:
```

## Regra

Aprovação em chat não basta para conhecimento durável. Toda aprovação que muda comportamento futuro precisa entrar no ledger e, se recorrente, virar skill/rotina.
