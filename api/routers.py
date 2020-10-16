from flask import Blueprint, request
from flask_restful import Api, Resource

from web.services import *

blueprint = Blueprint('api', __name__, url_prefix='/api')
blueprint_api = Api(blueprint)


@blueprint.route('/')
def index():
    return 'Here is api'


class Handler(Resource):
    def put(self):
        cpu_load_percent = float(request.form['cpu_load_percent'])

        create_new_entries(cpu_load_percent)

        return {'status': 'ok'}


class GettingStatistics(Resource):
    def get(self):
        return {'status': 'ok', 'result': {
            'min_max_avg': {
                'all': get_mma_all_entries(),
                'last_hundred': get_mma_last_hundred_entries(),
            },
            'last_hundred_entries': get_last_hundred_entries()
        }}


blueprint_api.add_resource(Handler, '/handler')
blueprint_api.add_resource(GettingStatistics, '/statistic')
