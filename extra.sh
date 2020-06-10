# SINGLE-BUILD
docker build -t docker_python_rest_api .
docker run -d -p 5000:5000 --name rest-api_1 docker_python_rest_api
docker tag docker_python_rest_api rafaeljvicente/docker_python_rest_api
docker push rafaeljvicente/docker_python_rest_api

# MULTI-BUILD
# https://www.docker.com/blog/multi-arch-images/
# NOTE: enable experimental features from docker
# Container creation to make multiplatform builds
docker buildx create --name mybuilder
docker buildx use mybuilder
docker buildx inspect --bootstrap

# Simple demo example for amd64, arm64 and arm32v7
mkdir test && cd test && cat <<EOF > Dockerfile
FROM ubuntu
RUN apt-get update && apt-get install -y curl
WORKDIR /src
COPY . .
EOF
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t  rafaeljvicente/demo:latest --push .
docker buildx imagetools inspect  rafaeljvicente/demo:latest

# Working python flask project
docker buildx build -t  rafaeljvicente/helloworld:latest --platform linux/386,linux/amd64,linux/arm/v6,linux/arm/v7,linux/arm64/v8,linux/ppc64le,linux/s390x --push github.com/rafaeljvicente/helloworld
