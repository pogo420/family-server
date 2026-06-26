#!/bin/bash

set -e

podman compose pull
podman compose up -d rest

podman image prune -f
