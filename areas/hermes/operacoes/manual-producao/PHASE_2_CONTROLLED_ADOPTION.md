# Fase 2 — Adoção controlada de features Hermes

Aberta em: 2026-05-30T22:02:16+00:00  
Status: **aberta / execução local-documental autorizada**  
Escopo: transformar a matriz de capabilities em pilotos seguros. **Este documento não autoriza alteração de runtime, Docker, VPS, Traefik, secrets, webhooks, crons, API pública, dispatcher produtivo, MCP remoto com credenciais, plugins ativos em produção ou writes externos.**

## 1. Tese da fase

A Fase 2 existe para tirar o Hermes do modo “Telegram bot turbinado” e aproximá-lo de uma plataforma operacional completa, mas sem aumentar superfície de risco.

O objetivo não é ativar todas as features. O objetivo é provar, uma por vez, quais features realmente reduzem risco, aumentam auditabilidade ou criam capacidade operacional útil.

## 2. Frentes abertas

### Frente A — Kanban piloto controlado

Objetivo: desenhar e depois testar um board real para melhorias Hermes/LK que sobreviva restart e tenha trilha persistente.

Estado inicial autorizado:

- criar backlog local/documental;
- definir board `hermes-lk-improvements`;
- manter cards inicialmente **unassigned**;
- não acionar dispatcher produtivo;
- não atribuir a workers reais até termos lane/toolset/rollback claros.

Critério de avanço:

- pelo menos 3 cards bem definidos;
- cada card com owner lógico, risco, evidência exigida, saída esperada e bloqueios;
- se houver execução real, primeiro worker deve ser local/read-only.

### Frente B — MCP piloto controlado

Objetivo: validar MCP como capacidade útil, começando por servidores já presentes ou read-only.

Estado inicial autorizado:

- inventariar configs MCP existentes sem imprimir secrets;
- validar se DataForSEO aparece nos perfis onde já foi configurado;
- documentar tools disponíveis, riscos e whitelist desejada;
- manter sampling desligado para servidores não confiáveis.

Bloqueado sem aprovação explícita:

- adicionar token novo;
- conectar MCP remoto com credenciais de produção;
- expor MCP tools em Telegram sem whitelist;
- ativar sampling em servidor não confiável.

### Frente C — Plugin local/read-only

Objetivo: especificar o primeiro plugin Hermes próprio de baixo risco.

Plugin candidato: **Hermes/LK Capability Status**.

Deve mostrar capability cards locais/read-only:

- profiles e estado esperado;
- API/webhook por profile;
- crons relevantes e delivery;
- MCPs configurados;
- plugins ativos;
- últimos receipts locais;
- riscos e próxima ação segura.

Bloqueado sem aprovação explícita:

- adicionar tool com write externo;
- acessar Shopify/Tiny/Crisp/GMC/ads/finance com escrita;
- publicar dashboard/plugin em superfície pública.

### Frente D — Dashboard/API como cockpit seguro

Objetivo: separar observabilidade runtime de decisão executiva.

Regra:

- Dashboard/API = runtime observability;
- Mission Control/Telegram = decisão, aprovação e receipts executivos.

Estado inicial autorizado:

- classificar exposição atual por evidência local/read-only;
- documentar plano loopback/Tailscale/auth;
- não abrir porta pública nem alterar Traefik/Docker.

### Frente E — Deliverable mode padronizado

Objetivo: definir quando entregar arquivo/media ao Lucas versus apenas salvar caminho local.

Regra inicial:

- relatório executivo curto no Telegram;
- artefato relevante anexado com `MEDIA:/absolute/path` quando o arquivo é o produto principal;
- receipts técnicos ficam locais, salvo falha/decisão.

## 3. Ordem de execução recomendada

1. Criar backlog Fase 2 e registrar cards documentais.
2. Fazer inventário read-only de MCP/DataForSEO e plugin surfaces.
3. Especificar plugin local/read-only.
4. Preparar approval packet separado para qualquer ativação real de Kanban/MCP/plugin/dashboard.
5. Só então executar um piloto real pequeno.

## 4. Critérios de sucesso

A Fase 2 só pode ser chamada de bem-sucedida quando houver:

- backlog canônico claro;
- pelo menos um piloto read-only/local validado;
- nenhum segredo exposto;
- nenhuma mudança runtime não aprovada;
- rollback documentado para qualquer mudança ativada;
- evidência de que a feature reduziu fricção real, não apenas “foi ligada”.

## 5. Approval packets exigidos

Criar approval packet separado antes de qualquer uma destas ações:

- criar/atribuir cards a workers com dispatcher ativo;
- iniciar/reiniciar gateway/profile;
- alterar config de API/webhook/dashboard;
- instalar/ativar plugin;
- adicionar/alterar MCP server em profile vivo;
- passar token/credencial para MCP/plugin;
- criar cron/hook/goal/batch operacional;
- qualquer write externo.

Cada approval packet deve conter:

- escopo exato;
- arquivos/configs a tocar;
- comandos previstos;
- risco/blast radius;
- rollback;
- verificação pós-ação;
- o que explicitamente **não** será feito.

## 6. Estado atual

Fase 2 aberta com autorização apenas para documentação, inventário read-only e preparação de backlog/packets.

Próximo arquivo canônico: `HERMES_FEATURE_BACKLOG.md`.
