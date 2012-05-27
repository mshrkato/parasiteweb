from google.appengine.ext import db

class parasiteData(db.Model):
	#name
	name = db.StringProperty()
	
	#statusOffset
	powOffset = db.IntegerProperty()
	agiOffset = db.IntegerProperty()
    senOffset = db.IntegerProperty()
    lucOffset = db.IntegerProperty()
    intOffset = db.IntegerProperty()
    mntOffset = db.IntegerProperty()
    
    #battleOffset
    
    #highClass
    highClasses_A = db.StringProperty()
    highClasses_B = db.StringProperty()