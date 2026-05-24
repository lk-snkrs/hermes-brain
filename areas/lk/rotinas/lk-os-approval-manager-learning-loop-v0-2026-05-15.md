# LK OS — Approval Manager + Learning Loop v0

Gerado em: `2026-05-15T19:43:38.534764+00:00`
Status: `active_local_rule_layer`
Escopo: LK OS + regra global reutilizável para Zipper/SPITI quando envolver aprovação/correção/ação externa.
Modo: documentação/guardrails locais; nenhum envio externo, campanha, Shopify, Tiny, Merchant, Meta, WhatsApp ou Gmail executado.

## Veredito

Transformei o bloco **Approval Manager + Learning Loop** em regra operacional do LK OS: aprovações, correções, rejeições e padrões do Lucas não ficam mais como conversa solta; viram ledger, regra viva, skill/Brain patch quando mudam procedimento e gate antes de execução.

## Correção crítica registrada em 2026-05-15

Feedback Lucas: `/background` enviou automaticamente um e-mail para Paulo/Zipper, mas a intenção correta era **gerar um draft**, não enviar.

Regra aprendida:

- `/background`, background execution, “seguir” ou aprovação ampla de trabalho **nunca** autorizam envio externo.
- Para e-mail, WhatsApp, cliente, colecionador, fornecedor, campanha/newsletter ou qualquer contato humano externo: gerar **draft/preview**.
- Só enviar se Lucas disser explicitamente, na conversa atual, algo equivalente a: `enviar este texto para [destinatário]`.
- Se houve erro de envio, não mandar correção automática; preparar draft de mitigação e pedir aprovação.

## Estados canônicos

- `draft_only`: resposta pronta, não enviada.
- `needs_lucas_approval`: exige aprovação atual com payload inline.
- `approved_exact_payload`: Lucas aprovou destinatário + texto + contexto exato no turno atual.
- `executed_verified`: ação executada e verificada.
- `rejected_or_corrected`: Lucas corrigiu/rejeitou; registrar regra viva.
- `rolled_back_or_mitigated`: ação desfeita/mitigada após aprovação.
- `needs_data`: falta dado; resolver read-only/local antes de pedir aprovação.

## Gates por área

### Cliente / e-mail / WhatsApp / fornecedor

Default: `draft_only`.

Bloqueado sem aprovação atual:

- envio de e-mail;
- resposta em WhatsApp;
- contato com cliente/colecionador/artista/fornecedor;
- mensagem de correção/disregard após erro;
- proposta, preço, disponibilidade ou promessa operacional.

### Campanhas / CRM / Klaviyo / Meta

Default: `preview_only`.

Enviar, agendar, ativar campanha, mexer em público/budget ou flow exige aprovação atual e payload/rollback inline.

### GMC / Merchant / Shopify / Tiny

Default: read-only/preview/local.

Writes só com escopo exato, snapshot/rollback, IDs/linhas exatos e aprovação específica.

### Tema / CRO / visual

Default: visual artifact/preview.

Correção visual aprovada vira baseline; se Lucas corrigir estética, atualizar regra e não repetir o padrão ruim. Exemplo já registrado: COMPRE JÁ deve preservar paridade visual original quando o objetivo for correção, não redesenho.

### Sourcing / compra

Default: decisão local/preview.

Contato, cotação externa, compra, reserva, PO ou negociação exigem aprovação atual. Dados/sourcing read-only podem seguir sozinhos.

## Rotina obrigatória após feedback do Lucas

1. Classificar: aprovação, correção, rejeição, regra factual, anti-padrão ou padrão aprovado.
2. Decidir camada:
   - memória compacta, se global;
   - Brain/PRD, se regra detalhada;
   - skill, se muda procedimento repetível;
   - backlog, se vira trabalho futuro.
3. Atualizar artefatos no mesmo turno quando possível.
4. Verificar readback/secret scan.
5. Reportar em uma linha o que mudou.

## Artefatos atualizados nesta implementação

- Memória operacional compacta do agente.
- Skill `google-workspace`: background não autoriza envio; draft only.
- Skill `multiempresa-routing-lucas`: contato externo exige aprovação atual com payload inline.
- Skill `lucas-chief-of-staff`: `/background`/`seguir` não são aprovação de envio.
- `empresa/gestao/hermes-learning-loop.md`: correção global registrada.
- `areas/lk/projetos/lk-os-future-configuration-map-2026-05-15.md`: Approval Manager promovido para regra ativa local.

## Não executado

- Nenhum e-mail enviado.
- Nenhum draft criado no Gmail.
- Nenhum contato com Paulo ou qualquer cliente.
- Nenhum write em sistemas comerciais.
