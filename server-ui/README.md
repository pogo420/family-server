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
        cp default server-ui
        # File server-ui from /var/www/html to root /var/www/html/server-ui
        ln -s /etc/nginx/sites-available/server-ui /etc/nginx/sites-enabled/
        sudo nginx -t
        sudo systemctl reload nginx
```

