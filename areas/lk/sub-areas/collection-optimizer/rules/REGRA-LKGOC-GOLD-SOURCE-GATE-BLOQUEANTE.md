# Regra LKGOC — Gold Source Gate Bloqueante

Registrado em: 20260606T135341Z

## Por que existe
Após erro no lote Nike Dunk / Puma Speedcat / Adidas Gazelle / Yeezy / Labubu, fica proibido executar LKGOC por aproximação visual ou componente novo inventado.

## Regra bloqueante
Antes de qualquer write LKGOC em tema, Page, template, snippet ou seção:

1. Abrir `AGENTS.md` do Collection Optimizer.
2. Abrir playbook aplicável (`playbooks/full-lkgoc-rebuild.md` ou equivalente).
3. Localizar e registrar o **gold source visual/código** aprovado.
4. Provar no receipt qual asset/template será copiado/adaptado.
5. Acionar workers temporários **antes** da execução:
   - Collection Intake Classifier
   - LKGOC Experience Architect
   - Guia LK Editorial Writer
   - Shopify DEV Preview Builder
   - Visual QA Mobile/Desktop Worker
   - SEO/GEO Validator
   - Rollback & Receipt Verifier
6. Executar primeiro **uma única frente**, nunca lote de 5 direto.
7. Só replicar após QA visual aprovado da primeira frente.

## Proibições
- Proibido criar namespace novo como `lk-goc5` para simular LKGOC.
- Proibido criar layout novo para “parecer LKGOC”.
- Proibido usar placeholder visual/card vazio/imagem genérica.
- Proibido chamar de canônico se não for clone/adaptação de gold source registrado.
- Proibido corrigir incrementalmente em cima de base errada; se Lucas apontar fora do padrão, rollback primeiro.

## Definition of Done adicional
Para declarar feito:
- screenshot comparado contra gold source;
- HTML sem marcadores inventados;
- readback Admin API;
- receipt com gold source, diff, rollback e QA;
- se houver ambiguidade visual, marcar como **não aprovado** e pedir revisão antes de replicar.
