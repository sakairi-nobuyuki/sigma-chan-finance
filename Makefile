IMAGE_NAME=time-series
IMAGE_TAG=00.00

K8S_NAMESPACE=$(IMAGE_NAME)



image:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
run:
	docker run -it $(IMAGE_NAME):$(IMAGE_TAG)
reset_docker_env:
	eval $(minikube -p minikube docker-env -u)
deploy:
	eval $(minikube -p minikube docker-env)
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	kubectl create namespace $(K8S_NAMESPACE)
	kubectl create -f ./manifests -n $(K8S_NAMESPACE)
clear_deploy:
	kubectl delete -f ./manifests -n $(K8S_NAMESPACE)
clear_containers:
	docker ps -aq | xargs docker rm
clear_images:
	docker ps -aq | xargs docker stop
	docker ps -aq | xargs docker rm
	docker images -aq | xargs docker -f rmi