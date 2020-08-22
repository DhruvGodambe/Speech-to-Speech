import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 170)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)

rate = engine.getProperty('rate')

# for i in range(5):
# 	a = input()
# 	engine.say(a)

r = sr.Recognizer()



with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    
engine.say('you just said: ' + r.recognize_google(audio))

# a,b = 10,12

# for word in r.recognize_google(audio).split():
# 	if(word == 'multiply'):
# 		result = a * b
# 	elif(word == 'add'):
# 		result = a + b


# engine.say('the result is ' + str(result))

engine.runAndWait()
