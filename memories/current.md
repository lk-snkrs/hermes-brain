# Contexto quente — Hermes Brain

Data de normalização: 2026-05-19  
Escopo: camada canônica de leitura rápida para prioridades, bloqueios, decisões recentes, próximos eventos e riscos.  
Status: documento versionado; não substitui dados vivos de banco/API/cron.

## Como usar

Ler este arquivo no boot quando a pergunta depender de estado atual, antes de abrir relatórios longos. Em seguida confirmar em fontes específicas:

1. `memories/pending.md` para tarefas pendentes.
2. `memories/decisions.md` para decisões permanentes.
3. `memories/lessons.md` para lições operacionais.
4. `empresa/rotinas/_index.md` e `empresa/skills/_index.md` para processos canônicos.
5. Fonte viva quando o assunto for número, pedido, estoque, campanha, deploy, cron, canal externo ou runtime.

## Prioridades quentes

- BRUNO-ATUAL: fechar gaps P0 documentais seguros no Brain sem copiar material bruto de terceiro.
- Segundo cérebro: manter Hermes Brain como fonte versionada de contexto, decisões, rotinas, skills e governança; Mem0/session_search são índices auxiliares, não fonte primária.
- LK/Zipper/SPITI: preservar separação de contexto, credenciais, clientes, dados e decisões.
- Operações Hermes: diferenciar sempre rotina documentada de cron/runtime realmente ativo.

## Bloqueios e guardrails ativos

- Material bruto de curso/terceiros permanece fora do Brain; versionar apenas auditorias, decisões e adaptações Hermes-native.
- Sem Docker, VPS, root/SSH, Traefik, volumes, redes, deploy ou runtime sem aprovação explícita e escopo atual.
- Sem envio externo por WhatsApp, email, campanha, post, proposta ou contato com cliente/colecionador sem aprovação de Lucas para conteúdo/canal/destinatário.
- Sem credenciais no repositório. Documentar nomes de secrets quando necessário, nunca valores.
- Dados operacionais atuais exigem fonte viva antes de afirmar.

## Decisões recentes relevantes

- A auditoria BRUNO-ATUAL concluiu que o segundo cérebro do Hermes está **direcionalmente correto**, mas não 100% pronto: nota geral inicial 8,0/10 na arquitetura e cerca de 6,8/10 na correção operacional antes dos P0 desta rodada.
- Gaps P0 documentais seguros tratados nesta rodada: camada `current/hot`, inventário runtime/profile/canal, auditoria de skills e documentação do Mordomo.
- Ainda não chamar de 10/10: há herança OpenClaw/`cerebro-cimino`, runtime/crons a reconciliar continuamente com fonte viva e Mission Control a simplificar como Mesa COO.
- Mesa COO diária foi operacionalizada no Telegram: skill `/mesa` criada e cron `749ee30b51eb` agendado para 08h30 BRT, entrega `origin`, sem writes externos.
- Mission Control exige reconciliação própria; este contexto aponta o trabalho de UI/produto sem autorizar deploy/runtime.

## Por área

### Lucas / Hermes Geral

- Hermes Geral é o Chief of Staff/Grande Mente: coordena áreas, roteia contexto e protege aprovações.
- Correções recorrentes de Lucas devem virar memória, rotina ou skill conforme a regra repetição → sistema.

### LK Sneakers

- Operação tem múltiplas rotinas de SEO/CRO, GMC, Shopify, Tiny, Growth e relatórios. Antes de afirmar execução automática, verificar cron real.
- Campanhas, Klaviyo, WhatsApp, Shopify visível, compra/fornecedor e alterações de produto/preço/estoque exigem aprovação quando aplicável.

### Zipper Galeria

- Usar tom consultivo e sofisticado; vendas reais dependem de fontes documentadas, especialmente `vendas_tango` quando disponível.
- Contato com artista, colecionador, lead ou parceiro exige preview e aprovação.

### SPITI Auction

- Silêncio é melhor que dado errado. Lances/lotes precisam de hierarquia de evidência e fonte viva antes de resposta operacional.

### Operações Hermes

- Inventário vivo de runtime/profile/canal fica em `areas/operacoes/rotinas/runtime-profile-channel-inventory-2026-05-19.md`.
- Auditoria de skills fica em `empresa/skills/skill-audit-2026-05-19.md`.
- Mordomo passa a ter documentação de agente/profile em `agentes/mordomo/`.

## Próximos checks recomendados

- Atualizar este arquivo quando uma decisão quente mudar ou quando um P0 passar de pendente para concluído.
- Ao iniciar trabalho de runtime real, rodar inventário live autorizado e atualizar o documento de runtime com evidência e timestamp.
- Ao promover rotina recorrente a skill, atualizar a auditoria de skills e o índice canônico.
