#Daniel O'Carroll
#May 19th, 2014
#DPW1405


import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')



#Create Animal Class
class AbstractAnimal(object):
    def __init__(self):
        self._phylum = ''
        self._class = ''
        self._order = ''
        self._family = ''
        self._genus = ''
        self._image = ''
        self._life = ''
        self._habitat = ''
        self._location = ''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
