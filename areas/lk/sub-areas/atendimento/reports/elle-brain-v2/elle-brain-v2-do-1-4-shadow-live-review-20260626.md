# Elle Brain v2 — shadow diff review + live OpenRouter classify-only — 2026-06-26

**Gerado:** 2026-06-26T16:15:47.270318+00:00  
**Escopo:** pedido Lucas “Fazer do 1 ao 4” após Fase B/C local + shadow.  
**Modo:** local/shadow; sem envio a cliente; sem Chatwoot/Shopify/Tiny/WhatsApp write.  
**values_printed:** false

## 1. Verificação de artefatos

- Módulo v2 paralelo atualizado no container: `/app/elle_brain_v2.py`.
- Regression suite atualizada no container: `/app/tests/elle_brain_v2_regression.py`.
- Shadow runner atualizado no container: `/app/scripts/elle_brain_v2_shadow_runner.py`.
- Cópia persistente local: `/opt/elle-chatwoot/brain-v2/`.
- Backup antes da atualização: `/root/elle-brain-v2-do-1-4-backups/20260626T160752Z`.
- `app.py` produtivo não foi alterado.

## 2. Regression suite ampliada

Resultado validado em container:

```json
{"ok": true, "tests": 30, "values_printed": false}
```

Cobertura adicionada:

- browsing seguro;
- contexto antigo de pós-venda não contaminando navegação atual;
- pós-venda atual;
- estoque/pronta entrega/loja física;
- produto incerto / baixa confiança;
- promessa proibida;
- observabilidade candidate/policy;
- cupom aprovado;
- fit/guia de tamanho;
- checkout;
- prazo/CEP;
- foto/print incerto;
- comparação sensível;
- pedido explícito de humano;
- autenticidade;
- sanitização de e-mail/telefone/CEP;
- parser JSON para candidate live;
- `decide_shadow` sem valores sensíveis.

## 3. Shadow heuristic — review de diferenças

Resumo:

```json
{
  "generated_at": "2026-06-26T16:08:05.439200+00:00",
  "events_tail": 2000,
  "processed_seen": 36,
  "v2_categories": [
    [
      "product_clear",
      20
    ],
    [
      "human_handoff",
      9
    ],
    [
      "stock_handoff",
      3
    ],
    [
      "greeting",
      3
    ],
    [
      "institutional",
      1
    ]
  ],
  "v2_policy_actions": [
    [
      "allow",
      17
    ],
    [
      "handoff",
      12
    ],
    [
      "clarify",
      6
    ],
    [
      "rewrite",
      1
    ]
  ],
  "v2_parse_status": [
    [
      "not_consulted",
      36
    ]
  ],
  "v2_providers": [
    [
      null,
      36
    ]
  ],
  "mode": "heuristic",
  "live_openrouter_used": 0,
  "live_openrouter_non_valid_json_or_error": 0,
  "policy_ids": [
    [
      "P-BROWSE-001",
      9
    ],
    [
      "P-POSTSALE-001",
      5
    ],
    [
      "P-PHOTO-001",
      5
    ],
    [
      "P-HUMAN-001",
      4
    ],
    [
      "P-STOCK-001",
      3
    ],
    [
      "P-UNKNOWN-PRODUCT-001",
      1
    ],
    [
      "P-FIT-001",
      1
    ],
    [
      "P-AUTH-001",
      1
    ]
  ],
  "category_diff_count": 19,
  "handoff_diff_count": 14,
  "writes_external": 0,
  "values_printed": false
}
```

Padrões de diferença vs legado:

| Legado | v2 | Quantidade | Interpretação |
|---|---|---:|---|
| human_handoff/True | product_clear/False action=clarify | 5 | possível redução de handoff indevido; revisar amostra antes de canary |
| human_handoff/True | product_clear/False action=allow | 4 | possível redução de handoff indevido; revisar amostra antes de canary |
| stock_handoff/True | product_clear/False action=allow | 3 | possível redução de handoff indevido; revisar amostra antes de canary |
| greeting/False | product_clear/False action=allow | 2 | revisar |
| human_handoff/True | greeting/False action=allow | 2 | possível redução de handoff indevido; revisar amostra antes de canary |
| human_handoff/True | stock_handoff/True action=handoff | 1 | proteção de estoque/lk-stock |
| institutional/False | product_clear/False action=allow | 1 | revisar |
| product_clear/False | institutional/False action=rewrite | 1 | revisar |


