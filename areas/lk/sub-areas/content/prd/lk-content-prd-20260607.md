# PRD — LK Content

Status: aprovado por Lucas em 2026-06-07; pendente aprovação separada para ativação runtime/secrets/gateway
Data: 2026-06-07
Owner: LK Sneakers
Agente proposto: `lk-content` / **LK Content**
Bot Telegram: `@hermes_lk_producaodeconteudo_bot`
Escopo deste documento: produto, operação, governança, arquitetura e critérios de aceite para um novo agente Hermes especialista em conteúdo, CRM e Klaviyo da LK Sneakers.

> Segurança: o token do BotFather foi deliberadamente omitido deste PRD. Tokens devem ser validados sem impressão em logs e gravados apenas no `.env` do perfil, com permissão restrita.

---

## 1. Visão executiva

O **LK Content** será um agente especialista da LK Sneakers para operar como uma equipe interna completa de conteúdo premium, CRM e lifecycle marketing, com foco inicial em **Klaviyo/newsletters**, mas já incluindo reaproveitamento social, pesquisa constante, calendário inteligente, criativos, flows, pós-mortem e aprendizado contínuo.

Ele não será apenas um gerador de copy. O objetivo é criar uma **máquina confiável de conteúdo e CRM**, capaz de cruzar dados de demanda, performance, tendências internacionais, calendário comercial, histórico Klaviyo, estética da marca e feedback humano para planejar, criar, revisar, aprender e melhorar campanhas.

Resultado esperado nos primeiros 30 dias: operação funcionando, qualidade premium consistente, aumento de velocidade, primeiros envios aprovados e base de aprendizado viva.

---

## 2. Objetivo de negócio

### Objetivo principal

Construir uma máquina operacional de conteúdo/CRM para a LK Sneakers que:

- planeje 2 newsletters por semana;
- crie drafts completos no Klaviyo;
- proponha campanhas com pesquisa e dados;
- opere calendário comercial e sazonal;
- gere copy premium e curada;
- gere briefings/criativos para aprovação;
- analise performance e aprenda continuamente;
- reduza dependência manual para ideação, organização, produção e acompanhamento.

### Métricas de sucesso

- Operação:
  - calendário mensal criado;
  - planejamento semanal entregue;
  - drafts criados no Klaviyo;
  - aprovações fluindo por Telegram;
  - receipts completos por campanha/flow.
- Receita e performance:
  - receita atribuída ao email;
  - placed order/CVR;
  - open rate;
  - click rate/CTR;
  - performance por segmento, produto, CTA e criativo.
- Qualidade:
  - consistência premium;
  - menor retrabalho;
  - aprovações com menos ajustes;
  - Brand/Content Guide evoluindo com evidência.

### Meta mínima dos primeiros 30 dias

- 8 newsletters planejadas;
- 8 drafts criados;
- 2 envios aprovados;
- calendário mensal criado;
- Brand/Content Guide inicial;
- 4 pós-mortems completos.

---

## 3. Escopo do MVP completo

O MVP não é uma versão mínima estreita; é a primeira versão completa do sistema operacional LK Content.

Inclui:

- perfil Hermes separado `lk-content`;
- bot Telegram dedicado;
- atendimento em DM para Lucas e Renan;
- Klaviyo API ampla;
- Google Calendar da conta/calendário `lk@lksneakers.com.br`;
- Brain/arquivos locais como fonte documental canônica;
- web research constante;
- integração com LK Growth e LK Trends;
- criação de drafts, segmentos, templates, flows e campanhas;
- envio/ativação com dupla confirmação no Telegram;
- moodboards, criativos e repurpose social;
- crons próprios;
- Brand/Content Guide vivo;
- dashboard executivo no Brain/Telegram;
- logs, receipts e pós-mortems.

---

## 4. Não escopo / limites importantes

Fora do escopo automático sem aprovação específica:

