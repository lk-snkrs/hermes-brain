# Mordomo WhatsApp — Autonomia Fase 2

Data: 2026-05-20
Status: aprovado por Lucas
Escopo: WhatsApp pessoal como interface global do Mordomo Hermes, com roteamento para pessoal, Zipper, SPITI, LK e Hermes/Infra.

## Decisão

Lucas aprovou ampliar a autonomia do Mordomo WhatsApp, não como permissão genérica para responder tudo, mas como avanço por classes estreitas, auditáveis e com guardrails fortes.

Princípio aprovado: aumentar liberdade por “ilhas de autonomia” bem definidas. O Mordomo deve pedir aprovação apenas quando há decisão humana real, risco comercial, nuance institucional, negociação, dinheiro, produção, fornecedor sensível, cliente sensível, infraestrutura ou dado não verificado.

## 12 melhorias aprovadas

### 1. Autonomy Registry por tipo de situação

Criar uma tabela viva para cada classe de caso:

- classe do caso;
- nível permitido: ler, registrar, criar evento, criar lembrete, criar draft, enviar automático, pedir decisão;
- templates permitidos;
- bloqueadores;
- última decisão/correção de Lucas;
- confiança atual;
- exemplos reais de acerto/erro.

### 2. Ampliar respostas automáticas A1 de secretaria pura

Permitir automação apenas em classes seguras, curtas e não comerciais.

Pode enviar automaticamente quando a conversa já estiver clara e não houver negociação:

- “recebi, obrigado”;
- “combinado, fico no aguardo”;
- “perfeito, obrigado pelo retorno”;
- “vou verificar e te retorno”, somente se uma pendência interna real for criada;
- confirmação simples de presença/horário;
- agradecimento por recusa cordial pós-PDF;
- acknowledgement de cliente analisando PDF/obra sem pedir preço, condição, reserva ou disponibilidade.

Nunca enviar automaticamente quando envolver:

- preço;
- Pix;
- condição de pagamento;
- desconto;
- disponibilidade;
- reserva;
- prazo comercial comprometedor;
- reclamação;
- fornecedor cobrando decisão;
- artista/colecionador com nuance institucional;
- negociação;
- qualquer dado não verificado.

### 3. Perfis por contato

Criar perfil operacional por contato relevante:

- pessoa/empresa/contexto;
- negócio associado;
- grau de proximidade com Lucas;
- tom observado;
- assuntos recorrentes;
- autonomia permitida;
- pendências abertas;
- exemplos de resposta de Lucas.

### 4. WhatsApp como caixa de decisão

Quando algo exigir Lucas, entregar um pacote de decisão, não um alerta genérico:

- contato;
- contexto;
- risco;
- recomendação;
- resposta sugerida;
- ação possível: enviar, editar, adiar, ignorar, criar tarefa, pedir mais contexto.

### 5. Silêncio inteligente

Separar eventos em:

- silencioso: registrei, arquivei, criei draft, atualizei fila;
- digest 17h: precisa de atenção, mas não urgente;
- interrupção imediata: risco de perder dinheiro, compromisso claro, cliente importante sem resposta, problema operacional, prazo curto.

### 6. Pendência com dono e próxima ação

Toda conversa relevante deve terminar em um estado:

- resolvida;
- esperando outra pessoa;
- esperando Lucas;
- esperando fornecedor/equipe;
- follow-up agendado;
- bloqueada por dado faltante;
- oportunidade comercial;
- compromisso de calendário;
- aprendizado/Brain.

### 7. Detecção automática de compromissos mais agressiva

Criar evento ou lembrete automaticamente quando houver data/hora/contexto suficiente:

- compromisso pessoal;
- reunião Zipper/SPITI/LK;
- retirada/entrega de obra;
- visita à galeria;
- ligação marcada;
- café/almoço;
- prazo combinado;
- promessa como “te mando até sexta”;
- passagem/local/horário combinados.

### 8. Zipper: separar lead comercial de relacionamento cultural

