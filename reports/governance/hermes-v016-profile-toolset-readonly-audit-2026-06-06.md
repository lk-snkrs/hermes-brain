# Read-only profile/toolset audit — Hermes v0.16 Adoption OS

Run dir: `/opt/data/hermes_v016_adoption_os_20260606_160015`

Scope: read-only config inspection only; no runtime/gateway/Docker/Traefik/credential/webhook/MCP/production mutation.

## Findings

### default
- Config: `/opt/data/config.yaml`
- Telegram toolsets: `['browser', 'clarify', 'code_execution', 'cronjob', 'delegation', 'file', 'image_gen', 'memory', 'messaging', 'session_search', 'skills', 'terminal', 'todo', 'tts', 'vision', 'web', 'mcp-time', 'mcp-fetch', 'mcp-sequential_thinking', 'mcp-metricool_readonly', 'mcp-dataforseo']`
- Agent max turns/iterations: `90`
- Model provider present: `openai-codex`; model default configured: `True`
- Delegation provider: `openai-codex`; delegation model configured: `True`
- Note: telegram includes high-power/heavy toolsets: browser, code_execution, cronjob, file, terminal

### lk-shopify
- Config: `/opt/data/profiles/lk-shopify/config.yaml`
- Telegram toolsets: `['clarify', 'file', 'memory', 'session_search', 'skills', 'todo', 'web', 'terminal', 'code_execution', 'mcp-dataforseo', 'mcp-time', 'mcp-fetch', 'mcp-sequential_thinking']`
- Agent max turns/iterations: `50`
- Model provider present: `openai-codex`; model default configured: `True`
- Delegation provider: `openai-codex`; delegation model configured: `True`
- Note: telegram includes high-power/heavy toolsets: code_execution, file, terminal

### lk-trends
- Config: `/opt/data/profiles/lk-trends/config.yaml`
- Telegram toolsets: `['browser', 'clarify', 'file', 'memory', 'session_search', 'skills', 'terminal', 'todo', 'web', 'mcp-dataforseo', 'mcp-time', 'mcp-fetch', 'mcp-sequential_thinking']`
- Agent max turns/iterations: `45`
- Model provider present: `openai-codex`; model default configured: `True`
- Delegation provider: `openai-codex`; delegation model configured: `True`
- Note: telegram includes high-power/heavy toolsets: browser, file, terminal

### spiti
- Config: `/opt/data/profiles/spiti/config.yaml`
- Telegram toolsets: `['browser', 'clarify', 'file', 'memory', 'session_search', 'skills', 'terminal', 'todo', 'vision', 'web', 'mcp-time', 'mcp-fetch', 'mcp-sequential_thinking', 'mcp-dataforseo']`
- Agent max turns/iterations: `55`
- Model provider present: `openai-codex`; model default configured: `True`
- Delegation provider: `openai-codex`; delegation model configured: `True`
- Note: telegram includes high-power/heavy toolsets: browser, file, terminal

### mordomo
- Config: `/opt/data/profiles/mordomo/config.yaml`
- Telegram toolsets: `['browser', 'clarify', 'code_execution', 'file', 'memory', 'messaging', 'session_search', 'skills', 'terminal', 'todo', 'vision', 'web', 'mcp-time', 'mcp-fetch', 'mcp-sequential_thinking']`
- Agent max turns/iterations: `45`
- Model provider present: `openai-codex`; model default configured: `True`
- Delegation provider: `openai-codex`; delegation model configured: `True`
- Note: telegram includes high-power/heavy toolsets: browser, code_execution, file, terminal

### lc-claude-cli
- Config: `/opt/data/profiles/lc-claude-cli/config.yaml`
- Telegram toolsets: `['clarify', 'file', 'memory', 'session_search', 'skills', 'todo', 'web']`
- Agent max turns/iterations: `50`
- Model provider present: `lc-claude-cli-proxy`; model default configured: `True`
- Delegation provider: `lc-claude-cli-proxy`; delegation model configured: `True`
- Note: telegram includes high-power/heavy toolsets: file

### lk-ops
- Config: `/opt/data/profiles/lk-ops/config.yaml`
- Telegram toolsets: `['clarify', 'file', 'memory', 'session_search', 'skills', 'todo', 'terminal', 'code_execution', 'mcp-time', 'mcp-fetch', 'mcp-sequential_thinking']`
- Agent max turns/iterations: `40`
- Model provider present: `openai-codex`; model default configured: `True`
- Delegation provider: `openai-codex`; delegation model configured: `True`
- Note: telegram includes high-power/heavy toolsets: code_execution, file, terminal

### lk-collection-optimizer
- Config: `/opt/data/profiles/lk-collection-optimizer/config.yaml`
- Telegram toolsets: `['terminal', 'mcp-metricool_readonly', 'mcp-meta_ads_readonly', 'mcp-time', 'mcp-fetch', 'mcp-sequential_thinking', 'mcp-dataforseo']`
- Agent max turns/iterations: `60`
- Model provider present: `openai-codex`; model default configured: `True`
- Delegation provider: `openai-codex`; delegation model configured: `True`
- Note: telegram includes high-power/heavy toolsets: terminal

### brain-process
- Config: `/opt/data/profiles/brain-process/config.yaml`
- Telegram toolsets: `['skills']`
- Agent max turns/iterations: `90`
- Model provider present: `openai-codex`; model default configured: `True`
- Delegation provider: `openai-codex`; delegation model configured: `True`
- Note: telegram toolsets look relatively narrow

### lk-content-reviewer
- Config: `/opt/data/profiles/lk-content-reviewer/config.yaml`
- Telegram toolsets: `['skills']`
- Agent max turns/iterations: `90`
- Model provider present: `openai-codex`; model default configured: `True`
- Delegation provider: `openai-codex`; delegation model configured: `True`
- Note: telegram toolsets look relatively narrow

### lk-growth
- Config: `/opt/data/profiles/lk-growth/config.yaml`
- Telegram toolsets: `['terminal', 'mcp-metricool_readonly', 'mcp-meta_ads_readonly', 'mcp-time', 'mcp-fetch', 'mcp-sequential_thinking', 'mcp-dataforseo']`
- Agent max turns/iterations: `60`
- Model provider present: `openai-codex`; model default configured: `True`
- Delegation provider: `openai-codex`; delegation model configured: `True`
- Note: telegram includes high-power/heavy toolsets: terminal

### lk-analyst-readonly
- Config: `/opt/data/profiles/lk-analyst-readonly/config.yaml`
- Telegram toolsets: `['skills']`
- Agent max turns/iterations: `90`
- Model provider present: `openai-codex`; model default configured: `True`
- Delegation provider: `openai-codex`; delegation model configured: `True`
- Note: telegram toolsets look relatively narrow

### hermes-ops-readonly
- Config: `/opt/data/profiles/hermes-ops-readonly/config.yaml`
- Telegram toolsets: `['skills']`
- Agent max turns/iterations: `90`
- Model provider present: `openai-codex`; model default configured: `True`
- Delegation provider: `openai-codex`; delegation model configured: `True`
- Note: telegram toolsets look relatively narrow

## Recommendations

- Do not change any profile toolsets automatically from this audit.
- For chat-heavy Telegram specialists, prefer explicit minimal Telegram toolsets and keep broad CLI/maintenance capability separate.
- Preserve exceptions where Lucas expects CLI/terminal operation from Telegram, such as Mordomo/WACLI, but document that as intentional.
- Before changing a specialist profile, prepare a scoped packet: target profile, old/new toolsets, reason, rollback, and post-restart verification.