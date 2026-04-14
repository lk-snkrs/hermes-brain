# Lições Aprendidas — Grupo Cimino

## 🔒 Estratégicas (Permanentes)

### Dados antes de afirmar
- Lucas afirma → verificar no banco. Nunca contradizer sem dados.
- Dizer "zerado" sem consultar Supabase = erro grave.
- **Regra:** dúvida → consulta. Sem consulta → sem resposta sobre dados.

### Credenciais
- NUNCA hardcodar credenciais. Usar `doppler secrets get NOME --plain`
- Fallback explícito: `os.getenv('A') or os.getenv('B')` — sem isso crashes são silenciosos
- `SUPABASE_CRM_SERVICE_KEY` não existe → usar `SUPABASE_ZIPPER_SERVICE_KEY`
- Shopify: `SHOPIFY_ACCESS_TOKEN` (não `SHOPIFY_API_TOKEN`)

### Webhook async é obrigatório
- Qualquer endpoint com processamento >2s deve responder 200/202 imediatamente
- n8n timeout ~10s. Playwright ~7s/lote → n8n abortava → 6 lances perdidos
- **Regra:** endpoint webhook → responde 2xx imediato → thread separada para trabalho

### Deduplicação
- Qualquer listener de webhook → dedup com TTL desde o início
- TTL atual SPITI: 24h, chave: `{lote_id}:{lance_atual}`

### Grupos WhatsApp
- Sessão de grupo não carrega decisions.md automaticamente
- Skills precisam de queries pré-embutidas

## 📊 LK Sneakers

### Cross-sell (5.7k pedidos analisados)
- Onitsuka Tiger = hub central (1.290 pedidos), 91.6% lealdade
- Jason Markk = upsell universal (funciona com qualquer tênis)
- NB 9060 → Onitsuka Tiger = fluxo mais forte (25 clientes)
- 378 clientes NB 9060 sem recompra = segmento prioritário Klaviyo

### Tickets março 2026
- Ticket médio: R$ 3.035 | 408 pedidos | R$ 1.238.292 total
- Referência real — não usar para projeções futuras sem ajuste sazonal

### Technical
- GraphQL metafieldsSet com JSON embutido → erro 500 → usar REST API
- Heredoc Python dentro de exec trava output → escrever arquivo .py
- Shopify REST API: 0.12s entre calls = seguro (não rate limit)
- Googlebot ignora crawl-delay em robots.txt
- GMC re-sincronização pode levar horas após correção

## 🎨 Zipper Galeria

### Dois bancos distintos — nunca confundir
- `vendas_tango` (banco `pcstqxpdzibheuopjkas`) → vendas reais de obras
- `spiti_lotes` (banco `rmdugdkantdydivgnimb`) → leilão SPITI

### Marzo 2026 excepcional
- R$ 679.000 em 8 vendas. Ticket médio altíssimo.
- Não usar como referência de mês normal para projeções

## 🏛️ SPITI

### Total de lances = fonte é o email
- Site mostra só 12 destaques. Fonte verdadeira = emails processados pelo n8n → Supabase
- NUNCA buscar total via scrape da home page

### Meta tag ≠ lance atual
- `product:price:amount` na meta tag = preço base, não lance atual

### Tipo de lance
- A = automático, O = normal — informar nas notificações

### Tom no grupo SPITI.M
- Leve e descontraído — mas não impulsivo
- Silêncio é melhor que dado errado

## 📱 Integrações

### Evolution API / WhatsApp
- Links no caption de imagem NÃO são clicáveis
- **Solução:** enviar URL como mensagem de texto separada após a mídia (1s delay)
- Sempre usar `limit: 20-30` max, nunca 100+ (timeout em 562 conversas)

### Processo após porta bloqueada
- Após deploy fix, confirmar PID/porta do processo que está respondendo

### Mensagens WhatsApp
- "Oi, Contato3!" + emojis = parecer amador
- Sempre extrair `primeiro_nome` do `push_name`
