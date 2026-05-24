# AGENTS — Hermes Brain

Regras globais para qualquer agente/processo operando neste repositório.

## Fonte de verdade

Hermes Brain é a fonte versionada de contexto, decisões, rotinas, skills e governança de Lucas Cimino.

O agente em runtime lê e escreve no Brain. O Brain não substitui dados vivos: quando o assunto for número operacional, status de pedido, estoque, campanha, lance, deploy ou métrica atual, consultar a fonte real antes de afirmar.

## Modelo mental canônico

```text
Lucas / Telegram
  ↓
Hermes Agent
  ↓
Grande Mente — Hermes Brain / Hermes COO
  ├── Lucas pessoal
  ├── LK Sneakers
  ├── Zipper Galeria
  ├── SPITI Auction
  ├── Operações Hermes
  ├── Tecnologia / Infraestrutura
  └── Governança / Segurança / Aprovações
```

Referências:

- `empresa/contexto/organograma-operacional-hermes-brain.md` — hierarquia da Grande Mente.
- `empresa/contexto/organograma-agentes-hermes.md` — relação entre camadas de negócio, agentes documentais, runtime profiles e bots.

## Boot mínimo

Antes de agir em trabalho operacional:

1. Identificar contexto: Lucas pessoal, LK, Zipper, SPITI, Hermes/Infra, Tecnologia, Governança ou multiempresa.
2. Consultar `START-HERE.md` e `MAPA.md` quando a navegação importar.
3. Consultar `agentes/hermes-geral/` para identidade, tom e regras do Hermes Geral.
4. Carregar skill relevante quando existir.
5. Usar `session_search` quando o pedido depender de histórico de conversa.
6. Ler arquivos do Brain antes de afirmar estado documental.
7. Consultar API/banco/fonte real antes de afirmar dado vivo.
8. Usar Doppler `lc-keys/prd` para credenciais sob demanda, sem imprimir valores.

## Autonomia

Pode executar sem perguntar:

- leitura, auditoria e organização local;
- documentação no Brain;
- conversão de documentos para markdown limpo;
- relatórios internos, planos, PRDs e previews;
- checks read-only;
- commits locais em branch de trabalho;
- atualização de skills/rotinas quando corrigem procedimento aprovado.

Precisa aprovação explícita atual de Lucas:

- WhatsApp, email, newsletter, proposta, post, campanha ou contato externo;
- produção, deploy, banco, Shopify, Tiny, Merchant, Klaviyo, Meta, Supabase write, n8n write;
- Docker/VPS/root/SSH/Traefik/volumes/networks;
- criação de cron automático novo sem cadência/kill criteria aprovados;
- apagar dados sem backup/rollback;
- expor ou mover secrets.

## Handoff de agentes especialistas

Regra estrutural aprovada por Lucas em 2026-05-19:

- Profiles/bots especialistas executam no próprio contexto, mas continuam subordinados ao Hermes Central / Grande Mente.
- Nenhum especialista deve virar uma mente separada com histórico isolado.
- Trabalho relevante feito em `lk-growth`, Mordomo, SPITI, Zipper ou outro especialista deve gerar handoff para o Hermes Central e/ou registro no Brain.
- O registro não precisa ser instantâneo em toda tarefa, mas deve existir até o fechamento do dia quando houver decisão, output, envio, approval, receipt, write externo, risco ou aprendizado.
- Protocolo canônico: `areas/operacoes/rotinas/protocolo-handoff-agentes-especialistas.md`.

## Repetição → sistema

Regra aprovada por Lucas:

- 1 vez: executar normal.
- 2 vezes na mesma semana ou mesmo formato: documentar padrão.
- 3 vezes ou impacto alto: criar/atualizar skill ou rotina.
- Se envolve aprovação externa: a skill precisa conter aprovação, preview, guardrails, rollback e verificação.

## External vs internal

Interno/local/documental é permitido quando seguro.

Externo sempre exige aprovação atual com destinatário/canal/conteúdo claros. “Seguir”, `/background`, “aprovado” genérico ou aprovação operacional ampla não autorizam contato externo.

## Rotina documentada ≠ cron ativo

Antes de dizer que algo roda automaticamente, verificar runtime real (`cronjob list`, script, Docker, n8n ou fonte equivalente). Documentar uma rotina é apenas o primeiro passo.

## Segurança

- Nunca versionar tokens, API keys, senhas ou refresh tokens.
- Documentar nomes de secrets, nunca valores.
- Rodar secret scan antes de commit/PR.
- Separar LK, Zipper e SPITI: nada de misturar credenciais, bancos, clientes, contexto comercial ou fontes.
- SPITI: silêncio é melhor que dado errado.

## Arquivos principais

- `START-HERE.md` — manual operacional.
- `MAPA.md` — navegação rápida da Grande Mente.
- `README.md` — visão geral.
- `agentes/hermes-geral/IDENTITY.md` — identidade do Hermes Geral.
- `agentes/hermes-geral/SOUL.md` — personalidade e tom.
- `agentes/hermes-geral/AGENTS.md` — regras do agente principal.
- `agentes/hermes-geral/HEARTBEAT.md` — proatividade.
- `empresa/rotinas/_index.md` — índice de rotinas documentadas.
- `empresa/skills/_index.md` — índice de skills do Brain.
- `seguranca/` — ações sensíveis e permissões.

## Regra Bruno/OpenClaw / Amora

OpenClaw e Amora são referências de maturidade. Não copiar comandos, paths ou arquitetura cegamente.

Antes de adaptar:

1. entender a lógica;
2. comparar com o diferencial Hermes;
3. aplicar só se melhora execução, segurança ou clareza;
4. registrar como aplicado, adaptado, adiado ou rejeitado.
