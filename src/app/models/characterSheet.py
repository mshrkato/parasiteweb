from google.appengine.ext import db

class CharacterSheet(db.Model):
	#user
	user = db.UserProperty()
	
	#experiencePoint
	experiencePoint = db.IntegerProperty()
	
	#chara
	name = db.StringProperty(default="Undefined")
	age = db.IntegerProperty(default=-1)
	sex = db.StringProperty(default="Undefined")
	species = db.StringProperty(default="Undefined")
	parasite = db.StringProperty(default="Undefined")
	job = db.StringProperty(default="Undefined")

	#Original
	powOriginal = db.IntegerProperty(default=-1)
	agiOriginal = db.IntegerProperty(default=-1)
	senOriginal = db.IntegerProperty(default=-1)
	lucOriginal = db.IntegerProperty(default=-1)
	intOriginal = db.IntegerProperty(default=-1)
	mntOriginal = db.IntegerProperty(default=-1)

	#powSkill
	bodySkill = db.IntegerProperty(default=-1)
	powSkill = db.IntegerProperty(default=-1)
	climeSkill = db.IntegerProperty(default=-1)
	swimSkill =  db.IntegerProperty(default=-1)

	#speedSkill
	exerciseSkill = db.IntegerProperty(default=-1)
	hideSkill = db.IntegerProperty(default=-1)
	driveSkill = db.IntegerProperty(default=-1)
	controlSkill = db.IntegerProperty(default=-1)

	#shotSkill
	shotSkill = db.IntegerProperty(default=-1)
	comunicationSkill = db.IntegerProperty(default=-1)
	noticeSkill = db.IntegerProperty(default=-1)
	artSkills = db.StringListProperty(default={})

	#luckSkill
	intuitionSkill = db.IntegerProperty(default=-1)
	gambleSkill = db.IntegerProperty(default=-1)
	negotiateSkill = db.IntegerProperty(default=-1)
	sociabilitySkill = db.IntegerProperty(default=-1)

	#IntelligenceSkill
	specialSkill = db.IntegerProperty(default=-1)
	treatSkill = db.IntegerProperty(default=-1)
	itSkill = db.IntegerProperty(default=-1)
	knowledgeSkills = db.StringListProperty(default={})

	#mindSkill
	jentleSkill = db.IntegerProperty(default=-1)
	leadingSkill = db.IntegerProperty(default=-1)
	questionSkill = db.IntegerProperty(default=-1)
	charmSkill = db.IntegerProperty(default=-1)
	
	#personality
	birth = db.StringProperty(default="Undefined")
	experience = db.StringProperty(default="Undefined")
	causeOfParasite = db.StringProperty(default="Undefined")
	feature = db.StringProperty(default="Undefined")
	feeling = db.StringProperty(default="Undefined")
	purpose = db.StringProperty(default="Undefined")
	appearance = db.StringProperty(default="Undefined")
	stance = db.StringProperty(default="Undefined")
	organization = db.StringProperty(default="Undefined")
	
	#items
	dustlicence = db.BooleanProperty(default=False)
	dustcoat = db.BooleanProperty(default=False)
	dustSeal = db.BooleanProperty(default=False)
	dustAwake = db.BooleanProperty(default=False)
	resident = db.BooleanProperty(default=False)
	car = db.BooleanProperty(default=False)
	bike = db.BooleanProperty(default=False)
	minibike = db.BooleanProperty(default=False)
	byecycle = db.BooleanProperty(default=False)
	mobile = db.BooleanProperty(default=False)
	bag = db.BooleanProperty(default=False)
	pickingtool = db.BooleanProperty(default=False)
	itembox = db.StringProperty(default="Undefined", multiline=True)
	
	def get_by_string(self, name):	
		return self.__dict__['_' + name]
	
	def set_by_string(self, name, value):
		if (self.__dict__['_' + name].__class__ == unicode):
			self.__dict__['_' + name] = value
		elif (self.__dict__['_' + name].__class__ == long):
			self.__dict__['_' + name] = int(value)
		elif (self.__dict__['_' + name].__class__ == bool):
			self.__dict__['_' + name] = value == "True"
		elif (self.__dict__['_' + name].__class__ == list):
			tmp = []
			flag = False
			for v in value:
				if v == '':
					flag = True
				elif flag:
					flag = False
				else:
					tmp.append(v)
					
			self.__dict__['_' + name] = tmp
