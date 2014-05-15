#Daniel O'Carroll
#DPW1405
#05/14/14
#What does the Fox say?
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out())

#Create a Page class
class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>What Does the Fox Say?</title>
    </head>
<body>'''
        self._content = '''
This is where all of the content will go'''
        self._close = '''
</body>
</html>'''
    #Create a Print Out Function for the Page
    def print_out(self):
        self.update()
        return self.all
    #create an update Function for {}'s
    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())



#Create the Abstract Animal Class
class AbstractAnimal(object):
    def __init__(self):
        #define properties of animals
        self._phylum = 'Test'
        self._class = 'Test'
        self._order = 'Test'
        self._family = 'Test'
        self._genus = 'Test'
        self._image = 'Test'
        self._life_span = 'Test'
        self._habitat = 'Test'
        self._geo_location = 'Test'

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
