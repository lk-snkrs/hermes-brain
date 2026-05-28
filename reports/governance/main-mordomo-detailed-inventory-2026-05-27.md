# Inventário detalhado — rotinas Main/Mordomo e adjacências

Data/hora: 2026-05-27 12:00 UTC  
Base: `cronjob(action='list')` + Brain docs read-only.  
Escopo: local/documental/read-only. Nenhum runtime, cron, gateway, Docker/VPS, produção, Shopify, Tiny, WhatsApp, e-mail, banco ou secret foi alterado.

## Resumo executivo

- Jobs vivos no scheduler: **21**.
- Delivery `local`: **18**.
- Delivery `origin`: **3**.
- `last_status != ok`: **0**.
- O ponto mais importante não é falha técnica; é **reconciliação de identidade**: alguns jobs ainda aparecem em docs como ativos/centrados no Main ou Mordomo, mas o live list já mostra um recorte mais enxuto.

## Leitura curta

O inventário atual separa em 4 grupos:

1. **Main/COO central legítimo** — manter.
2. **Mordomo e gateways de perfil** — manter, mas sem misturar com LK/Zipper por histórico.
3. **LK/Zipper/SPITI entregas vivas** — acompanhar por dono lógico, não por conveniência do runtime.
4. **Docs com sobra histórica** — rotinas que ainda aparecem no controle documental, mas não aparecem no scheduler vivo atual.

## 1) Main / COO central legítimo

### `749ee30b51eb` — Mesa COO diária Telegram
- **Owner lógico:** Operações / COO.
- **Runtime atual:** `/opt/data`.
- **Delivery:** `origin`.
- **Status:** **manter**.
- **Por quê:** é a fila executiva principal no Telegram.
- **Risco se mexer agora:** perder a superfície executiva mais útil; não há sinal de duplicidade grave por si só.

### `98478b820720` — Relatório Hermes diário 23h + 02h para Lucas
- **Owner lógico:** Operações / Hermes Brain.
- **Runtime atual:** `/opt/data`.
- **Delivery no live list:** `origin`.
- **Status:** **reconciliar**.
- **Por quê:** o cron-control-plane anterior já registrava esse job como `local`, mas o live list atual mostra `origin`.
- **Risco se mexer agora:** tocar delivery sem alinhar intenção pode reintroduzir ruído no Telegram ou duplicar a Mesa COO.
- **Nota:** esse é o principal item de divergência entre documentação e runtime vivo.

### `c1ce34b4449a` — Hermes multi-profile latency watchdog
- **Owner lógico:** Operações / monitoramento.
- **Runtime atual:** leitura local do scheduler.
- **Delivery:** `origin` por design de alerta.
- **Status:** **manter**.
- **Por quê:** watchdog de latência pode usar `origin` como canal de anomalia, não como recibo de sucesso.
- **Risco se mexer agora:** esconder alerta útil ou quebrar o canal de exceção.

## 2) Mordomo / intake pessoal

### `ac0b440e2643` — Mordomo Telegram gateway watchdog
- **Owner lógico:** Mordomo / Lucas pessoal.
- **Runtime atual:** `/opt/data/profiles/mordomo`.
- **Delivery:** `local`.
- **Status:** **manter**.
- **Por quê:** protege o gateway do perfil correto e não é, por si só, uma rotina de negócio LK/Zipper.
- **Risco se mexer agora:** perder observabilidade do canal pessoal e confundir falha de gateway com falha de conteúdo.

### `Mordomo` em docs com herança histórica
- **Doc pressure point:** várias rotinas antigas ainda citam Mordomo como executor histórico de fluxos Zipper/LK WhatsApp.
- **Status:** **marcar legado**, não apagar.
- **Regra:** se a rotina é Zipper/LK por identidade, o Mordomo só deve ser intake/rascunho quando isso estiver explicitamente documentado.

## 3) LK / negócio vivo no scheduler

