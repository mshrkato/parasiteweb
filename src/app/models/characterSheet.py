from google.appengine.ext import db

class CharacterSheet(db.Model):
	#user
	user = db.UserProperty()
	
	#chara
	name = db.StringProperty()
	age = db.IntegerProperty()
	sex = db.StringProperty()
	species = db.StringProperty()
	parasite = db.StringProperty()
	job = db.StringProperty()

	#Original
	powOriginal = db.IntegerProperty()
	agiOriginal = db.IntegerProperty()
	senOriginal = db.IntegerProperty()
	lucOriginal = db.IntegerProperty()
	intOriginal = db.IntegerProperty()
	mntOriginal = db.IntegerProperty()

	#powSkill
	bodySkill = db.IntegerProperty()
	powSkill = db.IntegerProperty()
	climeSkill = db.IntegerProperty()
	swimSkill =  db.IntegerProperty()

	#speedSkill
	exerciseSkill = db.IntegerProperty()
	hideSkill = db.IntegerProperty()
	driveSkill = db.IntegerProperty()
	controlSkill = db.IntegerProperty()

	#shotSkill
	shotSkill = db.IntegerProperty()
	comunicationSkill = db.IntegerProperty()
	noticeSkill = db.IntegerProperty()
	artSkill = db.StringProperty(multiline=True)

	#luckSkill
	intuitionSkill = db.IntegerProperty()
	gambleSkill = db.IntegerProperty()
	negotiateSkill = db.IntegerProperty()
	sociabilitySkill = db.IntegerProperty()

	#IntelligenceSkill
	specialSkill = db.IntegerProperty()
	treatSkill = db.IntegerProperty()
	itSkill = db.IntegerProperty()
	knowledgeSkill = db.StringProperty(multiline=True)

	#mindSkill
	jentleSkill = db.IntegerProperty()
	leadingSkill = db.IntegerProperty()
	questionSkill = db.IntegerProperty()
	charmSkill = db.IntegerProperty()
	
	#personality
	birth = db.StringProperty()
	experience = db.StringProperty()
	causeOfParasite = db.StringProperty()
	feature = db.StringProperty()
	feeling = db.StringProperty()
	purpose = db.StringProperty()
	appearance = db.StringProperty()
	stance = db.StringProperty()
	organization = db.StringProperty()
	
	#items
	items = db.StringProperty(multiline=True)
	
	def get_by_string(self, name):
		return self.__dict__['_' + name]
	
	def set_by_string(self, name, value):
		self.__dict__['_' + name] = value
		
		#/this_module = __import__("__main__")
		#this_class = getattr(this_module, CharacterSheet)
		#return getattr(this_class, name)
