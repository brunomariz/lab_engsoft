docker kill lab_engsoft_backend
docker kill lab_engsoft_db
docker system prune
docker rmi -f lab_engsoft_backend
docker build -t lab_engsoft_backend .
docker run --rm -d --name lab_engsoft_backend -p 8080:80 -v ${PWD}:/code lab_engsoft_backend

docker run -d \
	--name lab_engsoft_db \
	-p 5543:5432 \
	-e POSTGRES_PASSWORD=secret \
	-e POSTGRES_DB=lab_engsoft \
	-e POSTGRES_USER=aluno \
	postgres
