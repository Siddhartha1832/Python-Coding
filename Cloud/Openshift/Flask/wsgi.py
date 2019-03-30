from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
	return "Hello there! Welcome here!"

if __name__ == "__main__":
	application.run()
