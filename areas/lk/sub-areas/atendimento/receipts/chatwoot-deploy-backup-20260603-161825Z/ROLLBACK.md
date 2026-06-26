# Chatwoot rollback reference — 20260603-161825Z

Old containers will be kept as `.pre-20260603-161825Z` if swap proceeds.

Fast rollback:
```bash
docker stop chatwoot-rails-1 chatwoot-sidekiq-1 || true
docker rm chatwoot-rails-1 chatwoot-sidekiq-1 || true
docker rename chatwoot-rails-1.pre-20260603-161825Z chatwoot-rails-1 || true
docker rename chatwoot-sidekiq-1.pre-20260603-161825Z chatwoot-sidekiq-1 || true
docker start chatwoot-redis-1 chatwoot-postgres-1 chatwoot-sidekiq-1 chatwoot-rails-1
curl -fsS https://chat.lkskrs.online/api
```
