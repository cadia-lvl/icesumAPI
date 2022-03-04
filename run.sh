docker container stop icesum_api
docker container rm icesum_api
docker build . -t glaciersg/icesum_api:v1.0
docker run -d --name=icesum_api -p 8080:8080 glaciersg/icesum_api:v1.0
