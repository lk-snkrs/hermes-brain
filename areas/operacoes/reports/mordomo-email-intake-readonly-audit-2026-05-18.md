# Auditoria read-only — Mordomo Email Intake

Gerado em: 2026-05-18T17:26:54.162258+00:00

Escopo: leitura read-only via Gmail API; sem envio, sem draft, sem marcação, sem labels, sem mutações. Conteúdo mascarado.

## Resumo por conta

- `lucascimino@gmail.com`: 10 mensagens recentes; classes: FYI=4, lead_comercial=1, marketing_social_fyi=1, marketing_spend_financeiro=1, newsletter_ruido=3
- `lucas@zippergaleria.com.br`: 10 mensagens recentes; classes: FYI=5, lead_comercial=3, marketing_social_fyi=1, pos_venda_cliente=1
- `producao@zippergaleria.com.br`: 10 mensagens recentes; classes: FYI=1, financeiro_admin=2, lead_comercial=3, marketing_social_fyi=1, operacional_logistica=2, pos_venda_cliente=1
- `lk@lksneakers.com.br`: 10 mensagens recentes; classes: FYI=3, financeiro_admin=1, lead_comercial=2, marketing_social_fyi=1, marketing_spend_financeiro=1, newsletter_ruido=1, operacional_logistica=1
- `spiti@spiti.auction`: 10 mensagens recentes; classes: FYI=8, financeiro_admin=1, newsletter_ruido=1

## Amostra classificada

### lucascimino@gmail.com
1. **newsletter_ruido** / Lucas/global / urgência: normal
   - De: Pacsun <h***o@mkt.pacsun.com>
   - Assunto: Not your average hoodies & sweatpants 👉
   - Sinal: conta pessoal/global, newsletter/marketing
   - Saída sugerida: digest/ignorar; aprovação externa: não
2. **FYI** / Lucas/global / urgência: normal
   - De: Kith Women <n***r@kith.com>
   - Assunto: Kith Women | Summer Escape
   - Sinal: conta pessoal/global
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
3. **newsletter_ruido** / Lucas/global / urgência: normal
   - De: Serasa Experian <c***o@comunicacao.serasaexperian.com.br>
   - Assunto: Seu Score detalhado através do nosso chatbot
   - Sinal: conta pessoal/global, newsletter/marketing
   - Saída sugerida: digest/ignorar; aprovação externa: não
4. **FYI** / Lucas/global / urgência: normal
   - De: "Sabrina Ramonov 🍄" <s***v@substack.com>
   - Assunto: How to Win With AI in 2026
   - Sinal: conta pessoal/global
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
5. **marketing_social_fyi** / Zipper OS / urgência: normal
   - De: TikTok <n***n@service.tiktok.com>
   - Assunto: Zipper Galeria publicou: Em montagem → “Mega Hair”, individual de Romy...
   - Sinal: social automático
   - Saída sugerida: FYI/digest de social; aprovação externa: não
6. **marketing_spend_financeiro** / Zipper OS / urgência: normal
   - De: Meta for Business <n***y@business-updates.facebook.com>
   - Assunto: Seu recibo de anúncios de Meta (identificação da conta: [telefone])
   - Sinal: recibo/anúncios, sinal Zipper/arte/logística
   - Saída sugerida: pendência financeira/marketing spend; aprovação externa: sim
7. **lead_comercial** / Lucas/global / urgência: normal
   - De: Porto Seguro <c***o@novidades.portoseguro.com.br>
   - Assunto: Conserto gratuito para eletrodomésticos: saiba mais!
   - Sinal: conta pessoal/global, lead/proposta
   - Saída sugerida: Decision Packet ou draft/pendência interna; aprovação externa: sim
8. **FYI** / LK OS / urgência: normal
   - De: Booma Organic <n***y@loox.io>
   - Assunto: Lembrete: como foi o pedido #70568?
   - Sinal: sinal LK/ecommerce
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
9. **FYI** / Lucas/global / urgência: normal
   - De: Bahia Asset <b***t@bahiaasset.com.br>
   - Assunto: Fundos Bahia Asset
   - Sinal: conta pessoal/global
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
10. **newsletter_ruido** / Lucas/global / urgência: normal
   - De: SuperRare <s***s@substack.com>
   - Assunto: Defaced: A Series of Headaches
   - Sinal: conta pessoal/global, newsletter/marketing
   - Saída sugerida: digest/ignorar; aprovação externa: não

