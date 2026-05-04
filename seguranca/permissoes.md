# Permissionamento Hermes Brain

Este arquivo define o modelo de acesso do Hermes Brain após a adaptação Bruno/OpenClaw para o Hermes.

Princípio central:

```text
O agente não é o cérebro. O agente lê e escreve no cérebro dentro do seu escopo.
```

## Usuários autorizados

| Usuário | Telegram ID | Acesso |
|---|---:|---|
| Lucas Cimino | 171397651 | Total — todas as áreas, agentes e ações aprovadas |

Usuários adicionais por área podem ser documentados nos arquivos `agentes/*/AGENTS.md`. Se o usuário não estiver documentado, o agente deve responder que não tem autorização para atender.

## Camadas de acesso

| Camada | Função | Regra |
|---|---|---|
| `memories/` | Memória executiva compacta | Leitura global; escrita cuidadosa quando houver decisão, lição ou contexto permanente |
| `empresa/` | Contexto cross-área | Leitura para agentes de área; escrita preferencial do Hermes Geral |
| `areas/` | Operação por negócio/área | Cada agente escreve preferencialmente só na própria área |
| `agentes/` | Identidade, escopo e regras dos agentes | Alteração por Hermes Geral ou com aprovação Lucas |
| `seguranca/` | Permissões e ações sensíveis | Alteração por Hermes Geral; mudanças de política exigem aprovação Lucas |
| `skills/` | Skills canônicas | Atualizar quando workflow recorrente muda; não duplicar lógica divergente |
| `scripts/` | Scripts operacionais | Alterações exigem verificação e cuidado com produção |

## Agentes e escopos

| Agente | Leitura | Escrita preferencial | Bloqueios / limites |
|---|---|---|---|
| Hermes Geral | Tudo | Tudo com cuidado | Ações externas e destrutivas exigem aprovação Lucas |
| LK | `empresa/contexto/`, `empresa/decisoes/`, `areas/lk/`, `memories/lk.md` | `areas/lk/` | Não acessar Zipper/SPITI sem motivo explícito; não enviar campanha/WhatsApp sem aprovação |
| Zipper | `empresa/contexto/`, `empresa/decisoes/`, `areas/zipper/`, `memories/zipper.md` | `areas/zipper/` | Não misturar Zipper Vendas com SPITI; contato com colecionador exige aprovação Lucas/Osmar |
| SPITI | `empresa/contexto/`, `empresa/decisoes/`, `areas/spiti/`, `memories/spiti.md` | `areas/spiti/` | Email é fonte de verdade para lances; não enviar grupo/cliente sem aprovação |
| Operações | `empresa/`, `areas/operacoes/`, `scripts/`, `skills/brain-sync/` | `areas/operacoes/` e docs operacionais | Não alterar produção sem rollback/plano |
| Governança | `seguranca/`, `empresa/decisoes/`, `areas/governanca/` | `areas/governanca/`, `seguranca/` | Mudanças de política exigem Lucas |
| Tecnologia | `TOOLS.md`, `scripts/`, `areas/tecnologia/`, `empresa/contexto/` | `areas/tecnologia/` e docs técnicos | Secrets via Doppler; deploy/infra requer cuidado |

## Permissões por negócio

### LK Sneakers

Fontes permitidas quando necessário:

- Supabase LK `cnjimxglpktznenpbail`.
- Shopify LK.
- Klaviyo.
- GA4/GSC.
- Meta Ads.
- Evolution Clo somente para envios aprovados.

Regras:

- Consultar dados reais antes de afirmar métricas, clientes, pedidos ou produtos.
- Não sugerir produto fora de estoque.
- Campanhas, WhatsApp, email e contato com cliente exigem aprovação Lucas.

### Zipper Galeria

Fontes permitidas quando necessário:

- Supabase Zipper Vendas `pcstqxpdzibheuopjkas`.
- Tabela `vendas_tango` para vendas reais.
- SPITI/Zipper CRM `rmdugdkantdydivgnimb` apenas quando houver contexto explícito de CRM compartilhado.

Regras:

- Nunca confundir vendas reais da Zipper com leilão SPITI.
- Nunca afirmar que obra/artista “vende bem” sem consultar histórico real.
- Contato com colecionador, proposta ou decisão de curadoria exige aprovação Lucas/Osmar.

### SPITI Auction

Fontes permitidas quando necessário:

- Supabase/SPITI CRM `rmdugdkantdydivgnimb`.
- Tabela `spiti_lotes`.
- Email como fonte de verdade para total de lances.
- Site apenas com ressalva, pois pode mostrar destaques.

Regras:

- Meta tag é preço base, não lance atual.
- Silêncio é melhor que dado errado.
- Mensagens para grupo/cliente ou relatório externo exigem aprovação Lucas.

## Ações livres

Podem ser feitas sem aprovação adicional quando dentro do escopo:

- Ler arquivos do Brain.
- Consultar histórico com `session_search`.
- Consultar dados internos em modo leitura.
- Criar rascunhos e previews.
- Organizar documentação, índices, rotinas e skills.
- Criar commits/pushes de documentação ou correções seguras quando Lucas pediu para seguir.
- Buscar secrets no Doppler sem imprimir valores.

## Ações que exigem aprovação Lucas

- Enviar WhatsApp, email, campanha, post ou comentário público.
- Contatar cliente, colecionador, parceiro, artista ou fornecedor.
- Publicar relatório externo.
- Criar/alterar campanha Klaviyo, Meta Ads ou automação n8n que dispare mensagens.
- Alterar produção, deploy, infraestrutura, DNS ou workflow externo.
- Fazer writes em banco de produção que alterem dados de negócio.
- Rotacionar, revogar ou criar credenciais.
- Mudar este modelo de permissões.

## Ações bloqueadas sem plano explícito

- Expor secret completo em chat, arquivo ou log.
- Commitar secret, token, senha, refresh token ou chave privada.
- DELETE, DROP, TRUNCATE ou migração destrutiva sem backup e rollback.
- Alterar dados financeiros/comerciais sem trilha de auditoria.
- Enviar mensagens em massa sem preview aprovado.
- Misturar dados entre LK, Zipper e SPITI sem justificativa documentada.

## Doppler

Doppler `lc-keys/prd` é a fonte de verdade para credenciais.

Regras:

- Guardar nomes de secrets no Brain, nunca valores.
- Buscar valores sob demanda.
- Preferir rodar processos com Doppler injetando ambiente.
- Não colocar token em remote Git, README, logs ou mensagens finais.

## Revisão

Ao alterar permissões:

1. Atualizar este arquivo.
2. Atualizar `seguranca/acoes-sensiveis.md` se aplicável.
3. Rodar scan de secrets.
4. Commitar com mensagem clara.
5. Pedir aprovação Lucas se a mudança amplia autonomia ou reduz exigência de aprovação.
