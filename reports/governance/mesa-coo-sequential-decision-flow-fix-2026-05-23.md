# Mesa COO — fluxo sequencial de decisão — 2026-05-23

Status: aplicado.

## Correção de Lucas

Lucas apontou que a Mesa COO estava jogando muita informação junta. O formato preferido é uma sequência de decisões, não um bloco grande:

1. Separar até 5 decisões mais importantes.
2. Enviar uma decisão por vez (`1/5`, depois `2/5` etc.).
3. Cada decisão deve ter opções claras: **Fazer**, **Não fazer**, **Agendar para depois**.
4. Só avançar para a próxima decisão depois da resposta.
5. Depois das respostas, executar em ordem o que foi aprovado.

## Correções aplicadas

- Memória de preferência UX de Lucas atualizada.
- Skill `mesa` atualizada para substituir o formato de bloco por fluxo sequencial de decisão.
- Cron `749ee30b51eb` — `Mesa COO diária Telegram` — atualizado no prompt para enviar apenas `Decisão 1/N` e aguardar resposta, mantendo no máximo 5 decisões.

## Escopo não alterado

- Nenhum schedule foi alterado.
- Nenhum delivery foi alterado.
- Nenhum cron foi criado/removido/pausado.
- Nenhum gateway/Docker/VPS/Shopify/GMC/Tiny/WhatsApp/email foi tocado.

## Verificação esperada

Próxima Mesa COO deve aparecer como:

```md
## Mesa COO — YYYY-MM-DD

**Decisão 1/N:** <ação concreta>
- Por que importa: <1 frase>
- Se escolher **Fazer**: Hermes faz <escopo exato>
- Limite/risco: <1 frase>

Responda: **Fazer**, **Não fazer** ou **Agendar para depois**.
```
