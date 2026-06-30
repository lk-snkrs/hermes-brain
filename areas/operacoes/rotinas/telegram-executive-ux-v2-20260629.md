# Telegram Executive UX v2 — Onda 0

Data: 2026-06-29  
Status: contrato local/documental aprovado por Lucas.  
Escopo: formato e disciplina de entrega; não altera gateway, scheduler, botões, crons ou delivery.

## Objetivo

Fazer o Telegram parecer uma interface executiva, não um log de sistema.

## Contrato de mensagem executiva

Toda mensagem material para Lucas deve começar pelo resultado humano:

1. **Veredito/resultado**
2. **Por que importa**
3. **Evidência curta**
4. **Próximo passo ou decisão**
5. **Escopo/guardrail quando necessário**

## Não enviar por padrão

- raw JSON;
- wrapper de cron;
- prompt inteiro;
- job_id salvo quando não solicitado;
- logs longos;
- stack traces completos;
- markers técnicos;
- “OK” de rotina saudável;
- paths sem resumo executivo.

## Quando incluir evidência técnica

Inclua somente quando:

- Lucas pediu evidência;
- há bloqueio/risco;
- precisa provar que não houve write externo;
- é receipt de execução sensível;
- há divergência entre documentação e runtime.

Mesmo assim, resumir e redigir.

## Formatos aprovados

### Execução concluída

```markdown
Feito — [resultado humano].

## Evidência
- [gate/comando/fonte]: status
- [artefato]: path

## Não fiz
- sem cron/restart/write externo/etc.

## Próximo passo
[ação única ou decisão]
```

### Decisão

```markdown
## Decisão — [tema]

**Recomendação:** Fazer/Não fazer/Adiar/Piloto.

**Por que importa:** ...
**Escopo se aprovar:** ...
**Bloqueado sem aprovação:** ...
```

### Alerta

```markdown
Atenção — [o que mudou].

**Por que importa:** ...
**Evidência:** ...
**Ação automática:** ...
**Ação necessária:** ...
```

## Gate de qualidade

Uma mensagem executiva é boa se Lucas consegue responder uma destas sem abrir arquivo:

- aprovar;
- bloquear;
- ajustar;
- entender que está feito;
- entender que está bloqueado;
- saber qual risco existe.

## Relação com Mesa COO

- Uma decisão por mensagem.
- Botões nativos quando runtime suportar; se não suportar, opções textuais limpas.
- Mesa COO não deve despejar backlog nem relatório técnico.
- Decisões A3/A4 precisam escopo inline, rollback e readback.
