# Memory OS — synthetic resilience gap

Gerado para teste local controlado de resiliência v1.16.

## Escopo

Receipt sintético local/documental criado propositalmente fora do writer para validar que o daytime checker detecta e corrige drift via `receipt_writer --register-existing`.

## Não-ações

- Nenhum Docker/VPS/Traefik/gateway/restart.
- Nenhum write externo.
- Nenhum segredo.

## Rollback

Remover este receipt sintético e o evento writer correspondente se necessário.
