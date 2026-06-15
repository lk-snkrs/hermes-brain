# PRD — Hermes Systemwide Auto-Remediation Contract v1

Data: 2026-06-14  
Owner: Hermes Geral / Operações Hermes  
Status: aprovado para implantação local/documental e governança; runtime/prod/external writes seguem approval-gated.

## 1. Problema

Lucas identificou um padrão ruim: Hermes e agentes especialistas frequentemente diagnosticam uma falha, mas param no diagnóstico e esperam Lucas pedir “corrige isso?”. Isso transforma agentes operacionais em relatórios passivos. O comportamento esperado é: **erro identificado = correção iniciada**, salvo quando a correção exige aprovação sensível.

Exemplo motivador: um agente de atendimento/LK Ops tenta executar uma ação operacional, encontra problema e apenas reporta “deu problema”. O correto é reportar a falha, classificar o escopo e imediatamente iniciar o caminho de correção ou apresentar um approval packet específico quando a correção toca produção/externos/secrets.

## 2. Objetivo

Criar um contrato sistêmico para Hermes, agentes especialistas, scripts e crons:

> Todo agente/processo que detecta uma falha deve classificá-la, corrigir automaticamente quando estiver dentro do escopo seguro, verificar, registrar aprendizado/receipt quando material e só pedir aprovação quando a próxima ação cruzar uma fronteira sensível.

## 3. Não objetivos

- Não autoriza writes externos, campanhas, WhatsApp/e-mail, Shopify/Tiny/Klaviyo/GMC/Meta/Supabase ou banco sem aprovação atual.
- Não autoriza Docker/VPS/Traefik/root/SSH/restart geral sem aprovação escopada.
- Não cria cron novo nem altera delivery/schedule de cron existente por si só.
- Não transforma alertas em Telegram de sucesso; silent-OK permanece obrigatório.

## 4. Princípios de produto

1. **Agente operacional, não chatbot:** diagnosticar é etapa intermediária, não entrega final.
2. **Auto-correção segura por padrão:** local/read-only/documental/diagnóstico/skill/rotina/script sem side effect externo deve avançar.
3. **Aprovação sensível uma vez:** se precisar aprovação, pedir o pacote exato; se aprovado, executar o escopo aprovado sem novo loop.
4. **Verificação antes de conclusão:** só dizer “corrigido” com evidência.
5. **Aprendizado vira sistema:** erro recorrente vira skill, rotina, teste, watchdog ou regra no Brain.
6. **Telegram só acionável:** falhas atuais, decisões ou exceções; OK final de cron/watchdog deve ser silencioso salvo quando Lucas pediu relatório.

## 5. Escopo de aplicação

### 5.1 Hermes Geral

- Ao detectar falha própria de resposta, roteamento, contexto, memória, doc, script ou rotina local: corrigir imediatamente.
- Se a correção depende de especialista, rotear com handoff e critério de verificação, não apenas apontar.
- Se depende de ação sensível, produzir approval packet com alvo, ação, risco, rollback e comando/procedimento exato pós-aprovação.

### 5.2 Agentes especialistas

- Cada especialista deve seguir o ciclo: `detectar → classificar → corrigir/approval → verificar → registrar`.
- Exemplo LK Ops/Atendimento: erro de carrinho/template/link/preview/local CLI deve abrir diagnóstico e correção; envio real, preço/disponibilidade/cliente/WhatsApp externo segue aprovação.
- Especialista não deve devolver problema para Lucas quando a próxima ação segura é evidente.

### 5.3 Scripts

- Scripts locais/watchdogs devem distinguir falha esperada e corrigível de falha real.
- Quando uma falha local conhecida for corrigível sem risco, script deve auto-healar ou chamar helper allowlisted e registrar saída sanitizada.
- Contrato de saída: `rc=0 + stdout vazio = OK silencioso`; `rc=0 + stdout = alerta acionável`; `rc!=0 = falha do watchdog/script`.

### 5.4 Crons

