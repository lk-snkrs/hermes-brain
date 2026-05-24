# Caso — Lead arquiteta: Anna Campos / Flávia Junqueira

Data: 2026-05-18
Origem: e-mail encaminhado por Helô Goes / Zipper Galeria
Assunto: `Arquiteta Whatsapp — Flávia Junqueira`
Status: PDF enviado por WhatsApp e e-mail em 2026-05-18 — número da Anna confirmado correto por Lucas; aguardando resposta

## Resumo operacional

Helô encaminhou contato de uma arquiteta com interesse em obras disponíveis da Flávia Junqueira.

- Lead: Anna Campos
- Perfil informado: arquiteta
- Artista de interesse: Flávia Junqueira
- Contato: telefone e e-mail informados no e-mail original; PII não reproduzida integralmente nesta nota.
- Destinatário visível no encaminhamento: Osmar Santos + 1
- Anexo visível: 1 screenshot/anexo relacionado ao caso

## Leitura estratégica

Este é um lead comercial Zipper de boa qualidade porque:

1. O interesse é explícito: obras disponíveis de Flávia Junqueira.
2. O canal veio por pessoa interna da galeria, não por ruído/newsletter.
3. Perfil arquiteta sugere possível compra para cliente/projeto, com chance de relacionamento recorrente.
4. Flávia Junqueira tem forte histórico comercial recente na Zipper.

## Dados internos relevantes

Consulta read-only já existente sobre Flávia Junqueira:

- Últimos 12 meses: 78 linhas de venda; 65 contatos distintos; valor total aproximado R$ 3,251,000.00.
- Origem `Arquiteto`: 11 vendas no período.
- Menções em conversas: 170 mensagens; menções a PDF/proposta: 102 mensagens.
- Sinais negativos/desfit registrados no protótipo: 0.

## PDF validado

O PDF comercial da Flávia Junqueira foi recebido pelo WhatsApp do Hermes e validado localmente:

- Arquivo/catálogo validado: `Flávia Junqueira — Seleção Obras Disponíveis.pdf`
- Correção de Lucas: `Flávia Junqueira — Obras Disponíveis` era correção do **título/assunto do e-mail**, não do nome do PDF.
- Cópia local validada: `/opt/data/zipper_artist_pdfs/flavia-junqueira/flavia-junqueira__flavia-junqueira-selecao-obras-disponiveis__9fe96ad7c960.pdf`
- Tamanho: 28,092,746 bytes (~27 MB)
- Páginas: 41
- Validação textual: contém `FLÁVIA JUNQUEIRA` e `OBRAS DISPONÍVEIS`.
- Manifest local atualizado.
- Supabase `artist_pdfs`: pendente de confirmação/inserção por timeout ao gravar payload grande em base64.

Houve ação externa em 2026-05-18 por aprovação de Lucas; correções operacionais registradas abaixo para envios futuros.

## Próximos passos recomendados

1. Registrar a lead no CRM Zipper como interesse em Flávia Junqueira.
2. Confirmar se a seleção recebida é a versão comercial atual para envio externo.
3. Resolver a persistência no Supabase `artist_pdfs` para PDFs grandes ou manter envio a partir da cópia local validada.
4. Preparar resposta curta e elegante por WhatsApp/e-mail, com tom B2B para arquiteta.
5. Se Lucas aprovar o contato, enviar pelo canal mais apropriado e registrar `proposal_event`/log.
6. Agendar follow-up em 2 dias úteis se não houver resposta.

## Regra corrigida — WhatsApp para PDFs Zipper

Para envio de PDF/catálogo via WhatsApp, o arquivo deve seguir sozinho, sem texto introdutório e sem legenda/caption, salvo aprovação explícita de Lucas no turno.

Para arquitetas, não pressupor que a obra é para a própria arquiteta. Tratar sempre como obra/opção para cliente ou projeto.

## Ação executada — 2026-05-18

Lucas aprovou no Telegram o envio por WhatsApp e e-mail para Anna Campos, incluindo a formulação voltada a arquiteta/projeto.

Mensagem WhatsApp enviada via `wacli --account pessoal`:

```text
Boa tarde, Anna. Tudo bem?

Aqui é o Lucas, da Zipper Galeria. A Helô me encaminhou seu contato sobre obras disponíveis da Flávia Junqueira.

Registro da mensagem efetivamente enviada, posteriormente corrigida por Lucas: o WhatsApp deveria ter enviado apenas o PDF, sem mensagem e sem legenda; para arquitetas, a obra deve ser enquadrada sempre como sendo para um cliente/projeto.
```

WhatsApp:
- Texto enviado: message id `3EB033FE8717C10F939A67`.
- PDF enviado: message id `3EB0E5ACF8CBE8A406DD45`.
- Arquivo enviado visualmente como `Flávia Junqueira — Seleção Obras Disponíveis.pdf`.
- Correção posterior de Lucas: o número original estava correto, mesmo aparecendo como `Número desconhecido` no print. Não reenviar para hipótese com nono dígito.
- Observação operacional: foi testada por engano a hipótese de celular BR com nono dígito (`+55 46 99110-5468`), mas o `wacli` retornou falha `no LID found ... from server`; nenhum novo PDF foi entregue por WhatsApp nessa tentativa.

E-mail:
- Remetente: `lucas@zippergaleria.com.br`.
- Destinatário: Anna Campos (e-mail preservado fora desta nota por minimização de PII).
- Assunto enviado: `Flávia Junqueira — obras disponíveis`.
- Correção posterior de Lucas: título/assunto correto para uso futuro deve ser `Flávia Junqueira — Obras Disponíveis`.
- Gmail message id: `19e3c45d580589b9`.
- Anexo: versão comprimida/e-mail-safe do PDF (`6,436,136` bytes), mantendo o PDF/catálogo como `Flávia Junqueira — Seleção Obras Disponíveis.pdf`.
- Verificação pós-envio: anexo presente, marcador de corpo validado, zero padrões genéricos de segredo detectados.

Follow-up interno/reminder:
- Criado cron `46a38c54f72b` para 2026-05-20 13:15 BRT, apenas para lembrar Lucas; não envia mensagem externa automaticamente.

## Guardrail atualizado

Não enviar novos follow-ups/respostas externas automaticamente sem nova aprovação de Lucas, exceto se Lucas aprovar explicitamente o payload no turno futuro.

Para este caso específico, o número original da Anna foi confirmado correto por Lucas; não reenviar para variante inferida com nono dígito. O erro operacional restante foi formato do WhatsApp: deveria ter ido apenas o PDF, sem texto introdutório e sem caption.

## Correção de Lucas — 2026-05-18

- Correção: `Flávia Junqueira — Obras Disponíveis` é o título/assunto correto do e-mail; não era correção do nome do PDF.
- WhatsApp: quando enviar PDF/catálogo da Zipper, o arquivo deve seguir sozinho, sem mensagem antes e sem legenda/caption, salvo aprovação explícita no turno.
- Arquitetas: nunca pressupor que a obra é para a própria arquiteta; tratar como obra para um cliente/projeto.
- Follow-up futuro sugerido: se ela não responder, perguntar com naturalidade se existe algum outro artista da Zipper que ela gostaria de ver para o projeto.
