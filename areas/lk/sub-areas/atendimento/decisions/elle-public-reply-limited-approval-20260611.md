# Decisão — Elle: resposta pública limitada aprovada

Data: 2026-06-11
Origem: Lucas no Telegram.
Status: aprovação operacional conceitual para configurar/rodar fluxo com resposta pública limitada, sujeito a implantação técnica segura, kill switch, rollback e guardrails.

## Categorias aprovadas para resposta pública da Elle

Lucas confirmou `sim` para as 5 categorias propostas:

1. Saudação / abertura simples.
2. Pedido já enviado/em trânsito com rastreio verificado.
3. Dúvida simples de produto quando houver produto/link/contexto claro.
4. Print/link de concorrente conhecido ou com texto/logo suficiente, usando linguagem cautelosa sobre réplicas/similares.
5. Perguntas institucionais simples.

## Respostas institucionais aprovadas / estilo

Perguntas que a Elle pode responder:

- “vocês vendem original?”
- “a loja é confiável?”
- “tem site?”
- “qual o Instagram?”

Respostas-base:

```text
Sim, trabalhamos apenas com produtos originais. Todos os produtos da LK têm garantia de originalidade.
```

```text
Sim. A LK é uma sneaker boutique com loja física no Jardins, em São Paulo, além do nosso site oficial. Trabalhamos com curadoria de sneakers originais e suporte no pós-venda.
```

```text
Temos sim. Nosso site é: https://lksneakers.com.br/
```

```text
Nosso Instagram é @lk.sneakers.
```

## Cupom primeira compra

Lucas autorizou usar o cupom:

- Código: `ELLE5`
- Benefício: 5% de desconto
- Contexto: pergunta sobre cupom de primeira compra / cupom da Elle.

## Bloqueios mantidos

Mesmo com resposta pública limitada, continuam bloqueados para resposta final automática:

- estoque;
- pronta entrega;
- “tem na loja?”;
- tamanho disponível;
- reserva;
- desconto/negociação fora do cupom `ELLE5`;
- prazo prometido;
- pedido não enviado;
- pedido atrasado/problemático;
- troca/devolução;
- reclamação sensível;
- extravio/cancelamento/reembolso;
- foto solta de produto sem texto/link/logo suficiente;
- qualquer ambiguidade relevante.

## Requisito técnico antes de produção

Antes de ativar no inbox real, preparar:

- kill switch;
- rollback;
- fallback/handoff para humano;
- logs sanitizados;
- filtros para não responder outgoing/private notes;
- categorias e thresholds configuráveis;
- verificação de assinatura Chatwoot;
- readback/receipt após alteração.
