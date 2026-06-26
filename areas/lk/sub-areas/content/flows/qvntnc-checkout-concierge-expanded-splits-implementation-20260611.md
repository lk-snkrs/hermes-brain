# QVNtnC Checkout Concierge — implementação com splits expandidos

Data: 2026-06-11
Solicitação: Lucas — “Seguir” após discussão de mais splits por modelos e aprendizado do flow Hash.

## Status de segurança

- Flow original live `QVNtnC` permanece intocado.
- Draft anterior `U5C43z` permanece intocado até decisão explícita de montagem/edição.
- Ativação/envio/migração: não realizados.
- Desconto/cupom: não criado.
- Estoque/disponibilidade/pronta entrega: não utilizados.

## Arquitetura mantida

O flow continua com 3 emails:

1. Email 1 universal — continuidade do checkout.
2. Email 2 branchado por modelo/família — editorial + produto + CTA cedo.
3. Email 3 comercial — 10% off / urgência temporal real.

Não reintroduzir quarto email.

## Controle de compra aprendido do Hash

Replicar antes de qualquer ativação:

- Trigger: Started Checkout / Abandoned Checkout equivalente.
- Flow/profile filter: `Placed Order since starting this flow = 0`.
- Interpretação: se a pessoa comprar depois de entrar, não recebe os próximos emails de abandono.
- Reentry Hash observada: 7 dias.
- Reentry recomendada para nova versão: decidir entre:
  - 7 dias: paridade com Hash e maior captura;
  - 14–30 dias: menos repetição/pressão.

## Topologia recomendada no Klaviyo UI

```text
Started Checkout
  → Delay 1h
  → Email 1 universal
  → Conditional Split: contém 9060?
      YES → Email 2 — NB 9060
      NO → Conditional Split: contém 530?
        YES → Email 2 — NB 530
        NO → Conditional Split: contém Mexico 66 Sabot?
          YES → Email 2 — Onitsuka Mexico 66 Sabot
          NO → Conditional Split: contém Mexico 66?
            YES → Email 2 — Onitsuka Mexico 66
            NO → Conditional Split: contém Vomero / Vomero Premium?
              YES → Email 2 — Nike Vomero
              NO → Conditional Split: contém Mind 001 / Mind 002?
                YES → Email 2 — Nike Mind
                NO → Conditional Split: contém Samba/Gazelle/Campus/Taekwondo/SL 72?
                  YES → Email 2 — Adidas low-profile/terrace
                  NO → Email 2 — fallback curadoria LK
  → Delay
  → Email 3 — 10% off / condição temporal real
```

## Branches v1

### 1. New Balance 9060

Tese: runner retro-futurista/chunky com presença editorial, bom para denim amplo, alfaiataria relaxada e activewear premium.

CTA primário: `Fechar carrinho`

### 2. New Balance 530

Tese: running heritage mais limpo, leve e fácil; funciona como sneaker de rotina com leitura fashion discreta.

CTA primário: `Fechar carrinho`

### 3. Onitsuka Tiger Mexico 66

Tese: low-profile clássico, silhueta fina, leitura vintage/sportstyle e fácil de usar com calça reta, alfaiataria casual, saia/vestido e denim.

CTA primário: `Concluir com o Mexico 66`

### 4. Onitsuka Tiger Mexico 66 Sabot

Tese: variação mule/sabot com styling mais fashion, boa para rotina, viagem e looks de transição; precisa de linguagem cuidadosa sem prometer disponibilidade.

CTA primário: `Fechar carrinho`

### 5. Nike Vomero / Vomero Premium

Tese: runner com conforto e volume premium; combina com uniformes urbanos, travel look e peças mais técnicas.

CTA primário: `Concluir seleção`

### 6. Nike Mind 001 / Mind 002

Tese: produto de design/novidade, com apelo de forma e repertório; abordagem deve explicar a silhueta sem hype exagerado.

CTA primário: `Fechar carrinho`

### 7. Adidas low-profile / terrace

Inclui, se fizer sentido no payload: Samba, Gazelle, Campus, Taekwondo, SL 72.

Tese: low-profile/terrace como escolha versátil, casual e mais limpa, com força em looks urbanos e styling minimalista.

CTA primário: `Concluir seleção`

### 8. Fallback curadoria LK

Para produtos sem família detectada.

Tese: curadoria/procedência/suporte humano, sem inventar atributos específicos do modelo.

CTA primário: `Retomar checkout`

## Ordem interna de cada Email 2

Obrigatório:

1. Hero do modelo/família.
2. Bloco do produto abandonado — imagem/nome/variante quando disponível.
3. CTA primário imediato.
4. Editorial/styling/repertório.
5. CTA secundário ou WhatsApp como suporte, não como ação principal.

## Gate técnico antes de montar filtros finais

Validar no evento de checkout qual campo contém os dados de produto/modelo:

- item name/title;
- variant title;
- SKU;
- vendor/brand;
- line_items;
- collections/tags, se sincronizados.

Não assumir campo final sem readback/test profile.

## Dependência de `lk-stock`

A ordem final dos branches deve ser validada por ranking 90 dias por família/modelo, retornado por `[LK] Estoque Loja Física` / `lk-stock`.

LK Content pode seguir com blueprint/copy, mas prioridade final por venda/modelo deve consumir o retorno do owner.
