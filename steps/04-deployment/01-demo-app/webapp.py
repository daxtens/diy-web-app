from bottle import route, run, template, view, \
    static_file, response
from database import *
import os
import random
import json

root = os.path.dirname(__file__)
static_root = os.path.join(root, "static")
if root:
	os.chdir(root)

def randomslogan():
	slogan = random.choice(Slogan.objects()).slogan
	noun = random.choice(Noun.objects()).noun
	return {'slogan': slogan + ' ' + noun + '.'}

@route('/')
@view('index')
def slogan():
	return randomslogan()

@route('/slogan.json')
def sloganjson():
	response.set_header('Content-Type', 'application/json')
	return json.dumps(randomslogan())

@route('/noun/<noun>')
@view('saved')
def saveNoun(noun):
	# todo: not everyone should be able to set.
	dbnoun = Noun.objects(noun=noun).first() or Noun()
	dbnoun.noun = noun
	dbnoun.save()
	return {'type': 'noun', 'saved': noun}

@route('/slogan/<slogan>')
@view('saved')
def saveSlogan(slogan):
	# todo: not everyone should be able to set.
	dbslogan = Slogan.objects(slogan=slogan).first() or Slogan()
	dbslogan.slogan = slogan
	dbslogan.save()
	return {'type': 'slogan', 'saved': slogan}


@route('/contact')
@view('contact')
def contact():
	return {}

@route('/static/<path:path>')
def static(path):
    return static_file(path, root=static_root)

if __name__ == '__main__':
	run(host='0.0.0.0')