### lucas@zippergaleria.com.br
1. **lead_comercial** / Zipper OS / urgência: normal
   - De: Tidio <n***y@tidio.net>
   - Assunto: Tidio [4 novas mensagens] c***o@wlseguros.com.br (c***o@wlseguros.com.br)
   - Sinal: Tidio/site, possível lead
   - Saída sugerida: Decision Packet ou draft/pendência interna; aprovação externa: sim
2. **pos_venda_cliente** / Zipper OS / urgência: normal
   - De: "Helô Goes" <h***o@zippergaleria.com.br>
   - Assunto: Cliente Whatsapp — Obra Daniel Mullen com mofo
   - Sinal: sinal Zipper/arte/logística, pós-venda/problema
   - Saída sugerida: Decision Packet; possível urgência comercial; aprovação externa: sim
3. **FYI** / Zipper OS / urgência: normal
   - De: Camomila Steiner <c***a@jacarandamontagens.com.br>
   - Assunto: acerto do dia 20/04 ao dia 18/05
   - Sinal: sinal Zipper/arte/logística
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
4. **FYI** / Zipper OS / urgência: normal
   - De: "Sabrina Ramonov 🍄" <s***v@substack.com>
   - Assunto: How to Win With AI in 2026
   - Sinal: sinal Zipper/arte/logística
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
5. **FYI** / SPITI OS / urgência: normal
   - De: Soraia Cals <c***o@soraiacals.com.br>
   - Assunto: LEILÃO MAIO 2026
   - Sinal: sinal Zipper/arte/logística, sinal SPITI/leilão
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
6. **lead_comercial** / Zipper OS / urgência: normal
   - De: l***s@zippergaleria.com.br
   - Assunto: Obras disponíveis — Adriana Duque
   - Sinal: sinal Zipper/arte/logística, lead/proposta
   - Saída sugerida: Decision Packet ou draft/pendência interna; aprovação externa: sim
7. **FYI** / Zipper OS / urgência: normal
   - De: "Luis. A. via Artsy" <l***b@reply.artsy.net>
   - Assunto: New Inquiry from Luis. A. on “Proximity VII: pink-tourqoise shift” (2025) by Daniel Mullen
   - Sinal: sinal Zipper/arte/logística
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
8. **FYI** / Zipper OS / urgência: normal
   - De: Amelie Ducommun <a***e@gmail.com>
   - Assunto: Re: Following up SP-Arte'
   - Sinal: sinal Zipper/arte/logística
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
9. **lead_comercial** / Zipper OS / urgência: normal
   - De: "Helô Goes" <h***o@zippergaleria.com.br>
   - Assunto: Arquiteta Whatsapp — Flávia Junqueira
   - Sinal: sinal Zipper/arte/logística, lead/proposta
   - Saída sugerida: Decision Packet ou draft/pendência interna; aprovação externa: sim
10. **marketing_social_fyi** / Zipper OS / urgência: normal
   - De: Lucas Cimino <l***s@zippergaleria.com.br>
   - Assunto: Re: Compromisso — 20 de Julho
   - Sinal: social automático
   - Saída sugerida: FYI/digest de social; aprovação externa: não

### producao@zippergaleria.com.br
1. **pos_venda_cliente** / Zipper OS / urgência: normal
   - De: "Helô Goes" <h***o@zippergaleria.com.br>
   - Assunto: Cliente Whatsapp — Obra Daniel Mullen com mofo
   - Sinal: sinal Zipper/arte/logística, pós-venda/problema
   - Saída sugerida: Decision Packet; possível urgência comercial; aprovação externa: sim
2. **lead_comercial** / LK OS / urgência: normal
   - De: Camomila Steiner <c***a@jacarandamontagens.com.br>
   - Assunto: Re: APROVADO PARA PRODUCAO PEDIDO Nº 27569
   - Sinal: sinal Zipper/arte/logística, sinal LK/ecommerce, lead/proposta
   - Saída sugerida: Decision Packet ou draft/pendência interna; aprovação externa: sim
3. **FYI** / Zipper OS / urgência: normal
   - De: "s***s@terra.com.br" <s***s@terra.com.br>
   - Assunto: Re: Cotação PED 27568 - Chapada dos Guimarães/MT
   - Sinal: sinal Zipper/arte/logística
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
4. **lead_comercial** / Zipper OS / urgência: normal
   - De: p***o@zippergaleria.com.br
   - Assunto: Re: Cotação PED 27568 - Chapada dos Guimarães/MT
   - Sinal: sinal Zipper/arte/logística, lead/proposta
   - Saída sugerida: Decision Packet ou draft/pendência interna; aprovação externa: sim
