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

## 5. Gates obrigatórios

Antes de commit/push, o script deve:

1. listar mudanças do Git;
2. filtrar por allowlist;
3. bloquear arquivos grandes acima de 512 KB;
4. rodar secret scan nos arquivos permitidos;
5. stagear somente arquivos permitidos;
6. rodar secret scan novamente no staged set;
7. rodar `git diff --cached --check`;
8. criar commit convencional `docs: sync Hermes Brain daily consolidation YYYY-MM-DD`;
9. executar `git push origin HEAD:<branch-atual>` apenas se `--push` foi passado.

Se qualquer gate falhar, abortar antes do commit/push.

## 6. Baixo ruído

- Sucesso normal: silencioso/local.
- Falha de secret scan, conflito/push, erro Git ou risco crítico: reportar como exceção curta para Lucas quando o job tiver canal de mensagem habilitado.
- Nunca imprimir segredo; reportar apenas caminho e tipo de padrão detectado.

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
