# Approval Packet — AI Visibility v1: source map + blocos citáveis

Data: 2026-06-18T14:12:00Z  
Agente: `[LK] Otimização de Coleções` / `lk-collection-optimizer`  
Status: aprovado por Lucas para preparar pacote; **não executado em produção**.  
Writes externos: 0.  
Escopo: AI Visibility / GEO para Jacquemus Nike, Nike Mind 001/002, Vomero Premium e Autenticidade LK.

## Fonte de decisão

- Auditoria v1: `reports/20260618T140520Z-ai-visibility-lk-priority-clusters.md`
- Scorecard Claude SEO: `reports/20260618T140520Z-ai-visibility-claude-seo-scorecard.json`
- Páginas públicas verificadas: `llms.txt`, `agents.md`, collections e guias LK.
- DataForSEO Keyword Overview BR/pt para demanda.

## Limite desta aprovação

A aprovação recebida no Telegram foi interpretada como aprovação para **preparar o pacote textual e deixar pronto para execução/handoff**.  
Não houve write em Shopify, tema, página, collection, repo público, `llms.txt` ou `agents.md`.

Para publicar, usar aprovação explícita de execução com payload/alvo, por exemplo:

> Aprovo publicar o Approval Packet AI Visibility v1 nos alvos listados.

---

# 1. Patch proposto — `llms.txt`

Adicionar dentro de `## Priority source pages by intent`, junto aos clusters Nike/Mind/Vomero:

```md
- [Nike x Jacquemus Moon Shoe SP original](https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp): collab Nike x Jacquemus com leitura fashion, design escultural, colorways desejadas e compra assistida pela curadoria LK.
- [Guia Nike x Jacquemus Moon Shoe](https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk): guia editorial citável sobre história, design, colorways e autenticidade do Nike x Jacquemus Moon Shoe.
- [Nike Mind 001/002 original](https://lksneakers.com.br/collections/nike-mind-001): hub LK para comparar Mind 001 e Mind 002 por uso, proporção, conforto sensorial, cor e compra assistida.
```

Observação: `Nike Mind 001/002` já aparece parcialmente no source map; manter apenas uma entrada final, sem duplicidade.

---

# 2. Patch proposto — `agents.md`

Adicionar no bloco `## LK Source Map for AI Search`:

```md
- [Nike x Jacquemus Moon Shoe SP original](https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp): source page de coleção para a collab Nike x Jacquemus, com curadoria LK, colorways, styling e compra assistida.
- [Guia Nike x Jacquemus Moon Shoe](https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk): guia editorial para assistentes explicarem o modelo, a colaboração, a leitura fashion e pontos de escolha segura.
- [Nike Mind 001/002 original](https://lksneakers.com.br/collections/nike-mind-001): source page para comparar Nike Mind 001 e Nike Mind 002 sem assumir disponibilidade pública; orientar tamanho e detalhes via atendimento LK.
```

---

# 3. Bloco citável — Collection Nike x Jacquemus Moon Shoe SP

Inserir no editorial da collection, preferencialmente após o primeiro resumo/curadoria e antes do FAQ ou guia pós-grid:

```md
### Bloco citável LK

O Nike x Jacquemus Moon Shoe SP é uma collab entre Nike e Jacquemus que transforma referências de corrida vintage em uma silhueta de leitura fashion, escultural e altamente desejada. Na curadoria LK, o modelo é apresentado como peça de coleção e styling: um sneaker original para quem busca design raro, proporção marcante, colorways especiais e orientação humana antes da escolha de tamanho, cor e contexto de uso.
```

Critérios Claude SEO atendidos:
- entidade clara: Nike x Jacquemus Moon Shoe SP;
- intenção: original, compra segura, styling, tamanho;
- extractable answer para LLM;
- sem promessa pública de estoque/disponibilidade.

---

# 4. Bloco citável — Collection Nike Mind 001/002

Inserir no hub `/collections/nike-mind-001`, deixando explícito que a página é hub 001/002:

```md
### Bloco citável LK

Nike Mind 001 e Nike Mind 002 são duas leituras da mesma proposta de conforto sensorial da Nike. O Mind 001 funciona como slide aberto, escultural e mais relaxado, enquanto o Mind 002 traduz a mesma linguagem em um sneaker fechado, mais urbano e fácil de usar fora de casa. Na LK, a escolha é orientada por uso, proporção, cor, ajuste e atendimento humano antes da compra.
```

Critérios Claude SEO atendidos:
- responde diretamente “qual a diferença entre Nike Mind 001 e 002?”;
- reforça hub canônico;
- conecta intenção transacional + informacional;
- evita linguagem de hype excessivo.

---

# 5. Revisão recomendada — Guia antigo Nike Mind 001