- Crons no_agent/watchdogs devem tentar correções locais allowlisted antes de alertar Lucas.
- Alertas devem conter: o que mudou, impacto, evidência, ação automática tomada e ação de Lucas se necessária.
- Cron não deve enviar “consegui corrigir” no Telegram se o estado final é OK e Lucas não pediu relatório; deve registrar em receipt/log local.

## 6. Matriz de decisão

| Classe | Exemplos | Ação padrão | Telegram | Aprovação |
|---|---|---|---|---|
| A0 local/read-only | ler arquivos, auditar, comparar estado, gerar PRD/relatório | executar | só se pedido | não |
| A1 local/documental | corrigir Brain, skill, rotina, índice, receipt, teste local | executar e verificar | resumo se Lucas pediu | não |
| A2 local runtime/profile já aprovado | restart/launcher/env do perfil nomeado dentro de escopo aprovado | executar escopo e verificar | receipt curto | aprovação prévia específica |
| A3 externo/prod | Shopify/Tiny/Klaviyo/GMC/Meta/Supabase/write, WhatsApp/e-mail/campanha | approval packet | decisão acionável | sim |
| A4 infra/secrets | Docker/VPS/Traefik/root/SSH/secrets/ports | approval packet + rollback | decisão acionável | sim |

## 7. Contrato de resposta

Quando detectar falha:

```text
Identifiquei um problema: [falha].
Classificação: [A0/A1/A2/A3/A4].
Ação: [vou corrigir agora / preparei aprovação porque toca X].
Verificação esperada: [comando/readback/evidência].
```

Quando corrigir:

```text
Corrigido.
Evidência: [teste/check/readback].
Não mexi em: [produção/externos/secrets/runtime sensível].
Aprendizado registrado em: [skill/rotina/receipt], se material.
```

## 8. Critérios de aceite v1

- Política canônica de autonomia atualizada com auto-correção segura.
- Rotina operacional criada e indexada no Brain.
- Skills centrais de Hermes/runtime/Brain atualizadas.
- Script local de auditoria identifica scripts/crons com termos de diagnóstico/erro sem contrato de auto-remediação explícito para revisão futura.
- Gates locais passam: health check, docs guard, compile/audit script, execução do audit script.

## 9. Rollout

### Fase 1 — Local/documental agora

- Criar PRD, rotina e plano.
- Atualizar política de autonomia, MAPA e índice de rotinas.
- Atualizar skills centrais.
- Criar auditor local de contrato.

### Fase 2 — Scripts/crons por waves

- Rodar auditor em scripts/crons.
- Priorizar watchdogs/no_agent com histórico de “diagnostica mas não corrige”.
- Patchar scripts allowlisted para auto-heal local + silent-OK.
- Não mudar schedule/delivery sem aprovação.

### Fase 3 — Runtime enforcement opcional

- Só com aprovação: integrar regra a Task Router/gateway/dispatcher como observabilidade ou enforcement.
- Começar observe-only; depois fail-soft; só depois hard enforcement onde seguro.

## 10. Métricas

- Redução de mensagens “deu problema” sem próxima ação.
- Percentual de falhas locais auto-corrigidas antes de alerta.
- Número de approval packets específicos vs pedidos genéricos.
- Gates verdes após correções.
- Menos retrabalho verbal de Lucas dizendo “corrige isso”.

## 11. Riscos e mitigação

- **Auto-correção passar do limite:** mitigado por matriz A0-A4 e approval gates.
- **Telegram ficar mais barulhento:** silent-OK e stdout vazio em sucesso.
- **Scripts esconderem falhas reais:** auto-heal só para padrões conhecidos/allowlisted com logs/receipts locais.
- **Agentes confundirem diagnóstico com evidência:** verificação obrigatória antes de “corrigido”.

## 12. Estado desta implantação

Este PRD autoriza apenas Fase 1 local/documental e criação de auditor local. Qualquer Fase 2 que modifique crons vivos/schedules/delivery ou Fase 3 runtime enforcement exige aprovação escopada separada.
