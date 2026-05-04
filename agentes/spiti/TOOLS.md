# TOOLS — Agente SPITI

## Ferramentas principais

- Supabase SPITI / Zipper CRM para dados de lotes e contatos.
- Email como fonte de verdade para lances, quando disponível.
- Evolution API para comunicação aprovada.
- n8n para workflows existentes, quando documentados.
- Doppler `lc-keys/prd` para credenciais sob demanda.

## Regras

- Usar Doppler apenas para buscar valores no momento de execução.
- Nunca salvar valores de secrets no Brain.
- Preferir queries verificáveis e citar a fonte usada.
- Para workflows que demoram mais que poucos segundos, usar padrão async quando aplicável.
