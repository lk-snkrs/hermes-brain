# LK Growth Agentic OS — Orchestrator Telegram Summary Template v1

Status: template operacional
Escopo: transformar saída agentic em mensagem curta para Lucas, sem ruído

## Send / Suppress Decision

Antes de escrever a mensagem, marcar:

```yaml
telegram_send: yes | no
reason:
  - approval_needed | actionable_exception | confirmed_impact | requested_summary | risk_alert | silent_ok
noise_filter_passed: yes | no
```

Se `telegram_send: no`, registrar no Run Receipt e não enviar.

## Message Template — Approval Needed

```text
Growth encontrou uma decisão para aprovar.

Veredito: <1 frase>

Top ação:
- <ação>

Evidência:
- <2 bullets máximos>

Risco/rollback:
- <1 bullet>

Aprovação necessária:
- <A3 ou A4 + escopo exato>

Se aprovado, próximo passo:
- <ação concreta>
```

## Message Template — Actionable Exception

```text
Alerta Growth acionável.

Problema:
- <problema>

Impacto:
- <impacto provável>

O que já foi verificado:
- <fonte/status>

Próximo seguro:
- <ação A0/A1 ou aprovação necessária>
```

## Message Template — Weekly Agentic Summary

```text
Growth semanal — resumo acionável.

Veredito: <1 frase>

Top 3:
1. <ação/status/approval>
2. <ação/status/approval>
3. <ação/status/approval>

Bloqueado por falta de fonte:
- <gap principal>

Próximo seguro:
- <ação A0/A1/A2>
```

## Message Template — Impact Confirmed

```text
Growth D+<7/14/30> — impacto medido.

Hipótese:
- <hipótese curta>

Resultado:
- <improved/neutral/worsened/inconclusive + métrica>

Aprendizado:
- <lição>

Próximo:
- <repeat/refine/kill/monitor>
```

## Style Rules

- Máximo 5 bullets quando possível.
- Sem logs técnicos.
- Sem output bruto de subagente.
- Sem job IDs se não forem necessários para decisão.
- Dizer claramente se é `preview`, `recomendação` ou `aprovação`.
- Se precisa de aprovação, escopo deve ser exato.
- Se faltou fonte essencial, dizer `não decision-grade`.

## Suppress Examples

Não enviar Telegram quando:

- execução silent-OK sem decisão;
- relatório só foi salvo no Brain;
- fonte falhou mas há fallback benigno e sem impacto;
- subagente gerou análise intermediária;
- verificação local passou sem ação necessária.

## Approval Button Labels Suggested

Quando a plataforma permitir choices/botões:

- `Aprovar preview local`
- `Aprovar A3 escopado`
- `Pedir mais fontes`
- `Bloquear por enquanto`
