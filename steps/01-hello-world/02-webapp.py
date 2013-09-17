from bottle import route, run

@route('/')
def index():
	return "Hello World!"


@route('/greet/<name>')
def greet(name):
	return "Hello, %s!" % name


if __name__ == '__main__':
	run(debug=True, host='0.0.0.0')
