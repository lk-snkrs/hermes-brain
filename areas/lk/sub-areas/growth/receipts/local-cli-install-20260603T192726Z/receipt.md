# LKGOC local CLI install receipt
timestamp_utc: 20260603T192726Z
user: root
home: /opt/data/profiles/lk-collection-optimizer/home
scope: Doppler CLI + Shopify CLI + local Playwright for LKGOC QA
## Pre-state
doppler: shopify: node: /usr/bin/node
npm: /usr/bin/npm
chromium: /usr/bin/chromium
npm_prefix: /usr/local
\n## Post-state
doppler_path: /usr/bin/doppler
v3.76.0
shopify_path: /usr/local/bin/shopify
file:///usr/local/lib/node_modules/@shopify/cli/bin/run.js:4
import {enableCompileCache} from 'node:module'
        ^^^^^^^^^^^^^^^^^^
SyntaxError: The requested module 'node:module' does not provide an export named 'enableCompileCache'
    at ModuleJob._instantiate (node:internal/modules/esm/module_job:175:21)
    at async ModuleJob.run (node:internal/modules/esm/module_job:258:5)
    at async ModuleLoader.import (node:internal/modules/esm/loader:540:24)
    at async asyncRunEntryPointWithESMLoader (node:internal/modules/run_main:117:5)

Node.js v20.19.2
file:///usr/local/lib/node_modules/@shopify/cli/bin/run.js:4
import {enableCompileCache} from 'node:module'
        ^^^^^^^^^^^^^^^^^^
SyntaxError: The requested module 'node:module' does not provide an export named 'enableCompileCache'
    at ModuleJob._instantiate (node:internal/modules/esm/module_job:175:21)
    at async ModuleJob.run (node:internal/modules/esm/module_job:258:5)
    at async ModuleLoader.import (node:internal/modules/esm/loader:540:24)
    at async asyncRunEntryPointWithESMLoader (node:internal/modules/run_main:117:5)

Node.js v20.19.2
node_path: /usr/bin/node
v20.19.2
npm_path: /usr/bin/npm
9.2.0
chromium_path: /usr/bin/chromium
Chromium 148.0.7778.215 built on Debian GNU/Linux 13 (trixie)
playwright_local_dir: /opt/data/profiles/lk-collection-optimizer/tools/lkgoc-qa
lkgoc-qa@1.0.0 /opt/data/profiles/lk-collection-optimizer/tools/lkgoc-qa
└── playwright@1.60.0

playwright_smoke: ok
