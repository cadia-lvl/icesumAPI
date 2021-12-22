docker container stop glaciersg/icesum_api:v1.0
docker container rm glaciersg/icesum_api:v1.0
docker build . -t glaciersg/icesum_api:v1.0
docker run -d --name=icesum -p 8080:8080 glaciersg/icesum_api:v1.0
