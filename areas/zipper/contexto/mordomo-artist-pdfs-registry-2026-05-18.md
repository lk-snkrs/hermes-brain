# Zipper — Registro de PDFs comerciais de artistas

Atualizado: 2026-05-18

## Fonte de verdade operacional

- Supabase CRM/Main: tabela `artist_pdfs`.
- Colunas confirmadas por OpenAPI/PostgREST: `id`, `artist_name`, `pdf_filename`, `pdf_base64`, `created_at`, `updated_at`.
- Cópia local operacional: `/opt/data/zipper_artist_pdfs/`.
- Manifest local: `/opt/data/zipper_artist_pdfs/manifest.json`.

## PDFs salvos em 2026-05-18

- Romy Pocztaruk — `Mega Hair | Romy Pocztaruk.pdf`
- Laura Villarosa — `Laura Villarosa - Obras Disponíveis.pdf`
- Nina Pandolfo — `Nina Pandolfo — Obras Disponíveis.pdf`
- Ivan Grilo — `Ivan Grilo — Obras Disponíveis.pdf`
- Miguel Penha Chiquitano — `Miguel Penha Chiquitano - Obras Disponíveis.pdf`
- João Castilho — `João Castilho — Obras Disponíveis.pdf`
- Ian Salamente — `Ian Salamente — Obras Disponíveis.pdf`
- Daniel Mullen — `Daniel Mullen - Obras Disponíveis - ZPR.pdf`
- Fábio Baroli — `Fábio Baroli - Zipper Galeria.pdf`
- Rodrigo Braga — `Rodrigo Braga - Seleção de Obras Disponíveis.pdf`
- Rizza — `Rizza — Seleção Obras Disponíveis.pdf`
- William Santos — `William Santos — Obras Disponíveis.pdf`
- Adriana Duque — `Adriana Duque - Seleção de Obras Disponíveis.pdf`
- Flávia Junqueira — `Flávia Junqueira — Seleção Obras Disponíveis.pdf` — recebido via WhatsApp Hermes em 2026-05-18; cópia local validada em `/opt/data/zipper_artist_pdfs/flavia-junqueira/flavia-junqueira__flavia-junqueira-selecao-obras-disponiveis__9fe96ad7c960.pdf`. Observação operacional: WhatsApp deve enviar PDF sozinho, sem intro/caption, salvo aprovação explícita. Para e-mails, usar o assunto/título `Flávia Junqueira — Obras Disponíveis`. Supabase `artist_pdfs`: pendente de confirmação/inserção por timeout ao gravar payload grande em base64.

## Regras para próximos uploads

1. Receber PDF do Telegram em `/opt/data/profiles/mordomo/cache/documents/`.
2. Inferir artista pelo nome do arquivo:
   - `Título | Artista.pdf` → artista depois de `|`.
   - `Artista - Obras Disponíveis.pdf` → artista antes do sufixo comercial.
   - `Artista — Seleção de Obras Disponíveis.pdf` → artista antes do sufixo comercial.
3. Salvar cópia local em `/opt/data/zipper_artist_pdfs/{slug}/`.
4. Inserir/atualizar `artist_pdfs` no Supabase com `artist_name`, `pdf_filename`, `pdf_base64`.
5. Verificar readback por `id`, `artist_name`, `pdf_filename`.
6. Não enviar PDF a cliente sem aprovação explícita do turno atual para destinatário e payload.

## Observação

A tabela atual guarda o PDF em base64 diretamente. Para escala e versionamento futuro, considerar migrar para Supabase Storage/Drive com colunas adicionais como `sha256`, `file_size`, `version`, `active`, `source`, `validated_by`, `validated_at` e `expires_at`.
