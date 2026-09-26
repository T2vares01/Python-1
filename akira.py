import speech_recognition as sr
import pyttsx3 as p3

# --- Configuração da síntese de voz ---
engine = p3.init()
engine.setProperty("rate", 200)
engine.setProperty("volume", 1)

# Tenta usar uma voz em português, se disponível
for voice in engine.getProperty("voices"):
    if "brazil" in voice.name.lower() or "portuguese" in voice.name.lower() or "pt" in voice.id.lower():
        engine.setProperty("voice", voice.id)
        break


def falar(texto: str) -> None:
    engine.say(texto)
    engine.runAndWait()


def main() -> None:
    rec = sr.Recognizer()
    mic = sr.Microphone()

    # Calibra o ruído ambiente UMA vez, não a cada loop
    with mic as source:
        print("Calibrando ruído ambiente, aguarde...")
        rec.adjust_for_ambient_noise(source, duration=1)

    print("Pronto! Pode falar quando quiser (Ctrl+C para sair).")

    while True:
        try:
            with mic as source:
                print("\nOuvindo...")
                audio = rec.listen(source, timeout=5, phrase_time_limit=10)

            texto = rec.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {texto}")
            falar(f"Você disse: {texto}")

        except sr.WaitTimeoutError:
            print("Nenhuma fala detectada, tentando de novo...")
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
        except sr.RequestError:
            print("Erro ao conectar ao serviço de reconhecimento.")
        except KeyboardInterrupt:
            print("\nEncerrando...")
            break


if __name__ == "__main__":
    main()
