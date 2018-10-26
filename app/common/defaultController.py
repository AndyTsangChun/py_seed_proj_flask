#! /usr/bin/env python
import os, json, datetime
from flask import request, render_template
from app import app

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

DT_FORMAT = "%d-%m-%Y %H:%M:%S"

@app.after_request
def add_header(response):
	response.cache_control.max_age = 60
	if 'Cache-Control' not in response.headers:
		response.headers['Cache-Control'] = 'no-store'
	return response

#====================render section=========================

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')

#===========================================================
