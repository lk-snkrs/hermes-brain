# Rotina — LC Mordomo Source Confidence + Approval Ledger

**Data:** 2026-06-05
**Status:** v0.1
**Escopo:** LC Mordomo OS, subagentes e Decision Inbox.

## 1. Objetivo

Padronizar duas coisas críticas:

1. como o sistema classifica a confiabilidade de fontes;
2. como registra aprovações/correções de Lucas para não transformar aprovação pontual em autonomia ampla.

## 2. Source Confidence

Todo dado material deve carregar nível de fonte quando usado para decisão, resposta externa ou relatório sensível.

### SC0 — Não verificado

Informação inferida, lembrada, antiga ou sem fonte consultada.

Uso permitido:

- hipótese;
- pergunta interna;
- draft marcado como não verificado.

Não permitido:

- afirmar para cliente;
- preço/lance/disponibilidade;
- ação externa.

### SC1 — Fonte secundária

Fonte útil, mas não canônica.

Exemplos:

- site público;
- print;
- resumo anterior;
- e-mail de notificação incompleto;
- dashboard de plataforma com atribuição parcial.

Uso permitido:

- triagem;
- alerta;
- pacote de decisão com ressalva.

### SC2 — Fonte primária consultada

Fonte canônica do domínio foi consultada, mas sem reconciliação extra.

Exemplos:

- Shopify para pedido/venda LK;
- Tiny depósito oficial para estoque LK;
- `vendas_tango` para vendas Zipper;
- e-mail fonte de lance SPITI;
- calendário real para evento.

Uso permitido:

- decisão operacional;
- relatório interno;
- draft com fonte.

### SC3 — Verificado/reconciliado

Fonte primária + confirmação adicional quando necessário.

Exemplos:

- WhatsApp readback + Gmail raw MIME para envio;
- Shopify + GA4/Pareto reconciliado;
- Zipper PDF manifest + arquivo validado;
- cron state + execução manual + stdout/stderr verificados.

Uso permitido:

- afirmar com alta confiança;
- registrar receipt;
- executar classe segura se guardrails passam.

### SCB — Bloqueado

Fonte insuficiente para a ação solicitada.

Deve virar blocker/Decision Packet.

## 3. Aplicação por domínio

### Zipper

- Preço/disponibilidade/reserva: exige fonte primária atual ou Lucas.
- PDF comercial: exige arquivo validado/manifest/cache verificado.
- Interesse por artista: pode vir de CRM/e-mail/WhatsApp, mas campanha exige dedupe + supressões.

### SPITI

- Lance/lote: exige fonte primária; site/meta não bastam.
- Divergência: pode ser alertada com fonte secundária, mas conclusão exige primária.

### LK

- Receita/pedido: Shopify.
- Estoque: Tiny `LK | CONTROLE ESTOQUE`.
- ROAS/campanhas: reconciliar fontes; plataformas são diagnóstico, não verdade final.

### Hermes/Infra

- Status real: cron list/log/runtime atual.
- Docs/PRD não provam execução ativa.

## 4. Approval Ledger

Toda aprovação/correção material de Lucas deve ser registrada quando afeta comportamento futuro.

### Campos mínimos

```markdown
## Approval Ledger Entry — YYYY-MM-DD HH:MM

**Lucas disse:**
**Interpretação:** aprovação | correção | preferência | regra | revogação | autonomia
**Escopo:** one-off | classe estreita | domínio | global
**Domínio:** pessoal | Zipper | SPITI | LK | Hermes/Infra | global
**Ação autorizada:**
**Limites:**
**Validade:** turno atual | recorrente | até revogação | data específica
**External send permitido?:** sim/não
**Fonte necessária:** SC0 | SC1 | SC2 | SC3 | SCB
**Registro atualizado:** memory | Brain | skill | CRM | state | PRD
**Observação:**
```

## 5. Regras de interpretação

### Aprovação de envio

“Enviar”, “pode enviar”, “manda” valem como aprovação atual apenas quando recipient/canal/copy/attachment/contexto estão claros no turno atual ou no preview imediatamente anterior.

Não vira autorização permanente.

### “Seguir”

“Seguir” autoriza continuidade segura/documental/read-only/local. Não autoriza:

- envio externo amplo;
- produção;
- infra sensível;
- dinheiro;
- campanha;
- cliente/fornecedor fora de classe aprovada.

### Feedback positivo

“Perfeito”, “ótimo”, “isso” aprova direção/produto, mas não é necessariamente comando de envio externo.

### Correção

Correção de Lucas deve atualizar o lugar certo:

- preferência compacta → memory;
- regra operacional → Brain/rotina;
- processo repetido → skill;
- contato/cliente → CRM/profile;
- empresa → Brain da empresa.

## 6. Verificação antes de usar aprovação passada

Antes de executar com base em aprovação anterior:

1. A aprovação era recorrente ou one-off?
2. O recipient/canal/payload é o mesmo?
3. A fonte ainda é válida?
4. A classe segura está documentada?
5. Existe guardrail/recent-history check?
6. Houve revogação ou correção posterior?
7. O output deve ser silencioso, recibo, digest, urgente, aprovação ou erro?

## 7. Anti-padrão crítico

Nunca transformar aprovação operacional genérica em permissão ampla para falar com clientes, fornecedores, artistas, bidders, campanhas, produção, banco ou infraestrutura.
