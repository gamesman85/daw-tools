#!python3

import pyttsx3

def speak(phrase):
  engine = pyttsx3.init()
  engine.say(phrase)
  engine.runAndWait()