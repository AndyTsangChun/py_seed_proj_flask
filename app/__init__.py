__version__ = "0.0.0"

import os
# if you need a seperate config file for Flask
from .config import Config

# base variables
# templates set for .html
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'web')
# static set for .css .js and other resources
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'web')

print(TEMPLATE_DIR, STATIC_DIR)

# init flask
from flask import Flask,request
# we init Flask app here to allow other controller to easy access
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config.from_object(Config)
app.config.update(TEMPLATES_AUTO_RELOAD = True, SEND_FILE_MAX_AGE_DEFAULT=0)
#app.config['SECRET_KEY'] = 'my-key'

@app.after_request
def add_header(response):
	response.cache_control.max_age = 30
	if 'Cache-Control' not in response.headers:
		response.headers['Cache-Control'] = 'no-store'
	return response

# All controller must be import after init Flask()
from .common.appController import AppController
