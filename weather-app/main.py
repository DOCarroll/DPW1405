#Daniel O'Carroll
#DPW1405
#May 19th, 2014

import webapp2
from page import FormPage, Page
from xml.dom import minidom #library for working with xml in python
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()
        view._form_header = "Yahoo's Weather App"
        self.response.write(view.print_out())

        if self.request.GET:
            code = self.request.GET['code']
            url = 'http://xml.weather.yahoo.com/forecastrss?p=' + code
        #go get the api info
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            data = opener.open(req)
        #parse
            xmldoc = minidom.parse(data)
        #look at elements inside xml
            self.response.write(xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)
            list = xmldoc.getElementsByTagName('yweather:forecast')
            content = '<br/>'
            for item in list:
                content += item.attributes['day'].value + '<br/>'
                content += "High: " + item.attributes['high'].value + ' | Low: ' + item.attributes['low'].value + ' | Conditions: ' + item.attributes['text'].value + '<br/>'
            self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
