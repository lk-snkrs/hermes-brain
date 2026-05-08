# Material externo → documentação → PRD

## Objetivo

Transformar qualquer pacote externo enviado pelo Lucas — ZIP, pasta, curso, documentação, transcrição, template, starter kit ou export — em documentação rastreável, comparação com o Hermes Brain e PRD implementável, sem copiar material cegamente e sem tocar produção antes de aprovação.

Esta rotina nasceu da análise do upload Bruno/OpenClaw atualizado de 2026-05-08. A conclusão principal daquela rodada foi: o Hermes não deve virar OpenClaw; deve usar o que é útil como sistema de melhoria contínua.

## Área dona

Operações / Hermes Geral.

## Agenda

Sob demanda, quando Lucas enviar material externo ou pedir para “ler tudo”, “pensar se está ok”, “documentar” ou “fazer um PRD”.

Pode virar revisão semanal apenas depois de existir volume recorrente de pacotes/PRDs pendentes.

## Skill/script executado

- Skill operacional externa: `bruno-openclaw-hermes-brain-adaptation`, quando o material tiver relação com Bruno/OpenClaw.
- Skills auxiliares: workflow de PR quando a fase virar branch/PR; Doppler/GitHub safe workflow quando houver push.
- Scripts locais podem ser criados para extração/inventário, mas a rotina não depende de produção nem de VPS.

## Entrada esperada

- Caminho do ZIP/pasta/documento.
- Contexto mínimo: origem do material, objetivo do Lucas, se é apenas análise ou se já há autorização para PR.
- Se o material envolver credenciais, tokens, dumps ou dados pessoais: tratar como sensível e redigir valores.

## Saída obrigatória

Para cada ingestão relevante, gerar uma pasta de análise fora do repo de produção com:

- `TREE.md`: árvore limpa do pacote.
- `inventory.md`: inventário humano arquivo por arquivo.
- `inventory.json`: inventário estruturado quando útil.
- `texts/`: textos extraídos por arquivo.
- `corpus_all_text.md`: corpus consolidado.
- documentação executiva do pacote.
- análise aula/bloco/pasta quando aplicável.
- PRD ou plano de adaptação.

Para o Hermes Brain, registrar apenas o que for decisão, rotina, template ou plano reaproveitável. Não versionar material bruto de terceiros sem necessidade.

## Fluxo operacional

### 1. Preparar área segura

1. Criar diretório de trabalho fora do repo principal, normalmente em `/opt/data/hermes_bruno_ingest/`.
2. Nunca extrair diretamente dentro de `hermes-brain`.
3. Verificar se o arquivo existe e registrar caminho original.
4. Criar pasta com timestamp ou nome inequívoco.

### 2. Extrair com segurança

1. Proteger contra zip-slip: rejeitar paths absolutos ou com `..`.
2. Ignorar `__MACOSX`, `.DS_Store` e AppleDouble (`._*`).
3. Extrair nested ZIPs para subpasta própria de análise, sem sobrescrever fonte.
4. Preservar nomes de arquivos quando possível, mas gerar paths seguros para textos extraídos.

### 3. Inventariar

Gerar inventário com, no mínimo:

- path relativo;
- tipo/extensão;
- tamanho;
- origem: pacote principal ou nested ZIP;
- se foi extraído para texto;
- observações de risco: segredo, dados pessoais, binário, redundância.

### 4. Extrair texto

Prioridade:

1. Markdown, TXT, CSV, JSON, YAML e SRT: leitura direta.
2. DOCX: extrair XML interno e limpar texto.
3. HTML: limpar markup e preservar títulos/seções.
4. PDF: usar apenas quando não houver HTML/MD equivalente ou quando o conteúdo for crítico.
5. Binários, imagens e vídeos: inventariar; analisar só se necessário.

### 5. Ler pasta por pasta

Para cada pasta/bloco relevante, documentar:

- finalidade;
- arquivos principais;
- ideias novas;
- redundâncias;
- riscos;
- o que pode virar rotina, skill, template, projeto ou pendência.

### 6. Comparar com Hermes Brain

Antes de recomendar mudança, ler o Brain atual:

- `START-HERE.md`, `README.md`, `STARTUP.md`, `PROTOCOLS.md`, `TOOLS.md`;
- `memories/` relevantes;
- `empresa/MAPA.md`, `areas/MAPA.md`, `empresa/rotinas/_index.md`, `empresa/skills/_index.md`;
- área/agente/rotina afetada;
- `seguranca/permissoes.md` e `seguranca/acoes-sensiveis.md` se houver execução, credenciais ou contato externo.

### 7. Decidir Hermes-native

Para cada conceito importante, preencher a matriz:

- O que o material ensina?
- O que Hermes já faz melhor/diferente?
- Isso reduz fricção ou cria burocracia?
- Versão Hermes-native.
- Decisão: aplicar, adaptar, deferir ou rejeitar.
- Impacto em arquivos do Brain.

### 8. Gerar PRD

Usar o template `areas/operacoes/templates/prd-hermes-brain-improvement.md`.

O PRD deve separar claramente:

- fase local/análise;
- fase documentação no Brain;
- fase PR/código;
- fase produção, se existir;
- aprovações necessárias.

### 9. Implementar no Brain só quando fizer sentido

Mudanças permitidas sem aprovação extra quando Lucas disse para seguir:

- documentação local;
- branch/worktree;
- rotinas/templates/índices;
- PR draft.

Mudanças que exigem aprovação explícita:

- merge em `main`;
- deploy;
- Docker/VPS/Traefik/volumes/redes;
- alteração de secrets;
- envio de WhatsApp/email/campanha/post;
- mutação em banco;
- contato com cliente/colecionador/parceiro.

## Doppler keys

Nenhuma por padrão.

Se a etapa virar push/PR em repositório privado, usar apenas nomes de secrets Doppler, sem imprimir valores:

- `GITHUB_TOKEN`, quando aplicável ao `lk-snkrs/hermes-brain`.
- `GITHUB_SPITI_HUB_TOKEN`, quando aplicável ao `spiti-auction/spiti-hub`.

## Como verificar sucesso

Antes de concluir a fase:

1. Confirmar que os artefatos de análise existem.
2. Ler amostra dos documentos gerados.
3. Rodar secret scan nos artefatos criados e no repo se houve alteração versionada.
4. Se o Brain foi alterado: rodar `python3 scripts/brain_health_check.py`.
5. Revisar `git diff --stat` e diff representativo.
6. Confirmar que nenhuma ação externa/produtiva ocorreu.

Critério mínimo: `possible_secrets 0`.

## Se falhar

- Extração falhou: preservar erro, tentar estratégia alternativa e documentar lacuna.
- Texto ilegível: inventariar arquivo e marcar como pendente de OCR/PDF tool.
- Secret encontrado: redigir para `[REDACTED]`/placeholder e rerodar scan.
- Material conflita com Brain: preservar a regra do Brain até Lucas decidir.
- PR bloqueado por credencial: manter commit/local branch, documentar secret Doppler necessário, não pedir token em chat.

## Aprovação necessária

Não precisa para análise local, documentação e PR draft.

Precisa para qualquer ação externa, produção, merge, envio, credencial, mutação de dados ou infraestrutura.
