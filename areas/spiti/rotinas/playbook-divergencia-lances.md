# Playbook — SPITI Divergência de Lances

## Objetivo

Padronizar investigação e resposta quando email, site, monitor interno ou banco não concordam sobre lances/lotes.

## Quando usar

- Site mostra um valor, email indica outro ou não confirma.
- Monitor/alerta reporta anomalia.
- Lucas pergunta por que um lote parece divergente.
- Há risco de responder com dado errado.

## Princípio

Não existe "chute operacional" em SPITI. Se a fonte não fecha, declarar incerteza e investigar.

## Passo a passo

1. Identificar lote, pregão e horário da pergunta.
2. Listar fontes consultadas e horário de consulta.
3. Classificar divergência:
   - site vs email;
   - email vs banco;
   - monitor vs fonte manual;
   - meta tag/preço base confundido com lance;
   - atraso de atualização.
4. Responder internamente com matriz de evidências.
5. Se houver comunicação externa, preparar rascunho conservador e pedir aprovação Lucas.
6. Registrar a anomalia em lesson/relatório de leilão.

## Matriz de evidência

```text
Lote: ...
Pergunta: ...
Email: confirmado / não confirmado / divergente
Banco/monitor: confirmado / não confirmado / divergente
Site: destaque / parcial / não confiável para total
Meta tag: ignorada para lance atual
Conclusão segura: ...
Ação recomendada: ...
```

## Frases seguras

- "Não tenho confirmação suficiente para afirmar esse total."
- "O site pode não refletir o conjunto completo de lances; vou validar pela fonte correta."
- "A meta tag não representa lance atual; não vou usá-la como base."
- "Com a evidência atual, a resposta segura é aguardar/validar no email."

## Proibido

- Usar meta tag como lance atual.
- Inferir total por destaque visual do site.
- Confundir Zipper Vendas com SPITI.
- Enviar correção externa sem aprovação Lucas.
