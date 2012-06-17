# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
register = webapp.template.create_template_register()

# 元値から能力値を計算
def convertOri2Sta (value):
  return value/3

# 元値と悪魔化補正から能力値を計算
def calcDemonicSta (value, correct):
  return value/3 + correct
  
#アイテム所持
def checkHavingItem (value):
	if value == True:
		return "checked='checked'"
	else:
		return ""

#skillLv
def transSkillLvToJa (value):
	if value == 0:
		return u"--"
	elif value == 5:
		return u"初級"
	elif value == 10:
		return u"中級"
	elif value == 15:
		return u"上級"
	else:
		return u"error"

#可変個スキル表示
def showArtSkill (value,count):
	if count%2 == 0:
		return u"<tr><td>芸術：" + value + u"</td>"
	else:
		value = transSkillLvToJa(value)
		return u"<td>" + value + u"</td></tr>"

def showKnwSkill (value,count):
	if count%2 == 0:
		return u"<tr><td>知識：" + value + u"</td>"
	else:
		value = transSkillLvToJa(value)
		return u"<td>" + value + u"</td></tr>"


register.filter(convertOri2Sta)
register.filter(calcDemonicSta)
register.filter(transSkillLvToJa)
register.filter(showArtSkill)
register.filter(showKnwSkill)
register.filter(checkHavingItem)