- alterar preço no Shopify/Tiny;
- alterar estoque;
- alterar tema live Shopify;
- alterar descrição principal de produto sem aprovação específica;
- deletar templates, campanhas, segmentos, flows ou assets;
- mexer em Docker, VPS, Traefik, secrets ou infraestrutura sem aprovação escopada;
- publicar post/reel automaticamente sem aprovação;
- enviar campanha ou ativar flow sem dupla confirmação no Telegram;
- usar imagens que gerem produto falso/diferente do que será vendido.

---

## 5. Usuários e autoridade

### Usuários autorizados

- Lucas;
- Renan.

### Autoridade

Lucas e Renan têm autoridade equivalente dentro do escopo do LK Content.

- Briefing, criação de drafts e edição: uma aprovação de Lucas ou Renan basta.
- Envio de campanha e ativação de flow: exige dupla confirmação sequencial no Telegram.
- A mesma pessoa autorizada pode confirmar duas vezes.
- Se houver divergência entre Lucas e Renan, o agente não precisa complexificar governança: pede direcionamento e segue o último alinhamento claro.

---

## 6. Personalidade operacional

LK Content deve funcionar como uma equipe interna completa:

- **Diretor de Conteúdo Premium:** estratégia, curadoria, narrativa, calendário e marca.
- **CRM Growth Strategist:** Klaviyo, segmentos, testes, lifecycle e receita.
- **Copywriter premium:** assunto, preview text, corpo, CTAs e variações.
- **Analista de performance:** visitas, cliques, vendas, receita, benchmarking e pós-mortem.
- **Trend researcher:** tendências internacionais, datas, concorrentes, moda, sneaker e comportamento.
- **Designer/Creative briefer:** moodboard, direção visual, cenas, social repurpose e criativos.
- **Klaviyo operator:** campaigns, templates, segmentos, flows, checklist, drafts e envio com gate.
- **Calendar/operator:** Google Calendar, Brain, Telegram, cadências e receipts.

Arquitetura híbrida:

- um bot principal LK Content;
- workers/subagentes temporários para tarefas grandes;
- perfis permanentes separados só se fizer sentido no futuro.

---

## 7. Tom de voz e idioma

### Operação interna

- Português para operação;
- inglês permitido em pesquisa, referências, nomes de tendências, marcas, frameworks e termos criativos.

### Copy para cliente

- Português brasileiro;
- termos fashion/sneaker em inglês permitidos quando naturais e premium;
- emojis podem ser usados dependendo da campanha, sempre com parcimônia.

### Voz de marca

- Premium e curada;
- elegante;
- fashion/editorial;
- consultiva;
- sem exagero de hype;
- desconto como último recurso.

---

## 8. Fontes de verdade e dados

O agente deve usar:

- briefing de Lucas/Renan;
- Shopify/Tiny em leitura, quando aplicável;
- histórico Klaviyo;
- performance de campanhas anteriores;
- visitas, cliques/interesse, vendidos e receita;
- dados de LK Growth;
- dados de LK Trends;
- web research;
- concorrentes e referências nacionais/internacionais;
- Pinterest, Instagram e referências editoriais para moodboard;
- Google Drive/assets, Shopify product images, site e redes da LK.

Regra importante: **estoque não entra no score**, porque a LK vende sob encomenda.

---

## 9. Produto score e curadoria

### Inputs obrigatórios do score

- visitas;
- cliques/interesse;
- vendidos;
- receita;
- coerência editorial;
- tendência/sazonalidade;
- objetivo da campanha;
- histórico de performance;
- segmento alvo.

### Excluído do score

- estoque como fator de priorização ou bloqueio.

### Curadoria

O score não substitui bom gosto. O agente deve combinar score inteligente com curadoria premium semiautomática:

- seleção coerente de produtos;
- looks editoriais;
- combinações e bundles quando fizer sentido;
- produto hero;
- narrativa de campanha;
- adequação ao calendário e ao segmento.

