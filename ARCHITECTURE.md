# Arquitetura Hermes Brain

Hermes não é OpenClaw. O Hermes usa uma arquitetura multicamada:

```text
Lucas / Telegram
  ↓
Hermes Agent
  ├── memória persistente: preferências e regras compactas
  ├── session_search: histórico de conversas
  ├── Hermes Brain GitHub: contexto estruturado do negócio
  ├── Doppler lc-keys/prd: credenciais sob demanda
  ├── Supabase/Shopify/APIs: dados vivos
  └── cronjobs: execução autônoma
```

GitHub Brain guarda decisões, processos, áreas, agentes, rotinas e skills de negócio.
Doppler guarda secrets.
Bancos e APIs guardam dados vivos.
