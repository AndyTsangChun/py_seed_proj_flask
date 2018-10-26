#! /usr/bin/env python

import unittest
import inspect

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

TEST_MSG = "Test {0:20} : [{1:4}]"
class TestExample(unittest.TestCase):
	def setUp(self):
		pass

	def test01Function(self):
		start_time = time.time()

		#assert sth u want to test
		
		print((TEST_MSG+" T: {2:.2f}s").format(inspect.stack()[0][3],"OK",time.time()-start_time))


