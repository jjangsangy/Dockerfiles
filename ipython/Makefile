TAG=jjangsangy/ipython

build:
	docker build -t $(TAG) .
bash:
	docker run -i -t $(TAG) /bin/bash -l
daemon:
	docker run -d -P $(TAG)
