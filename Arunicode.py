# coding: utf8
from __future__ import unicode_literals

abjad = { u"\u0621":"'",	#   Hamza
        u"\u0623":">",	#   Alif + HamzaAbove
		u"\u0624":"&",	#   Waw + HamzaAbove
		u"\u0625":"<",	#   Alif + HamzaBelow
		u"\u0626":"}",	#   Ya + HamzaAbove
		u"\u0627":"A",	#   Alif
		u"\u0628":"b",	#   Ba
		u"\u0629":"p",	#   TaMarbuta
		u"\u062A":"t",	#   Ta
		u"\u062B":"v",	#   Tha
		u"\u062C":"j",	#   Jeem
		u"\u062D":"H",	#   HHa
		u"\u062E":"x",	#   Kha
		u"\u062F":"d",	#   Dal
		u"\u0630":"*",	#   Thal
		u"\u0631":"r",	#   Ra
		u"\u0632":"z",	#   Zain
		u"\u0633":"s",	#   Seen
		u"\u0634":"$",	#   Sheen
		u"\u0635":"S",	#   Sad
		u"\u0636":"D",	#   DDad
		u"\u0637":"T",	#   TTa
		u"\u0638":"Z",	#   DTha
		u"\u0639":"E",	#   Ain
		u"\u063A":"g",	#   Ghain
		u"\u0640":"_",	#   Tatweel
		u"\u0641":"f",	#   Fa
		u"\u0642":"q",	#   Qaf
		u"\u0643":"k",	#   Kaf
		u"\u0644":"l",	#   Lam
		u"\u0645":"m",	#   Meem
		u"\u0646":"n",	#   Noon
		u"\u0647":"h",	#   Ha
		u"\u0648":"w",	#   Waw
		u"\u0649":"Y",	#   AlifMaksura
		u"\u064A":"y",	#   Ya
		u"\u064B":"F",	#   Fathatan
		u"\u064C":"N",	#   Dammatan
		u"\u064D":"K",	#   Kasratan
		u"\u064E":"a",	#   Fatha
		u"\u064F":"u",	#   Damma
		u"\u0650":"i",	#   Kasra
		u"\u0651":"~",	#   Shadda
		u"\u0652":"o",	#   Sukun
		u"\u0653":"^",	#   Maddah
		u"\u0654":"#",	#   HamzaAbove
		u"\u0670":"`",	#   AlifKhanjareeya
		u"\u0671":"{",	#   Alif + HamzatWasl
		u"\u06DC":":",	#   SmallHighSeen
		u"\u06DF":"@",	#   SmallHighRoundedZero
		u"\u06E0":'"',	#   SmallHighUprightRectangularZero
		u"\u06E2":"[",	#   SmallHighMeemIsolatedForm
		u"\u06E3":";",	#   SmallLowSeen
		u"\u06E5":",",	#   SmallWaw
		u"\u06E6":".",	#   SmallYa
		u"\u06E8":"!",	#   SmallHighNoon
		u"\u06EA":"-",	#   EmptyCentreLowStop
		u"\u06EB":"+",	#   EmptyCentreHighStop
		u"\u06EC":"%",	#   RoundedHighStopWithFilledCentre
		u"\u06ED":"]"}	#   SmallLowMeem

alphabet = {}
for key in abjad:
    alphabet[abjad[key]] = key