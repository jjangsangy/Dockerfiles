
TAG=jjangsangy/python3

build:
	docker build -t $(TAG) .
bash:
	docker run -i -t $(TAG) /bin/bash -l
daemon:
	docker run -d -P $(TAG)

release:
	docker build -t $(TAG) --no-cache .
	docker push $(TAG)
