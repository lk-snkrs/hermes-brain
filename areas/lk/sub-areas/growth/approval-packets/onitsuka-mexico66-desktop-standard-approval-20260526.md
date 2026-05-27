# Approval packet — Onitsuka Tiger Mexico 66 como padrão de coleção

Data: 2026-05-26
URL auditada: https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66?_ab=0&_fd=0&_sc=1&cb=20260526-013141

## Pedido limpo

Corrigir a coleção Onitsuka Tiger Mexico 66 e usar como padrão visual/comercial para próximas coleções LK.

## Correções solicitadas

1. Padronizar a distância/alinhamento entre o título da coleção e o bloco editorial superior.
2. Transformar o Guia Editorial LK em uma versão desktop real, mantendo mobile comprimido.
3. Preservar a estrutura product-first: produtos primeiro, guia depois do grid/carregar mais.

## Diagnóstico read-only

- H1 `Onitsuka Tiger Mexico 66`: left ≈ 40px.
- Bloco superior `Perfil baixo, herança japonesa.` antes do ajuste: left ≈ 28px.
- Guia editorial antes do ajuste: card interno ocupava ~481px dentro de um painel de ~1076px, gerando aparência mobile em desktop e vazio à direita.
- O conteúdo público já está sem o rótulo `Sinal editorial`.

## Patch preparado

Arquivo CSS pronto:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/onitsuka-mexico66-desktop-standard-hotfix-20260526.css`

Escopo do patch:

- alinha a rail superior em 40px no desktop;
- mantém padding mobile em 16px;
- amplia o Guia Editorial LK para `max-width: 1180px`;
- transforma o card interno em grid desktop de duas colunas;
- força o card wide a ocupar toda a largura útil do painel;
- preserva CTA preto com texto branco.

## Validação visual em navegador

Teste não persistente via CSS injetado no navegador:

- Antes: `/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_bbaade6ac5b44d059511494923594f42.png`
- Intermediário v1: `/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_1105ad5eb8df47bdbaaaf3a380710370.png`
- Candidato aprovado visualmente v2: `/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_73ec5593c8d0463facfed9cbf10d2e2c.png`

Resultado v2:

- guia ocupa melhor o desktop;
- card interno fica amplo;
- FAQ/editorial em duas colunas;
- sem quebra óbvia de layout/contraste;
- ponto fino opcional: reduzir duplicidade entre FAQ interno e FAQ geral em etapa posterior.

## Risco

Baixo se aplicado em dev/preview primeiro. O patch é escopado ao handle/classes da coleção Onitsuka e ao ID do guia.

## Rollback

Remover o bloco CSS aplicado ou restaurar o backup do asset de tema anterior.

## Próximo passo

Aplicar no tema dev/preview e devolver link para aprovação visual. Produção só após validação explícita.
