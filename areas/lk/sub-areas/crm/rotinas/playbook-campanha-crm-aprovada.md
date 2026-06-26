# Playbook — LK Campanha CRM Aprovada

## Objetivo

Transformar oportunidade de CRM em campanha segura, com segmentação real, recomendação coerente e aprovação explícita antes de qualquer envio.

## Quando usar

- Cross-sell pós-pedido.
- Reativação de clientes parados.
- Segmentos RFM.
- Segunda compra e retenção 90 dias.
- Campanhas Klaviyo/Evolution/WhatsApp com base em comportamento de compra.

## Fontes

1. Supabase LK e/ou Shopify para pedidos, clientes e produtos.
2. `memories/lk.md` para metas e decisões vigentes.
3. `areas/lk/sub-areas/crm/MAPA.md` para regra do loop CRM.
4. Skills canônicas:
   - `areas/lk/sub-areas/crm/skills/cross-sell/SKILL.md`.
   - `areas/lk/sub-areas/crm/skills/leads-esfriando/SKILL.md`.
5. Rotinas:
   - `areas/lk/sub-areas/crm/rotinas/rfm-semanal.md`.
   - `areas/lk/sub-areas/crm/rotinas/outcomes-tracker.md`.
   - `areas/lk/sub-areas/crm/rotinas/cross-sell-monitor.md`.

## Loop

```text
segmento → evidência de compra/interesse → produto elegível em estoque → mensagem/benefício → preview Lucas → envio aprovado → resultado → lesson
```

## Checklist antes do preview

- [ ] Segmento definido com critério claro.
- [ ] Fonte consultada e data da consulta registrada.
- [ ] Produto recomendado está em estoque.
- [ ] Regra de 90 dias respeitada quando aplicável.
- [ ] Mensagem não promete disponibilidade/preço sem confirmação.
- [ ] Canal proposto identificado: Klaviyo, Evolution/WhatsApp, email, Telegram interno ou outro.
- [ ] Métrica de sucesso definida: segunda compra, receita, resposta, clique, conversão ou aprendizado.

## Preview para Lucas

Toda campanha externa deve chegar a Lucas como rascunho:

```text
Campanha proposta: ...
Segmento: ...
Tamanho do segmento: [consultado / a confirmar]
Fonte: ...
Oferta/mensagem: ...
Produtos: ...
Canal: ...
Risco/ressalva: ...
Métrica de sucesso: ...
Aprovação necessária: responder APROVADO para enviar / ajustar / cancelar
```

## Execução

Somente depois de aprovação explícita:

1. Preparar payload ou instrução operacional.
2. Validar canal e ambiente.
3. Executar apenas o escopo aprovado.
4. Registrar horário, segmento, canal e identificador da campanha.
5. Criar lembrete/rotina para leitura de resultado.

## Pós-campanha

Registrar:

- resultado quantitativo;
- respostas qualitativas;
- problemas de segmentação ou estoque;
- hipótese validada/invalidada;
- próxima ação sugerida.

## Proibido sem aprovação

- Enviar mensagem real.
- Criar campanha ativa.
- Subir público/audiência.
- Alterar orçamento ou automação.
- Modificar dados de cliente.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Playbook — LK Campanha CRM Aprovada` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Playbook — LK Campanha CRM Aprovada` no caminho `areas/lk/sub-areas/crm/rotinas/playbook-campanha-crm-aprovada.md`.
- Owner operacional: LK Atendimento / CRM / Operações, com governança Hermes Geral e aprovação final Lucas.

### Escopo permitido
- Escopo permitido somente após aprovação explícita: executar apenas os itens, IDs, fluxos, mensagens, campos, coleções, arquivos ou rotinas descritos neste packet, sem ampliar alvo por inferência.
- Pode fazer localmente sem nova aprovação: validação documental, preview, auditoria read-only, receipt e classificação de blockers.

### O que continua bloqueado
- Não pode fazer mensagem a cliente, WhatsApp/e-mail, campanha, Chatwoot/webhook/runtime, contato externo, preço, disponibilidade, reserva, negociação, reembolso ou logística sem aprovação específica.
- Aprovação genérica como `seguir`, `fazer tudo` ou contexto antigo não amplia escopo; novo alvo exige novo approval packet.

### Risco
- Risco principal: transformar preview/packet em autorização ampla e executar ação sensível fora do escopo exato.
- Mitigação: fail-closed, approval textual específica, backup/snapshot quando aplicável, readback e receipt com contagens.

### Rollback
- Rollback obrigatório: reverter somente a alteração aprovada usando backup/snapshot/artefato anterior quando aplicável; se a ação foi apenas preview/read-only, rollback é manter sem execução e registrar o bloqueio.
- Qualquer rollback que toque sistema externo exige o mesmo escopo aprovado, readback e receipt.

### Verificação / readback
- Verificação obrigatória: readback do artefato/preview, ledger/receipt local, amostragem de contatos/conversas quando aplicável e confirmação de zero envio externo não aprovado.
- Se houver divergência de identidade, fonte, escopo ou aprovação, bloquear execução e registrar causa sanitizada.

### Opções de aprovação
- Aprovar exatamente o escopo descrito neste packet.
- Aprovar apenas preview/dry-run/read-only.
- Ajustar alvo/limite antes de executar.
- Bloquear execução e manter como histórico/rascunho.

### Secret hygiene
- Usar credenciais somente via Doppler/wrapper seguro quando houver integração; não imprimir tokens, refresh tokens, passwords, service-account JSON, API keys ou connection strings.
- Relatórios e receipts devem manter `values_printed=false` e redigir qualquer valor sensível como `[REDACTED]`.
