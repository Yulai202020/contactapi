# fastapi

# Runing app with docker

export POSTGRES_CONTAINER="postgresdb"

export DB_PASS="password"

export DATABASE_URL="postgresql://postgres:$DB_PASS@$POSTGRES_CONTAINER:5432"

podman network create contactapi

podman pull docker.io/library/postgres

podman pull ghcr.io/yulai202020/contactapi

podman images

podman run --network contactapi -e POSTGRES_PASSWORD=$DB_PASS -d --name $POSTGRES_CONTAINER docker.io/library/postgres

podman run --network contactapi -e DATABASE_URL=$DATABASE_URL -p 8000:8000 -d ghcr.io/yulai202020/contactapi 

podman ps