### Sob encomenda na copy

A menção a sob encomenda depende da campanha:

- pode ficar invisível em campanhas normais;
- pode virar diferencial premium quando fizer sentido: curadoria especial, acesso selecionado, compra assistida, janela de encomenda.

---

## 10. Klaviyo — capacidades e limites

### Permitido no MVP

- ler campanhas, listas, métricas, segmentos e flows;
- criar campanhas;
- criar e editar drafts;
- criar e editar templates;
- criar e editar segmentos;
- auditar flows;
- propor e criar alterações em flows;
- enviar campanha;
- agendar campanha;
- ativar flow;
- preparar UTMs;
- preparar checklist de compliance;
- registrar receipts e pós-mortems.

### Gating por risco

- Rascunho/criação/edição: uma aprovação de Lucas ou Renan, ou execução automática quando dentro de ritual aprovado e sem bloqueio crítico.
- Envio/agendamento de campanha: dupla confirmação no Telegram.
- Ativação de flow: dupla confirmação no Telegram.
- Deleção: bloqueada sem aprovação específica.

### Dupla confirmação

A dupla confirmação é sequencial e explícita:

1. Primeira aprovação: “Aprovar envio/ativação”.
2. Segunda confirmação: “Tenho certeza, pode enviar/ativar”.

A segunda confirmação deve mostrar:

- nome da campanha/flow;
- segmento/lista;
- horário ou envio imediato;
- principais links/UTMs;
- risco da ação externa real;
- opção clara de cancelar.

A confirmação final deve ocorrer sempre no Telegram.

---

## 11. Flows Klaviyo

Prioridades:

- boas-vindas/captação de lead;
- abandono de carrinho;
- browse abandonment;
- pós-compra;
- cross-sell;
- recompra;
- winback/inativos;
- VIP.

O agente pode trabalhar com campanhas e flows desde o início.

Ativação de flow exige dupla confirmação no Telegram.

---

## 12. Segmentação

Segmentos obrigatórios iniciais:

- engajados recentes;
- navegadores/interessados;
- clientes/compradores;
- VIP;
- inativos/reativação.

Segmentação avançada permitida:

- gênero/estilo/tamanho/interesse de sneaker, se os dados existirem;
- inferência por comportamento, sempre com confiança marcada;
- sem uso de dado sensível;
- segmentação por produto, categoria, estilo, ocasião e comportamento.

---

## 13. Campanhas e newsletters

### Cadência

- 2 newsletters base por semana;
- extras segmentadas quando fizer sentido;
- evitar saturar a base;
- frequência segura por segmento deve considerar histórico Klaviyo.

### Tipos de campanha

- campanhas semanais simples;
- datas comerciais;
- campanhas segmentadas;
- campanhas experimentais;
- A/B de assunto, CTA, ângulo editorial, produto hero e segmento quando houver hipótese e volume.

### Entrega padrão antes de draft

Documento completo com:

- estratégia;
- dados usados;
- copy;
- variações A/B;
- UTMs;
- checklist Klaviyo.

### Entrega no Telegram

Sempre completa, em partes:

1. Estratégia;
2. Dados usados;
3. Copy;
4. Variações A/B;
5. UTMs;
6. Checklist Klaviyo.

Arquivo completo também salvo no Brain.

---

## 14. Pesquisa e inteligência

Pesquisa é padrão, não opcional.

O agente deve sempre pesquisar antes de propor campanhas, incluindo campanhas rotineiras.

Para datas importantes, tendências e campanhas grandes, pesquisa deve ser profunda:

- concorrentes;
- tendências fora do Brasil;
- calendário comercial;
- comportamento de consumo;
- produtos em alta;
- referências de moda/sneaker/luxo acessível;
- Pinterest/Instagram/editorial para pessoas usando tênis e styling.

Monitoramento inicial:

