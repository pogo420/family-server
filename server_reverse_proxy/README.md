# Server reverse proxy

## Paths
* All paths needs to be defined in `nginx.conf`.

## Setup in server
* copy the compose file in /opt/server_reverse_proxy
* copy the service file in /opt/server_reverse_proxy
* copy the nginx.conf file in /opt/server_reverse_proxy
* copy the deploy.sh file in /opt/server_reverse_proxy
* Do the following podman steps:

```
podman compose ps
# Get all containers
podman compose pull
```
* copy the service file(first time) to /etc/systemd/system/server_reverse_proxy.service
* First time service commands:
```
podman network create home-server
sudo systemctl daemon-reload
sudo systemctl enable server_reverse_proxy
sudo systemctl start server_reverse_proxy
```
* During changes:
```
sudo systemctl stop server_reverse_proxy
# Do all changes
sudo systemctl daemon-reload
sudo systemctl start server_reverse_proxy
```