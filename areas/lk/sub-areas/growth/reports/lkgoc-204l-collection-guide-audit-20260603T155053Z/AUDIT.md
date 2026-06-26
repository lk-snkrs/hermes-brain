# Audit LK-GOC — 204L Collection + Guide

- Timestamp UTC: 20260603T155053Z
- Escopo: auditoria read-only das URLs públicas para padronização `lk-goc-*`.
- Observação: isso não faz write em Shopify/production.

## collection_204l
- Status: 200
- HTML bytes: 591155
- Classes `lk-goc-*`: 0
- Classes `lk-lkgoc-*`: 9
- Classes `lk-204l-*`: 10
- Classes `lk-collection-v2*`: 1
- Liquid error: False
- Termos placeholder/técnicos: [{'term': 'placeholder', 'count': 22}, {'term': 'fix', 'count': 90}, {'term': 'TODO', 'count': 32}]

## guide_204l
- Status: 200
- HTML bytes: 444363
- Classes `lk-goc-*`: 0
- Classes `lk-lkgoc-*`: 0
- Classes `lk-204l-*`: 0
- Classes `lk-collection-v2*`: 0
- Liquid error: False
- Termos placeholder/técnicos: [{'term': 'placeholder', 'count': 22}, {'term': 'fix', 'count': 80}, {'term': 'TODO', 'count': 31}]

## Diagnóstico inicial
- A coleção e o guia devem virar a gold source LK-GOC.
- O contrato novo deve ser `lk-goc-*`, com `lk-204l-*` apenas como alias legado quando necessário.
- `lk-lkgoc-*` deve ser considerado namespace transitório/obsoleto e removido do padrão canônico conforme migrarmos os assets.

## Próximo passo seguro
- Readback dos assets Shopify em tema DEV/unpublished.
- Migrar collection + guide em DEV para `lk-goc-*`.
- QA técnico + visual desktop/mobile.
- Approval Lucas.
- Só depois merge para Production.