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

#可変個スキル表示
def showVariableSkill (value,count):
	if count%2 == 0:
		return u"<tr><td>知識：" + value + u"</td>"
	else:
		return u"<td>" + value + u"</td></tr>"


register.filter(convertOri2Sta)
register.filter(calcDemonicSta)
register.filter(checkHavingItem)
register.filter(showVariableSkill)