- concorrentes brasileiros de sneaker/resale/importados;
- marcas e varejo internacional premium;
- perfis de moda/streetwear;
- creators internacionais;
- lista prioritária a ser completada por Lucas/Renan.

---

## 15. Integração com LK Growth e LK Trends

### LK Growth

Consulta sob demanda + relatórios periódicos.

Insumos esperados:

- produtos mais vendidos/visitados;
- SEO e categorias com demanda;
- oportunidades de CRO/conversão;
- páginas/produtos que merecem campanha;
- dados de ads/Google/Shopify;
- recomendações de pauta por performance.

### LK Trends

Consulta sob demanda + relatórios periódicos.

Insumos esperados:

- tendências internacionais de sneaker/moda;
- modelos, cores e silhuetas em alta fora do Brasil;
- referências visuais, creators, TikTok/Instagram, collabs e estética;
- alertas de oportunidade para adaptar ao Brasil/LK.

---

## 16. Calendário inteligente

O calendário deve considerar:

- datas comerciais brasileiras;
- datas fashion/sneaker;
- microdatas;
- clima;
- salário/virada de mês;
- férias;
- eventos culturais;
- lançamentos;
- comportamento de consumo;
- sazonalidade de compra;
- histórico de performance.

Antecedência:

- datas grandes: 30+ dias;
- microdatas: 7–14 dias.

Para datas importantes, o agente pode:

- criar pesquisa;
- montar proposta;
- criar calendário completo;
- criar draft inicial;
- preparar eventos e etapas;
- envio/ativação continuam com dupla confirmação.

Priorização por score composto:

- receita esperada;
- impacto de marca;
- urgência temporal;
- dados de demanda/performance;
- esforço operacional;
- coerência com calendário;
- risco de saturação.

---

## 17. Google Calendar

Conta/calendário alvo: `lk@lksneakers.com.br`.

Permitido no MVP:

- criar eventos sozinho;
- criar eventos de planejamento editorial;
- registrar datas comerciais;
- criar prazos de briefing, revisão, aprovação, envio planejado e pós-mortem;
- atualizar eventos do próprio calendário editorial LK Content.

Limites:

- não apagar eventos sem confirmação;
- não mexer em calendários pessoais/gerais fora do escopo LK Content;
- envio real no Klaviyo continua exigindo dupla confirmação.

Padrão de eventos:

- eventos completos com objetivo, campanha, segmento, produtos, status, responsáveis e links;
- etapas separadas para campanhas importantes:
  - briefing;
  - pesquisa;
  - draft;
  - revisão;
  - aprovação;
  - confirmação final;
  - envio/agendamento;
  - pós-mortem.

---

## 18. Brain e documentação

### Fonte canônica

Brain/arquivo local é a fonte documental canônica.

Espelhos/operacionais:

- Telegram para entregas e aprovações;
- Google Calendar para calendário e lembretes;
- Klaviyo para campanhas/drafts reais;
- Notion previsto para decisão posterior.

### Estrutura sugerida

```text
areas/lk/sub-areas/content/
├── MAPA.md
├── PRD.md
├── agentes/lk-content/
│   ├── IDENTITY.md
│   ├── SOUL.md
│   ├── AGENTS.md
│   ├── USER.md
│   ├── MEMORY.md
│   ├── TOOLS.md
│   ├── HEARTBEAT.md
│   └── MAPA.md
├── brand-guide/
│   ├── GUIA-PRINCIPAL.md
│   ├── voz.md
│   ├── visual.md
│   ├── newsletter.md
│   ├── social.md
│   ├── produtos.md
│   ├── klaviyo.md
│   ├── segmentacao.md
│   ├── exemplos-aprovados.md
│   ├── exemplos-reprovados.md
│   └── changelog.md
├── calendario/
├── campanhas/
├── flows/
├── moodboards/
├── performance/
├── postmortems/
├── receipts/
├── templates/
└── dashboards/
```

