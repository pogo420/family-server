# ServerUi
UI for family server.

## Package requirements

* Node and Ts

  package | version
  --|--
  node | 20.20.2
  typeScript | 5.9.3

* Angular: 21


## Deploy in server:

* copy the compose file in /opt/server_ui
* copy the service file in /opt/server_ui
* copy the deploy.sh file in /opt/server_ui
* Do the following podman steps:

```
podman compose ps
# Get all containers
podman compose pull
```
* copy the service file(first time) to /etc/systemd/system/server_ui.service
* First time service commands:
```
podman network create home-server
sudo systemctl daemon-reload
sudo systemctl enable server_ui
sudo systemctl start server_ui
```
* During changes:
```
sudo systemctl stop server_ui
# Do all changes
sudo systemctl daemon-reload
cd /opt/server_ui; podman compose pull
sudo systemctl start server_ui
```