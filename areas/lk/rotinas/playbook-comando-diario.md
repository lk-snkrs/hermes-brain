# Playbook — LK Comando Diário

## Objetivo

Dar ao Hermes um roteiro executivo para abrir o dia da LK Sneakers sem inventar dados, sem disparar ações externas e sem misturar rotina documentada com execução real.

## Quando usar

Use quando Lucas pedir:

- "como está a LK hoje";
- briefing diário/semana;
- prioridades comerciais do dia;
- revisão de pedidos, CRM, tráfego, ecommerce ou atendimento.

## Fontes obrigatórias

1. `memories/lk.md` para contexto executivo e metas permanentes.
2. Shopify e/ou Supabase LK para números atuais, quando a pergunta exigir dados vivos.
3. `areas/lk/contexto/metricas.md` e `areas/lk/contexto/geral.md` para definições internas.
4. Rotinas específicas:
   - `areas/lk/rotinas/morning-briefing.md`.
   - `areas/lk/sub-areas/crm/rotinas/rfm-semanal.md`.
   - `areas/lk/sub-areas/crm/rotinas/cross-sell-monitor.md`.
   - `areas/lk/sub-areas/trafego-pago/rotinas/creative-pipeline.md`.
   - `areas/lk/sub-areas/atendimento/rotinas/consolidar-faq.md`.

## Loop operacional

```text
pergunta Lucas → identificar área LK → consultar contexto/fonte viva → separar fato de hipótese → montar prioridade → pedir aprovação se houver ação externa → registrar resultado/lesson
```

## Passo a passo

1. Classificar a demanda:
   - métrica/diagnóstico;
   - CRM/campanha;
   - tráfego/criativo;
   - ecommerce/estoque;
   - atendimento/FAQ;
   - problema operacional.
2. Se envolver número atual, consultar fonte viva antes de responder.
3. Se envolver recomendação, explicitar:
   - dado observado;
   - interpretação;
   - ação proposta;
   - risco ou ressalva.
4. Se envolver envio para cliente, WhatsApp, Klaviyo, campanha, público, post ou alteração operacional, preparar preview e aguardar aprovação Lucas.
5. Após execução aprovada por Lucas, registrar resultado em rotina ou lesson apropriada.

## Saída esperada

Formato recomendado:

```text
Resumo: ...
Dados consultados: ...
Prioridades: 1) ... 2) ... 3) ...
Ações livres: ...
Ações que exigem aprovação: ...
Próxima verificação: ...
```

## Regras de segurança

- Não afirmar faturamento, pedidos, ticket, estoque ou retenção sem fonte.
- Não sugerir produto fora de estoque.
- Não disparar campanha/WhatsApp/email/post sem aprovação.
- Não alterar Shopify, Klaviyo, Meta Ads, Supabase ou Evolution sem aprovação explícita.
- Doppler é fonte de secrets; nunca escrever valores de credenciais no Brain.

## Indicadores de qualidade

- Números atuais vêm de fonte viva ou são marcados como contexto histórico.
- Prioridades são poucas e acionáveis.
- A resposta separa o que Hermes pode fazer sozinho do que exige aprovação.
- Resultado volta para `lessons`, `outcomes_tracker` ou rotina relacionada.
