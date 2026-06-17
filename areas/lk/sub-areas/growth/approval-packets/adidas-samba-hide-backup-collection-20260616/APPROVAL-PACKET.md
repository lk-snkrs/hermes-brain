# Approval Packet — Ocultar backup da duplicata Adidas Samba

Gerado: 2026-06-16T22:20:09.706699+00:00

## Contexto
A consolidação `/collections/samba -> /collections/adidas-samba` foi concluída. Para liberar a rota `/samba`, a coleção duplicada virou `/collections/samba-duplicata-backup-20260616`.

## Problema
O handle de backup ainda é público e apareceu no sitemap. Isso pode criar uma nova duplicata indexável se o Google descobrir a URL.

## Recomendação
Fazer uma etapa separada para ocultar/despublicar/arquivar a coleção backup da loja online, mantendo rollback documentado. Antes de executar, validar o método Shopify mais seguro para remover a publicação sem afetar produtos.

## Aprovação necessária
`Aprovo ocultar/despublicar a coleção backup /collections/samba-duplicata-backup-20260616 da loja online, sem mexer em produtos, preço, estoque, feed, campanhas ou theme, com backup, QA e rollback.`