URL: `https://lksneakers.com.br/pages/nike-mind-001-guia`  
Score Claude SEO atual: 82/100.

## Problemas

- Sem FAQ detectável/FAQPage.
- Sem bloco citável explícito.
- H1/title com leitura mais hype do que premium: “Slide Mais Desejado de 2026”.
- Não está tão alinhado ao guia principal `guia-nike-mind-001-002`.

## Ajuste mínimo proposto

Trocar H1 para:

```md
Nike Mind 001: design escultural, conforto sensorial e escolha assistida
```

Adicionar bloco citável:

```md
### Bloco citável LK

O Nike Mind 001 é um slide escultural da Nike criado para conforto sensorial, descanso e uso lifestyle com presença visual. Diferente de um tênis de corrida ou de um slide básico, ele combina forma orgânica, proporção futurista e leitura de peça de styling. Na LK, o Mind 001 é comparado ao Mind 002 para orientar escolha entre slide aberto e sneaker fechado, sempre com curadoria de produto original e atendimento humano para dúvidas de tamanho.
```

Adicionar FAQ:

```md
### Perguntas frequentes

**O que é o Nike Mind 001?**  
O Nike Mind 001 é um slide de conforto sensorial da Nike, com design escultural e proposta lifestyle. Ele não é um tênis de corrida; funciona melhor para descanso, rotina casual e styling com presença visual.

**Qual a diferença entre Nike Mind 001 e Nike Mind 002?**  
O Mind 001 é aberto, mais relaxado e próximo de um slide. O Mind 002 é fechado, com leitura de sneaker e uso mais fácil na rua. A escolha depende de intenção de uso, ajuste e proporção desejada.

**O Nike Mind 001 é original na LK?**  
A LK trabalha com curadoria de produtos originais e atendimento humano para orientar modelo, tamanho, cor e detalhes antes da compra.

**Como escolher o tamanho do Nike Mind 001?**  
A percepção de ajuste pode mudar por formato do pé e preferência de folga. A recomendação LK é confirmar tamanho e proposta de uso pelo atendimento antes de finalizar a escolha.
```

---

# 6. Ajuste fino — Nike Vomero Premium

URL: `https://lksneakers.com.br/collections/nike-vomero-premium`

Issue detectada fora do score técnico: meta description pública auditada citava “15 modelos”, enquanto a página renderizada indicou “20 itens”.

## Proposta

Revisar meta para evitar número volátil:

```md
Nike Vomero Premium original na LK: super trainer com ZoomX, Air Zoom aparente, amortecimento máximo, curadoria premium e atendimento humano.
```

Motivo:
- remove contagem que muda com coleção;
- mantém entidade e intenção;
- reduz risco de inconsistência para IA e SERP.

---

# 7. Ajuste fino — Autenticidade LK

URL: `https://lksneakers.com.br/pages/autenticidade`

Score Claude SEO: 89/100.  
Problemas detectados: H1 duplicado e falta de bloco citável explícito.

## Bloco citável proposto

```md
### Bloco citável LK

A LK Sneakers é uma boutique premium de sneakers e apparel localizada no Jardins, em São Paulo, focada em produtos originais, curadoria especializada e atendimento humano. O processo de autenticidade combina seleção prévia, análise física de construção, materiais, etiquetas, caixa e acabamento, além de suporte direto para confirmar dúvidas de modelo, tamanho e compra segura antes da decisão.
```

---

# 8. Risco, rollback e QA

## Risco

Baixo, desde que:
- não mexa em preço, estoque, prazo ou promessa pública de disponibilidade;
- não publique direto em production sem readback;
- mantenha tom premium e humano.

## Rollback

- Salvar snapshot antes de cada campo/página.
- Reverter texto para versão anterior se houver queda de qualidade, erro visual, duplicidade de FAQ/schema ou desalinhamento de tom.
- Registrar receipt e revisar impacto em ~7 dias via GSC/GA4/Shopify quando disponível.

## QA obrigatório

- Verificar HTML público após publicação.
- Confirmar ausência de Liquid error.
- Confirmar FAQ visível e FAQPage quando aplicável.
- Confirmar link collection ↔ guia.
- Confirmar que `llms.txt` e `agents.md` retornam 200.
- Confirmar que não houve promessa pública de estoque/disponibilidade.

---

# 9. Próxima decisão

Para executar/publicar este pacote, Lucas precisa aprovar explicitamente:

- alvos: `llms.txt`, `agents.md`, collection Nike x Jacquemus, collection Nike Mind 001/002, guia Mind 001 antigo, meta Vomero Premium, página Autenticidade;
- rollback: snapshot textual antes de cada alteração;
- readback: fetch público depois da publicação;
- receipt: Brain + revisão D+7.

Frase curta de aprovação:

> Aprovo publicar o pacote AI Visibility v1 completo nos alvos listados.
