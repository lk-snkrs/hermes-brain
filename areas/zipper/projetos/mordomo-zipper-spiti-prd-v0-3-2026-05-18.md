# PRD — Mordomo Hermes Zipper/SPITI v0.3

Data: 2026-05-18  
Owner: Lucas Cimino  
Produto: Mordomo Hermes / Zipper OS / SPITI OS  
Status: design aprovado conceitualmente por Lucas; implementação ainda não autorizada para writes/envios externos

## 1. Decisão central

Lucas aprovou o caminho recomendado:

1. Fazer primeiro um mapa completo, rápido e read-only do Supabase Zipper/SPITI.
2. Em seguida entregar busca inteligente por artista/cliente, com segmentação por compra, interesse, proposta enviada, conversa e sinais negativos.
3. Depois implementar o fluxo de proposta/PDF com registro, follow-up e resposta automática dentro de regras seguras.

O Mordomo deve evoluir o schema atual, não criar um CRM paralelo. A prioridade de produto é **Zipper e SPITI primeiro; LK depois**.

## 2. Modelo mental

Lucas fala com o Mordomo em um único contato/interface. O Mordomo roteia internamente para:

- Zipper OS: galeria, artistas, obras, colecionadores, propostas, feiras, logística, vendas reais.
- SPITI OS: leilões, lotes, bidders, contatos e fonte oficial de cada informação.
- LK OS: e-commerce, pedidos, vendas, estoque e clientes, em prioridade posterior.
- Lucas pessoal: compromissos, lembretes e pendências pessoais.

A experiência para Lucas é uma só; a persistência e governança ficam separadas por contexto.

## 3. Fontes de verdade e bases existentes

### Zipper Vendas

Projeto Supabase: `pcstqxpdzibheuopjkas`  
Tabela: `vendas_tango`  
Uso: vendas reais da Zipper Galeria.

Auditoria read-only em 2026-05-18 confirmou 2102 registros e colunas úteis:

- `cliente_nome`
- `email`
- `whatsapp`
- `artista_nome`
- `valor_obra_final`
- `pedido_data`
- `pedido_origem`
- `pedido_evento`
- `acervo_id`
- `deal_name`

Consultas de validação sem PII:

- Flávia Junqueira nos últimos 12 meses: 78 registros de venda.
- Laura Villarosa nos últimos 12 meses: 9 registros de venda.

### Zipper CRM/Main + SPITI

Projeto Supabase: `rmdugdkantdydivgnimb`

Tabelas confirmadas:

- `contacts`: 1960
- `conversations`: 76056
- `secretary_log`: 78
- `followups`: 19
- `artists`: 36
- `exhibitions`: 20
- `contents`, `content_metrics`, `content_tags`, `exhibition_artists`
- SPITI: `spiti_lotes` 251, `spiti_contacts` 507, `crm_spiti` 452

Regra: SPITI pode coexistir no mesmo projeto, mas nunca deve ser usado como evidência de venda real da Zipper.

## 4. Objetivos do Mordomo Zipper

O Mordomo deve responder perguntas operacionais como:

- Quem comprou obra da Flávia Junqueira nos últimos 12 meses?
- Quem gostou ou pediu PDF de Laura Villarosa?
- Quem recebeu proposta e não teve follow-up?
- Quem demonstrou interesse, mas falou que a obra era cara demais?
- Quem foi impactado por determinada artista, feira, exposição ou conteúdo?
- Para quais clientes faz sentido enviar um PDF específico?

E deve conseguir agir, quando aprovado e seguro:

- enviar ou preparar PDF por WhatsApp/e-mail;
- responder perguntas documentais simples de clientes;
- criar drafts de e-mail;
- registrar o envio;
- agendar follow-up;
- excluir automaticamente clientes sem fit quando houver sinal negativo claro.

## 5. Segmentação inteligente: interesse não basta

A segmentação por artista deve combinar sinais positivos e negativos.

Sinais positivos:

- compra anterior do artista;
- pedido de PDF/catálogo;
- resposta positiva sobre obra ou artista;
- proposta enviada;
- conversa sobre preço/disponibilidade;
- presença em feira/exposição relacionada;
- engajamento com conteúdo do artista.

Sinais negativos ou de revisão manual:

- cliente disse que era caro demais;
- faixa de preço incompatível;
- reação negativa;
- pediu para não receber;
- conversa delicada ou negociação em aberto;
- disponibilidade/preço não verificados;
- cliente importante que exige revisão humana.

Exemplo aprovado por Lucas: se uma pessoa mostrou interesse em Flávia Junqueira, mas também deixou claro que R$ 60 mil era caro demais, ela não deve receber automaticamente uma nova mensagem de Flávia Junqueira. Deve ser excluída ou ir para revisão manual.

## 6. Evolução do schema atual

Diretriz aprovada: evoluir o schema existente.

Usar primeiro:

- `contacts`
- `conversations`
- `secretary_log`
- `followups`
- `artists`
- `exhibitions`
- `exhibition_artists`
- `contents`
- `content_metrics`
- `content_tags`
- `vendas_tango`
- tabelas SPITI existentes

Criar views/consultas antes de novas tabelas.

Adicionar campos/tabelas mínimas apenas quando lacunas forem confirmadas. Candidatos:

