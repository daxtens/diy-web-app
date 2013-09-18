from bottle import route, run, template, view, static_file
import os

root = os.path.dirname(__file__)
static_root = os.path.join(root, "static")


@route('/')
@route('/greet/<name>')
@view('hello')
def greet(name="World"):
	return {'name': name}


@route('/static/<path:path>')
def static(path):
    return static_file(path, root=static_root)

if __name__ == '__main__':
	run(debug=True, reloader=True, host='0.0.0.0')
