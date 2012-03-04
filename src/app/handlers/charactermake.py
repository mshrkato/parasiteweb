from os.path import dirname, join

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users

class CharacterMake(webapp.RequestHandler):
    def get(self):
        path = join(dirname(dirname(dirname(__file__))), 'template', 'charactermake.html')
        self.response.out.write(template.render(path,0))