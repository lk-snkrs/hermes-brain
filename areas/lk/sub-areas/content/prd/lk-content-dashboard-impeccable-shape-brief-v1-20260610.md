# LK Content Dashboard — Impeccable Shape Brief v1

Data: 2026-06-10
Status: aguardando confirmação de Lucas antes de código
Registro: product UI

## 1. Feature Summary

Refazer o LK Content Dashboard do zero como uma superfície administrativa premium para Lucas/Renan operarem conteúdo, CRM, Klaviyo, calendário editorial, performance, flows, aprovações e receipts.

Não deve parecer landing page, card grid genérico ou dashboard SaaS arredondado. Deve parecer uma mesa administrativa de maison: silenciosa, reta, editorial, densa, clara e confiável.

## 2. Primary User Action

Ao abrir a home, Lucas precisa entender em poucos segundos:

- o que exige decisão agora;
- o que está rodando;
- o que está bloqueado;
- qual campanha precisa leitura;
- qual próxima ação segura;
- quais gates impedem write externo.

## 3. Design Direction

Direção escolhida por Lucas:

**Dior/Maison administrativa: editorial, reta, off-white, serif discreta, luxo silencioso.**

Cena: Lucas abre o dashboard durante rotina operacional da LK, em desktop, para decidir próximos movimentos de conteúdo/CRM sem ruído técnico. O ambiente pede clareza, confiança e estética premium, não espetáculo visual.

Color strategy: **Restrained**

- Canvas off-white/porcelain.
- Sidebar graphite/taupe ou taupe profundo, sem preto puro.
- Texto graphite.
- Linhas finas taupe.
- Caramel apenas para seleção, ação segura e ênfase funcional.
- Estados sem saturação excessiva.

Anti-direções:

- nada de rounded/candy;
- nada de card grid grande;
- nada de CSS “bonitinho”;
- nada de hero de landing;
- nada de dark command center genérico;
- nada de glassmorphism;
- nada de gradient text;
- nada de borda lateral colorida grossa.

## 4. Scope

Fidelity: production-ready.

Breadth: app surface completo, não uma tela só.

Interactivity: shipped-quality static/read-only MVP com navegação real entre rotas, estados e dados locais sanitizados. Writes externos continuam bloqueados.

Time intent: reconstruir do zero e depois iterar visualmente até ficar digno de uso.

## 5. Layout Strategy

Estrutura escolhida por Lucas:

**Sidebar expansível + rotas completas estilo app administrativo.**

Home escolhida:

**Operação completa primeiro: visão COO com tudo em ledger compacto.**

Topologia:

- App shell com sidebar expansível.
- Header utilitário discreto, não hero.
- Home como COO Ledger: uma matriz operacional compacta com decisões, campanhas, calendário, watchdog, Klaviyo, flows, learning e bloqueios.
- Rotas internas completas:
  1. Overview / COO Ledger
  2. Lucas Queue / Aprovações
  3. Campanhas
  4. Calendário Editorial
  5. Klaviyo Monitor
  6. Flows & Segments
  7. Pós-mortems / Learnings
  8. Brand Guide
  9. Receipts / Audit Trail
  10. Guardrails / Settings

Componentes visuais:

- Ledgers/tabelas compactas em vez de cards arredondados.
- Painéis retos, raio mínimo ou zero.
- Divisórias finas, ritmo editorial.
- Tipografia de títulos com serif discreta, UI/data com sans premium e legível.
- Sidebar com agrupamentos e status discretos.

## 6. Key States

Obrigatórios no rebuild:

- Default operacional com dados atuais.
- Empty state para rotas sem dados.
- Loading/skeleton discreto.
- Error state sem drama visual.
- Blocked state para Advanced KDP, Renan, estoque/pronta entrega etc.
- Read-only/write-gated state para Klaviyo/Calendar/externos.
- Mobile/tablet com sidebar colapsável.
- Long text em receipts sem quebrar layout.
- Dados stale com timestamp claro.

## 7. Interaction Model

- Sidebar expansível/colapsável.
- Rotas reais no Next App Router.
- Navegação por domínio operacional.
- Filtros/tabs discretos por status: decision, blocked, monitoring, done.
- Ações seguras como “preparar pacote”, “abrir receipt”, “ver evidência”, “copiar briefing”.
- Botões que poderiam gerar write externo devem ser desabilitados/rotulados como approval required.

## 8. Content Requirements

Dados iniciais sanitizados:

- Campanha Gifts Dia dos Namorados.
- Métricas 2h conhecidas.
- Watchdog Klaviyo status.
- Webhook Advanced KDP bloqueado.
- Calendar mirror status.
- Flow audit read-only.
- Pendência Renan.
- Próximos checkpoints 24h/72h.
- Receipts principais.
- Guardrails de writes externos.

Sem secrets, sem tokens, sem endpoints internos sensíveis no frontend.

## 9. Recommended Impeccable References During Implementation

- product.md
- craft.md
- spatial-design.md
- typography.md
- color-and-contrast.md
- responsive-design.md
- interaction-design.md
- ux-writing.md
- harden.md
- polish.md
- mission-control references relevant to COO Desk / Decision Inbox / Maison Ledger

## 10. Definition of Done

Antes de dizer “pronto”:

- Projeto reconstruído do zero ou estrutura antiga substituída claramente.
- PRODUCT.md e DESIGN.md presentes no projeto.
- Build passa.
- Secret scan passa.
- `npx impeccable detect --fast --json` nos paths frontend retorna limpo ou findings corrigidos.
- Screenshot/visual review mostra topologia diferente do MVP antigo.
- Sidebar expansível funcionando.
- Rotas principais funcionando.
- Production deploy/readback, se Lucas autorizar deploy.

## Open Questions

Nenhuma pergunta bloqueante depois das respostas de Lucas. Próximo passo é confirmação deste brief.
