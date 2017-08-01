#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost:3306/flask_demo?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # DEBUG = True
    DEBUG = False

config = {
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}

