from flask import Blueprint, render_template

from web.services import *

blueprint = Blueprint('web', __name__, url_prefix='/')


@blueprint.route('/')
def index():
    mma_all = get_mma_all_entries()
    mma_last_hundred = get_mma_last_hundred_entries()
    last_hundred_entries = get_last_hundred_entries()

    return render_template('index.html', mma_all=mma_all, mma_last_hundred=mma_last_hundred,
                           last_hundred_entries=last_hundred_entries)
