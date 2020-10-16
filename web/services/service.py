from typing import NoReturn, Dict

from loguru import logger
from peewee import fn, SQL

from database import Statistics


def create_new_entries(cpu_load_percent: float) -> NoReturn:
    """ Функция записывает новые данные в базу """

    try:
        Statistics.create(cpu_load_percent=cpu_load_percent)
    except:
        logger.error(f'Не удалось записать показание в БД! ({cpu_load_percent})')
        # Тут было бы не плохо обработать ошибку, или хотя бы отправить уведомление
        pass


def get_mma_all_entries() -> Dict[str, float]:
    """ Функция возвращает min, max и avg всех записей """

    query = Statistics \
        .select(fn.Max(Statistics.cpu_load_percent),
                fn.Min(Statistics.cpu_load_percent),
                fn.AVG(Statistics.cpu_load_percent))\
        .scalar(as_tuple=True)

    data = {'max': query[0], 'min': query[1], 'avg': round(query[2], 2)}

    return data


def get_mma_last_hundred_entries() -> Dict[str, float]:
    """ Функция возвращает min, max и avg 100 последних записей """

    last_hundred = Statistics\
        .select(Statistics.cpu_load_percent.alias('clp'))\
        .order_by(Statistics.create_at.desc())\
        .limit(100)

    clp = SQL('clp')

    query = Statistics\
        .select(fn.Max(clp), fn.Min(clp), fn.AVG(clp))\
        .from_(last_hundred)\
        .scalar(as_tuple=True)

    data = {'max': query[0], 'min': query[1], 'avg': round(query[2], 2)}

    return data


def get_last_hundred_entries() -> list:
    """ Функция возвращает данные о 100 последних записях в БД """

    query = Statistics.select() \
        .order_by(Statistics.create_at.desc()) \
        .limit(100).execute()

    result = []

    for item in query:
        result.append({'id': item.id,
                       'cpu_load_percent': item.cpu_load_percent,
                       'create_at': item.create_at.isoformat()})

    return result
