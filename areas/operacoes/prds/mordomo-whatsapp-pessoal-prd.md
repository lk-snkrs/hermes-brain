# PRD — Mordomo Hermes para WhatsApp Pessoal

Data: 2026-05-14
Owner: Lucas Cimino
Produto: Hermes Agent / WhatsApp pessoal
Status: draft aprovado conceitualmente, pendente desenho técnico e implementação

## 1. Resumo executivo

Criar um agente pessoal chamado **Mordomo Hermes** para atuar como secretária operacional no WhatsApp pessoal de Lucas. O agente monitora apenas conversas/listas definidas por Lucas, lê mensagens em modo read-only, classifica sinais por contexto e transforma mensagens acionáveis em agenda, lembretes, follow-ups comerciais, tarefas e alertas no Telegram.

O Mordomo pode ler o conteúdo autorizado do WhatsApp pessoal, mas **não envia mensagens externas sem aprovação explícita no Telegram**. Para eventos com data/hora/local claros, pode criar automaticamente o evento no calendário e avisar Lucas no Telegram depois da criação.

## 2. Problema

Lucas recebe no WhatsApp pessoal sinais operacionais misturados entre vida pessoal, LK Sneakers, Zipper Galeria, SPITI Auction, convites, eventos, clientes, feiras, pagamentos, logística, agenda e oportunidades comerciais.

Hoje, esses sinais dependem de leitura manual e memória humana. O risco é perder convites, reuniões, follow-ups, visitas a feiras, oportunidades comerciais e tarefas simples.

## 3. Objetivo

Transformar o WhatsApp pessoal de Lucas em uma camada de entrada operacional segura para Hermes, sem perder privacidade, sem misturar empresas e sem executar ações externas sem aprovação.

O Mordomo deve:

- ler conversas autorizadas;
- identificar mensagens relevantes;
- classificar por contexto;
- criar eventos claros no calendário e avisar;
- preparar follow-ups e lembretes;
- perguntar no Telegram antes de qualquer envio externo;
- aprender com aprovações e correções de Lucas;
- manter trilha de decisão e fonte.

## 4. Decisões de produto já aprovadas

1. **Escopo de leitura:** o Mordomo pode ler todos os contatos, conversas e grupos do WhatsApp pessoal. A restrição não é leitura; a restrição é ação externa.
2. **Autonomia:** modo misto ampliado.
   - Pode criar sozinho eventos, lembretes e tarefas internas quando a intenção estiver clara.
   - Pode preparar follow-ups e pacotes de resposta sozinho.
   - Aprovação obrigatória continua para qualquer envio externo, resposta a cliente/fornecedor/artista/colecionador, dinheiro, proposta, fonte de verdade, produção, infra ou ação sensível.
3. **Calendário:** se data/hora/local estiverem claros, criar o evento direto e avisar Lucas no Telegram.
4. **Calendários por contexto:** eventos gerais/Zipper usam `lucas@zippergaleria.com.br`. Eventos da LK usam `lk@lksneakers.com.br`.
5. **Follow-up comercial:** preparar texto e criar/agendar lembrete; pedir aprovação antes de enviar.
6. **Canal de aprovação:** Telegram.
7. **Categorias V1:** todas as categorias propostas entram no escopo.
8. **Frequência:** resumo 2x por dia, às 09:00 e 17:00 BRT, + gatilhos urgentes/quase real.
9. **Gatilhos em tempo real:** todos os gatilhos sugeridos estão aprovados para alertar em quase tempo real.
10. **Privacidade:** Lucas autorizou leitura ampla do WhatsApp pessoal para o Mordomo. O cuidado de privacidade continua na persistência, exposição em Telegram e ações externas.
11. **Aprendizado:** memória curta + manual operacional versionado no Hermes Brain.
12. **Tom por cliente:** sempre que Lucas responder um cliente, o Mordomo deve aprender o tom específico usado com aquela pessoa. Alguns clientes exigem formalidade; outros permitem proximidade. Para cliente desconhecido ou sem histórico, usar base mais formal.
13. **Nome/persona:** Mordomo Hermes.

