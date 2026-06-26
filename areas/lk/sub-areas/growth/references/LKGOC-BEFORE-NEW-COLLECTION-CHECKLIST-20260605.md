# LKGOC — Checklist obrigatório antes de nova coleção

Atualizado: 2026-06-05T01:38:46Z

## Objetivo
Evitar repetir os erros das execuções anteriores de LKGOC e preservar o que funcionou antes de iniciar qualquer nova coleção.

## O que NÃO fazer de novo

- Não começar por Shopify/tema sem antes ler o padrão canônico LKGOC, Gold Source 204L, workflow, input contract e evidence packet.
- Não transformar coleção em artigo/blog antes do grid de produto.
- Não criar layout, hero, grid, card, tipografia ou bloco editorial novo “porque ficou bonito”; seguir a lógica LKGOC/204L.
- Não reaproveitar snippet legado específico por coleção como base de crescimento, especialmente padrões `lk-samba-*`, `lk-sambae-*`, `lk-lkgoc-*`.
- Não validar apenas presença de HTML; medir no browser real desktop/mobile.
- Não pedir approval sem preview direto, screenshots desktop/mobile, scorecard, limitações e rollback.
- Não fazer production write sem aprovação explícita atual de Lucas, backup/readback/receipt.
- Não apresentar draft local/Brain como se fosse resultado final visual; resultado visual precisa de DEV preview quando houver mudança de tema/página.
- Não resolver LKGOC com remendo incremental quando a página pede rewrite/refactor canônico.
- Não duplicar FAQ visual/schema nem criar bloco citável sem fonte/evidência.
- Não usar “pronta entrega/encomenda/estoque” como linguagem/taxonomia pública da loja; disponibilidade e prazo ficam para atendimento/chat.

## O que funcionou e deve ser repetido

- Para approvals no Telegram, preferir botões inline com escopo claro em vez de pedir aprovação textual manual.

- Usar Gold Source 204L como fonte visual e funcional principal.
- Trabalhar em DEV/preview primeiro; produção só depois de approval escopado.
- Separar coleção + guia dedicado como pacote LKGOC, com fluxo: coleção produto-first -> guia -> seleção -> FAQ/trust.
- Preencher input contract e evidence packet antes da copy final.
- Usar camada SEO/GEO com intenção de busca, blocos citáveis, FAQ e schema quando aplicável.
- Usar namespace canônico `lk-goc-*` e componente parametrizado em vez de snippets legados por coleção.
- Fazer readback Asset API/HTML depois de alteração em DEV.
- Fazer QA com browser real:
  - desktop e mobile;
  - screenshots;
  - largura/tipografia computadas;
  - clique real em interações mobile, como “Ler mais”.
- Rodar scorecard LKGOC; mínimo recomendado para approval: 85/100.
- Enviar approval packet curto: preview, score, evidências, limitações, risco, rollback e decisão pedida.
- Registrar receipt/rollback e revisar impacto depois da publicação.

## Fontes canônicas a abrir antes de executar

- `LKGOC-PADRAO-CANONICO.md`
- `LKGOC-EXECUTION-WORKFLOW.md`
- `LKGOC-INPUT-CONTRACT.md`
- `LKGOC-EVIDENCE-PACKET.md`
- `LKGOC-SCORECARD-100.md`
- `references/LKGOC-IMPLEMENTATION-GUARDRAIL.md`
- `references/lkgoc-good-bad-examples.md`
- `references/lkgoc-gold-source-204l/README.md`
- `references/lkgoc-gold-source-204l/ADIDAS-SAMBA-INCIDENT-20260603.md`
- `references/lkgoc-gold-source-204l/LKGOC-NO-LEGACY-SNIPPET-RULE-20260603.md`
- `templates/lkgoc-liquid-contract.md`
- `templates/lkgoc-copy-template.md`

## Critério para começar nova coleção

Só iniciar execução quando houver:

1. handle/URL da coleção alvo;
2. objetivo comercial;
3. produto/modelo principal;
4. evidência mínima de demanda ou prioridade comercial;
5. nível LKGOC definido: Full, Lite, Correção ou Não-LKGOC;
6. plano DEV/preview sem production write automático.

## Regra operacional

Para a próxima coleção, primeiro preparar o pacote LKGOC e preview em DEV. O pedido de aprovação deve vir depois da evidência visual e técnica, nunca antes.


## Guardrail obrigatório — remover FAQ/descrição legado `coll-rich-content`

Registrado em: 2026-06-05T17:42:57

Para qualquer coleção otimizada com LKGOC, o bloco legado `.coll-rich-content` — especialmente a seção antiga de **Perguntas frequentes** — deve ser removido/ocultado no escopo da coleção otimizada. QA obrigatório: não pode haver `.coll-rich-content` visível nem FAQ antigo duplicado depois do LKGOC.

Fonte: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/rules/REGRA-LKGOC-REMOVER-COLL-RICH-CONTENT-LEGADO.md`
