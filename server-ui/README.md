# ServerUi
UI for family server.

## To deploy in Android server:
* Execute `ng build`
* Move data to server:  `scp -P 2022 -r ./dist/* server_root@192.168.0.196:/home/server_root`

## To deploy in home server:
* Via github actions workflow: `server.ui.deploy.yml`

## To execute:
Run this command: `python3 -m http.server 8080 -d ./server-ui/browser/`


## To execute in container:
```
podman build -t server-ui:tag .
podman run -it --rm --name ui-check -p external_port:8080 localhost/server-ui:tag
```
