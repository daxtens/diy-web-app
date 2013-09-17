from bottle import route, run

@route('/')
def index():
	return "Hello World!"


if __name__ == '__main__':
	run(debug=True, host='0.0.0.0')
