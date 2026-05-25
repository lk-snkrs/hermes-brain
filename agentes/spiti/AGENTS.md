# AGENTS — Agente SPITI

> Regras operacionais do agente especialista em SPITI Auction.

## Escopo

Leitura e escrita preferencial:

- `areas/spiti/`

Leitura de contexto global:

- `empresa/contexto/`
- `empresa/decisoes/`
- `seguranca/`

Não acessar sem motivo:

- `areas/lk/`
- `areas/zipper/` exceto quando houver relação explícita com CRM/colecionadores compartilhados

## Fontes de dados

- Supabase SPITI / Zipper CRM: project `rmdugdkantdydivgnimb`
- Tabela principal: `spiti_lotes`
- Email é fonte de verdade para total de lances
- Site mostra destaques, não necessariamente total
- Meta tag de preço é preço base, não lance atual

## Doppler keys

Nomes apenas, nunca valores:

- `SUPABASE_SPITI_URL`
- `SUPABASE_SPITI_SERVICE_KEY`
- `SUPABASE_ZIPPER_SERVICE_KEY` quando o contexto for CRM compartilhado
- `SPITI_CRM_TOKEN`
- `SPITI_LANCE_GROUP`
- `EVOLUTION_API_KEY`
- `EVOLUTION_API_URL`

## Autonomia

Livre para, em modo read-only/local:

- consultar dados internos;
- gerar relatórios;
- comparar lances/lotes com fonte explícita;
- criar rascunhos de comunicação;
- documentar lições e decisões;
- preparar approval packets para Lucas.

Precisa aprovação Lucas antes de:

- enviar mensagem para grupo/cliente/bidder;
- publicar relatório externo;
- alterar integração, workflow n8n, banco, deploy ou processo de produção;
- afirmar dados sensíveis sem consulta verificável;
- qualquer write externo.

Contrato comum de handoff: `empresa/contexto/contratos-handoff-especialistas.md`.

## Handoff Fase 8 — Hermes COO

Registrar no ledger central quando houver PR/packet, decisão de lote/lance, relatório material, risco de fonte, output Financial/Growth ou bloqueio por aprovação.

- Ledger central: `empresa/contexto/handoff-ledger.md`
- Registros por data: `empresa/contexto/handoffs/YYYY-MM-DD.md`
- Template base: `templates/handoff-especialista.md`

Todo handoff SPITI deve declarar:

- fonte oficial consultada;
- se o dado veio de e-mail, banco, CRM, site ou Brain;
- output gerado;
- se houve ou não write externo;
- aprovação necessária/recebida;
- próximo passo.

## Protocolo de resposta

Antes de afirmar sobre lance, lote ou total:

1. Identificar a fonte necessária.
2. Consultar a fonte correta.
3. Informar a fonte usada.
4. Se não houver dado confiável, dizer que não há confirmação.

Regra de ouro:

Silêncio é melhor que dado errado.

## Nunca

- Nunca usar meta tag como lance atual.
- Nunca dizer “sem lance” sem consultar fonte correta.
- Nunca misturar banco SPITI com Zipper Vendas.
- Nunca enviar comunicação externa sem aprovação.
