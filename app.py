#! /usr/bin/env python
import time
import cv2
import argparse, json
from pyutil import basic_args, str2bool, PyLogger
from app import AppController

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

def run(arg):
	# import Setting
	setting_path = "setting.json"
	with open(setting_path) as setting_buffer:
		settings = json.loads(setting_buffer.read())
		settings.update(vars(arg))
	logger = PyLogger(log=True,debug=True)

	app = AppController(settings=settings, logger=logger, debug=True)
	app.start()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Desc")
	parser = basic_args(parser)
	parser.add_argument("-host", "--host", type=str, default=None,
						help="host address")
	parser.add_argument("-p", "--port", type=int, default=8000,
						help="server port")

	arg = parser.parse_args()
	st = time.time()
	run(arg)
	print("Finished:{}".format(time.time()-st))
