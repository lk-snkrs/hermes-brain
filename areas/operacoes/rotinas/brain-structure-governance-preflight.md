# Rotina — Brain Structure Governance Preflight

## Objetivo

Impedir que o Hermes “continue criando coisa” no Brain antes de validar a estrutura correta.

Esta rotina é o gate documental antes de criar, mover ou alterar `skills/`, `agentes/`, `USER.md`, `AGENTS.md`, `HEARTBEAT.md`, rotinas, crons, regras de agente ou qualquer reorganização relevante do Hermes Brain.

## Quando usar

Usar antes de:

- criar ou editar skill canônica;
- criar agente, subagent, canal permanente, heartbeat ou rotina recorrente;
- adaptar material Bruno/OpenClaw, Pixel AI Hub, Brainzinho, Amora ou curso externo;
- reorganizar pastas do Brain;
- mover conteúdo entre Lucas pessoal, LK, Zipper, SPITI, Operações, Tecnologia ou Governança;
- transformar uma ideia em automação/cron.

## Princípio

Antes de alimentar conteúdo, validar a estrutura.

O agente não deve mudar identidade, skills ou configuração operacional se ainda não sabe:

1. onde o conteúdo deve morar;
2. quem é o dono;
3. qual camada é fonte de verdade;
4. quais riscos existem;
5. o que será tocado e o que não será tocado.

## Workflow obrigatório

### 1. Classificar escopo e dono

Responder internamente:

- Contexto: Lucas pessoal, LK, Zipper, SPITI, Operações, Tecnologia, Governança ou multiempresa?
- Tipo: documentação, rotina, skill, agente, cron, integração, produção ou externo?
- Risco: read-only/documental, write local, external-send, produção/infra, credencial ou destrutivo?
- Dono: Hermes Geral ou especialista documentado?

### 2. Auditar estrutura atual antes de mexer

Ler/inspecionar os arquivos relevantes antes de escrever:

- `START-HERE.md`, `MAPA.md`, `areas/MAPA.md`, `empresa/MAPA.md` quando for navegação global;
- `areas/<area>/MAPA.md` quando for área específica;
- `agentes/<agente>/` quando for identidade/agente;
- `empresa/rotinas/_index.md` quando for rotina;
- `empresa/skills/_index.md` e `skills/` quando for skill;
- `seguranca/permissoes.md` e `seguranca/acoes-sensiveis.md` quando houver risco.
- `areas/operacoes/rotinas/data-boundaries-authorized-summaries.md` quando houver dado vivo, relatório multiempresa, Mission Control ou handoff entre agentes.

### 3. Mapear destino correto

Gerar uma leitura curta:

- árvore/pastas relevantes atuais;
- arquivos que serão criados/alterados;
- área dona;
- índice/MAPA que precisa ser atualizado;
- skill/rotina canônica existente que deve ser reaproveitada;
- fonte de verdade: Brain, Doppler, Shopify, Tiny, Supabase, GitHub, WhatsApp, email, API ou outro.

Separar explicitamente:

- **conhecimento estável**: decisões, contexto, rotinas, skills, PRDs, regras e aprendizados → pode morar no Brain/Git;
- **dado vivo**: pedidos, estoque, margem, faturamento, lances, campanhas, logs, status de deploy/runtime e métricas atuais → consultar fonte viva e, no Brain, registrar apenas snapshot datado, regra, resumo autorizado ou link para artefato.

Quando o material externo usa `pessoal/`, `empresa/` e `diretoria/`, traduzir para o modelo Hermes:

- `pessoal/` → Lucas pessoal / preferências / agenda / inbox pessoal;
- `empresa/` → LK, Zipper, SPITI ou empresa/contexto global;
- `diretoria/` → Governança, decisões, aprovações, riscos, financeiro sensível, segurança e permissões.

### 4. Apontar riscos antes da escrita

Checar explicitamente:

- algo pessoal foi parar em área de empresa?
- algo de empresa ficou em memória pessoal/global sem separação?
- algo sensível deveria estar em Governança/Segurança/Diretoria?
- há duplicação de skill/rotina já existente?
- o arquivo proposto é genérico demais para virar regra operacional?
- falta `MAPA.md`, README, índice ou link de navegação?
- a mudança criaria cron/agente/canal permanente sem kill criteria?
- há dados vivos, secrets, cliente, preço, campanha, proposta ou produção?
- o Hermes Geral/Mission Control precisa mesmo do dado bruto, ou basta um resumo executivo autorizado da área dona?
- o pedido cruza LK, Zipper e SPITI? Se sim, há escopo explícito para cada fonte e foi evitado vazamento cruzado?

### 5. Preview antes de aplicar

Para mudanças documentais locais de baixo risco, o preview pode ser o próprio diff planejado ou commit em branch/worktree.

Para qualquer mudança com risco de produção, externo, credencial, banco, cron runtime, Docker/VPS ou contato com cliente, parar e preparar approval packet com:

- escopo exato;
- evidência;
- diff/preview;
- backup/rollback;
- destinatário/canal se houver externo;
- o que não será tocado.

### 6. Escrever com menor superfície

Se for seguro seguir:

- criar/alterar o menor conjunto de arquivos;
- atualizar MAPA/índice correspondente na mesma rodada;
- não duplicar lógica canônica de skill sem linkar a fonte;
- manter material bruto de terceiro fora do Brain salvo aprovação explícita;
- manter dados vivos/brutos fora do Brain salvo snapshot datado necessário, minimizado e sem PII/secrets;
- para multiempresa, fazer hub-and-spoke: área/agente especialista gera resumo autorizado; Hermes Geral usa síntese para decisão/roteamento, não acesso irrestrito por conveniência;
- não criar cron/UI/runtime por implicação.

### 7. Verificar antes de concluir

Antes de dizer que ficou pronto:

```bash
python3 scripts/brain_health_check.py --json reports/brain-health-check-YYYY-MM-DD-structure-preflight.json
git diff --check
```

Também rodar secret scan para arquivos alterados/untracked ou whole-repo quando a rodada tocar scripts, integrações, agentes, imports ou material externo.

## Saída esperada

```md
## Brain Structure Governance Preflight — YYYY-MM-DD

- Escopo:
- Dono:
- Área correta:
- Arquivos lidos:
- Arquivos a alterar/criar:
- Riscos encontrados:
- Índices/MAPAs a atualizar:
- Aprovação necessária? Sim/Não
- Próxima ação segura:
- O que não será tocado:
```

## Aprovação necessária

Não precisa para leitura, auditoria, documentação local, branch/worktree, relatório, PRD, MAPA/índice e commit documental de baixo risco.

Precisa aprovação explícita atual de Lucas para:

- envio externo ou contato com cliente/fornecedor/colecionador;
- campanha, post, proposta, preço, negociação ou publicação;
- produção, deploy, banco, Shopify/Tiny/Merchant/Klaviyo/Meta/Supabase write;
- Docker/VPS/root/SSH/Traefik/volumes/redes;
- criar/alterar cron runtime, agente/canal permanente ou automação recorrente;
- mexer em secrets, permissões reais ou credenciais.

## Relação com Brain Improvement Score

O `Brain Improvement Score` usa esta rotina como gate qualitativo: a nota é útil apenas se vier depois da validação de estrutura e se as recomendações forem priorizadas por risco, não por vaidade de score.
