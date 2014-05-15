#Daniel O'Carroll
#DPW1405
#05/14/14
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
       p = FormPage()
       p.title = "Welcome to All"
       p.css_url = "css/styles.css"
       self.response.write(p.print_out())


class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" type="text/css" href="{self.css_url}" />
    </head>
<body>'''
        self._content = "This is my content"
        self._close = '''
</body>
</html>'''
        self._css_url = ''
        self._title = ''
        self.all = ''
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

    @property
    def css_url(self):
        return self._css_url

    @css_url.setter
    def css_url(self, c):
        self._css_url = c

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())

class FormPage(Page):
    def __init__(self):
        #call the super
        Page.__init__(self)
        #super(FormPage, self).__init__()
        self.__form_open = '<form method="GET" action="">'
        self.__inputs = '''
        <input type="text" placeholder="First Name" name="l_name" />
        <input type="text" placeholder="Last Name" name="f_name" />
        <input type="submit" name="submit" />'''
        self.__form_close = '</form>'
        self._form_header = ">>Form Header<<"
        self._content = self.__form_open + self._form_header + self.__inputs + self.__form_close

    def update(self):
        self.all = self._open + self._form_header + self.__form_open + self.__inputs + self.__form_close + self._close
        self.all = self.all.format(**locals())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
