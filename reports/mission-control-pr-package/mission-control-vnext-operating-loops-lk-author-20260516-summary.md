# Mission Control vNext Operating Loops — redeploy com autor LK

## Correção aplicada

Lucas apontou que deploys usando `hermes@lksneakers.com.br` podem ser bloqueados pela Vercel porque esse e-mail não é membro/autorizado no time. A correção foi usar autoria Git autorizada `lk@lksneakers.com.br` para o commit local que alimenta o deploy.

## Commit local

- Commit: `fabae1a3cf3727faa743ee7f6af2749435074467`
- Author: `LK Sneakers <lk@lksneakers.com.br>`
- Committer: `LK Sneakers <lk@lksneakers.com.br>`
- Mensagem: `feat: add Mission Control operating loops`

## Deploy

Workflow usado:

1. `vercel pull --yes --environment=production --scope lk-snkrs-projects`
2. `vercel build --prod --scope lk-snkrs-projects`
3. `vercel deploy --prebuilt --prod --yes --scope lk-snkrs-projects`

Resultado:

- Production URL temporária: `https://mission-control-v5-public-preview-57woooygl-lk-snkrs-projects.vercel.app`
- Alias produção: `https://mission.lucascimino.com`
- Status Vercel: Ready

## QA pós-deploy

- `npm run lint`: OK
- `npm run build`: OK
- `/api/mission/state`: 200, versão `mission-control-vnext-operating-loops-20260516`
- `/api/mission/execute`: 200
- POST `/api/mission/execute`: OK, redaction de segredo/email validada
- Browser produção: renderizou Mission Control vNext
- Browser console: 0 erros
- `.vercel/.env.production.local`: removido

## Observação de plano Vercel

Não é necessário pagar assento/Pro extra para `hermes@lksneakers.com.br` se os deploys forem feitos com autor/identidade autorizada `lk@lksneakers.com.br`. Se quisermos que `hermes@lksneakers.com.br` apareça como autor/deployer no Vercel, aí sim esse e-mail precisa ter acesso ao time/projeto, possivelmente consumindo seat conforme o plano.

## Rollback

- Promover deployment anterior no Vercel; ou
- Reverter commit `fabae1a3cf3727faa743ee7f6af2749435074467` e redeploy prebuilt; ou
- Remover/ocultar `/api/mission/execute` e seções vNext caso seja necessário voltar para Reliability Layer.
