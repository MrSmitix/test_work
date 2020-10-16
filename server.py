from flask import Flask, g
from flask_restful import Api

from loguru import logger

from api import blueprint as api_bl
from web import blueprint as app_bl

from settings import DATABASE, LOGURU_CONFIG

# Настрайваем логгер
logger.configure(**LOGURU_CONFIG)

app = Flask(__name__)
api = Api(app)

app.register_blueprint(api_bl)
app.register_blueprint(app_bl)


@app.errorhandler(500)
def handler(error):
    """ Функция вызывается в случает внутренней ошибки сервера """

    g.db.close()

    logger.error(f'500 ошибка! {error}')

    return {'status': 'error', 'message': str(error)}


@app.before_request
def before_request():
    """ Функция вызывается перед началом обработки запроса и проверяет подключение к БД """

    g.db = DATABASE
    if g.db.is_closed():
        g.db.connect()


@app.after_request
def after_request(response):
    """ Функция вызывается после обработки запроса и закрывает подключение к БД """

    g.db.close()

    return response


if __name__ == '__main__':
    app.run(debug=True)
