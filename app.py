#! /usr/bin/env python
import time
import cv2
import argparse, json
from app.util import basic_args, str2bool
from app import AppController

__version__ = "1.0.0"

def run(arg):
	# import Setting
	setting_path = "setting.json"
	with open(setting_path) as setting_buffer:
		settings = json.loads(setting_buffer.read())
		settings.update(vars(arg))

	app = AppController(settings=settings, debug=True)
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
