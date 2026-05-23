# PRD — Mordomo Zipper: automação de Enquiry Form ZPR para envio de PDF de artista

**Data:** 2026-05-22  
**Empresa:** Zipper Galeria  
**Conta monitorada:** `lucas@zippergaleria.com.br`  
**Produto:** Mordomo Hermes / Zipper OS  
**Status:** PRD para aprovação e implementação  

---

## 1. Objetivo

Criar uma automação do Mordomo para monitorar o e-mail `lucas@zippergaleria.com.br`, identificar novos e-mails do formulário do site/ZPR com assunto/remetente relacionado a:

`Zipper Galeria | Galeria de Arte Contemporânea localizada em São Paulo | Enquiry form`

A partir de cada e-mail, o Mordomo deve:

1. Extrair dados do lead:
   - nome
   - e-mail
   - telefone
   - artista de interesse
   - obra específica de interesse, quando houver
   - data/hora do formulário
   - mensagem livre, quando houver
2. Localizar o PDF comercial validado de obras disponíveis do artista.
3. Executar o mesmo fluxo padrão do comando **“enviar”**:
   - enviar mensagem padrão por WhatsApp, quando houver telefone válido;
   - enviar PDF por WhatsApp;
   - enviar e-mail com o PDF em anexo;
   - registrar o lead e os recibos;
   - criar follow-up pós-PDF na fila do Mordomo.

A automação deve funcionar como um intake comercial da Zipper, sem depender de Lucas copiar e colar manualmente o bloco do lead no Telegram.

---

## 2. Exemplo de entrada

E-mail recebido:

```text
Enquiry form
Date Maio 22, 2026 15:10
Name Gabrielle
Email gabifmatos@gmail.com
Telephone 21993081866
Message
Item

Flávia Junqueira
Theatro Municipal do Rio de Janeiro 1909, #2, 2025
Pigmento mineral sobre papel de algodão
150 x 174 cm
Subscribe to mailing list Yes
```

Resultado esperado da extração:

```json
{
  "source": "ZPR Enquiry form",
  "received_at": "2026-05-22T15:10:00-03:00",
  "name": "Gabrielle",
  "email": "gabifmatos@gmail.com",
  "telephone_original": "21993081866",
  "artist": "Flávia Junqueira",
  "artwork_title": "Theatro Municipal do Rio de Janeiro 1909, #2",
  "artwork_year": "2025",
  "medium": "Pigmento mineral sobre papel de algodão",
  "dimensions": "150 x 174 cm",
  "message": "",
  "subscribe_to_mailing_list": true
}
```

---

## 3. Contexto operacional atual

Hoje, quando Lucas envia o comando **“enviar”** ou cola um lead de ZPR/Tidio/site, o Mordomo já segue um padrão:

1. identifica nome, telefone, e-mail e artista;
2. encontra o PDF comercial do artista;
3. usa o WhatsApp pessoal de Lucas (`wacli --account pessoal`) para leads Zipper, salvo instrução contrária;
4. envia um texto padrão antes do PDF;
5. envia o PDF sem legenda;
6. envia e-mail pelo `lucas@zippergaleria.com.br` com assinatura da Zipper;
7. registra o follow-up pós-PDF;
8. não fala preço, desconto, reserva ou disponibilidade específica sem fonte validada.

Esta PRD transforma esse fluxo em um watcher automático de e-mail.

---

## 4. Escopo funcional

### 4.1 Monitoramento de e-mail

O sistema deve monitorar a caixa `lucas@zippergaleria.com.br` em intervalo curto, sugerido:

- a cada 2 a 5 minutos; ou
- via webhook/Gmail push notification, se disponível posteriormente.

Filtro inicial:

- assunto contém `Enquiry form`; e
- assunto/remetente/corpo contém indícios de ZPR/Zipper site; e
- destinatário é `lucas@zippergaleria.com.br`; e
- mensagem ainda não foi processada pelo Mordomo.

Critérios de dedupe:

- Gmail message ID/thread ID;
- hash normalizado de `email + telefone + artista + obra + date`;
- estado persistido em arquivo/DB do Mordomo.

### 4.2 Parsing do e-mail

O parser deve suportar:

- e-mail HTML com tabela visual;
- texto extraído do HTML;
- campos vazios, como `Message` em branco;
- item com imagem antes do texto;
- artista na primeira linha do bloco `Item`;
- obra e ano na segunda linha;
- técnica na terceira linha;
- dimensões na quarta linha;
- telefone brasileiro com ou sem `+55`, espaços, nono dígito ou formatação.

