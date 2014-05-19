#Daniel O'Carroll
#May 19th, 2014
#DPW1405


import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_page())


#Create Page Class
class Page(object):
    def __init__(self):
        self.open = '''
<!DOCTYPE html>
<html>
    <head>
    <title></title>
    </head>
<body>'''
        self.close = '''
</body>
</html>'''
        self.content = '''
<h3></h3>
<p>Phylum: </p>
<p>Class: </p>
<p>Order: </p>
<p>Family: </p>
<p>Genus: </p>
<p>Img: </p>
<p>Life Span: </p>
<p>Habitat: </p>
<p>Geo Location: </p>'''

    def print_page(self):
        return self.open + self.content + self.close

#Create Animal Class
class AbstractAnimal(object):
    def __init__(self):
        self.name = ''
        self.phylum = ''
        self.animal_class = ''
        self.order = ''
        self.family = ''
        self.genus = ''
        self.image = ''
        self.life = ''
        self.habitat = ''
        self.location = ''
#Create First Animal
RedFox = AbstractAnimal()
RedFox.name = 'Red Fox'
RedFox.phylum = 'BS'
RedFox.animal_class = 'BS'
RedFox.order = 'BS'
RedFox.family = 'BS'
RedFox.genus = 'BS'
RedFox.image = 'BS'
RedFox.life = 'BS'
RedFox.habitat = 'BS'
RedFox.location = 'BS'

#Create Second Animal
ArcticWolf = AbstractAnimal()
ArcticWolf.name = 'Arctic Wolf'
ArcticWolf.phylum = 'BS'
ArcticWolf.animal_class = 'BS'
ArcticWolf.order = 'BS'
ArcticWolf.family = 'BS'
ArcticWolf.genus = 'BS'
ArcticWolf.image = 'BS'
ArcticWolf.life = 'BS'
ArcticWolf.habitat = 'BS'
ArcticWolf.location = 'BS'

#Create Third Animal
PolarBear = AbstractAnimal()
PolarBear.name = 'Polar Bear'
PolarBear.phylum = 'BS'
PolarBear.animal_class = 'BS'
PolarBear.order = 'BS'
PolarBear.family = 'BS'
PolarBear.genus = 'BS'
PolarBear.image = 'BS'
PolarBear.life = 'BS'
PolarBear.habitat = 'BS'
PolarBear.location = 'BS'

#Create Array to Store Animals
animals = [RedFox, ArcticWolf, PolarBear]


print animals

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
