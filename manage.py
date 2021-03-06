#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

from flask_script import Manager

from app import create_app, db


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
