# ServerUi
UI for family server.

## To deploy in Android server:
* Execute `ng build`
* Move data to server:  `scp -P 2022 -r ./dist/* server_root@192.168.0.196:/home/server_root`

## To deploy in home server:
* Via github actions workflow: `server.ui.deploy.yml`

## To execute:
Run this command: `python3 -m http.server 8080 -d ./server-ui/browser/`


## To execute in container locally:
```
podman build -t server-ui:tag .
podman run -it --rm --name server-ui -p <external_port>:8080 localhost/server-ui:tag
```

## To execute in PI4(Manually):
```
# Build is done via actions, serveruitag is having the latest tag
# Adding user to run the comtainer: useradd -r server-ui -s /sbin/nologin
# steps to execute container:
serveruitag=<take the value from ../server_setup/application_tags.md>
username=g2pfamilyserver
podman login -u $username -p <> -v docker.io
podman pull $username/server-ui:$serveruitag
podman run -d --user "$(id -u server-ui):$(id -g server-ui)" --rm --name server-ui -p <external_port>:8080 $username/server-ui:$serveruitag
```
