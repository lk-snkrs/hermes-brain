# Scorecard curto — Hermes vs Amora por agente

Data: 2026-05-27
Escopo: leitura local/read-only, sem tocar runtime.

## Leitura executiva

A estrutura Hermes está **bem feita** e já ficou mais próxima da maturidade da Amora em:

- contratos por especialista;
- separação entre dono lógico, runtime e cron;
- handoff/receipt;
- aprovação escopada sem perder autonomia.

O que ainda diferencia a Amora é menos “quantidade de agentes” e mais a disciplina ritual do ciclo: ação → registro → memória → reuse.

## Scorecard por agente

### Hermes Geral
- **Nota:** 8,5/10
- **Estado:** muito sólido como COO/orquestrador central.
- **Forças:** roteamento, governança, guardrails, Brain, separação por domínio.
- **Gap principal:** ainda carrega rotinas históricas em Main/Mordomo.

### LK Growth
- **Nota:** 8,5/10
- **Estado:** próximo do nível Amora em clareza operacional.
- **Forças:** contrato forte, autonomia clara, boa separação de leitura vs write.
- **Gap principal:** reduzir ruído operacional e manter o recorte Growth puro.

### LK Ops / Atendimento
- **Nota:** 8,0/10
- **Estado:** bem documentado e já com fronteira clara.
- **Forças:** fonte de verdade bem definida, bloqueios corretos, handoff bom.
- **Gap principal:** ainda existe herança histórica fora do lugar ideal.

### LK Shopify
- **Nota:** 8,0/10
- **Estado:** melhorou bastante e já tem contrato mais maduro.
- **Forças:** preview, receipt, rollback, fronteira com Ops/Growth/Tiny.
- **Gap principal:** manter uniformidade e evitar variação de pacote por caso.

### LK Trends
- **Nota:** 7,8/10
- **Estado:** bom como radar/sourcing intelligence.
- **Forças:** foco em sinais de mercado e pesquisa read-only.
- **Gap principal:** continuar evitando mistura com compra, Ops e Growth.

### Mordomo
- **Nota:** 7,5/10
- **Estado:** correto como intake pessoal e triagem.
- **Forças:** útil para agenda, follow-up e rascunhos internos.
- **Gap principal:** ainda hospeda rotinas históricas que pedem owner explícito.

### SPITI
- **Nota:** 7,8/10
- **Estado:** bom e seguro, com o padrão certo de silêncio > erro.
- **Forças:** fonte verificável, bloqueios claros, leitura read-only saudável.
- **Gap principal:** declarar melhor a política de crons/rituais locais.

### Zipper
- **Nota:** 7,0/10
- **Estado:** correto como documental/read-only por enquanto.
- **Forças:** evita bot/runtime por simetria.
- **Gap principal:** só promover runtime se houver gatilho objetivo de volume/risco/canal.

### LK CRM
- **Nota:** 7,6/10
- **Estado:** agora tem pacote documental suficiente para operar sem improviso.
- **Forças:** guardrails de contato externo e campanhas estão claros.
- **Gap principal:** consolidar playbooks e receipts recorrentes.

### LK E-commerce
- **Nota:** 7,2/10
- **Estado:** bom como camada de coordenação, não como executor primário.
- **Forças:** ajuda a separar jornada, problema e dono.
- **Gap principal:** precisa continuar só como ponte, sem invadir Shopify/Ops/Growth.

### LK Tráfego Pago
- **Nota:** 7,3/10
- **Estado:** documentado o bastante para análise segura.
- **Forças:** bom para hipóteses, leitura de campanha e handoff.
- **Gap principal:** manter disciplina de aprovação e reconciliação com operação real.

## O que já está no nível Amora-ish

- contratos mais explícitos;
- fronteiras mais limpas;
- autonomia preservada por design;
- handoff/receipt mais uniforme;
- risco reduzido de um agente virar “mente separada”.

## O que ainda falta para ficar mais próximo da Amora

- menos herança histórica no Main/Mordomo;
- mais uniformidade de handoff/receipt em toda a malha;
- mais clareza sobre quem é runtime ativo e quem é apenas documentação;
- mais disciplina de fechar o ciclo no Brain sem microgerenciar execução.

## Conclusão

**Hermes já está bem feito.**

A diferença para a Amora agora é mais de **ritual e uniformidade** do que de arquitetura.

E o ponto mais importante: **não reduzir autonomia dos especialistas** — a governança deve dar contexto, proteger fronteiras e registrar memória, não centralizar execução desnecessariamente.