Campos obrigatórios para agir:

- nome;
- pelo menos um canal de contato: e-mail ou telefone;
- artista.

Campos opcionais:

- obra específica;
- mensagem livre;
- dimensões;
- técnica;
- opt-in de mailing.

### 4.3 Normalização de telefone

O sistema deve guardar sempre:

- `telephone_original`: como veio no e-mail;
- `telephone_e164_candidate`: com prefixo `55` quando aplicável;
- `whatsapp_number_used`: número efetivamente usado pelo wacli, se houver envio.

Regra brasileira já aprendida:

- tentar primeiro a normalização canônica;
- se `wacli` retornar `no LID found` e o número tiver padrão móvel brasileiro com nono dígito, tentar fallback removendo o `9` logo após o DDD;
- registrar as duas tentativas;
- não tratar `Número desconhecido` como erro se o envio resolver para DM válido.

Exemplo:

```text
21993081866 → 5521993081866
Fallback possível: 552193081866, somente se a primeira resolução falhar e o padrão fizer sentido.
```

### 4.4 Identificação do artista

Para e-mails ZPR Enquiry form, o artista deve ser extraído prioritariamente da primeira linha textual do bloco `Item`.

Exemplo:

```text
Flávia Junqueira
Theatro Municipal do Rio de Janeiro 1909, #2, 2025
...
```

Artista = `Flávia Junqueira`.

Fallbacks:

1. campo `Message`, se mencionar artista;
2. assunto do e-mail, se contiver nome de artista;
3. busca no título da obra em base local/Supabase, somente como fallback;
4. se não houver confiança, bloquear envio e pedir decisão.

### 4.5 Localização do PDF

Fonte preferencial:

- Supabase CRM/Main tabela `artist_pdfs`;
- cópias locais em `/opt/data/zipper_artist_pdfs/`;
- manifesto `/opt/data/zipper_artist_pdfs/manifest.json`.

Critérios para PDF válido:

- artista bate com normalização acento/case;
- arquivo é comercial de obras disponíveis/seleção do artista;
- não é recibo, comprovante Pix, nota fiscal, ordem de venda, financeiro ou documento interno;
- nome e/ou texto extraído confirmam relação com o artista.

Se PDF não encontrado ou incerto:

- não enviar nada externamente;
- criar um pacote de decisão para Lucas no Telegram:
  - lead;
  - artista;
  - obra específica;
  - motivo do bloqueio;
  - sugestão: “subir PDF comercial da artista”.

---

## 5. Comportamento de envio

### 5.1 Modo recomendado de rollout

A automação deve ter três modos:

#### Modo 0 — dry-run

- monitora e-mails;
- extrai leads;
- localiza PDF;
- monta preview;
- não cria rascunho externo;
- não envia WhatsApp/e-mail;
- registra auditoria local.

Uso: testes iniciais.

#### Modo 1 — approval-gated

- monitora e-mails;
- extrai lead;
- localiza PDF;
- preflighta canais;
- envia preview no Telegram para Lucas aprovar;
- só executa após Lucas aprovar.

Uso: primeira fase em produção.

#### Modo 2 — auto-send estreito, após aprovação explícita de Lucas

A automação envia automaticamente somente quando todos os critérios forem verdadeiros:

- e-mail é claramente `ZPR Enquiry form`;
- nome extraído com confiança;
- artista extraído com confiança;
- PDF comercial validado existe;
- mensagem livre não contém negociação sensível;
- obra específica não exige resposta de preço/disponibilidade;
- pelo menos um canal de contato válido;
- lead ainda não processado;
- nenhuma regra de bloqueio A3/A4 foi acionada.

Após envio, o sistema reporta no Telegram:

- nome;
- artista;
- canais usados;
- PDF enviado;
- follow-up criado;
- qualquer fallback de telefone usado.

### 5.2 Mensagem padrão WhatsApp

Usar exatamente o padrão já aprovado para leads Zipper, ajustando gênero do artista:

```text
Olá {{nome}}, tudo bem? Obrigado pelo seu contato! Quem escreve é Lucas Cimino, sócio-diretor da Zipper Galeria, muito prazer!

Recebi seu interesse pelas obras da artista {{artista}} e gostaria de compartilhar o PDF abaixo com as obras que temos atualmente disponíveis.
```

