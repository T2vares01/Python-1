import speech_recognition as sr
import pyttsx3 as p3

engine = p3.init()
engine.setProperty("rate", 200)
engine.setProperty("volume", 1)

rec = sr.Recognizer()
# print(sr.Microphone().list_microphone_names())
with sr.Microphone(5) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)