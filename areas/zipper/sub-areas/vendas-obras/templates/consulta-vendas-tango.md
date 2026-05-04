# Template — Consulta `vendas_tango` Zipper

## Objetivo

Padronizar consultas comerciais read-only no banco Zipper Vendas antes de afirmar histórico, canal, recorrência ou performance de obra/artista.

## Uso permitido

- Preparar resposta interna para Lucas/Osmar.
- Embasar abordagem de colecionador antes do rascunho.
- Comparar artista, obra, faixa de valor, período ou canal de venda.
- Preparar insumos para feira/comunicação.

## Uso bloqueado sem aprovação

- Enviar dado para colecionador, artista, imprensa ou público externo.
- Alterar qualquer registro no banco.
- Usar resultado como proposta comercial sem revisão Lucas/Osmar.

## Fonte de verdade

- Banco: Zipper Vendas `pcstqxpdzibheuopjkas`.
- Tabela principal: `vendas_tango`.
- Campo crítico quando existir: `pedido_origem`.
- Credenciais: Doppler `lc-keys/prd`, apenas nomes `SUPABASE_ZIPPER_VENDAS_URL` e `SUPABASE_ZIPPER_VENDAS_SERVICE_KEY`.

## Entrada mínima

```text
Pergunta comercial:
Período:
Artista/obra/colecionador/canal:
Recorte necessário:
Decisão que a consulta vai informar:
```

## Checklist antes da consulta

- [ ] Confirmar que a pergunta é Zipper Vendas, não SPITI/leilão.
- [ ] Definir período explícito.
- [ ] Declarar se março/2026 aparece no recorte; se aparecer, marcar como mês excepcional.
- [ ] Rodar apenas leitura (`select`/API read-only).
- [ ] Não imprimir secrets, URLs assinadas ou chaves.

## Modelo de saída interna

```text
Resumo:
- Pergunta respondida:
- Fonte consultada:
- Período:
- Total de registros no recorte:
- Receita/valor quando aplicável:
- Canais/origem (`pedido_origem`) quando disponível:
- Top obras/artistas quando aplicável:

Interpretação:
- O que o dado sustenta:
- O que o dado NÃO sustenta:
- Ressalvas:

Recomendação:
- Próxima ação sugerida:
- Precisa de aprovação Lucas/Osmar? sim/não
- Pode virar mensagem externa? somente após aprovação
```

## Regras de linguagem

- Não escrever “vende muito” sem volume, período e comparação.
- Preferir “no recorte consultado...” a afirmações gerais.
- Se o dado estiver incompleto, usar `[a confirmar]`.
- Separar fato, interpretação e recomendação.

## Registro posterior

Se a consulta virar decisão comercial, registrar em `areas/zipper/contexto/lessons.md` ou no CRM/fonte operacional indicada por Lucas/Osmar.