Para artista masculino:

```text
Recebi seu interesse pelas obras do artista {{artista}} e gostaria de compartilhar o PDF abaixo com as obras que temos atualmente disponíveis.
```

Depois enviar o PDF sem legenda.

Não incluir:

- preço;
- disponibilidade da obra específica;
- desconto;
- reserva;
- prazo de pagamento;
- promessa de que a obra específica está disponível.

### 5.3 E-mail padrão

O e-mail deve ser enviado a partir de:

`lucas@zippergaleria.com.br`

Assunto sugerido:

```text
{{artista}} | Obras disponíveis
```

Corpo base:

```text
Olá {{nome}}, tudo bem?

Obrigado pelo seu contato e pelo interesse no trabalho da artista {{artista}}.

Compartilho em anexo o PDF com obras atualmente disponíveis. Caso alguma obra chame sua atenção, fico à disposição para conversar e te passar mais informações.

Atenciosamente,
Lucas Cimino
Zipper Galeria
```

A assinatura HTML da Zipper deve ser aplicada quando disponível.

Para artista masculino, ajustar:

```text
no trabalho do artista {{artista}}
```

### 5.4 Tratamento quando o lead perguntou sobre uma obra específica

Mesmo que o formulário tenha sido enviado a partir de uma obra específica, a resposta inicial automática não deve afirmar disponibilidade da obra.

A copy deve permanecer em nível seguro:

- “interesse no trabalho da artista”;
- “PDF com obras atualmente disponíveis”.

Se a mensagem livre perguntar explicitamente:

- “qual o valor?”
- “essa obra está disponível?”
- “consigo desconto?”
- “quero reservar”
- “quero comprar”

Então o envio automático deve ser bloqueado e Lucas deve receber um pacote de decisão, porque há preço/disponibilidade/reserva/negociação.

---

## 6. Regras de risco e aprovação

### A0 — Sem risco

- leitura do e-mail;
- parsing;
- dedupe;
- busca local de PDF;
- criação de log local.

Pode executar automaticamente.

### A1 — Baixo risco

- criar pacote de preview no Telegram;
- criar registro local/Supabase do lead;
- criar rascunho Gmail, se habilitado.

Pode executar automaticamente, desde que sem envio externo.

### A2 — Envio comercial seguro e padronizado

- envio do PDF padrão para lead novo do formulário, sem preço/disponibilidade/negociação, com PDF validado.

Pode virar auto-send somente após Lucas aprovar este subfluxo explicitamente em produção.

### A3 — Exige Lucas

Bloquear auto-send e pedir decisão quando houver:

- pergunta de preço;
- pedido de desconto;
- disponibilidade de obra específica;
- reserva;
- pagamento;
- reclamação;
- mensagem ambígua;
- PDF ausente/incerto;
- artista não identificado;
- telefone/e-mail suspeito;
- lead duplicado com conversa recente ativa.

### A4 — Proibido automático

- responder com preço sem fonte validada;
- prometer disponibilidade/reserva;
- negociar condições;
- apagar ou mover e-mails sem política;
- alterar CRM de venda final sem validação.

---

## 7. Persistência e CRM

Cada lead processado deve ser salvo em estrutura auditável.

### 7.1 Registro mínimo local

Arquivo/DB sugerido:

`/opt/data/profiles/mordomo/state/zipper_zpr_enquiry_leads.jsonl`

Campos:

```json
{
  "id": "zpr_enquiry:<gmail_message_id>",
  "source": "ZPR Enquiry form",
  "gmail_message_id": "...",
  "gmail_thread_id": "...",
  "received_at": "...",
  "processed_at": "...",
  "name": "Gabrielle",
  "email": "gabifmatos@gmail.com",
  "telephone_original": "21993081866",
  "whatsapp_number_used": "5521993081866",
  "artist": "Flávia Junqueira",
  "artwork_title": "Theatro Municipal do Rio de Janeiro 1909, #2",
  "pdf_filename": "Flávia Junqueira — Obras Disponíveis.pdf",
  "status": "sent" ,
  "channels": ["whatsapp", "email"],
  "receipts": {
    "whatsapp_text_id": "...",
    "whatsapp_file_id": "...",
    "gmail_sent_message_id": "..."
  },
  "followup_id": "...",
  "risk_level": "A2",
  "block_reason": null
}
```

