# Server setup

## Theory:

* Node -> Physical machine. A cluster has multiple nodes.
```
Cluster
│
├── Node-1 (Pi-1)
├── Node-2 (Pi-2)
└── Node-3 (Pi-3)
```
* Namespace logical partition of cluster.
* k3s is light weight(IOTs) version of k8s(Enterprise).

## k3s setup:
* Install: `curl -sfL https://get.k3s.io | sh -`
* Remove traefik as we are using nginx(conflict with ports will be there).
```
kubectl delete helmchart traefik -n kube-system
kubectl delete helmchart traefik-crd -n kube-system
```

* Update pod subnet to add in postgres:
   * `kubectl get pods -A -o wide` -> X.Y.0.0/16

## Additional setups:
* Check the [file](pi4_ubuntu_26.04.LTS.server.md)
