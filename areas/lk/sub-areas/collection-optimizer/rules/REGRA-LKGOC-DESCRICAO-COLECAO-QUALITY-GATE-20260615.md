# Regra LKGOC — Quality Gate de descrição de coleção

Registrado em: 20260615

## Erro corrigido
Não permitir que uma coleção LKGOC receba `body_html`, descrição curta, SEO description, hero intro ou resumo editorial com texto genérico, sistêmico ou fraco, mesmo quando o template/preview DEV esteja tecnicamente correto.

Exemplo bloqueado:

> Curadoria Salomon XT-6 na LK Sneakers: modelos técnicos com estética outdoor urbana, colorways claras e atendimento humano para orientar a escolha com segurança.

Motivo: genérico, pouco premium, pouca densidade editorial, parece placeholder e não sustenta tráfego pago/orgânico.

## Regra obrigatória
Antes de criar ou atualizar coleção/guia LKGOC, o agente deve gerar e validar um **Description Packet** com:

1. **Descrição curta da coleção** (`collection.body_html` quando aplicável): 1–2 frases, premium, específica do modelo/linha e com curadoria LK.
2. **Hero intro**: texto editorial mais rico, sem soar como sistema.
3. **SEO/meta description** quando fizer parte do pacote: comercial, clara e sem prometer disponibilidade.
4. **Guia intro/final text**: coerente com Gold Source 204L, sem duplicar frases genéricas.
5. **Termos proibidos ou fracos**: “modelos técnicos” sem contexto, “atendimento humano” como enchimento, “orientar com segurança” como CTA genérico, repetição de “curadoria” sem especificidade.
6. **Tom LK**: premium, minimalista, humano, comercial; foco em seleção, autenticidade, construção técnica, estética, presença e composição.

## Acceptance test
A descrição só passa se responder:

- Qual é a silhueta/modelo?
- O que torna a seleção desejável?
- Qual é a leitura estética/comercial?
- A frase parece escrita para cliente premium, não para checklist interno?
- Evita prometer estoque, pronta entrega, prazo ou disponibilidade?

Se falhar, status: `COPY_BLOCKED / NÃO LKGOC`.

## Exemplo aprovado — Salomon XT-6

> Seleção LK de Salomon XT-6 em colorways claras e sofisticadas, unindo construção técnica, estética outdoor contemporânea e curadoria exclusiva para quem busca presença, conforto e autenticidade.

Versão curta:

> Curadoria LK de Salomon XT-6 em colorways claras, com construção técnica, estética outdoor contemporânea e presença sofisticada.

## Implicação operacional
Todo bootstrap LKGOC deve incluir este gate antes de qualquer write Shopify, mesmo em DEV/unpublished. Se for necessário escrever placeholder técnico, ele deve ser marcado explicitamente como `COPY_PLACEHOLDER_BLOCKED` e não pode ir para approval/publish.
