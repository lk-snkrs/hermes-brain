# LK Ops/Atendimento — Contrato Operacional

Data: 2026-05-26  
Status: categoria operacional/documental ativa; runtime dedicado ainda não aprovado  
Owner lógico: LK Ops/Atendimento  
Supervisor: Hermes Geral / COO  
Runtimes atuais: Main Hermes e Mordomo conforme cron/entrada existente; LK Growth não deve virar dono por conveniência  
Writes externos: bloqueados sem aprovação explícita + snapshot/readback/receipt/rollback

## Princípio

LK Ops/Atendimento cobre atendimento, WhatsApp, loja, vendas operacionais, estoque, preço, disponibilidade, reservas, Tiny/Shopify operacional e relatórios comerciais.

LK Growth continua dono de SEO/GEO/CRO/GMC/conteúdo/analytics. Growth pode analisar impacto comercial, mas não deve assumir atendimento, estoque, preço ou operação de loja por conveniência.

## Fonte de verdade

### Estoque

- Tiny é a fonte de verdade do estoque.
- Shopify não é controle de estoque.
- Shopify serve como gatilho/evento e superfície de publicação.
- Qualquer sync deve seguir: evento Shopify → identificar item/variante/tamanho exato → buscar saldo real no Tiny → preparar/atualizar Shopify com esse saldo.
- Nunca calcular por delta local como `estoque Shopify - quantidade vendida` ou `estoque Shopify + quantidade cancelada`.

### Pedido/venda/cliente

- Fonte viva antes de afirmação: Shopify/Tiny/CRM/WhatsApp/fonte oficial aplicável.
- Memória e Brain ajudam a rotear, mas não substituem consulta viva para disponibilidade, status, preço, pedido ou prazo.

### Atendimento

- Respostas externas sensíveis exigem fonte e/ou aprovação.
- Rascunho interno é permitido.
- Follow-up simples conhecido/verificado segue exceção aprovada; preço/disponibilidade/reserva/negociação/reclamação/fornecedor/bulk continuam bloqueados.

## Permitido sem nova aprovação

- Leitura read-only de fontes autorizadas.
- Diagnóstico local.
- Resolução local de variantes/SKU/tamanho.
- Rascunho interno de resposta.
- Relatório comercial read-only.
- Alertar Lucas sobre exceção/risco.
- Preparar approval packet.
- Dry-run local com ledger quando já aprovado no escopo e sem writes externos.

## Exige aprovação explícita

- Prometer preço, disponibilidade, reserva, prazo, troca, desconto ou negociação.
- Enviar mensagem externa sensível para cliente/fornecedor/parceiro.
- Alterar Shopify, Tiny, CRM, WhatsApp automation, n8n, Klaviyo ou qualquer sistema externo.
- Criar/alterar cron, runtime, gateway, profile, bot ou delivery.
- Ativar sync produtivo de estoque.
- Qualquer write externo sem snapshot/readback/receipt/rollback.

## Contrato de write LK

Quando um write externo for aprovado, exigir:

1. **Snapshot** antes da alteração.
2. **Preview** do que será alterado.
3. **Execução escopada** só no item/rota aprovada.
4. **Readback** na fonte viva após alteração.
5. **Receipt** no Brain com evidência e horário.
6. **Rollback** documentado/testável quando aplicável.

## Rotinas atualmente relacionadas

### Main Hermes

- `LK Daily Sales Brief read-only mandatory delivery`
- `LK Weekly CEO Review read-only mandatory delivery`
- `LK Pulso Comercial 16h read-only delivery`
- `LK 09h previous-day sales report external delivery`
- `LK 19h30 physical store close external delivery`

Interpretação: Main pode hospedar enquanto LK Ops não tiver runtime próprio, mas o dono lógico deve ser LK Ops/Comercial.

### Mordomo

- `LK WhatsApp Hermes responder watchdog`
- `LK WhatsApp Hermes responder regression watchdog`

Interpretação: podem permanecer temporariamente por conexão com intake/WhatsApp, mas devem ter handoff para LK Ops/Hermes Central e não se misturar com rotinas pessoais sem rótulo.

## Critério para runtime LK Ops futuro

Só considerar profile/bot próprio se 2+ condições persistirem por pelo menos 2 semanas:

- Mais de 5 interações operacionais LK por semana exigindo contexto próprio.
- WhatsApp/atendimento LK competindo com Mordomo pessoal.
- Necessidade de separar logs/receipts de estoque, pedidos, loja e atendimento.
- Rotinas LK Ops exigindo cadência própria além de relatórios atuais.
- Equipe LK precisando de canal/bot dedicado.
- Alto risco de confusão entre Growth e Operações.

Antes de criar runtime:

1. Definir humano aprovador.
2. Definir fontes autorizadas.
3. Listar crons a migrar/manter.
4. Fazer backup dos registries.
5. Preparar rollback.
6. Desabilitar API/webhook por padrão se não forem necessários.
7. Criar watchdog silent-OK.
8. Testar boot read-only.

## Handoff obrigatório

Registrar quando houver:

- resposta material a cliente ou equipe;
- divergência Tiny/Shopify/CRM;
- estoque/preço/disponibilidade consultados;
- sync/dry-run/ledger;
- bloqueio por aprovação;
- relatório comercial entregue;
- mudança de rotina/guardrail.

Template curto:

```md
## HH:MM — LK Ops/Atendimento — [tema]

- Pedido:
- Fonte viva consultada:
- Resultado:
- Output/rascunho:
- Writes externos: não/sim + aprovação
- Risco/bloqueio:
- Próximo passo:
- Onde ficou documentado:
```

## Veredito atual

LK Ops/Atendimento deve virar categoria explícita no organograma e nos crons, mas ainda não precisa de runtime próprio antes de saneamento do Mordomo, classificação dos crons e prova de volume/risco.
