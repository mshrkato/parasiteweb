from os.path import dirname, join

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users

from app.models.characterSheet import CharacterSheet

class CharacterEdit(webapp.RequestHandler):
    def get(self):
        template_values = {
        	"sheet": {
                "name": 'test',
                "age": 25,
                "sex": 'unknown',
                "species": 'human',
                "parasite": 'javelin',
                
                "powOriginal": 2,
                "agiOriginal": 3,
                "senOriginal": 4,
                "lucOriginal": 6,
                "intOriginal": 7,
                "mntOriginal": 9,

                "bodySkill": 0,
                "powSkill": 5,
                "climeSkill": 10,
                "swimSkill": 15,

                "shotSkill": 0,
                "comunicationSkill": 5,
                "noticeSkill": 10,
                
                "specialSkill": 0,
                "treatSkill": 5,
                "itSkill": 10,
                
                "exerciseSkill": 5,
                "hideSkill": 10,
                "driveSkill": 15,
                "controlSkill": 0,
                
				"intuitionSkill": 0,
				"gambleSkill": 5,
				"negotiateSkill": 10,
				"sociabilitySkill": 10,
				
				"jentleSkill": 5,
				"leadingSkill": 10,
				"questionSkill": 15,
				"charmSkill": 5,
				
				"dustlicence": 1,
				"dustcoat": 0,
				"dustSeal": 1,
				"dustAwake": 0,
				
				"resident": 0,
				"car": 1,
				"bike": 0,
				"minibike": 1,
				"byecycle": 1,
				"mobile": 1,
				"bag": 0,
				"pickingtool": 1,
				"itembox": "aaabbb",
				
				"experiencePoint": 2000,
				
				"evolutionRouteMain": ["second","first"],
				"evolutionRouteSub": []
        	},
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
        path = join(dirname(dirname(dirname(__file__))), 'template', 'characteredit.html')
        self.response.out.write(template.render(path,template_values))