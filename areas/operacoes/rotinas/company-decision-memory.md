# Rotina — Memória de Decisões por Empresa

Última atualização: 2026-05-17  
PRD base: `../prds/company-decision-memory-prd-2026-05-17.md`

## Regra curta

Toda decisão feita com Lucas sobre uma empresa deve ser salva na memória operacional daquela empresa.

Não basta ficar no chat, em cron response, em report pontual ou em arquivo gerado. Se muda comportamento futuro, precisa virar memória viva e, quando aplicável, skill.

## Quando usar

Use esta rotina sempre que Lucas:

- corrigir uma preferência operacional;
- aprovar formato de relatório, rotina, campanha, atendimento ou automação;
- definir uma fonte de verdade;
- estabelecer guardrail de aprovação/autonomia;
- decidir tom, canal, frequência ou público de comunicação;
- mudar regra comercial, logística, CRM, sourcing, estoque ou produto;
- disser algo como “sempre”, “nunca”, “daqui pra frente”, “o certo é”, “anota”, “salva na memória”.

## Roteamento

1. LK Sneakers → `areas/lk/` e skills LK aplicáveis.
2. Zipper Galeria → `areas/zipper/` e skills Zipper aplicáveis.
3. SPITI Auction → `areas/spiti/` e skills SPITI aplicáveis.
4. Cross-empresa / Grande Mente → `empresa/` e, se envolver risco, `areas/governanca/`.
5. Operação interna Hermes → `areas/operacoes/`.
6. Infra/integrações → `areas/tecnologia/` e skills técnicas.

## Checklist obrigatório

Antes de responder ao Lucas:

- [ ] Classifiquei a empresa/área correta.
- [ ] Separei fato, decisão, interpretação e pendências.
- [ ] Salvei a decisão no artefato vivo da empresa/área.
- [ ] Atualizei a skill se a decisão muda comportamento futuro.
- [ ] Atualizei índice/mapa se criei arquivo novo relevante.
- [ ] Não salvei secrets nem dados sensíveis desnecessários.
- [ ] Não executei envio externo, mutação produtiva ou infra sem aprovação explícita.
- [ ] Respondi onde ficou salvo.

## Formato padrão de registro

```md
## Decisão — [título curto]

Data: YYYY-MM-DD  
Empresa/área: [LK OS / Zipper OS / SPITI OS / Global / Operações]  
Fonte: [conversa Lucas / relatório / PRD / reunião / fonte viva]

### Fato
[O que foi observado ou dito.]

### Decisão
[O que ficou definido.]

### Aplicação operacional
[Como o Hermes deve agir daqui para frente.]

### Guardrails
[O que continua exigindo aprovação ou verificação.]

### Artefatos atualizados
- `...`

### Pendências
- [ ] ...
```

## Exemplo — relatório LK OS

Decisões como estas devem ficar em memória LK, não só no chat:

- 19h30 é exclusivo Loja Física/POS;
- relatório começa por dia/período e depois mês;
- vendedores aparecem no dia/período e no mês quando houver atribuição POS;
- share de marcas mensal mostra % de receita e BRL;
- categorias estranhas agrupam em `Outras marcas`;
- newsletter/e-mail tem subject, preheader e preheader oculto;
- decisões estratégicas e próximos passos vão para Lucas no Telegram; não para grupo/externo sem aprovação.

## Anti-padrões

- “Eu lembro do chat” → errado; salvar no Brain/skill.
- “Está no report gerado” → insuficiente; report é evidência, não fonte viva.
- “Está na memória global genérica” → insuficiente se a decisão é de empresa; salvar na empresa.
- “Atualizei o código mas não a skill” → incompleto se muda comportamento futuro.
- “Aprovação ampla autoriza enviar” → falso; envio externo exige aprovação atual com destinatário e payload.
