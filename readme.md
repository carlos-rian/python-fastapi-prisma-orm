# Prisma Python Client ORM

## Create an instance Postgresql using Docker

```sh
docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

## Create a virtualenv and activate using Poetry

```sh
poetry shell
```

## Install dependencies

```sh
poetry install
```

## Run python file

```sh
python main.py
```