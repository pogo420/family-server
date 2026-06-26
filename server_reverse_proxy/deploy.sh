#!/bin/bash

set -e

podman compose pull
podman compose up -d proxy

podman image prune -f
