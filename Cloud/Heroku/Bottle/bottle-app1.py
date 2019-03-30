import os
from bottle import route, run, request, get, static_file, post, error, HTTPResponse, template

@route('/')
def index():
	return "<h1> Hello AkashJeez </h1>"

@route('/login')
def login():
	return "<h1> On the login page </h1>"

@route('/register')
def register():
	return "<h1> On the register page </h1>"

@route('/article/<id>')
def article(id):
	return "<h1> You are viewing article {} </h1>".format(id)

@route('/page/<id>/<name>')
def page(id, name):
	return "<h1> You are viewing page {} with a name of {} </h1>".format(id, name)

# # if method is post, will show error.
# # if method is get, you can see output as 'Posted'
@route('/posted', method='GET')
def posted():
	return "<h1> Posted </h1>"

@route('/templatee')
def templatee():
	return template('sample1', name='Guest')

@route('/username')
def username():
    name = request.cookies.username or 'Guest'
    return template('Hello {{name}}', name=name)

@error(404)
def error404(error):
	return '<h1> You have experinced a 404 </h1>'

@error(405)
def error405(error):
	return '<h1> This method is not allowed </h1>'

@error(500)
def error500(error):
	return '<h1> Something went wrong! </h1>'

@route('/zero')
def zero():
	return 1/0

@route('/querytest')
def querytest():
    param1 = request.query.param1
    param2 = request.query.param2
    return "<h1> Values of param1 is {} and param2 is {} </h1>".format(param1, param2)

if os.environ.get('APP_LOCATION') == 'heroku':
	run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
	run(host='localhost', port=8080, debug=True)