- `interest_signals`
- `proposal_sends`
- `negative_fit_signals`
- `artist_pdf_assets`
- `client_artist_segments`

O nome final deve respeitar o padrão real do Supabase existente após o mapeamento completo.

## 7. PDFs, artistas e Dropbox

O Mordomo deve manter ou acessar uma base de PDFs/catálogos/propostas por artista/obra.

Fontes previstas:

- Supabase Zipper;
- site público da Zipper;
- acervo/site quando acessível;
- Dropbox de Lucas/Zipper quando conectado com credencial segura;
- PDFs/catálogos internos;
- conversas WhatsApp;
- e-mails;
- dados de vendas.

Site da Zipper já foi verificado como acessível por navegador. Dropbox ainda depende de credencial/conector autorizado.

## 8. Automação de WhatsApp/e-mail

Modelo aprovado: híbrido.

Pode seguir direto quando:

- o cliente/contato está identificado;
- o artista/obra/PDF está cadastrado e validado;
- a pergunta é simples e documental;
- a resposta não envolve preço sensível, desconto, reserva, negociação ou promessa;
- o fluxo está previamente habilitado com logs e kill switch.

Exemplo: cliente pergunta “você pode me enviar as obras disponíveis da Flávia Junqueira?” e há PDF validado. O Mordomo responde com o PDF correto, registra o envio e agenda follow-up.

Precisa preview/aprovação quando:

- cliente novo/importante;
- disponibilidade ou preço incerto;
- negociação, desconto, reserva, prazo ou promessa;
- reclamação ou problema sensível;
- sinal negativo/desfit;
- fonte duvidosa;
- campanha em massa.

## 9. Follow-up automático

O Mordomo deve detectar promessas claras e criar follow-ups naturais.

Exemplo aprovado:

- Sexta: cliente diz “vou ver com minha mulher e te aviso”.
- Segunda: follow-up curto e contextual: “Olá, falou com sua mulher? O que ela achou?”

O follow-up deve respeitar o tom da conversa e o histórico com aquela pessoa. Se houver desfit, objeção forte ou cliente sensível, enviar para revisão manual.

## 10. Guardrails

- Não expor PII em Telegram/Brain sem necessidade.
- Não salvar corpos brutos de conversa/e-mail no Brain.
- Não misturar Zipper com SPITI.
- Não afirmar venda, preço, disponibilidade, lote ou lance sem fonte oficial.
- Não criar campanha/envio em massa sem aprovação e segmentação revisada.
- Todo write em Supabase, WhatsApp, e-mail ou automação precisa de fluxo aprovado; este PRD é design/read-only.

## 11. Fases aprovadas

### Fase 1 — Mapa Supabase Zipper/SPITI

Entregável:

- mapa completo das tabelas, campos, relações prováveis, contagens e lacunas;
- separação Zipper vs SPITI;
- identificação de tabelas vazias ou subutilizadas como `artist_pdfs`/`scheduled_sends` se presentes;
- recomendações de views/tabelas mínimas.

### Fase 2 — Busca inteligente por artista

Entregável:

- consulta/protótipo para “quem comprou/gostou/recebeu proposta de artista X”;
- exclusão por sinais negativos;
- ranking por confiança;
- saída PII-minimizada para Lucas.

### Fase 3 — Fluxo de proposta/PDF

Entregável:

- localizar PDF correto;
- preparar ou enviar conforme regra híbrida;
- registrar `proposal_send` ou equivalente;
- agendar follow-up;
- documentar aprendizado.

## 12. Próximos passos operacionais

### Passo 1 — Mapa completo read-only do Supabase Zipper/SPITI

Executar a Fase 1 em read-only e produzir o relatório:

`areas/zipper/contexto/mordomo-zipper-spiti-supabase-map-2026-05-18.md`

Escopo:

- listar tabelas, campos, contagens e relações prováveis;
- separar Zipper, SPITI e tabelas compartilhadas;
- identificar tabelas vazias/subutilizadas como `artist_pdfs` e `scheduled_sends`, se existirem;
- mapear quais tabelas já cobrem contatos, conversas, follow-ups, PDFs, artistas, exposições, vendas, conteúdo e automações;
- registrar lacunas mínimas para views/campos/tabelas futuras.

Critério de conclusão: relatório salvo no Brain, com zero PII bruta e zero secrets.

### Passo 2 — Protótipo de busca inteligente por artista

Criar uma consulta/protótipo read-only para responder perguntas como:

- quem comprou obra de artista X nos últimos 12 meses;
- quem demonstrou interesse por artista X;
- quem recebeu proposta/PDF de artista X;
- quem deve ser excluído por sinal negativo/desfit.

Critério de conclusão: consulta testada com Flávia Junqueira e Laura Villarosa, saída PII-minimizada para Lucas.

### Passo 3 — Desenho do fluxo proposta/PDF

Desenhar o fluxo operacional para:

- localizar PDF correto por artista/obra;
- decidir entre envio direto, preview ou revisão manual;
- registrar envio/proposta;
- agendar follow-up;
- bloquear clientes com desfit/sinal negativo.

Critério de conclusão: especificação pronta para implementação, sem envio externo ainda.

Nenhum envio externo, write no banco, campanha, WhatsApp/e-mail ou automação será executado sem aprovação específica da fase correspondente.
