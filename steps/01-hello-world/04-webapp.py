from bottle import route, run, template, view

@route('/')
def index():
	return "Hello World!"

@route('/greet/<name>')
@view('hello')
def greet(name):
	return {'name': name}


if __name__ == '__main__':
	run(debug=True, reloader=True, host='0.0.0.0')
