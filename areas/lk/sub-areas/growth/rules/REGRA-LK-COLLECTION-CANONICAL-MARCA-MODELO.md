# Regra — Canonical de coleções por marca + modelo

Criado: 2026-06-16T21:56:03.136933+00:00
Origem: correção do Lucas durante consolidação Adidas Samba.

## Regra

Quando houver duplicidade de coleções para o mesmo cluster de busca, a URL canonical principal deve priorizar o handle mais explícito para SEO/GEO quando ele representar melhor a intenção de busca, especialmente `marca + modelo`.

Exemplo canônico LK:

- Principal correta: `/collections/adidas-samba`
- Duplicata/atalho a consolidar: `/collections/samba`

Não escolher automaticamente o handle mais curto só por ser mais limpo. Em e-commerce de sneakers, o handle com marca + modelo tende a ser mais claro para Google, AI Search e usuário.

## Aplicação operacional

Antes de recomendar canonical/redirect de coleção:

1. Comparar intenção de busca principal.
2. Verificar se o handle contém marca + modelo.
3. Verificar linkagem interna, sitemap, GSC/SEO quando disponível.
4. Se houver conflito entre handle curto e handle SEO-explicativo, tratar o handle marca+modelo como default recomendado, salvo evidência forte em contrário.
5. Qualquer redirect/handle/despublicação segue exigindo aprovação explícita.

## Caso Adidas Samba

Decisão do Lucas: manter `/collections/adidas-samba` como principal por SEO. A rota `/collections/samba` deve ser tratada como duplicata/atalho apenas quando houver aprovação para consolidação estrutural.
