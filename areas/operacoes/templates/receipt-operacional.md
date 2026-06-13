# Template — Receipt Operacional Hermes Brain

Use para toda execução relevante feita por Hermes Central, profile especialista, cron, webhook ou integração. O receipt é a ponte entre execução e Brain; sem receipt, a execução não é fonte durável.

```md
# Receipt — <empresa/área> — <ação> — <YYYY-MM-DD>

- Data/hora:
- Agente/profile/cron:
- Empresa/área:
- Responsável humano:
- Pedido original:
- Classificação: read-only | local-write | external-write | customer-facing | infra-sensitive
- Fontes usadas:
- O que foi feito:
- Output/artefato:
- Aprovação:
- Envio/publicação:
- Writes externos:
- Riscos/bloqueios:
- Rollback/mitigação:
- Próximos passos:
- Reminder OS loop needed: yes/no
- Reminder OS owner:
- Reminder OS next action:
- Reminder OS review trigger:
- Reminder OS evidence:
- Onde foi documentado no Brain:
- Source confidence: runtime-verificado | fonte-primária | fonte-secundária | inferido | não-verificado
```

## Regra

- Ações externas, customer-facing, infra, campanha, preço, disponibilidade, reserva, negociação e fornecedor exigem aprovação ou fonte/escopo previamente autorizados.
- Receipts devem ficar na área que executou: `areas/<empresa>/.../receipts/` ou `areas/operacoes/receipts/`.
- Reports brutos podem ficar locais; receipts curados são artefatos de governança.
- Se `Próximos passos` não estiver fechado, preencher o bloco Reminder OS ou criar/encaminhar loop com dono, próxima ação, gatilho e evidência. O Reminder OS não autoriza execução; ele só preserva continuidade.

## Memory OS hook obrigatório

Preferência v1.4 para receipts novos: criar o receipt pelo wrapper local, que valida campos mínimos, salva o arquivo e chama o hook automaticamente:

```bash
python3 /opt/data/scripts/hermes_memory_os_receipt_writer.py --path <caminho-do-receipt> --title '<título>' --empresa-area '<área>' --pedido '<pedido>' --fonte '<fonte>' --feito '<ação>' --output '<artefato>' --aprovacao '<escopo/aprovação>' --rollback '<rollback>' --documentado '<onde>'
```

Memory OS v1.12: receipt operacional novo deve sair pelo writer. Hook direto em receipt novo é drift local (`drift_receipt_hook_only`). Para regularizar receipt local já existente sem sobrescrever conteúdo, usar `--register-existing` com motivo explícito.

Se o receipt foi criado por outro meio, executar localmente após salvar:

```bash
python3 /opt/data/scripts/hermes_memory_os_event_hook.py <caminho-do-receipt>
```

Contrato: stdout vazio quando verde; se imprimir alerta, registrar no próprio receipt ou em follow-up. O wrapper atualiza `reports/memory-hygiene/receipt-writer-latest.json`; o hook atualiza `reports/memory-hygiene/hook-latest.json` e `hook-events.jsonl`, sem ler/despejar conteúdo do receipt e sem Telegram em sucesso.
