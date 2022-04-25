# sigma-chan-nandece
そうです。私がΣちゃんなんです。

## Docker
### Docker build
```
$ docker build -t sigma-chan-nandece:00.00 .
```


### Docker run for inference
```
$ docker run -it sigma-chan-nandece:00.00 python3 time_series_analysis.py --help

### Minikube

```
$ eval $(minikube docker-env)
```

## Argo

```
$ kubectl create namespace argo
$ kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=default:default
$ kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/master/manifests/install.yaml
$ kubectl -n argo port-forward deployment/argo-server 3333:3333 &
```

```
$ kubectl -n argo exec -it $(kubectl get --no-headers=true pods -n argo -o name -l app=argo-server) -- argo auth token
```