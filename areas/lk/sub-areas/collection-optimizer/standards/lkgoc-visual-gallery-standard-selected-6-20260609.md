# LKGOC Standard — Galeria visual selecionada de 6 imagens

Data: 2026-06-09
Status: padrão operacional aprovado por Lucas para próximas coleções/guias LKGOC.
Origem: Guia LK New Balance 204L — Lucas pediu usar a mesma lógica como padrão das próximas coleções.

## Princípio
Para guias e páginas editoriais de coleção, a galeria visual não deve ser uma vitrine longa de produto isolado. O padrão é uma seleção enxuta e forte, com **6 imagens escolhidas editorialmente**, priorizando uso real, proporção no corpo e leitura aspiracional.

## Regra padrão
Usar uma galeria principal de **6 imagens** quando houver material suficiente:

1. **On feet / uso real** — melhor imagem para entender shape, volume e proporção no pé.
2. **Corpo inteiro / styling** — mostra como o sneaker conversa com silhueta e look.
3. **Close de proporção** — evidencia cabedal, altura, desenho e leitura low/profile ou chunky.
4. **Imagem aspiracional/editorial** — reforça desejo, moda e contexto premium.
5. **Referência editorial ou campaign context** — dá autoridade e repertório visual.
6. **Segundo on feet ou ângulo complementar** — confirma proporção e reduz dúvida de compra.

## Como aplicar
- Preferir imagens com produto em uso antes de packshot isolado.
- Packshots de produto entram em cards de produto ou apoio, não como eixo principal da galeria editorial.
- A legenda deve explicar o motivo comercial da imagem: proporção, styling, textura, volume, cor, uso ou decisão de compra.
- A galeria deve ajudar a responder: “como fica no pé/corpo?” e “combina com meu uso?”
- Se houver muitas imagens boas, selecionar as 6 mais fortes; não aumentar a grade sem motivo.
- Se houver menos de 6 boas, usar menos e marcar como limitação no QA/approval packet.

## Tom e hierarquia
- Premium, minimalista, humano e comercialmente útil.
- Evitar legenda genérica tipo “imagem do produto”.
- Usar linguagem de curadoria: proporção, leitura, textura, styling, presença visual, versatilidade.

## QA obrigatório
Antes de approval/promoção:
- DEV theme precisa estar com `role: unpublished` verificado por API.
- Confirmar ausência de `Liquid error`.
- Confirmar contagem da galeria no HTML/Playwright.
- Testar mobile e desktop.
- Registrar screenshots e rollback.
- Production apenas com aprovação explícita de Lucas.

## Exceções
- Para collection page puramente comercial, adaptar a lógica mantendo seleção enxuta, mas sem forçar bloco editorial longo.
- Para coleção sem campanha/on-feet disponível, usar imagens de produto apenas como fallback e recomendar captação/curadoria de assets.
- Qualquer mudança para galeria maior, novo layout ou comportamento visual diferente precisa ser marcada como exceção no approval packet.
