#!/usr/bin/env bash
docker image prune -f
docker build -t auth-service .