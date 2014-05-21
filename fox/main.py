#Daniel O'Carroll
#DPW1405
#May 20th, 2014
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Reference the Subclasses in the main so they can be pushed into an array
        p = Page()
        bear = Bear()
        wolf = Wolf()
        fox = Fox()
        #Create Array to Store Animals
        animals = [bear, wolf, fox]
        #Detect a request
        if self.request.GET:

            a = self.request.GET['animal']
            #Check for the animal keyword, and populate accordingly
            if a == "fox":
                self.response.write(animals[2].update())
            elif a == "wolf":
                self.response.write(animals[1].update())
            elif a == "bear":
                self.response.write(animals[0].update())
        else:
            self.response.write(p.update())


#create a class that will populate the page with html
class Page(object):
    def __init__(self):
        self.open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>What Does the Fox Say?</title>
        <link rel="stylesheet" type="text/css" href="css/main.css"  />
    </head>
<body>'''

        self.nav = '''
<ul>
    <a href="?animal=fox"><li class='leftLi'>Red Fox</li></a>
    <a href="?animal=wolf"><li>Arctic Wolf</li></a>
    <a href="?animal=bear"><li>Polar Bear</li></a>
</ul>'''

        self.content = '''
<div class="content">
<h1>{self.name}</h1>
<img src="{self.image}"/>
<p>{self.phylum}</p>
<p>{self.animal_class}</p>
<p>{self.order}</p>
<p>{self.family}</p>
<p>{self.genus}</p>
<p>{self.life}</p>
<p>{self.habitat}</p>
<p>{self.location}</p>
<p>{self.sound}</p>
</div>
        '''

        self.close = '''
</body>
</html>'''
        self.all = self.open + self.nav + self.content + self.close
        #I had to assign Page the Abstract Animal attributes to
        # allow functional use of the update function across all the classes
        self.name = 'Please Pick an Animal'
        self.phylum = 'A detailed description of the animals will be displayed, along with an image.'
        self.animal_class = ''
        self.order = ''
        self.family = ''
        self.genus = ''
        self.image = ''
        self.life = ''
        self.habitat = ''
        self.location = ''
        self.sound = ''

    def update(self):
            self.all = self.all.format(**locals())
            return self.all


class AbstractAnimal(Page):
    def __init__(self):
        Page.__init__(self)
        self.name = ''
        self.phylum = 'Phylum: Chordata'
        self.animal_class = 'Class: Mammalia'
        self.order = 'Order: Carnivora'
        self.family = ''
        self.genus = ''
        self.image = ''
        self.life = ''
        self.habitat = ''
        self.location = ''

    def fetch(self, animalsub):
        self.name = animalsub.name
        self.phylum = animalsub.phylum
        self.animal_class = animalsub.animal_class
        self.order = animalsub.animal_class
        self.family = animalsub.family
        self.genus = animalsub.genus
        self.image = animalsub.image
        self.life = animalsub.life
        self.habitat = animalsub.habitat
        self.location = animalsub.location
        self.sound = animalsub.sound


#Create First Animal
class Fox(AbstractAnimal):
    def __init__(self):
        AbstractAnimal.__init__(self)
        redfox = AbstractAnimal()
        redfox.name = 'Red Fox'
        redfox.family = 'Family: Canidae'
        redfox.genus = 'Genus: Vulpes'
        redfox.image = 'css/images/redfox.jpg'
        redfox.life = 'Life Span: 5 Years'
        redfox.habitat = 'Habitat: Forests, Deserts, Mountains, and Grasslands'
        redfox.location = 'Location: BS'
        redfox.sound = 'Sound: "Ring ding ding ding"'
        self.fetch(redfox)


#Create Second Animal
class Wolf(AbstractAnimal):
    def __init__(self):
        AbstractAnimal.__init__(self)
        arcticwolf = AbstractAnimal()
        arcticwolf.name = 'Arctic Wolf'
        arcticwolf.family = 'Family: Canidae'
        arcticwolf.genus = 'Genus: Canis'
        arcticwolf.image = 'css/images/arcticwolf.jpg'
        arcticwolf.life = 'Life Span: 7 to 10 years'
        arcticwolf.habitat = 'Habitat: Arctic, most of Northern Hemisphere'
        arcticwolf.location = 'Location: BS'
        arcticwolf.sound = 'Sound: "AAWWWOOOOOOOOOO!!!"'
        self.fetch(arcticwolf)


#Create Third Animal
class Bear(AbstractAnimal):
    def __init__(self):
        AbstractAnimal.__init__(self)
        polarbear = AbstractAnimal()
        polarbear.name = 'Polar Bear'
        polarbear.family = 'Family: Ursidae'
        polarbear.genus = 'Genus: Ursus'
        polarbear.image = 'css/images/polarbear.jpg'
        polarbear.life = 'Life Span: 15 to 18 Years'
        polarbear.habitat = 'Habitat: The entire Arctic Region'
        polarbear.location = 'Location: BS'
        polarbear.sound = 'Sound: "GRARAWWWRRRRRR!"'
        self.fetch(polarbear)


app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
