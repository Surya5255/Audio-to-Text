import speech_recognition as sr
r = sr.Recognizer()

with sr.AudioFile('Audio.wav') as source:
    print("listening to audio")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("Audio:", text)
    except:
        print('Error')