#!/usr/bin/env python
"""Flask base-code

Uses Flask.
"""

from flask import Flask

__author__ = "Shivanshu Raj Shrivastava"
__credits__ = ["Shivanshu Raj Shrivastava"]
__license__ = "GPL"
__version__ = "0.1.0"
__email__ = "shivanshu1333@gmail.com"
__status__ = "Non-Production"

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World"


if __name__ == '__main__':
	app.run(debug = True)