# Rotina — Hermes Auto-Remediation Contract

Status: canônica para Hermes/agentes/scripts/crons  
Criada em: 2026-06-14  
PRD: `../prds/hermes-systemwide-auto-remediation-prd-2026-06-14.md`

## Regra curta

**Erro identificado = correção iniciada**, salvo quando a próxima ação exige aprovação sensível.

## Loop obrigatório

1. **Detectar** — reconhecer a falha real, não maquiar.
2. **Classificar** — A0/A1/A2/A3/A4 conforme política de autonomia.
3. **Corrigir ou pedir aprovação** — executar automaticamente A0/A1; executar A2 apenas se o escopo já estiver aprovado; criar approval packet para A3/A4.
4. **Verificar** — rodar teste, readback, health check, diff check ou smoke test adequado.
5. **Registrar aprendizado** — atualizar skill/rotina/receipt/regressão quando a falha for recorrente ou sistêmica.

## Aplicação por superfície

### Hermes Geral

- Não parar em “deu problema” quando a correção é local/documental/read-only.
- Ao falar com Lucas, já trazer a próxima ação corretiva.
- Se for sensível, trazer aprovação escopada com rollback e verificação, não uma desculpa genérica.

### Especialistas

- LK Ops/Atendimento, LK Growth, LK Shopify, LK Stock, Mordomo, SPITI, Zipper e demais especialistas devem aplicar o mesmo contrato.
- Especialista deve corrigir falha de template, link, preview, skill, prompt, documentação, cache local, script local e roteamento seguro sem pedir nova ordem.
- Especialista deve bloquear e pedir aprovação para contato externo, preço, disponibilidade, envio, produção e write de sistema vivo.

### Scripts/watchdogs

- O script deve preferir auto-heal local allowlisted antes de alertar.
- Saída cron/no_agent: `rc=0 + stdout vazio = OK`; `stdout` só para alerta acionável; erro não tratado deve ser raro e sanitizado.
- Se a correção local foi feita e o estado final é OK, registrar localmente e não mandar Telegram de sucesso por padrão.

### Crons

- Cron que detecta falha histórica ou recuperada deve suprimir ruído.
- Cron que detecta falha atual e auto-corrige deve ficar silencioso se a correção foi completa.
- Cron que não pode corrigir deve emitir alerta acionável com causa, evidência e ação necessária.

## Frases padrão

### Falha corrigível

```text
Identifiquei um problema: [X].
Classificação: A1 — correção local segura.
Vou corrigir agora e verificar com [check].
```

### Falha corrigida

```text
Corrigido.
Evidência: [check passou].
Não houve write externo/produção/secrets/runtime sensível.
```

### Falha sensível

```text
Identifiquei um problema: [X].
A correção toca [produção/externo/secret/infra], então está bloqueada sem aprovação.
Approval packet: alvo=[...], ação=[...], risco=[...], rollback=[...], verificação=[...].
```

## Relação com políticas existentes

- Complementa `empresa/contexto/politica-autonomia-aprovacao-hermes.md`.
- Não substitui approval gates A3/A4.
- Complementa Memory OS, Reminder OS, Runtime Truth Reconciler e Cron Control Plane.

## Auditoria

Rodar localmente:

```bash
python3 scripts/auto_remediation_contract_audit.py
```

O auditor é heurístico: aponta candidatos para revisão, não prova bug. Priorizar arquivos que falam de erro/falha sem mencionar auto-heal, correção, approval ou silent-OK.

## Matriz de cobertura

Para decidir se um detector já pode auto-corrigir ou só pode abrir approval packet, consultar `hermes-autoheal-coverage-matrix.md`.

A matriz separa:

- detector/watchdog existente;
- autoheal A0/A1 permitido;
- boundary que exige approval packet;
- estado atual dos 75 candidatos sensíveis remanescentes.
