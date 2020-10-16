from sys import stdout
from peewee import SqliteDatabase


# Данные для подключения к базе данных
DATABASE = SqliteDatabase('database/database.db')

# Настройки loguru
LOGURU_FORMAT = '[<blue>Server</blue>] <white>{time:HH:MM:ss}</white> <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{level}</level> - {message}'
LOGURU_CONFIG = {
    'handlers': [
        {'sink': stdout, 'level': 'INFO', 'format': LOGURU_FORMAT, 'backtrace': True, 'diagnose': True, 'enqueue': True},
        {'sink': 'file.log', 'backtrace': True, 'diagnose': True, 'enqueue': True, 'serialize': True, 'rotation': '15 MB', 'compression': 'zip'},
    ]
}