## 5. Persona e tom

Nome: **Mordomo Hermes**.

Tom:

- discreto;
- objetivo;
- elegante;
- sem intimidade falsa;
- com bom senso cultural/comercial;
- não invasivo;
- sempre separando fato, hipótese e ação recomendada.

Exemplo de voz:

> Lucas, encontrei um convite com data, horário e local completos. Criei no calendário e deixei a fonte registrada.

> Esse cliente mencionou que irá à ARPA. Preparei um follow-up no tom Zipper. Quer que eu agende o lembrete ou envie apenas se você aprovar?

## 6. Escopo V1

### 6.1 Fontes

- WhatsApp pessoal, conta `pessoal`, usando wacli/OpenClaw local.
- Calendário Google de Lucas, quando autorizado.
- Telegram como canal de aprovação e resumo.
- Hermes Brain para manual operacional e aprendizado não sensível.

### 6.2 Categorias monitoradas

- Agenda, eventos e convites.
- Clientes e leads.
- Feiras e eventos da Zipper.
- Compras e fornecedores LK.
- SPITI, leilões, lotes e clientes.
- Financeiro, pagamentos e cobranças.
- Entregas e logística.
- Família e pessoal.
- Saúde, viagem e documentos.
- Infra/Hermes.
- Outros sinais acionáveis.

### 6.3 Escopo de conversas

V1 pode ler o WhatsApp pessoal inteiro: todos os contatos, conversas individuais e grupos. Lucas explicitou que não há problema em o Mordomo ler tudo.

A governança deve se concentrar em:

- não enviar nada sem aprovação;
- não expor conteúdo privado desnecessário no Telegram;
- não salvar bruto no Brain/Git;
- aprender tom e contexto por cliente;
- reduzir ruído com ranking de relevância.

Comandos futuros úteis:

- `pausar chat X`
- `silenciar grupo X no resumo`
- `monitorar apenas agenda neste grupo`
- `não aprender tom desse contato`
- `esse cliente é próximo`
- `esse cliente exige formalidade`

## 7. Fora de escopo V1

- Envio automático de WhatsApp para terceiros.
- Responder clientes sem aprovação.
- Prometer preço, disponibilidade, desconto, obra, lote, entrega ou prazo sem fonte de verdade.
- Ações em Shopify, Supabase, bancos, campanhas, Meta/Google, SPITI Hub ou produção.
- Mineração irrestrita de todos os grupos sem lista definida.
- Decisões financeiras autônomas.

## 8. Matriz de autonomia A0-A4

### A0/A1 — pode executar sem perguntar

- Ler mensagens de todos os contatos, conversas e grupos do WhatsApp pessoal.
- Classificar sinais.
- Gerar resumo local/Telegram.
- Criar evento quando data/hora/local estiverem claros, escolhendo calendário por contexto.
- Avisar Lucas que evento foi criado.
- Criar lembrete interno sem envio externo.
- Criar tarefa interna quando a intenção estiver clara.
- Registrar aprendizado operacional não sensível.
- Aprender tom por cliente a partir das respostas enviadas por Lucas.

### A2 — pode preparar e pedir aprovação

- Preparar follow-up comercial.
- Preparar mensagem para cliente/fornecedor/contato.
- Preparar tarefa futura.
- Preparar proposta de agenda quando data/hora/local estiverem incompletos.
- Preparar resumo de conversa com PII minimizada.

### A3 — exige plano/rollback/aprovação se virar fonte de verdade

- Escrever em CRM/Supabase/planilha oficial.
- Alterar calendário crítico compartilhado com múltiplas pessoas.
- Registrar decisões como fonte oficial.
- Integrar com sistemas de negócio.

### A4 — sempre exige aprovação atual com conteúdo inline

- Enviar WhatsApp para qualquer pessoa.
- Enviar email.
- Confirmar presença em evento pelo telefone/WhatsApp.
- Falar com cliente, fornecedor, artista, colecionador, bidder ou parceiro.
- Envolver dinheiro, preço, desconto, pagamento, cobrança ou proposta.
- Executar ação de produção, infraestrutura, secrets ou banco.

