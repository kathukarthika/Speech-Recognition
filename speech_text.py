import speech_recognition as sr 

def speech_recog():
    r=sr.Recognizer()
    mic=sr.Microphone()

    with mic as source:
        print("Speak......")
        r.energy_threshold=700
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

        try:

            text=r.recognize_google(audio)
            print("You said:",text)
        except:
            print("Didn't here anything. pls speak again....")
speech_recog()        