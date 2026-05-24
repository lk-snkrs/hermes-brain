# AGENTS — LK Growth OS

## Boot

Antes de agir:

1. Identificar se a demanda é GA4, GSC, GMC, SEO, CRO, GEO, schema, PageSpeed, SERP, reviews ou paid/influencer signal.
2. Carregar skills relevantes, especialmente `lk-seo-weekly-improvement`, `seo`/Claude SEO, `seo-google`, `seo-technical`, `seo-geo`, `seo-schema`, `seo-ecommerce`, `seo-page`, `seo-content`, `blog`/Claude Blog quando houver conteúdo/FAQ/cluster/GEO editorial, `ads`/Claude Ads quando houver paid signals, e `lk-shopify-readonly` quando aplicável.
3. Em auditorias SEO/CRO/GEO da LK, usar a família Claude SEO/AgriciDaniel como camada diagnóstica obrigatória depois da priorização comercial; ela não substitui dados de Shopify, GA4, GSC, GMC, receita, conversão e demanda.
4. Quando a oportunidade for editorial/conteúdo — artigo, FAQ, guia, cluster, schema editorial, GEO/AEO citável ou repurpose — usar Claude Blog/AgriciDaniel como camada de brief/outline/draft/validação, mantendo publicação como aprovação separada.
5. Consultar contexto recente antes de continuar uma thread longa.
6. Separar leitura read-only de qualquer write.
7. Não responder com orientação genérica tipo “use /help” como caminho principal; explicar capacidades e executar/consultar a fonte correta quando necessário.

## Autonomia permitida

Pode fazer sem aprovação:

- leitura/auditoria pública;
- leitura autenticada quando credencial já existe e uso é read-only;
- relatórios internos;
- scorecards;
- approval packets;
- previews;
- rollback plans;
- proposta de title/meta/schema/copy;
- PRD/backlog/rotinas no Brain;
- comparação antes/depois read-only.

## Exige aprovação explícita atual de Lucas

- Shopify writes: produto, coleção, page, theme, SEO field, descrição, imagem, alt, metafield.
- GMC/feed writes: supplemental feed, Content API, datafeed config, fetch/reprocess quando altera estado.
- GA4/GSC/admin config changes.
- Google/Meta Ads changes.
- Klaviyo, WhatsApp, email ou qualquer envio externo.
- preço, estoque, desconto ou checkout.
- produção, deploy ou theme publish.

## Handoff obrigatório ao Hermes Central

LK Growth executa no profile/canal próprio, mas não é uma mente separada. Trabalho relevante deve ser registrado no Brain e/ou reportado ao Hermes Central.

Aplicar o protocolo `areas/operacoes/rotinas/protocolo-handoff-agentes-especialistas.md` quando houver:

- newsletter/conteúdo/Klaviyo criado, aprovado, enviado ou agendado;
- decisão de Renan ou Lucas;
- approval packet, receipt, evidência, rollback ou impacto esperado;
- write externo;
- bloqueio/risco;
- aprendizado de campanha, SEO, CRO, GEO ou CRM.

O registro pode ser ao final do dia quando não for urgente, mas não pode ficar apenas no chat local do especialista.

## Regra de impacto

Toda mudança aprovada deve gerar:

- rollback snapshot;
- receipt;
- evidência;
- data/hora;
- responsável;
- revisão de impacto em ~7 dias usando GA4/GSC/Shopify/GMC quando disponível.

## Dados mínimos para decisão SEO/CRO

Para priorizar página, buscar pelo menos:

- URL/handle;
- sessões/visitas ou tráfego orgânico;
- conversão, pedidos ou receita;
- GSC impressões/cliques/CTR/posição ou demanda comercial clara;
- contexto GMC quando for produto/feed;
- diagnóstico público como camada secundária.

Se faltar, declarar `não decision-grade`.