## 9. Fluxos principais

### 9.1 Convite/evento claro

Entrada:

- mensagem contém data, hora e local.

Processo:

1. Ler mensagem.
2. Extrair título, data, hora, local, descrição e origem.
3. Verificar calendário para conflito relevante.
4. Criar evento automaticamente.
5. Avisar Lucas no Telegram.

Mensagem Telegram:

> Lucas, criei no calendário: Preview Pinakotheke — Surrealismos, 15/05, 19h–21h, Rua Minas Gerais, 246. Origem: WhatsApp, Katia Maciel. Conflitos: nenhum relevante.

### 9.2 Convite/evento incompleto

Entrada:

- mensagem sugere evento, mas falta data, hora ou local.

Processo:

1. Extrair o que existe.
2. Não criar evento.
3. Perguntar no Telegram.

Mensagem Telegram:

> Lucas, isso parece um evento, mas falta horário. Quer que eu pergunte para a pessoa, crie lembrete provisório ou ignore?

### 9.3 Lead/cliente em feira Zipper/ARPA

Entrada:

- cliente diz que irá à ARPA ou feira/evento onde a Zipper participa.

Processo:

1. Classificar como Zipper + oportunidade comercial.
2. Preparar follow-up culturalmente sofisticado, sem hard sell.
3. Criar sugestão de lembrete.
4. Perguntar no Telegram.

Mensagem Telegram:

> Lucas, esse cliente disse que vai à ARPA. Quer que eu agende um lembrete e prepare uma mensagem para ele visitar o estande da Zipper? Sugestão de texto: [texto inline].

Nunca enviar sem aprovação.

### 9.4 Cliente pede proposta/preço/obra

Processo:

1. Classificar contexto: Zipper, LK ou SPITI.
2. Buscar fonte de verdade se disponível e aprovado.
3. Se não houver fonte, declarar desconhecido.
4. Preparar resposta para aprovação.

Regra:

- silêncio > informação errada, especialmente SPITI.

### 9.5 Financeiro/pagamento/cobrança

Processo:

1. Classificar como sensível.
2. Resumir minimamente.
3. Nunca executar pagamento/cobrança.
4. Perguntar no Telegram com risco A4.

### 9.6 Resumo diário

Frequência:

- 2x por dia: 09:00 e 17:00 BRT.
- Gatilhos urgentes aprovados para alerta quase em tempo real.

Conteúdo:

- eventos criados;
- aprovações pendentes;
- follow-ups sugeridos;
- mensagens importantes não resolvidas;
- riscos por empresa;
- aprendizados/correções.

Formato:

```text
Mordomo Hermes — resumo

Agenda:
- Evento X criado para 15/05, 19h.

Aprovações pendentes:
- Zipper: cliente Y mencionou ARPA. Preparar follow-up?

Riscos:
- SPITI: mensagem menciona lote sem fonte verificada. Nenhuma resposta preparada.

Aprendizado:
- Feiras Zipper: perguntar antes de agendar/enviar follow-up.
```

## 10. Classificação multiempresa

Toda mensagem relevante deve receber:

- contexto: pessoal, LK, Zipper, SPITI, Hermes/Infra ou indefinido;
- categoria;
- risco A0-A4;
- fonte;
- confiança;
- próxima ação segura.

### LK Sneakers

Tom: premium, comercial, analítico.

Atenção:

- fornecedores;
- produtos;
- compras;
- clientes;
- loja;
- campanhas;
- pedidos.

Nunca:

- prometer estoque/preço/prazo sem fonte;
- enviar campanha sem aprovação.

### Zipper Galeria

Tom: culturalmente sofisticado, leve, sem hard sell.

Atenção:

- colecionadores;
- artistas;
- feiras;
- ARPA;
- propostas;
- visitas;
- obras.

Nunca:

- pressionar cliente;
- prometer preço/disponibilidade sem fonte;
- falar de obra/artista de forma imprecisa.

### SPITI Auction

Regra central: silêncio > dado errado.

Atenção:

- lotes;
- bids;
- leilões;
- clientes;
- CRM;
- prazos.

