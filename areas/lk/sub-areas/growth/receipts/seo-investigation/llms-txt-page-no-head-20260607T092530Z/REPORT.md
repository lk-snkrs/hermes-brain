# Investigação — /pages/llms-txt sem title/meta

Data UTC: 20260607T092530Z
Contexto: Lucas aprovou investigar pendência do cron `LK Revalidar Pages SEO + Judge.me cache pós-patch 60m`.

## Escopo
- Classificação: SEO técnico + GEO/AI Search + Shopify theme/page.
- Modo: read-only. Nenhum write externo executado.

## Evidências públicas
- `https://lksneakers.com.br/pages/llms-txt`
  - HTTP 200
  - Content-Type: `text/html; charset=utf-8`
  - Body começa direto com markdown `# LK Sneakers`
  - Ausente: `<title>`, `<meta name="description">`, canonical.
  - ETag indica `PageDetailsController`.
- `https://lksneakers.com.br/llms.txt`
  - HTTP 200
  - Content-Type: `text/markdown; charset=utf-8`
  - Ausente title/meta por natureza de arquivo markdown/texto; isso é esperado.
  - ETag indica `LlmsTxtController`.
- `https://lksneakers.com.br/sitemap.xml`
  - Inclui `sitemap_pages_1.xml?...` e `sitemap_agentic_discovery.xml`.
- `sitemap_pages_1.xml?...`
  - Inclui `https://lksneakers.com.br/pages/llms-txt` com lastmod `2026-06-06T22:17:59-03:00`.
- `robots.txt`
  - Não bloqueia `/pages/llms-txt`; bots de AI permitidos genericamente.
- `agents.md`
  - Já aponta para `/llms.txt` e `/llms-full.txt`; não depende de `/pages/llms-txt`.

## Causa provável
O template Shopify `templates/page.llms-txt.liquid` está com `{%- layout none -%}` e entrega markdown puro em uma Shopify Page. Como a Page está publicada, entra no sitemap de pages, mas por não renderizar layout/head não tem title/meta/canonical.

Snapshot local relacionado encontrado:
- `receipts/shopify-theme/prod-to-dev-theme-sync-20260531T141707Z/prod-theme-snapshot/templates__page.llms-txt.liquid.value`
- Conteúdo inicia com `{%- layout none -%}`.

## Diagnóstico
A pendência não é cache. É conflito de intenção:
- Para `/llms.txt`, markdown puro sem title/meta é correto.
- Para `/pages/llms-txt`, por estar em sitemap como Page HTML, o Google/SEO espera head/canonical/title/meta.

## Risco
Baixo/médio técnico:
- Página inútil/duplicada em sitemap.
- Possível URL thin/sem head em GSC.
- Não parece bloquear o funcionamento do `/llms.txt` nem do `/agents.md`.

## Recomendação Growth
Prioridade recomendada: remover/neutralizar `/pages/llms-txt` como URL indexável, mantendo `/llms.txt` como fonte canônica de AI Search.

Opção preferida: transformar `/pages/llms-txt` em uma página HTML mínima com head normal e canonical/CTA apontando para `/llms.txt`, ou noindex se a implementação permitir no template/page SEO.

Opção limpa se confirmarmos que `/llms.txt` não depende da Page: despublicar/deletar a Shopify Page `/pages/llms-txt` para removê-la do sitemap. Requer confirmar dependência no admin/Shopify antes.

## Aprovação necessária
Qualquer correção exige write Shopify production ou theme production/page field, portanto precisa aprovação explícita escopada de Lucas.

## Próximo pacote sugerido
Approval packet curto:
1. Snapshot/rollback do template/page atual.
2. Patch em dev theme ou ajuste de Page SEO/template, conforme acesso.
3. Readback público: `/pages/llms-txt` com title/meta/canonical ou removida do sitemap; `/llms.txt` intacto.
4. Revalidar em 60m e revisar GSC em ~7 dias.
