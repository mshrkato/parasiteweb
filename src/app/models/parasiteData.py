from google.appengine.ext import db

class parasiteData(db.Model):
	#name
	parasiteNumber = db.IntegerProperty()

	#name
	parasiteName = db.StringProperty()
	#className
	parasiteClassName = db.StringProperty()
	
	#unableSpiecies
	human = db.BooleanProperty()
	animal = db.BooleanProperty()
	
	#statusOffset
	powOffset = db.IntegerProperty()
	agiOffset = db.IntegerProperty()
	senOffset = db.IntegerProperty()
	lucOffset = db.IntegerProperty()
	intOffset = db.IntegerProperty()
	mntOffset = db.IntegerProperty()
	
	#battleOffset
	physAtk = db.IntegerProperty()
	physDef = db.IntegerProperty()
	shotAtk = db.IntegerProperty()
	shotDef = db.IntegerProperty()
	specAtk = db.IntegerProperty()
	specDef = db.IntegerProperty()
	
	#actionOffset
	actOffset = db.IntegerProperty()
	
	#energy
	eneOffset = db.IntegerProperty()
	
	#highClass
	highClassA = db.StringProperty()
	highClassB = db.StringProperty()
	
	def get_by_string(self, name):
		return self.__dict__['_' + name]
	
	def set_by_string(self, name, value):
		property = self.__dict__['_' + name]
		
		if (type(property) ==  db.IntegerProperty):
			property = int(value)
		else:
			property = value
