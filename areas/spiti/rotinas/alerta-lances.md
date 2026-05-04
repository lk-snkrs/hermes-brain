# Rotina — Alerta de lances SPITI

## O que faz

Documenta alertas internos sobre mudança de lance/lote e regras de deduplicação.

## Fontes documentadas

- Monitor `spiti-lances`.
- n8n workflow `OHC9FfEsK0JRVMBK`.
- Supabase `rmdugdkantdydivgnimb`.
- Email como fonte de verdade para total.

## Deduplicação documentada

Memória atual registra TTL 24h e chave `{lote_id}:{lance_atual}`.

## Aprovação

Alertas internos podem ser preparados. Mensagens externas ou para grupo/cliente exigem aprovação Lucas.

## Falhas conhecidas

- n8n timeout curto pode abortar workflow mesmo com Playwright funcionando.
- Solução documentada: webhook async responde 2xx imediato e processa em thread separada.
