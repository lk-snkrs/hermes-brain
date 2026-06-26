# Mordomo Zipper — Fluxo proposta/PDF inspirado no `!enviar`

Atualizado: 2026-05-18T15:23:17.937460+00:00

## Padrão atual informado por Lucas

Entrada operacional: Lucas envia ao bot um bloco iniciado por `!enviar` contendo histórico do Flow/ZPR Chatbot. Exemplo de campos extraídos:

- Artista de interesse: aparece no nome do fluxo, por exemplo `ZPR Chatbot | Flávia Junqueira`.
- Nome do cliente: respostas a “Qual seu primeiro nome?” e “Qual seu sobrenome?”. O sobrenome deve ser extraído literalmente da resposta ao campo de sobrenome — no teste de 2026-05-18, `Maga` é sobrenome, não dado a ocultar no raciocínio do parser.
- E-mail: resposta a “Qual seu email?”.
- WhatsApp: resposta a “Qual seu WhatsApp?”.
- Confirmação de interesse: resposta positiva do cliente, por exemplo “Sim, por favor!”.

Saída atual pelo WhatsApp:

1. `Olá {{nome}}, tudo bem? Obrigado pelo seu contato! Quem escreve é Lucas Cimino, sócio-diretor da Zipper Galeria, muito prazer!`
2. `Recebi seu interesse pelas obras da artista {{artista}} e gostaria de compartilhar o PDF abaixo com as obras que temos atualmente disponíveis.`
3. PDF com obras disponíveis.

## Entendimento para o novo Mordomo

O novo fluxo deve preservar a praticidade do `!enviar`, mas com roteamento, validação e registro:

1. Parsear o bloco recebido no Telegram.
2. Extrair `nome`, `sobrenome`, `email`, `whatsapp`, `artista`, `origem_flow`, `timestamp_aproximado` e `mensagem_de_interesse`.
3. Normalizar artista contra `artists`/aliases e contra PDFs disponíveis.
4. Conferir sinais negativos/desfit antes de enviar.
5. Localizar PDF validado em `artist_pdfs` ou diretório/conector autorizado.
6. Gerar preview interno com as mensagens e o arquivo encontrado.
7. Só enviar automaticamente se houver comando explícito de Lucas no turno atual e o caso estiver dentro das regras seguras; caso contrário, salvar/mostrar preview.
8. Registrar evento de proposta/envio e agendar follow-up.

## Campos extraídos do exemplo recebido

- `artist`: Flávia Junqueira
- `first_name`: extraído do bloco original, mas não salvo em Brain por minimização de PII.
- `last_name`: extraído do bloco original, mas não salvo em Brain por minimização de PII.
- `email`: presente no bloco original, mas deve ser tratado como PII e não repetido em relatórios.
- `whatsapp`: presente no bloco original, mas deve ser tratado como PII e não repetido em relatórios.
- `lead_source_raw`: Flow/ZPR Chatbot
- `lead_source_normalized`: Site - Tidio
- `intent`: quer receber mais informações/obras disponíveis da artista.

Observação de integração: Lucas confirmou que grande parte dos leads vem da plataforma **Tidio**. A integração futura deve preferir acessar Tidio diretamente por OpenAPI/Webhooks, em vez de depender apenas de Lucas colar o bloco `!enviar`. Docs Tidio confirmadas em 2026-05-18: OpenAPI tem `Contacts` e `Conversations/Get contact messages`; Webhooks ficam em `Settings > Developer > Webhooks` e exigem plano Plus/Premium.

## Template v1 Zipper

Mensagem 1:

`Olá {{primeiro_nome}}, tudo bem? Obrigado pelo seu contato! Quem escreve é Lucas Cimino, sócio-diretor da Zipper Galeria, muito prazer!`

Mensagem 2:

`Recebi seu interesse pelas obras da artista {{artista}} e gostaria de compartilhar o PDF abaixo com as obras que temos atualmente disponíveis.`

Anexo:

`{{pdf_validado_da_artista}}`

## Guardrails

- Não enviar WhatsApp/e-mail sem aprovação explícita de Lucas no turno atual com destinatário e payload.
- Não prometer disponibilidade, preço ou reserva se o PDF não estiver validado como atual.
- Se houver sinal negativo de preço/orçamento/desfit, não enviar automaticamente; classificar como revisão manual.
- Se o artista estiver ambíguo ou sem PDF, pedir confirmação/preview interno.
- Registrar PII somente no Supabase/fonte autorizada; Brain e Telegram devem usar resumo minimizado.

## Continuidade pós-envio

Após cliente responder com agradecimento/recebimento do PDF, manter tom humano, curto e aberto — sem pressão comercial.

Correção de Lucas: **não dizer “valores”**, porque os valores já estão no PDF. O termo correto é **condições de pagamento**.

Este subcaso foi aprovado por Lucas como fluxo automático fechado: se a resposta do cliente for apenas agradecimento/recebimento cordial do PDF, pode responder sem novo preview, usando a cópia abaixo, e registrar follow-up para 2 dias depois.

Template automático:

`Boa tarde, {{primeiro_nome}}! Eu que agradeço o retorno.`

`Fique à vontade para olhar o PDF com calma. Se alguma obra chamar sua atenção, me avise que te passo as condições de pagamento.`

Follow-up automático em 2 dias se não houver nova resposta relevante:

`Oi, {{primeiro_nome}}, tudo bem? Conseguiu olhar o PDF da {{artista}} com calma? Se alguma obra tiver chamado sua atenção, fico à disposição para te passar as condições de pagamento.`

Aprendizado documentado também na skill `multiempresa-routing-lucas`, referência `zipper-mordomo-enviar-pdf-followup-20260518.md`.

## Estrutura mínima de evento futuro

- `company`: Zipper
- `source`: `telegram_command` ou `zpr_chatbot_block`
- `artist_id` / `artist_name`
- `contact_id` ou hash operacional
- `proposal_pdf_id`
- `status`: `previewed`, `approved_to_send`, `sent`, `blocked_negative_fit`, `needs_manual_review`
- `followup_at`
- `created_by`: Lucas/Hermes
- `approval_context`: referência do turno/aprovação

## Critério para implementação

Antes de qualquer envio real, preencher ou conectar fonte confiável de PDFs (`artist_pdfs`/Dropbox/site), criar registro estruturado de propostas e testar parser em modo dry-run com blocos reais anonimizados.
