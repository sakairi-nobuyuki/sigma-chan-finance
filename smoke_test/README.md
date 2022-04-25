# Preparation
- Install `poetry`
- Install `minikube`
- Install `kubectl`

# Run API

```
$ poetry run uvicorn smoke_test:app
```

Open `Uvicorn running on http://127.0.0.1:8000` with an web browser, you can find API running.


# Deployment

## Docker build

```
$ sh build_image.sh
```


<strike>Since establishing local conrainer registry requires many painful procedures, 
sharing local Docker images to minikube might be better.

```
$ eval $(minikube docker-env)
$ docker build -t smoke-test:00 .
```
</strike>

## Deploy images

```
$ eval $(minikube docker-env)
$ kubectl apply -f ./manifests
```

<strike>
Reset image sharing between local and minikube,

```
$ eval $(minikube -p minikube docker-env -u)
```

## Minikube miscellanae

```
$ minikube tunnel
$ minikube dashboard
```
</strike>

## Confirmation of services by port-forwarding

```
$ kubectl porf-forward 8080:80
```

In another console,
```
$ curl localhost:90
```

or, open `localhost:80` in a web browser.

