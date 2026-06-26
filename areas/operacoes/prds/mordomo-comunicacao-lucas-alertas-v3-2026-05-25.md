# Mordomo — Comunicação com Lucas / Alertas v3

Data: 2026-05-25
Status: proposta operacional para aprovação/implementação
Escopo: Telegram/origin do Mordomo para Lucas; WhatsApp/e-mail/calendário entram como fontes, não como linguagem de saída.

## Problema

Os alertas atuais misturam material interno com comunicação executiva:

- aparecem wrappers de cron/job e linguagem técnica;
- itens de naturezas diferentes entram no mesmo bloco;
- status internos viram texto para Lucas;
- não fica claro se Lucas precisa decidir, aprovar envio, responder pessoalmente, ignorar, ou só saber;
- follow-up vencido e cliente urgente aparecem no mesmo nível;
- a mensagem não termina com uma ação única.

Resultado: Lucas recebe uma lista grande, sem direção, com ruído operacional.

## Princípio de produto

Lucas não deve receber logs. Lucas deve receber decisões.

Toda comunicação do Mordomo precisa responder, em segundos:

1. O que aconteceu?
2. Por que isso importa agora?
3. O que eu recomendo?
4. O que preciso que Lucas faça?
5. Qual botão/resposta resolve?

Se não houver uma resposta clara para essas perguntas, o item não deve interromper Lucas; deve ficar em artefato local, CRM, fila ou digest não urgente.

## Nova hierarquia de comunicação

### Nível 0 — Silencioso

Não manda nada para Lucas.

Exemplos:
- rotina executada sem problema;
- candidato bruto;
- item classificado como ruído;
- follow-up seguro enviado automaticamente;
- artefato local atualizado;
- leitura/análise sem decisão.

Registro permitido: logs, CRM, Brain, arquivo local, Mission Control.

### Nível 1 — Recibo curto

Usar quando algo foi feito e Lucas precisa saber, mas não decidir.

Formato:

```text
Feito: [ação]
Contexto: [cliente/empresa]
Registro: [onde ficou]
```

Exemplo:

```text
Feito: follow-up pós-PDF enviado para Clau Xavier.
Contexto: Zipper / Adriana Duque.
Registro: fila atualizada como auto_sent.
```

### Nível 2 — Digest organizado

Usar para visão consolidada, sem urgência imediata.

Regras:
- no máximo 5 itens;
- separado por empresa;
- cada item tem status e próximo passo;
- sem job id, sem classe interna, sem wrapper.

Formato:

```text
Resumo Mordomo — [período]

Zipper
1. [Cliente] — [estado]
   Próximo: [ação]

LK
1. [tema] — [estado]
   Próximo: [ação]
```

### Nível 3 — Decisão urgente

Usar quando Lucas precisa decidir/responder/aprovar algo agora.

Formato obrigatório:

```text
Cliente urgente — [Empresa]

[Cliente / assunto]
O que aconteceu: ...
Por que importa: ...
Risco/Cuidado: ...
Minha recomendação: ...

Sugestão de resposta:
"..."

Decisão: [uma ação]
```

Botões quando seguro:
- Enviar sugestão
- Rascunhar
- Lembrar amanhã
- Ignorar/Silenciar

### Nível 4 — Aprovação de ação externa

Usar quando há envio WhatsApp/e-mail, cliente, fornecedor, campanha, preço, disponibilidade, reserva, pagamento ou produção.

Formato:

```text
Aprovação necessária — [Empresa]

Destino: [canal + pessoa]
Pedido limpo: [o que será feito]
Evidências: [fontes consultadas]
Preview: [texto exato ou anexo]
Risco: [baixo/médio/alto + por quê]
Bloqueios: [o que não está confirmado]
Rollback: [o que dá para desfazer; se não dá, dizer]

Decisão: aprovar / ajustar / cancelar
```

## Gramática proibida em mensagens para Lucas

Não expor:

- `Cronjob Response`;
- job IDs;
- `To stop/manage this job...`;
- JSON/preflight/router metadata;
- nomes internos de classe como `needs_lucas_decision`, `post_pdf_followup`, `price_or_availability_or_conditions`;
- listas de flags sem tradução;
- stack traces ou erros crus sem resumo e impacto.

Se precisar mencionar automação, usar linguagem humana:

