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
        arguments = self.request.arguments()
        
        to = int(self.request.get('to'))
        arguments.remove('to')        
        key = self.request.get('key')
        arguments.remove('key')
        
        sheet = CharacterSheet.get(db.Key(key))

        for arg in arguments:
            vals = self.request.get_all(arg)
            if len(vals) == 1:
                sheet.set_by_string(arg, vals[0])
            else:
                sheet.set_by_string(arg, vals)
        
        sheet.put()
        
        self.show_page(to, sheet)

    def show_page(self, page, sheet):
        template_values = {
            "page": page,
            "next": page+1,
            "back": page-1,
            "sheet": sheet,
            "demonic": {
                "action": 10,
                "energy": 20,
                "level": 1,
                "powOffset": 0,
                "agiOffset": 1,
                "senOffset": 2,
                "lucOffset": 3,
                "intOffset": 4,
                "mntOffset": 5,
                "highClasses":[{"name":"class1"}, {"name":"class2"}, {"name":"class3"}],
                "subClasses":[{"name":"class1"}, {"name":"class2"}, {"name":"class3"}]
            }
        }
        path = join(dirname(dirname(dirname(__file__))), 'template', self.page_templates[page])
        self.response.out.write(template.render(path,template_values))
