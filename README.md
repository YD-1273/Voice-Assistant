# Ana - Voice Assistant

Ana is a Python-based voice assistant that can recognize speech, perform various system tasks, manage files, interact with an SQLite database, and provide Wikipedia search results.  

---

## Features  
1. **Speech Recognition** – Listens and responds to voice commands.  
2. **Wikipedia Search** – Fetches brief Wikipedia summaries.  
3. **Web Navigation** – Opens Google, YouTube, Gmail, Stack Overflow.  
4. **Music Playback** – Opens Spotify for music streaming.  
5. **Time Check** – Tells the current time.  
6. **File Management** – Lists and deletes files from a directory.  
7. **Database Management** – Stores and retrieves user data in an SQLite database.  
8. **System Control** – Can shutdown or restart the system.  

---

## Functions and Commands  

| Command | Function |
|---------|----------|
| `"open google"` | Opens Google in the web browser |
| `"open youtube"` | Opens YouTube |
| `"open stackoverflow"` | Opens Stack Overflow |
| `"open mail"` | Opens Gmail |
| `"play music"` | Opens Spotify |
| `"current time"` | Tells the current time |
| `"list files"` | Lists all files in the current directory |
| `"delete file"` | Deletes a specified file |
| `"create database"` | Creates an SQLite database |
| `"add user"` | Adds a user to the database (requires name and age) |
| `"show users"` | Displays all users from the database |
| `"shut down system"` | Shuts down the system |
| `"restart system"` | Restarts the system |

---

## Installation  

### Clone the Repository  
```bash
git clone https://github.com/yourusername/bunny-voice-assistant.git
cd bunny-voice-assistant
```

### Install Dependencies  
```bash
pip install -r requirements.txt
```

### Run the Assistant
```bash
python Ana.py
```

## How to Use
1. Run the script
2. **Speak when prompted** – The assistant listens and processes your command.
Example interactions:
You: "Open Google"

Bunny: (Opens Google in a web browser)

You: "What is Python from Wikipedia?"

Bunny: (Gives a brief summary from Wikipedia)

You: "Add user"

Bunny: "Please say the name"

You: "John"

Bunny: "Please say the age"

You: "25"

Bunny: "Added John with age 25 to the database"



### Requirements
Install the necessary dependencies using:
```bash
pip install pyttsx3 speechrecognition wikipedia pyaudio sqlite3
```
