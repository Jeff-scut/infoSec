#coding=utf-8

import addon1
import scut
from flask import Flask

addons=[
   #addon1.Joker()
   scut.Faker()
]

# def create_app(test_config=None):
#     app=Flask(__name__)
#     app.register_blueprint(indexpage.bp)

#     return app
