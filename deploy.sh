#!/bin/bash

# Run the Docker container
docker run --rm -v $(pwd)/models:/app/models $DOCKER_USERNAME/housing-model:latest

