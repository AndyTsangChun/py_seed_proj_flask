#! /usr/bin/env python

from app import app

__version__ = "1.0.0"

DEFAULT_USE_RELOADER = True

class AppController():
	def __init__(self, settings, **kwargs):
		self.settings = settings
		self.debug = kwargs["debug"]

	def start(self):
		# host: 0.0.0.0 to run on machines IP address, default localhost
		# port: default run on 5000
		if "host" in self.settings and self.checkHost(self.settings["host"]) and "port" in self.settings:
			app.run(debug=self.debug, host=self.settings["host"], port=self.settings["port"], use_reloader=DEFAULT_USE_RELOADER)
		elif "host" in self.settings and self.checkHost(self.settings["host"]):
			app.run(debug=self.debug, host=self.settings["host"], use_reloader=DEFAULT_USE_RELOADER)
		elif "port" in self.settings:
			app.run(debug=self.debug, port=self.settings["port"], use_reloader=DEFAULT_USE_RELOADER)
		else:
			app.run(debug=self.debug, use_reloader=DEFAULT_USE_RELOADER)

	def checkHost(self, host):
		if host is not None:
			# Do sth to check the host is a valid host address or not
			# E.g. its a valid IPv4 address
			return True
		return False