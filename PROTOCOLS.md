# Lei COO #7 — Sempre Corrigir Eternamente

> Cada bug encontrado uma vez é bug encontrado para sempre.  
> O sistema deve se auto-proteger contra erros conhecidos.

## Regra de Ouro

**Bug encontrado → 3 ações no mesmo momento:**
1. **Corrigir** — fazer funcionar agora
2. **Prevenir** — criar mecanismo que impede o bug de se repetir
3. **Documentar** — salvar como lesson se for insight não-óbvio

## Padrão de Auto-Correção

### Nível 1: Erro Conhecido (determinístico)
Exemplo: token revoked, VPS refused, rate limit
→ `hermes_remediate.sh <categoria>` resolve automaticamente

### Nível 2: Bug Novo (descoperto em produção)
Exemplo: timezone bug, schema mismatch, pagination break
→ 1. Corrigir o script
→ 2. Adicionar test no `hermes_health_check.py`
→ 3. Se涉及的 padrão → adicionar ao `hermes_remediate.sh`
→ 4. Documentar em `lessons.md`

### Nível 3: Erro Estrutural (arquitetura)
Exemplo: 3 sources de brain, crons duplicados, scripts em /tmp desatualizados
→ 1. Corrigir arquitetura
→ 2. Criar script de validação
→ 3. Atualizar skill relevante

## Como Isso Se Aplica Na Prática

| Situação | Ação Automática |
|----------|----------------|
| Script quebrou → | Corrigir + health_check detecta antes da próxima execução |
| Bug de lógica → | Corrigir + salvar como lesson |
| Schema mudou → | health_check valida schema antes de scripts correrem |
| Token expirou → | remediate.sh renova + alerta |
| Decisão tomada → | decisions.md atualizado + push para VPS |

## Checklist ao Fechar Cada Sessão

1. ✅ Fix aplicado hoje → prevention criada?
2. ✅ Lições → lessons.md atualizado + brain sync
3. ✅ Pendências → pending.md atualizado
4. ✅ Git push → hermes-brain comitado

## Histórico de Auto-Correções

| Data | Bug | Prevenção Criada |
|------|-----|------------------|
| 19/04 | PAT revocada (23 scripts) | `hermes_health_check.py` — escaneia tokens em todo /tmp e /root |
| 19/04 | Timezone UTC vs BRT | Pattern no lessons.md + health check de datas |
| 19/04 | Pagination Shopify page_info | Fix no script + fallback implementado |
| 19/04 | transactions_full sync missing | Script recriado + adicionado ao full_sync |
| 19/04 | Brain 3 fontes divergindo | `brain_sync.sh` bidirecional |
| 19/04 | Consolidation 3 crons same time | Pausados 2, остался only 1 |
| 19/04 | hermes_learning_loop.py broken | Script reescrito com state.db correto |
