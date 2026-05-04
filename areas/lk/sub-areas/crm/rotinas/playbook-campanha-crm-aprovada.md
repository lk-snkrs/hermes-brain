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
