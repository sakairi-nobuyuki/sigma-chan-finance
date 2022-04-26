IMAGE_NAME=rnn-dayo
IMAGE_TAG=00.00

image:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
run:
	docker run -it $(IMAGE_NAME):$(IMAGE_TAG)