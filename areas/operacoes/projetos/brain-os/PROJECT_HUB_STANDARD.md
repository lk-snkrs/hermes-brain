# Brain OS — Project Hub Standard

## Quando criar um hub

Criar um hub canônico quando 3+ condições forem verdadeiras:

- mais de 100 artefatos ou volume alto de receipts/reports/work;
- múltiplos agentes ou perfis dependem do tema;
- há PRDs soltos sem estado atual consolidado;
- há risco de confundir histórico com fonte viva;
- existe risco de write externo;
- Lucas perguntou/corrigiu o estado recentemente;
- o tema cruza áreas de negócio.

## Estrutura obrigatória

```text
projetos/<slug>/
├── README.md
├── CURRENT_STATE.md
├── DECISIONS_AND_GUARDRAILS.md
├── ARTIFACT_INDEX.md
├── TIMELINE.md
├── NEXT_STEPS.md
└── manifest.json
```

## Papel de cada arquivo

- `README.md`: visão executiva, dono, status, links principais.
- `CURRENT_STATE.md`: estado atual, última evidência, fonte viva, pendências.
- `DECISIONS_AND_GUARDRAILS.md`: decisões válidas, bloqueios, autorização necessária.
- `ARTIFACT_INDEX.md`: índice dos principais artefatos existentes, com paths relativos.
- `TIMELINE.md`: evolução/histórico sem confundir com estado atual.
- `NEXT_STEPS.md`: próximas ações recomendadas, separando local/documental de externo/sensível.
- `manifest.json`: contagem, fontes, criado_em, escopo, paths e status.

## Regras de escrita

- Escrever resumo e apontar para evidência; não duplicar tudo.
- Preservar originals.
- Usar paths relativos ao Brain.
- Não copiar dados sensíveis.
- Marcar incerteza quando depender de fonte viva.
- Verificar após criar.
