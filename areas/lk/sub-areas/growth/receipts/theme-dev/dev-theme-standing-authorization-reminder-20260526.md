# Correção operacional — autorização permanente para tema dev LK

Data: 2026-05-26
Contexto: Lucas corrigiu a execução de LK Growth após o agente tratar ajuste em `lk-new-theme/dev` como se precisasse de aprovação adicional.

## Regra confirmada

Lucas já autorizou que ajustes reversíveis no tema dev Shopify da LK podem ser aplicados diretamente pelo Hermes/LK Growth sem pedir aprovação a cada vez.

Produção continua bloqueada sem aprovação explícita no turno atual.

## Aplicação prática

Quando o pedido envolver coleção/PDP/theme em `lk-new-theme/dev`:

- executar backup/readback antes do write;
- aplicar patch no tema dev;
- verificar DOM + screenshot/vision;
- devolver preview link com cache-busting;
- não pedir aprovação intermediária para o dev;
- não publicar produção sem aprovação explícita.

## Erro reconhecido

Neste fluxo Onitsuka/Samba, o agente deveria ter aplicado a correção no dev theme imediatamente após Lucas dizer `Seguir`, em vez de parar em approval packet local.

## Próxima execução esperada

Aplicar diretamente no `lk-new-theme/dev`:

- remover `Sinal editorial` de Onitsuka e Samba;
- padronizar topo visual com descrição + fotos/moodboard;
- manter produtos primeiro;
- validar visualmente antes de reenviar preview.