**Leitura:** o v2 heurístico moveu muitos casos de `human_handoff` para `product_clear/clarify`, que é exatamente a hipótese de melhoria: menos transbordo burro para navegação/produto seguro. Isso ainda precisa de revisão amostral antes de canary porque shadow não sabe se havia contexto humano fora do log resumido.

## 4. Shadow live OpenRouter classify-only

Resumo:

```json
{
  "generated_at": "2026-06-26T16:14:20.008367+00:00",
  "events_tail": 2000,
  "processed_seen": 36,
  "v2_categories": [
    [
      "product_clear",
      17
    ],
    [
      "human_handoff",
      10
    ],
    [
      "stock_handoff",
      4
    ],
    [
      "greeting",
      4
    ],
    [
      "institutional",
      1
    ]
  ],
  "v2_policy_actions": [
    [
      "allow",
      17
    ],
    [
      "handoff",
      12
    ],
    [
      "clarify",
      6
    ],
    [
      "rewrite",
      1
    ]
  ],
  "v2_parse_status": [
    [
      "valid_json",
      27
    ],
    [
      "invalid_json_or_empty",
      8
    ],
    [
      "not_consulted",
      1
    ]
  ],
  "v2_providers": [
    [
      "openrouter",
      35
    ],
    [
      null,
      1
    ]
  ],
  "mode": "live_openrouter",
  "live_openrouter_used": 35,
  "live_openrouter_non_valid_json_or_error": 8,
  "policy_ids": [
    [
      "P-BROWSE-001",
      9
    ],
    [
      "P-POSTSALE-001",
      5
    ],
    [
      "P-PHOTO-001",
      5
    ],
    [
      "P-HUMAN-001",
      4
    ],
    [
      "P-STOCK-001",
      3
    ],
    [
      "P-UNKNOWN-PRODUCT-001",
      1
    ],
    [
      "P-FIT-001",
      1
    ],
    [
      "P-AUTH-001",
      1
    ]
  ],
  "category_diff_count": 19,
  "handoff_diff_count": 16,
  "writes_external": 0,
  "values_printed": false
}
```

Padrões de diferença vs legado live:

| Legado | v2 live | Quantidade | Interpretação |
|---|---|---:|---|
| human_handoff/True | product_clear/False action=clarify | 5 | possível redução de handoff indevido; bom candidato a canary após amostra |
| human_handoff/True | product_clear/False action=allow | 4 | possível redução de handoff indevido; bom candidato a canary após amostra |
| stock_handoff/True | product_clear/False action=allow | 3 | possível redução de handoff indevido; bom candidato a canary após amostra |
| human_handoff/True | greeting/False action=allow | 2 | possível redução de handoff indevido; bom candidato a canary após amostra |
| human_handoff/True | stock_handoff/True action=handoff | 1 | guardrail de estoque venceu; correto por política se houver disponibilidade/loja física |
| institutional/False | human_handoff/True action=allow | 1 | v2 mais conservadora; checar falso positivo |
| greeting/False | product_clear/False action=allow | 1 | revisar |
| product_clear/False | institutional/False action=rewrite | 1 | revisar |
| product_clear/False | stock_handoff/True action=allow | 1 | v2 mais conservadora; checar falso positivo |


## 5. Go/no-go técnico para canary

**Recomendação atual:** **NO-GO para canary automático hoje; GO para continuar shadow live + corrigir structured output.**

Motivos:

1. Live OpenRouter classify-only funcionou sem write externo, mas teve `valid_json` em 27/35 chamadas live e `invalid_json_or_empty` em 8/35.
2. O policy engine segurou os casos de risco mesmo com fallback, mas canary público precisa parse mais estável.
3. Existem 19 diferenças de categoria e 16 diferenças de handoff vs legado no live shadow; várias parecem melhorias, mas ainda exigem amostra qualitativa antes de cliente real.

## 6. Próximo ajuste antes de canary

- Melhorar structured output/retry do OpenRouter para mirar ≥95% `valid_json` em shadow live.
- Rodar nova janela com pelo menos 100 processed quando houver volume.
- Revisar qualitativamente amostras de:
  - `human_handoff -> product_clear/clarify`;
  - `stock_handoff -> product_clear`;
  - `product_clear -> stock_handoff/human_handoff`.

## 7. Segurança

- `writes_external=0`.
- `values_printed=false`.
- Nenhum segredo impresso.
- Nenhum telefone/e-mail/CEP salvo em relatório.
- Nenhum customer reply enviado pela v2.
