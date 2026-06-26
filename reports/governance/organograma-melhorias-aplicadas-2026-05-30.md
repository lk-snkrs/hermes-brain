# Relatório — Melhorias aplicadas no organograma vivo Hermes/Amora

Data: 2026-05-30
Pedido: melhorar o que ainda faltava no organograma após a auditoria documental.

## Escopo executado

Foram aplicadas apenas melhorias locais/documentais no Brain. Nenhuma mudança foi feita em runtime, cron scheduler, gateway, Docker, VPS, Traefik, Shopify, Tiny, CRM, WhatsApp ou qualquer sistema externo.

## Melhorias feitas

### 1. Matriz de crons por dono lógico

Criado:

- `empresa/contexto/matriz-crons-dono-logico-status.md`

Resolve a lacuna de dono lógico vs runtime atual. Agora está explícito que:

- registry do cron não define dono final;
- Main e Mordomo podem hospedar rotina por histórico;
- LK Ops/LK Shopify/LK Trends/SPITI sem registry próprio não é erro automático;
- migração de cron exige inventário, rollback e aprovação quando mudar runtime/schedule/delivery/side effect.

### 2. Critérios de promoção de profiles auxiliares e Zipper

Criado:

- `empresa/contexto/criterios-promocao-agentes-auxiliares.md`

Resolve a lacuna de profiles com token mas sem runtime esperado. Classificações documentadas:

- `brain-process`: governança/documentação local, prepared/read-only;
- `hermes-ops-readonly`: operações Hermes read-only;
- `lk-analyst-readonly`: análise LK read-only/experimental;
- `lk-content-reviewer`: reviewer de conteúdo LK read-only/experimental;
- Zipper: documental/read-only até gatilho objetivo.

Regra fixada: token/profile/pasta não promove agente automaticamente.

### 3. Rotina de revisão do organograma vivo

Criado:

- `areas/operacoes/rotinas/revisao-organograma-vivo-amora-bruno.md`

Resolve a lacuna de maturidade ritual. Define quando revisar, checklist por agente, runtime truth, dono lógico, handoff, silent-OK e outputs obrigatórios da revisão.

### 4. Matriz de agentes atualizada

Atualizado:

- `empresa/contexto/matriz-agentes-profiles-bots-crons-status-2026-05-26.md`

Melhorias:

- Mordomo deixou de aparecer como “ajustar” genérico e virou “correto como Mordomo; pendente classificar rotinas históricas”.
- LK Ops virou “correto como dono lógico; pendência de inventário/migração opcional de crons”.
- LK Trends virou “correto; fronteira documentada com Growth/Ops”.
- Zipper virou “correto documental/read-only”.
- Auxiliares agora apontam para a política de promoção.

### 5. Organograma canônico atualizado

Atualizado:

- `empresa/contexto/organograma-agentes-hermes.md`

Melhorias:

- adicionadas as novas fontes canônicas;
- lacunas reescritas de forma mais objetiva;
- SPITI sem cron próprio tratado como escolha segura até ritual aprovado;
- Zipper com critérios de promoção em arquivo próprio.

## Estado depois das melhorias

O organograma agora tem:

- estrutura de agentes;
- matriz de roteamento;
- matriz agente/profile/bot/cron/status;
- matriz cron/dono lógico/status;
- critérios de promoção para auxiliares/Zipper;
- rotina de revisão viva;
- handoff/receipt já existentes;
- watchdog global dos gateways anotado.

## Pendências restantes

Não há pendência documental crítica. Restam apenas decisões operacionais que exigem aprovação futura se Lucas quiser executar:

1. migrar crons históricos de Main/Mordomo para perfis especialistas;
2. criar crons próprios para LK Ops/LK Shopify/LK Trends/SPITI;
3. promover Zipper ou auxiliares para runtime operacional;
4. mudar delivery/schedule de rotinas.

Essas ações não foram feitas porque seriam runtime/cron/produção, não simples documentação.
