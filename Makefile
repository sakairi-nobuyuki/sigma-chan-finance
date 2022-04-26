IMAGE_NAME=rnn-dayo
IMAGE_TAG=00.00

K8S_NAMESPACE=$(IMAGE_NAME)

image:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
run:
	docker run -it $(IMAGE_NAME):$(IMAGE_TAG)
reset_docker_env:
	eval $(minikube -p minikube docker-env -u)
deploy:
	eval $(minikube docker-env)
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	kubectl create namespace $(K8S_NAMESPACE)
	kubectl create -f ./manifests
	
