# Receipt — correção do remetente do report de vendas LK 09h

Data: 2026-05-20
Contexto: Lucas reportou via screenshot que o e-mail `LK OS · Fechamento de ontem — 19/05` chegou para `lk@lksneakers.com.br`, mas saiu como Zipper Galeria / `producao@zippergaleria.com.br`. Correção esperada: relatório LK deve sair de `lk@lksneakers.com.br` para `lk@lksneakers.com.br`.

## Problema

O script `/opt/data/scripts/lk_report_external_delivery.py` podia cair em credenciais Gmail não-LK quando as chaves `GMAIL_CLIENT_ID_LK`/`GMAIL_CLIENT_SECRET_LK` não existiam, usando conta adjacente de Zipper/produção para envio do report LK.

## Correção aplicada

- `gmail_access_token()` agora recebe `expected_sender` e só aceita OAuth cujo perfil Gmail autenticado seja exatamente `lk@lksneakers.com.br`.
- Foi adicionado fallback seguro para o formato real de produção: `GMAIL_REFRESH_TOKEN_LK` com `GMAIL_CLIENT_ID`/`GMAIL_CLIENT_SECRET` padrão.
- Foram removidos fallbacks para `producao`, Zipper, Lucas pessoal e `GMAIL_USER` genérico no envio de reports LK.
- A verificação Gmail pós-envio agora checa também `from_ok`, além de `to_ok`, `subject_ok`, HTML part, marker e `secret_hits=0`.
- Se não houver credencial LK válida, o script falha fechado em vez de enviar por conta errada.

## Verificação executada

- `python3 -m py_compile /opt/data/scripts/lk_report_external_delivery.py`: OK.
- Probe OAuth sem imprimir segredo: token obtido com `credential_label=lk_default_client`, `sender=lk@lksneakers.com.br`.
- Dry-run sem envio externo: `python3 /opt/data/scripts/lk_report_external_delivery.py --report previous-day-09h` retornou `status=dry_run_ok`, alvo WhatsApp `[LK] Vendas/Trocas/Envios`, e `email_to=[lk@lksneakers.com.br]`.

## Escopo não alterado

- Nenhum e-mail corretivo foi enviado automaticamente.
- Nenhum WhatsApp foi enviado neste reparo.
- Nenhum Docker/VPS/gateway/container/restart foi alterado.
- Nenhum segredo foi impresso.

## Comportamento esperado

Próximo envio real do report LK 09h deve sair de `lk@lksneakers.com.br` para `lk@lksneakers.com.br`. Se a credencial LK falhar, o job deve falhar/alertar em vez de usar conta Zipper/produção.
