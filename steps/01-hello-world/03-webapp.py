from bottle import route, run, template

@route('/')
def index():
	return "Hello World!"


@route('/greet/<name>')
def greet(name):
	return template("Hello, {{name}}!", name=name)


if __name__ == '__main__':
	run(debug=True, reloader=True, host='0.0.0.0')
