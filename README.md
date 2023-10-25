# Blog

## Overview

This is a sample blog built with Django and Vue.js.

## Features

- You can post articles from the Django admin page.
- It supports both Japanese and English content. (Switchable via the language switch button at the bottom of the page)

---

## Setting up the Environment

- Clone this repository & make .env

```sh
$ git clone https://github.com/selfsryo/blog
$ cp .env.sample .env
$ cp ./blog/vue3_frontend/.env.sample ./blog/vue3_frontend/.env
```

- Set up Vue.js

```sh
$ make npm-install
$ make npm-build
```

- Docker compose up & build

```sh
$ make build-up
```

- Set up Django

```sh
$ make migrate
# Load sample initial data as needed
$ make loaddata
```

- Open in your browser

```sh
$ open http://localhost:8000
```

## Adding an Article

- Add articles from the admin page.

```sh
$ make createsuperuser
$ open http://127.0.0.1:8000/admin/
```

### Notes on Adding Articles

- This blog is designed for Markdown formatting and assumes the creation of Table of Contents. Therefore, you need to include the text `[TOC]` at the very beginning of main text (in the fields of `Text` and `Text En`).

## Development

### Frontend

- The frontend is entirely written in Vue.js without editing Django templates.
- Files are stored in the ./blog/vue3_frontend/ directory.
- When you run the build, ./blog/templates/blog/index.html is created. You can see the output on port 8000 by loading it in Django.
- The following were deleted or had random values set, so you can set them as you like:
  - img tag src attributes
  - meta and link tags in ./blog/vue3_frontend/public/index.html

```sh
# Build
$ make npm-build
$ open http://localhost:8000
# During development, autoreloading is enabled, so it's safe to use port 8080.
$ make npm-serve
$ open http://localhost:8080
```

### Backend

- API Endpoint
  - http://localhost:8000/api/posts/
  - http://localhost:8000/api/tags/

```sh
# Dump the DB data in SQL format as ./db/dump.sql
# Even if you later perform 'make down-v' to remove the volume, the dumped SQL will be automatically loaded when you run 'make build-up'
$ make db-dump
```

### Common

```sh
# Python linter and formatter are automatically run on commit. Configure as needed.
$ make pre-commit
```

## Production(Deployment)

- This blog can be deployed on [Fly.io](https://fly.io/) using [GitHub Actions](./.github/workflows/fly_deploy.yml).
- Refer to [this](https://fly.io/docs/hands-on/) for creating an application on Fly.io.
- Refer to [this](https://fly.io/docs/app-guides/continuous-deployment-with-github-actions/) for issuing `FLY_API_TOKEN`.
- Thumbnails for this blog are automatically uploaded to a specified AWS S3 bucket. After creating your own bucket on AWS S3, obtain the access key of an IAM user with CRUD permissions.
- Push this branch to your own GitHub repository. (Recommended to make it a private repository.)
- Set environment variables in the GitHub repository's Secrets:
  - `FLY_API_TOKEN`: The token obtained above.
  - `SECRET_KEY`: Django's secret key (any unpredictable, random string).
  - `DATABASE_URL`: URL displayed after creating the PostgreSQL application on Fly.io.
  - `AWS_ACCESS_KEY_ID`: ID of the AWS IAM user mentioned above.
  - `AWS_SECRET_ACCESS_KEY`: Access key of the AWS IAM user mentioned above.
  - `AWS_STORAGE_BUCKET_NAME`: AWS bucket name.
- Change the `on.push.branches` in ./.github/workflows/fly_deploy.yml to your preferred branch. Deployment will be executed when you push to the configured branch.
- If you have a custom domain, change the "example" string in ./project/middleware.py to your custom domain. This way, when accessed through the URL issued by Fly.io `your-custom-domain.fly.dev`, it will redirect to your custom domain.
