# Rotina — Brain Sync Seguro

Status: **ativo como etapa pós-Fechamento Ágil 23h**
Criada: 2026-05-20 UTC
Área: Operações / Hermes Brain / Versionamento

## 1. Objetivo

Versionar no GitHub as mudanças documentais relevantes do Hermes Brain após consolidações, evitando perda de contexto da Grande Mente sem transformar o sync em um canal de vazamento de segredo ou artefatos pesados.

Princípio: **se importa para o Brain, deve estar versionado; se contém segredo/infra/bruto, deve ficar fora do push automático.**

## 2. Script operacional

Executor aprovado:

```text
/opt/data/scripts/brain_sync_safe.py
```

Executor legado bloqueado:

```text
scripts/brain_sync.sh
```

`./scripts/brain_sync.sh` é histórico/OpenClaw-era e deve sair com `DEPRECATED` sem tocar SSH/VPS/arquivos. Não usar helper de senha SSH, paths legados de root ou sync bidirecional manual como fonte de verdade.

Uso pelo fechamento:

```bash
/opt/data/scripts/brain_sync_safe.py --push
```

Uso de auditoria manual:

```bash
/opt/data/scripts/brain_sync_safe.py --dry-run --verbose
```

## 3. Escopo permitido no push automático

O script só pode stagear arquivos em allowlist:

- documentos raiz do Brain (`MAPA.md`, `AGENTS.md`, `CHANGELOG.md`, `README.md`, `START-HERE.md`, `STARTUP.md`, `PROTOCOLS.md`, `TOOLS.md`, `ARCHITECTURE.md`, `ROADMAP-30-DIAS-HERMES.md`);
- `areas/**/*.md`;
- `empresa/**/*.md`;
- `agentes/**/*.md`;
- `memories/**/*.md`;
- `reports/daily-consolidation/**/*.md` e JSONs de fechamento, se existirem;
- `reports/hermes-continuous-improvement/**/*.md`;
- `reports/brain-weekly-panel/**/*.md`;
- `reports/governance/**/*.md` — relatórios curados de governança/auditoria que precisam sobreviver à compactação;
- `reports/brain-health-check-*.json`.

## 4. Escopo proibido

O push automático não deve stagear:

- `.env`, keys, certificados, tokens ou connection strings;
- `config/`;
- `scripts/` e `tests/`;
- `__pycache__`, `.pytest_cache`, `node_modules`, `.venv`, `venv`;
- HTML (`.html`, `.htm`), PDFs, imagens, zips, DBs ou SQLite;
- relatórios brutos/pesados de operação quando não estiverem no escopo do fechamento;
- artefatos de infra, Docker, Traefik, volumes, redes ou VPS.

## 4.1 Política para relatórios

Relatórios só entram no Brain Sync automático quando viram documentação executiva ou evidência de governança. Regra prática:

**Podem virar documentação oficial:**

- `reports/daily-consolidation/*.md` — fechamento diário, curado e sem dados brutos sensíveis;
- `reports/brain-health-check-*.json` — evidência de saúde do Brain;
- `reports/hermes-continuous-improvement/*.md` — melhorias do Hermes já resumidas;
- `reports/governance/*.md` — auditorias/relatórios curados de governança, memória, decisões e guardrails;
- relatórios `.md` promovidos para `areas/**/rotinas/`, `areas/**/reports/` ou `areas/**/contexto/` com síntese, fontes, guardrails e não-ações.

**Devem ficar bloqueados no push automático:**

- HTML de e-mail/preview, CSVs, JSONs brutos, dumps, snapshots privados, receipts operacionais, logs, anexos e arquivos com PII;
- relatórios gerados por crons que ainda não foram curados para narrativa executiva;
- qualquer artefato com credenciais, IDs sensíveis, payloads de API, mensagens completas de cliente ou dados de infraestrutura.

Quando um relatório bruto for importante, criar uma síntese `.md` sob a área correspondente e deixar o bruto local/privado.

## 5. Gates obrigatórios

Antes de commit/push, o script deve:

1. listar mudanças do Git;
2. filtrar por allowlist;
3. bloquear arquivos grandes acima de 512 KB;
4. rodar secret scan nos arquivos permitidos;
5. stagear somente arquivos permitidos;
6. rodar secret scan novamente no staged set;
7. bloquear marcadores de conflito Git (`<<<<<<<`, `=======`, `>>>>>>>`);
8. criar commit convencional `docs: sync Hermes Brain daily consolidation YYYY-MM-DD`;
9. executar `git push origin HEAD:<branch-atual>` apenas se `--push` foi passado.

Se qualquer gate falhar, abortar antes do commit/push.

## 6. Baixo ruído

- Sucesso normal: silencioso/local.
- Falha de secret scan, conflito/push, erro Git ou risco crítico: reportar como exceção curta para Lucas quando o job tiver canal de mensagem habilitado.
- Nunca imprimir segredo; reportar apenas caminho e tipo de padrão detectado.

## 6.1 Auto-remediação

- Falhas A0/A1 do sync seguro — arquivo fora de allowlist, conflito local reexecutável, relatório bruto que precisa de síntese, índice/MAPA faltando, health check local reexecutável — devem iniciar correção local/documental ou gerar síntese/approval packet antes de alertar Lucas.
- Secret scan positivo, push remoto, credencial, GitHub auth, cron schedule/delivery, runtime, Docker/VPS/Traefik ou qualquer write externo continuam approval-gated; nesses casos, abortar antes da mutação e registrar alvo, causa, rollback e verificação esperada.
- Bloqueio por allowlist é proteção normal; só vira alerta se houver mudança Brain importante que precise ser promovida para documentação permitida.

## 7. Relação com Fechamento Ágil 23h

O `Fechamento Ágil 23h` escreve `reports/daily-consolidation/YYYY-MM-DD.md` e, depois da validação local, chama o Brain Sync seguro.

A ordem correta é:

1. consolidar o dia;
2. escrever o relatório no Brain;
3. validar arquivo + secret scan;
4. rodar Brain Sync seguro;
5. se houver erro crítico, notificar Lucas; caso contrário, ficar silencioso.

## 8. Guardrails

- Brain Sync é write no GitHub, mas limitado a documentação/Brain. Não executa writes em Shopify, GMC, WhatsApp, e-mail, banco, Docker, VPS ou gateway.
- O script vive fora do repositório (`/opt/data/scripts`) para não forçar versionamento automático de código operacional.
- Mudanças de escopo da allowlist exigem nova decisão/documentação.
