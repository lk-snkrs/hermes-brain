# Decisão — Opções para Hermes Runtime v0.9.0 → v0.12.0

Data: 2026-05-05.

Status: decisão preparada; nenhuma alteração aplicada nesta rodada.

## Contexto confirmado

Runtime atual em `lc.vps`:

- containers Hermes `Up` há ~15h na coleta de 2026-05-05 10:08 UTC;
- `hermes-agent-5ajw-hermes-agent-1`: `Hermes Agent v0.9.0 (2026.4.13)`;
- `hermes-agent-5ajw-hermes-telegram-1`: `Hermes Agent v0.9.0 (2026.4.13)`;
- imagem: `ghcr.io/hostinger/hvps-hermes-agent:latest`;
- tentativa segura anterior de `docker compose pull/up` manteve o mesmo digest e a mesma versão;
- release upstream atual: `v2026.4.30` / `Hermes Agent v0.12.0 (2026.4.30)`.

Gateway/Telegram atual:

- `hermes gateway run` é PID 1 no container Telegram;
- Telegram API `getMe` OK para o bot `HermesLC_botbot`;
- `getWebhookInfo.url` vazio, compatível com polling;
- `pending_update_count = 0`;
- logs das últimas 2h não mostraram novo conflito;
- `hermes cron list/status` ainda reporta `Gateway is not running`, apesar do processo gateway existir.

Interpretação: o funcionamento Telegram atual é vivo, mas o detector de cron/gateway do runtime v0.9.0 continua divergente. O cron `Hermes release watch` só deve ser considerado automaticamente confiável após execução real em 2026-05-11 ou após correção/validação adicional.

## Opções

| Opção | O que é | Risco | Benefício | Recomendação |
|---|---|---:|---|---|
| Aguardar Hostinger | manter imagem atual até Hostinger publicar runtime mais novo | baixo | zero mudança em produção | seguro, mas mantém v0.9.0 |
| Cobrar/suportar tag oficial Hostinger | buscar confirmação de tag/roadmap oficial Hostinger | baixo | pode preservar suporte/catalogo | bom antes de imagem customizada |
| Imagem customizada Hermes v0.12.0 | construir/usar imagem própria baseada no Hermes upstream | médio/alto | destrava release atual | só com aprovação, staging/backup/rollback |
| Instalar gateway systemd no host | tentar satisfazer detector do cron fora do Docker | alto | poderia fazer cron reconhecer gateway | não recomendado sem desenho; risco de poller duplicado |
| Não mexer e validar cron em 2026-05-11 | aguardar primeira execução do release watch | baixo | evidência real sobre cron | recomendado como observação se não houver urgência |

## Recomendação operacional atual

1. Não instalar gateway systemd no host agora: risco de criar poller duplicado e conflitar com o container Telegram.
2. Não trocar imagem/compose sem janela aprovada.
3. Tratar v0.12.0 como melhoria desejável, não emergência, porque Telegram está respondendo.
4. Aguardar a execução de `Hermes release watch` em 2026-05-11 para validar se o cron dispara apesar do warning; se não disparar, priorizar correção do gateway/cron.
5. Em paralelo, preparar plano de imagem customizada em documento técnico separado, mas não executar.

## Go/no-go para upgrade customizado futuro

Go somente se:

- Lucas aprovar explicitamente janela de manutenção;
- backup atual de `/docker/hermes-agent-5ajw/data` e compose/env estiver feito fora do repo;
- imagem customizada for testada localmente/staging antes;
- rollback para digest/tag anterior estiver testado conceitualmente;
- escopo limitar-se aos dois serviços Hermes;
- Traefik, n8n, Paperclip, volumes, redes, root/SSH/firewall ficarem fora do escopo.

No-go se:

- não houver tag/digest pinável;
- compose/env precisar de mudança ampla;
- teste local não confirmar Telegram/gateway/cron;
- houver risco de afetar outros apps Docker;
- secrets precisarem ser expostos.

## Evidência read-only usada

- `docker ps --filter name=hermes-agent-5ajw`.
- `docker exec ... /opt/hermes/.venv/bin/hermes --version`.
- `ps auxww` no host e containers, com credenciais redigidas.
- `hermes cron list/status` no host e container Telegram.
- `docker logs --since 2h` do container Telegram.
- Telegram API `getMe` e `getWebhookInfo`, sem imprimir token.
- GitHub API release latest do Hermes upstream.

## Próximo passo seguro

Foi criado um post-check one-shot para 2026-05-11 09:15 UTC:

- Job: `Hermes release watch post-check`;
- ID: `1f60e374d0ba`;
- objetivo: verificar se o `Hermes release watch` executou/entregou após a janela esperada;
- escopo: read-only, sem alterar VPS/Docker/crons/secrets/produção.

Interpretação esperada:

- se `Hermes release watch` entregar relatório, manter observação;
- se não entregar, documentar falha e pedir aprovação para correção mínima;
- se Lucas quiser acelerar v0.12.0, preparar PR/plano técnico de imagem customizada antes de qualquer Docker action.
