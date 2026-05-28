# Receipt / approval packet — Correções produção coleção New Balance 204L

Data: 2026-05-27
Status: aprovado por Lucas no Telegram; execução externa pendente de ferramenta Shopify Admin no runtime atual
URL: https://lksneakers.com.br/collections/new-balance-204l

## Pedido aprovado

Lucas aprovou aplicar em produção as correções na página de coleção New Balance 204L:

1. Título/H1: `New Balance 204L` — aumentar fonte em 3pt.
2. Subtítulo/kicker: remover duplicação do nome da coleção.
   - De: `CURADORIA LK · NEW BALANCE 204L`
   - Para: `CURADORIA LK`
3. Paginação/grid: mudar de 24 para 20 produtos por página.

## Evidência pública antes da execução

Inspeção pública em `https://lksneakers.com.br/collections/new-balance-204l?hermes_qa=20260527`:

- H1 detectado: `New Balance 204L`
- Fonte H1 detectada via computed style: `48px`
- Kicker visível: `CURADORIA LK · NEW BALANCE 204L`
- Produtos renderizados na primeira página: 24
- Total da coleção visível: 32 itens

## Correção canônica para o template

- H1 deve ficar dominante e limpo.
- Se o H1 já contém o nome da coleção, o kicker não repete o nome.
- Coleções produto-first usam 20 produtos por página como padrão, salvo exceção aprovada.

## Escopo autorizado

Pode alterar apenas o necessário para esta coleção/padrão:

- collection template/section responsável pelo hero/kicker da coleção 204L;
- configuração de paginação para coleção produto-first/204L;
- CSS/setting do H1 para +3pt.

## Fora de escopo

Não autorizado neste approval:

- mudar preço, estoque, produto, imagens, ordem comercial, filtros, menus, campanhas, Klaviyo, Meta/Google Ads ou qualquer página fora do padrão 204L sem nova aprovação.

## Rollback

Antes de aplicar no Shopify production, salvar backup do asset/theme setting atual. Rollback é re-aplicar o asset/settings anteriores e verificar:

- H1 volta ao tamanho anterior;
- kicker volta ao texto anterior;
- paginação volta a 24.

## QA pós-write obrigatório

- Readback do asset/settings alterado.
- Abrir URL pública com cachebuster.
- Confirmar H1 `New Balance 204L` com fonte aproximadamente 3pt maior que o baseline atual.
- Confirmar kicker `CURADORIA LK` sem `NEW BALANCE 204L`.
- Confirmar primeira página com 20 produtos.