5. **operacional_logistica** / LK OS / urgência: normal
   - De: "Produção Zipper" <p***o@zippergaleria.com.br>
   - Assunto: NOVO PEDIDO: RETIRADA DO DEPÓSITO - PEDIDO 27574
   - Sinal: sinal Zipper/arte/logística, sinal LK/ecommerce, logística/agenda
   - Saída sugerida: tarefa/calendário se dados completos e regra permitir; aprovação externa: não
6. **operacional_logistica** / Zipper OS / urgência: normal
   - De: "s***s@terra.com.br" <s***s@terra.com.br>
   - Assunto: Re: Cotação PED 27568 - Chapada dos Guimarães/MT
   - Sinal: sinal Zipper/arte/logística, logística/agenda
   - Saída sugerida: tarefa/calendário se dados completos e regra permitir; aprovação externa: não
7. **lead_comercial** / LK OS / urgência: normal
   - De: Livia Janes <l***s@grupoalke.com>
   - Assunto: Ferias - Vacation Re: PEDIDO DE ORÇAMENTO Nº 27530
   - Sinal: sinal Zipper/arte/logística, sinal LK/ecommerce, lead/proposta
   - Saída sugerida: Decision Packet ou draft/pendência interna; aprovação externa: sim
8. **marketing_social_fyi** / Zipper OS / urgência: normal
   - De: p***o@zippergaleria.com.br
   - Assunto: Re: PEDIDO DE ORÇAMENTO Nº 27530
   - Sinal: social automático
   - Saída sugerida: FYI/digest de social; aprovação externa: não
9. **financeiro_admin** / LK OS / urgência: normal
   - De: p***o@zippergaleria.com.br
   - Assunto: Pagamento referente à coleta de obras Willian Santos
   - Sinal: sinal Zipper/arte/logística, sinal LK/ecommerce, financeiro
   - Saída sugerida: Decision Packet ou pendência financeira; aprovação externa: sim
10. **financeiro_admin** / LK OS / urgência: normal
   - De: p***o@zippergaleria.com.br
   - Assunto: Pagamento para início do restauro Obras Teresa Viana
   - Sinal: sinal Zipper/arte/logística, sinal LK/ecommerce, financeiro
   - Saída sugerida: Decision Packet ou pendência financeira; aprovação externa: sim

