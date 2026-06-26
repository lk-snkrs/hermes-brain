# Learning Ledger — Bruno Hermes 7 passos

Data: 2026-06-04
Fonte: vídeo Bruno Okamoto — “7 essential steps to using Hermes and creating agents that work for you (complete guide)”
Transcript: obtido via TranscriptAPI com chave armazenada em Doppler (`lc-keys/prd`, secret `TRANSCRIPT_API_KEY`). Valor da chave não registrado.

## Aprendizado central

Hermes deve ser operado como infraestrutura de agentes, não como chatbot. Agentes precisam de função empresarial, contexto, Brain, skills, tools, rotinas, permissões e governança.

## Lições incorporadas

- Agente = funcionário operacional com missão, dono, fontes, tools, skills, rotinas, outputs e limites.
- Brain é a memória rica/canônica; memória curta injetada é boot mínimo.
- Crons são o heartbeat; devem ter dono, cadência, output, silent-OK, kill criteria e risco documentado.
- Repetição vira sistema: 1 vez executa, 2 vezes documenta/template, 3 vezes skill/rotina.
- Padrão Dexter adaptado: inbox → score/classificação → roteamento → skill → output/receipt → feedback → melhoria.
- Segredos ficam em Doppler/cofre; Brain/skills guardam nomes e uso seguro, nunca valores.
- Autonomia sem governança vira risco automatizado.

## Artefatos atualizados

- Skill `youtube-full`: adicionada convenção Doppler/helper TranscriptAPI.
- Skill `youtube-content`: fallback atualizado para TranscriptAPI antes de pedir transcript manual.
- Script `/opt/data/scripts/youtube_transcriptapi_fetch.py`: helper seguro para carregar chave do Doppler e buscar transcript.
- Brain `AGENTS.md`: modelo operacional de agente como funcionário, não chatbot.
- Skill `bruno-openclaw-hermes-brain-adaptation`: referência curada `references/bruno-hermes-7-steps-agent-operating-model-20260604.md`.

## Próxima curadoria recomendada

Em próxima janela de melhoria, revisar organograma/matriz de agentes para garantir que cada agente tenha: missão, dono, fonte de verdade, permissões, crons, skills, output, supervisor e critérios de escalonamento.
