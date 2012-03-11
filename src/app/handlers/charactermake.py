from os.path import dirname, join

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from app.models.characterSheet import CharaSheet

class CharacterMake(webapp.RequestHandler):
    def get(self):
        path = join(dirname(dirname(dirname(__file__))), 'template', 'charactermake.html')
        self.response.out.write(template.render(path,0))

    def post(self):
        self.response.out.write('posted:' + self.request.get('selectExerciseSkill'))

        sheet = CharaSheet()
        
        #chara
        sheet.name = self.request.get('inputCharaName')
        sheet.age = int(self.request.get('inputCharaAge'))
        sheet.sex = int(self.request.get('optionsCharaSex'))
        sheet.species = self.request.get('selectspecies')
        sheet.parasite = self.request.get('selectParasite')
        sheet.job = self.request.get('selectJob')

        #Original
        sheet.powOriginal =int(self.request.get('selectpow'))
        sheet.agiOriginal = int(self.request.get('selectagi'))
        sheet.fealOriginal = int(self.request.get('selectfeal'))
        sheet.lucOriginal = int(self.request.get('selectluc'))
        sheet.intOriginal = int(self.request.get('selectint'))
        sheet.mentOriginal = int(self.request.get('selectment'))
        
        #bodyskill
        sheet.PunchSkill = int(self.request.get('selectPunchSkill'))
        sheet.powSkill = int(self.request.get('selectPowerSkill'))
        sheet.swimSkill =  int(self.request.get('selectSwimSkill'))
        sheet.climeSkill = int(self.request.get('selectClimeSkill'))
        
        #speedSkill
        sheet.exerSkill = int(self.request.get('selectExerciseSkill'))
        sheet.hideSkill = int(self.request.get('selectHideSkill'))
        sheet.driveSkill = int(self.request.get('selectDriveSkill'))
        sheet.controlSkill =  int(self.request.get('selectOperateSkill'))
        
        #shotSkill
        sheet.shotSkill = int(self.request.get('selectShotSkill'))
        sheet.comuSkill = int(self.request.get('selectComunicationSkill'))
        sheet.noticeSkill = int(self.request.get('selectNoticeSkill'))
        sheet.artSkill = 'test'
        
        #luckSkill
        sheet.IntuitionSkill = int(self.request.get('selectIntuitionSkill'))
        sheet.GambleSkill = int(self.request.get('selectGambleSkill'))
        sheet.NegotiateSkill = int(self.request.get('selectNegotiateSkill'))
        sheet.SociabilitySkill = int(self.request.get('selectNegotiateSkill'))
        
        #IntelligenceSkill
        sheet.SpecialSkill = int(self.request.get('selectSpecialSkill'))
        sheet.TreatSkill = int(self.request.get('selectTreatSkill'))
        sheet.ItSkill = int(self.request.get('selectITSkill'))
        sheet.knowledgeSkill = 'test'
        
        #mindSkill
        sheet.JentleSkill = int(self.request.get('selectJentleSkill'))
        sheet.LeadingSkill = int(self.request.get('selectLeadingSkill'))
        sheet.QuestionSkill = int(self.request.get('selectQuestionSkill'))
        sheet.CharmSkill = int(self.request.get('selectCharmSkill'))
        
        #personality
        sheet.Birth = self.request.get('inputBirth')
        sheet.Experience = self.request.get('inputExperience')
        sheet.CauseOfParasite = self.request.get('inputCauseOfParasite')
        sheet.Feature = self.request.get('inputFeature')
        sheet.Feeling = self.request.get('inputFeeling')
        sheet.Purpose = self.request.get('inputPurpose')
        sheet.Appearance = self.request.get('inputAppearance')
        sheet.Stance = self.request.get('selectStance')
        sheet.Organization = self.request.get('selectOrganization')
        sheet.items = self.request.get('selectJentleSkill')
        
        #save
        sheet.put()
        
        #redirect
        self.redirect('/')