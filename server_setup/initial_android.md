#  Server initial setup post os install via UserLand

## Before start:
`sudo apt-get update && sudo apt-get upgrade`

## Install vim 
`sudo apt-get install vim`

## Install ssh
```
sudo apt-get install net-tool
sudo apt-get install iptables
sudo update-alternatives --list iptables
sudo update-alternatives --set iptables /usr/sbin/iptables-legacy
sudo apt-get install openssh-server
```

## To get ip of server:
`hostname -I`

## login into server:
`ssh <user_name>@< ip of system > -p <port_number>`

## In laptop:
```
ssh-keygen -t ed25519 -C "comment for key"
ssh-copy-id -i /path/to/public/key.pub <server_host>
```

## server disable password login:
```
vim /etc/ssh/sshd_config
set key `PasswordAuthentication` to `no`
```

## install git:
`sudo apt install git`

## end init:
`sudo apt-get update && sudo apt-get upgrade`

