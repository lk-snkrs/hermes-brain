# Receipt — Elle sem reapresentação repetida

- Data/hora UTC: 2026-06-15T15:53Z
- Área: LK / Atendimento / Elle / Chatwoot
- Correção humana: Lucas reportou que a Elle se apresentou mais de uma vez na mesma conversa, repetindo variações como “Aqui é a Elle da LK” / “Sou uma IA...” depois de já ter se apresentado.

## Regra correta

- A Elle deve se apresentar apenas na primeira resposta pública útil da conversa.
- Depois que já houve uma mensagem com “Aqui é a Elle da LK” na conversa, respostas seguintes devem ir direto ao ponto.
- Não repetir “Aqui é a Elle da LK”, “Sou uma IA...” ou o disclaimer de aprendizado em turnos posteriores.

## Diagnóstico

- Já havia uma função para remover intro repetida quando havia apresentação anterior.
- A remoção dependia de prefixo quase exato (`elle_intro(name)` ou `elle_intro(None)`).
- Se o Gemini ou o nome do cliente gerasse pequena variação, a reapresentação podia escapar.

## Alteração

- Fortalecido `strip_repeated_intro()` com padrões robustos para remover variações de:
  - saudação + “Como vai? Aqui é a Elle da LK.”;
  - “Aqui é a Elle da LK.”;
  - “Sou a Elle / Sou Elle da LK.”;
  - disclaimer “Sou uma IA de atendimento...” quando já houve apresentação anterior.
- Mantida a apresentação na primeira resposta quando não há histórico anterior.

## Verificação

- `python3 -m py_compile app.py`: OK.
- Testes sintéticos locais:
  - variações com nome diferente e disclaimer foram removidas;
  - primeira resposta sem histórico manteve “Aqui é a Elle da LK”;
  - segunda resposta com histórico anterior removeu “Aqui é a Elle da LK” e “Sou uma IA de atendimento”.
- Rebuild/recreate do container `elle-chatwoot`: OK.
- Smoke no container novo:
  - `first_has_intro=true`;
  - `second_has_intro=false`;
  - `second_has_ia_disclaimer=false`;
  - segunda resposta começa com `Nosso atendimento...`.
- Health público:
  - `ok=true`;
  - `write_enabled=true`;
  - `kill_switch=false`;
  - `public_reply_enabled=true`;
  - `ai_enabled=true`;
  - `ai_model=google/gemini-2.5-flash`;
  - `ai_secret_present=true`;
  - `debounce_enabled=true`;
  - `debounce_seconds=15.0`.

## Rollback

- Backup salvo em `/opt/elle-chatwoot/backups/lucas-no-repeat-elle-intro-20260615T155114Z/app.py`.

## Segurança

- Sem teste em cliente real.
- Sem impressão de PII, tokens, secrets ou URLs sensíveis.
- Sem consulta/alteração de estoque, Shopify ou Tiny.
