import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr
import wikipedia
import random
import time
import pyaudio
import sqlite3
import os

# Initialize voice engine
engineio = pyttsx3.init('sapi5')
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 200)
engineio.setProperty('voice', voices[0].id)
engineio.setProperty('volume', 1)

# Predefined responses
command = ['hey', 'hello', 'yo']
reply = ['welcome', 'hello', "what's up"]

# Function to speak
def speak(text):
    engineio.say(text)
    engineio.runAndWait()

# Greeting Function
def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning Sir")
    elif 12 <= hour < 18:
        speak("Good afternoon Sir")
    else:
        speak("Good evening Sir")
    speak("Hi! My name is ANA.")
    print("Hi! My name is ANA.")
    speak("How can I help you?")
    print("How can I help you?")

# Take voice command
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")
    except Exception:
        speak("Say it again please")
        return "None"
    return query.lower()

# SQL Functions
def create_database():
    conn = sqlite3.connect("bunny_assistant.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    conn.commit()
    conn.close()
    speak("Database created successfully")

def insert_data(name, age):
    conn = sqlite3.connect("bunny_assistant.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
    speak(f"Added {name} with age {age} to the database")

def fetch_data():
    conn = sqlite3.connect("bunny_assistant.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    speak(f"Retrieved {len(rows)} records")
    for row in rows:
        print(row)

# File Management
def list_files():
    files = os.listdir()
    speak(f"There are {len(files)} files in this directory.")
    for file in files:
        print(file)

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        speak(f"Deleted {file_name}")
    else:
        speak("File not found")

# System Control
def shutdown_system():
    speak("Shutting down your system")
    os.system("shutdown /s /t 5")  # Windows shutdown command

def restart_system():
    speak("Restarting your system")
    os.system("shutdown /r /t 5")  # Windows restart command

# Main Loop
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand()

        if "wikipedia" in query:
            speak("Searching please wait")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open('youtube.com')

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            webbrowser.open("https://www.spotify.com")

        elif "current time" in query:
            speak(datetime.datetime.now().strftime("%H:%M:%S"))

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open mail" in query:
            webbrowser.open_new("gmail.com")

        elif query in command:
            speak(random.choice(reply))

        elif "wait" in query:
            time.sleep(10)

        elif "create database" in query:
            create_database()

        elif "add user" in query:
            speak("Please say the name")
            name = takecommand()
            speak("Please say the age")
            age = takecommand()
            if age.isdigit():
                insert_data(name, int(age))
            else:
                speak("Invalid age input")

        elif "show users" in query:
            fetch_data()

        elif "list files" in query:
            list_files()

        elif "delete file" in query:
            speak("Which file should I delete?")
            file_name = takecommand()
            delete_file(file_name)

        elif "shut down system" in query:
            shutdown_system()

        elif "restart system" in query:
            restart_system()
