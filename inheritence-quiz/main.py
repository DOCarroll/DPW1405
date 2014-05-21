#Daniel O'Carroll
#DPW1405
#May 19th, 2014
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class Dog(object):
    def __init__(self):
        __dog_sound = 'Bark!'
        favorite_game = 'Fetch'

    def getsound(self, __dog_sound):
        return __dog_sound

    def getgame(self, favorite_game):
        return favorite_game


class Husky(Dog):
    Dog.__init__(self):
    husky = Dog()
    husky




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
