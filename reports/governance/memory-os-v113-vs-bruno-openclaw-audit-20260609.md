# Memory OS v1.13 vs Bruno/OpenClaw — validação executiva

Gerado: 2026-06-09T19:36:44.797722+00:00
Escopo: comparar o Memory OS local atual contra o modelo Bruno/OpenClaw de agentes operacionais.

## Veredito

**Estamos bem: 8,6/10.**

A arquitetura agora está alinhada com Bruno/OpenClaw e a execução saiu do papel: há rotina real a cada 30min, watchdog, scorecard, receipts, worker contract, auto-heal e alerta acionável. O sistema não está “mal”.

Ainda não é 10/10 porque há pontos de maturação/observabilidade: precisa acumular 21 ciclos reais verdes, melhorar prova direta de recuperação de contexto em latest persistido, reduzir dependência de disciplina/documentação em workers legados, e criar um score Bruno-grade explícito recorrente.

## Comparação com os 7 blocos Bruno/OpenClaw

1. **Caso real de negócio** — **verde**
   - Memory OS resolve problema real: perda/fragmentação de memória, daily/hot stale, receipts fora do writer e contexto quebrado após compactação.

2. **Segundo cérebro antes da autonomia** — **verde**
   - Brain continua fonte rica/canônica; boot memory é índice mínimo; provider externo/Mem0 permanece off.

3. **Separar contexto, skills e rotina** — **verde**
   - Contexto: hot/daily/política/reports.
   - Skills: `hermes-brain-governance` e referência Memory OS.
   - Rotinas: checker, weekly observability, worker contract, receipts/handoffs.

4. **Memória como continuidade, não depósito infinito** — **verde**
   - `reports/memory-hygiene/latest.json`: `status=ok`, over_limit=0, near_saturation=0, template_missing=0, external_provider_active=false.
   - `scorecard-latest.json`: `status=ok`, score=100.

5. **Repetição vira skill/template/rotina** — **quase verde**
   - Receipts viraram writer/guard; workers têm contrato; todos os 19 AGENTS.md foram atualizados.
   - Lacuna residual: ainda pode existir script legado/manual fora do padrão; checker corrige, mas prevenção total depende de adoção contínua.

6. **Identidade/contrato operacional dos agentes** — **verde**
   - 19/19 `AGENTS.md` incluem contrato Memory OS v1.13.
   - Contrato: receipts novos via writer, worker legado via guard/register-existing, OK silencioso, problema → auto-heal primeiro, Mission Control fora.

7. **Governança: permissões, cofre, crons, supervisão** — **verde com maturação**
   - Cron daytime: every 30m, no_agent, deliver=origin, alert-only wrapper.
   - Weekly: local/silent.
   - Secret scan focado: 0 findings.
   - Brain health/docs guard: fail=0.
   - Maturidade: `pilot_real_cycles`, score=100; falta chegar a 21 ciclos reais para “mature”.

## Evidência viva coletada

- `reports/memory-hygiene/latest.json`: status ok; alert_count=0; over_limit=0; near_saturation=0; template_coverage_missing=0; provider externo ativo=false.
- `daytime-latest.json`: status ok; routes=0; adoption gap_count=0.
- `scorecard-latest.json`: status ok; score=100.
- `adoption-latest.json`: status ok; drift_receipt_count=0.
- `weekly-observability-latest.json`: status ok; findings=0.
- `cycle-maturity-latest.json`: status ok; maturity=`pilot_real_cycles`; score=100.
- Alert wrapper smoke: rc=0 e bytes=0 quando saudável.
- Cron Memory OS daytime: `bc96bb03d2b0`, every 30m, deliver=origin, no_agent=true, script `hermes_memory_os_daytime_alerting_watchdog.py`.
- Cron weekly observability: `e4c6b7c9b6dc`, local/silent, no_agent=true.
- Memory hygiene watchdog noturno: `f9a1d43caf48`, local/silent, no_agent=true.
- `hot.md`: atual, contém v1.13.
- daily 2026-06-09: atual, contém v1.13; menção a skeleton é histórica, não estado atual.
- Todos os 19 `AGENTS.md`: contrato v1.13 presente.

## Lacunas/próximas melhorias

### P0 — nada crítico agora
Não há over-limit, drift, findings, routes nem segredo detectado.

### P1 — maturar de pilot para mature
- Esperar/monitorar até 21 ciclos reais verdes.
- Critério: daytime silent/recovered OK, weekly ok, scorecard 100, drift 0.

### P1 — score Bruno-grade recorrente
Criar um `bruno-grade-memory-os-audit.py` ou incorporar no weekly observability um score explícito 0–10 contra os 7 blocos Bruno/OpenClaw.

### P1 — prova persistida de context recovery
O probe direto retorna ok, mas o artifact `context-recovery-latest.json` não estava presente no snapshot inicial. Próximo ajuste: persistir latest JSON sempre que o probe roda, mantendo silent-OK.

### P2 — endurecer prevenção em scripts legados
Hoje o auto-heal corrige receipt manual local. Para chegar a 10/10, os principais scripts legados que escrevem receipt devem chamar writer/worker guard nativamente antes de depender do checker.

## Conclusão

**Não estamos mal. Estamos bons e operacionalmente acima do ponto em que estava antes.**

Comparado ao Bruno, a grande diferença que ainda falta é maturidade por tempo e score recorrente: o desenho já segue o método; agora precisa provar estabilidade por ciclos e transformar a validação Bruno-grade em rotina automática.

## Não-ações

- Não usei Mission Control.
- Não ativei provider externo/Mem0.
- Não toquei Docker/VPS/Traefik/gateway.
- Não fiz writes externos em Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco.
- Não imprimi secrets.
