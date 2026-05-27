# Dashboard — coerência operacional Hermes

Data: 2026-05-26  
Escopo: Brain/local/read-only. Sem runtime, cron ou produção.

## Status geral

- Organograma macro: correto.
- LK Shopify: agora explícito como nó próprio do LK OS.
- P0: matriz + handoff/receipt documentados.
- P1: profiles dormentes/especialistas classificados e contratos LK Shopify/LK Trends reforçados.
- P2: preparado como pacote de aprovação, não executado.

## Status por frente

### Hermes Geral
- Estado: ativo.
- Papel: COO/orquestrador central.
- Atenção: não virar executor universal por conveniência.

### Mordomo
- Estado: ativo.
- Papel: intake pessoal e follow-ups.
- Atenção: rotinas LK/Zipper dentro do Mordomo exigem dono lógico e handoff.

### LK Ops
- Estado: profile preparado, gateway não observado como ativo nesta leitura.
- Papel: atendimento, estoque, preço, disponibilidade, vendas operacionais.
- Atenção: Tiny é fonte de estoque; Shopify é superfície.

### LK Growth
- Estado: ativo.
- Papel: SEO/GEO/CRO/GMC/analytics/conteúdo.
- Atenção: D+7 reviews precisam classificação de delivery para reduzir ruído.

### LK Shopify
- Estado: profile preparado/documentação reforçada.
- Papel: produto/upload/coleções/superfície Shopify/preview.
- Atenção: nenhum Shopify/Tiny write sem aprovação escopada, snapshot, readback, receipt e rollback.

### LK Trends
- Estado: profile preparado/documentação reforçada.
- Papel: tendências, sourcing intelligence e radar de mercado.
- Atenção: oportunidade não é autorização de compra/negociação.

### SPITI
- Estado: ativo, sem cron registry local observado.
- Papel: Hub, obras, leilões, clientes, CRM/admin, análises verificáveis.
- Atenção: documentar se ausência de crons é escolha ou pendência.

### Zipper
- Estado: documental/read-only.
- Papel: CRM/Main, vendas, artistas, colecionadores, enquiries.
- Atenção: runtime próprio só com gatilho objetivo de volume/risco/canal.

### Profiles auxiliares
- Estado: dormentes/read-only.
- Profiles: `brain-process`, `hermes-ops-readonly`, `lk-analyst-readonly`, `lk-content-reviewer`.
- Atenção: não expor/ativar sem caso de uso claro.

## Gaps remanescentes

1. Classificar linha-a-linha quais crons de Main/Mordomo devem permanecer, migrar futuramente ou virar silent-OK/local.
2. Validar no runtime, com aprovação separada, se profiles preparados devem ser ativados.
3. Definir gatilho formal para Zipper runtime.
4. Decidir postura de SPITI: sem crons próprios por escolha ou backlog.
5. Reduzir ruído dos D+7 Growth sem perder decisões importantes.

## Próximo bloco seguro

Somente local/read-only:

- manter esta matriz como fonte de consulta;
- usar o ledger diário de handoff;
- preparar pacotes de aprovação por lote quando houver runtime/cron.

Bloqueado sem aprovação escopada:

- restart de gateway;
- criação/pausa/migração de cron;
- ativação de bot/profile;
- Docker/VPS/Traefik;
- qualquer write externo.