### `7c688553e293` — LK Daily Sales Brief read-only mandatory delivery
- **Owner lógico:** LK Ops / Comercial / Atendimento.
- **Runtime atual:** live scheduler.
- **Delivery:** `local`.
- **Status:** **manter**.
- **Por quê:** briefing diário read-only é coerente com o escopo operacional.
- **Risco se mexer agora:** o relatório deixar de existir ou ganhar ruído de decisão sem fonte.

### `953b9055458e` — LK Weekly CEO Review read-only mandatory delivery
- **Owner lógico:** LK Ops / Comercial / Atendimento.
- **Runtime atual:** live scheduler.
- **Delivery:** `local`.
- **Status:** **manter**.
- **Por quê:** revisão semanal read-only faz sentido como execução de suporte.
- **Risco se mexer agora:** virar daily duplicado sem insight adicional.

### `c3bb587519d2` — LK Pulso Comercial 16h read-only delivery
- **Owner lógico:** LK Ops / Comercial / Atendimento.
- **Runtime atual:** live scheduler.
- **Delivery:** `local`.
- **Status:** **manter**.
- **Por quê:** é um pulso comercial local, não um write externo.
- **Risco se mexer agora:** duplicação de briefings se for confundido com daily sales.

### `e3279babbc4a` — LK 09h previous-day sales report external delivery
- **Owner lógico:** LK Ops / Comercial / Atendimento.
- **Runtime atual:** live scheduler.
- **Delivery:** `local`.
- **Status:** **manter com cautela**.
- **Por quê:** o nome fala “external delivery”, mas o live list atual mostra `local`.
- **Risco se mexer agora:** introduzir entrega externa sem escopo/recebimento claro.
- **Ação segura:** reconciliação do naming contra o comportamento vivo.

### `a2ead305eab2` — LK 19h30 physical store close external delivery
- **Owner lógico:** LK Ops / Comercial / Atendimento.
- **Runtime atual:** live scheduler.
- **Delivery:** `local`.
- **Status:** **manter com cautela**.
- **Por quê:** o nome sugere entrega externa, mas o delivery vivo está local.
- **Risco se mexer agora:** abrir um canal externo sem necessidade.

## 4) Zipper / leitura, sinal e documentação

### `71b147362ec1` — Zipper Gmail style learning refresh
- **Owner lógico:** Zipper OS / documental-read-only.
- **Runtime atual:** live scheduler.
- **Delivery:** `local`.
- **Status:** **manter**.
- **Por quê:** é um refresh de estilo/leitura, não um write comercial.
- **Risco se mexer agora:** trocar aprendizado por ação externa.

### `357d40a5863e` — Zipper OS vendas 09h WhatsApp/email
- **Owner lógico:** Zipper OS.
- **Runtime atual:** live scheduler.
- **Delivery:** `local`.
- **Status:** **manter com cautela**.
- **Por quê:** o live job existe, mas Zipper continua sem runtime dedicado; isso precisa continuar sendo tratado como fluxo limitado/guardrailed.
- **Risco se mexer agora:** contato externo fora do guardrail ou mistura com SPITI/LK.

### Zipper em docs com histórico de Main/Mordomo
- **Doc pressure point:** várias rotinas antigas de Zipper ainda aparecem como hospedadas no Main/Mordomo.
- **Status:** **marcar legado**.
- **Regra:** sem profile Zipper dedicado, manter como documental/read-only e aprovar caso a caso para qualquer comunicação externa.

## 5) SPITI / perfil ativo, sem cron local consolidado

### `663e3e6a148c` — SPITI Telegram gateway watchdog
- **Owner lógico:** SPITI OS.
- **Runtime atual:** `/opt/data/profiles/spiti`.
- **Delivery:** `local`.
- **Status:** **manter**.
- **Por quê:** é watchdog de superfície, coerente com o runtime ativo.
- **Risco se mexer agora:** perder sinal de saúde do canal.

### SPITI sem cron local consolidado
- **Doc pressure point:** cron-control-plane e matriz apontam que a ausência de cron local consolidado deve ser uma escolha explícita ou pendência documentada.
- **Status:** **manter / declarar escolha**.
- **Risco se mexer agora:** inventar automação sem necessidade ou criar ruído operacional.

## 6) Watchdogs centrais / saúde do runtime

