# fastapi

# Runing app with docker

export DB_PASS="password"

export DATABASE_URL="postgresql://postgres:$DB_PASS@localhost:5432"

podman create network contactapi

podman pull docker.io/library/postgres

podman pull ghcr.io/yulai202020/contactapi

podman images

podman run --network contactapi -e POSTGRES_PASSWORD=$DB_PASS -d --name postgresdb docker.io/library/postgres

podman run --network contactapi -e DATABASE_URL=$DATABASE_URL -p 8000:8000 -d ghcr.io/yulai202020/contactapi 

podman ps