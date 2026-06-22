# Server setup steps:

## Pi-4 wifi setup:
* Follow the steps:
   * system boot setup - usb 
      * ubuntu: 26.04 server
      * OS customization: 
         * Add wifi ssid, wifi pass
         * enable ssh pass auth in service.
         * Set host name
         * Set user name/passwd
      * Keyboard: us
   * connect monitor
   * connect keyboard
   * Boot up Pi-4
    
## Root password setup:
* Switch to: `sudo su - root`
* Change password: `passwd`
* Do all setup in root.

## Enable wifi(Ethernet recommended for main server):
* Check wifi: `ip a`
* wlan0 status -> DOWN
* vim `/etc/netplan/50-cloud-init.yaml` and update password, example file
   ```
   network:
   version: 2
   renderer: networkd
   ethernets:
      eth0:
         dhcp4: true
   wifis:
      wlan0:
         dhcp4: true
         access-points:
         "WIFI_NAME":
            password: "PASSWORD"
   ```
* Bring up interface: `ip link set wlan0 up`
* Apply netplan: `netplan apply`
* Reboot: `reboot`
* Disable power saver: `sudo iw dev wlan0 set power_save off`

## SSh setups:
* Edit file `/etc/ssh/sshd_config`
* Add/Update: `PermitRootLogin  no`
* Add/Update: `PasswordAuthentication yes`
* Add/Update: `AllowUsers   server_manager` (Here intentation is  NOT space, it's a TAB)
* ssh demon restart: `sudo systemctl restart sshd`

## Time setup:
```
# su to root
# for the status of date time (NTP service has to be active)
timedatectl

# setup timezone:
timedatectl set-timezone Asia/Kolkata
```

## Nginx Install:
* commands to install
    ```
    apt update
    apt upgrade
    apt install nginx
    systemctl status nginx
    ```
* Check the for nginx configuration: vim /etc/nginx/sites-available/default
* If issue seen, check different browser.

## Node Js and angular install
* Steps:
    ```
    apt update
    apt install nodejs
    apt install npm
    npm cache clean -f
    npm install -g n
    n stable
    npm install -g @angular/cli
    ```

## postgrest setup:
* Steps:
```
apt update && sudo apt upgrade -y
apt install postgresql postgresql-contrib -y
systemctl status postgresql
pg_lsclusters # if not output execute the below command
pg_createcluster 14 main --start

# change passwd
sudo -u postgres psql
ALTER USER postgres PASSWORD 'yourpassword';

# enable passwd login:
# Edit the file with below content(118 and 123)
# local   all             postgres                                md5
# local   all             all                                     md5
vim /etc/postgresql/18/main/pg_hba.conf

# Make listen_addresses='*'
vim /etc/postgresql/18/main/postgresql.conf

# Get the podman compose subnet IP and add in pg_hba
podman network inspect <folder_containing_compose>_default

# Updae following in the end
# host    all    all    <subnet>    scram-sha-256
vim /etc/postgresql/18/main/pg_hba.conf

# restart postgres
systemctl restart postgresql

# testing connection
psql -U postgres -h localhost

```

## Setup tailscale:
* Private vpn setup for remote access.
   * Install tailscale: `curl -fsSL https://tailscale.com/install.sh | sh`
   * Up tailscale: `tailscale up`
   * Open the link and authenticate in different system, as we don't have browser.
   * Create services: `sudo systemctl enable tailscaled; sudo systemctl start tailscaled`
 
# Setup MQTT:
* Update all: `apt update; apt upgrade -y`
* Install broker and client: `apt install mosquitto mosquitto-clients -y`
* Enable broker service:
   ```
   systemctl enable mosquitto
   systemctl start mosquitto
   systemctl status mosquitto
   ```
* Testing broker:
   * terminal 1: `mosquitto_sub -t test/topic`
   * terminal 2: `mosquitto_pub -t test/topic -m "Hello MQTT"`
* Creating user and password for MQTT:
   * `mosquitto_passwd -c /etc/mosquitto/passwd <user_name>`
* Configure Auth:
   * Creating file: vim /etc/mosquitto/conf.d/auth.conf
   * Add following cotent
   ```
   allow_anonymous false
   password_file /etc/mosquitto/passwd

   listener 1883
   ```
* setting permissions:
   ```
   sudo chown root:mosquitto /etc/mosquitto/passwd
   sudo chmod 640 /etc/mosquitto/passwd
   ```
* Restart broker service:
   ```
   systemctl restart mosquitto
   systemctl status mosquitto
   ```
* validate flow:
   * `mosquitto_sub -h localhost -u <user> -P <pass> -t test/topic`
   * `mosquitto_pub -h localhost -u <user> -P <pass> -t test/topic -m "hello world"`

## Graceful shutdown:
* Connect to the pi-4 via keyboard and mmonitor.
* Execute `sudo shutdown -h now`.
* Unplug system.


## Fixed ip for server:
* Execute `ip addr show eth0` for current IP address of server(via ethernet): `inet <IP>/24`
* Execute `ip route` for gatewayIP: `default via <gatewayIP> dev eth0
* Edit netplan config: `/etc/netplan/<config>.yaml`

   ```
         dhcp4: true
         addresses:
          - <STATIC_IP>/24
         routes:
          - to: default
            via: <GATEWAY_IP>

   ```
* From router config choose STATIC_IP, between range and not allocated.
* Check config via `netplay generate`
* Apply changes `netplan apply`
* Set hostmane of server.
* Install `apt install avahi-daemon` in server.
* Reboot and server will be accessable via `hostname.local`