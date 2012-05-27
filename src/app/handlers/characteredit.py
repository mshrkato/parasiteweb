from os.path import dirname, join

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users

from app.models.characterSheet import CharacterSheet

class CharacterEdit(webapp.RequestHandler):
    def get(self):
        template_values = {
            "powOriginal": 6,
        }
        path = join(dirname(dirname(dirname(__file__))), 'template', 'characteredit.html')
        self.response.out.write(template.render(path,template_values))