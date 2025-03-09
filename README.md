# Ana - Voice Assistant

Ana is a Python-based voice assistant that can recognize speech, perform various system tasks, manage files, interact with an SQLite database, and provide Wikipedia search results.  

---

## Features  
✅ **Speech Recognition** – Listens and responds to voice commands.  
✅ **Wikipedia Search** – Fetches brief Wikipedia summaries.  
✅ **Web Navigation** – Opens Google, YouTube, Gmail, Stack Overflow.  
✅ **Music Playback** – Opens Spotify for music streaming.  
✅ **Time Check** – Tells the current time.  
✅ **File Management** – Lists and deletes files from a directory.  
✅ **Database Management** – Stores and retrieves user data in an SQLite database.  
✅ **System Control** – Can shutdown or restart the system.  

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

## Features
- Text-to-speech using `pyttsx3`
- Speech recognition using `speech_recognition`
- Time-based greetings
- Basic voice command handling
- MySQL database connection

## Requirements
Install the necessary dependencies using:
```bash
pip install pyttsx3 speechrecognition mysql-connector-python
