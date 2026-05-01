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

## Enable wifi:
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

# postgrest setup 
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

# testing connection
psql -U postgres -h localhost

```

# Setu up tailscale:
* Private vpn setup for remote access.
   * Install tailscale: `curl -fsSL https://tailscale.com/install.sh | sh`
   * Up tailscale: `tailscale up`
   * Open the link and authenticate in different system, as we don't have browser.
   * Create services: `sudo systemctl enable tailscaled; sudo systemctl start tailscaled`
 

## Graceful shutdown:
* Connect to the pi-4 via keyboard and mmonitor.
* Execute `sudo shutdown -h now`.
* Unplug system.
