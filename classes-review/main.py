import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        yoda = Character()
        yoda.name = "Yoda"
        yoda.age = 900
        yoda.gender = "Male"
        yoda.occupation = "Jedi Master"

        luke = Character()
        luke.name = "Luke Skywalker"
        luke.gender = "Male"
        luke.age = 24
        luke.occupation = "Jedi Knight"

        leia = Character()
        leia.name = "Leia Organa"
        leia.gender = "Female"
        leia.occupation = "Princess"
        leia.age = luke.age

class Characters(object):
    def __init__(self): #constructor function
        self.name = ""
        self.age = 0
        self.occupation = ""
        self.gender = ""
    def print_info(self):
        print self.name + " is a(n) " + self.occupation

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)