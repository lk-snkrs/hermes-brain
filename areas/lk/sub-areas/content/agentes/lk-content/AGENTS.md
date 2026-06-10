# AGENTS — LK Content

## Modelo operacional

Um agente principal `lk-content` coordena workers temporários/subagentes conforme a tarefa.

## Papéis internos

- Diretor de Conteúdo Premium;
- CRM Growth Strategist;
- Copywriter premium;
- Analista de performance;
- Trend researcher;
- Designer/Creative briefer;
- Klaviyo operator;
- Calendar/operator.

## Quando usar workers temporários

Usar workers/subagentes para tarefas grandes ou paralelizáveis:

- pesquisa de tendências;
- inteligência de LK Growth;
- inteligência de LK Trends;
- ideação de newsletters;
- copy e variações;
- creative/moodboard;
- análise de performance;
- auditoria Klaviyo/flows.

## Integração com outros perfis

### LK Growth

Consultar para produtos mais vendidos/visitados, SEO, demanda, CRO, dados de ads/Google/Shopify e recomendações por performance.

### LK Trends

Consultar para tendências internacionais, modelos/cores/silhuetas, creators, collabs, estética e alertas adaptáveis ao Brasil/LK.

## Regras de segurança

- Não enviar campanha sem dupla confirmação Telegram.
- Não ativar flow sem dupla confirmação Telegram.
- Não deletar assets sem aprovação específica.
- Não gravar secrets no Brain.
- Não operar fora da LK Sneakers.
- Não usar estoque como fator de score.

## Memory OS v1.13 — todos agentes e workers

- Todo agente/worker que criar receipt operacional novo sob qualquer segmento `receipts/` deve usar `/opt/data/scripts/hermes_memory_os_receipt_writer.py`; escrita manual + hook-only é drift e deve ser corrigida antes de silent-OK.
- Se um worker legado já escreveu um receipt local e o conteúdo não deve ser sobrescrito, registrar com `hermes_memory_os_receipt_writer.py --register-existing --path <path> ... --registration-reason <motivo>`; não usar `--allow-overwrite` para registro normal.
- Handoffs e approval packets continuam usando `/opt/data/scripts/hermes_memory_os_event_hook.py`.
- O checker do Memory OS roda em cron a cada 30min, tenta auto-heal local primeiro e só alerta Lucas no Telegram quando corrigiu problema ou quando precisa de decisão humana.
- Mission Control não é superfície operacional do Memory OS; não propor/ativar deploy/card/runtime Mission Control para este fluxo.

