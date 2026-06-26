# LK Trend — runtime handoff

Status: correção de roteamento aprovada em conversa.
Data: 2026-05-26.

## Correção

Lucas apontou corretamente que a continuidade operacional do LK Trend não deve ficar como saída do Hermes Geral por conveniência.

## Fronteira correta

### Hermes Geral

Responsável por:

- governança;
- desenho da rotina;
- documentação local;
- roteamento;
- pacotes de aprovação;
- auditoria de segurança;
- manter o Brain como fonte de verdade.

Não deve ser o executor recorrente dos relatórios operacionais do LK Trend quando houver perfil especialista disponível.

### LK Trend / LK Growth

Responsável por:

- gerar o relatório semanal;
- montar fila de oportunidades;
- preparar previews internos de conteúdo;
- manter separação conteúdo vs compra/reposição;
- consultar fontes LK read-only conforme guardrails;
- devolver ao Lucas no Telegram como saída especialista, com decisão limpa.

Lucas confirmou que o correto é criar o especialista LK Trend. O perfil local `lk-trends` foi preparado em `/opt/data/profiles/lk-trends`; `lk-growth` fica como executor de conteúdo/SEO/GEO quando o LK Trend fizer handoff, e `lk-shopify` permanece apenas para Shopify/catalog/theme/GMC quando a oportunidade virar preview técnico.

## Regra operacional

1. Hermes Geral pode preparar/atualizar a especificação e o handoff.
2. A primeira execução real pode ser registrada como dry-run/governança se feita aqui.
3. Próximas edições do LK Trend devem ser executadas pelo perfil especialista, preferencialmente em Telegram/canal próprio.
4. Se for criado um novo bot/profile `LK Trends`, isso é alteração de runtime/gateway e precisa de aprovação técnica separada.
5. Publicação, envio externo, compra, fornecedor, Shopify/Tiny/Merchant/Klaviyo writes continuam bloqueados sem aprovação explícita.

## Próximo handoff

Entrada para o especialista:

- especificação: `areas/lk/rotinas/lk-trend-weekly-v1-2026-05-26.md`;
- template: `areas/lk/rotinas/templates/lk-trend-weekly-v1.md`;
- primeira edição: `areas/lk/rotinas/lk-trend-weekly-report-v1-2026-05-26.md`;
- fila JSON: `areas/lk/rotinas/lk-trend-opportunity-queue-v1-2026-05-26.json`.

Pedido limpo para o especialista:

> Continuar o LK Trend dentro do perfil especialista. Transformar os 3 P1 de conteúdo da primeira edição em previews internos, sem publicar/enviar, mantendo bloqueio para compra/reposição e qualquer write externo.

## Decisão pendente

Escolher o runtime:

- ativar o Telegram do `lk-trends` com token dedicado e aprovação de runtime/gateway;
