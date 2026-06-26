# Regra operacional — Shopify theme Dev → Production

Data: 2026-05-31
Área: LK Sneakers / Growth / Shopify Theme

## Regra canônica

Quando Lucas disser “subir para produção”, “subir production”, “aprovado produção”, “merge na production” ou equivalente em trabalho de tema Shopify, isso significa obrigatoriamente:

1. A alteração deve existir e estar validada no tema Dev.
2. Production deve receber a promoção/merge do diff aprovado do Dev.
3. Não se deve fazer patch independente direto em Production, porque isso quebra a sequência/histórico entre Dev e Production.
4. A promoção deve preservar linhagem: Dev → Production.
5. Após a promoção, verificar:
   - snapshot antes;
   - comparação Dev vs Production;
   - readback API;
   - storefront público;
   - receipt;
   - rollback.

## Exceção

Patch direto em Production só é aceitável se Lucas aprovar explicitamente como hotfix emergencial direto em Production, nomeando essa exceção.

## Motivo

Dev e Production não podem virar dois temas independentes. O histórico operacional precisa permanecer sequencial, com Dev como origem das mudanças aprovadas e Production como destino da promoção.

## Aplicação prática

Frase de Lucas: “aprovado, subir para produção”

Interpretação correta do Hermes:

> Promover/mergear o tema Dev para Production no escopo aprovado, mantendo histórico e verificações.

Interpretação incorreta:

> Fazer um patch solto em Production copiando trechos manualmente sem tratar como promoção Dev → Production.
