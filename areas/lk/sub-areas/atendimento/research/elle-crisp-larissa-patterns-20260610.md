# Elle — Aprendizado de padrões Larissa a partir do export Crisp LK

Data: 2026-06-10
Fonte: ZIP local enviado por Lucas (`crisp-export-lk.zip`), analisado read-only.
Escopo: 574 conversas do Crisp Chat / WhatsApp LK, com atendimento humano associado a Larissa/Atendimento.
PII: não expor telefone, e-mail, nomes de clientes, rastreios, pedidos ou conteúdo sensível em outputs públicos. Amostras abaixo foram redigidas/sanitizadas.

## Resumo quantitativo

- Conversas: 574
- Mensagens totais: 11.552
- Período UTC do export: 2026-05-14T18:52:43.869Z até 2026-06-10T23:57:53.549Z
- Mensagens por lado:
  - Cliente/user: 5.941
  - Operador: 5.611
- Tipos de mensagem:
  - Texto: 9.878
  - Arquivo: 794
  - Evento: 636
  - Nota: 182
  - Áudio: 59
- Origem dominante:
  - WhatsApp via Crisp: 6.007
  - Chat: 5.089
  - Auto-responder: 444
- Mensagens por conversa:
  - Mediana: 14
  - P90: 42
  - Máximo: 179
- Tempo até resposta humana do operador após mensagem do cliente:
  - Amostras calculadas: 2.745
  - Mediana: 4,9 min
  - P75: 30,2 min
  - P90: 85,1 min

## Temas recorrentes nas conversas

Contagem por conversa, por presença de sinais/keywords no diálogo:

- Atendimento humano / falar com atendente: 538
- Loja / endereço / horário: 461
- Produto / modelo / autenticidade / marcas: 430
- Estoque / disponibilidade / tamanho: 399
- Pedido / status / rastreamento: 398
- Entrega / frete / prazo: 296
- Preço / desconto / pagamento: 136
- Troca / devolução / pós-venda: 103

Leitura operacional: a Elle precisa tratar a maioria das entradas como triagem comercial/operacional, não como FAQ genérico. Os fluxos críticos são estoque+tamanho, pedido/status, prazo/encomenda, loja/retirada e troca/devolução.

## Padrão de voz da Larissa

Padrão dominante:

- Saudação curta e humana:
  - “Bom dia! Larissa da LK.”
  - “Boa tarde! Larissa da LK.”
  - “Bom dia! Larissa da LK. Como posso ajudar?”
  - “Oie! Tudo bem? Larissa da LK.”
- Mensagem direta, com pouca explicação desnecessária.
- Quando precisa de dado, pergunta uma coisa por vez:
  - “Qual o número do pedido?”
  - “Qual tamanho?”
- Quando precisa consultar fonte, usa hold/ack curto:
  - “Conferindo disponibilidade em loja e te retorno. Ok?”
  - “Conferindo pra você.”
  - “Só mais um momento, por favor.”
- Para encomenda/reposição, frase padrão forte:
  - “Conferi seu pedido e o modelo escolhido é sob encomenda, com previsão de chegada entre 4 e 6 semanas.”
  - “Reposição chega em 4 a 6 semanas.”
- Para disponibilidade em loja/site:
  - “Tem que reservar o tamanho no site.”
  - “Tem que reservar no site.”
  - “Esgotado em loja. Reposição chega em 4 a 6 semanas.”
- Para rastreio/status:
  - envia código/link quando tem evidência;
  - não inventa status, primeiro pede número do pedido ou diz que vai conferir.
- Para cancelamento/estorno:
  - linguagem formal e de processo, com prazo operacional; exige fonte/aprovação humana antes de prometer.

## Implicações para a Elle

### 1. Elle não deve responder como “bot”

Tom-alvo: atendente breve e humano, estilo Larissa.

Modelo de abertura segura:

```text
Bom dia! Elle da LK.
Como posso ajudar?
```

Ou, se for continuidade:

```text
Oie! Tudo bem? Elle da LK.
Vou conferir pra você.
```

Evitar:

- textos longos;
- linguagem institucional demais;
- múltiplas perguntas no mesmo turno;
- prometer disponibilidade, reserva, preço, prazo ou solução sem fonte viva.

### 2. Macro de triagem por intenção

- Pedido/status:
  - pedir número do pedido quando ausente;
  - consultar Shopify/Brain antes de sugerir status;
  - se prazo/atraso/cancelamento/estorno, elevar para humano.
