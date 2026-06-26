# LK Growth Agentic OS — Governor Checklist v1

Status: template operacional
Escopo: checagem obrigatória antes do `lk-growth` gerar síntese, packet, Telegram ou recomendação final

## Metadata

- run_id: `<run id>`
- date: `<YYYY-MM-DD>`
- reviewed_by: `Growth Governor / Critic`
- source_run_receipt: `<path>`
- specialist_outputs_reviewed:
  - `<subagent>`

## 1. Evidence Quality

- [ ] Cada finding tem fonte explícita.
- [ ] Fonte essencial está verificada ou gap declarado.
- [ ] URL/SKU/handle está presente quando aplicável.
- [ ] Métricas têm janela e fonte.
- [ ] Evidência, hipótese, opinião e decisão estão separadas.
- [ ] Claims sem fonte foram removidos ou rebaixados.

Notes:

```text
<notes>
```

## 2. Source Hierarchy

- [ ] Estoque não foi usado como proxy de prioridade SEO/CRO.
- [ ] Tiny/Shopify/GSC/GA4/GMC/Brain foram usados conforme hierarquia correta.
- [ ] Sinais auxiliares não sustentam causalidade isolada.
- [ ] Fonte ausente rebaixou confidence quando necessário.

Notes:

```text
<notes>
```

## 3. Autonomy & Approval

- [ ] A0/A1/A2 estão dentro de autonomia segura.
- [ ] A3 foi marcado para qualquer pequeno write externo.
- [ ] A4 foi marcado para bulk/produção/campanha/infra.
- [ ] Nenhum write externo está implícito sem aprovação.
- [ ] Rollback/verificação foram exigidos para A3/A4.

Blocked items:

```yaml
blocked_pending_A3:
  - <item>
blocked_pending_A4:
  - <item>
```

## 4. Anti-duplication / Learning

- [ ] O item não duplica experimento sem citar histórico.
- [ ] Hipóteses novas foram registradas para ledger.
- [ ] D+7/D+14/D+30 foi definido quando aplicável.
- [ ] Falhas de fonte ou prompt foram marcadas como context/skill update candidates.
- [ ] Recomendações repetidas sem resultado foram marcadas `kill` ou `refine`.

Notes:

```text
<notes>
```

## 5. Telegram Noise Filter

Telegram só pode sair se houver:

- [ ] decisão pedindo aprovação;
- [ ] exceção/falha acionável;
- [ ] resumo desejado pelo Lucas;
- [ ] impacto confirmado;
- [ ] risco que exige atenção.

Não enviar Telegram para:

- [ ] silent-OK;
- [ ] fallback benigno recuperado;
- [ ] logs técnicos;
- [ ] output bruto de subagente;
- [ ] relatório longo sem decisão.

Telegram decision:

- send: `yes | no`
- reason: `<why>`

## 6. Final Classification

```yaml
approved_A0_A1:
  - <safe diagnostic/preview>
approved_A2_recommendation:
  - <evidence-based recommendation>
requires_A3_approval:
  - <small external write>
requires_A4_approval:
  - <bulk/production/campaign/infra>
regraded_non_decision_grade:
  - item: <item>
    reason: <reason>
blocked:
  - item: <item>
    reason: <reason>
```

## 7. Governor Verdict

- verdict: `pass | pass_with_regrades | blocked | needs_more_sources`
- next_safe_action: `<action>`
- next_approval_gate: `<approval if any>`

## Failure Conditions

Governor must block final output if:

- a recommendation implies write without A3/A4;
- essential source is absent but confidence remains high;
- no follow-up metric exists;
- output would create Telegram noise;
- production/infra/secrets are touched without approval packet.
