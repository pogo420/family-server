# Rest server

* FastApi based family rest server

## For development:

* For dev server:

```
poetry run uvicorn server_rest.main:app --reload
```

## For server deployment:

* Locally create the wheel file via `poetry build`
* Scp the wheel file to server `/opt/server_rest`
* Create virtual env
* Install wheel.
* create the start.sh 
* Do the systemd service config, check the service file.
* Service first time setup:
```
sudo systemctl daemon-reload
sudo systemctl enable server_rest
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

        location /api {
                proxy_pass http://127.0.0.1:8000/;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
        }

}
```
