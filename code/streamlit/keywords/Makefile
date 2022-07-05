BINARY := apsu
VERSION :=`/bin/cat VERSION`
.DEFAULT_GOAL := apsu

docker-awslambda: 
	podman build  --tag="ufokn/apsu-lambda:$(VERSION)"  --file=./build/lambda/Dockerfile .

docker-awslambdapush: 
	podman tag  ufokn/apsu-lambda:$(VERSION) 412361828787.dkr.ecr.us-east-1.amazonaws.com/apsu-lambda:latest
	podman push 412361828787.dkr.ecr.us-east-1.amazonaws.com/apsu-lambda:latest


