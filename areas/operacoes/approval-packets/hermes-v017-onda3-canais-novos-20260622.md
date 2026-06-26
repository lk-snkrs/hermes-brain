# Approval Packet — Hermes v0.17 Onda 3: canais novos

Data: 2026-06-22
Status: preparado; nenhuma ativação executada.

## Escopo da Onda 3

Avaliar e, somente após aprovação escopada, ativar canais novos trazidos/amadurecidos no Hermes v0.17:

1. WhatsApp Business Cloud API oficial.
2. iMessage via Photon Spectrum.
3. Raft agent network.
4. SimpleX.

## Evidência atual

Doppler candidate presence probe:

- `WHATSAPP_CLOUD_ACCESS_TOKEN`: ausente sob nome testado.
- `WHATSAPP_CLOUD_PHONE_NUMBER_ID`: ausente sob nome testado.
- `WHATSAPP_CLOUD_VERIFY_TOKEN`: ausente sob nome testado.
- `PHOTON_PROJECT_ID`: ausente sob nome testado.
- `PHOTON_PROJECT_SECRET`: ausente sob nome testado.
- `PHOTON_ALLOWED_USERS`: ausente sob nome testado.
- `RAFT_PROFILE`: ausente sob nome testado.
- `SIMPLEX_PROFILE`: ausente sob nome testado.

Observação: ausência nesses nomes não prova inexistência absoluta; antes de concluir, consultar mapa Doppler/candidatos canônicos. `values_printed=false`.

## Opção A — WhatsApp Business Cloud API

### Valor esperado

- Canal oficial Meta, melhor que bridge pessoal quando há caso de atendimento/comercial aprovado.
- Pode reduzir dependência de WACLI/Baileys para fluxos oficiais.

### Requisitos

- Meta Business ativo.
- Phone Number ID.
- Access token.
- Verify token.
- Webhook URL público.
- Política clara de mensagens, aprovação e opt-in.

### Riscos

- Webhook público e credenciais Meta.
- Envio indevido para clientes.
- Mistura atendimento pessoal/comercial.

### Guardrails

- Sem sends automáticos na primeira fase.
- Canary observe-only ou inbound-only primeiro.
- Approval separado para qualquer outbound.
- Receipts sanitizados.

## Opção B — iMessage via Photon Spectrum

### Valor esperado

- Canal pessoal/iMessage sem relay Mac tradicional.

### Requisitos

- `hermes photon setup`.
- Device login/projeto/sidecar.
- Allowlist de usuários.

### Riscos

- Canal pessoal sensível.
- Privacidade e identidade do remetente.

### Guardrails

- Allowlist estrita.
- Sem automações outbound no início.
- Teste com uma conversa controlada.

## Opção C — Raft agent network

### Valor esperado

- Conectar Hermes a rede de agentes externos.

### Riscos

- Exposição de capacidades/contexto.
- Wake payloads, trust boundary e roteamento.

### Guardrails

- PoC metadata-only.
- Sem ferramentas sensíveis.
- Sem terminal/file/secrets expostos à rede.

## Opção D — SimpleX

### Valor esperado

- Canal privado alternativo.

### Riscos

- Nova superfície operacional sem caso claro.

### Guardrails

- Avaliar apenas se houver caso de uso concreto.

## Aprovação necessária

Escolher uma destas opções:

1. **Aprovar Onda 3A WhatsApp Cloud observe-only/inbound-only**.
2. **Aprovar Onda 3B Photon/iMessage canary allowlist**.
3. **Aprovar Onda 3C Raft metadata-only PoC**.
4. **Bloquear Onda 3 por enquanto**.

Sem uma dessas aprovações, nenhuma ativação de canal deve ocorrer.

## Rollback geral

- Remover/pausar canal configurado.
- Revogar/rotacionar credenciais no provedor se expostas ou mal configuradas.
- Remover webhook/subscription pública.
- Conferir gateway health e Telegram default após qualquer mudança.

`values_printed=false`
