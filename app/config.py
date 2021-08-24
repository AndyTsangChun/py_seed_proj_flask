#! /usr/bin/env python
import os

__version__ = "1.0.0"

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'