- ruim: `job_id e46ea230f0cf emitted stdout`
- bom: `O digest das 6h encontrou um cliente urgente.`

## Regra de separação por intenção

Nunca misturar no mesmo alerta:

- cliente urgente;
- follow-up rotineiro;
- erro técnico;
- digest informativo;
- decisão de aprovação;
- aprendizado/correção.

Se houver vários tipos no mesmo ciclo, entregar só o nível mais urgente e registrar o resto localmente.

## Filtro antes de interromper Lucas

Antes de mandar Telegram, o Mordomo deve perguntar:

1. É cliente/contato externo real?
2. Existe decisão, aprovação ou resposta pendente de Lucas?
3. É urgente ou material agora?
4. Eu consigo recomendar uma ação concreta?
5. Existe risco de eu enviar/afirmar algo sem confirmação?

Só interrompe se 1 + 2 + 3 forem sim. Se 4 for não, o alerta deve pedir uma decisão específica de triagem, não despejar a fila. Se 5 for sim, bloquear envio e mostrar o cuidado.

## Formatos finais

### A. Cliente urgente

```text
Cliente urgente — Zipper

Thais Laynes / Nina Pandolfo
O que aconteceu: gostou da print e perguntou sobre Pix e opção vermelha; depois cobrou resposta.
Por que importa: lead quente esperando condição comercial.
Cuidado: não posso confirmar Pix, preço, cor ou disponibilidade sem fonte atual.
Minha recomendação: responder agora confirmando que vamos checar as condições.

Sugestão:
"Oi, Thais! Que bom que você gostou da print da Nina. Vou confirmar aqui as condições certinhas de pagamento por Pix e também a disponibilidade das opções em vermelho para te passar com segurança."

Decisão: aprovar envio ou me passar as condições finais.
```

### B. Follow-up automático enviado

```text
Feito: follow-up pós-PDF enviado.
Cliente: [nome]
Contexto: Zipper / [artista]
Status: aguardando cliente.
```

### C. Digest não urgente

```text
Resumo Mordomo — hoje

Zipper
1. [Cliente] — aguardando cliente desde [data].
   Próximo: follow-up automático em [data] se não houver resposta.

LK
1. [tema] — registrado, sem decisão sua agora.
```

### D. Erro técnico

```text
Falha no Mordomo — WhatsApp watcher

Impacto: posso deixar de ver novas mensagens do WhatsApp pessoal.
Causa provável: [curto]
Ação segura feita: [read-only/local]
Preciso de você: nenhuma / aprovar restart / enviar código.
```

## Mudanças de lógica recomendadas

1. Criar um `message_composer` único para alertas do Mordomo.
2. Todo watcher/cron deve enviar objetos estruturados para o composer, não texto pronto.
3. O composer escolhe `silent`, `receipt`, `digest`, `urgent_decision`, `approval_packet` ou `technical_error`.
4. O composer remove linguagem técnica antes de Telegram.
5. Crons no-agent devem continuar silent-OK: stdout vazio quando não houver interrupção real.
6. Artefatos locais podem continuar completos; Telegram deve ser filtrado.
7. Botões devem mapear para ações internas seguras e sempre remover teclado após clique.
8. `Ignorar` deve ser aprendizado durável: limpar fila, silenciar chat/classe quando aplicável e impedir ressurgimento de estado antigo.

## Critério de pronto

- Nenhum alerta do Mordomo para Lucas contém wrapper de cron, job id ou classe interna.
- Todo alerta tem uma decisão ou próximo passo único.
- Follow-up automático seguro não vira pedido de aprovação.
- Follow-up bloqueado vira decisão clara com motivo.
- Rotina sem urgência fica silenciosa ou em digest.
- Botões antigos não podem executar ação depois de Lucas escolher ignorar/silenciar.
- Testes/regressões cobrem pelo menos: cliente urgente, follow-up seguro enviado, rotina silenciosa, digest não urgente, erro técnico, ignorar/silenciar.

## Próxima decisão

Aprovar transformar esta proposta em implementação nos scripts do Mordomo.

Escopo de implementação sugerido:
- scripts de digest/WhatsApp watcher/Decision Inbox;
- composer comum;
- regressões locais;
- uma rodada de dry-run sem envio externo.

Sem aprovação, manter como PRD/local e usar manualmente como padrão de resposta.
