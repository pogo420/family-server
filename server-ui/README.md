# ServerUi
UI for family server.

## Deploy in server
* clone the repo.
* navigate to server-ui
* Execute following:
```
        su - root
        npm install
        ng build --configuration production
        cp -r /home/server_manager/family-server/server-ui/dist/server-ui/browser/  /var/www/html/server-ui
```

* Nginix configuration changes(First time setup, no required for source changes):
```
        su - root
        cd /etc/nginx/sites-available
        cp default server-master
        # File server-master from /var/www/html to root /var/www/html/server-ui
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

        location / {
                root /var/www/html/server-ui;
                index index.html index.htm index.nginx-debian.html;
                try_files $uri $uri/ =404;
        }
}
```
