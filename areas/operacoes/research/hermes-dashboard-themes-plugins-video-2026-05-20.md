# Hermes Agent Web Dashboard Themes + Plugins — aula Onchain AI Garage

Fonte: https://youtu.be/kLDUh20-AJA
Título: Hermes Agent Web Dashboard Themes + Plugins: I Built My Own Plugin!
Canal: Onchain AI Garage
Data publicada no YouTube: 2026-04-28
Duração: 17:58
Status de transcrição: YouTube sem captions disponíveis para esta sessão; resumo baseado em metadados/descrição oficial e capítulos extraídos da página.

## Tese central

O Hermes Agent lançou um painel web local, baseado em navegador, personalizável, com temas e SDK de plugins. A aula mostra o painel de ponta a ponta, instala um plugin comunitário e cria um plugin próprio open source de carteira.

## Capítulos extraídos

- 0:00 — Introdução: apresentação do painel do Hermes.
- 1:47 — Tour pelo painel: sessões, análises, logs, habilidades, configuração.
- 6:13 — Temas e troca de idiomas.
- 7:00 — Instalação da central de comando Chronos Forge / Hermes Command Center do JoeyNYC.
- 9:16 — Criação de plugin próprio: especificação de plugin de carteira.
- 13:23 — Primeira execução com depuração Token-2022.
- 16:10 — Plugin de carteira funcionando e código aberto.
- 17:30 — Conclusão.

## Funcionalidades do dashboard destacadas

- Sessões.
- Analytics: queima de tokens, detalhamento por modelo, principais skills.
- Logs.
- Cron jobs.
- Skills.
- Toolsets/ferramentas.
- Configuração via UI, reduzindo necessidade de mexer manualmente em `config.yaml`.
- Gerenciamento de chaves.
- Documentação integrada.
- Temas: Hermes Teal, Midnight, Ember, Cyberpunk e Rosé.
- Alternância de idioma, incluindo chinês.
- SDK de plugins para extensão comunitária.

## Plugins citados

### Chronos Forge / Hermes Command Center

Plugin comunitário do JoeyNYC instalado a partir de repositório. A descrição cita uma nova visualização de sessões com:

- queima de tokens;
- missões recentes;
- plano de controle;
- queima de modelos;
- capacidades em uma visualização consolidada.

### Plugin de carteira Solana + EVM

Plugin criado pelo autor da aula:

- somente endereços públicos;
- sem seed phrase;
- sem conexão MCP;
- importação manual limpa;
- API Jupiter para metadados de tokens e preços em tempo real;
- suporte Solana + EVM;
- filtragem de dados não identificados;
- agregação de carteiras monitoradas;
- importação/exportação JSON;
- código aberto.

## Insight para Lucas / Hermes Brain / Mission Control

1. **Mission Control como camada operacional do dashboard**
   - O dashboard oficial resolve observabilidade/configuração do runtime.
   - O Mission Control deve ser a camada de decisão, filas, approvals, receipts, rollback e visão executiva multiempresa.
   - Evitar duplicar tudo do dashboard; integrar/espelhar apenas o que ajuda Lucas a decidir.

2. **Plugin marketplace mental**
   - Tratar cada vertical como um plugin/capability card: LK Growth, LK sourcing, Zipper CRM, SPITI obras, Mordomo, Brain learning loop.
   - Cada card deve declarar: fonte, permissões, modo atual, último run, risco, próximo safe action.

3. **Carteira/agente que gasta exige política rígida**
   - A aula antecipa agentes com carteiras e pagamentos X402 / gateways pagos / serviços on-chain.
   - Para o ambiente Lucas: qualquer agente com capacidade de gastar dinheiro deve ficar fora de execução automática até existir approval explícito, limite de gasto, payload, destinatário, recibo, rollback e auditoria.

4. **Padrão seguro para plugins sensíveis**
   - O plugin de carteira da aula é um bom exemplo: public-address only, sem seed, sem MCP, read-only.
   - Esse padrão deve guiar plugins de Shopify/GMC/Ads/financeiro: começar read-only, com dados sanitizados, sem writes externos.

5. **Temas e i18n importam para adoção**
   - O painel mostra que personalização visual e idioma não são supérfluos: melhoram adoção operacional.
   - Para o Mission Control, manter UI premium/minimal e labels executivos em português é estratégico.

6. **Observabilidade unificada reduz atrito**
   - A maior promessa do dashboard é parar de vasculhar arquivos e logs manualmente.
   - Para Lucas, o equivalente prático é a Health Center / cron registry / receipts / Waiting Lucas sempre atualizados no Mission Control e no Brain.

## Dicas práticas para aplicar aqui

- Próximo bloco seguro no Mission Control: criar uma área “Capabilities/Plugins” preview-only, listando capacidades ativas e bloqueadas por risco.
- Cada capability deveria mostrar:
  - `status`: read-only, preview-only, approval-required, active-restricted, disabled;
  - `externalWritesEnabled`: sempre explícito;
  - último receipt;
  - fonte de dados;
  - botão de preparar preview, não executar real;
  - rollback/evidência quando aplicável.
- Para LK/Shopify/GMC/Ads: começar como plugins read-only com snapshots e health, nunca como writes.
- Para wallet/on-chain: se algum dia entrar, manter somente leitura por endereço público; nunca armazenar seed/private key; nunca assinar transação.
- Para Hermes Brain: registrar aprendizados de plugins como skills/referências, não apenas em chat.

## Links citados na descrição oficial

- Newsletter Onchain AI Garage: https://www.onchainaigarage.com/
- X Tonbi: https://x.com/tonbistudio
- GitHub Tonbi: https://github.com/tonbistudio
- Portfólio: https://www.tonbistudio.com
- Plugin de carteira: indicado como repositório Tonbi/Hermes wallet plugin na descrição do YouTube.
- Chronos Forge / Hermes Command Center: indicado como repositório JoeyNYC/Hermes Chronos na descrição do YouTube.
- Docs Hermes dashboard: https://hermes-agent.nousresearch.com/

## Decisão operacional sugerida

A aula reforça que o caminho certo para o nosso Mission Control é **capability/plugin registry preview-first**, não execução automática. O próximo avanço seguro é mapear capacidades reais em cards com status, riscos, receipts e permissões explícitas, mantendo writes externos em zero até aprovação específica.
