# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
register = webapp.template.create_template_register()

# 元値から能力値を計算
def convertOri2Sta (value):
  return value/3

# 元値と悪魔化補正から能力値を計算
def calcDemonicSta (value, correct):
  return value/3 + correct

register.filter(convertOri2Sta)
register.filter(calcDemonicSta)
