- Production: `main` -> New hotfixes
- Hotfix: `hotfix-<task_id>` -> `main`

- Release: `release-<year>-<month>-<day>-<seq_number>` -> Test -> `main`

- Waiting Release: `waiting` -> New release `release-<year>-<month>-<day>-<seq_number>`
- Development: `dev` -> New tasks

- Tasks: `task-<task_id>` -> Pull Request -> `dev` -> When setted as priority ->  Merged into `waiting`