#Daniel O'Carroll
#Assignment
#Date
#

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        home_page = Page()
        home_page.title = "Home Page"
        home_page.update()

        contact_page = Page()
        contact_page.title = "Contact Us"
        contact_page.update()

        self.response.write(contact_page.print_out())


class Page(object):
    def __init__(self):
        self.__title = "Welcome to Page"
        self.__open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
    </head>
<body>'''
        self.__content = "Welcome!"
        self.__close = '''
</body>
</html>'''
        self.__all = self.__open + self.__content + self.__close

    @property
    def title(self): #GETTER
        return self.__title
    @title.setter
    def title(self, new_title): #SETTER
        self.__title = new_title
        self.update()

    def print_out(self):
        return self.__all

    def update(self):
        ##replaces all the { } with the values of the corresponding variables
        self.__all = self.__all.format(**locals())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
