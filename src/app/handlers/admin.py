from os.path import dirname, join

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db
from app.models.parasiteData import parasiteData

class registClass(webapp.RequestHandler):
    def get(self):
        self.show_page()


    def post(self):
        if self.request.get('edit'):
        	a = 1    
        elif self.request.git('delete'):
            b = 2
        else:
            #登録or削除
            parasite = parasiteData()
            
            #No
            parasite.parasiteNumber = int(self.request.get('parasiteNumber'))
            parasite.parasiteName = self.request.get('parasiteName')
            parasite.parasiteClassName = self.request.get('parasiteClassName')

            #status
            parasite.powOffset = int(self.request.get('powOffset'))
            parasite.agiOffset = int(self.request.get('agiOffset'))
            parasite.senOffset = int(self.request.get('senOffset'))
            parasite.lucOffset = int(self.request.get('lucOffset'))
            parasite.intOffset = int(self.request.get('intOffset'))
            parasite.mntOffset = int(self.request.get('mntOffset'))
            
            #battle
            parasite.punchAttack = int(self.request.get('punchAttack'))
            parasite.punchDeffence = int(self.request.get('punchDeffence'))
            parasite.shotAttack = int(self.request.get('shotAttack'))
            parasite.shotDeffence = int(self.request.get('shotDeffence'))
            parasite.specialAttack = int(self.request.get('specialAttack'))
            parasite.specialDeffence = int(self.request.get('specialDeffence'))
            
            #other
            parasite.actionOffset = int(self.request.get('actionOffset'))
            parasite.energyOffset = int(self.request.get('energy'))
            
            #highClass
            highClassA = int(self.request.get('highClassA'))
            highClassB = int(self.request.get('highClassB'))
            
            parasite.put()

        self.show_page()
        
    def show_page(self):
        #登録済み寄生体を取得
        q = parasiteData.all()
        q.order("-parasiteNumber")
        classes = q.fetch(200)

        #渡して表示
        template_values = {
            "classes": classes,
        }
        path = join(dirname(dirname(dirname(__file__))), 'template', 'admin_registrationClass.html')
        self.response.out.write(template.render(path,template_values))
