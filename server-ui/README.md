# ServerUi
UI for family server.

## To deploy:
* Execute `ng build`
* Move data to server:  `scp -P 2022 -r ./dist/* server_root@192.168.0.196:/home/server_root`

## To execute:
Run this command: `python3 -m http.server 8080 -d ./server-ui/browser/`
