# PRD — Pixel AI Hub / Brainzinho / Openclawzinho Learning Loop no Hermes Agent

Atualizado em: 2026-05-25
Owner: Hermes Agent / Operações Hermes
Status: migração documental aprovada por Lucas; migração de cron real ainda exige alteração controlada no scheduler
Origem histórica: `/opt/data/profiles/mordomo/docs/prd-pixel-ai-hub-daily-learning.md`

## 1. Resumo executivo

O loop diário Pixel AI Hub / Brainzinho / Openclawzinho deve pertencer ao **Hermes Agent central / Operações Hermes**, não ao Mordomo operacional.

Motivo: esse fluxo não é atendimento, cliente, agenda ou follow-up pessoal. É benchmark e melhoria contínua do próprio Hermes: Brain, skills, rotinas, PRDs, Mission Control, governança e comportamento de agentes.

## 2. Princípio de ownership

- **Fonte lida**: grupos/chats de aprendizado como Pixel AI Hub, Brainzinho e Openclawzinho.
- **Executor conceitual**: Hermes Agent / Operações Hermes.
- **Não executor**: Mordomo de WhatsApp pessoal, exceto como superfície técnica de leitura se a fonte estiver no WhatsApp pessoal e não houver outro conector.
- **Destino durável**: `areas/operacoes/`, `reports/governance/`, skills/rotinas/PRDs do Hermes central.
- **Entrega a Lucas**: só quando houver aprendizado relevante, decisão necessária ou bloqueio; silêncio em OK/no-op.

## 3. Não objetivos

Este loop não deve:

- responder no WhatsApp;
- virar alerta em tempo real;
- tratar comunidade como lead, suporte ou CRM;
- copiar dumps, prints crus ou material proprietário/extenso para o Brain;
- salvar PII desnecessária;
- implementar mudanças sensíveis automaticamente;
- ficar acoplado ao Mordomo como dono do raciocínio.

## 4. Matriz Bruno/OpenClaw → Hermes

Para cada aprendizado incluído no digest:

1. O que foi discutido, em síntese própria.
2. O que Hermes já faz melhor/diferente.
3. Se melhora ou burocratiza.
4. Versão Hermes-native.
5. Recomendação: aplicar, adaptar, adiar ou ignorar.
6. Destino: skill, rotina, PRD, Brain, Mission Control, backlog ou nenhum.

## 5. Saída esperada

Digest máximo de 1–5 aprendizados, em português brasileiro, com formato:

```markdown
## Pixel AI Hub — aprendizado diário
Janela: últimas 24–36h
Fontes: Brainzinho / Openclawzinho / Pixel AI Hub
Status: read-only; nenhuma resposta enviada

### 1. [Título]
- Lição: ...
- Hermes hoje: ...
- Julgamento: melhora / burocracia / depende
- Versão Hermes-native: ...
- Recomendação: aplicar / adaptar / adiar / ignorar
- Destino sugerido: skill / rotina / PRD / Brain / Mission Control / backlog
```

## 6. Aplicação imediata aprovada por Lucas em 2026-05-25

Lucas apontou que os itens 1 e 2 do digest de 2026-05-25 devem ser feitos no Hermes Agent, não no Mordomo.

Itens promovidos:

1. **Auditoria de crons não pode ser “cego olhando o próprio umbigo”**
   - Destino: `areas/operacoes/rotinas/hermes-agent-cron-e-performance-diagnostico.md`.
   - Owner: Hermes Agent / Operações.

2. **Performance de agente: investigar contexto e tool calls antes de “limpar tudo”**
   - Destino: `areas/operacoes/rotinas/hermes-agent-cron-e-performance-diagnostico.md`.
   - Owner: Hermes Agent / Operações.

## 7. Migração do cron real

O cron histórico existe no profile Mordomo como `Pixel AI Hub / Brainzinho daily learning scan`, com prompt e skill do digest.

A intenção de produto agora é:

- pausar/remover o ownership operacional do Mordomo;
- recriar/transferir o job para o runtime/profile do Hermes Agent central;
- manter a fonte WhatsApp read-only se ainda for tecnicamente necessária;
- alterar o prompt para remover “Você é o Mordomo Hermes” e usar “Você é o Hermes Agent / Operações Hermes”;
- manter `deliver=origin` somente para aprendizados relevantes; silent-OK quando sem achado.

Essa migração altera scheduler/cron real. Deve ser feita via `hermes cron`/ferramenta de cron, com backup do registro antes/depois, e não por edição manual de `jobs.json`.

## 8. Preview de prompt corrigido

```text
Você é o Hermes Agent central de Lucas Cimino, operando a área Operações Hermes / Hermes Brain.

Tarefa diária de fim de dia: revisar em modo read-only os grupos/chats Pixel AI Hub, Brainzinho e Openclawzinho como fonte de aprendizado Bruno/OpenClaw para melhoria do Hermes Agent, Hermes Brain, skills, rotinas, PRDs, Mission Control e governança.

Regras obrigatórias:
- Não envie, responda, reaja, encaminhe nem interaja no WhatsApp.
- Não copie dumps, prints crus, material extenso de terceiros, PII desnecessária nem segredos.
- Não implemente mudanças sensíveis automaticamente.
- Não trate Brainzinho/Openclawzinho/Pixel AI Hub como lead, suporte comercial ou alerta em tempo real.
- Use apenas síntese própria e operacional.
- Se não houver aprendizado relevante, fique silencioso quando tecnicamente possível.

Processo:
1. Inspecione read-only as mensagens recentes, janela padrão 24–36h, dos chats/labels relacionados a Pixel AI Hub, Brainzinho e Openclawzinho.
2. Agrupe tópicos e descarte ruído.
3. Para cada item relevante, aplique a matriz Bruno → Hermes.
4. Entregue no máximo 1–5 aprendizados úteis para Lucas.
5. Se houver proposta sensível/externa/produtiva, apresente como recomendação/preview, não execute.
```

## 9. Critérios de aceite da migração real

- Job novo/transferido roda no profile/runtime Hermes Agent central.
- Prompt não se identifica como Mordomo.
- Output durável cai em `areas/operacoes/` ou `reports/governance/`.
- Sem WhatsApp send/reply/react/forward.
- Sem raw dump de comunidade no Brain.
- No-op fica silencioso.
- Registro de cron-control-plane atualizado com owner e kill criteria.
- Backup antes/depois do scheduler salvo em `reports/governance/cron-registry-backups/`.

## 10. Rollback

Se a migração gerar ruído, falha de fonte ou perda de leitura:

1. Pausar o novo cron Hermes Agent.
2. Reativar o job anterior no Mordomo somente como executor técnico temporário, com prompt corrigido e owner documental Hermes Agent.
3. Registrar receipt em `reports/governance/`.
4. Ajustar skill/rotina antes de nova tentativa.
