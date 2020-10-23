'''
Python script to test TTS using pyttsx3
'''
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)

engine.setProperty('voice', 'en+f3')
engine.say("DEPSTAR")

engine.runAndWait()
