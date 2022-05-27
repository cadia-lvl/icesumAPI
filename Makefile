build:
	docker build . -t icesum_api
run:
	docker run -d -p 8080:8080 --name=icesum icesum_api
stop:
	docker stop icesum
	docker rm icesum
