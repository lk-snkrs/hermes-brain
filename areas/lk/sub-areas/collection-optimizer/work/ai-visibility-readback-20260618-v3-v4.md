# AI Visibility readback — v3 Lululemon + v4 Travis Scott

Data: 2026-06-18
Método: fetch público + script Python com `User-Agent: Hermes-LK-AI-Visibility-Readback/1.0` e `Cache-Control: no-cache`.

## Source maps públicos

- `https://lksneakers.com.br/llms.txt`: 200 OK; contém `LK_TRAVIS_SCOTT_AI_V4_START`, `LK_LULULEMON_AI_V3_START` e regra anti-inferência de estoque/preço/prazo/tamanho.
- `https://lksneakers.com.br/agents.md`: 200 OK; contém `LK_TRAVIS_SCOTT_AI_V4_START`, `LK_LULULEMON_AI_V3_START` e orientação para encaminhar detalhes comerciais ao atendimento LK.

## Storefront público

### Lululemon v3

- Collection `/collections/lululemon`: 200 OK; sem `Liquid error`; HTML contém `lk-goc-lululemon` e texto `Lululemon original no Brasil`.
- Guia `/pages/lululemon-original-brasil-guia-lk`: 200 OK; sem `Liquid error`; HTML contém `Lululemon original no Brasil`, mas não retornou classe `lk-goc-lululemon` nem marker técnico `LK_LULULEMON_AI_V3` no readback público.

Interpretação: source map e collection estão OK; guia Lululemon precisa de revalidação posterior ou checagem Admin/template se quisermos confirmar o bloco visual dedicado. Não há erro visível.

### Travis Scott v4

- Collection `/collections/air-jordan-travis-scott`: 200 OK; sem `Liquid error`; HTML contém `lk-goc-travis` e texto `Air Jordan Travis Scott original no Brasil`.
- Guia `/pages/air-jordan-travis-scott-original-brasil-guia-lk`: 200 OK; sem `Liquid error`; HTML contém `lk-goc-travis` e texto `Air Jordan Travis Scott original no Brasil`.

Interpretação: v4 propagou no Storefront público para collection e guia.

## Status executivo

- v4 Travis Scott: validado publicamente.
- v3 Lululemon: validado em `llms.txt`, `agents.md` e collection; guia sem erro, mas bloco/section dedicado não confirmado no HTML público atual.
- Nenhuma página retornou `Liquid error`.

## Próxima ação recomendada

- Não fazer correção de produção agora sem necessidade; monitorar/revalidar guia Lululemon depois de nova janela de CDN ou checar Admin/template em read-only antes de qualquer patch.
