# Rest server

* FastApi based family rest server

## For development:

* For dev server:

```
poetry run uvicorn server_rest.main:app --reload
```

## Container local testing:

* Build: `podman build -t hm-rest:local .`
* Run: `podman run --rm --name home-server-rest --env-file rest.env -p 8000:8000 hm-rest:local`

## Server deployment:

* copy the compose file in /opt/server_rest
* copy the env file in /opt/server_rest
* copy the service file in /opt/server_rest
* Make sure compose subnet is updated in DB [configs](../server_setup/pi4_ubuntu_26.04.LTS.server.md#postgrest-setup).
* Host for non container SW in rest env: `host.containers.internal`
* Above means The host machine running the container. It translates to server host.
* Do the following podman steps:

```
podman compose ps
# Get all containers
podman compose pull
# migration
podman compose run --rm migrate
```
* copy the service file(first time) to /etc/systemd/system/server_rest.service
* First time service commands:
```
podman network create home-server
sudo systemctl daemon-reload
sudo systemctl enable server_rest
sudo systemctl start server_rest
```
* During changes:
```
sudo systemctl stop server_rest
# Do all changes
sudo systemctl daemon-reload
sudo systemctl start server_rest
```

## Nginix configurations(First time)
* Nginix configuration changes(First time setup, no required for source changes):
```
        su - root
        cd /etc/nginx/sites-available
        cp default server-master
        ln -s /etc/nginx/sites-available/server-master /etc/nginx/sites-enabled/
```
* Reload config if configuration changes are done
```
        sudo nginx -t
        sudo systemctl reload nginx
```
* Sample nginix configuration:
```
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _;

        location /api/ {
                proxy_pass http://127.0.0.1:8000/;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
        }

}
```
