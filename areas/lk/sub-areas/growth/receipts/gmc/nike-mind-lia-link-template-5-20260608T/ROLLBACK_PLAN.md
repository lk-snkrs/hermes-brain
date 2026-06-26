# Rollback plan — Nike Mind LIA link_template 5

Usar somente se os campos gerarem nova reprovação ou se o source owner pedir reversão.

1. Ler `merchantapi_before_products.json`.
2. Para cada offerId, usar o mesmo `dataSource` registrado no snapshot.
3. Aplicar Merchant API `accounts.productInputs.patch` com `updateMask=productAttributes.linkTemplate,productAttributes.mobileLinkTemplate,productAttributes.adsRedirect` e valores vazios/removidos conforme compatibilidade da API, ou reinserir o product input a partir do estado anterior sem esses campos.
4. Readback em Merchant API processed product.
5. Confirmar itemLevelIssues/destinationStatuses.

Observação: rollback não foi executado porque o readback final mostrou 5/5 aprovados em LOCAL_INVENTORY_ADS e FREE_LOCAL_LISTINGS.
