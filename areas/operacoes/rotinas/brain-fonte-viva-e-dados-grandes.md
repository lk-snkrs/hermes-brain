# Rotina — Brain como índice de fonte viva e dados grandes

Status: canônica
Owner: LC Hermes / Operações Hermes
Criada em: 2026-06-09
Fonte inicial: `areas/operacoes/handoffs/handoff-lc-hermes-brain-fonte-viva-governance-20260609T000522Z.md`

## Regra canônica

O Hermes Brain guarda contexto versionado, decisões, rotinas, índices, resumos, políticas, interpretações, receipts, handoffs e governança.

O Brain **não** deve virar réplica integral de dados vivos, bases grandes ou históricos brutos que mudam continuamente. Para estado atual, número operacional ou dado transacional, o agente deve consultar a fonte viva apropriada antes de afirmar.

Regra prática:

> Brain aponta para a fonte viva; não replica dados grandes.

## O que é fonte viva

Fonte viva é o sistema, API, banco, arquivo controlado ou runtime que contém o estado operacional atual e consultável. Exemplos:

- Shopify/Tiny/GMC/Klaviyo/Meta/GA4/Metricool para produto, estoque, vendas, feed, campanha e métricas.
- Supabase/CRM/planilha operacional autorizada para fila, contato, lead, interesse, proposta ou follow-up.
- WhatsApp/e-mail/Gmail/Calendar/Drive quando a fonte primária do evento ou documento estiver nesses canais.
- GitHub/Vercel/Docker/gateway/cron registry/logs para deploy, runtime, job e status técnico.
- APIs/bancos internos ou arquivos de snapshot datados quando forem a fonte primária documentada.

## Padrão obrigatório para bases grandes ou vivas

Quando uma área precisa representar um catálogo, base, fila, histórico ou sistema vivo no Brain, criar no máximo uma camada documental navegável:

1. `resumo.md` — escopo, dono, fonte primária, freshness esperada, limites, riscos e exemplos de consulta.
2. `MAPA.md` ou índice — navegação por categorias, objetos, relatórios, queries, receipts e fontes.
3. Docs por categoria — regras, interpretações, decisões, exceções, campos relevantes e uso operacional.
4. Fonte viva consultável — banco/API/runtime/arquivo controlado como verdade operacional para estado atual.
5. Receipts/handoffs — evidência datada de decisões, writes, aprovações, outputs e mudanças relevantes.
6. Source Confidence — marcar se a afirmação veio de fonte viva, snapshot, documento, inferência ou histórico.

## Matriz Brain vs fonte viva

### Catálogo, produto e estoque

- Guardar no Brain: estratégia de coleção, regras de curadoria, taxonomia, decisões de copy/SEO, templates, receipts de alteração e links para fonte primária.
- Guardar só índice/resumo: listas grandes de produtos, coleções, variantes, SKUs, imagens e atributos.
- Consultar fonte viva: preço, disponibilidade, estoque, status de publicação, feed GMC, reviews atuais e vendas.
- Proibido persistir bruto sem justificativa: dumps integrais de Shopify/Tiny/GMC, histórico transacional ou dados de cliente.

### CRM, contatos e conversas

- Guardar no Brain: política de atendimento, categorias de decisão, drafts aprovados, decisões sensíveis, handoffs e receipts mascarados.
- Guardar só índice/resumo: filas, cohorts, segmentos, threads e listas de leads.
- Consultar fonte viva: mensagem original, consentimento, status de follow-up, dado de contato, histórico completo e timing atual.
- Proibido persistir bruto sem justificativa: conversas completas, PII, telefones/e-mails em massa, prints ou exports sem minimização.

### Campanhas, ads e analytics

- Guardar no Brain: objetivos, hipóteses, naming conventions, decisões de orçamento, experimentos, aprendizados e relatórios datados.
- Guardar só índice/resumo: dashboards, cohorts, UTMs, campanhas ativas e métricas extensas.
- Consultar fonte viva: CPA, ROAS, spend, receita, conversões, status de campanha, públicos e criativos ativos.
- Proibido persistir bruto sem justificativa: exports completos de plataformas, dados pessoais de audiência e métricas sem data/fonte.

### Propostas, PDFs, artistas, obras e documentos comerciais

