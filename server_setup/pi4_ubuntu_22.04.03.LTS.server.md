# Server setup steps:

## Pi-4 wifi setup:
* Follow the answer [here](https://raspberrypi.stackexchange.com/a/113642/160536).

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
* Add/Update: `AllowUsers   server_manager` (Here intentation is  NOT space it's a TAB)
* ssh demon restart: `sudo systemctl restart sshd`

## Podman Install:
* `sudo apt-get update`
* `sudo apt-get -y install podman`
* Edit: `/etc/containers/registries.conf`
* Add/Modify: `unqualified-search-registries = ["docker.io"]`


## Graceful shutdown:
* Connect to the pi-4 via keyboard and mmonitor.
* Execute `sudo shutdown -h now`.
* Unplug system.
