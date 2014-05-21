#Daniel O'Carroll
#May 19th, 2014
#DPW1405


import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):

        #Create First Animal
        redfox = AbstractAnimal()
        redfox.name = 'redfox'
        redfox.phylum = 'Chordata'
        redfox.animal_class = 'Mammalia'
        redfox.order = 'Carnivora'
        redfox.family = 'Canidae'
        redfox.genus = 'Vulpes'
        redfox.image = 'BS'
        redfox.life = '5 Years'
        redfox.habitat = 'Forests, Deserts, Mountains, and Grasslands'
        redfox.location = 'BS'

        #Create Second Animal
        arcticwolf = ArcticWolf()
        arcticwolf.name = 'arcticwolf'
        arcticwolf.phylum = 'Chordata'
        arcticwolf.animal_class = 'Mammalia'
        arcticwolf.order = 'Carnivora'
        arcticwolf.family = 'Canidae'
        arcticwolf.genus = 'Canis'
        arcticwolf.image = 'BS'
        arcticwolf.life = '7 to 10 years'
        arcticwolf.habitat = 'Arctic, most of Northern Hemisphere'
        arcticwolf.location = 'BS'

        #Create Third Animal
        polarbear = PolarBear()
        polarbear.name = 'polarbear'
        polarbear.phylum = 'Chordata'
        polarbear.animal_class = 'Mammalia'
        polarbear.order = 'Carnivora'
        polarbear.family = 'Ursidae'
        polarbear.genus = 'Ursus'
        polarbear.image = 'BS'
        polarbear.life = '15 to 18 Years'
        polarbear.habitat = 'The entire Arctic Region'
        polarbear.location = 'BS'

        #Create Array to Store Animals
        Animals = [redfox, polarbear, arcticwolf]




class Page(object):
    def __init__(self):
        self.open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>What Does the Fox Say?</title>
    </head>
<body>'''

        self.nav = '''
<ul>
    <a href="?animals=redfox"><li>Red Fox</li></a>
    <a href="?animals=arcticwolf"><li>Arctic Wolf</li></a>
    <a href="?animals=polarbear"><li>Polar Bear</li></a>
</ul>'''

        self.content = '''
        Fuck this
        '''

        self.close = '''
</body>
</html>'''
        self.all = self.open + self.nav + self.content + self.close

    def update(self):
        self.all = self.all.format(**locals())
        return self.all


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

class RedFox(AbstractAnimal):
    def __init__(self):
        super(RedFox, self).__init__()

class ArcticWolf(AbstractAnimal):
    def __init__(self):
        super(ArcticWolf, self).__init__()

class PolarBear(AbstractAnimal):
    def __init__(self):
        super(PolarBear, self).__init__()

app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