Classificar contatos Zipper por função:

- comprador/colecionador ativo;
- arquiteto/advisor;
- artista apresentando portfólio;
- curador/instituição;
- fornecedor/logística;
- cliente pós-PDF;
- cliente com objeção/preço;
- contato institucional sem urgência.

Cada classe tem autonomia diferente.

### 9. SPITI conservador, mas estruturado

Para SPITI, manter cautela externa, mas registrar sinais:

- interessados;
- potenciais consignantes/compradores;
- perguntas sobre lote/bid/pagamento;
- follow-up interno;
- resposta preparada para aprovação;
- separação entre curioso e lead real;
- nenhuma afirmação sem fonte verificada.

### 10. Aprender com respostas reais de Lucas

Comparar respostas manuais de Lucas com a classificação do Mordomo:

- teria respondido ou bloqueado?;
- tom estava certo?;
- Lucas foi mais curto/longo?;
- Lucas ignorou?;
- Lucas respondeu por áudio?;
- tom formal ou íntimo?;
- decisão vira regra por contato/classe.

### 11. Modo rascunho invisível

Para casos médios, criar draft/pendência sem interromper:

- draft local/Gmail;
- fila atualizada;
- aparecer apenas no digest;
- pronto para aprovação em lote.

### 12. Guardrail de não parecer robô

Mensagens automáticas devem ser:

- curtas;
- sem excesso de cordialidade;
- sem “com calma” ou “fez sentido”;
- sem explicar demais;
- sem tom genérico de atendimento;
- sem inventar contexto;
- ajustadas ao contato e empresa.

## Prioridade de implementação recomendada

1. Autonomy Registry.
2. Contact Profiles.
3. Decision Inbox 17h com pacotes de decisão.
4. Ampliação de classes A1 automáticas.
5. Aprendizado por resposta real de Lucas.
6. Expansão para SPITI e Zipper cultural/institucional com cautela.

## Implementação inicial executada

Arquivos operacionais criados/atualizados:

- `/opt/data/profiles/mordomo/config/mordomo_autonomy_registry.json`: registry de classes de autonomia aprovadas, com níveis permitidos, bloqueadores, templates, confiança e exemplos.
- `/opt/data/profiles/mordomo/state/mordomo_contact_profiles.json`: base inicial de perfis por contato, usando hash em vez de JID cru quando possível.
- `/opt/data/profiles/mordomo/scripts/mordomo_whatsapp_global_watch.py`: agora consulta o Autonomy Registry antes de qualquer auto-send de follow-up, grava `autonomy_class`, atualiza perfil de contato e registra a classe no audit log Strategy/Executor.
- `/opt/data/profiles/mordomo/scripts/mordomo_whatsapp_daily_digest.py`: Decision Inbox 17h passou a exibir classe de autonomia e bloqueadores, para diferenciar o que é seguro, o que é decisão humana e o que ficou bloqueado.

## Implementação incremental 2026-05-21

- `generic_secretary_ack` foi ligado ao Autonomy Registry, mas permanece bloqueado por padrão: só pode enviar se o perfil do contato permitir explicitamente essa classe.
- O watcher reconhece `simple_ack`, `received` e `waiting_other_person` como candidatos a `generic_secretary_ack`, porém bloqueia envio quando o perfil ainda não contém permissão.
- O script de callbacks do Telegram agora alimenta o learning loop dos Contact Profiles: `ignore`/`silence` bloqueiam a classe para o contato, `draft` registra preferência por preview sem inferir autorização de envio, e `remind9` registra preferência por pendência humana.
- O registry ganhou `implementation_status` para deixar claro o que está ativo e o que continua protegido.

## Guardrail soberano

Esta aprovação não autoriza envio genérico externo. Autoriza a construção e ativação de classes estreitas, seguras e auditáveis. Qualquer classe nova de envio automático deve ter template, bloqueadores, logs, exemplos e rollback/disable simples.
