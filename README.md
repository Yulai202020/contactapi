# fastapi

# Runing API via podman

```bash

### create vars

export DB_IMAGE="docker.io/library/postgres"
export DB_CONTAINER="postgresdb"

export DB_PASS="password"
export DATABASE_URL="postgresql://postgres:$DB_PASS@$DB_CONTAINER:5432"

export APP_IMAGE="ghcr.io/yulai202020/contactapi"

### create network

podman network create contactapi

### pull images

podman pull $DB_IMAGE
podman pull $APP_IMAGE
podman images

### run containers

podman run --network contactapi -e POSTGRES_PASSWORD=$DB_PASS -d --name $DB_CONTAINER $DB_IMAGE
podman run --network contactapi -e DATABASE_URL=$DATABASE_URL -p 8000:8000 -d $APP_IMAGE

### check

podman ps
curl http://localhost:8000/

```