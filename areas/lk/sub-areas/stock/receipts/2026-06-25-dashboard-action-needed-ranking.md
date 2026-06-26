# Receipt — LK Stock dashboard ação necessária ranqueada

- Data/hora: 2026-06-25T16:01:49.624770+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock OS
- Responsável humano: lk-stock
- Pedido original: Lucas apontou que a aba Ação necessária estava mostrando produto P3/sem prioridade como Calça Dane-se Touch Linha Verde no topo, o que não fazia sentido operacional.
- Classificação: external-write
- Fontes usadas:
- Comentário e screenshot de Lucas; código src/public/dashboard-utils.js, src/index.js e src/public/index.html; API produção /api/estoque/detail?quickFilter=action-needed; CDP Chromium; npm test; Impeccable detect.
- O que foi feito:
- Criado quickFilter action-needed como padrão; P3/NO_ACTION/score0/units0 fica fora da fila; ranking força P0-P1-P2 por prioridade operacional; backend/frontend compartilham compareActionNeeded; timeout Stock OS default aumentado para 60s para evitar erro em cache miss; container lk-estoque-web reiniciado com aprovação de Lucas.
- Output/artefato:
- Commit 54afce4 em feat/stock-os-api-adapter; produção HTTP 200; API action-needed totalFiltered 986 e primeiros itens P0/P1; Calça Dane-se ausente dos primeiros resultados/render inicial; npm test 39/39; Impeccable detect [].
- Aprovação: Aprovação escopada explícita de Lucas para corrigir dashboard e aprovação adicional no Telegram para reiniciar agora o container lk-estoque-web. Escopo: UI/ranking do dashboard Stock OS; sem Tiny/Shopify/Notion/customer write.
- Envio/publicação: Telegram final para Lucas
- Writes externos: GitHub branch feat/stock-os-api-adapter push; produção/container lk-estoque-web /app/src atualizado e reiniciado. Tiny write 0; Shopify write 0; Notion write 0; contato externo 0.
- Riscos/bloqueios: Mudança de ranking e restart curto do dashboard; mitigado com backup, testes, detector, API smoke e CDP.
- Rollback/mitigação: Backups em .hermes/backups/action-needed-ranking-20260625T155053Z, /opt/data/profiles/lk-stock/backups/lk-estoque-web-action-needed-ranking-20260625T155216Z e /opt/data/profiles/lk-stock/backups/lk-estoque-web-action-needed-restart-20260625T155624Z; rollback via git revert 54afce4 e restart do container.
- Próximos passos: Lucas revisar visualmente; se quiser, próximo passe pode ajustar labels/explicação da fila.
- Onde foi documentado no Brain: Skill lk-stock atualizada com regra Action-needed ranking rule.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
