# Sherpa Tribe Internship Task

Django + DRF + Dockerized environment with Postgres, Redis.
Implements a minimal Task management API (Tasks / Comments / Tags) 
aligned with test requirements.


## Prerequisites
Docker (Desktop on macOS/Windows, Engine on Linux): 
https://docs.docker.com/get-docker/

Git: https://git-scm.com/downloads
No local Python needed – everything runs in Docker.


Any IDE (PyCharm, VS Code, etc.) can be used for development, 
but it’s not required to run the project.

## Clone

```commandline
git clone YOUR_REPO_URL.git
cd repo-folder
```

Environment
Copy the sample and set a secure secret:

```commandline
cp .env.sample .env
```
 Edit .env and set SECRET_KEY (escape $ as $$ if present).

## Run

Build and start:

```commandline
docker compose up -d --build
```
When you run `docker compose up -d --build`, Docker will:  
- Build the Django/DRF app image  
- Pull official images for Postgres and Redis  
- Start and link all containers together (web, db, redis, worker, beat)  


Check containers:

```commandline
docker compose ps
```

Apply migrations & create admin:

```commandline
docker compose exec web python manage.py migrate
docker compose exec -it web python manage.py createsuperuser
```
## URLs
- API Root: http://localhost:8000/api/

- Tasks: http://localhost:8000/api/tasks/

- Comments: http://localhost:8000/api/comments/

- Teams: http://localhost:8000/api/teams/

- Admin: http://localhost:8000/admin/


### What’s implemented

- Models: Task, Tag, Comment with required relations (FK, M2M, JSONField, timestamps, indexes).
-API (DRF):
  - /api/tasks/ – full CRUD, pagination, filtering (status, priority, is_archived), search (title, description), ordering (created_at, priority, due_date).
  - /api/tasks/{id}/comments/ – nested GET/POST for task comments.
  - /api/comments/ – CRUD for comments + filtering by task/author.
  - /api/teams/ – CRUD for teams (name, members).

- Browsable API enabled for quick manual testing.
- Admin: Tasks/Tags/Comments manageable via Django Admin.


### Quick create examples
Create a task (replace created_by with your admin user id, usually 1):

```commandline
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title":"One","description":"desc","status":"todo","priority":"medium","estimated_hours":"1.50","due_date":"2025-12-31T12:00:00Z","created_by":1}'
```

Add a comment to task 1:
```commandline
curl -X POST http://localhost:8000/api/tasks/1/comments/ \
  -H "Content-Type: application/json" \
  -d '{"author":1,"body":"First comment!"}'
```

### Teams examples

Create a team with one member (id=1):
```commandline
curl -X POST http://localhost:8000/api/teams/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Backend Team","member_ids":[1]}'
```

Add more members to the team (PATCH):
```
curl -X PATCH http://localhost:8000/api/teams/1/ \
  -H "Content-Type: application/json" \
  -d '{"member_ids":[1,2]}'
```

### Tech stack

- Django 5, Django REST Framework 3.16
- Postgres 15, Redis 7
- Docker Compose (web / db / redis / worker / beat)
- django-filter for filtering
- Celery (infrastructure ready, not yet used).


### Notes & trade-offs

Focused on core API and data model per test; frontend templates and Celery tasks not fully implemented due to time.
Code organized in a single app tasks/ for brevity (can be split into modules in a bigger codebase).

##### Disclaimer

This repository is provided for a recruitment technical test.
It is intended for educational and demonstration purposes.

### Acknowledgment

Thanks to **Sherpa Tribe** for the opportunity to work on this technical assignment.  
It has been a valuable learning experience and a great chance to practice Django, Docker, 
and DRF in a real-world context.


