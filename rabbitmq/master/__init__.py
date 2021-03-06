#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

from .models import db
from .views.admin.nodes import admin_nodes
from .views.admin.users import admin_users


def setup(**config):
    app = Flask(__name__)
    app.config.update(**config)

    app.db = db
    app.db.init_app(app)

    app.register_blueprint(admin_nodes)
    app.register_blueprint(admin_users)

    return app
