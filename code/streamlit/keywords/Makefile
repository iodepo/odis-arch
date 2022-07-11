VERSION :=`/bin/cat VERSION`

docker-build: 
	podman build  --tag="fils/oih-keywords:$(VERSION)"  --file=./Dockerfile .

docker-push: 
	podman tag  fils/oih-keywords:$(VERSION) docker.io/fils/oih-keywords:$(VERSION)
	podman push  docker.io/fils/oih-keywords:$(VERSION)