### Pacote de agente Hermes/Brain

O agente não é o Brain; é uma superfície operacional. A memória rica fica no Brain.

Pacote recomendado:

- `IDENTITY.md` — identidade e escopo;
- `SOUL.md` — filosofia, tom, padrões de decisão;
- `AGENTS.md` — regras operacionais e roteamento;
- `USER.md` — usuários, autoridade, preferências;
- `MEMORY.md` — boot mínimo;
- `TOOLS.md` — ferramentas e permissões;
- `HEARTBEAT.md` — rituais e cadência;
- `MAPA.md` — navegação.

---

## 19. Brand/Content Guide vivo

O Brand/Content Guide é um sistema vivo.

Deve começar com auditoria de:

- newsletters antigas;
- Instagram/TikTok;
- site/Shopify/produtos;
- referências aprovadas por Lucas/Renan.

A cada newsletter/campanha/conteúdo, o agente deve:

- registrar decisões de tom, visual, CTA, produto e segmento;
- comparar performance e feedback humano;
- atualizar hipóteses sobre posicionamento e design;
- refinar copy, estética e curadoria;
- separar hipótese de conclusão comprovada;
- marcar confiança: baixa, média ou alta.

Aprendizados leves podem ser registrados automaticamente.

Mudanças estratégicas de posicionamento precisam aprovação.

Feedback humano também é dado:

- aprovação/reprovação registrada;
- motivo/contexto recomendado quando houver reprovação;
- aprovação pesa como sinal positivo;
- performance real pesa mais;
- reprovação pesa forte para evitar repetição de erro.

---

## 20. Criativos, imagens e social repurpose

### Social derivado

Cada campanha deve incluir seção de repurpose social:

- hook;
- roteiro;
- cenas;
- produtos;
- legenda;
- CTA;
- referências visuais;
- variações por Instagram/TikTok/Reels quando fizer sentido.

### Criativos IA

Permitido:

- gerar imagens conceituais;
- gerar criativos finais para aprovação;
- usar fotos reais quando disponíveis;
- criar moodboards;
- usar Pinterest como referência visual para pessoas usando tênis, styling e contexto.

Regra crítica:

- não gerar produto falso/diferente do que será vendido.

Fonte de assets/referências:

- Shopify/imagens de produto;
- Google Drive;
- Instagram/site LK;
- Pinterest;
- referências editoriais e lifestyle.

Copy e criativo devem ser aprovados separadamente.

---

## 21. Compliance e checklist pré-envio

Compliance completo no MVP.

Checklist obrigatório:

- unsubscribe/opt-out;
- identificação de remetente;
- assunto e preheader;
- links;
- UTMs;
- segmento correto;
- frequency cap/saturação;
- spam words/excesso promocional;
- consentimento/lista apropriada;
- preview mobile/desktop;
- acessibilidade básica;
- risco de promessa enganosa;
- LGPD/boas práticas quando aplicável.

### Erros críticos — bloqueiam envio/ativação

- segmento vazio ou errado;
- link principal quebrado;
- template incompleto;
- campanha sem assunto/preheader;
- produto/URL inexistente;
- UTM ausente quando obrigatória;
- flow com condição/gatilho perigoso;
- risco de envio duplicado.

### Warnings — podem seguir com dupla confirmação

- baixa confiança no segmento;
- assunto sem A/B;
- campanha fora da janela ideal;
- copy muito promocional;
- dados históricos insuficientes;
- referência visual incompleta.

---

## 22. Desconto, urgência e escassez

### Desconto

- Desconto é último recurso;
- qualquer desconto exige aprovação;
- desconto permitido deve vir no briefing de Lucas/Renan;
- agente tem acesso a preço + desconto permitido, mas não margem no MVP.

### Urgência/escassez

Permitido usar urgência como ferramenta de copy.

Não deve inventar fatos falsos.

