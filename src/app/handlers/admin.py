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
    	#登録or削除
        parasite = parasiteData()
        parasite.parasiteName = self.request.get('parasiteName')
        parasite.parasiteClassName = self.request.get('parasiteClassName')
        parasite.powOffset = int(self.request.get('powOffset'))
        parasite.agiOffset = int(self.request.get('agiOffset'))
        parasite.senOffset = int(self.request.get('senOffset'))
        parasite.lucOffset = int(self.request.get('lucOffset'))
        parasite.intOffset = int(self.request.get('intOffset'))
        parasite.mntOffset = int(self.request.get('mntOffset'))
        parasite.put()

        self.show_page()
        
    def show_page(self):
    	#登録済み寄生体を取得
		q = parasiteData.all()
		classes = q.fetch(10)

		#渡して表示
		template_values = {
			"classes": classes,
		}
		path = join(dirname(dirname(dirname(__file__))), 'template', 'admin_registrationClass.html')
		self.response.out.write(template.render(path,template_values))
