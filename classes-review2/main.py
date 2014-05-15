#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        yoda = Character()
        yoda.name = "Yoda"
        yoda.age = 1900
        yoda.gender = "Male"
        yoda.occupation = "Jedi Master"
        yoda.print_info()
        #instance.attribute
        #instance.method
        #instance.property

        luke = Character()
        luke.name = "Luke Skywalker"
        luke.gender = "Male"
        luke.age = 24
        luke.occupation = "Jedi Knight"
        luke.print_info()

        leia = Character()
        leia.name = "Leia Organa"
        leia.gender = "Female"
        leia.occupation = "Princess"
        leia.age = luke.age
        leia.squad_no = "Pink 5"
        print leia.squad_no

class Character(object):
    def __init__(self): #constructor function
        self.name = ""
        self.__age = 0
        self.occupation = ""
        self.gender = ""
        self.__rogue_squadron_no = "DEFAULT"
    def print_info(self):
        print self.name + " is a(n) " + self.occupation


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        #VALIDATION
        if new_age < 0 or new_age > 1000:
            print "Error with age input!!!!!!"
        else:
            self.__age = new_age

    #PROVIDES READ ACCESS
    @property
    def squad_no(self):
        return self.__rogue_squadron_no
    #PROVIDES WRITE ACCESS
    @squad_no.setter
    def squad_no(self, new_no):
        self.__rogue_squadron_no = new_no

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)