- Estoque/tamanho/disponibilidade:
  - identificar modelo + tamanho;
  - encaminhar para lk-stock/Tiny antes de disponibilidade final;
  - resposta pública só depois da fonte viva.
- Encomenda/reposição:
  - sempre sensível;
  - não prometer prazo de 4–6 semanas automaticamente; isso apareceu como padrão histórico, mas precisa de política vigente/fonte.
- Loja/endereço/horário:
  - pode ser baixa complexidade se informação canônica estiver versionada;
  - manter mensagem curta.
- Troca/devolução/reclamação/financeiro:
  - alto risco;
  - nota interna + handoff humano.

### 3. Classificador Elle atual precisa aprender contexto de conversa

Rodando o classificador MVP 1C atual nos textos do cliente:

- Primeira mensagem por conversa:
  - 574 classificadas
  - saudação: 541
  - produto: 198
  - pedido: 103
  - estoque: 35
  - prazo: 25
  - alto risco/handoff: 32
- Todas as mensagens de cliente:
  - 5.416 classificadas
  - ambíguo: 2.628
  - saudação: 1.208
  - pedido: 811
  - produto: 699
  - estoque: 653
  - prazo: 394
  - financeiro: 127
  - devolução: 96
  - encomenda: 82
  - troca: 77
  - reclamação: 16

Interpretação: muita mensagem isolada é curta (“sim”, “pode”, “38”, “obrigado”, etc.), então a Elle precisa classificar por **janela de conversa** e não apenas pela última mensagem isolada.

Recomendação técnica:

- Para cada evento incoming, montar contexto com:
  - última mensagem do cliente;
  - 3–8 mensagens anteriores;
  - último assunto classificado;
  - entidades extraídas: pedido, tamanho, modelo, canal, status, links.
- Se a última mensagem for curta/ambígua, herdar intenção do turno anterior.
- Só sugerir resposta pública se:
  - intenção baixa;
  - fonte necessária presente;
  - guardrail não bloqueia;
  - nenhuma palavra sensível.

### 4. Macros seguras iniciais para Elle/copilot

Estas macros são para **rascunho/nota interna ou sugestão**, não envio automático sem aprovação do modo público.

Saudação:

```text
Bom dia! Elle da LK.
Como posso ajudar?
```

Pedido sem número:

```text
Qual o número do pedido?
```

Consulta de disponibilidade:

```text
Conferindo disponibilidade em loja e te retorno. Ok?
```

Pedido/status em consulta:

```text
Conferindo o status do seu pedido e te retorno. Pode ser?
```

Aguardar fonte:

```text
Só mais um momento, por favor.
```

Tamanho ausente:

```text
Qual tamanho?
```

### 5. Guardrails que o export confirma

- Estoque/pronta entrega/tamanho é recorrente e precisa continuar roteado para lk-stock/Tiny.
- Encomenda e reposição aparecem muito; não automatizar prazo histórico como verdade viva.
- Pedido/status/rastreio é recorrente; consultar Shopify/transportadora antes de resposta final.
- Cancelamento, estorno, troca/devolução e reclamação exigem humano.
- A Elle MVP deve começar como copiloto: classificar, rotular, criar nota privada e sugerir macro; resposta pública só em fase posterior e com aprovação escopada.

## Próximos passos recomendados

1. Criar dataset sanitizado de treinamento/avaliação com janelas de conversa, não só mensagens soltas.
2. Atualizar `elle_intents.yaml` com intents/labels mais finos:
   - `loja_horario_endereco`
   - `tamanho_disponibilidade`
   - `pedido_sem_numero`
   - `encomenda_reposicao`
   - `rastreio_codigo`
   - `curta_continuacao`
3. Atualizar classificador para herdar intenção em mensagens curtas.
4. Adicionar biblioteca de macros Larissa-style como sugestões internas.
5. Rodar dry-run em amostra de conversas Crisp e medir:
   - acerto de intenção;
   - taxa de handoff correto;
   - falsos positivos de resposta pública;
   - frases sugeridas versus padrão Larissa.

## Arquivos locais de análise

- Resumo JSON sanitizado: `/opt/data/profiles/lk-ops/reports/crisp-elle-learning/crisp_export_lk_analysis_summary.json`
- ZIP original: `/opt/data/profiles/lk-ops/cache/documents/doc_e5941cc8b172_crisp-export-lk.zip`

