# Receipt — LK Finance local PDF/OCR stack installed and validated

- Data/hora: 2026-06-18T12:34:21.953599+00:00
- Agente/profile/cron: Hermes Geral
- Empresa/área: LK / Finance
- Responsável humano: Hermes
- Pedido original: Habilitar leitura local de PDFs financeiros/faturas no perfil lk-finance sem envio a serviços externos.
- Classificação: local-write
- Fontes usadas:
- Pedido direto de Lucas no Telegram em 2026-06-18; execução local apt-get e validação em /tmp/lk-finance-ocr-validate-20260618T123333Z.
- O que foi feito:
- Instalados pacotes poppler-utils, tesseract-ocr, tesseract-ocr-por, mupdf-tools, qpdf e ocrmypdf via apt-get; validados binários no PATH e fluxo local pdftotext, pdftoppm, tesseract -l por, qpdf, mutool e ocrmypdf com fixture não sensível.
- Output/artefato:
- Binários disponíveis em /usr/bin; idiomas Tesseract eng, osd e por; fluxo PDF local para imagem e OCR validado; nenhum PDF financeiro real processado.
- Aprovação: Ação local no ambiente Linux/Hermes solicitada explicitamente por Lucas; sem serviços externos e sem dados sensíveis.
- Envio/publicação: Nenhum envio externo; validação local somente.
- Writes externos: 0
- Riscos/bloqueios: Ferramentas instaladas no sistema atual; se lk-finance rodar em outro container/host, repetir instalação nesse runtime. Não persistir faturas/textos OCR em logs públicos.
- Rollback/mitigação: Remover pacotes via apt-get remove/purge se necessário; nenhum dado financeiro real criado.
- Próximos passos: Lucas pode reenviar/testar a fatura Itaú de Maio para categorização local dos gastos da LK.
- Onde foi documentado no Brain: areas/lk/sub-areas/finance/receipts/20260618T123421Z-local-pdf-ocr-stack-installed.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
