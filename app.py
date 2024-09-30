import time

from flask import Flask

print('Startup wait...')
time.sleep(60)

app = Flask(__name__)

@app.route('/')
def index():
	print('Got request, waiting...')
	time.sleep(10)
	print('Request done!')
	return '<p>Hello, World!</p>'
