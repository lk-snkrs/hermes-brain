# Template — Decisão Customer-facing Aprovada

Use este template quando Lucas aprovar ou corrigir copy, tom, sequência, fluxo, canal, segmento, oferta, cadência ou guardrail de qualquer comunicação com cliente, lead, comprador, colecionador, bidder, fornecedor ou público externo.

Regra Bruno/OpenClaw adaptada para Hermes: o agente não é o cérebro; o agente registra no Brain. Aprovação em chat não é suficiente depois de compactação de contexto.

## Metadados

Data: YYYY-MM-DD  
Empresa/área: LK / Zipper / SPITI / Multiempresa  
Sub-área: CRM / atendimento / vendas / leilão / comunicação / sourcing / outra  
Canal: WhatsApp / email / Klaviyo / Crisp / Meta template / Telegram interno / outro  
Status: draft / approved_copy / approved_flow / needs_current_send_approval / executed_verified / superseded  
Fonte da aprovação: conversa Lucas / reunião / PRD / teste interno / outro  
Responsável humano: Lucas / equipe / a confirmar

## Contexto

- Situação que gerou a decisão:
- Segmento/público:
- Produto/obra/lote/campanha, se aplicável:
- Artefato anterior substituído, se houver:

## Payload aprovado

### Copy / mensagem

```text
[Texto exato aprovado]
```

### Botões / CTAs

```text
[Texto exato dos botões/CTAs]
```

### Variáveis

- `{{1}}`:
- `{{2}}`:
- `{{3}}`:

### Mídia / visual

- Header/imagem/arquivo:
- Regra de uso:
- Fallback se a mídia falhar:

## Tom aprovado

- Voz:
- O que reforçar:
- O que evitar:

## Fluxo aprovado

- T0 / gatilho:
- T1:
- T2:
- T3:
- Condições de supressão:
- Frequência máxima:

## Guardrails

- Não prometer:
- Não mencionar:
- Não enviar se:
- Precisa verificar antes:
- Continua exigindo aprovação atual de Lucas:

## Próxima ação permitida

Escolher uma:

- [ ] Registrar decisão apenas.
- [ ] Preparar preview/draft interno.
- [ ] Criar/editar template em ambiente seguro.
- [ ] Fazer teste interno para número/e-mail aprovado.
- [ ] Executar envio externo apenas se Lucas aprovar destinatário + payload nesta etapa.

## Artefatos atualizados

- `...`

## Verificação

- [ ] Decisão registrada na área correta.
- [ ] MAPA da área aponta para esta decisão ou pasta `decisions/`.
- [ ] Playbook/skill conflitante foi atualizado ou marcado como superseded.
- [ ] Nenhum secret/dado sensível foi salvo.
- [ ] Nenhum envio externo foi feito sem aprovação atual.

## Histórico / supersede

- Substitui:
- Substituído por:
- Motivo:
