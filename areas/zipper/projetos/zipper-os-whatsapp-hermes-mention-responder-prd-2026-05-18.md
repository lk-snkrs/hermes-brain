# PRD — Zipper OS · Hermes responder no WhatsApp por menção

Data: 2026-05-18  
Status: PRD v1  
Área: Zipper OS / Operações internas / WhatsApp  
Grupo alvo: `[ZPR] IA Bot`  
Conta WhatsApp: `hermes`  

## 1. Contexto

Lucas pediu que o Hermes saiba responder perguntas sobre a Zipper Galeria dentro do grupo WhatsApp `[ZPR] IA Bot`, quando for marcado/mencionado.

A rotina existente do Zipper OS já envia report diário de vendas no grupo, usando Supabase `vendas_tango` como fonte de verdade para vendas. Este PRD define a próxima camada: um responder interno, sob menção explícita, para perguntas operacionais sobre Zipper.

## 2. Objetivo

Criar um agente de resposta interna no WhatsApp que:

1. Escute apenas o grupo aprovado `[ZPR] IA Bot`.
2. Responda somente quando o Hermes for mencionado ou quando a mensagem for reply direto a uma mensagem do Hermes.
3. Responda perguntas sobre Zipper Galeria com base em fontes internas confiáveis, incluindo vendas, CRM Zipper, conteúdos, artistas, exposições e Brain — sempre em modo read-only na V1.
4. Mantenha tom cultural, objetivo e sem hard sell.
5. Não fale com clientes/coletadores/artistas fora desse grupo.
6. Não execute writes externos sem aprovação.

## 3. Não objetivos

- Não substituir atendimento humano da Zipper.
- Não responder em grupos ou conversas não allowlistados.
- Não enviar proposta comercial, preço, disponibilidade ou compromisso para cliente externo.
- Não criar follow-up, Gmail draft, evento ou ação operacional sem gate próprio.
- Não usar SPITI/LK como fonte para fatos Zipper.
- Não inferir venda a partir de conversa; venda vem de `vendas_tango`.

## 4. Usuários

- Lucas Cimino.
- Time interno Zipper no grupo `[ZPR] IA Bot`.
- Hermes como assistente operacional interno.

## 5. Fontes de verdade

### Vendas

- Supabase Zipper Vendas: projeto `pcstqxpdzibheuopjkas`.
- Tabela: `vendas_tango`.
- Uso: vendas realizadas, totais, artistas vendidos, origem/canal, report mensal.
- Modo: read-only.

### CRM / Operação / Conteúdo

- Supabase CRM/Main como fonte ampla read-only do Zipper: projeto `rmdugdkantdydivgnimb`.
- Tabelas conhecidas: `contacts`, `conversations`, `secretary_log`, `followups`, `contents`, `artists`, `exhibitions`.
- Uso: contexto operacional interno, CRM, conteúdos, artistas, exposições, conversas e follow-ups — nunca como confirmação final de venda realizada.

### Brain Zipper

- PRDs e documentação em `/opt/data/hermes_bruno_ingest/hermes-brain/areas/zipper/`.
- Textos de artistas: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/zipper/sub-areas/comunicacao/artistas/`.
- Uso: contexto cultural/biográfico, não preço/disponibilidade/proposta.

### WhatsApp

- Conta: `hermes`.
- Grupo allowlistado: `[ZPR] IA Bot`.
- JID já validado pela rotina de report: `120363423418674006@g.us`.

## 6. Matriz de autonomia

### A0 — Sempre permitido

- Ler mensagens novas do grupo allowlistado.
- Detectar menção ao Hermes ou reply a mensagem do Hermes.
- Classificar pergunta: vendas, artista, exposição, operação, desconhecido.
- Consultar fontes internas read-only.
- Responder com informação factual interna quando segura.
- Dizer “não encontrei com segurança” quando faltarem dados.

### A1 — Permitido com cautela

- Responder totais de venda do mês, artistas vendidos, origem/canal, dados já no report.
- Responder resumo cultural de artista a partir dos textos do Brain.
- Responder perguntas sobre status de rotina interna, como report diário.

### A2 — Preview primeiro

- Sugestões de follow-up, texto para cliente, e-mail, convite, lembrete ou cobrança.
- Resposta que envolva compromisso comercial ou tom sensível.
- Deve responder com draft/preview interno e pedir aprovação de Lucas antes de enviar externamente.

### A3 — Bloqueado sem aprovação explícita

- Criar evento de calendário.
- Criar Gmail draft.
- Atualizar CRM/Supabase.
- Mudar cron/job.
- Gerar proposta ou promessa de disponibilidade/preço.

### A4 — Nunca automático

- Enviar WhatsApp/e-mail para cliente, colecionador, artista, fornecedor ou produção fora do grupo aprovado.
- Confirmar compra/venda sem fonte `vendas_tango`.
- Prometer reserva, entrega, retirada ou prazo.
- Misturar dados SPITI/LK com Zipper.

## 7. Trigger de resposta

O responder só deve agir se TODAS as condições forem verdadeiras:

1. Mensagem veio do grupo JID allowlistado.
2. Conta usada é `hermes`.
3. Mensagem menciona Hermes ou é reply a uma mensagem enviada pelo Hermes.
4. Mensagem não é duplicada já processada.
5. Conteúdo não é vazio e não é apenas reação/sticker/mídia sem texto.

O responder deve ignorar silenciosamente:

- Mensagens sem menção/reply.
- Outros grupos.
- Conversas privadas.
- Mensagens antigas já processadas.
- Mídia sem texto.

## 8. Tipos de pergunta V1

### 8.1 Vendas do mês

Exemplos:

- “@Hermes quanto vendemos esse mês?”
- “@Hermes quais artistas venderam?”
- “@Hermes resumo das vendas da Zipper?”

Resposta deve usar `vendas_tango` e período mês corrente até ontem, alinhado ao report diário.

### 8.2 Quantidade por artista

Exemplo:

- “@Hermes quantas obras da Janaina venderam?”

Resposta deve informar quantidade de obras/linhas e total quando disponível.

### 8.3 Origem/canal

Exemplo:

- “@Hermes vendas vieram de onde?”

Resposta deve consolidar `pedido_origem` e, se relevante, `pedido_evento`.

### 8.4 Artista / texto cultural

Exemplo:

- “@Hermes me lembra quem é João Castilho?”

Resposta deve usar textos do Brain, com tom cultural, breve e sem inventar.

### 8.5 Exposição/evento

Exemplo:

- “@Hermes temos algo sobre exposição X?”

V1 pode responder apenas se houver fonte clara no Brain/Supabase read-only; caso contrário, pedir checagem humana.

### 8.6 Desconhecido ou sensível

Responder:

> Não encontrei uma fonte segura para responder isso agora. Posso preparar um caminho de checagem no Zipper OS.

## 9. Formato de resposta WhatsApp

Respostas curtas, internas, sem excesso.

Template geral:

```text
Zipper OS · [assunto]

