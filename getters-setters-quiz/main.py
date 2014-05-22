#Daniel O'Carroll
#May 21st, 2014
#DPW1405

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):


#create a page class
class Page(object):
    def __init__(self):
        self.counter = Counter()
        self._open = '''
<!DOCTYPE html>
<head>
<title>Counter</title>
</head>
<body>
        '''
        self._content = ''
        self._close = '''
</body>
</html>
        '''
        self.all = self._open + self._content + self._close

    def print_out(self):
        self.all = self.all.format(**locals())
        return self.all

#Create counter class
class Counter(object):
    def __init__(self):
        self.__counter = 0

        self.__button = '''
        <br />
        <a href="count={self.counter}">Count Up</a>
        '''

    def update(self):
        self.button.format(**locals())
        self.counter += 1
        return self.button

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
