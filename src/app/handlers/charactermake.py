from os.path import dirname, join

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db
from app.models.characterSheet import CharacterSheet

class CharacterMake(webapp.RequestHandler):
    page_templates = [
        "charactermake_top.html",
        "charactermake_skill.html",
        "charactermake_personal.html",
        "charactermake_confirm.html"
    ]
    
    def get(self):
        sheet = CharacterSheet()
        sheet.put()
        
        self.show_page(0, sheet)

    def post(self):
        page = int(self.request.get('page'))
        to = int(self.request.get('to'))
        key = self.request.get('key')
        sheet = CharacterSheet.get(db.Key(key))

        #ここにシート更新処理を書く      
        for arg in self.request.arguments():
            val = self.request.get(arg)
            sheet.set_by_string(arg, val)
            
        sheet.put()
        
        self.show_page(to, sheet)

    def show_page(self, page, sheet):
        name = sheet.get_by_string("name")
        
        template_values = {
            "page": page,
            "next": page+1,
            "back": page-1,
            "sheet": sheet,
        }
        path = join(dirname(dirname(dirname(__file__))), 'template', self.page_templates[page])
        self.response.out.write(template.render(path,template_values))