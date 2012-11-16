#!/usr/bin/ python
# -*- coding: utf-8 -*-
# Auther: lomatus@163.com
# 
from flask import Flask,render_template
from flaskext.sqlalchemy import SQLAlchemy
#
app = Flask(__name__)
db = SQLAlchemy(app)
#
@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

@app.before_request
def before_request():
    db.create_all()

@app.teardown_request
def teardown_request(exception):
	db.session.close()

#import blueprint
from app.blog.views import mod as blogModule
app.register_blueprint(blogModule)

