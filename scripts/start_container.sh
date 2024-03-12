#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull dhanikataria/dhani_docker_repo:latest

# Run the Docker image as a container
echo "hello" | docker run -it dhanikataria/dhani_docker_repo cat