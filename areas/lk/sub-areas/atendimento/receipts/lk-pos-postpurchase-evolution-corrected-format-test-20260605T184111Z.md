# Receipt — correção de formatação Evolution API / LK Flagship

Data UTC: 2026-06-05T18:41:11Z

## Contexto

Lucas reportou que o primeiro teste chegou desconfigurado, com `\n` literal/aspas aparentes. Causa operacional: o script de teste montou a variável `message` usando `repr(json.dumps(...))`, transformando a mensagem em string JSON literal em vez de texto com quebras reais.

## Correção executada

Reenvio único para o mesmo número de teste autorizado (`5511991203361`) pela Evolution API, instância `LK Flagship`, usando string Python normal e `json.dumps` apenas no corpo HTTP.

Mensagem reenviada:

```text
Oi, tudo bem? Aqui é a equipe da LK Sneakers.

Este é um teste interno do novo fluxo de pós-venda POS 30min via Evolution API / LK Flagship.

Nenhuma automação de cliente está ativa ainda.
```

## Resultado sanitizado

```json
{
  "mode": "EXECUTE_SEND_CORRECTED_FORMAT_TEST",
  "instance": "LK Flagship",
  "phone_hash": "a6ceac695ca3",
  "message_chars": 188,
  "payload_has_literal_backslash_n": false,
  "payload_newline_count": 4,
  "send_status": "sent",
  "http_status": "201",
  "status": "PENDING",
  "fromMe": true,
  "id_present": true
}
```

## Lição técnica

Para Evolution `/message/sendText/{instance}`, montar `message` como texto normal e aplicar `json.dumps({'number': ..., 'text': message})` apenas no payload HTTP. Não usar `repr(json.dumps(message))` para injetar texto em script, pois isso envia aspas e barras escapadas ao WhatsApp.