### `edd06fe19397` — Hermes runtime + cron watchdog no_agent
- **Owner lógico:** Operações / infraestrutura interna.
- **Delivery:** `local`.
- **Status:** **manter**.
- **Risco se mexer agora:** cegar o watchdog base de runtime.

### `4bb4e2223fd3` — Hermes compression failure self-heal watchdog
- **Owner lógico:** Operações / runtime safety.
- **Delivery:** `local`.
- **Status:** **manter**.
- **Risco se mexer agora:** perder auto-recuperação controlada.

### `d03fa04e1188` — Hermes Brain Operating Layer structural watchdog
- **Owner lógico:** Operações / Brain.
- **Delivery:** `local`.
- **Status:** **manter**.
- **Risco se mexer agora:** reduzir a cobertura estrutural do Brain.

### `d9badcd83411` — Hermes Brain strict-runtime guard watchdog
- **Owner lógico:** Operações / segurança runtime docs.
- **Delivery:** `local`.
- **Status:** **manter**.
- **Risco se mexer agora:** enfraquecer o guard de instruções vivas perigosas.

### `2404c0766d33` — Hermes Brain Runtime Truth Reconciler
- **Owner lógico:** Operações / reconciliação.
- **Delivery:** `local`.
- **Status:** **manter**.
- **Risco se mexer agora:** perder a ponte entre doc e runtime vivo.

## 7) Docs vivos x live scheduler: sobras históricas que precisam reconciliação

Esses itens aparecem em documentação recente do control-plane, mas **não apareceram no `cronjob list` vivo desta rodada**. Não significa necessariamente que estão errados; significa que hoje estão **historicamente documentados, mas não confirmados como vivos**.

### Itens a reconciliar

- `c358f8f56a26` — Pixel AI Hub / Brainzinho daily learning scan.
  - **Status:** histórico/legado até prova viva em outro scheduler.
  - **Risco:** owner/canal ainda pode estar sendo atribuído ao executor técnico errado.

- `71b2636add5d` — LK WhatsApp Hermes responder watchdog.
  - **Status:** não visto no live list desta rodada.
  - **Risco:** documentação pode estar adiantada em relação ao runtime.

- `a5d7a392eed9` — LK WhatsApp Hermes responder regression watchdog.
  - **Status:** não visto no live list desta rodada.
  - **Risco:** idem acima.

- `d4c26da4cd48` — LK GMC Review read-only mandatory delivery.
  - **Status:** não visto no live list desta rodada.
  - **Risco:** a doc ainda o trata como vivo; precisa reconciliação antes de qualquer decisão sobre manutenção/remoção.

## 8) Diagnóstico final por tipo de ação

### Manter
- Mesa COO diária Telegram.
- Gateway watchers de Mordomo, LK Growth e SPITI.
- Watchdogs centrais do Brain/runtime.
- LK Daily Sales Brief.
- LK Weekly CEO Review.
- LK Pulso Comercial 16h.
- Zipper Gmail style learning refresh.
- SPITI Telegram gateway watchdog.

### Manter com cautela / reconciliação de identidade
- `98478b820720` — Relatório Hermes diário 23h + 02h.
- `e3279babbc4a` — LK 09h previous-day sales report external delivery.
- `a2ead305eab2` — LK 19h30 physical store close external delivery.
- `357d40a5863e` — Zipper OS vendas 09h WhatsApp/email.

### Marcar legado
- Rotas Zipper ainda mencionadas como hospedadas no Mordomo/Main.
- Pixel AI Hub / Brainzinho enquanto não houver prova viva no runtime correto.
- Jobs/documentos LK WhatsApp e GMC que não apareceram no scheduler vivo desta rodada.

### Ação posterior necessária
- Fazer uma rodada de reconciliação específica para os itens documentados mas não vivos, antes de qualquer migração ou exclusão.

## Próximo passo seguro

Criar uma **tabela de reconciliação final** com estas colunas:

- rotina;
- presente no live scheduler?
- owner lógico;
- runtime atual;
- status final;
- ação segura recomendada.

Essa próxima rodada ainda deve ser read-only. A migração real continua exigindo packet separado.
