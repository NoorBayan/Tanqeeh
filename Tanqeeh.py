# coding: utf8
from __future__ import unicode_literals
import os
import re
import pyarabic.araby as araby

class Tanqeeh:
    def __init__(self, stopwords=None):
        """
        Initializes the ArabicTextCleaner with optional stopwords.
        """
        self.stopwords = stopwords if stopwords else {"في", "من", "إلى", "على", "عن", "هذا", "ذلك", "تلك", "كما", "لكن"}
        self.num_dict = {'0': 'صفر', '1': 'واحد', '2': 'اثنان', '3': 'ثلاثة', '4': 'أربعة',
                         '5': 'خمسة', '6': 'ستة', '7': 'سبعة', '8': 'ثمانية', '9': 'تسعة'}

    def remove_tatweel(self, text):
        return text.replace("ـ", "")

    def normalize_persian_urdu(self, text):
        replacements = {"ک": "ك", "ی": "ي", "ٱ": "ا", "ە": "ه", "چ": "ج", "ڤ": "ف",
                        "پ": "ب", "گ": "ق", "ژ": "ز", "ں": "ن", "ھ": "ه", "ۀ": "ه"}
        return text.translate(str.maketrans(replacements))

    def clean_arabic_text(self, text):
        return re.sub(r'[^\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\s]', '', text)

    def remove_isolated_letters(self, text):
        return re.sub(r'\b[\u0600-\u06FF]\b', '', text)

    def remove_extra_spaces(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def trim_text(self, text):
        return text.strip()

    def remove_incorrect_diacritics(self, text):
        valid_diacritics = "\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652"
        invalid_combinations = re.compile(f'([\u0600-\u06FF])([{valid_diacritics}]{{3,}})')
        text = invalid_combinations.sub(r'\1', text)
        return re.sub(f'([\u0600-\u06FF])\u0652[{valid_diacritics.replace("\u0652", "")}]', r'\1', text)

    def remove_numbers(self, text):
        return re.sub(r'[0-9٠-٩]', '', text)

    def remove_punctuation(self, text):
        return re.sub(r'[،؛؟!:.,"\'\[\]\(\){}<>«»—ـ]', '', text)

    def unify_alef(self, text):
        return re.sub(r'[أإآٱ]', 'ا', text)

    def remove_stopwords(self, text):
        return ' '.join(word for word in text.split() if word not in self.stopwords)

    def remove_repeated_chars(self, text):
        return re.sub(r'(.)\1{2,}', r'\1', text)

    def fix_punctuation_spacing(self, text):
        text = re.sub(r'\s+([،؛؟!:.])', r'\1', text)
        return re.sub(r'([،؛؟!:.])(\S)', r'\1 \2', text)

    def remove_emojis(self, text):
        emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"u"\U0001F300-\U0001F5FF"u"\U0001F680-\U0001F6FF"u"\U0001F700-\U0001F77F"u"\U0001F780-\U0001F7FF"u"\U0001F800-\U0001F8FF"u"\U0001F900-\U0001F9FF"u"\U0001FA00-\U0001FA6F"u"\U0001FA70-\U0001FAFF"u"\U00002702-\U000027B0"u"\U000024C2-\U0001F251"]+", flags=re.UNICODE)
        return emoji_pattern.sub('', text)

    def remove_latin_chars(self, text):
        return re.sub(r'[a-zA-Z]', '', text)

    def unify_final_ya(self, text):
        return re.sub(r'ى\b', 'ي', text)

    def remove_repeated_words(self, text):
        return re.sub(r'\b(\w+)\s+\1\b', r'\1', text)

    def remove_short_words(self, text, min_length=2):
        return ' '.join(word for word in text.split() if len(word) > min_length)

    def replace_numbers_with_words(self, text):
        return ''.join(self.num_dict[char] if char in self.num_dict else char for char in text)

    def remove_foreign_words(self, text):
        return re.sub(r'\b[a-zA-Z]+\b', '', text)

    def remove_urls(self, text):
        return re.sub(r'http[s]?://\S+', '', text)

    def full_clean(self, text):
        """
        Apply all cleaning functions in sequence.
        """
        text = self.remove_urls(text)
        text = self.remove_emojis(text)
        text = self.remove_latin_chars(text)
        text = self.normalize_persian_urdu(text)
        text = self.unify_alef(text)
        text = self.unify_final_ya(text)
        text = self.remove_tatweel(text)
        text = self.clean_arabic_text(text)
        text = self.remove_numbers(text)
        text = self.remove_punctuation(text)
        text = self.remove_isolated_letters(text)
        text = self.remove_repeated_chars(text)
        text = self.remove_extra_spaces(text)
        text = self.remove_stopwords(text)
        text = self.fix_punctuation_spacing(text)
        return text.strip()


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