### lk@lksneakers.com.br
1. **newsletter_ruido** / LK OS / urgência: normal
   - De: Rafa Coelho - LK Sneakers <m***s@lksneakers.on.crisp.email>
   - Assunto: Re: Boa tarde Larissa (#10a)
   - Sinal: sinal LK/ecommerce, newsletter/marketing
   - Saída sugerida: digest/ignorar; aprovação externa: não
2. **lead_comercial** / Zipper OS / urgência: normal
   - De: Zapier Alerts <a***s@mail.zapier.com>
   - Assunto: [ALERT] Possible error on your Tidio → Webhook: ZPRALL Zap
   - Sinal: Tidio/site, possível lead
   - Saída sugerida: Decision Packet ou draft/pendência interna; aprovação externa: sim
3. **lead_comercial** / Zipper OS / urgência: normal
   - De: Zapier Alerts <a***s@mail.zapier.com>
   - Assunto: [ALERT] Possible error on your Tidio → Webhook: ZPRALL Zap
   - Sinal: Tidio/site, possível lead
   - Saída sugerida: Decision Packet ou draft/pendência interna; aprovação externa: sim
4. **financeiro_admin** / LK OS / urgência: normal
   - De: Financeiro MFashion <f***n@matacompany.com>
   - Assunto: RE: Consignação Mata Lab | Vendas - LK SNEAKERS - Dez/25
   - Sinal: sinal LK/ecommerce, financeiro
   - Saída sugerida: Decision Packet ou pendência financeira; aprovação externa: sim
5. **FYI** / LK OS / urgência: normal
   - De: Meta for Business <n***n@facebookmail.com>
   - Assunto: Inclua automaticamente informações mais detalhadas sobre páginas e produtos usando o Pixel da Meta
   - Sinal: sinal LK/ecommerce
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
6. **marketing_social_fyi** / LK OS / urgência: normal
   - De: "CC Strategic AI (Skool)" <n***y@skool.com>
   - Assunto: 1 new notification since 1:54 pm (May 17, 2026)
   - Sinal: social automático, sinal LK/ecommerce
   - Saída sugerida: FYI/digest de social; aprovação externa: não
7. **FYI** / LK OS / urgência: normal
   - De: Crisp <s***t@crisp.chat>
   - Assunto: Confirm your Crisp account email
   - Sinal: sinal LK/ecommerce
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
8. **FYI** / LK OS / urgência: normal
   - De: rhode <h***o@rhodeskin.com>
   - Assunto: Spot motion
   - Sinal: sinal LK/ecommerce
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
9. **operacional_logistica** / LK OS / urgência: normal
   - De: Cintia Schaeffer - LK Sneakers <m***s@lksneakers.on.crisp.email>
   - Assunto: Re: Olá! Alguma notícia sobre a entrega da minha compra? (#b7e)
   - Sinal: sinal Zipper/arte/logística, sinal LK/ecommerce, logística/agenda
   - Saída sugerida: tarefa/calendário se dados completos e regra permitir; aprovação externa: não
10. **marketing_spend_financeiro** / LK OS / urgência: normal
   - De: Meta for Business <n***y@business-updates.facebook.com>
   - Assunto: Seu recibo de anúncios de Meta (identificação da conta: [telefone])
   - Sinal: recibo/anúncios, sinal Zipper/arte/logística, sinal LK/ecommerce
   - Saída sugerida: pendência financeira/marketing spend; aprovação externa: sim

### spiti@spiti.auction
1. **financeiro_admin** / SPITI OS / urgência: normal
   - De: Spiti Auction <s***i@spiti.auction>
   - Assunto: Re: Spiti - Leilão | Nota fiscal
   - Sinal: sinal SPITI/leilão, financeiro
   - Saída sugerida: Decision Packet ou pendência financeira; aprovação externa: sim
2. **FYI** / SPITI OS / urgência: normal
   - De: Google Ads <a***y@google.com>
   - Assunto: Continue no caminho certo para otimizar sua campanha
   - Sinal: sinal SPITI/leilão
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
3. **newsletter_ruido** / SPITI OS / urgência: normal
   - De: "Filipe da Zenvia 💜" <n***y@zenvia.com>
   - Assunto: O fim do número de telefone no WhatsApp? Entenda a mudança para 2026.
   - Sinal: sinal SPITI/leilão, newsletter/marketing
   - Saída sugerida: digest/ignorar; aprovação externa: não
4. **FYI** / SPITI OS / urgência: normal
   - De: GitHub <n***y@github.com>
   - Assunto: [GitHub] Sudo email verification code
   - Sinal: sinal SPITI/leilão
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
5. **FYI** / SPITI OS / urgência: normal
   - De: GitHub <n***y@github.com>
   - Assunto: [GitHub] Sudo email verification code
   - Sinal: sinal SPITI/leilão
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
6. **FYI** / SPITI OS / urgência: normal
   - De: GitHub <n***y@github.com>
   - Assunto: [GitHub] Hostinger is requesting updated permissions
   - Sinal: sinal SPITI/leilão
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
7. **FYI** / SPITI OS / urgência: normal
   - De: Spiti Auction <s***i@spiti.auction>
   - Assunto: Re: Comprovante - Renato Tescari
   - Sinal: sinal SPITI/leilão
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
8. **FYI** / SPITI OS / urgência: normal
   - De: Supabase <w***e@supabase.com>
   - Assunto: Supa Update May 2026
   - Sinal: sinal SPITI/leilão
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
9. **FYI** / SPITI OS / urgência: normal
   - De: Renato Tescari <r***c@gmail.com>
   - Assunto: Re: Comprovante - Renato Tescari
   - Sinal: sinal SPITI/leilão
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não
10. **FYI** / SPITI OS / urgência: normal
   - De: Google Play <g***y@google.com>
   - Assunto: Your Google Play Order Cancellation Receipt from May 5, 2026
   - Sinal: sinal SPITI/leilão
   - Saída sugerida: FYI ou classificar melhor; aprovação externa: não

## Observações de calibração

- Esta é uma primeira triagem heurística, não automação final.
- Próximo passo: Lucas corrigir falsos positivos/falsos negativos em uma amostra real; depois atualizamos a KB e o classificador.
- Nenhuma ação externa foi executada.