# fastapi

# Runing API via podman

```bash

### create vars

export POSTGRES_CONTAINER="postgresdb"
export DB_PASS="password"
export DATABASE_URL="postgresql://postgres:$DB_PASS@$POSTGRES_CONTAINER:5432"

### create network

podman network create contactapi

### pull images

podman pull docker.io/library/postgres
podman pull ghcr.io/yulai202020/contactapi
podman images

### run containers

podman run --network contactapi -e POSTGRES_PASSWORD=$DB_PASS -d --name $POSTGRES_CONTAINER docker.io/library/postgres
podman run --network contactapi -e DATABASE_URL=$DATABASE_URL -p 8000:8000 -d ghcr.io/yulai202020/contactapi 

### check

podman ps
curl localhost:8000/

```