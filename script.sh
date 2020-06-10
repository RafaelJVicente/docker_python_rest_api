docker buildx create --name mybuilder
docker buildx use mybuilder
docker buildx inspect --bootstrap

docker buildx build -t rafaeljvicente/docker_python_rest_api:latest --platform linux/386,linux/amd64,linux/arm/v6,linux/arm/v7,linux/arm64/v8,linux/ppc64le,linux/s390x --push github.com/RafaelJVicente/docker_python_rest_api
