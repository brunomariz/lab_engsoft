# Remove running containers
docker kill lab_engsoft_backend
docker kill lab_engsoft_db
# Remove stopped containers
docker system prune
# Remove backend image 
docker rmi -f lab_engsoft_backend
# Build new image
docker build -t lab_engsoft_backend .
# Run backend contiainer
docker run --rm -d --name lab_engsoft_backend -p 8080:80 -v ${PWD}:/code lab_engsoft_backend
# Run db container
docker run -d \
	--name lab_engsoft_db \
	-p 5543:5432 \
    -v ${PWD}/scripts:/lab_scripts \
	-e POSTGRES_PASSWORD=secret \
	-e POSTGRES_DB=lab_engsoft \
	-e POSTGRES_USER=aluno \
	postgres