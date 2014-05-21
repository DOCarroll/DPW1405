#Daniel O'Carroll
#May 19th, 2014
#DPW1405


import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        if self.request.GET:
            animal = self.request.GET['animals']
            if animal == 'RedFox':
                animals = 'RedFox'
                p.content = p.content.format(**locals())
                self.response.write(p.print_page(animals))
                self.response.write(animals[0].name)
        else:
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
                    <link rel='stylesheet' type="text/css" href='css/main.css' />
                <body>'''

            self.nav = '''
                <ul>
                    <a href='?animals=RedFox'><li>Red Fox</li></a>
                    <a href='?animals=ArcticWolf'><li>Arctic Wolf</li></a>
                    <a href='?animals=PolarBear'><li>Polar Bear</li></a>
                </ul>
                        '''

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

            self.close = '''
                </body>
                </html>'''

            self.all = self.open + self.nav + self.content + self.close


    def print_page(self, animals):
        for i in animals:
            animals.name = i.name
            animals.phylum = i.phylum
            animals.animal_class = i.animal_class
            animals.order = i.order
            animals.family = i.family
            animals.genus = i.genus
            animals.image = i.image
            animals.life = i.life
            animals.habitat = i.habitat
            animals.location = i.location

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
        RedFox.name = 'RedFox'
        RedFox.phylum = 'Chordata'
        RedFox.animal_class = 'Mammalia'
        RedFox.order = 'Carnivora'
        RedFox.family = 'Canidae'
        RedFox.genus = 'Vulpes'
        RedFox.image = 'BS'
        RedFox.life = '5 Years'
        RedFox.habitat = 'Forests, Deserts, Mountains, and Grasslands'
        RedFox.location = 'BS'


        #Create Second Animal
        ArcticWolf = AbstractAnimal()
        ArcticWolf.name = 'ArcticWolf'
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
        PolarBear.name = 'PolarBear'
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
        animals = [RedFox, PolarBear, ArcticWolf]

app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
