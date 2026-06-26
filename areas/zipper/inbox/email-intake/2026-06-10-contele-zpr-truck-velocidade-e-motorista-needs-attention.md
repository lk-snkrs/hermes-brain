---
date: 2026-06-10T10:45:07+00:00
updated_at: 2026-06-10T14:26:17+00:00
source: gmail_lucas_zipper
message_ids:
  - 19eb0da4edbc0566
  - 19eb0df3a5d2571f
  - 19eb0e3e1ca13758
  - 19eb0e0c46c0c53e
  - 19eb11411e6226da
  - 19eb11785c8510de
  - 19eb119b2c217bae
  - 19eb151f290ad47b
  - 19eb1608ecb49812
  - 19eb16fcbee3cb09
  - 19eb1799912b9a1e
  - 19eb1814d8dcf01a
  - 19eb1acada9c8273
  - 19eb1b08de4ab7a0
  - 19eb1b1ff467c410
  - 19eb1b89e72c1a13
  - 19eb1bd44bbaa2ce
  - 19eb1e41b38dab54
  - 19eb1e8df98e58f9
thread_ids:
  - 19eb0da4edbc0566
  - 19eb0a9e8d9532a2
status: needs_attention
business: zipper
class: operacional_security_vehicle_alert
---

# Alerta Contele: ZPR Truck com excesso de velocidade e motorista não identificado

## Resumo

E-mails automáticos da Contele Rastreador para `lucas@zippergaleria.com.br` indicam eventos operacionais no veículo `ZPR Truck kia bongo GCD-4F11` na manhã de 10/06/2026:

- 06:25:41: velocidade 111 km/h; limite 110 km/h.
- 06:31:05: velocidade 116 km/h; limite 110 km/h.
- 06:32:44: veículo em uso sem motorista identificado.
- 06:36:08: velocidade 114 km/h; limite 110 km/h.
- 07:28:45: velocidade 112 km/h; limite 110 km/h.
- 07:32:24: veículo em uso sem motorista identificado.
- 07:34:54: velocidade 111 km/h; limite 110 km/h.
- 08:36:21: velocidade 114 km/h; limite 110 km/h.
- 08:52:18: velocidade 115 km/h; limite 110 km/h.
- 09:08:54: velocidade 112 km/h; limite 110 km/h.
- 09:19:39: veículo em uso sem motorista identificado.
- 09:28:03: velocidade 116 km/h; limite 110 km/h.
- 10:15:27: velocidade 114 km/h; limite 110 km/h.
- 10:19:21: veículo em uso sem motorista identificado.
- 10:21:27: velocidade 113 km/h; limite 110 km/h.
- 10:28:29: velocidade 121 km/h; limite 110 km/h.
- 10:33:32: velocidade 122 km/h; limite 110 km/h.
- 11:15:56: velocidade 111 km/h; limite 110 km/h.
- 11:21:11: velocidade 114 km/h; limite 110 km/h.

## Classificação

Não é financeiro interno, newsletter ou ruído promocional. É alerta operacional/security ligado a veículo da Zipper, com repetição em janela curta e identificação de motorista ausente. Por isso foi marcado como `needs_attention`.

Não é material para draft ao remetente Contele.

## Por que importa

O burst mistura excesso de velocidade e uso sem motorista identificado no veículo operacional, o que pode indicar risco de segurança, rota/uso não rastreado ou falha de disciplina operacional.

## Dono provável

Logística/entregas Zipper.

## Próxima ação recomendada

Checar com logística/entregas quem estava conduzindo o ZPR Truck entre 06:25 e 11:21, confirmar se a rota/uso eram esperados e, se necessário, abrir o mapa/evento no Contele para validar local e responsável.

## Bloqueio/dado faltante

Os e-mails exigem clique externo para o local exato; este registro contém horários, veículo, tipo de alerta e velocidades extraídos do corpo dos alertas.

## Ação executada

- Mensagens novas marcadas no helper como `needs_attention`: `19eb11411e6226da`, `19eb11785c8510de`, `19eb119b2c217bae`, `19eb151f290ad47b`, `19eb1608ecb49812`, `19eb16fcbee3cb09`, `19eb1799912b9a1e`, `19eb1814d8dcf01a`.
- Mensagens incrementais marcadas no helper como `needs_attention`: `19eb1acada9c8273`, `19eb1b08de4ab7a0`, `19eb1b1ff467c410`, `19eb1b89e72c1a13`, `19eb1bd44bbaa2ce`.
- Artefato reutilizado/atualizado às 13:40 UTC para consolidar os alertas adicionais de 10:15 a 10:33 no mesmo pacote do dia.
- Artefato reutilizado/atualizado às 14:26 UTC para consolidar os alertas adicionais de 11:15 e 11:21 no mesmo pacote do dia; mensagens `19eb1e41b38dab54` e `19eb1e8df98e58f9` marcadas como `needs_attention`.
- Nenhum e-mail foi enviado.
- Nenhum draft foi criado.
- Rechecagem de candidatos retornou fila vazia.
