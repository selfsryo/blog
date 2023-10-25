# Docker
build:
	docker compose -f docker-compose.dev.yml build
up:
	docker compose -f docker-compose.dev.yml up
up-d:
	docker compose -f docker-compose.dev.yml up -d
build-up:
	docker compose -f docker-compose.dev.yml up --build
build-up-d:
	docker compose -f docker-compose.dev.yml up -d --build
down:
	docker compose -f docker-compose.dev.yml down
down-v:
	docker compose -f docker-compose.dev.yml down -v
bash:
	docker compose -f docker-compose.dev.yml exec django bash

# Django
makemigrations:
	docker compose -f docker-compose.dev.yml run --rm django python manage.py makemigrations
migrate:
	docker compose -f docker-compose.dev.yml run --rm django python manage.py migrate
createsuperuser:
	docker compose -f docker-compose.dev.yml run --rm django python manage.py createsuperuser
shell:
	docker compose -f docker-compose.dev.yml run --rm django python manage.py shell
loaddata:
	docker compose -f docker-compose.dev.yml run --rm django python manage.py loaddata init.json

# Postgres
db-bash:
	docker compose -f docker-compose.dev.yml exec postgres bash
db-dump:
	docker compose -f docker-compose.dev.yml exec postgres pg_dump -U postgres --file=dump.sql postgres; docker cp blog-postgres-1:/dump.sql ./db

# Vue.js
npm-install:
	npm install --prefix ./blog/vue3_frontend
npm-serve:
	npm run serve --prefix ./blog/vue3_frontend
npm-build:
	npm run build --prefix ./blog/vue3_frontend

# Develop lint & format
pre-commit:
	python -m venv env; source env/bin/activate; pip install pre-commit; pre-commit install; deactivate