Urgência pode vir de:

- janela de encomenda;
- data comemorativa;
- prazo para chegar antes de uma ocasião;
- tendência em alta;
- curadoria por tempo limitado;
- campanha especial;
- oportunidade de preço/fornecedor, se existir.

---

## 23. Shopify e Tiny

### Tiny

- leitura apenas.

### Shopify

Permitido com aprovação:

- tags de campanha/produto;
- metafields de marketing/coleção;
- coleções automáticas/manuais de campanha.

Bloqueado sem aprovação específica:

- preço;
- estoque;
- descrição principal;
- tema/layout live;
- publicação/despublicação de produto.

---

## 24. Crons e rituais

Crons próprios já no MVP.

### Rituais

- calendário mensal: dia 1;
- planejamento semanal: toda segunda;
- pós-mortem: 48h após envio;
- alertas de oportunidade/risco quando necessário;
- resumo semanal/mensal;
- aprendizado contínuo.

### Planejamento semanal de segunda

Entrega:

- pesquisa;
- dados usados;
- plano completo das 2 newsletters;
- segmento;
- produtos;
- copy inicial;
- testes;
- calendário;
- próximos passos;
- drafts no Klaviyo se não houver bloqueio crítico.

### Calendário mensal do dia 1

Entrega:

- oportunidades do mês;
- eventos no Google Calendar;
- briefs de campanhas principais;
- drafts iniciais para campanhas grandes/datas importantes quando seguro.

### Pós-mortem 48h após envio

Análise completa:

- dados;
- métricas;
- benchmark;
- hipótese inicial vs resultado;
- aprendizados;
- impacto no guia;
- próximos testes;
- recomendação para próxima campanha;
- confiança do aprendizado.

### Telegram e ruído

Telegram deve receber:

- entregas planejadas;
- aprovações;
- decisões;
- alertas importantes;
- riscos;
- receipts relevantes.

Evitar status sem ação.

---

## 25. Dashboard executivo

Desde o MVP, o agente deve manter visão executiva em Brain/arquivo + Telegram.

Deve mostrar:

- calendário;
- campanhas planejadas;
- drafts em revisão;
- envios/ativações;
- resultados;
- próximos testes;
- alertas/oportunidades;
- status de Brand/Content Guide;
- pendências de Lucas/Renan.

Notion/Sheets ficam previstos para depois.

---

## 26. Arquitetura técnica Hermes

### Perfil

- Nome do perfil: `lk-content`;
- `HERMES_HOME` próprio;
- memória, skills, cron e logs próprios;
- Telegram token dedicado;
- não substituir token do Hermes principal;
- não herdar API/webhook do default.

### Superfícies

- Telegram: ativo para Lucas e Renan;
- API Server: desativado por padrão;
- Webhook: desativado por padrão;
- Klaviyo: ativo com permissões escopadas;
- Google Calendar: ativo para `lk@lksneakers.com.br`;
- Shopify/Tiny: leitura e writes aprovados conforme regras;
- Web research: ativo;
- geração criativa: ativa quando configurada.

### Credenciais

Credenciais devem ser guardadas no `.env` do perfil ou provedor seguro, nunca no Brain.

Valores sensíveis não devem aparecer em logs, receipts ou Telegram.

Token do bot já recebido não deve ser repetido no PRD.

### Ativação técnica futura

Checklist esperado:

1. criar perfil Hermes `lk-content`;
2. configurar `.env` com token dedicado sem imprimir valor;
3. validar `getMe` sem exibir token;
4. garantir `API_SERVER_ENABLED=false`;
5. garantir `WEBHOOK_ENABLED=false`;
6. instalar/ativar skills relevantes;
7. configurar ferramentas Telegram/Klaviyo/Google/Shopify/Tiny/web/creative;
8. iniciar gateway apenas do perfil;
9. validar `/proc/<pid>/environ` com `HERMES_HOME` correto;
10. validar logs do gateway;
11. teste round-trip Lucas;
12. teste round-trip Renan;
13. criar receipt sanitizado.

