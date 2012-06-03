from google.appengine.ext import db

class parasiteData(db.Model):
	#name
	parasiteName = db.StringProperty()
	#className
	parasiteClassName = db.StringProperty()
	
	#statusOffset
	powOffset = db.IntegerProperty()
	agiOffset = db.IntegerProperty()
	senOffset = db.IntegerProperty()
	lucOffset = db.IntegerProperty()
	intOffset = db.IntegerProperty()
	mntOffset = db.IntegerProperty()
	
	#battleOffset
	
	#highClass
	highClasses_Upper = db.StringProperty()
	highClasses_Down = db.StringProperty()
	
	def get_by_string(self, name):
		return self.__dict__['_' + name]
	
	def set_by_string(self, name, value):
		property = self.__dict__['_' + name]
		
		if (type(property) ==  db.IntegerProperty):
			property = int(value)
		else:
			property = value
