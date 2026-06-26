# LK SEO/CRO — próximas 5 frentes após ordenação de coleções e tags/badges

Data: 2026-05-31
Responsável: Hermes LK Shopify / LK Growth
Status: Frente 1 iniciada em modo read-only

## Contexto

Lucas informou que a ordenação das coleções e as tags/badges já foram feitas. Próxima etapa: escolher novas frentes de melhoria em Shopify/CRO/SEO/GEO sem write externo sem aprovação explícita.

## Backlog aprovado para acompanhamento

1. Auditoria mobile/visual das páginas públicas principais da LK: home, coleção, PDP, busca/menu/filtros e carrinho público.
2. Levantar lista dos 20 PDPs prioritários para CRO/SEO com base em tráfego/venda/risco de baixa conversão.
3. Diagnóstico das coleções principais com checklist SEO/GEO: conteúdo editorial, FAQ, links internos, intenção e mobile.
4. Pacote GMC/feed read-only: reprovações, warnings, preço/disponibilidade, imagem, título, GTIN/brand/categoria Google.
5. Preparar approval packet com mudanças pequenas, evidência, risco, rollback e próxima decisão.

## Frente 1 — auditoria mobile/visual pública

Escopo inicial read-only:

- Home: https://lksneakers.com.br/
- Coleção Samba: https://lksneakers.com.br/collections/samba
- Coleção Todos os Produtos/Últimos lançamentos: https://lksneakers.com.br/collections/ultimos-lancamentos-2
- PDP exemplo: https://lksneakers.com.br/products/nike-dunk-low-rose-whisper
- Busca: https://lksneakers.com.br/search?q=samba
- Carrinho vazio: https://lksneakers.com.br/cart

Evidência inicial coletada via DataForSEO OnPage/Lighthouse com user-agent mobile em modo read-only.

## Achados preliminares

- Home tem title longo: 78 caracteres; meta description longa: 187 caracteres.
- Home tem `og:title` genérico (`LK`) diferente do title SEO completo.
- Coleção Samba tem title curto (`Samba - LK Sneakers`) versus H1 bom (`Adidas Samba`) e conteúdo editorial/FAQ já presente.
- PDP Nike Dunk Low Rose Whisper tem title longo: 78 caracteres; conteúdo/FAQ/reviews/guia de tamanho presentes.
- Carrinho vazio não tem H1; usa H2 `Seu carrinho está vazio`.
- Padrão recorrente nas páginas: HTML parser aponta tag de fechamento incompatível perto do footer/newsletter; verificar no tema antes de qualquer mudança.
- Páginas de coleção/PDP têm DOM grande, mais de 1500 nós, e 1–3 recursos render-blocking; não é bloqueio crítico, mas é ponto de performance/limpeza.
- Lighthouse inicial: performance alta em home/coleção/PDP, SEO ~0.92, best practices ~0.73; PDP com agentic-browsing menor (~0.67), bom candidato para revisão de markup/semântica.

## Guardrails

- Nenhum write em Shopify/theme/GMC/Klaviyo/ads sem aprovação explícita atual de Lucas.
- Próximo output deve separar evidência, interpretação, risco, rollback e próxima decisão.
