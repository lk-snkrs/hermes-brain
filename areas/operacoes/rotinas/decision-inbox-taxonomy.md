# Decision Inbox Taxonomy — COO Queue

Atualizado em: 2026-05-22 13:37 UTC

## Objetivo

Reduzir falso positivo no Decision Inbox/Mordomo e transformar mensagens em uma fila executiva curta, segura e acionável para Lucas.

## Regra de ouro

Nem toda mensagem com palavras como prazo, pix, pagamento, live, macro, dúvida ou interesse precisa virar decisão Lucas.

A classificação deve responder:

1. Há uma ação segura a tomar?
2. A ação exige fonte externa ou aprovação?
3. O item pertence a LK, Zipper, SPITI, pessoal ou infra?
4. É cliente real, fornecedor, newsletter, banco, grupo interno ou ruído?
5. Pode ser suprimido sem risco?

## Categorias canônicas

### `commercial_reply`

Use quando há resposta comercial de cliente/lead que pede continuidade, mas não necessariamente preço/disponibilidade.

Exemplos:

- “Gostei da obra, como seguimos?”
- “Tenho interesse nesse modelo.”
- “Pode me mandar opções?”

Ação:

- preparar preview de resposta;
- checar fonte se envolver item/obra/produto específico;
- enviar automaticamente apenas se o subfluxo já estiver aprovado e não envolver bloqueios materiais.

### `followup_due`

Use quando existe pendência clara de follow-up, retorno prometido, pós-PDF, pós-orçamento, entrega, retirada ou confirmação.

Ação:

- preparar follow-up elegante;
- pode ser automático somente dentro da exceção aprovada para follow-up simples/verificado;
- bloquear se incluir preço, disponibilidade, reserva, negociação ou reclamação.

### `newsletter_noise`

Use para newsletter, live gravada, conteúdo macro, banco, research, marketing genérico e comunicações informativas sem pedido direto.

Exemplos:

- “Live Itaú Private | Cenário Macro Maio.”
- Newsletter de mercado.
- Convite institucional sem ação clara.

Ação:

- suprimir por padrão;
- promover para briefing apenas se houver relação direta com decisão ativa de Lucas.

### `price_availability_blocked`

Use quando a mensagem pede ou implica preço, disponibilidade, prazo material, reserva, condição de pagamento, desconto, negociação ou promessa comercial.

Exemplos:

- “Qual o valor?”
- “Tem vermelho?”
- “Como fica o pagamento via Pix?”
- “Preciso de um prazo para o cliente.”

Ação:

- bloquear automação externa;
- buscar fonte de verdade;
- pedir/usar aprovação Lucas quando necessário;
- nunca prometer sem fonte.

### `customer_complaint`

Use para reclamação, frustração, atraso percebido, cobrança dura, ameaça de cancelamento, problema com pedido/obra/entrega.

Ação:

- escalar para Lucas/humano;
- preparar resumo e opções;
- não responder automaticamente salvo texto explicitamente aprovado para o caso.

### `supplier_or_internal`

Use para fornecedores, parceiros, equipe interna, operações, compra, logística ou grupos de trabalho.

Ação:

- separar de cliente final;
- checar empresa correta;
- não enviar compromisso de compra, pagamento, prazo ou negociação sem aprovação.

### `calendar_or_logistics`

Use para data/hora/local claros de reunião, entrega, retirada, coleta, visita, evento ou lembrete.

Ação:

- se claro e dentro da autonomia vigente, criar evento/lembrete e notificar Lucas;
- se faltar data/hora/local, preparar pergunta/preview.

### `finance_or_bank`

Use para banco, cobrança, extrato, relatório financeiro, investimentos, pagamentos e reconciliação.

Ação:

- read-only/triagem;
- não movimentar dinheiro;
- não responder como autorização financeira.

### `ignore`

Use quando não há ação, risco, fonte nova ou decisão.

Ação:

- suprimir.

## Critério para entrar na COO Queue

Só entra se tiver pelo menos um:

- decisão Lucas necessária;
- ação segura recomendada;
- risco de perda/oportunidade;
- follow-up vencido/próximo;
- bloqueio material;
- divergência de fonte.

## Formato recomendado da fila

- Contexto: LK/Zipper/SPITI/pessoal/infra.
- Categoria: uma das categorias canônicas.
- Decisão: sim/não.
- Recomendação: uma frase.
- Fonte: conversa/documento/sistema.
- Ação bloqueada: se houver.
- Próxima ação segura: preview, verificar fonte, suprimir, escalar.

## Exemplos de correção

- Itaú Private “Live Cenário Macro Maio” não deve ser `price_or_availability_or_conditions`; deve ser `newsletter_noise` ou `finance_or_bank` se houver ação financeira real.
- “Eu só preciso de um prazo, cliente aguardando” deve ser `price_availability_blocked` ou `customer_complaint` conforme tom/contexto, nunca follow-up automático.
- “Qualquer dúvida me chama” normalmente é `ignore` ou `followup_due` apenas se houver tarefa previamente combinada.
