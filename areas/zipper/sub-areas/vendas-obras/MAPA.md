# Zipper — Vendas de Obras

## Objetivo

Organizar análise comercial de obras vendidas da Zipper usando dados reais do banco Zipper Vendas.

## Fonte de verdade

- Banco: Zipper Vendas `pcstqxpdzibheuopjkas`.
- Tabela principal citada: `vendas_tango`.
- Campo crítico: `pedido_origem`, quando disponível, para entender canal de venda.

## Loop Hermes

```text
pergunta comercial → consulta vendas_tango → obra/artista/canal → análise → recomendação → aprovação Lucas/Osmar → registro do aprendizado
```

## Quando usar

- Perguntas sobre artista, obra, recorrência, canal ou histórico de venda.
- Preparação de abordagem comercial.
- Priorização de obras para feira ou comunicação.
- Comparação entre vendas reais e narrativa comercial.

## Regras

- Nunca dizer que uma obra ou artista “vende bem” sem consultar dados.
- Não usar março/2026 como baseline sem ressalva: foi mês excepcional.
- Não misturar vendas reais da Zipper com lances/leilão SPITI.

## Credenciais

Buscar via Doppler `lc-keys/prd`; nunca versionar valores.

- `SUPABASE_ZIPPER_VENDAS_URL`
- `SUPABASE_ZIPPER_VENDAS_SERVICE_KEY`

## Templates

- `templates/consulta-vendas-tango.md` — consulta read-only padronizada para `vendas_tango`, com período, ressalvas e separação fato/interpretação/recomendação.