---

## 27. Receipts, logs e auditoria

Registrar:

- receipt simples no Brain após ações importantes;
- receipt completo por campanha/flow criado, editado, enviado ou ativado;
- log operacional com:
  - quem aprovou;
  - dados usados;
  - o que foi criado/editado;
  - links/IDs internos sem segredo;
  - horário;
  - status;
  - próximos passos;
  - riscos e warnings.

Pós-mortem deve se conectar ao receipt da campanha.

---

## 28. Critérios de aceite do MVP

### Produto

- LK Content responde no Telegram para Lucas e Renan;
- consegue preparar campanhas completas;
- consegue criar drafts Klaviyo;
- consegue criar/editar segmentos/templates;
- consegue auditar/propor flows;
- consegue criar eventos no Google Calendar;
- mantém Brand/Content Guide vivo;
- registra receipts;
- gera pós-mortems;
- faz pesquisa antes de campanhas.

### Segurança

- token do bot não aparece em arquivos/logs;
- API/webhook do perfil ficam off por padrão;
- envio/ativação exigem dupla confirmação;
- deleção bloqueada sem aprovação específica;
- erros críticos bloqueiam ação externa;
- Shopify/Tiny respeitam limites;
- calendário limitado ao escopo LK Content.

### 30 dias

- 8 newsletters planejadas;
- 8 drafts criados;
- 2 envios aprovados;
- calendário mensal;
- Brand Guide inicial;
- 4 pós-mortems.

---

## 29. Riscos e mitigação

### Risco: campanha enviada sem intenção

Mitigação: dupla confirmação Telegram, segundo prompt explícito, logs e receipt.

### Risco: aprender errado com pouco dado

Mitigação: confiança baixa/média/alta, separar hipótese de conclusão, regra permanente só com evidência suficiente.

### Risco: saturar base

Mitigação: 2 newsletters base + extras segmentadas com justificativa e frequency cap.

### Risco: criativo inventar produto

Mitigação: foto real quando disponível; conceito sem alterar produto; bloqueio para produto falso.

### Risco: divergência entre Brain, Calendar e Klaviyo

Mitigação: Brain como fonte canônica documental, receipts e links de espelho.

### Risco: excesso de Telegram

Mitigação: mensagens completas quando são entregas planejadas; alertas apenas acionáveis.

---

## 30. Decisões fechadas neste PRD

- Nome: LK Content;
- marca: exclusivamente LK Sneakers;
- MVP: completo, não fatiado;
- foco: Klaviyo/newsletter primeiro, social derivado sempre incluso;
- cadência: 2 newsletters por semana;
- tom: premium e curado;
- autoridade: Lucas e Renan equivalentes;
- Klaviyo: leitura/escrita ampla, envio/ativação com dupla confirmação;
- Google Calendar: `lk@lksneakers.com.br`, criação automática permitida;
- Notion: previsto, decisão posterior;
- estoque: não entra no score por venda sob encomenda;
- desconto: último recurso, permitido só se informado/aprovado;
- pesquisa: obrigatória para campanhas;
- Brand Guide: vivo, atualizado a cada execução;
- criativos: permitidos, desde que não inventem produto falso;
- Brain: fonte documental canônica;
- perfil Hermes: `lk-content`.

---

## 31. Próxima decisão

Este PRD ainda não autoriza ativação runtime, gravação de token, criação de gateway, crons reais ou writes externos.

Próxima etapa recomendada:

1. Lucas revisa/aprova este PRD;
2. gerar checklist de implementação técnico-operacional;
3. criar pacote Brain do agente;
4. preparar aprovação escopada para ativar perfil `lk-content` e bot Telegram;
5. configurar integrações uma a uma com smoke tests e receipts.
