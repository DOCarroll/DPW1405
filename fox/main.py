#Daniel O'Carroll
#DPW1405
#05/14/14
#What does the Fox say?
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

#Create the Abstract Animal Class
class AbstractAnimal(object):
    def __init__(self):


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
