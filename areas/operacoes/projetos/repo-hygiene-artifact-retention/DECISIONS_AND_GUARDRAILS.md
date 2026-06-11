# Decisions and Guardrails — Brain Repo Hygiene / Artifact Retention

## Decisões

- Onda 12 registra a necessidade de governança de retenção porque o repo contém muitos artefatos locais/untracked úteis, mas não todos devem virar Git automaticamente.

## Guardrails

- Não apagar, mover ou versionar artefatos em massa sem aprovação e backup.
- Untracked não significa lixo; pode ser evidência operacional ainda não curada.
- Git status grande deve ser tratado por allowlist escopada por onda.
- Não alterar .gitignore ou política de sync nesta onda.
