import pyttsx3
import engineio
import datetime
import speech_recognition as sr
import mysql.connector

engineio = pyttsx3.init('sapi5')
voices = engineio.getProperty('voices')
rate=engineio.getProperty('rate')
engineio.setProperty('rate',200)
engineio.setProperty('voice',voices[0].id)
vol=engineio.getProperty('volume')
engineio.setProperty('volume',1)
command=['hey','hello','yo']
reply=['welcome','hello',"what 's app"]
db=mysql.connector.connect(host='localhost',user='root',passwd='1425367890+-@')
con=db.cursor()
def speak(text):
    engineio.say(text)
    engineio.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour<=0 and hour>12:
        speak("Good morning Sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon  Sir")
    else:
        speak("good evening Sir")
    speak("mera nam hae Ana")
    speak("how can i help you ")
    
