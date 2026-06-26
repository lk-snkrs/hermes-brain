# PRD — Hermes Brain Watchdog Auto-Heal para lacunas locais — 2026-05-21

## Problema

O watchdog `Hermes Brain Operating Layer structural watchdog` alertou Lucas no Telegram porque faltava `memories/daily/2026-05-21.md`.

A lacuna era real, mas de baixo risco e totalmente local/documental. O comportamento anterior exigia Lucas como roteador manual: ele precisava ver o erro, pedir correção e lembrar o Hermes de transformar o erro em melhoria sistêmica.

## Objetivo

Transformar alertas estruturais simples do Hermes Brain em um ciclo de autocorreção seguro:

1. detectar lacuna local/documental;
2. corrigir automaticamente quando o risco for A0/A1;
3. registrar evidência no Brain;
4. voltar ao contrato silent-OK;
5. escalar Lucas apenas quando houver risco, decisão, aprovação ou falha não autocorrigível.

## Escopo v1

Incluído:

- Daily note ausente em `memories/daily/YYYY-MM-DD.md`.
- Atualização documental local do Brain.
- Registro de PRD/receipts quando o erro revela melhoria de processo.
- Saída sanitizada e curta no Telegram somente quando houve autocorreção ou lacuna não resolvida.

Fora de escopo:

- Docker, VPS, gateway, Traefik, redes, containers, volumes ou root/SSH.
- Shopify, GMC, Crisp, n8n, Meta, Klaviyo, Supabase ou qualquer sistema externo.
- Secrets, tokens, credenciais ou payloads sensíveis.
- Criação indiscriminada de novos crons.

## Regras de autonomia

- **Autocorrigir sem perguntar:** arquivos locais de Brain, skeletons, índices, PRDs, receipts, relatórios e health artifacts, desde que não contenham secrets nem mudem runtime.
- **Alertar com decisão:** quando a correção depender de escolher prioridade, remover algo, alterar contrato de entrega, criar novo cron, mudar schema canônico ou tocar fonte de verdade externa.
- **Bloquear e pedir aprovação:** qualquer ação A3/A4: Docker/VPS/gateway/produção/sistemas externos/secret/destrutivo.

## Comportamento esperado do watchdog

### Healthy

- `rc=0`, stdout vazio.
- Nenhuma mensagem para Lucas.

### Lacuna autocorrigida

- `rc=0`, stdout curto com:
  - o que foi corrigido;
  - arquivo criado/alterado;
  - confirmação de que não tocou runtime/externos/secrets.

### Lacuna não autocorrigível

- `rc=1`, stdout curto com:
  - lacunas;
  - por que não pôde corrigir;
  - próxima ação segura.

## Critérios de aceite

- Criar daily note ausente automaticamente com conteúdo mínimo seguro.
- Reexecutar `brain_operating_layer_audit.py` e obter `rc=0` depois da correção.
- Não imprimir secrets.
- Não alterar Docker/VPS/gateway/sistemas externos.
- Preservar silent-OK quando tudo estiver saudável.
- Registrar esta melhoria como PRD no Brain.

## Métricas

- Redução de alertas manuais por lacuna documental simples.
- Tempo de recuperação: no mesmo run ou no próximo run do watchdog.
- Zero falso positivo de runtime/infra para lacuna documental.
- Zero exposição de secrets.

## Roadmap

### v1 — agora

- Criar daily note ausente.
- Patchar watchdog estrutural para auto-criar skeleton de daily note em falta.
- Verificar silent-OK.

### v2 — próximo ciclo seguro

- Adicionar receipt automático em `areas/operacoes/receipts/` quando houver autocorreção.
- Consolidar contagem de autocorreções no relatório 02h30.
- Criar classe comum de `BrainLocalAutoHeal` se mais watchdogs repetirem o padrão.

## Status

Status: v1 implementado localmente em 2026-05-21.  
Dono: Hermes Geral / Operações Hermes.  
Risco: baixo, local/documental.  
Rollback: restaurar versão anterior de `/opt/data/scripts/brain_operating_layer_audit.py` e remover skeleton daily note se criada por engano.
