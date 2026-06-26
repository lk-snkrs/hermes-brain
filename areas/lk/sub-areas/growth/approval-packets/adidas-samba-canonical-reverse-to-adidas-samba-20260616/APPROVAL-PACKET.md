# Approval Packet — Corrigir Canonical Adidas Samba para /collections/adidas-samba

Gerado: 2026-06-16T20:26:17.452308+00:00

## Decisão corrigida
Lucas definiu que a URL principal correta deve ser:

`https://lksneakers.com.br/collections/adidas-samba`

Motivo: melhor alinhamento SEO por conter marca + modelo no handle.

## Estado atual após etapa anterior
- `/collections/adidas-samba`: continua ativa, otimizada, HTTP 200 e canonical próprio.
- `/collections/samba`: também recebeu o conteúdo otimizado e está ativa.
- Foi criado no Admin um redirect `/collections/adidas-samba` → `/collections/samba`, mas ele NÃO está efetivo publicamente porque `/collections/adidas-samba` segue como rota ativa.

## Correção necessária
1. Remover o redirect criado anteriormente: `/collections/adidas-samba` → `/collections/samba`.
2. Manter `/collections/adidas-samba` como coleção principal ativa e otimizada.
3. Resolver `/collections/samba` como duplicata. Como redirects Shopify não sobrepõem rota ativa, para `/collections/samba` redirecionar de verdade para `/collections/adidas-samba`, provavelmente será necessário liberar a rota `/collections/samba` alterando o handle da coleção duplicada ou arquivando/despublicando a duplicata.
4. Criar redirect 301: `/collections/samba` → `/collections/adidas-samba`.
5. QA público: `/collections/adidas-samba` HTTP 200 canonical próprio; `/collections/samba` 301 para `/collections/adidas-samba`.

## Risco
- Médio: envolve handle/rota de coleção que hoje está linkada pela homepage/menu.
- Benefício: se `/samba` virar 301, os links internos atuais passam autoridade para `/adidas-samba`.
- Não mexe em produtos, preço, estoque, feed, campanhas ou theme.

## Rollback
- Restaurar handles e SEO/description pelo backup.
- Recriar/remover redirects conforme estado anterior.

## Aprovação necessária
Para executar a correção completa, preciso da frase explícita:

`Aprovo corrigir a canonical do Adidas Samba para /collections/adidas-samba: remover o redirect anterior, liberar a rota /collections/samba se necessário alterando o handle da duplicata, criar 301 de /collections/samba para /collections/adidas-samba, com backup, QA e rollback.`

## Alternativa sem mexer na rota /samba agora
Se quiser só desfazer o erro sem tocar na duplicata:

`Aprovo apenas remover o redirect anterior /collections/adidas-samba -> /collections/samba e manter /collections/adidas-samba como principal, sem mexer na /collections/samba ainda.`
