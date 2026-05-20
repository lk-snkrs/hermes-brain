# PRD — lucas@zippergaleria.com.br: intake, triagem e drafts do Mordomo

Atualizado: 2026-05-18
Status: v0.1 operacional — acesso validado; geração automática de drafts em modo controlado/dry-run antes de ativação ampla

## 1. Objetivo

Transformar `lucas@zippergaleria.com.br` em uma caixa operacional assistida pelo Mordomo para Zipper Galeria: ler e-mails recebidos, separar ruído de mensagens acionáveis, registrar clientes/assuntos no Brain/CRM, criar follow-ups e preparar drafts com linguagem de Lucas quando for seguro.

## 2. Estado técnico verificado

- Conta verificada via Gmail API: `lucas@zippergaleria.com.br`.
- IMAP de rascunhos disponível: sim.
- Helper existente: `/opt/data/scripts/zipper_gmail_draft_helper.py`.
- State file do helper: `/opt/data/state/zipper_auto_drafts.json`.
- PRD global relacionado: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/prds/mordomo-email-intake-prd-2026-05-18.md`.
- PRD Mordomo global: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/prds/mordomo-global-intake-followup-prd-2026-05-18.md`.

## 3. Escopo da conta

`lucas@zippergaleria.com.br` cobre, para o Mordomo:

- clientes e colecionadores Zipper;
- artistas e representantes quando houver relação comercial/curatorial;
- contatos de arquitetos, instituições, curadores e parceiros;
- leads de obra/artista/PDF/proposta;
- exposições novas, convites, feiras, imprensa e oportunidades relacionais;
- follow-ups comerciais/relacionais.

Fora do foco por padrão:

- financeiro, pagamentos, boletos, notas, comprovantes, fechamentos mensais, parcelas e repasses de artista. Lucas corrigiu que isso é assunto dele/Cibele e não deve gerar alerta/ação por padrão.

Não misturar com LK, SPITI ou pessoal sem classificação explícita.

## 4. Classificação antes de draft

Cada e-mail deve ser classificado como:

- `lead_comercial`: interesse em obra/artista/PDF/proposta;
- `cliente_respondeu_pdf`: cliente respondeu a PDF ou follow-up;
- `preco_disponibilidade`: pedido de valor, disponibilidade, reserva ou condição específica;
- `logistica_producao`: coleta, entrega, montagem, retirada, agenda de obra;
- `financeiro_admin`: pagamento, nota, cobrança, imposto;
- `artista_relacao`: comunicação com artista/estúdio;
- `evento_institucional`: feira, exposição, convite, instituição;
- `newsletter_ruido`: marketing/boletim sem ação;
- `unknown`: precisa de revisão.

## 5. Autonomia de drafts

### Pode gerar draft sozinho

- Resposta cordial a lead genérico quando não envolve preço/disponibilidade e há material validado.
- Agradecimento/acknowledgment simples.
- Follow-up leve já aprovado por contexto.
- Pedido interno de mais informação quando não há compromisso comercial.

### Não deve gerar draft externo automaticamente sem revisão mais forte

Pode gerar Decision Packet, mas não draft final pronto quando houver:

- preço, disponibilidade, reserva, desconto, condição de pagamento específica;
- promessa de prazo ou logística sensível;
- contrato, nota, pagamento, cobrança;
- conflito, reclamação ou objeção;
- mensagem de artista com decisão curatorial/comercial;
- qualquer ambiguidade de destinatário ou empresa.

## 6. Regras Zipper para linguagem

- Tom pessoal, cultural, elegante, sem hard sell.
- Lucas como sócio-diretor.
- Para lead de artista, falar das obras do/da artista e dos trabalhos disponíveis.
- Não explicar preventivamente que obra do site pode estar vendida.
- Não perguntar “quais obras?” no primeiro WhatsApp; em e-mail curatorial mais completo, a pergunta pode entrar quando natural.
- Para Flávia Junqueira, usar template curatorial salvo em `/opt/data/hermes_bruno_ingest/hermes-brain/areas/zipper/comunicacao/templates/email-flavia-junqueira-obras-disponiveis-2026-05-18.md`.

## 7. Pipeline desejado

1. Rodar varredura frequente de `lucas@zippergaleria.com.br`.
2. Ignorar newsletters/ruído.
3. Para e-mails acionáveis:
   - ler histórico da thread;
   - classificar;
   - extrair contato/assunto/artista/obra/prazo;
   - registrar ou atualizar caso no Brain/CRM;
   - criar follow-up quando aplicável;
   - gerar draft se classe for segura;
   - caso contrário, gerar Decision Packet para Lucas.
4. Nunca enviar diretamente sem subfluxo aprovado ou aprovação corrente.

## 8. Critério para ativar auto-drafts reais

Ativar gradualmente:

- Fase 1: dry-run — listar candidatos e classificar sem criar rascunhos.
- Fase 2: draft-only para leads simples e respostas leves.
- Fase 3: draft-only com anexos/PDF validado.
- Fase 4: follow-up externo fechado A2 quando já aprovado por Lucas.

Drafts devem ser rastreados por message/thread ID para evitar duplicidade.

## 9. Estado atual em 2026-05-18

- Acesso técnico confirmado.
- Script de helper existe e consegue criar rascunhos via IMAP.
- Ainda não há cron ativo de e-mail/drafts; cron ativo atual é apenas WhatsApp global.
- Teste de candidatos recente retornou 3 e-mails; nenhum é lead simples óbvio para draft automático imediato.

## 10. Próximo passo recomendado

Criar cron de e-mail `dry-run` a cada 10 minutos para:

- detectar e-mails acionáveis;
- classificar;
- criar Decision Packet/draft candidate no Brain;
- permanecer silencioso quando não houver ação.

Depois de 24h calibrando falsos positivos, ativar criação real de rascunhos para classes seguras.
