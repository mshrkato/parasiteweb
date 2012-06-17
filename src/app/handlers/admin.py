from os.path import dirname, join

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db
from app.models.parasiteData import parasiteData

class registClass(webapp.RequestHandler):
    def get(self):
        self.show_page({})


    def post(self):
        rewrite = {}
        if self.request.get('load') != "":
            q = parasiteData.get(db.Key(self.request.get('load')))
            rewrite = {
                "parasiteNumber": q.parasiteNumber,
                "parasiteName": q.parasiteName,
                "parasiteClassName": q.parasiteClassName,

                "powOffset": q.powOffset,
                "agiOffset": q.agiOffset,
                "senOffset": q.senOffset,
                "lucOffset": q.lucOffset,
                "intOffset": q.intOffset,
                "mntOffset": q.mntOffset,
                
                "physAtk": q.physAtk,
                "physDef": q.physDef,
                "shotAtk": q.shotAtk,
                "shotDef": q.shotDef,
                "specAtk": q.specAtk,
                "specDef": q.specDef,

                "actOffset": q.actOffset,
                "eneOffset": q.eneOffset,
                
                "highClassA": q.highClassA,
                "highClassB": q.highClassB
            }
        elif self.request.get('delete') != "":
            q = parasiteData.get(db.Key(self.request.get('delete')))
            q.delete()
        else:
            parasite = {}
            #既にあれば読み込み
            q = parasiteData.all()
            q.filter("parasiteClassName =", self.request.get('parasiteClassName'))
            parasite = q.fetch(1)
            
            if len(parasite) == 0:
                parasite = parasiteData()
            else:
   	            parasite = parasite[0]

            #parasite = parasiteData.get_or_insert('parasiteNumber',self.request.get('parasiteName'))
            
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
            parasite.physAtk = int(self.request.get('physAtk'))
            parasite.physDef = int(self.request.get('physDef'))
            parasite.shotAtk = int(self.request.get('shotAtk'))
            parasite.shotDef = int(self.request.get('shotDef'))
            parasite.specAtk = int(self.request.get('specAtk'))
            parasite.specDef = int(self.request.get('specDef'))
            
            #other
            parasite.actOffset = int(self.request.get('actOffset'))
            parasite.eneOffset = int(self.request.get('eneOffset'))
            
            #highClass
            parasite.highClassA = self.request.get('highClassA')
            parasite.highClassB = self.request.get('highClassB')
            
            parasite.put()

        self.show_page(rewrite)

    def show_page(self, rewrite):
        #登録済み寄生体を取得
        q = parasiteData.all()
        q.order("parasiteNumber")
        classes = q.fetch(200)

        #渡して表示
        template_values = {
            "classes": classes,
            "rewrite": rewrite,
        }
        path = join(dirname(dirname(dirname(__file__))), 'template', 'admin_registrationClass.html')
        self.response.out.write(template.render(path,template_values))
