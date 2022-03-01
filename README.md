## Desafio Scraping da Promáxima Gestão

### Pré-requisitos

- Docker
- Docker-Compose

### Uso

```
docker-compose build
```

```
docker-compose up
```

Depois do container estar pronto pegue o id do container e acesse o shell do mesmo:

```
docker container ls
```

```
docker exec -it <ID_CONTAINER> sh
```

E então faça as migrações:

```
python manange.py makemigrations
```

```
python manange.py migrate
```

E por fim acesse localhost:8000/scraping
