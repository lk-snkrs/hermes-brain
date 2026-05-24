# Receipt — arquitetura checkout > cart intent no CRM WhatsApp LK

Data: 2026-05-21T10:55:07Z
Área: LK CRM / WhatsApp / Crisp / n8n / Supabase

## Decisão aprovada

Lucas aprovou seguir a recomendação de **não unificar fisicamente** os workflows de Checkout Abandonado e Cart Intent neste momento.

Decisão operacional:

- Manter os dois workflows separados.
- Usar Supabase como camada central de estado/deduplicação/supressão.
- Regra comercial: **checkout abandonado vence cart intent**.
- Cart intent só pode enviar se, imediatamente antes do envio, não existir checkout ativo para o mesmo telefone/identidade.

## Verificação executada

Foram lidos via n8n API os workflows ativos:

1. `kWQbmEMuvdipcGjd` — `LK - Checkout Abandonado 30min/24h/72h Polling GraphQL - Crisp (ATIVO)`
2. `XLODECE4MvNRNCQ9` — `LK - Cart Intent 30min Full Funnel - Crisp (ATIVO)`

Snapshots read-only antes da auditoria foram salvos em `.secrets/n8n-snapshots/` com permissão restrita.

## Resultado técnico

O workflow de Cart Intent já contém o gate recomendado antes do envio:

1. `LK Cart Intent Webhook`
2. `Wait 30 min`
3. `Crisp REST Get Conversation Meta`
4. `Filtrar cart intent elegíveis`
5. `Supabase Load Active Checkout Suppression`
6. `Aplicar supressão checkout > cart`
7. `Preparar payload Crisp Cart`
8. `Crisp Send cart intent`
9. `Marcar cart enviado no dedup`
10. `Supabase Persist Cart Result`

O node `Supabase Load Active Checkout Suppression` consulta a tabela `lk_crm_checkout_sequences` por telefone e considera status ativos:

- `pending`
- `sent`
- `request_accepted`
- `delivered`
- `read`

O node `Aplicar supressão checkout > cart` registra supressão quando encontra checkout ativo dentro da janela configurada e não segue para o envio do Cart Intent.

## Conclusão

Não foi necessário patch adicional nesta etapa: a arquitetura aprovada já está implementada no fluxo ativo de Cart Intent.

O ponto importante para monitoramento é diferenciar nos relatórios:

- cart intent capturado;
- cart intent sem telefone resolvido;
- cart intent elegível;
- cart intent suprimido por checkout ativo;
- cart intent enviado;
- checkout enviado.

## Segurança

- Nenhum teste WhatsApp foi enviado nesta verificação.
- Nenhum cliente foi contatado.
- Nenhum workflow foi executado manualmente.
- Nenhuma credencial foi exposta no Brain.
- Nenhum write externo foi feito.

## Próxima validação recomendada

Na próxima ocorrência real de cart intent com telefone resolvido, verificar a execução n8n para confirmar se caiu em uma destas trilhas:

- `suppressed_by_checkout` quando houver checkout ativo;
- envio cart intent quando não houver checkout ativo;
- skip por ausência de telefone/identidade quando aplicável.
