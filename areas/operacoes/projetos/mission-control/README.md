# Mission Control

Status: hub canônico Brain OS Onda 2 para Mission Control/Cockpit; separado de Mesa COO por fronteira clara de produto/cockpit.

Owner: `areas/operacoes`.

## Escopo

- `Mission Control Hermes-native / COO Cockpit`
- Decision Inbox e work kernel
- PR packages, deploy reports e snapshots
- Relação com Brain como fonte de verdade, não cópia paralela

## Regra Brain OS

Este hub é camada canônica de leitura e navegação. Ele preserva os arquivos originais e aponta para evidências, sem mover/apagar histórico e sem executar writes externos.
