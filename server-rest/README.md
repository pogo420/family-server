# Rest server

* FastApi based family rest server

## For development:

* For dev server:

```
poetry run uvicorn server_rest.main:app --reload
```

## For server deployment(First time):

* Locally create the wheel file via `poetry build`
* Scp following files to server `/opt/server_rest` via home directory
   * execute: `scp -r alembic alembic.ini server_rest.service start.sh`
* Create virtual env
* Install wheel.
* Create log folder.
* Change ownership ang group of folder: `chown -R rest_user:rest_group /opt/server_rest`
* Give 755 permission to the log folder and start.sh
* Service first time setup:
```
sudo systemctl daemon-reload
sudo systemctl enable server_rest
sudo systemctl start server_rest
```

## For server deployment(Recurring):

* Locally create the wheel file via `poetry build`
* Scp the wheel file to server `/opt/server_rest`
* Scp `alembic.ini` and `alembic` folder.
* Activate virtual env
* Service stop: `sudo systemctl stop server_rest`
* uninstall old wheel: `pip uninstall server_rest`
* Install latest wheel.
* Execute: `alembic upgrade head`
* Service start: `sudo systemctl start server_rest`


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