Nunca:

- inferir lance/lote de conversa isolada;
- responder cliente sem fonte verificada.

### Hermes/Infra

Atenção:

- VPS;
- Docker;
- runtime;
- tokens;
- falhas;
- automações.

Nunca:

- reiniciar, alterar infra, deployar ou tocar secrets sem aprovação e rollback.

## 11. Aprendizado

O Mordomo aprende em duas camadas:

### 11.1 Memória curta/perfil

Usada para preferências estáveis e regras compactas, por exemplo:

- ARPA/feiras Zipper geram pergunta no Telegram antes de follow-up.
- Eventos claros podem ser criados e avisados.

### 11.2 Manual operacional no Hermes Brain

Documento versionado com:

- gatilhos;
- exemplos aprovados;
- exemplos rejeitados;
- tom por empresa;
- matriz A0-A4;
- templates de pergunta;
- templates de mensagem para aprovação.

Não salvar PII bruta, conversas privadas completas ou segredos.

## 12. Dados e privacidade

Lucas autorizou leitura dentro do escopo definido. Ainda assim, a implementação deve seguir higiene mínima:

- não expor mensagens inteiras no Telegram salvo quando necessário;
- preferir resumo e IDs internos;
- não salvar conteúdo bruto no Git/Hermes Brain;
- não salvar mídia pessoal sem necessidade;
- não imprimir telefones completos em logs finais;
- manter extratos temporários em caminho restrito e limpar quando possível;
- nunca commitar dumps de WhatsApp.

## 13. Requisitos funcionais

### RF1 — Leitura ampla com filtros de ruído

O sistema deve poder ler todos os chats, contatos e grupos do WhatsApp pessoal de Lucas, mantendo controles para pausar, silenciar ou reduzir prioridade de conversas específicas.

### RF2 — Sync/read-only

O sistema deve ler mensagens novas da conta `pessoal` sem enviar nada.

### RF3 — Classificador

O sistema deve classificar mensagens por contexto, categoria, risco, confiança e próxima ação.

### RF4 — Calendário automático

Quando evento claro for detectado, o sistema deve criar evento no calendário configurado por contexto e avisar Lucas no Telegram.

- Geral/Zipper: `lucas@zippergaleria.com.br`.
- LK: `lk@lksneakers.com.br`.

### RF5 — Pergunta de aprovação

Para qualquer mensagem externa/follow-up, o sistema deve perguntar no Telegram com texto proposto inline.

### RF6 — Resumo diário

O sistema deve enviar resumo 2x por dia.

### RF7 — Gatilhos urgentes

O sistema deve alertar quase em tempo real para categorias críticas: evento próximo, cliente importante, pagamento/cobrança, SPITI sensível, infraestrutura/secrets, oportunidade comercial quente.

### RF8 — Aprendizado

O sistema deve registrar correções de Lucas em manual operacional e/ou memória compacta.

## 14. Requisitos não funcionais

- Segurança por padrão.
- Read-only por padrão no WhatsApp.
- Logs sem segredos/PII desnecessária.
- Operação reversível.
- Sem dependência de envio automático.
- Resiliência a mensagens duplicadas.
- Idempotência para calendário: evitar criar o mesmo evento duas vezes.
- Rate limiting para não spammar Telegram.
- Separação entre pessoal, LK, Zipper, SPITI e Hermes.

## 15. Critérios de aceite V1

1. Sistema lê mensagens novas do WhatsApp pessoal amplo, com capacidade de pausar/silenciar chats específicos.
3. Sistema detecta evento claro e cria calendário uma única vez.
4. Sistema avisa no Telegram após criação.
5. Sistema detecta lead/feira Zipper e pergunta antes de follow-up.
6. Sistema prepara texto inline para aprovação.
7. Sistema envia resumo diário 2x por dia.
8. Sistema registra correção de Lucas no manual.
9. Sistema nunca envia WhatsApp sem aprovação atual.
10. Sistema não mistura LK/Zipper/SPITI.

## 16. Métricas de sucesso