### 7.2 Supabase / Zipper CRM

Quando a integração estiver estabilizada, salvar também no Supabase correto de Zipper CRM/Main, sem misturar com LK ou SPITI.

Possíveis entidades:

- `contacts`: atualizar/criar contato;
- `conversations` ou `secretary_log`: registrar origem e ação do Mordomo;
- `followups`: registrar follow-up pós-PDF;
- tabela específica `site_enquiries`, se existir ou for criada.

Nunca salvar como venda. É lead/interesse.

---

## 8. Follow-up pós-PDF

Após envio bem-sucedido, criar follow-up na fila global do Mordomo:

- contexto: `zipper`;
- intenção: `post_pdf_followup`;
- autonomia: `zipper_post_pdf_followup`;
- status inicial: `waiting_client` ou equivalente;
- vencimento: 2 dias úteis ou janela padrão já usada pelo comando “enviar”;
- artista;
- nome;
- telefone/e-mail;
- origem: `ZPR Enquiry form`;
- recibos de WhatsApp/e-mail;
- PDF enviado.

Regra crítica:

Antes de qualquer follow-up automático, ler o histórico recente. Se o cliente já respondeu com preço/disponibilidade/pagamento/reserva/negociação ou se Lucas já encerrou a conversa, não enviar follow-up genérico.

Se Lucas encerrou por obra vendida/indisponível e o cliente apenas agradeceu/aceitou, marcar como resolvido sem follow-up.

---

## 9. Interface com Lucas

### 9.1 Preview no Telegram, Modo 1

Mensagem exemplo:

```text
Novo lead ZPR — Flávia Junqueira

Nome: Gabrielle
E-mail: gabifmatos@gmail.com
WhatsApp: 21993081866
Obra de origem: Theatro Municipal do Rio de Janeiro 1909, #2, 2025
PDF encontrado: Flávia Junqueira — Obras Disponíveis.pdf
Risco: A2, envio padrão sem preço/disponibilidade

Ação sugerida:
- WhatsApp pelo pessoal: texto padrão + PDF
- E-mail por lucas@zippergaleria.com.br: PDF em anexo
- Follow-up em 2 dias

Responder: enviar
```

### 9.2 Recibo pós-envio, Modo 2

```text
✅ Lead ZPR processado — Zipper

Gabrielle, Flávia Junqueira
Canais: WhatsApp + e-mail
PDF: Flávia Junqueira — Obras Disponíveis.pdf
Follow-up: criado para DD/MM, se não houver resposta

Nenhuma informação de preço ou disponibilidade específica foi enviada.
```

### 9.3 Bloqueio

```text
⚠️ Lead ZPR bloqueado — precisa Lucas

Nome: Gabrielle
Artista: Flávia Junqueira
Motivo: perguntou valor/disponibilidade da obra específica
Obra: Theatro Municipal do Rio de Janeiro 1909, #2, 2025

Não enviei nada. Posso preparar um rascunho neutro ou você prefere confirmar disponibilidade/preço primeiro?
```

---

## 10. Casos de borda

### 10.1 Lead sem telefone

- enviar apenas e-mail, se PDF validado e sem bloqueios;
- criar follow-up por e-mail;
- registrar que WhatsApp estava ausente.

### 10.2 Lead sem e-mail

- enviar apenas WhatsApp, se telefone válido;
- registrar follow-up WhatsApp.

### 10.3 Lead com artista sem PDF

- bloquear envio;
- avisar Lucas;
- sugerir subir/validar PDF comercial.

### 10.4 Lead duplicado

Se o mesmo lead/artista já foi processado recentemente:

- não reenviar PDF automaticamente;
- verificar conversa recente;
- se já houve envio, apenas atualizar follow-up ou alertar Lucas com contexto.

### 10.5 Obra específica vendida

O formulário sozinho não deve ser usado para afirmar disponibilidade. Se houver base de disponibilidade confiável no futuro, ela pode enriquecer o pacote, mas não deve liberar preço/reserva automaticamente.

### 10.6 Mailing list

Se `Subscribe to mailing list = Yes`, registrar o opt-in como sinal, mas não cadastrar em ferramenta de mailing sem política específica de consentimento e integração aprovada.

---

## 11. Requisitos não funcionais

