# Protocolo de Handoff — Agentes especialistas para Hermes Central

Data: 2026-05-19
Status: decisão operacional de Lucas

## Princípio

Agentes especialistas podem executar dentro do próprio perfil/canal, mas não podem virar “mentes separadas”. O Hermes Central / Brain precisa saber o que aconteceu para manter memória, governança, aprendizado e continuidade entre LK, Zipper, SPITI, Mordomo e demais OSs.

Handoff não significa tirar autonomia do especialista. Significa registrar contexto, decisão e resultado para que o próprio perfil continue executando com menos ruído e menos retrabalho.

## Regra de Lucas

Quando um especialista fizer trabalho relevante, ele deve reportar ao Hermes Central e/ou registrar no Brain:

> “Estou fazendo isso no meu perfil. Documente/registre no Brain o que foi feito, fontes, decisão, resultado e próximos passos.”

O registro não precisa ser instantâneo em todos os casos, mas deve existir até o fechamento do dia.

## O que exige handoff

Registrar sempre que houver:

- decisão operacional ou mudança de autonomia;
- conteúdo criado, revisado, aprovado, enviado ou agendado;
- campanha, newsletter, Klaviyo, WhatsApp, e-mail ou publicação;
- alteração em Shopify, tema, GMC, feed, ads, SEO, CRO ou dados;
- relatório recorrente ou output para equipe;
- approval packet, receipt, rollback, evidência ou impacto esperado;
- correção de Lucas ou aprendizado novo;
- bloqueio, risco, fonte ausente ou decisão pendente.

## Frequência

- Alta criticidade: reportar imediatamente ao Hermes Central.
- Baixa/média criticidade: registrar no Brain durante a execução ou no fechamento do dia.
- Rotina recorrente: consolidar no daily handoff do especialista.

## Formato mínimo do handoff

```md
# Handoff especialista → Hermes Central

Data/hora:
Agente/profile:
Empresa/área:
Responsável humano:
Pedido original:
O que foi feito:
Fontes usadas:
Output/artefato:
Aprovação:
Envio/publicação:
Writes externos:
Riscos/bloqueios:
Próximos passos:
Onde foi documentado no Brain:
```

## Formato canônico de receipt

Quando houver decisão, output ou write aprovado, preferir este esqueleto único para evitar variação entre áreas:

```md
# Receipt — [especialista]

Data:
Agente/profile:
Pedido original:
Escopo aprovado:
O que foi feito:
Fontes usadas:
O que não foi feito:
Riscos/bloqueios:
Rollback:
Onde ficou documentado no Brain:
```

O receipt não é um segundo bloqueio; é a memória operacional que preserva autonomia e continuidade.

## LK Growth / Renan

Para conteúdo/newsletter/Klaviyo da LK:

- Profile/canal operacional: `lk-growth` / `@LKGrowth_HermesBot`.
- Responsável humano: Renan.
- Renan tem autonomia aprovada para aprovar e enviar conteúdos/newsletters via Klaviyo dentro do escopo de conteúdo LK.
- Cada campanha/newsletter deve registrar no Brain:
  - briefing;
  - fontes/insights usados;
  - copy final ou link/artefato;
  - segmento/lista quando aplicável;
  - aprovação de Renan;
  - envio/agendamento no Klaviyo;
  - resultado esperado;
  - follow-up de impacto quando houver dados.
- Bloqueios seguem para preço, estoque, Shopify/theme/produto, WhatsApp operacional/massa, campanha paga, compra/sourcing, financeiro e infra.

## Papel do Hermes Central

O Hermes Central deve:

1. receber ou buscar handoffs dos especialistas;
2. garantir que decisões e outputs relevantes foram versionados no Brain;
3. identificar conflitos entre agentes;
4. manter guardrails globais;
5. cobrar handoff quando um especialista executar algo sem registrar;
6. consolidar aprendizados em memória/skills/rotinas quando repetíveis.

## Regra de autonomia preservada

- O especialista continua dono da execução no seu escopo.
- O handoff existe para alinhar contexto, não para pedir nova autorização do que já foi aprovado.
- Se a aprovação for escopada, a execução deve seguir livre dentro desse escopo sem centralizar microdetalhes desnecessários.
- Hermes Central intervém quando houver conflito, risco, falta de contexto, write fora do escopo ou necessidade de governança.

## Anti-padrão proibido

- Cada agente ter “vida própria” sem comunicar o Brain.
- Um especialista executar e deixar apenas no chat local.
- Aprovações ficarem perdidas em Telegram sem artefato no Brain.
- Campanhas/conteúdos serem enviados sem receipt/handoff mínimo.
- O Hermes Central descobrir depois por acaso o que um especialista fez.

## Verificação

Antes de declarar uma rotina ou especialista “operacional”, verificar:

- existe profile/bot real;
- existe escopo documental;
- existe regra de autonomia;
- existe rota de handoff para o Hermes Central;
- existe local no Brain para receipts/outputs;
- existe fechamento diário ou equivalente.
