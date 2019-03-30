from flask import Flask
application = Flask(__name__)

@application.route('/')
def index():
	return "<h2> AkashJeez loves Coding & Racing !!! </h2>"

if __name__ == '__main__':
	application.run(debug = True)