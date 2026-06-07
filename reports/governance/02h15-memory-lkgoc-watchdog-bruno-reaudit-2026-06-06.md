# Reauditoria 02h15 memória + LKGOC watchdog vs Bruno

Data: 2026-06-06

## Pedido Lucas

Repensar o cron de compactação 02h15 e comparar com o padrão Bruno/OpenClaw, além de corrigir o fato de `[LK] Otimização de Coleções` poder responder e precisar ficar supervisionado por watchdog.

## Veredito

A arquitetura 01h → 02h → 02h15 → 02h30 está correta em intenção, mas o 02h15 ainda precisava de dois ajustes para ficar no padrão Bruno:

1. **Cobertura por roster real**, não por exceção histórica.
2. **Supervisão operacional do especialista**, não só memória documentada.

Padrão Bruno aplicado: agente não é só docs/profile; precisa de loop vivo `inbox → classificação → skill/worker mínimo → output/receipt → feedback → melhoria`.

## O que estava bom

- 02h15 é `no_agent`, `deliver=local`, silent-OK.
- Escreve receipt local em `reports/memory-hygiene/latest.json`.
- Faz backup antes de compactar.
- Não ativa provider externo, Mem0, Docker/VPS, Shopify/Tiny/GMC, nem produção.
- Agora varre todos os arquivos `profiles/*/memories/{MEMORY,USER}.md` existentes.

## O que estava abaixo do ideal

- O receipt não expunha explicitamente `coverage_missing_for_existing_memory`, então a pergunta “todos os profiles com boot memory têm template seguro?” dependia de inspeção externa.
- O watchdog global de gateways não incluía `lk-collection-optimizer`, embora o runtime watchdog já esperasse esse profile como obrigatório. Resultado: o runtime watchdog detectava ausência, mas o auto-heal não trazia o especialista de volta.
- O template default antigo ainda usava fraseamento de LKGOC como Growth, não como agente permanente independente.

## Correções executadas

### 1. 02h15 memory hygiene watchdog

Arquivo alterado: `/opt/data/scripts/hermes_memory_hygiene_watchdog.py`

- Corrigido template default para incluir `lk-collection-optimizer` como especialista independente.
- Corrigido LKGOC para fonte `areas/lk/sub-areas/collection-optimizer/` e peers Growth/Shopify.
- Adicionado bloco `auto_template_coverage` ao receipt:
  - `coverage_missing_for_existing_memory`
  - `existing_memory_files`
  - `templated_files`
  - `template_paths_without_current_file`

Verificação atual:

- `status=ok`
- `files_checked=24`
- `coverage_missing_for_existing_memory=[]`
- `near_saturation_count=0`
- `over_limit_count=0`
- `possible_secret_locator_count=0`
- stdout manual: vazio

### 2. LKGOC / `[LK] Otimização de Coleções` gateway watchdog

Arquivo alterado: `/opt/data/scripts/hermes_all_gateway_watchdog.py`

- Adicionado `lk-collection-optimizer` ao roster `EXPECTED` do watchdog global.
- Modo: `managed`.
- `HERMES_HOME=/opt/data/profiles/lk-collection-optimizer`.
- API/webhook forçados off.
- `HERMES_MAX_ITERATIONS=50`.
- Cópia fonte espelhada em `areas/operacoes/scripts/hermes_all_gateway_watchdog.py`.

Estado verificado:

- Gateway LKGOC vivo: `pid=6298`.
- Telegram: `connected`.
- API: `false`.
- Webhook: `false`.
- Watchdog global manual: stdout vazio.
- Runtime watchdog manual: stdout vazio.

## Decisão operacional

`[LK] Otimização de Coleções` agora está no nível:

- Documentado: sim.
- Configurado: sim.
- Conectado: sim.
- Supervisionado por watchdog: sim.
- Operante/auto-melhorando: próximo passo é provar com um caso real/receipt do próprio profile.

Não chamar ainda de “auto-melhorando completo” só porque o gateway está vivo. Bruno exige loop real.

## Melhor forma daqui para frente

- 02h15 deve continuar sendo só higiene/receipt local, não executor narrativo.
- 02h deve consumir o receipt e transformar gaps sistêmicos em auto-melhoria A0/A1.
- 02h30 deve reportar apenas decisão/exceção/materialidade para Lucas.
- Todo novo profile com boot memory precisa aparecer automaticamente em `auto_template_coverage`; se faltar template, vira alerta governável.
- Todo especialista que “pode responder” precisa estar em watchdog global ou marcado explicitamente como dormant/preparado.

## Escopo/segurança

Ações feitas:

- escrita local de scripts/docs/receipts;
- início local do gateway `lk-collection-optimizer` via watchdog global, com API/webhook off.

Ações não feitas:

- nenhum Docker/VPS/Traefik/compose/restart de container;
- nenhum Shopify/Tiny/GMC/Meta/Klaviyo/write externo;
- nenhum provider externo de memória;
- nenhum segredo impresso.
