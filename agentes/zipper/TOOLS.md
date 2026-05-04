# TOOLS — Agente Zipper

## Fontes principais

- Supabase Zipper Vendas: `SUPABASE_ZIPPER_VENDAS_URL`, `SUPABASE_ZIPPER_VENDAS_SERVICE_KEY`
- Supabase SPITI/CRM apenas quando contexto pedir, com cuidado para não misturar bases
- Evolution ZipperGaleria para comunicações aprovadas
- GA4/Instagram/Metricool quando aplicável

## Regras

- Usar Doppler para valores sob demanda.
- Nunca salvar secret value no Brain.
- Antes de afirmar histórico de venda, consultar `vendas_tango`.
- Comunicação com colecionadores exige aprovação Lucas/Osmar.
