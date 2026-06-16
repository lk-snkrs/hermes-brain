# REGRA — LKGOC textos e seleção de imagens

Registrado em: 20260609T120721Z
Status: **CANÔNICO / BLOQUEANTE PARA PRODUCTION**

## Decisão operacional

Toda coleção LKGOC deve ter textos e imagens produzidos por um processo auditável, antes de qualquer aprovação para Production.

O agente não deve inventar contexto, imagem, fonte, tendência, release, material, collab ou atributo do produto. Tudo que entra no texto e no hero precisa estar apoiado em evidence packet, fonte oficial, fonte editorial reconhecível, SERP/GSC/DataForSEO quando disponível, ou Shopify/read-only.

## Como fazer os textos

### 1. Evidence antes de escrever

Antes do draft, criar/atualizar o evidence packet da coleção com:

- fonte oficial da marca/modelo/collab;
- páginas editoriais reconhecíveis;
- SERP e concorrentes;
- People Also Ask/perguntas reais;
- GSC/DataForSEO quando disponível;
- Shopify/read-only: produtos, handle, SEO atual, descrição atual, tags/metafields relevantes;
- fatos confirmados vs interpretações.

Se faltarem dados autenticados de demanda/conversão/GSC, marcar como limitação; ainda pode haver preview editorial, mas não chamar priorização de decision-grade.

### 2. Estrutura de texto LKGOC

Para cada coleção, produzir:

- **Kicker** curto, premium e específico;
- **Headline** editorial, não genérica;
- **Intro/hero** com intenção, silhueta, materiais, contexto de uso e curadoria LK;
- **Guia pós-grid** com densidade semelhante ao Gold Source 204L;
- **FAQ único** baseado em dúvidas reais, sem duplicar FAQ/schema existente;
- **Title/meta** quando fizer parte do pacote;
- **Schema FAQ/Product/Collection quando aplicável**;
- **Referências editoriais e contexto**, quando houver guia dedicado/source page.

### 3. Tom LK obrigatório

- Premium, minimalista, humano e comercialmente inteligente.
- Foco em curadoria exclusiva, autenticidade, proporção, material, styling, escolha assistida e atendimento humano.
- Não usar linguagem pública de pronta entrega/encomenda/estoque como taxonomia.
- Disponibilidade, tamanho e prazo ficam para atendimento/chat quando necessário.
- Não exagerar claims: se não há fonte, não afirmar.

### 4. Critérios de qualidade

O texto reprova se:

- parece SEO genérico;
- troca produto-first por blog;
- inventa tendência ou história sem fonte;
- usa termos de estoque/pronta entrega publicamente;
- duplica FAQ/schema;
- não diferencia modelo, material, colorway ou intenção de uso;
- não conversa com o grid real da coleção.

## Como selecionar imagens

### 1. Objetivo visual

Hero LKGOC deve parecer editorial/lifestyle, com pessoa usando ou contexto visual de moda/cultura. Packshot, PDP isolado, foto de produto em fundo branco ou render sem contexto não é hero LKGOC.

### 2. Fontes prioritárias

Buscar e registrar candidatas a partir de:

1. campanhas oficiais da marca/collab;
2. press/release oficial;
3. editoriais e veículos reconhecíveis: Vogue, Vogue Brasil, Highsnobiety, Hypebeast, GQ, Complex, Sneaker News, WWD, Harper's Bazaar, Elle, Footwear News, NSS, The Business of Fashion quando relevante;
4. varejistas/editoriais premium apenas como apoio;
5. conteúdo próprio LK, quando existir e for melhor que a fonte externa.

### 3. Media manifest obrigatório

Para cada coleção, registrar um media manifest com:

- URL da imagem/página fonte;
- veículo/fonte;
- modelo/cor/contexto mostrado;
- uso pretendido: hero principal, collage secundário, guia, referência;
- motivo da escolha;
- risco/licença/atribuição;
- alternativa se a imagem não puder ir para Production.

### 4. Seleção visual

Priorizar imagens que tenham:

- pessoa usando o produto;
- styling compatível com o público LK;
- leitura premium/minimalista/editorial;
- boa proporção para crop desktop/mobile;
- contraste suficiente com o shell 204L;
- coerência com o texto e os produtos da coleção.

### 5. Bloqueios

Production fica bloqueada se:

- hero principal for packshot/PDP/produto isolado sem aprovação excepcional;
- fonte da imagem não estiver registrada;
- imagem tiver risco óbvio/licença indefinida sem alternativa;
- o crop mobile/desktop quebrar o padrão 204L;
- houver placeholder visível;
- visual divergir do Gold Source 204L.

DEV pode usar placeholder explícito para construir preview, mas deve marcar `PRODUCTION_BLOCKED` até trocar por asset aprovado.

## Output obrigatório por coleção

Cada execução LKGOC Full/Lite deve gerar ou atualizar:

- evidence packet;
- text packet;
- media manifest;
- template/metafields map;
- QA visual 204L side-by-side;
- approval packet;
- rollback/receipt.

## 2.1. Description Packet obrigatório

Além do pacote textual geral, cada coleção LKGOC deve passar pelo quality gate de descrição definido em `REGRA-LKGOC-DESCRICAO-COLECAO-QUALITY-GATE-20260615.md`.

Descrições genéricas, com tom de sistema ou sem densidade premium ficam bloqueadas como `COPY_BLOCKED / NÃO LKGOC`.
