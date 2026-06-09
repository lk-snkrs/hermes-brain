# Handoff Mordomo → Agente LC Hermes Central

Data/hora: 2026-06-09T00:05:22+00:00
Agente/profile: Mordomo (`mordomo`)
Empresa/área: Agente LC Hermes / Governança do Brain / Arquitetura de contexto
Responsável humano: Lucas Cimino

## Pedido original

Lucas aprovou/promoveu a regra de governança:

> Para catálogos e bases grandes: `resumo.md` + índice + docs por categoria + fonte viva consultável; nunca dump integral no Brain.

E pediu handoff para o agente LC Hermes com recomendação da próxima ação.

## O que foi feito

Este handoff registra a decisão como pauta sistêmica para o agente LC Hermes Central, porque a regra afeta arquitetura de Brain, Mission Control, subagentes, skills, ingestões, bases vivas e governança multiempresa.

## Fontes usadas

- `areas/operacoes/rotinas/protocolo-handoff-agentes-especialistas.md`
- `areas/operacoes/MAPA.md`
- `AGENTS.md` do Hermes Brain, que já contém a fronteira geral: Brain não substitui dados vivos; consultar fonte real antes de afirmar dado operacional atual.

## Decisão / regra proposta

O Brain deve guardar contexto versionado, decisões, rotinas, índices, resumos, documentação e governança.

O Brain **não** deve virar depósito integral de dados vivos, catálogos grandes, histórico transacional completo, mensagens brutas, tabelas operacionais extensas, dumps de Shopify/Tiny/Supabase/WhatsApp/e-mail/Meta/GA4 ou bases que mudam continuamente.

Para bases grandes ou vivas, o padrão recomendado é:

1. `resumo.md` — visão executiva, escopo, dono, atualização, fonte primária e limites.
2. `MAPA.md` ou índice — navegação por categorias, objetos, relatórios e queries.
3. Docs por categoria — regras, interpretações, decisões, exceções e uso operacional.
4. Fonte viva consultável — banco/API/arquivo controlado/runtime real como fonte operacional.
5. Receipts/handoffs — evidência de decisões, writes, aprovações, outputs e mudanças relevantes.
6. Source Confidence — cada afirmação deve indicar se veio de fonte viva, snapshot, documento, inferência ou histórico.

## Por que importa

- Reduz entropia e custo de contexto.
- Evita que agentes carreguem dumps enormes e obsoletos.
- Mantém o Brain como camada de inteligência/governança, não como réplica frágil de bancos.
- Força consulta à fonte real antes de afirmar estoque, preço, pedidos, disponibilidade, campanha, status de cliente, lote, lance, deploy ou métrica atual.
- Facilita subagentes com contexto mínimo: índice primeiro, fonte sob demanda, handoff compacto.

## Próxima ação recomendada para o agente LC Hermes

Criar uma rotina/política canônica em `areas/operacoes/rotinas/` chamada, por exemplo:

`brain-fonte-viva-e-dados-grandes.md`

Conteúdo mínimo recomendado:

1. Definir a fronteira Brain vs fonte viva.
2. Definir padrões por tipo de dado:
   - catálogo/produto/estoque;
   - CRM/contatos/conversas;
   - campanhas/ads/analytics;
   - propostas/PDFs/artistas/obras;
   - logs/runtime/deploy/crons;
   - documentos estratégicos/decisões.
3. Criar matriz: “guardar no Brain”, “guardar só índice/resumo”, “consultar fonte viva”, “proibido persistir bruto”.
4. Adicionar checklist para novos PRDs/ingests/subagentes:
   - Qual é a fonte viva?
   - O que entra como resumo/índice?
   - Qual freshness esperada?
   - Qual dado é PII/sensível?
   - Qual consulta read-only valida afirmações atuais?
   - Qual receipt/handoff deve ficar versionado?
5. Atualizar `areas/operacoes/MAPA.md` com a nova rotina.
6. Se aprovado pelo LC Hermes, promover a regra para skills relevantes: `lucas-chief-of-staff`, `hermes-agent`, `obsidian`, `ocr-and-documents`, `google-workspace`, `lk-shopify-readonly`, `lk-operational-intelligence`, `wacli-whatsapp-cli` e rotinas de ingestão.

## Critério de pronto

- Existe rotina canônica no Brain.
- `areas/operacoes/MAPA.md` aponta para ela.
- A rotina tem matriz Brain vs fonte viva.
- Próximos PRDs/ingests passam a declarar fonte viva, resumo, índice, freshness e política de persistência.
- Nenhum dump integral novo de base viva entra no Brain sem justificativa explícita.

## Riscos / bloqueios

- Não fazer mudança runtime/produção aqui.
- Não mover ou apagar dados existentes sem inventário, backup e plano de rollback.
- Não transformar a regra em burocracia: para docs pequenos/estáticos, arquivo completo no Brain continua correto.

## Onde foi documentado no Brain

`areas/operacoes/handoffs/handoff-lc-hermes-brain-fonte-viva-governance-20260609T000522Z.md`
