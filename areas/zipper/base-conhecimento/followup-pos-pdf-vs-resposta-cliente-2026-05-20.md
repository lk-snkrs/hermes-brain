# Zipper — diferença entre follow-up pós-PDF e cliente sem resposta

Data: 2026-05-20
Origem: correção de Lucas por screenshot WhatsApp.

## Regra

Antes de qualquer follow-up pós-PDF, o Mordomo precisa ler o histórico real recente do WhatsApp/e-mail.

Se o cliente respondeu depois do PDF, o caso deixa de ser `post_pdf_followup` normal e vira `needs_lucas_decision` / A3 quando houver:

- pergunta sobre pagamento, Pix, condição, preço, disponibilidade, reserva ou desconto;
- escolha de obra/cor/variante, exemplo: “Vermelho vcs tb?”;
- cobrança posterior tipo “Oii”, “oi oi oi”, indicando que Lucas não respondeu.

Nesses casos, **não enviar** mensagem genérica como “conseguiu olhar com calma?”. O correto é avisar Lucas que existe uma resposta comercial não respondida e preservar o contexto da pergunta.

## Caso Thais / Nina Pandolfo

Cliente respondeu depois do PDF:

- “Gostei muito da print da Nina! Como fica o pagamento com pix?”
- “Vermelho vcs tb?”
- depois cobrou com “Oii” e “oi oi oi”.

Classificação correta: cliente esperando resposta de Lucas sobre pagamento/Pix e obra/cor, não follow-up silencioso.

## Correção operacional

O watcher deve:

1. resolver contato numérico para JID quando possível;
2. ler mensagens recentes antes de qualquer follow-up;
3. se existir inbound depois do último outbound/PDF, bloquear follow-up automático;
4. se o inbound contiver pagamento/preço/disponibilidade/condição, elevar para A3 / `needs_lucas_decision`;
5. só permitir follow-up automático se não houver resposta substantiva do cliente desde o PDF.
