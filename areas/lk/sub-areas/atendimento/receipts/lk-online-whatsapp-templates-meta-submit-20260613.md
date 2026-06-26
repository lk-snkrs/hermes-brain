# Receipt — LK Online WhatsApp templates enviados para Meta

- Data/hora: 2026-06-13T17:06:20.314892+00:00
- Agente/profile/cron: lk-ops
- Empresa/área: LK / atendimento / WhatsApp Business API
- Responsável humano: Lucas Cimino
- Pedido original: Publicar todos os templates aprovados desta régua no WhatsApp Business API/Meta, sem envio a clientes.
- Classificação: external-write
- Fontes usadas:
- Aprovação explícita no Telegram: Publicar todos os templates aprovados desta régua; Doppler lc-keys/prd values_printed=false; Chatwoot LK WhatsApp inbox id 2; Meta Graph API v23; Shopify read-only para imagem de exemplo.
- O que foi feito:
- Submetidos à Meta via Graph API com HEADER IMAGE, BODY e BUTTONS os templates: lk_online_pedido_enviado_v1, lk_online_pedido_entregue_v1, lk_online_avaliacao_compra_v1, lk_online_pagamento_pendente_v1, lk_online_pagamento_nao_aprovado_v1, lk_online_troca_devolucao_solicitada_v1. Templates com Falar com a LK foram ajustados para QUICK_REPLY porque Meta bloqueou URL direta para WhatsApp.
- Output/artefato:
- Todos os 6 templates aparecem no readback Chatwoot após sync: status PENDING, idioma pt_BR, components_count=3. Categorias: avaliação=MARKETING; demais=UTILITY. Meta IDs: enviado 1376158064334550; entregue 27296934356595915; avaliação 2285160415225282; pagamento pendente 1973476630197909; pagamento não aprovado 3499409256899532; troca/devolução 1726724895339530.
- Aprovação: Aprovado por Lucas no Telegram para publicar todos os templates aprovados desta régua.
- Envio/publicação: Nenhuma mensagem WhatsApp enviada; nenhuma automação ativada; apenas submissão de templates para aprovação Meta e sync Chatwoot.
- Writes externos: Meta/WABA message_templates create: 6 templates criados/submetidos. Chatwoot WhatsApp templates sync: HTTP 200. Sem Shopify/Tiny/Klaviyo/Judge.me writes.
- Riscos/bloqueios: Todos ainda PENDING, dependem de aprovação Meta. Botões Falar com a LK estão como QUICK_REPLY, não URL para WhatsApp, porque Meta não permite links diretos para WhatsApp em botões. URLs dinâmicas de avaliação/pagamento usam padrão posicional/sufixo e exigem mapping correto na camada de envio.
- Rollback/mitigação: Templates Meta não foram enviados a clientes; se reprovados ou se a copy/CTA mudar, criar nova versão v2 e não ativar a v1. Não ativar automações até status APPROVED e novo approval de envio/fluxo.
- Próximos passos: Aguardar revisão Meta; depois readback de status APPROVED/REJECTED, validar variáveis/mapping de envio e só então pedir aprovação separada para ativar automações ou enviar testes.
- Onde foi documentado no Brain: Receipt criado via hermes_memory_os_receipt_writer; valores de secrets não impressos; values_printed=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
