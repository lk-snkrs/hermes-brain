# Rotina — SPITI Monitor Health

## Objetivo

Verificar, em modo read-only, se existe monitor operacional de lances SPITI ativo antes de confiar em alertas automáticos, webhooks ou dados derivados.

Esta rotina não corrige produção, não reinicia serviços, não altera Docker, não altera n8n e não envia mensagens. Qualquer correção exige aprovação explícita do Lucas com plano de rollback.

## Fontes esperadas

Memória histórica documenta:

- systemd esperado: `spiti-lances`;
- porta esperada: `19123`;
- workflow n8n histórico: `OHC9FfEsK0JRVMBK`;
- base SPITI/CRM Supabase: `rmdugdkantdydivgnimb`.

Regra crítica: histórico documentado não prova execução atual. Confirmar em fonte viva antes de afirmar que está ativo.

## Checklist read-only

1. Confirmar host/ambiente consultado.
2. Listar unidades systemd candidatas:
   - `spiti`, `lance`, `auction`, `leil`.
3. Listar processos candidatos sem imprimir secrets.
4. Verificar listener na porta `19123`.
5. Verificar containers Docker candidatos sem mexer neles.
6. Se n8n estiver envolvido, consultar workflows em modo read-only/API ou SQLite sem ler credenciais.
7. Registrar data, fonte e lacunas.

## Comando seguro de referência

Rodar apenas em ambiente autorizado, preferindo Doppler/SSH já configurado e sem imprimir secrets:

```bash
systemctl list-units --all --no-pager | grep -Ei 'spiti|lance|auction|leil' || true
systemctl list-unit-files --no-pager | grep -Ei 'spiti|lance|auction|leil' || true
ps auxww | grep -Ei 'spiti|lance|auction|leil|19123' | grep -v grep || true
(ss -ltnp 2>/dev/null || netstat -ltnp 2>/dev/null) | grep -E '19123|:19123' || true
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}' | grep -Ei 'spiti|lance|auction|leil' || true
```

Cuidado: `ps auxww` pode expor credenciais em argumentos de processo. Redigir qualquer `-c usuario:senha`, token, password, api key ou secret antes de salvar/mostrar evidência.

## Resultado read-only — `lc.vps` em 2026-05-05

Ambiente consultado: `lc.vps` (`72.60.150.124`), modo read-only.

Evidência:

- `systemctl list-units/list-unit-files` não encontrou unidades `spiti`, `lance`, `auction` ou `leil`.
- `ps auxww` não encontrou processos candidatos.
- porta `19123` sem listener encontrado.
- `docker ps` não encontrou container candidato SPITI/lances.
- arquivos históricos SPITI foram encontrados em `/root/cerebro-cimino/`, mas isso é acervo/documentação, não execução ativa.

Conclusão operacional:

> Em `lc.vps`, na coleta de 2026-05-05, não foi encontrado monitor `spiti-lances` ativo por systemd, processo, porta `19123` ou Docker. Tratar monitor de lances como não confirmado nesse host até nova validação.

## Estados possíveis

| Estado | Critério | Comunicação |
|---|---|---|
| Ativo confirmado | Serviço/processo/porta/workflow encontrado e saudável | “Monitor ativo confirmado em fonte viva X, horário Y.” |
| Não encontrado | Nenhuma evidência viva no host | “Monitor não encontrado neste host; não vou assumir alertas automáticos.” |
| Parcial | Serviço existe, mas porta/API/workflow falha | “Há indício parcial; precisa diagnóstico antes de confiar.” |
| Desconhecido | Sem acesso à fonte viva | “Não consegui confirmar; silêncio > dado errado.” |

## O que nunca fazer sem aprovação

- Reiniciar serviço, container, gateway ou n8n.
- Criar/alterar workflow n8n.
- Alterar `systemd`, cron, Docker, compose, firewall ou porta.
- Enviar alerta para grupo/cliente.
- Afirmar lance/status usando apenas site/meta tag.

## Saída padrão para Lucas

```text
SPITI monitor health: [ativo confirmado / não encontrado / parcial / desconhecido]
Fonte: [host/API/banco/log]
Horário da coleta: [UTC]
Risco: [baixo/médio/alto]
Próximo passo: [read-only / pedir aprovação / aguardar fonte correta]
```
