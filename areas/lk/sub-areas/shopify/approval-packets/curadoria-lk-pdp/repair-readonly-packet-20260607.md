# Approval packet read-only — Curadoria LK PDP maintenance revalidation

Data: 2026-06-07 14:15 BRT
Operador: Hermes LK Shopify
Escopo: read-only; storefront público `/products/<handle>.js`; sem Shopify/Admin/theme write.

## Veredito

Não recomendo abrir write DEV agora para os grupos vermelhos do piloto anterior.

A revalidação focada e o relatório forçado mais recente indicam que os 7 grupos antes vermelhos voltaram a passar no storefront público. O único ponto remanescente é amarelo: 1 produto Air Jordan 4 existe publicamente, mas está `available=false`.

## Evidência

Relatório piloto anterior:

- Arquivo: `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/curadoria-lk-pdp-maintenance-20260607T071257-0300.md`
- Resultado anterior: verde 27 · amarelo 1 · vermelho 7 · cinza 0
- Grupos vermelhos anteriores: `top30-nb-9060`, `top30-sl72-og`, `top30-mexico66-sd`, `top30-nb-530`, `top30-sb-dunk-low`, `top30-adidas-gazelle`, `top30-asics-gel-1130-regular`

Revalidação focada manual, read-only:

- `top30-nb-9060`: 9/9 valid_available; 0 bad; 0 placeholder
- `top30-sl72-og`: 10/10 valid_available; 0 bad; 0 placeholder
- `top30-mexico66-sd`: 10/10 valid_available; 0 bad; 0 placeholder
- `top30-nb-530`: 10/10 valid_available; 0 bad; 0 placeholder
- `top30-sb-dunk-low`: 10/10 valid_available; 0 bad; 0 placeholder
- `top30-adidas-gazelle`: 8/8 valid_available; 0 bad; 0 placeholder
- `top30-asics-gel-1130-regular`: 6/6 valid_available; 0 bad; 0 placeholder
- `top30-air-jordan-4-regular`: 7/8 valid_available; 1 unavailable (`tenis-air-jordan-4-retro-military-blue-branco`); 0 bad; 0 placeholder

Relatório forçado atualizado:

- Comando: `HERMES_HOME=/opt/data/profiles/lk-shopify /opt/data/profiles/lk-shopify/scripts/lk_curadoria_pdp_maintenance_report.py --force`
- Exit code: 0
- Arquivo: `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/curadoria-lk-pdp-maintenance-20260607T141034-0300.md`
- JSON: `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/curadoria-lk-pdp-maintenance-20260607T141034-0300.json`
- Resultado atualizado: verde 34 · amarelo 1 · vermelho 0 · cinza 0
- Handles públicos checados: 260
- Output confirmou: “Nenhum write Shopify/DEV/Production foi executado.”

## Interpretação

O vermelho anterior parece ter sido ruído temporário de storefront/CDN/rate-limit ou uma janela instável de `/products/<handle>.js`, não falha persistente nos grupos.

O único problema persistente é de disponibilidade do item `tenis-air-jordan-4-retro-military-blue-branco` dentro de `top30-air-jordan-4-regular`. Como o grupo ainda mantém 7 produtos publicamente válidos e disponíveis, não há urgência de reparo técnico para evitar bloco quebrado.

## Preview / proposta de ação

Proposta segura agora: monitorar via cron e não mexer no tema.

Opção DEV futura, se Lucas quiser limpar o amarelo:

- Escopo: remover ou substituir somente `tenis-air-jordan-4-retro-military-blue-branco` no grupo `top30-air-jordan-4-regular` do snippet `lk-variante-top30-visited-v2` em DEV/unpublished.
- Motivo: evitar card de produto público porém indisponível dentro da Curadoria.
- Observação: isso é write em tema Shopify e exige aprovação explícita específica antes de executar.

## Risco

- O scanner usa storefront público `.js`; resultados podem variar por edge/CDN, bloqueio temporário ou rate-limit.
- O `git fetch origin production` reportou falta de credencial (`fatal: could not read Username for 'https://github.com'`), então a leitura do source usou o estado/cache disponível de `origin/production`. A revalidação pública dos handles, porém, foi feita ao vivo no storefront.
- Remover o item amarelo sem substituto reduziria o grupo AJ4 de 8 para 7 itens no source, ainda acima do limite operacional mínimo após exclusão do produto atual.

## Bloqueio

Nenhum bloqueio para monitoramento read-only.

Para write DEV/unpublished, bloqueio é aprovação explícita atual de Lucas com escopo exato.

## Rollback

Como nenhum write foi executado, não há rollback aplicado.

Se uma limpeza DEV futura for aprovada, rollback deve ser: backup do snippet antes do PUT, readback do asset, e restauração do backup no mesmo theme se o QA falhar.

## Próxima decisão

Minha recomendação: **não aprovar write agora**. Deixar o cron rodar e só agir se o amarelo persistir ou se algum grupo voltar a vermelho em duas leituras consecutivas.

Se Lucas quiser limpar imediatamente o amarelo, a aprovação precisa ser explícita no formato: “Aprovo DEV remover/substituir AJ4 Military Blue indisponível na Curadoria LK PDP”.

## Segurança operacional

Não houve write em:

- Shopify/Admin
- tema DEV/unpublished
- tema Production
- produto/collection/metafield/tag/menu/page
- preço/estoque/Tiny
- GMC/feed
- Klaviyo/ads/WhatsApp/e-mail/campanha
