import speech_recognition as sr
Recognizer=sr.Recognizer()
filetoopen=sr.AudioFile('1.wav')
with filetoopen as source :
	audio=Recognizer.record(source)
text=Recognizer.recognize_google(audio)
file1=open(r"C:\laragon\www\HOW-TO-EXTRACT-TEXT-FROM-SPEECH-speech-recognition-using-python\1.txt","a") # your directory
file1.writelines(text)
file1.close()

