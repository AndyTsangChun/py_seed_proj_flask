import numpy as np
import datetime

DT_FORMAT = "%d-%m-%Y %H:%M:%S"

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

class MyCore:
	def __init__(self):
		#np.random.seed(1)
		seed = np.random.rand()
		self.x = int(3*seed)
		self.y = int(5*seed)

	def coreFunction(self):
		return "Now: {}, Lucky Number = {}".format(datetime.datetime.now().strftime(DT_FORMAT), self.x+self.y)