[Resposta objetiva]

Fonte: [fonte segura]
```

Para vendas:

```text
Zipper OS · Vendas do mês

De 01/05 a 17/05:
• Total vendido: R$ ...
• Obras/vendas: N
• Artistas/obras: Nome (N obras), ...
• Origem: Art Advisor (...), Galeria (...)

Fonte: Supabase vendas_tango.
```

## 10. Segurança e privacidade

- Não incluir telefone, e-mail, endereço ou dado pessoal de cliente no WhatsApp por padrão.
- Não imprimir secrets em logs.
- Logs devem salvar message_id, group_jid, intent, fontes usadas, status e hash do texto, não o conteúdo bruto completo quando desnecessário.
- Receipts locais devem ficar chmod restrito.
- Em erro, alertar Lucas/Telegram apenas com mensagem sanitizada.

## 11. Arquitetura proposta

### Componentes

1. `zipper_group_mention_responder.py`
   - Loop/watchdog ou webhook listener do `wacli`.
   - Filtra grupo/menção/reply.
   - Deduplica mensagens.
   - Chama roteador de intents.
   - Envia resposta no grupo quando seguro.

2. `zipper_knowledge.py`
   - Funções read-only para vendas MTD via Supabase.
   - Busca textual em Brain de artistas.
   - Utilidades de formatação cultural.

3. `zipper_group_responder_watchdog.py`
   - Mantém processo vivo ou roda poll incremental.
   - Silencioso quando OK/no-op.
   - Em falha, alerta sanitizado.

4. Estado local:
   - `/opt/data/hermes_bruno_ingest/local_sql/zipper_group_responder/state.json`
   - `/opt/data/hermes_bruno_ingest/local_sql/zipper_group_responder/receipts.jsonl`

## 12. Plano de implementação seguro

### Fase 1 — Read-only/dry-run

- Validar auth da conta `hermes`.
- Validar grupo `[ZPR] IA Bot`.
- Ler últimas mensagens do grupo sem enviar.
- Detectar menções/replies e registrar intent em dry-run.
- Testar parser de perguntas.

### Fase 2 — Respostas simuladas

- Gerar resposta local sem enviar.
- Salvar preview/receipt.
- Testar perguntas de vendas/artistas/desconhecido.

### Fase 3 — Envio controlado no grupo

- Ativar envio apenas para grupo allowlistado.
- Enviar resposta quando mencionado.
- Deduplicar por message_id.
- Registrar receipt.

### Fase 4 — Watchdog silencioso

- Agendar/rodar watcher.
- No-op silencioso.
- Erros alertam e são auto-corrigidos quando seguros.

## 13. Critérios de aceite

- Sem menção: Hermes não responde.
- Menção no grupo `[ZPR] IA Bot`: Hermes responde.
- Outro grupo/DM: Hermes ignora.
- Pergunta de vendas: resposta usa `vendas_tango` e mês corrente até ontem.
- Pergunta de artista/CRM/exposição/conteúdo: resposta usa Brain + Supabase CRM/Main read-only quando disponível.
- Pergunta sensível: Hermes não inventa e não promete.
- Nenhum write em Supabase/CRM.
- Nenhum envio externo fora do grupo aprovado.
- Logs sem secrets.
- Deduplicação funcionando.
- Watchdog no-op silencioso.

## 14. Testes mínimos

- Parser de menção com `@Hermes`, reply e possíveis IDs numéricos/LID.
- Dedup por message_id.
- Intent: vendas_mtd.
- Intent: artista_bio.
- Intent: desconhecido.
- Guardrail: outro grupo não envia.
- Guardrail: sem menção não envia.
- Guardrail: pergunta sensível gera resposta segura.
- Supabase read-only retorna consolidado MTD.
- Secret scan em resposta/log.

## 15. Decisões pendentes

1. Nome/menção exata observada no grupo para o Hermes: pode aparecer como nome, número ou LID. Precisa ser medido em dry-run.
2. Se respostas devem citar “Fonte: Supabase vendas_tango” sempre ou só em perguntas numéricas.
3. Limite de tamanho da resposta no WhatsApp.
4. Se o responder deve ter comando `@Hermes ajuda` com lista de perguntas suportadas.

## 16. Próxima ação recomendada

Implementar Fase 1 em dry-run, sem envio automático:

- descobrir formato real de menção ao Hermes no `[ZPR] IA Bot`;
- ler/poll incremental sem responder;
- produzir receipts locais de detecção;
- só depois ativar envio controlado.
