# Continuation Packet — Alo Yoga FAQ + Samba Next Wave — 2026-06-24

Status: **preparado; sem write executado nesta continuação**.

## 1) Alo Yoga FAQ/schema — investigação read-only

Evidência: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/alo-yoga-faq-implementation-20260624/alo-yoga-collection-admin-public-readonly.json`

### Achados
- Collection `/collections/alo-yoga-1` existe.
- SEO title/meta já foram atualizados e validados via `view=`.
- Metafields lidos: 4.
- FAQPage público atual: **0**.
- Ou seja: há espaço para publicar FAQ sem duplicar FAQPage, mas a execução deve ter readback para garantir que ficou **1 FAQPage**, não 0 e não 2.

### Recomendação
Executar FAQ Alo Yoga como **próximo pacote separado**, com escopo:
- adicionar FAQ visível/estruturado para collection Alo Yoga;
- gerar/validar FAQPage se o tema/metafield suportar;
- não alterar handle/canonical;
- não alterar preço/estoque/produtos/PDPs;
- rollback por metafield/description/theme asset conforme implementação real.

### Aprovação segura sugerida

`Aprovo publicar o FAQ Alo Yoga na collection /collections/alo-yoga-1 em escopo mínimo, com readback público garantindo 1 FAQPage, rollback salvo, sem alterar handle, canonical, preço, estoque, produtos, PDPs, campanhas, Klaviyo ou WhatsApp.`

---

## 2) Samba Next Wave — no-rework e ranking candidates

Evidência: `work/ranking-attack-no-rework-20260624/next-candidate-keywords-after-batch.json`

### Defender
- `adidas samba jane` — pos. 2, vol. 1.000.

### Atacar 11–30
- `adidas samba marrom` — pos. 19, vol. 3.600, landing PDP Marrom.
- `adidas samba feminino` — pos. 26, vol. 49.500, landing collection Adidas Samba.
- `tenis adidas samba` — pos. 28, vol. 27.100, landing collection Adidas Samba.
- `samba verde` — pos. 18, vol. 1.000, landing blog.
- `samba branco` — pos. 17, vol. 880, landing PDP Branco.

### Sem ranking — oportunidade de superfície/intent
- `adidas samba masculino` — vol. 5.400.
- `adidas samba og` — vol. 4.400.
- `adidas samba preto` — vol. 4.400.
- `adidas samba xlg` — vol. 2.900.
- `adidas samba feminino original` — vol. 2.400.

### Recomendação Samba
Não mexer em tudo. Primeiro pacote mínimo:
1. Auditar collection `adidas-samba` Admin + público.
2. Auditar PDP Marrom e PDP Branco.
3. Propor SEO meta apenas se houver meta operacional/truncada.
4. Verificar se `samba verde` deve continuar no blog ou ganhar ponte collection/PDP.

### Aprovação segura sugerida para próxima etapa

`Aprovo fazer somente readback Admin/público da collection Adidas Samba e dos PDPs Samba Marrom/Branco, preparar proposta de SEO meta/linkagem sem write, e não alterar produção ainda.`

---

## 3) Ponto técnico pendente

- NB 9060 Bisque: Admin OK e `view=` OK; URL limpa ainda cacheada antiga. Não agir agora; recheck posterior.

## Ordem recomendada

1. Se quiser ganho GEO/FAQ em activewear: aprovar FAQ Alo Yoga.
2. Se quiser continuar ranking sneakers: aprovar readback Samba sem write.
3. Recheck NB9060 Bisque cache em algumas horas.