- **Idempotência:** o mesmo e-mail nunca pode gerar dois envios.
- **Auditoria:** todo parse, bloqueio, envio e follow-up deve ter log.
- **Segurança:** nunca imprimir tokens ou credenciais.
- **Separação de contexto:** Zipper apenas, sem misturar LK/SPITI.
- **Silêncio:** sem Telegram quando não há novo lead, erro ou ação.
- **Observabilidade:** erros de e-mail, PDF, WhatsApp ou Gmail devem aparecer como alerta técnico resumido.
- **Rollback:** flag global para pausar auto-send imediatamente.

---

## 12. Flags de configuração

Sugeridas:

```yaml
zipper_zpr_enquiry_watcher:
  enabled: true
  mode: approval_gated # dry_run | approval_gated | auto_send
  gmail_account: lucas@zippergaleria.com.br
  poll_interval_minutes: 3
  subject_contains: "Enquiry form"
  allowed_sender_patterns:
    - "zippergaleria"
    - "zpr"
  whatsapp_account: pessoal
  email_from: lucas@zippergaleria.com.br
  create_followup: true
  followup_delay_days: 2
  auto_send_requires_valid_pdf: true
  block_on_material_question: true
  telegram_receipts: true
  kill_switch_file: /opt/data/profiles/mordomo/state/zipper_zpr_enquiry_watcher.paused
```

---

## 13. Métricas de sucesso

- % de e-mails ZPR corretamente detectados.
- % de leads parseados sem intervenção.
- % de PDFs encontrados automaticamente.
- tempo médio entre chegada do e-mail e envio/preview.
- número de duplicidades evitadas.
- número de bloqueios corretos por risco A3/A4.
- número de follow-ups criados e resolvidos.
- taxa de resposta dos leads pós-PDF.

---

## 14. Critérios de aceite

### MVP aprovado quando:

- detectar e-mails `Enquiry form` em `lucas@zippergaleria.com.br`;
- extrair corretamente nome, e-mail, telefone, artista e obra do exemplo Gabrielle/Flávia Junqueira;
- localizar PDF validado do artista ou bloquear com motivo claro;
- gerar preview Telegram com payload correto;
- em modo approval-gated, executar o envio padrão após Lucas responder “enviar”;
- registrar recibos de WhatsApp/e-mail;
- criar follow-up pós-PDF;
- impedir duplicidade;
- não enviar preço/disponibilidade/reserva.

### Auto-send aprovado somente quando:

- MVP rodar sem erro por período de teste;
- Lucas aprovar explicitamente `mode: auto_send`;
- kill switch estiver operacional;
- logs e recibos estiverem confiáveis;
- regressões de follow-up estiverem cobertas por testes.

---

## 15. Plano de implementação sugerido

### Fase 1 — Parser e dry-run

- Criar parser de e-mail HTML/texto.
- Testar com o exemplo Gabrielle/Flávia Junqueira.
- Criar registro JSONL local.
- Não enviar nada.

### Fase 2 — Busca de PDF e preview

- Integrar manifest/local `artist_pdfs`.
- Validar tipo de PDF.
- Gerar pacote de preview no Telegram.

### Fase 3 — Execução approval-gated

- Integrar botão/comando “enviar” no preview.
- Preflight WhatsApp + e-mail + PDF antes de qualquer envio.
- Enviar WhatsApp texto + PDF com delay.
- Enviar e-mail com anexo e assinatura.
- Registrar recibos.

### Fase 4 — Follow-up

- Criar/update fila global do Mordomo.
- Confirmar que itens enviados não aparecem como pendências indevidas.
- Aplicar regras de resposta recente e encerramento por obra indisponível.

### Fase 5 — Auto-send estreito

- Ativar somente após aprovação explícita de Lucas.
- Começar com artistas/PDFs validados.
- Gerar recibo Telegram depois do envio.
- Manter bloqueios A3/A4.

---

## 16. Decisão pendente de Lucas

Para implementação, Lucas precisa decidir:

1. Começar em `dry_run` ou `approval_gated`?
2. Auto-send deve ser objetivo futuro ou já desejado após testes?
3. O envio deve ser sempre WhatsApp + e-mail quando ambos existem, ou priorizar WhatsApp e usar e-mail como complemento?
4. Follow-up padrão deve ser 2 dias corridos, 2 dias úteis ou regra já existente do Mordomo?

Recomendação do Mordomo: iniciar em **approval-gated**, com previews no Telegram. Depois de 1–2 dias sem falsos positivos, promover para **auto-send estreito** para leads limpos com PDF validado.
