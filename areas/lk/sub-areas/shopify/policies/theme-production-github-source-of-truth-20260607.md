# Política — Tema Production via GitHub, nunca Asset API direto

Data: 2026-06-07

## Regra

Para qualquer mudança de tema da LK em Production — Liquid, CSS, JS, snippet, section, template ou asset de tema — o GitHub é a fonte de verdade.

O caminho padrão obrigatório é:

1. validar em DEV/unpublished quando aplicável;
2. aplicar o diff no repositório do tema;
3. abrir PR/merge para `production`;
4. deixar o pipeline/deploy/sync atualizar Shopify;
5. fazer readback Shopify;
6. rodar QA público/visual conforme risco;
7. registrar receipt e rollback.

## Bloqueio

É proibido fazer write direto no tema Shopify Production via Asset API por padrão.

Uma aprovação genérica como `Aprovo`, `Aprovo Production` ou `pode subir` **não** autoriza write direto no tema live via Asset API.

## Exceção

Direct Asset API no tema Production só pode ocorrer se Lucas aprovar explicitamente um hotfix emergencial direto e nomear esse caminho, por exemplo:

`Aprovo hotfix direto no tema Production via Asset API para [escopo exato], com backup, readback e rollback.`

Sem essa frase/escopo, parar e preparar PR GitHub.

## Aplicação prática

- DEV/unpublished pode receber upload aprovado para preview/QA.
- Production Shopify é runtime/publicação, não fonte de verdade.
- O merge real deve existir no GitHub/branch `production`.
- Se Shopify live e GitHub divergirem por write antigo direto, fazer PR de reconciliação primeiro; não escrever de novo no Shopify salvo necessidade do pipeline ou aprovação emergencial explícita.

## Motivo

Evita que deploys futuros revertam hotfixes, mantém revisão/auditoria, preserva rollback versionado e alinha a operação LK Shopify ao fluxo correto do tema.