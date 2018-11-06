#pip install SpeechRecognition
import speech_recognition as recog
rec = recog.Recognizer()
harv = recog.AudioFile('harvard.wav')

with harv as source:
	rec.adjust_for_ambient_noise(source)
	audio = rec.record(source)

r.recognize_google(audio)

#To access your microphone with SpeechRecognizer
#pip install pyaudio
r=recog.Recognizer()
mic=recog.Microphone()

with mic as source:
   audio = r.listen(source)

r.recognize_google(audio)
