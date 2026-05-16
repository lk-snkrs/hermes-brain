# Crítica COO — LK OS WhatsApp Sales Report

Data: 2026-05-16
Escopo: leitura operacional do formato atual de mensagem para grupo WhatsApp LK Vendas, sem PII de clientes.

## Diagnóstico rápido

O report atual é seguro e já tem boa base: não expõe cliente, separa online/loja, mostra receita/pedidos/TM, mix, produtos líderes, vendedores por tag `Vendedor: Nome` e fecha com prioridade. Para o grupo de vendas, porém, ainda parece mais “relatório de BI colado no WhatsApp” do que “comando operacional do dia”.

## Principais problemas operacionais

1. Excesso de blocos para a tomada de decisão rápida
   - Ontem, hoje e loja aparecem em sequência com métricas parecidas.
   - No celular, o vendedor precisa garimpar o que fazer agora.

2. Falta uma leitura de ritmo/meta
   - “R$ abaixo de ontem” ajuda, mas não diz se está bom/ruim para o horário, nem qual esforço falta.
   - O grupo precisa de uma chamada tipo: “foco até fechamento: +R$ X / Y vendas”.

3. Mix sem conversão em ação
   - “New Balance (7), Onitsuka (5)” é útil, mas deveria virar recomendação: empurrar reposição, vitrine, stories, abordagem no balcão ou atenção a grade/tamanho.

4. Ranking de vendedores pode gerar ruído se não vier com contexto
   - Receita por vendedor é útil, mas precisa evitar clima punitivo.
   - Melhor mostrar “destaques da loja” e “oportunidade do time”, com pedido médio/quantidade quando possível.

5. Produtos líderes estão muito detalhados para WhatsApp
   - Nome completo + cor + tamanho + qtd ocupa linhas e pode esconder o insight.
   - Melhor agrupar como “produto/modelo que está puxando” e “tamanhos saindo”.

6. Alerta de cadastro aparece, mas sem dono/prazo
   - “corrigir SKU” é correto, mas para operação precisa de dono: cadastro/estoque/retaguarda, e prazo: hoje antes do fechamento ou até amanhã 10h.

7. Falta seção explícita de próximas ações
   - A conclusão tem prioridade, mas deveria haver um bloco “Ações para agora” com 2–4 bullets, em linguagem de execução.

## Estrutura recomendada para mensagem diária no LK Vendas

Objetivo: mensagem curta, acionável, legível em 30 segundos e segura para grupo comercial.

```text
🟡 *LK Vendas · Pulso diário*
_16/05 · 18:23 BRT · Shopify read-only · sem dados de cliente_

*1) Placar do dia*
• Hoje: R$ 33.698,98 · 14 vendas · TM R$ 2.407
• Vs ontem: -R$ 10.865,87
• Canal: Loja 52% · Online 48%

*2) Leitura COO*
• Loja está puxando o dia; online ainda equilibrado.
• Ticket médio caiu vs ontem — oportunidade é elevar composição/add-on.
• Mix quente: New Balance e Onitsuka.

*3) Ações até o fechamento*
• Loja: priorizar abordagem em New Balance/Onitsuka e tentar 1 item complementar por atendimento.
• Online/WhatsApp: reforçar modelos mais pedidos nos atendimentos e recuperar leads quentes do dia.
• Cadastro: corrigir 2 itens sem SKU para não perder leitura de estoque/mix.

*4) Loja física — destaque do time*
• R$ 17.369,92 · 8 vendas · TM R$ 2.171
• Vendedores: Danilo R$ 8.499,96 · Biel R$ 6.469,97 · Wesley R$ 2.399,99
• Produto puxando: NB 204L Arid Timberwolf · tam. 35

*5) Mix que merece atenção*
• New Balance: 7 unidades
• Onitsuka: 5 unidades
• Verificar grade/tamanhos dos modelos que saíram hoje.

*Próximo check:* fechamento loja 19h30.
```

## Regras de conteúdo

- Não incluir nome, telefone, endereço, e-mail, pedido com identificação de cliente ou print de Shopify.
- Não expor IDs internos de POS/staff; usar somente tag humana `Vendedor: Nome` quando validada.
- Evitar linguagem técnica crua: trocar “AOV” por “TM”, “source_name” por “canal”.
- Não transformar ranking em cobrança individual; usar tom de time, foco e oportunidade.
- Sempre terminar com próxima ação e próximo horário de check.

## Versão mais curta para rotina diária

```text
🟡 *LK Vendas · Pulso diário* — 16/05 18:23

*Placar:* R$ 33.698,98 · 14 vendas · TM R$ 2.407
*Vs ontem:* -R$ 10.865,87 · Loja 52% / Online 48%

*Leitura:* loja está puxando; TM abaixo de ontem; mix quente em New Balance e Onitsuka.

*Ações agora:*
• Loja: focar NB/Onitsuka + composição por atendimento.
• Online/WhatsApp: recuperar leads quentes e reforçar modelos pedidos.
• Retaguarda: corrigir 2 SKUs sem cadastro.

*Loja:* R$ 17.369,92 · 8 vendas · vendedores: Danilo, Biel, Wesley.
_Próximo check: fechamento 19h30 · sem dados de cliente._
```

## Recomendação final

Manter o report completo como artefato interno/JSON/HTML, mas mandar no WhatsApp uma versão “comando do dia”: placar, leitura, ações, loja/time e próximo check. O grupo LK Vendas precisa sair da mensagem sabendo o que vender, onde focar e qual pendência operacional resolver — não apenas ver números.
