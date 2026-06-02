# Addendum PRD — LK Crisp Observe-Only + Aprendizado pelas Respostas da Gisele

Data: 2026-06-01
Área: LK / Atendimento / CRM / Crisp
Decisão Lucas: neste momento, Hermes deve apenas mapear mensagens que chegam, parear com respostas humanas já dadas pela Gisele/time e aprender o padrão correto antes de responder clientes.
Nome/persona da atendente virtual: **Elle** — de “Ele Ka”.
Status: aprovado para seguir com leitura read-only do Crisp; sem envio externo, sem alteração no Crisp.

## 1. Decisão de produto

O MVP imediato não é bot respondendo cliente. O MVP imediato é **aprendizado supervisionado por histórico real**:

```text
Cliente pergunta no WhatsApp/Crisp
→ Gisele/time responde manualmente
→ Hermes lê o par pergunta/resposta
→ Hermes classifica intenção, política, tom e fonte provável
→ Hermes salva lesson/rascunho de regra
→ Lucas/time corrigem quando necessário
→ Só depois vira padrão aprovado
```

## 2. Objetivo do addendum

Construir uma rotina que puxe histórico de conversas do Crisp e transforme respostas reais da Gisele em exemplos de treinamento operacional, sem enviar nada para cliente.

## 3. Fonte preferida

Crisp é a fonte ideal para este estágio porque:

- reúne conversa do cliente e resposta humana no mesmo thread;
- tem metadados de operador, sessão e tempo;
- permite separar `visitor/customer` de `operator`;
- já existem credenciais Crisp no secret store local/Doppler por nome, sem valores expostos;
- já existe documentação anterior de integração Crisp/Hermes no Brain.

## 4. Escopo do Canary 0 — Observe + Learn

### Entrada

- Conversas Crisp recentes.
- Mensagens inbound de clientes.
- Mensagens outbound de operadores humanos, principalmente Gisele.
- Timestamp e ordem da conversa.
- Metadados mínimos: session_id, operator_id/email hash/label, canal, status.

### Saída

- Pares pergunta/resposta sanitizados.
- Classificação de intenção.
- Nível A0-A4.
- Se a resposta humana usou ou deveria usar fonte viva.
- Lessons de tom/estrutura.
- Candidatos a templates aprováveis.
- Alertas de risco quando uma resposta humana não deve virar regra geral.

## 5. O que aprender

Hermes pode aprender:

- como Gisele cumprimenta;
- como pede tamanho/modelo/código;
- como contorna falta de informação;
- como explica próximos passos sem prometer demais;
- quando transfere para humano;
- estrutura de resposta para perguntas recorrentes;
- tom comercial da LK.

Hermes não pode aprender como regra automática:

- desconto dado em caso específico;
- promessa de reserva;
- prazo de entrega sem fonte;
- solução de reclamação;
- exceção comercial;
- decisão sobre troca/devolução;
- qualquer resposta que dependa de pedido/estoque/preço atual sem fonte viva.

## 6. Regra de pareamento pergunta/resposta

Para cada resposta da Gisele/time:

1. Buscar mensagens imediatamente anteriores do cliente na mesma sessão.
2. Montar janela contextual pequena:
   - até 5 mensagens anteriores;
   - até 2 mensagens posteriores se necessário;
   - excluir dados sensíveis no artefato final.
3. Criar par:
   - `customer_question_summary`;
   - `human_reply_summary`;
   - `human_reply_pattern`;
   - `intent`;
   - `autonomy_level`;
   - `source_required`;
   - `reuse_status`.

## 7. Estados de aprendizado

### `approved_pattern_candidate`

Resposta parece segura e recorrente, mas ainda precisa revisão.

### `source_required_pattern`

Boa estrutura, mas só pode ser usada depois de consultar Tiny/Shopify/CRM/Brain.

### `human_only_pattern`

Serve para orientar rascunho, mas não pode virar auto-resposta.

### `blocked_pattern`

Não deve ser reutilizada automaticamente.

## 8. Dados persistidos

### Arquivos Brain

- `areas/lk/sub-areas/atendimento/knowledge/lk-response-brain/daily-lessons/YYYY-MM-DD.md`
- `areas/lk/sub-areas/atendimento/knowledge/lk-response-brain/approved-answer-patterns.md`
- `areas/lk/sub-areas/atendimento/knowledge/lk-response-brain/larissa-gisele-tone.md`
- `areas/lk/sub-areas/atendimento/knowledge/lk-response-brain/blocked-topics.md`

### SQLite local

Tabela sugerida: `human_reply_learning_pairs`

Campos:

- `pair_id`
- `provider` = `crisp`
- `session_id_hash`
- `customer_id_hash`
- `operator_label`
- `operator_id_hash`
- `customer_question_redacted`
- `human_reply_redacted`
- `intent`
- `autonomy_level`
- `source_required`
- `reuse_status`
- `lesson_summary`
- `created_at`

## 9. PII e privacidade

- Não salvar telefone/e-mail bruto no Brain.
- Não salvar corpo integral quando houver dados sensíveis.
- Hash para session/customer/operator quando possível.
- Exemplos no Brain devem ser sanitizados.
- Dados brutos, se necessários temporariamente, ficam em diretório local restrito e não vão para Telegram.

## 10. Métricas do Canary 0

- quantidade de conversas analisadas;
- quantidade de pares pergunta/resposta montados;
- % pares reutilizáveis;
- % pares que exigem fonte viva;
- % casos human-only;
- principais intenções;
- principais lacunas de política;
- exemplos que Lucas precisa revisar.

## 11. Critério de avanço para Draft Mode

Avançar apenas quando:

- pelo menos 50 pares forem analisados;
- Lucas/time revisar os padrões principais;
- houver lista inicial de respostas A0 aprovadas;
- houver bloqueios claros para preço/reserva/prazo/reclamação;
- o sistema provar que não envia nada ao cliente.

## 12. Implementação recomendada agora

1. Criar extractor read-only Crisp histórico.
2. Identificar operador Gisele por metadado Crisp ou label/hash já configurado.
3. Montar pares pergunta/resposta.
4. Sanitizar PII.
5. Classificar A0-A4.
6. Gerar relatório diário local/Brain.
7. Lucas corrige e ensina padrões.
8. Atualizar response brain com approved/blocked/source-required.

## 13. Status técnico verificado

- Existem documentos e receipts anteriores de Crisp no Brain.
- Existem nomes de credenciais Crisp no Doppler/secret store, valores não expostos.
- Existe rotina conceitual anterior `aprendizado-diario-larissa-crisp-hugo.md`; este addendum atualiza o foco para Gisele/time e para observe-only via Crisp/inbox.

## 14. Guardrail final

Até nova aprovação explícita, Hermes neste fluxo deve:

- **ler e analisar** histórico/conversas;
- **não responder cliente**;
- **não criar automação de envio**;
- **não alterar Crisp/Hugo/CRM**;
- **não transformar resposta humana em regra automática sem revisão**.