- Guardar no Brain: modelo de proposta, política de aprovação, resumo de oportunidade, decisões e receipts.
- Guardar só índice/resumo: acervo grande de PDFs, catálogos, obras, artistas e anexos.
- Consultar fonte viva: arquivo original, versão final, disponibilidade da obra, preço vigente, status da negociação e restrições de envio.
- Proibido persistir bruto sem justificativa: contratos/documentos sensíveis completos, dados bancários, preço privado ou anexos com PII.

### Logs, runtime, deploys e crons

- Guardar no Brain: runbook, inventário documental, kill criteria, receipts de mudança, incidentes resumidos e ponte para registro vivo.
- Guardar só índice/resumo: snapshots datados de registry/log, matriz de owner e status observado.
- Consultar fonte viva: processo atual, estado do gateway, status de cron, porta, container, deploy, branch e log recente.
- Proibido persistir bruto sem justificativa: logs extensos, env dumps, tokens, service-account JSON, comandos sensíveis e segredos.

### Documentos estratégicos, políticas e decisões estáveis

- Guardar no Brain: texto completo quando for pequeno/estático e o Brain for a fonte canônica.
- Guardar só índice/resumo: materiais longos externos, cursos, transcrições e bases de referência volumosas.
- Consultar fonte viva: versão externa atual quando houver fonte primária mutável.
- Proibido persistir bruto sem justificativa: material licenciado/sensível, anexos grandes sem curadoria e cópias que fiquem obsoletas rapidamente.

## Checklist para PRDs, ingests, subagentes e Mission Control

Antes de criar PRD, rotina, subagente, cockpit ou ingestão que toque base grande ou dado vivo, responder:

1. Qual é a fonte viva primária?
2. Quem é o dono operacional da fonte?
3. Qual parte entra no Brain como regra, resumo, índice ou receipt?
4. Qual parte deve permanecer somente na fonte viva?
5. Qual freshness esperada para afirmações atuais?
6. Qual consulta read-only valida status, número, preço, estoque, campanha, lead, pedido, deploy ou fila?
7. Há PII, segredo, dado comercial sensível ou material licenciado?
8. Como minimizar ou mascarar dados persistidos?
9. Qual Source Confidence deve acompanhar a afirmação?
10. Qual receipt/handoff deve ficar versionado depois de decisão, write, aprovação ou output material?

## Critério de aceite para novos artefatos

Um novo artefato passa pela regra quando:

- Declara a fonte viva quando fala de dado operacional atual.
- Não copia dump integral se um resumo/índice resolve.
- Separa documento estável de snapshot datado.
- Usa receipts/handoffs para evidência, não logs brutos.
- Marca limites e freshness.
- Não persiste segredo, PII desnecessária ou base externa sensível.
- Explica como verificar afirmações atuais em read-only antes de agir.

## Exceções permitidas

- Documentos pequenos, estáticos e canônicos podem ficar completos no Brain.
- Snapshots datados podem ser salvos quando são evidência de auditoria, incidente, receipt ou baseline; devem ter data, fonte, escopo e limites.
- Bases derivadas locais podem existir para análise se houver minimização, motivo claro, caminho documentado, secret scan quando aplicável e regra de expiração/atualização.

## Anti-padrões

- Colar export completo de Shopify/Tiny/WhatsApp/e-mail/CRM/ads no Brain para “memória”.
- Responder estoque, preço, pedido, status de campanha, deploy ou fila usando documento antigo sem consultar fonte viva.
- Criar subagente com dump gigante em prompt/contexto em vez de índice + busca sob demanda.
- Usar Brain como banco paralelo sem owner, freshness e validação.
- Versionar logs extensos ou arquivos com segredos.

## Relação com outras rotinas

- `source-confidence.md` — classificar confiabilidade das afirmações.
- `protocolo-handoff-agentes-especialistas.md` — subir decisões e outputs materiais ao Hermes Central sem virar ilha.
- `brain-health-check.md` — validar estrutura, links e higiene.
- `semantic-recovery-session-search.md` — promover achados duráveis de histórico sem copiar conversa inteira.
- `mission-control-brain-cockpit.md` — Mission Control é cockpit/decision inbox, não fonte paralela.

## Regra de promoção para skills

Quando uma skill opera com dados vivos ou grandes, ela deve incorporar esta regra no procedimento: carregar índice/resumo primeiro, consultar fonte viva para estado atual, persistir apenas decisões/receipts/resumos e nunca imprimir ou copiar secrets/PII/dumps brutos.
