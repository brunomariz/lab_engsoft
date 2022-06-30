docker system prune
docker kill lab_engsoft_backend
docker rmi -f lab_engsoft_backend
docker build -t lab_engsoft_backend .
docker run --rm -d --name lab_engsoft_backend -p 8080:80 -v ${PWD}:/code lab_engsoft_backend

