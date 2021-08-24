#! /usr/bin/env python
import os, json, datetime
from flask import request, render_template
from app import app

__version__ = "1.0.0"

DT_FORMAT = "%d-%m-%Y %H:%M:%S"

@app.after_request
def add_header(response):
	response.cache_control.max_age = 60
	if 'Cache-Control' not in response.headers:
		response.headers['Cache-Control'] = 'no-store'
	return response

@app.route('/test', methods=['GET', 'POST'])
def testFunction():
    #TODO
    #serviceSrc = request.args.get('source')
    #value = request.args.get('value')

    return "Done", 200
    