# ServerUi
UI for family server.

## Deploy in server
* clone the repo.
* navigate to server-ui
* Run `su - root`
* Run `ng build`
* Run `cp -r /home/server_manager/family-server/server-ui/dist/server-ui/browser/  /var/www/html/server-ui`
* Edit `/etc/nginx/sites-enabled/default` for `root /var/www/html/server-ui`
* Nginix config with angular files.
```
        location / {
                root /var/www/html/server-ui;
                index index.html;
                try_files $uri $uri/ =404;
        }
```

