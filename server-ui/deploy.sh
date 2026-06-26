#!/bin/bash

set -e

podman compose pull
podman compose up -d ui

podman image prune -f
