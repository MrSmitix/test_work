# Тестовое задание на full stack python junior
ТЗ: [docs.google.com](https://docs.google.com/document/u/0/d/1MMvfrpp4B28eoFqr-TuFoufCBbX848PiyJvijB9RMeU/mobilebasic)

Разработка небольшой системы мониторинга. Клиент и Сервер.

## Запуск сервера:
### Установка зависимостей
> pip install requirements.txt
### Запуск
> python server.py


## Запуск клиента (клиент находится в папке [client](https://github.com/MrSmitix/test_work/client)):
### Установка зависимостей (requirements.txt из папки client)
> pip install requirements.txt
### Изменяете путь до client.py в файле cpu_logger.service на тот который у вас
### Перемещаете файл cpu_logger.service в /lib/systemd/system/
### Разрешаете его запуск
> systemctl enable cpu_logger
### Запускаете командой
> systemctl start cpu_logger

## В базе уже присутствует около 500 строк.

Что и где находится?
- api - роутер реализующие работу api
- web - роутер реализующий поведение сайта
- web/service - функций для работы с данными в бд, дабы не делать это во вью, вынес в отдельный модуль
- database - файлы моделей и сама база данных (sqlite3)
- client - демон

С фронтом не сильно дружу, по этому дашборд выглядит так топорно. 
