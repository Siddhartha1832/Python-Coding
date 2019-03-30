# Import the Flask class from the flask module.
from flask import Flask
import os

# create the app object
app = Flask(__name__)

@app.route('/')
def index():
	return "Hello world!!"

# Start the server with the 'run()' method.
if __name__ == '__main__':
	app.run(port = os.getenv('port'), debug=True)
