from google.appengine.ext import db

class CharaSheet(db.Model):
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
	fealOriginal = db.IntegerProperty()
	lucOriginal = db.IntegerProperty()
	intOriginal = db.IntegerProperty()
	mentOriginal = db.IntegerProperty()

	#powSkill
	PunchSkill = db.IntegerProperty()
	powSkill = db.IntegerProperty()
	swimSkill =  db.IntegerProperty()
	climeSkill = db.IntegerProperty()

	#speedSkill
	exerSkill = db.IntegerProperty()
	hideSkill = db.IntegerProperty()
	driveSkill = db.IntegerProperty()
	controlSkill = db.IntegerProperty()

	#shotSkill
	shotSkill = db.IntegerProperty()
	comuSkill = db.IntegerProperty()
	noticeSkill = db.IntegerProperty()
	artSkill = db.StringProperty(multiline=True)

	#luckSkill
	IntuitionSkill = db.IntegerProperty()
	GambleSkill = db.IntegerProperty()
	NegotiateSkill = db.IntegerProperty()
	SociabilitySkill = db.IntegerProperty()

	#IntelligenceSkill
	SpecialSkill = db.IntegerProperty()
	TreatSkill = db.IntegerProperty()
	ItSkill = db.IntegerProperty()
	knowledgeSkill = db.StringProperty(multiline=True)

	#mindSkill
	JentleSkill = db.IntegerProperty()
	LeadingSkill = db.IntegerProperty()
	QuestionSkill = db.IntegerProperty()
	CharmSkill = db.IntegerProperty()
	
	#personality
	Birth = db.StringProperty()
	Experience = db.StringProperty()
	CauseOfParasite = db.StringProperty()
	Feature = db.StringProperty()
	Feeling = db.StringProperty()
	Purpose = db.StringProperty()
	Appearance = db.StringProperty()
	Stance = db.StringProperty()
	Organization = db.StringProperty()

	#item
	items = db.StringProperty(multiline=True)
