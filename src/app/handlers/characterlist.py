from os.path import dirname, join

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users

from app.models.characterSheet import CharacterSheet

class CharacterList(webapp.RequestHandler):
    def get(self):
        q = CharacterSheet.all()
        characters = q.fetch(10)
        
        template_values = {
            "characters": characters,
        }
        
        path = join(dirname(dirname(dirname(__file__))), 'template', 'characterlist.html')
#        self.response.out.write(template.render(path,0))
        self.response.out.write(template.render(path,template_values))

    def post(self):
        if self.request.get('delete') != "":
            q = CharacterSheet.get(db.Key(self.request.get('delete')))
            q.delete()
    
        q = CharacterSheet.all()
        characters = q.fetch(10)
        characters[0].name = self.request.get('delete')
        
        template_values = {
            "characters": characters,
        }
        
        path = join(dirname(dirname(dirname(__file__))), 'template', 'characterlist.html')
#        self.response.out.write(template.render(path,0))
        self.response.out.write(template.render(path,template_values))
