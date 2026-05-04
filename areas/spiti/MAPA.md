# SPITI Auction — Mapa

Fonte resumida atual: `memories/spiti.md`.

## Regra crítica

Email é fonte de verdade de lances. Site mostra destaques. Meta tag é preço base, não lance atual.

Silêncio é melhor que dado errado.

## Dados e ferramentas documentados

- Supabase/SPITI CRM: `rmdugdkantdydivgnimb`.
- Tabela principal: `spiti_lotes`.
- Monitor de lances: systemd `spiti-lances`, porta `19123`.
- n8n workflow documentado: `OHC9FfEsK0JRVMBK`.
- Painel: leiloesbr.com.br / leilão documentado em `memories/spiti.md`.


## Sistemas e projetos GitHub

- `contexto/spiti-hub-github.md` — inventário inicial do repo privado `spiti-auction/spiti-hub`, sistema operacional unificado da Spiti.

## Rotinas

- `rotinas/verificacao-lances.md` — checagem segura de lances/lotes.
- `rotinas/alerta-lances.md` — alertas e deduplicação.
- `rotinas/relatorio-leilao.md` — relatório interno, com fonte e ressalvas.

## Playbooks operacionais

- `rotinas/playbook-pregao-ao-vivo.md` — resposta segura durante pregão, com hierarquia de fontes.
- `rotinas/playbook-divergencia-lances.md` — investigação quando fontes de lance/lote divergem.

## Regras de comunicação

- Informar tipo de lance quando disponível: A = automático, O = normal.
- Não dizer “sem lance” sem fonte correta.
- Não usar dado não confirmado.
- Não enviar mensagem para grupo/cliente sem aprovação Lucas.
