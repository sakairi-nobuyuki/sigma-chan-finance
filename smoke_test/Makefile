IMAGE_NAME=smoke_test
IMAGE_TAG=00.01

K8S_NAMESPACE=$(IMAGE_NAME)

image:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
run:
	docker run -it $(IMAGE_NAME):$(IMAGE_TAG)


start_argo_wf:
	kubectl create namespace argo
	kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/master/manifests/install.yaml
