# Rotina — Evolution / WhatsApp Approval Flow

Objetivo: garantir que qualquer envio via Evolution API/WhatsApp só ocorra com preview e aprovação de Lucas.

## Integração

- Doc: `empresa/integracoes/evolution.md`.
- Secrets: `EVOLUTION_API_URL`, `EVOLUTION_API_KEY`.
- Negócios: LK, Zipper e SPITI conforme número/instância configurada.

## Permissões

- Read-only: checar status de instância, conexão e metadados sem enviar mensagem.
- Write: criar draft/local de mensagem é permitido.
- External-send: qualquer envio, áudio, imagem, template ou contato exige preview e aprovação Lucas.
- Admin/destructive: conectar/desconectar instância, trocar webhook, apagar sessão ou mexer em produção exige aprovação explícita.

## Fluxo obrigatório antes de enviar

1. Identificar negócio, público, destinatário e motivo.
2. Consultar dados vivos necessários e registrar fonte.
3. Criar mensagem em draft com tom adequado ao negócio.
4. Enviar preview para Lucas no Telegram.
5. Aguardar aprovação explícita.
6. Só então executar envio.
7. Registrar resultado e eventuais erros.

## Bloqueios

- Não enviar mensagem por inferência.
- Não disparar massa/campanha sem segmentação, preview e aprovação.
- Não contatar cliente/colecionador se houver incerteza material sobre dado de pedido, obra ou lance.
