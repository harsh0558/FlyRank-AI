## Database

This project uses Postgres running in Docker.

Start it with:
​```bash
docker run --name taskdb -e POSTGRES_PASSWORD=dev -e POSTGRES_DB=tasks -p 5432:5432 -v taskdata:/var/lib/postgresql/data -d postgres
​```

Check it's running: `docker ps`
Connect with psql: `docker exec -it taskdb psql -U postgres -d tasks`