import pyttsx3 as p3
from Merlim import *
import speech_recognition as sr

engine = p3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate", 150)
engine.setProperty('voice', voices[0].id)
engine.setProperty("volume", 0.9)

rec = sr.Recognizer()
# print(sr.Microphone().list_microphone_names())

while True:
    with sr.Microphone(1) as mic:
        rec.adjust_for_ambient_noise(mic)
        audio = rec.listen(mic)
        txt = rec.recognize_google(audio, language="pt-BR")
        if txt == None:
            pass
        else:
            print(txt)
            if "Merlin" in txt:
                p3.speak("Olá mestre")