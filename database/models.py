from peewee import Model, PrimaryKeyField, FloatField, DateTimeField

from datetime import datetime

from settings import DATABASE


class BaseModel(Model):
    class Meta:
        database = DATABASE
        if database.is_closed():
            database.connect()


class Statistics(BaseModel):
    """ Модель для описания таблицы с данными """

    # Первичный ключ
    id = PrimaryKeyField(unique=True, null=False)

    # Нагрузка на CPU в %
    cpu_load_percent: float = FloatField(null=False)

    # Время прихода запроса
    create_at: datetime = DateTimeField(default=datetime.now)
