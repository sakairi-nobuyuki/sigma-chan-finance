# Preparation
- Install `poetry`
- Install `minikube`
- Install `kubectl`

# Argo workflow

Start minikube.

```
$ minikube start
```

Create a Docker image under minikube environment.

```
$ eval $(minikube -p minikube docker-env)
$ make image
```

Install Argo workflow.

```
$ make start_argo_wf
```

Submit job.

```
$ make submit_argo_wf
```

Start Argo workflow dashboard by port forwarding.

```
$ kubectl -n argo port-forward deployment/argo-server 2746:2746 &
```

Access to `https://localhost:2746` with your web browser. It will complain you to the volunarability or something like that, however let us ingnore it and access to the port. Then the Argo workflow dashboard starts and may require you to put password or credential something. Then run the following command to get credentials.

```
$ kubectl -n argo exec -it $(kubectl get --no-headers=true pods -n argo -o name -l app=argo-server) -- argo auth token
```

Copy the password and past it to the password input field of the Argo workflow dashboard.

Stop the workflow and minikube.

```
$ make delete_argo_wf
$ minikube delete
$ eval $(minikube -p minikube docker-env -u)
```

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

