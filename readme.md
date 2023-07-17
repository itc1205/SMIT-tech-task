# SMIT Тестовое задание

Задача: Реализовать HTTP-сервис на с использованием FastAPI

## Используемые технологии

    - Docker
    - docker-compose
    - FastAPI
    - TortoiseORM

## Требования

* docker вместе с docker-compose
* _опционально_ make

## Запуск проекта

Для запуска через Make

```sh
make build
make up
#Для завершения работы
make down
```

Для запуска через docker-compose
```sh
docker-compose build
docker-compose up -d
#Для завершения работы
docker-compose down --remove-orphans
```
