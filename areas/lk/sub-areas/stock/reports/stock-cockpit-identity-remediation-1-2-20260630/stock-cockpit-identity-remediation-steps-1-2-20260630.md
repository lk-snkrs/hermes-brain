# Stock Cockpit identity remediation — passos 1 e 2 — 2026-06-30

- generated_at_utc: `2026-06-30T14:17:48.007179+00:00`
- values_printed: false
- writes_executed: 0

## 1) Shopify SKU duplicados — 18

| Bucket | Qtde |
|---|---:|
| `shopify_sku_duplicate_needs_variant_sku_normalization_preview` | 18 |

### Amostra/linhas
- `CV1659001` · Tênis Nike SB Dunk Low VX 1000 Camcorder Cinza · alvo size `35` · variantes com mesmo SKU: 35 (45341347021022), 36 (45341347053790), 37 (45341347119326)
- `CZ0790104` · Tênis Nike Air Jordan 1 Low OG UNC Azul · alvo size `34` · variantes com mesmo SKU: 34 (45346420621534), 35 (45346420654302), 36 (45346420687070), 37 (45346420719838), 42 (45346420752606), 43 (45346420785374)
- `PACEWAFFLE` · Camiseta Pace Waffle Knit Off White · alvo size `P/S` · variantes com mesmo SKU: P/S (46207668748510), M (46207668781278), GG/XL (46207668814046)
- `U9060BLK` · Tênis New Balance 9060 Black Castlerock Grey Preto · alvo size `34` · variantes com mesmo SKU: 34 (47095709270238), 35 (47095709303006), 37 (47095709368542), 38 (47095709401310), 39 (46181348737246)
- `Rep20` · Camiseta Represent Clo Revere Manor Stained Black Preto · alvo size `S/P` · variantes com mesmo SKU: S/P (47890042323166), M/M (47890042355934), L/G (47890042388702), XL/GG (47890042421470)
- `1183C102100` · Tênis Onitsuka Tiger Mexico 66 White Blue Branco · alvo size `42` · variantes com mesmo SKU: 42 (46199067214046), 43 (46199067246814)
- `DJ9955800` · Tênis Nike Dunk Low Patent Halloween Laranja · alvo size `36` · variantes com mesmo SKU: 36 (45389958316254), 37 (45389958349022), 38 (45389958381790)
- `MR530EMA` · Tênis New Balance 530 Silver White Branco · alvo size `34` · variantes com mesmo SKU: 34 (47119200682206), 40 (47119200747742)
- `Rep19` · Camiseta Represent Clo Revere Manor Aged White Branco · alvo size `S/P` · variantes com mesmo SKU: S/P (47890042454238), M/M (47890042487006), L/G (47890042519774), XL/GG (47890042552542)
- `GY0042` · Tênis Adidas Campus 00s Crystal White Branco · alvo size `34` · variantes com mesmo SKU: 34 (46146065694942), 36 (46146065727710)
- `1183C123.200` · Tênis Onitsuka Tiger Mexico 66 Sabot Birch Peacoat Bege · alvo size `34` · variantes com mesmo SKU: 34 (47634751750366), 35 (47634751783134), 36 (47634751815902), 37 (47634751848670), 38 (47634751881438), 39 (47634751914206), 40 (47634751946974), 41 (47634751979742), 42 (47634752012510), 43 (47634752045278)
- `Rep01` · Moletom Represent Clo Masking Tape Initial Cedar Marrom · alvo size `S/P` · variantes com mesmo SKU: S/P (47890163466462), M/M (47890163499230), L/G (47890163531998), XL/GG (47890163564766)
- `DV1308004` · Tênis Nike Air Jordan 1 Mid SE Space Jam Preto ou · alvo size `35.5` · variantes com mesmo SKU: 35.5 (45502629544158), 37.5 (45502632853726)
- `183A872` · Tênis Onitsuka Tiger Mexico 66 SD Kill Bill Amarelo · alvo size `40` · variantes com mesmo SKU: 40 (45968992993502), 41 (45968993911006), 42 (45968993943774)
- `FJ3453-200` · Tênis Air Jordan 1 Low SE "Legend Coffee" Marrom · alvo size `41` · variantes com mesmo SKU: 42 (47604797472990), 41 (47604798357726)
- `FQ0997-389` · Jersey Off White x Nike "Allover Print Kelly Green" Verde · alvo size `G` · variantes com mesmo SKU: G (44750744453342), XG (44750744486110), XXG (44750744518878)
- `U1906LNU` · Tênis New Balance 1906L Khaki Bege · alvo size `37.5` · variantes com mesmo SKU: 40.5 (47741944791262), 37.5 (48191119851742)
- `U9060GCB` · Tênis New Balance 9060 Moonbeam Vintage Rose Lime Colorido · alvo size `35` · variantes com mesmo SKU: 35 (44986163364062), 36 (45378461171934), 37 (44986163396830), 38 (44986163429598), 39 (44986163462366), 40 (44986163495134), 41 (44986163527902), 42 (44986163560670)

## 2) Missing116 — fila de triagem

| Bucket | Qtde |
|---|---:|
| `tiny_mapping_or_cadastro_required_no_size_match` | 7 |
| `tiny_ambiguous_mapping_required` | 91 |
| `blocked_by_shopify_duplicate_before_tiny_mapping` | 18 |

## Decisão operacional

- Nenhuma linha ficou `write_ready=true`.
- Próxima etapa é decisão humana/lk-stock/lk-shopify por linha; depois rerodar preflight e só então usar wrapper governado.
- Tiny/Shopify/Supabase writes continuam `0`.
