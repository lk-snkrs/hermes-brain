# Direcionamento — Bot de atendimento LK no Chatwoot Cloud — 2026-06-09-091655 -03

## Origem

Lucas explicou por voz que está configurando o Chatwoot Cloud por conta própria. O objetivo para Hermes/LK Ops não é configurar o Chatwoot em si agora, mas construir o bot de atendimento.

## Objetivo declarado

Criar um bot de atendimento chamado/associado a Elle/L para toda mensagem que chegar no Chatwoot:

1. Receber/observar toda nova mensagem.
2. Fazer triagem operacional.
3. Atender automaticamente quando for seguro.
4. Responder baseado em inteligência operacional e uma base de conteúdo que será alimentada continuamente.

## Guardrails LK

- Estoque, disponibilidade, pronta entrega, tamanho disponível e divergência SKU/Tiny/Shopify continuam obrigatoriamente com `lk-stock`/Tiny.
- Reclamação sensível, financeiro, cancelamento, troca/devolução complexa, desconto, reserva, prazo ambíguo e negociação escalam para humano.
- Automação pública só deve ser ativada após aprovação explícita, kill switch, logs, modo dry-run validado e escopo de respostas allowlisted.

## Arquitetura sugerida

Fases:

1. Dry-run: ler eventos e gerar classificação sem escrever no Chatwoot.
2. Copiloto interno: criar nota privada com resumo, intenção, risco e resposta sugerida.
3. Triagem operacional: aplicar labels/roteamento, ainda sem resposta pública para casos sensíveis.
4. Autoatendimento seguro: responder publicamente apenas FAQs e casos de baixo risco com base de conhecimento validada.
5. Aprendizado operacional: toda dúvida nova vira item para base de conteúdo/Brain, com aprovação humana antes de virar resposta automática.

## Próximo deliverable recomendado

Especificar o MVP do bot:

- intents iniciais;
- respostas permitidas;
- casos proibidos/escalados;
- formato da base de conteúdo;
- contrato webhook Chatwoot Cloud -> Hermes/Elle;
- política de kill switch e auditoria.
