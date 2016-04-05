# -*- encoding:utf -8 -*-

from flask.blueprints import Blueprint

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")


def init(app):
    from . import views, models, forms
