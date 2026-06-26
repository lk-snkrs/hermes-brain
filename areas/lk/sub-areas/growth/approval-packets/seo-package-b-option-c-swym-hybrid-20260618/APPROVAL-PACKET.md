# Approval Packet — Pacote B3 / Opção C: SWYM híbrido sob demanda

Data: 2026-06-18

## Objetivo

Reduzir o custo de SWYM/Wishlist Plus no primeiro carregamento mobile sem abandonar SWYM como sistema real de wishlist.

Modelo proposto:

1. Wishlist local da LK continua instantânea no primeiro paint.
2. SWYM não carrega automaticamente em home/coleções.
3. Ao clicar no coração ou acessar a página de wishlist, carregamos SWYM sob demanda.
4. A ação local é enfileirada e sincronizada com SWYM quando `_swat` estiver disponível.

## Status atual

Somente protótipo local preparado. Nenhum upload para tema dev/production foi feito nesta etapa.

Arquivos locais preparados:

- `/opt/data/profiles/lk-shopify/runtime/lk-swym-hybrid-v1.js`
- `/opt/data/profiles/lk-shopify/runtime/layout-theme-with-swym-hybrid-prototype.liquid`
- `/opt/data/profiles/lk-shopify/runtime/lk-swym-hybrid-theme.diff`

Validação local:

- `node --check /opt/data/profiles/lk-shopify/runtime/lk-swym-hybrid-v1.js` passou.
- Segredos SWYM presentes no Doppler: `SWYM_PID`, `SWYM_API_KEY`, `SWYM_API_ENDPOINT`; valores não impressos.

## Evidência usada

Do Pacote B anterior:

- Production baseline mobile com SWYM: TBT ~12.950ms; SWYM verdadeiro ~38 requests / ~304.6KB.
- Preview dev sem SWYM app embed: SWYM requests 0; TBT ~5.710ms.
- Teste production por edição direta de `settings_data.json` não foi confiável; Shopify/app embed reconciliou/continuou carregando SWYM em parte dos testes.

## Design técnico do protótipo

### Asset novo

`lk-swym-hybrid-v1.js`

Responsabilidades:

- Escutar clique em `.pc__wishlist`, `.pdp-gallery__wishlist` e `[data-lk-wishlist]` em fase capture, antes do handler local parar propagação.
- Manter UX local imediata usando o código existente de localStorage.
- Criar fila de ações `add/remove`.
- Carregar SWYM SDK somente após intenção real do usuário.
- Quando `_swat` existir, executar `addToWishList` ou `removeFromWishList`.
- Em `/pages/my-wishlist`, carregar SWYM imediatamente porque a página é explicitamente de wishlist.

### Alteração proposta em `layout/theme.liquid`

Inserir após o script local `LK Wishlist — localStorage`:

```liquid
{%- comment -%} LK SWYM Hybrid Loader v1 — dev candidate, loads SWYM only after wishlist intent. {%- endcomment -%}
<script>
  window.LK_SWYM_CONFIG = window.LK_SWYM_CONFIG || {
    retailerId: '__SWYM_PUBLIC_PID_FROM_DOPPLER_OR_PUBLIC_APP_SNIPPET__'
  };
</script>
<script src="{{ 'lk-swym-hybrid-v1.js' | asset_url }}" defer></script>
```

Na execução real, o placeholder de `retailerId` será preenchido pelo PID público SWYM recuperado via Doppler ou pelo snippet público já renderizado pelo app. O valor não será impresso em logs/receipts.

## Limite importante

Para o híbrido funcionar, o tema de teste deve estar sem app embed SWYM automático — como o `lk-new-theme/dev` no preview anterior — ou o embed oficial deve ser desligado pelo Theme Editor/App Embed. Caso contrário, o SWYM continuará carregando no primeiro paint e o híbrido não reduz o custo.

## QA necessário no tema dev

Páginas:

- Home
- Coleção `adidas-samba`
- PDP de produto piloto
- `/pages/my-wishlist`

Checks:

- Primeiro carregamento home/coleção sem requests `swym-relay`, `swym-ext-shopify` ou `wishlist-plus`.
- Coração visual aparece e alterna estado imediatamente.
- Após clique no coração, SWYM SDK carrega sob demanda.
- `_swat` aparece e fila sincroniza sem erro console crítico.
- Add-to-cart e cart drawer não são afetados.
- Lighthouse mobile compara antes/depois.

## Riscos

- Médio: SWYM pode exigir inicialização oficial completa para algumas funções avançadas.
- Médio: sincronização cross-device só acontece depois do primeiro clique/load sob demanda.
- Baixo visual inicial: fallback local já existe e foi testado no preview dev.
- Médio técnico: o SDK pode carregar, mas algum método `_swat` pode depender de globais adicionais do snippet oficial; por isso o teste precisa ser em dev antes de produção.

## Rollback

Se aprovado upload no tema dev:

1. Snapshot de `layout/theme.liquid` e eventual asset novo antes da alteração.
2. Upload de `assets/lk-swym-hybrid-v1.js` no tema dev.
3. Patch de `layout/theme.liquid` no tema dev.
4. QA.
5. Rollback dev: remover chamada do script e remover/restaurar asset.

Nenhuma mudança em production sem novo approval packet e aprovação explícita.

## Próxima decisão necessária

Para avançar além do protótipo local, é preciso aprovação explícita para upload em tema dev/unpublished:

**“Aprovo upload da Opção C no tema dev 155065450718 para QA, sem produção.”**
