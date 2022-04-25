eval $(minikube docker-env)
docker build -t smoke-test:00.00 .
#eval $(minikube -p minikube docker-env -u)