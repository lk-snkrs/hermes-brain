# Checklist mensal — governança dos crons do Mordomo

Objetivo: garantir que o Mordomo interrompa Lucas só quando há decisão real, sem logs técnicos, filas jogadas ou ações externas sem aprovação.

## 1. Inventário

- Listar scheduler principal: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.
- Listar perfil Mordomo: `HERMES_HOME=/opt/data/profiles/mordomo /opt/hermes/.venv/bin/hermes cron list --all`.
- Confirmar jobs pausados por segurança: executor A2 deve continuar pausado até aprovação explícita.

## 2. Destinos

- `local`: artefatos, logs, CRM sync, ingestões e resumos internos.
- Telegram/origin: apenas decisão, alerta urgente, erro real ou aprovação.
- Jobs com Telegram direto devem manter stdout vazio quando o envio direto funcionar.
- Fallback por stdout só pode conter mensagem limpa, sem `Cronjob Response`, `job_id`, JSON, classe interna, tier/autonomia/status cru.

## 3. Qualidade das mensagens

Cada alerta para Lucas precisa ter:

- 🚨/⚠️/🟢/📅 conforme urgência.
- **Contexto claro**: quem, empresa, assunto.
- **O que aconteceu** em português humano.
- **Por que importa**.
- **Cuidado/bloqueador**.
- **Próximo passo recomendado**.

Proibido em Telegram:

- `Cronjob Response`
- `job_id`
- `needs_lucas_decision`
- `price_or_availability_or_conditions`
- `tier`
- `autonomia`
- JSON bruto
- fila completa sem decisão

## 4. Watchdog do gateway

Política aprovada para documentação local:

- Pode observar saúde e registrar evidência.
- Pode alertar erro real com mensagem limpa.
- Não deve expor segredo, token, compose, Docker socket ou detalhes sensíveis.
- Reinício/alteração de gateway, Docker, compose, rede, Traefik, volume, imagem ou VPS continua exigindo aprovação explícita com plano e rollback, salvo exceção previamente documentada.
- Se um watchdog já reinicia automaticamente por configuração existente, auditoria mensal deve verificar: escopo limitado, logs sem segredo, último status, e ausência de loop de reinício.

## 5. Verificação mínima

Rodar:

```bash
python3 -m py_compile /opt/data/profiles/mordomo/scripts/mordomo_decision_digest.py \
  /opt/data/profiles/mordomo/scripts/mordomo_whatsapp_global_watch.py \
  /opt/data/profiles/mordomo/scripts/mordomo_whatsapp_daily_digest.py \
  /opt/data/profiles/mordomo/scripts/mordomo_calendar_global_watch.py

python3 /opt/data/profiles/mordomo/scripts/test_mordomo_decision_comms.py
python3 /opt/data/profiles/mordomo/scripts/test_mordomo_whatsapp_global_watch_noise.py
python3 /opt/data/profiles/mordomo/scripts/test_mordomo_daily_digest.py
python3 /opt/data/profiles/mordomo/scripts/test_mordomo_callback_learning.py
```

Critério de pronto: saída Telegram limpa + testes OK + artefatos locais gravados + nenhum termo proibido nos previews.
