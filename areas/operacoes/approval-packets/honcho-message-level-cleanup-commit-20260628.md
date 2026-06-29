# Approval packet — Honcho message-level cleanup COMMIT

## Pedido

Aprovar ou não a etapa destrutiva real de limpeza message-level no Honcho.

## Evidência do dry-run/readback

- Snapshot rollback já existe: `/opt/data/backups/honcho-provider-snapshot-20260628T200831Z`
- Candidate IDs: `173`
- Matched messages: `173`
- Match rate: `100%`
- Direct embeddings: `173`
- Direct queue rows: `0`
- Document source refs: `0`
- Distinct sessions: `173`
- Distinct peers: `1`
- Raw content/IDs/secrets impressos: não
- Delete executado: não

## Por que não apagar sessões inteiras

Os 173 candidatos estão em 173 sessões distintas. `Session.delete()` teria blast radius maior e poderia remover contexto útil junto com cada mensagem contaminada.

## Escopo se Lucas aprovar COMMIT

1. Atualizar o migrator para permitir `--commit` com approval reference explícita.
2. Rodar preflight/readback imediatamente antes.
3. Executar SQL transacional em ordem segura:
   - deletar queue rows referenciando mensagens candidatas se existirem;
   - deletar mensagens candidatas por `public_id`;
   - validar cascade/remoção de `message_embeddings` associadas;
   - não mexer em documents/source_refs porque dry-run deu `0`.
4. Fazer readback pós-commit.
5. Rodar auditor semântico Honcho pós-limpeza.
6. Se necessário, restaurar snapshot.

## Fora de escopo

- Não apagar sessões inteiras.
- Não resetar workspace.
- Não mexer em Brain/memória canônica.
- Não expor raw content, PII, IDs crus, tokens ou secrets.

## Riscos

- É alteração direta no DB Honcho, não API pública do SDK.
- Pode haver derivados não capturados por FK se a aplicação mudou schema/semântica.
- Requer aceitar rollback por snapshot lógico se algo degradar.

## Recomendação

Aprovar somente se Lucas quiser remover a contaminação histórica agora. Tecnicamente o blast radius está baixo e bem delimitado, mas ainda é uma ação destrutiva em provider de memória.
