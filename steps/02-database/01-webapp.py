from bottle import route, run, template, view, static_file
from mongoengine import *
import os

root = os.path.dirname(__file__)
static_root = os.path.join(root, "static")

connect('greeter')

class Name(Document):
	name=StringField(default="World")

@route('/')
@route('/greet/<name>')
@view('hello')
def greet(name=None):
	# todo: not everyone should be able to set.
	dbname = Name.objects().first() or Name()
	if name is not None:
		dbname.name = name
		dbname.save()
	return {'name': dbname.name}


@route('/static/<path:path>')
def static(path):
    return static_file(path, root=static_root)

if __name__ == '__main__':
	run(debug=True, reloader=True, host='0.0.0.0')
