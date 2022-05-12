IMAGE_NAME=time-series
IMAGE_TAG=00.00

K8S_NAMESPACE=$(IMAGE_NAME)



image:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
run:
	docker run -it $(IMAGE_NAME):$(IMAGE_TAG)
reset_docker_env:
	eval `minikube -p minikube docker-env -u`
set_docker_env:	
	eval `minikube -p minikube docker-env`
deploy:
	eval $(minikube -p minikube docker-env)
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	kubectl create namespace $(K8S_NAMESPACE)
	kubectl create -f ./manifests -n $(K8S_NAMESPACE)
apply:
	kubectl create -f ./manifests -n $(K8S_NAMESPACE)
start_argo_wf:
	kubectl create namespace argo
	kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/master/manifests/install.yaml
submit_argo_wf:
	argo submit -n argo --watch manifests/argo_workflow.yml	
submit_cron_wf:
	argo cron create -n argo manifests/cron_workflow.yml		
delete_argo_wf:
	kubectl delete -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/master/manifests/install.yaml
	kubectl delete rolebinding default-admin
	kubectl delete namespace argo

clear_deploy:
	kubectl delete -f ./manifests -n $(K8S_NAMESPACE)
clear_containers:
	docker ps -aq | xargs docker rm
clear_images:
	docker images -aq | xargs docker rmi
stop_containers:
	docker ps -aq | xargs docker stop