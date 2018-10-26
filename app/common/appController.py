#! /usr/bin/env python

from app import app

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

class AppController():
	def __init__(self, settings, logger, **kwargs):
		self.settings = settings
		self.__logger=logger

	def start(self):
		app.run(debug=True, use_reloader=True)
