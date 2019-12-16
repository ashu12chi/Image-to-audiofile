# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 01:28:03 2019

@author: ASHUTOSH CHITRANSHI
"""

from PIL import Image
import pytesseract
from gtts import gTTS 
img = Image.open('test.jpg')
mytext = pytesseract.image_to_string(img)
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("test.mp3") 