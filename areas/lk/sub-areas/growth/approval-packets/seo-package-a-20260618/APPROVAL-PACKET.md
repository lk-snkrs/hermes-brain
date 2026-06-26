# Approval Packet — LK SEO/CRO Pacote A

Data: 2026-06-18 11:15 BRT  
Executor: `lk-shopify`  
Escopo: SEO/CRO rápido — pacote A em preview  
Status: **aguardando aprovação explícita de Lucas para qualquer write externo**

## Reminder OS

- Reminder OS loop needed: yes
- Reminder OS owner: `lk-shopify`
- Reminder OS next action: se Lucas aprovar, executar somente o escopo aprovado, com backup/readback/rollback e receipt.
- Reminder OS review trigger: resposta explícita de Lucas aprovando o lote e escopo.
- Reminder OS evidence:
  - `lk_seo_package_a_admin_public_summary.json`
  - `lk_seo_package_a_admin_public_scan.csv`
  - `lk_seo_package_a_admin_public_issues_preview.csv`
  - `lk_seo_package_a_batch1_proposed_changes.csv`

## Escopo executado até agora

Executado apenas read-only:

1. Varredura Shopify Admin GraphQL **read-only** para produtos e coleções.
2. Varredura HTML pública para páginas e home.
3. Geração de CSV completo, CSV de issues e CSV de mudanças propostas para lote 1.
4. Nenhum write em Shopify, tema, robots, páginas, produtos, coleções, apps ou campanhas.

Credenciais: usadas via Doppler helper, `values_printed=false`.

## Evidência resumida

Total analisado: 2.080 objetos

- Produtos ativos via Admin: 1.838
- Coleções via Admin: 181
- Páginas + home via HTML público: 61

Distribuição por prioridade:

- P0: 175
- P1: 1.190
- P2: 377
- OK: 338

Issues detectadas:

- Missing SEO description no Admin: 175
- Short title: 86
- Long title: 395
- Short meta description: 59
- Long meta description: 427
- Multiple H1 em páginas públicas: 7
- Generic meta copy: 544
- Product meta sem sinal de originalidade/autenticidade: 1.022

Observação importante: para produtos/coleções, o scan Admin mede o campo SEO no Shopify. Em alguns casos o storefront pode gerar fallback público a partir do conteúdo; mesmo assim, campo SEO vazio no Admin é oportunidade de controle e consistência.

## Arquivos gerados

Diretório Brain:

`areas/lk/sub-areas/growth/approval-packets/seo-package-a-20260618/`

Arquivos:

- `lk_seo_package_a_admin_public_summary.json`
- `lk_seo_package_a_admin_public_scan.csv`
- `lk_seo_package_a_admin_public_issues_preview.csv`
- `lk_seo_package_a_batch1_proposed_changes.csv`

Origem local de execução:

`/opt/data/profiles/lk-shopify/cron/output/seo_package_a_20260618/`

## Lote 1 proposto para aprovação

Total de mudanças propostas: 56

Quebra:

- 1 ajuste técnico de robots:
  - `Sitemap: /sitemap.xml`
  - para `Sitemap: https://lksneakers.com.br/sitemap.xml`
- 7 ajustes de H1 em páginas:
  - `autenticidade`
  - `guia-adidas-samba`
  - `guia-adidas-sambae`
  - `guia-onitsuka-tiger-mexico-66`
  - `llms-txt`
  - `sobre-a-lk`
  - `sobre-a-lk-sneakers-e-apparels`
- 23 ajustes em coleções:
  - 11 SEO titles
  - 12 SEO descriptions
- 25 SEO descriptions de produtos P0 como lote piloto.

## Exemplos de mudanças propostas

### Robots

Atual:

```txt
Sitemap: /sitemap.xml
```

Proposto:

```txt
Sitemap: https://lksneakers.com.br/sitemap.xml
```

### Página Sobre

Atual:

- H1: `O que é raro merece ser encontrado.`
- H1: `LK na Imprensa`

Proposto:

- manter H1: `O que é raro merece ser encontrado.`
- rebaixar para H2: `LK na Imprensa`

### Coleção Adidas by Stella McCartney

SEO title atual:

```txt
Adidas by Stella McCartney
```

SEO title proposto:

```txt
Adidas by Stella McCartney Original | LK Sneakers
```

SEO description proposta:

```txt
Compre Adidas by Stella McCartney original na LK Sneakers: curadoria premium, autenticidade garantida, atendimento humano e até 10x sem juros.
```

### Produto piloto

Padrão proposto para produto P0 com SEO description vazia:

```txt
Compre [nome do produto] original na LK Sneakers. Produto 100% autêntico, com curadoria premium, atendimento humano e pagamento em até 10x sem juros.
```

## Risco

### Baixo

- Ajuste de robots sitemap absoluto.
- Ajuste semântico H1 → H2, se feito no template/page correto e validado no público.

### Baixo/médio

- SEO titles/descriptions em coleções e produtos.
- Risco principal: copy muito genérica se aplicada em massa sem revisão editorial.
- Por isso o lote 1 limita produtos a 25 itens P0 e deixa o CSV como preview.

### Médio

- Se H1 estiver vindo de template compartilhado, pode afetar mais páginas do que o handle alvo. Exige backup e readback.

## Rollback

Antes de qualquer write aprovado:

1. Exportar snapshot dos objetos alterados:
   - robots/theme asset atual;
   - páginas afetadas;
   - coleções afetadas;
   - produtos afetados.
2. Salvar rollback JSON no Brain/receipt.
3. Aplicar somente escopo aprovado.
4. Fazer readback Admin e público.
5. Se houver erro:
   - restaurar valor anterior de SEO field;
   - restaurar heading anterior;
   - restaurar linha anterior do robots/theme asset.

## Critérios de verificação pós-execução

- Admin readback dos campos alterados.
- Public readback das URLs alteradas.
- `robots.txt` público contendo sitemap absoluto.
- Páginas de H1 com exatamente 1 H1.
- Titles/metas dentro da faixa alvo quando possível:
  - SEO title: ~30–65 chars
  - SEO description: ~110–160 chars
- Nenhum ajuste em preço, estoque, disponibilidade, checkout, apps, Klaviyo, Meta, GMC ou campanhas.

## Bloqueio atual

Aguardando aprovação explícita de Lucas.

Nada foi alterado em produção.

## Próxima decisão

Opções:

1. Aprovar lote 1 completo: 56 mudanças.
2. Aprovar só robots + H1: 8 mudanças.
3. Aprovar só coleções P0: 23 mudanças.
4. Pedir revisão manual do CSV antes de aprovar qualquer write.
