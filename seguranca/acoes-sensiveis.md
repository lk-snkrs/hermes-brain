# Ações Sensíveis — Hermes Brain

Este arquivo classifica ações por risco e define quando o Hermes pode agir diretamente, quando precisa de aprovação Lucas e quando precisa de plano explícito com rollback.

## Níveis de risco

| Nível | Nome | Descrição | Regra |
|---|---|---|---|
| L0 | Leitura/organização | Sem efeito externo ou alteração de produção | Livre dentro do escopo |
| L1 | Escrita no Brain | Documentação, índices, rascunhos, skills e rotinas | Livre quando Lucas pediu a tarefa/“seguir”, com scan de secrets |
| L2 | Consulta operacional | Consultas internas em bancos/APIs, preferencialmente read-only | Livre dentro do escopo, sem expor dados sensíveis desnecessários |
| L3 | Ação externa reversível | Rascunhos, previews, PRs, alterações documentais e config não produtiva | Pode preparar; execução externa exige aprovação se impactar terceiros |
| L4 | Produção / comunicação / dados | Mensagens, campanhas, writes em produção, deploys, workflows, credenciais | Aprovação Lucas obrigatória |
| L5 | Destrutivo / irreversível | Delete/drop, perda de dados, exposição de secrets, envio em massa sem preview | Bloqueado sem plano explícito, backup e aprovação |

## Livres dentro do escopo

- Ler arquivos do Brain.
- Pesquisar histórico de conversa.
- Consultar documentação e fontes internas.
- Criar rascunhos, previews e planos.
- Criar ou atualizar MAPAs, rotinas e índices.
- Criar commits/pushes de documentação quando Lucas pediu continuidade.
- Consultar Doppler para buscar secret necessário, sem imprimir valor.
- Rodar scan de secrets, `git status`, `git diff`, verificações e testes.

## Precisam aprovação Lucas

### Comunicação externa

- WhatsApp para cliente, colecionador, parceiro, artista ou fornecedor.
- Email externo.
- Campanha Klaviyo, Meta, n8n ou qualquer automação que envie mensagens.
- Post público, comentário público ou alteração pública de conteúdo.
- Relatório externo para grupo/cliente/parceiro.

### Produção e infraestrutura

- Deploy.
- Alteração de DNS, Railway, Vercel, Cloudflare, Hostinger/VPS ou Docker em produção.
- Alteração/removal/recriação de containers, compose, volumes, Docker networks, Traefik, n8n, Paperclip ou Hermes na VPS.
- Alteração de root password, SSH access, firewall, portas ou arquivos sob `/docker/*`.
- Alteração de workflow n8n ativo.
- Alteração de cron que impacte operação real.
- Rotação, revogação ou criação de secrets.

### Dados

- INSERT/UPDATE/DELETE em banco de produção, salvo quando for rotina explicitamente aprovada e idempotente.
- Mudança de schema, migração ou permissão de banco.
- Enriquecimento ou alteração de dados de cliente/colecionador.

### Negócio

- Proposta comercial.
- Cupom, desconto, preço, condição de pagamento.
- Decisão de curadoria.
- Abordagem personalizada a colecionador.
- Mensagem de cross-sell ou reativação para cliente LK.

## Bloqueadas sem plano explícito

- Expor secret completo em qualquer lugar.
- Commitar secret.
- Colocar token em URL de remote Git.
- Rodar DELETE, DROP, TRUNCATE ou migração destrutiva.
- Enviar mensagem em massa sem preview aprovado.
- Alterar produção sem backup/rollback.
- Afirmar dado sensível de negócio sem fonte consultada.
- Misturar bases LK, Zipper e SPITI sem justificar fonte e escopo.
- Versionar dados vivos como se fossem conhecimento permanente sem fonte viva, timestamp e minimização.
- Dar ao Hermes Geral/Mission Control dados brutos de uma empresa quando um resumo autorizado bastaria.

## Dados vivos e resumos autorizados

Conhecimento estável pertence ao Hermes Brain/Git. Dado operacional atual pertence à fonte viva: Shopify, Tiny, Supabase, GA4/GSC, Meta/Metricool, Klaviyo, WhatsApp, email, GitHub/runtime, logs ou sistema equivalente.

Ao gerar report, painel ou handoff multiempresa:

1. consultar a fonte viva correta;
2. registrar `generated_at`, fonte e limite do snapshot;
3. separar fato, interpretação e recomendação;
4. omitir PII, dumps brutos e dados sensíveis desnecessários;
5. compartilhar com Hermes Geral/Mission Control somente resumo autorizado da área dona;
6. bloquear qualquer ação externa, banco/produção/infra ou campanha sem aprovação Lucas.

Rotina canônica: `areas/operacoes/rotinas/data-boundaries-authorized-summaries.md`.

## Regras por negócio

### LK Sneakers

Sensível:

- Campanha Klaviyo.
- WhatsApp via Evolution Clo.
- Cross-sell individual ou em massa.
- Cupom/desconto.
- Alteração em Shopify.
- Escrita no Supabase LK.

Livre:

- Consultar pedidos/clientes/produtos para análise.
- Gerar preview e recomendação.
- Atualizar documentação do Brain.

### Zipper Galeria

Sensível:

- Contato com colecionador.
- Proposta de obra.
- Decisão de curadoria.
- Publicação em redes.
- Afirmação comercial sobre obra/artista sem `vendas_tango`.

Livre:

- Consultar histórico em Zipper Vendas.
- Criar rascunho de abordagem.
- Criar checklist de feira.
- Organizar comunicação e tom.

### SPITI Auction

Sensível:

- Mensagem para grupo/cliente.
- Relatório externo de lances.
- Alteração no monitor de lances ou workflow n8n.
- Afirmação de total de lances sem email/fonte correta.

Livre:

- Preparar relatório interno com fonte e ressalvas.
- Documentar regras de verificação.
- Consultar banco/fonte correta quando disponível.

## Regras de secrets

- Doppler `lc-keys/prd` é fonte de verdade.
- O Brain só documenta nomes de secrets.
- Nunca imprimir valores em resposta final.
- Nunca salvar valores em arquivo local.
- Se um secret apareceu em chat/log/repo, recomendar rotação/revogação.
- Scan obrigatório antes de commit quando houver alteração em docs/scripts.

## Checklist antes de executar ação sensível

1. A ação afeta cliente, colecionador, público, produção ou dados?
2. Existe aprovação Lucas explícita?
3. Existe preview/plano claro?
4. Existe rollback ou forma de desfazer?
5. Secrets não serão expostos?
6. A fonte de dados foi verificada?
7. O resultado será registrado no Brain se virar decisão ou aprendizado?

Se qualquer resposta crítica for “não”, preparar rascunho/plano e pedir aprovação antes de executar.
