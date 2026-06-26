# Mordomo Zipper/SPITI — Protótipo read-only de busca por artista

Atualizado: 2026-05-18T15:23:17.937409+00:00

## Escopo e segurança

- Consultas read-only em `vendas_tango`, `contacts` e `conversations`.
- Saída PII-minimizada: não salva nomes, e-mails, WhatsApps, telefones nem corpo bruto de mensagens.
- Janela de vendas testada: `2025-05-18` a `2026-05-18`.
- Sinal negativo/desfit é heurístico nesta versão: detecta termos de preço/orçamento em contatos/conversas; deve virar campo estruturado antes de envio automático.

## Resultado dos testes

### Flávia Junqueira

- Compras Zipper últimos 12 meses: 78 linhas de venda; 65 contatos distintos; valor total R$ 3,251,000.00.
- Origens de venda mais comuns: Site/Email/Redes Sociais=33, Galeria=17, Arquiteto=11, Art Advisor=6, Feira=4, sem_origem=4, Artista=1, Whastapp=1.
- Eventos/canais mais comuns: WhatsApp=36, Acervo=32, SP-Arte=4, sem_evento=4, Email=1, Site=1.
- Regiões mais comuns: São Paulo/SP=37, Belo Horizonte/MG=5, Rio de Janeiro/RJ=5, sem_região=5, Campinas/SP=3, Brasília/DF=2, Campo Grande/MS=1,  São Paulo/SP=1.
- Contatos com `artist_interest`: 56 registros; 56 contatos distintos.
- Menções em conversas: 170 mensagens; 26 telefones distintos mascarados.
- Menções a PDF/proposta dentro dessas conversas: 102 mensagens; 17 telefones distintos mascarados.
- Possíveis sinais negativos/desfit: 0 mensagens; 0 telefones distintos mascarados; 0 contatos com sinal em notas/tags/contexto.
- Direção das mensagens negativas: n/d.
- Datas recentes de sinal: 2026-03-12T18:22:00.496+00:00, 2026-03-12T18:21:30.015+00:00, 2026-03-12T18:21:28.711+00:00, 2026-04-03T01:05:11.314668+00:00, 2026-04-03T01:05:10.828174+00:00, 2026-04-03T01:05:10.712473+00:00.

### Laura Villarosa

- Compras Zipper últimos 12 meses: 9 linhas de venda; 7 contatos distintos; valor total R$ 368,800.00.
- Origens de venda mais comuns: Site/Email/Redes Sociais=3, Galeria=2, Feira=2, Art Advisor=1, Arquiteto=1.
- Eventos/canais mais comuns: WhatsApp=3, Acervo=2, Exposição=1, SP-Arte=1, SP-Arte 2026=1, ArtRio=1.
- Regiões mais comuns: São Paulo/SP=5, sem_região=2, Rio de Janeiro/RJ=1, Nova Lima/MG=1.
- Contatos com `artist_interest`: 1 registros; 1 contatos distintos.
- Menções em conversas: 13 mensagens; 5 telefones distintos mascarados.
- Menções a PDF/proposta dentro dessas conversas: 3 mensagens; 2 telefones distintos mascarados.
- Possíveis sinais negativos/desfit: 1 mensagens; 1 telefones distintos mascarados; 0 contatos com sinal em notas/tags/contexto.
- Direção das mensagens negativas: out=1.
- Datas recentes de sinal: 2026-03-12T18:50:32.503+00:00, 2026-03-12T18:50:12.53+00:00, 2026-03-12T18:21:28.687+00:00, 2026-03-05T14:58:37.668798+00:00.

## Consulta lógica v0

1. `buyers_12m`: buscar em `vendas_tango` por `artista_nome ilike artista` e `pedido_data >= hoje-365`.
2. `interest_contacts`: buscar em `contacts.artist_interest` e, futuramente, tags normalizadas por artista.
3. `conversation_interest`: buscar em `conversations.message` por artista e termos como `obras disponíveis`, `PDF`, `catálogo`, `proposta`.
4. `negative_fit`: excluir/revisar quando mensagens/notas tiverem preço caro, orçamento, inviável, fora de budget ou equivalente.
5. `proposal_sent`: hoje é inferido por conversas/mensagens; precisa de `proposal_events` ou preenchimento de `scheduled_sends`/`artist_pdfs` para ficar confiável.

## Regras de decisão v0

- Compra recente do artista: sinal positivo alto, mas ainda revisar disponibilidade/PDF antes de contato.
- Interesse explícito + sem negativo + PDF validado: elegível para preview ou envio comandado por Lucas.
- Interesse explícito + negativo de preço/orçamento: bloquear envio automático e mandar para revisão manual.
- Sem PDF validado ou artista ambíguo: não enviar; pedir/gerar preview interno.

## Próximo passo técnico

Criar uma view/read model que materialize essas quatro listas com IDs internos e hashes operacionais, mantendo PII apenas no Supabase.
