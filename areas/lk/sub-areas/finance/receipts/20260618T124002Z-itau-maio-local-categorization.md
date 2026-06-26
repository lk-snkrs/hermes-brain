# Receipt — Itaú Maio local categorization processed

- Data/hora: 2026-06-18T12:40:03.021157+00:00
- Agente/profile/cron: Hermes Geral
- Empresa/área: LK / Finance
- Responsável humano: Hermes
- Pedido original: Categorizar localmente a fatura Itaú de Maio enviada por Lucas para gastos da LK.
- Classificação: read-only
- Fontes usadas:
- PDF recebido no Telegram e salvo em cache local; extração local com pdftotext.
- O que foi feito:
- Extraído texto localmente, identificados 88 lançamentos de Maio e gerado resumo por categoria; OCR externo não usado.
- Output/artefato:
- Total de compras de Maio: R$ 56.528,25; provável operacional/LK: R$ 51.174,66; revisar/pessoal: R$ 5.353,59. Relatório local: /tmp/lk-itau-current/relatorio_fatura_itau_maio_lk_sanitizado.md
- Aprovação: Processamento local/read-only de documento enviado por Lucas; sem serviços externos.
- Envio/publicação: Nenhum envio externo; somente resposta Telegram e artefatos locais temporários.
- Writes externos: 0
- Riscos/bloqueios: Documento financeiro sensível; não salvar cartão/conta/CPF/CNPJ em logs públicos; manter artefatos locais restritos.
- Rollback/mitigação: Remover artefatos temporários em /tmp/lk-itau-current e cache do documento se Lucas solicitar.
- Próximos passos: Lucas revisar categorias marcadas como revisar/pessoal antes de contabilização final.
- Onde foi documentado no Brain: areas/lk/sub-areas/finance/receipts/20260618T124002Z-itau-maio-local-categorization.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