- Eventos úteis criados sem retrabalho.
- Follow-ups comerciais não perdidos.
- Redução de mensagens importantes esquecidas.
- Baixo ruído no Telegram.
- Zero mensagens externas enviadas sem aprovação.
- Zero vazamento de PII/segredos em logs ou Brain.
- Correções de Lucas incorporadas ao manual.

## 17. Riscos

### R1 — Ruído excessivo

Mitigação: allowlist + resumo 2x/dia + urgência limitada.

### R2 — Erro de classificação

Mitigação: mostrar confiança e perguntar quando ambíguo.

### R3 — Evento duplicado

Mitigação: dedupe por título/data/local/origem antes de criar.

### R4 — Mistura de empresas

Mitigação: classificador multiempresa + fonte/contexto obrigatório.

### R5 — Privacidade

Mitigação: não salvar bruto, Telegram com resumo, logs restritos.

### R6 — Ação externa indevida

Mitigação: WhatsApp send desabilitado na V1, aprovação A4 obrigatória.

## 18. Arquitetura sugerida

Componentes:

1. **WhatsApp Intake**
   - wacli `--account pessoal`.
   - Busca mensagens novas em chats autorizados.

2. **Normalizer**
   - Remove mídia desnecessária.
   - Extrai texto/caption/data/origem.

3. **Classifier**
   - Contexto multiempresa.
   - Categoria.
   - Risco A0-A4.
   - Confiança.

4. **Action Router**
   - Evento claro → calendar create + Telegram receipt.
   - Follow-up → Telegram approval packet.
   - Sensível → Telegram alert.
   - Baixa prioridade → resumo diário.

5. **Calendar Adapter**
   - Google Calendar via OAuth/Doppler.
   - Dedupe antes de criar.

6. **Telegram Approval Adapter**
   - Envia perguntas e pacotes de aprovação.
   - Inclui texto inline.

7. **Learning Store**
   - Manual operacional no Hermes Brain.
   - Memória compacta para preferências estáveis.

8. **Audit Log**
   - IDs, timestamps, hash de mensagem, ação tomada.
   - Sem conteúdo bruto salvo desnecessariamente.

## 19. Templates

### 19.1 Evento criado

```text
Mordomo Hermes

Criei no calendário:
- Evento: [título]
- Quando: [data/hora]
- Local: [local]
- Origem: WhatsApp, [contato/grupo]
- Conflito: [nenhum / possível conflito]
```

### 19.2 Aprovação de follow-up

```text
Mordomo Hermes

Sinal encontrado:
- Contexto: Zipper
- Pessoa: [nome]
- Sinal: vai à ARPA
- Risco: A4 se enviar mensagem

Sugestão:
"[texto proposto]"

Quer que eu:
1. Agende lembrete
2. Envie após sua aprovação
3. Ignore
4. Ajuste o texto
```

### 19.3 Ambiguidade

```text
Mordomo Hermes

Encontrei algo possivelmente importante, mas está ambíguo:
- Fonte: [chat]
- Possível categoria: [evento/cliente/financeiro]
- Falta: [data/hora/contexto]

Quer que eu investigue, pergunte para a pessoa, crie lembrete ou ignore?
```

## 20. Próximas perguntas técnicas antes de implementação

1. Qual calendário deve ser usado para eventos estritamente pessoais, quando não forem Zipper nem LK? Usar `lucas@zippergaleria.com.br` por padrão ou outro?
2. Onde salvar o manual operacional definitivo no Hermes Brain?
3. O resumo 09:00/17:00 deve ser enviado todos os dias ou só dias úteis?
4. Para tarefas internas, qual destino preferido: Telegram reminder, cron job, calendário como lembrete, ou arquivo/manual no Brain?

## 21. Próximo passo recomendado

Criar um plano de implementação V1 em branch/local, sem envio de WhatsApp, com:

- allowlist de chats;
- cron de leitura;
- classificador;
- calendário automático com dedupe;
- Telegram approval packets;
- resumo diário;
- manual operacional.

Nível de risco: A1/A2 enquanto read-only + calendário autorizado + Telegram. A4 para qualquer envio externo.
