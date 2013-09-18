from bottle import route, run, template, view

@route('/')
@route('/greet/<name>')
@view('hello')
def greet(name="World"):
	return {'name': name}

if __name__ == '__main__':
	run(debug=True, reloader=True, host='0.0.0.0')
