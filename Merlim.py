import datetime
from time import sleep
import speech_recognition as sr
import pyttsx3 as p3
import pyautogui as py

rec = sr.Recognizer()
tim = datetime.datetime.today().hour
time = datetime.datetime.today().time()
engine = p3.init()
engine.setProperty("rate", 200)
engine.setProperty("volume", 1)

def comand():
    with sr.Microphone(6) as mic:
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language='pt-BR')
        txt = str(texto).lower()

while True:
    with sr.Microphone(6) as mic:
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language='pt-BR')
        txt = str(texto).lower()
        print(txt)
        if "merlin" in txt:
            sleep(0.25)
            p3.speak('Olá mestre pode falar')
            sleep(0.5)
            comand()

            a = txt.find('abra')
            b = txt.find('playlist')
            c = txt.find('pesquise')
            d = txt.find('lembre')
            d1 = txt.find('tempo')
            e = txt.find('Volume')
            f = txt.find('ligação')

            if 'abra' in txt:
                p3.speak('Abrindo')
                py.press('win')
                sleep(0.3)
                py.write('google')
                sleep(0.5)
                py.press('enter')
                sleep(3)
                py.write(txt[a + 5:])
                sleep(0.5)
                py.press('enter')
                sleep(1)
                py.moveTo(150, 350)
                py.click(150, 350)


            elif 'pesquise' in txt:
                p3.speak('pesquisando')
                py.press('win')
                sleep(0.3)
                py.write('google')
                sleep(0.5)
                py.press('enter')
                sleep(3)
                py.write(txt[c + 9:])
                py.press('enter')

            elif 'horas' in txt:
                p3.speak('são {}'.format(time))
                print(time)

            elif 'playlist' in txt:
                py.press('win')
                sleep(0.3)
                py.write('deezer')
                py.press('enter')
                sleep(3)
                py.moveTo(95, 450)
                py.click(95, 450)
                sleep(1.5)
                py.moveTo(585, 305)
                py.click(585, 305)
                sleep(1.5)
                py.moveTo(1250, 15)
                py.click(1250, 15)
                py.moveTo(1250, 10)
                py.click(1250, 10)

            elif 'trocar' in txt:
                py.press('win')
                sleep(0.3)
                py.write('deezer')
                py.press('enter')
                sleep(3)
                sleep(1)
                py.moveTo(135, 690)
                py.click(135, 690)
                sleep(1.5)
                py.moveTo(1250, 10)
                py.click(1250, 10)

            elif 'lembre' in txt:
                da = txt[d + 7]
                d2 = bool(da)
                if 'segundo' in txt:
                    d3 = d2 * 10
                elif 'minuto' in txt:
                    d3 = d2 * 600
                elif 'hora' in txt:
                    d3 = d2 * 36000
                sleep(d3)
                p3.speak(txt[d + 7:d1])

            elif 'volume' in txt:
                py.moveTo(1175, 750)
                py.click(1175, 750)
                sleep(0.3)
                py.moveTo(1150, 665)
                py.click(1150, 665)
                if '25' in txt:
                    sleep(0.3)
                    py.moveTo(1130, 700)
                    py.click(1130, 700)
                    sleep(0.8)
                    py.moveTo(1175, 750)
                    py.click(1175, 750)
                elif '50' in txt:
                    sleep(0.3)
                    py.moveTo(1187, 700)
                    py.click(1187, 700)
                    sleep(0.8)
                    py.moveTo(1175, 750)
                    py.click(1175, 750)
                elif '75' in txt:
                    sleep(0.3)
                    py.moveTo(1243, 700)
                    py.click(1243, 700)
                    sleep(0.8)
                    py.moveTo(1175, 750)
                    py.click(1175, 750)
                elif '100' in txt:
                    sleep(0.3)
                    py.moveTo(1300, 700)
                    py.click(1300, 700)
                    sleep(0.8)
                    py.moveTo(1175, 750)
                    py.click(1175, 750)

            elif 'ligação' in txt:
                p3.speak('ligando')
                py.press('win')
                sleep(0.3)
                py.write('wha')
                sleep(1)
                py.press('enter')
                sleep(2)
                py.hotkey('ctrl', 'f')
                if 'vídeo' in txt:
                    py.write(txt[f + 16:])
                    sleep(1)
                    py.moveTo(175, 180)
                    py.click(175, 180)
                    sleep(1)
                    py.moveTo(230, 185)
                    py.click(230, 185)
                    sleep(1)
                    py.moveTo(1195, 70)
                    py.click(1195, 70)
                elif 'voz' in txt:
                    py.write(txt[f + 14:])
                    sleep(1)
                    py.moveTo(175, 180)
                    py.click(175, 180)
                    sleep(1)
                    py.moveTo(230, 185)
                    py.click(230, 185)
                    sleep(1)
                    py.moveTo(1245, 60)
                    py.click(1245, 60)
                else:
                    py.hotkey('ctrl', 'f5')