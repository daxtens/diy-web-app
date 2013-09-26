from mongoengine import *

connect('slogans')

class Noun(Document):
    noun = StringField(required=True)


class Slogan(Document):
    slogan = StringField(required=True)

