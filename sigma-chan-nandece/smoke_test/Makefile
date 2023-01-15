IMAGE_NAME=smoke-test
IMAGE_TAG=00.00

K8S_NAMESPACE=$(IMAGE_NAME)

image:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
run:
	docker run -it $(IMAGE_NAME):$(IMAGE_TAG)


start_argo_wf:
	kubectl create namespace argo
	kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/master/manifests/install.yaml
submit_argo_wf:
	argo submit -n argo --watch manifests/argo_workflow.yml	
submit_argo_seq_wf:
	argo submit -n argo --watch manifests/argo_wf_steps.yml		
delete_argo_wf:
	kubectl delete -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/master/manifests/install.yaml
	kubectl delete rolebinding default-admin
	kubectl delete namespace argo

