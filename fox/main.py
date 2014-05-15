#Daniel O'Carroll
#DPW1405
#05/14/14
#What does the Fox say?
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = AbstractAnimal()
        self.response.write(p.print_out())

#Create the Abstract Animal Class
class AbstractAnimal(object):
    def __init__(self):
        #define properties of animals
        self._name = 'Test'
        self._phylum = 'Test'
        self._class = 'Test'
        self._order = 'Test'
        self._family = 'Test'
        self._genus = 'Test'
        self._image = 'Test'
        self._life_span = 'Test'
        self._habitat = 'Test'
        self._geo_location = 'Test'

        self._open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>What Does the Fox Say?</title>
    </head>
<body>'''
        self.content = '''
        <h2>Animal: {self._name}</h2>
        <p>Phylum: {self._phylum}</p>
        <p>Class: {self._class}</p>
        <p>Order: {self._order}</p>
        <p>Family: {self._family}</p>
        <p>Genus: {self._genus}</p>
        <p>Image: {self._image}</p>
        <p>Life Span: {self._life_span}</p>
        <p>Habitat: {self._habitat}</p>
        <p>Geo-Location: {self._geo_location}</p>'''
        self._close = '''
</body>
</html>'''
    #Create a Print Out Function for the Page
    def print_out(self):
        self.update()
        return self.all
    #create an update Function for {}'s
    def update(self):
        self.all = self._open + self.content + self._close
        self.all = self.all.format(**locals())

#Create the first Animal Class
class RedFox(AbstractAnimal):
    def __init__(self):
        #add AbstractAnimal properties
        AbstractAnimal.__init__(self)
        self._name = 'Red Fox'
        self._phylum = ''
        self._class = ''
        self._order = ''
        self._family = ''
        self._genus = ''
        self._image = ''
        self._life_span = ''
        self._habitat = 'All over the Northern Hemisphere, some places in Southern Hemisphere.'
        self._geo_location = ''

#Create the first Animal Class
class PolarBear(AbstractAnimal):
    def __init__(self):
        #add AbstractAnimal properties
        AbstractAnimal.__init__(self)
        self._name = 'Polar Bear'
        self._phylum = ''
        self._class = ''
        self._order = ''
        self._family = ''
        self._genus = ''
        self._image = ''
        self._life_span = ''
        self._habitat = 'Way North'
        self._geo_location = ''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
