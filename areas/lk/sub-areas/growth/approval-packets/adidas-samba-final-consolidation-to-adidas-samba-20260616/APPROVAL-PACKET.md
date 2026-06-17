# Approval Packet — Finalizar Adidas Samba em /collections/adidas-samba

Gerado: 2026-06-16T21:55:39.981524+00:00

## Decisão estratégica
URL principal correta:

`https://lksneakers.com.br/collections/adidas-samba`

Motivo: handle contém marca + modelo e é superior para SEO/GEO.

## Estado atual confirmado
- `/collections/adidas-samba`: HTTP 200, canonical próprio, conteúdo otimizado e FAQ presentes.
- `/collections/samba`: HTTP 200, canonical próprio, também com conteúdo otimizado; segue como duplicata.
- Não há redirect exato ativo para `/collections/samba`.
- As duas coleções têm o mesmo volume de produtos: 95.

## Problema
Enquanto `/collections/samba` continuar ativa com canonical próprio, o Google pode dividir sinais entre duas URLs para a mesma intenção. A página principal `/collections/adidas-samba` fica correta, mas não consolidada.

## Ação recomendada
1. Backup completo das duas coleções.
2. Alterar o handle da coleção duplicada `/collections/samba` para um handle de backup, por exemplo:
   - `/collections/samba-duplicata-backup-20260616`
3. Criar redirect 301:
   - de `/collections/samba`
   - para `/collections/adidas-samba`
4. QA público:
   - `/collections/adidas-samba` deve continuar HTTP 200 com canonical próprio.
   - `/collections/samba` deve responder 301 para `/collections/adidas-samba`.
5. Registrar rollback.

## Impacto esperado
- Consolidação de autoridade/link equity na URL SEO correta.
- Redução de canibalização interna.
- Links antigos para `/collections/samba` passam a reforçar `/collections/adidas-samba`.

## Risco
- Médio: mexe no handle/rota de coleção ativa.
- Homepage/menu hoje pode linkar `/collections/samba`; com 301, o usuário será redirecionado para a URL correta.
- Não mexe em produtos, preço, estoque, feed, campanhas ou theme.

## Rollback
- Remover redirect `/collections/samba -> /collections/adidas-samba`.
- Restaurar handle da coleção duplicada para `samba`.
- Restaurar SEO/descrição a partir do backup se necessário.

## Aprovação necessária
Para executar, preciso da frase explícita:

`Aprovo finalizar Adidas Samba em /collections/adidas-samba: alterar o handle da coleção duplicada /collections/samba para um handle de backup, criar 301 de /collections/samba para /collections/adidas-samba, com backup, QA e rollback.`
