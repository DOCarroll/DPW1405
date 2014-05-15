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
        #define properties of animals
        self._phylum = ''
        self._class = ''
        self._order = ''
        self._family = ''
        self._genus = ''
        self._image = ''
        self._life_span = ''
        self._habitat = ''
        self._geo_location = ''

        animal = [self._phylum, self._class, self._order, self._family, self._genus, self._image, self._life_span, self._habitat, self._geo_location]
        print animal

#Create the first Animal Class
class RedFox(AbstractAnimal):
    def __init__(self):
        #add AbstractAnimal properties
        AbstractAnimal.__init__(self)
        self._phylum = ''
        self._class = ''
        self._order = ''
        self._family = ''
        self._genus = ''
        self._image = ''
        self._life_span = ''
        self._habitat = 'All over the Northern Hemisphere, some places in Southern Hemisphere.'
        self._geo_location = ''



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
