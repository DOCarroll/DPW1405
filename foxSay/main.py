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
#Create First Animal
RedFox = AbstractAnimal()
RedFox._phylum = 'BS'
RedFox._class = 'BS'
RedFox._order = 'BS'
RedFox._family = 'BS'
RedFox._genus = 'BS'
RedFox._image = 'BS'
RedFox._life = 'BS'
RedFox._habitat = 'BS'
RedFox._location = 'BS'

#Create Second Animal
ArcticWolf = AbstractAnimal()
ArcticWolf._phylum = 'BS'
ArcticWolf._class = 'BS'
ArcticWolf._order = 'BS'
ArcticWolf._family = 'BS'
ArcticWolf._genus = 'BS'
ArcticWolf._image = 'BS'
ArcticWolf._life = 'BS'
ArcticWolf._habitat = 'BS'
ArcticWolf._location = 'BS'


print animals

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
