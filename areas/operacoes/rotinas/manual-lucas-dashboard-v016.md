# Manual Lucas — Dashboard Hermes v0.16

Status: ativo como guia operacional
Criado em: 2026-06-06
Interface principal: `https://hermes.lucascimino.com`

## Objetivo

Usar o Dashboard Hermes v0.16 como cockpit visual/admin do Hermes remoto, mantendo Telegram como canal limpo de pedidos, decisões e alertas acionáveis.

## Regra de ouro

- **Dashboard**: explorar, visualizar, conferir sessões/status/tools/skills/configuração e entender o sistema.
- **Telegram**: pedir trabalho, aprovar decisões, receber alertas importantes e resumos executivos.
- **Não usar Dashboard para writes sensíveis sem approval packet**: credentials, webhooks, canais, MCP, gateway controls, Docker/Traefik/API pública/model defaults.

## O que você pode fazer com segurança no Dashboard

1. Entrar e navegar pelas sessões.
2. Ver status/configurações sem alterar nada.
3. Consultar skills/tools/catálogo.
4. Ver páginas de system/debug para entender estado.
5. Usar o chat embutido para exploração leve, se preferir.

## O que exige aprovação antes

Antes de clicar/aplicar qualquer ação que altere algo, pedir pelo Telegram:

- “prepare um pacote de aprovação para mudar X no Dashboard”.

Áreas que exigem aprovação:

- Credentials/API keys/OAuth.
- Webhooks/hook creation.
- Channels/messaging platforms.
- MCP enable/disable quando tiver permissões fortes.
- Gateway controls/restart/update.
- Model default/fallback de perfis vivos.
- Exposição pública de API ou mudança em Traefik/Docker.
- Qualquer ação externa: Shopify, Ads, email, clientes, fornecedores, dinheiro.

## Como pedir uma mudança segura

Formato recomendado no Telegram:

```text
Quero alterar [X] no Dashboard. Prepare approval packet com benefício, risco, rollback e verificação.
```

Eu devo responder com:

- escopo exato;
- o que será alterado;
- o que está excluído;
- backup/rollback;
- verificação;
- botões/opções quando a plataforma suportar.

## Novo hábito v0.16: `/undo`

Use quando você mandou algo errado ou quer voltar a direção.

```text
/undo
```

Volta o último turno.

```text
/undo 2
```

Volta dois turnos.

Quando usar:

- pedido mal formulado;
- direção errada;
- falou “seguir” mas percebeu que queria outra coisa;
- quer editar a última mensagem em vez de criar mais contexto.

## Como interpretar Dashboard vs Desktop

- Dashboard é o caminho principal agora: remoto, já funcionando, protegido, sem túnel.
- Desktop Mac é opcional: bom para conforto nativo, mas adiciona configuração de remote mode/auth/túnel.
- Não criar Hermes local paralelo como fonte de verdade.

## Checklist rápido de saúde antes de confiar no Dashboard

Estado saudável esperado:

- `https://hermes.lucascimino.com/` redireciona para `/login` se anônimo.
- `/api/config` anônimo retorna `401`.
- API local do gateway retorna `status: ok`.
- Brain Health passa.
- Nenhum secret aparece em receipts/relatórios.

## Sinais de alerta

Pedir verificação antes de usar se aparecer:

- Dashboard sem login em página admin.
- Erro 500 persistente.
- API config pública sem auth.
- Botões/admin actions que parecem aplicar mudanças sem confirmação.
- Telegram recebendo wrappers técnicos, JSON, job IDs ou ruído.
- Qualquer prompt pedindo segredo no chat.

## Frase curta para Lucas

“Dashboard é para enxergar e administrar; Telegram é para decidir e comandar. Mudança sensível precisa pacote com rollback.”
