docker container stop icesum
docker container rm icesum
docker build . -t icesum:example
docker run -d --name=icesum -p 8080:8080 icesum:example
