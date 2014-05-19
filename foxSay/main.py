#Daniel O'Carroll
#May 19th, 2014
#DPW1405


import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_page(animals))



#Create Page Class
class Page(object):
    def __init__(self):
        self.open = '''
<!DOCTYPE html>
<html>
    <head>
    <title>What Does the Fox Say</title>
    </head>
<body>'''
        self.close = '''
</body>
</html>'''
        self.content = '''
        <h3>{self.name}</h3>
<p>Phylum: {self.phylum}</p>
<p>Class: {self.animal_class}</p>
<p>Order: {self.order}</p>
<p>Family: {self.family}</p>
<p>Genus: {self.genus}</p>
<p>Img: {self.image}</p>
<p>Life Span: {self.life}</p>
<p>Habitat: {self.habitat}</p>
<p>Geo Location: {self.location}</p>
        '''
        self.nav = '''
<ul>
    <a href='?animals=RedFox'><li>Red Fox</li></a>
    <a href='?animals=ArcticWolf'><li>Arctic Wolf</li></a>
    <a href='?animals=PolarBear'><li>Polar Bear</li></a>
</ul>
        '''
        self.all = self.open + self.nav + self.content + self.close


    def print_page(self, animals):
        for i in animals:
           self.name = i.name
           self.phylum = i.phylum
           self.animal_class = i.animal_class
           self.order = i.order
           self.family = i.family
           self.genus = i.genus
           self.image = i.image
           self.life  = i.life
           self.habitat = i.habitat
           self.location = i.location

        self.update()
        return self.all

    def update(self):
        self.all = self.open + self.nav + self.content + self.close
        self.all = self.all.format(**locals())

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
ArcticWolf.phylum = 'Chordata'
ArcticWolf.animal_class = 'Mammalia'
ArcticWolf.order = 'Carnivora'
ArcticWolf.family = 'Canidae'
ArcticWolf.genus = 'Canis'
ArcticWolf.image = 'BS'
ArcticWolf.life = '7 to 10 years'
ArcticWolf.habitat = 'Arctic, most of Northern Hemisphere'
ArcticWolf.location = 'BS'

#Create Third Animal
PolarBear = AbstractAnimal()
PolarBear.name = 'Polar Bear'
PolarBear.phylum = 'Chordata'
PolarBear.animal_class = 'Mammalia'
PolarBear.order = 'Carnivora'
PolarBear.family = 'Ursidae'
PolarBear.genus = 'Ursus'
PolarBear.image = 'BS'
PolarBear.life = '15 to 18 Years'
PolarBear.habitat = 'The entire Arctic Region'
PolarBear.location = 'BS'

#Create Array to Store Animals
animals = [RedFox, ArcticWolf, PolarBear]


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
