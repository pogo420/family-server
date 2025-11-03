# Server setup steps:

## Pi-4 wifi setup:
* Follow the steps:
   * Burn the sd card with 
      * ubuntu: 22.04.04 LTS server
      * OS customization: Add wifi ssid, wifi pass and enable ssh pass auth in service.
   * Eject and insert sd card(all file indentation -> spaces; NOT TAB)
      *  check the network-config file:
            ```
            version: 2
            renderer: networkd
            wifis:
            wlan0:
                dhcp4: true
                dhcp6: true
                optional: true
                access-points:
                "SSID":
                    password: "PassPhrase"
            ```
        * Add anything is missing/incorrect; password is always encrypted(It won't match with real one).
      * check the user-data file:
        * Adding following in the end of file
            ```
            ##Reboot after cloud-init completes
            power_state:
                mode: reboot
            ```
    * Boot up Pi-4
    
## Root password setup:
* Switch to: `sudo su - root`
* Change password: `passwd`

## Hostname change:
* Host name file: `/etc/hostname`
* Change Name -> family-server
* Reboot system: `reboot`

## Add user:
* Add user: `useradd -m server_manager`
* Set password: `sudo passwd server_manager`
* Change shell: `sudo usermod --shell /bin/bash server_manager`
* Adding user for container: `useradd -r <container_user> -s /sbin/nologin`

## Remove default user:
* `userdel -r ubuntu`

## SSh setups:
* Edit file `/etc/ssh/sshd_config`
* Add/Update: `PermitRootLogin  no`
* Add/Update: `PasswordAuthentication yes`
* Add/Update: `AllowUsers   server_manager` (Here intentation is  NOT space, it's a TAB)
* ssh demon restart: `sudo systemctl restart sshd`

## Podman Install:
* `sudo apt-get update`
* `sudo apt-get -y install podman`
* Edit: `/etc/containers/registries.conf`
* Add/Modify: `unqualified-search-registries = ["docker.io"]`

## Sqllite Install:
* `sudo apt update`
* `sudo apt install sqlite3` 
* Checking for install `sqlite3 --version`

## Nginx Install:
* `sudo apt update`
* `sudo apt upgrade`
* Intall nginx: `sudo apt install nginx`
* Check for service status: `systemctl status nginx`
* Check the for nginx configuration: vim /etc/nginx/sites-available/default

## Node Js and angular  install
* `sudo apt update`
* `sudo apt install nodejs`
* `sudo apt install npm`
* `sudo npm cache clean -f`
* `sudo npm install -g n`
* `sudo n stable`
* `npm install -g @angular/cli`

## Postgres install 
* `sudo apt update`
* `sudo apt upgrade`
* `sudo apt install postgresql`
* `sudo su postgres`
* Go to home directory: `cd`
* Create new user: `createuser <USERNAME> -P --interactive`
* Go to terminal `psql`
* create db with username `CREATE DATABASE <USERNAME>`;
* server db: `CREATE DATABASE <db-name>`; 
* Exit from terminal `exit`

## Graceful shutdown:
* Connect to the pi-4 via keyboard and mmonitor.
* Execute `sudo shutdown -h now`.
* Unplug system.

## Imporant commands:
* checking the user of containers: `podman top -l`

## System restart activity:
* Do `podman ps - a` and collect all containers.
* For all containers: `podman restart container_id`

## Podman container systemd 
* Update /etc/containers/registries.conf to add localhost in `unqualified-search-registries`
* Generating systemd unit file: `sudo podman generate systemd --new --name <container name> -f`
* Move the file to systemd location: `sudo mv -v <unit_file> /etc/systemd/system/`
* Reload systemd demon: `sudo systemctl daemon-reload`
* Enable service: `sudo systemctl enable podman-restart.service`
* Enable service: `sudo systemctl enable <SERVICE_NAME>.service`
* Check status, it will be dead now, just reboot.
* Reboot system: `sudo reboot`
