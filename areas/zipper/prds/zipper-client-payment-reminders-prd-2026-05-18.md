# PRD — Zipper: lembretes de parcelas de clientes a partir de venda/documentos

Atualizado: 2026-05-18
Status: v0.1 — conceito aprovado por Lucas; implementação futura por fonte estruturada/PDF

## 1. Correção de escopo

Lucas corrigiu que o Mordomo não deve se preocupar por padrão com financeiro interno geral da Zipper: pagamentos, fechamentos mensais, repasses de artista, boletos, notas e comprovantes são assuntos de Lucas/Cibele.

Há uma exceção útil: **pagamentos/parcelas de clientes ligados a uma venda específica**. Isso não é “financeiro interno”; é CRM operacional da venda.

## 2. Objetivo

Quando uma venda tiver condições parceladas ou datas de pagamento, o Mordomo deve transformar essas datas em lembretes estruturados para acompanhamento.

Exemplo:

- Cliente X comprou obra Y.
- Pedido/venda tem parcelas 1/2/3/4.
- Cada parcela vence em datas específicas.
- O Mordomo deve lembrar antes/no dia, indicar quem deve cobrar/acompanhar e manter o status.

## 3. Fontes possíveis

- PDF/documento de nova venda.
- E-mail com anexo de venda/proposta aprovada.
- Sistema/CRM/Supabase de vendas, quando existir fonte estruturada.
- Planilha/relatório de venda.
- Automação futura criada por Lucas ou equipe: cliente + pedido + parcelas + vencimentos.

## 4. Dados mínimos

Cada lembrete deve conter:

- cliente;
- contato do cliente;
- obra/artista;
- pedido/venda;
- número da parcela;
- valor;
- vencimento;
- status: pendente / pago / atrasado / cancelado / confirmado por outro canal;
- dono interno: Lucas / Cibele / financeiro / produção;
- canal recomendado: e-mail / WhatsApp / interno;
- observação de origem: PDF, e-mail, sistema, planilha.

## 5. Regra de ação

### Autônomo / interno

O Mordomo pode sozinho:

- extrair datas de pagamento de documentos autorizados;
- criar lembretes;
- avisar Lucas/Cibele internamente;
- preparar texto de cobrança/lembrança;
- atualizar status local quando houver evidência clara.

### Externo / cliente

Mensagem externa ao cliente exige regra aprovada ou aprovação corrente.

Subfluxo futuro possível:

- lembrete cordial de parcela antes do vencimento;
- confirmação de recebimento;
- aviso interno de atraso.

Antes de ativar envio externo automático, precisa haver:

- texto aprovado;
- fonte de verdade da parcela;
- confirmação de que o pagamento não foi realizado;
- logs;
- kill switch.

## 6. Não confundir com financeiro interno

Não alertar Lucas por padrão sobre:

- repasse mensal de artista;
- comprovante de pagamento interno;
- fechamento geral de mês;
- cobrança administrativa sem relação direta com acompanhamento de cliente/venda.

Esses só entram se Lucas pedir ou se houver risco crítico explícito.

## 7. Próximo passo técnico

Criar parser/ingest para “nova venda”:

1. receber PDF/documento;
2. extrair cliente, obra, artista, valor e parcelas;
3. validar extração com confidence score;
4. criar registros em fila local/CRM;
5. criar lembretes por vencimento;
6. gerar alerta útil no dia correto.

## 8. Critério de pronto

- Um PDF/documento de venda de teste gera lista correta de parcelas.
- Lembretes aparecem na fila global do Mordomo.
- Lembrete não dispara se status estiver pago/cancelado.
- Nenhuma mensagem externa é enviada sem regra aprovada.
