import pyttsx3
import speech_recognition as sr
import eel
import time
def speak(text):
    engine = pyttsx3.init('sapi5') # sapi5 is for Windows, 'espeak' for Linux & 'nsss' for macOS
    voices = engine.getProperty('voices')  # Get available voices
    engine.setProperty('voice', voices[0].id) # Set the first voice
    engine.setProperty('rate', 160)  # Set the rate of speech
    eel.displaySpeakMsg(f"You said: {text}")
    engine.say(text) 
    engine.runAndWait()
    
@eel.expose    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.displaySpeakMsg("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, 10, 5)
    try:
        print("Recognizing Plz Wait...")
        eel.displaySpeakMsg("Recognizing Plz Wait...")
        query = r.recognize_google(audio, language='en-us')
        # print(f"You said: {query}\n") # it will print the recognized text
        eel.displaySpeakMsg(f"You said: {query}")
        # speak(f"You said: {query}") # It will speak the recognized text
    except Exception as e:
        print(f"Sorry, I did not understand that. {e}")
        return None
    return query.lower()

@eel.expose 
def allCommands():
    query = takeCommand()
    print(f"Command received: {query}")
    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "on youtube" in query:
        from engine.features import playYoutube
        playYoutube(query)    
    else:
        print("Command not recognized.")    
    eel.showHood()
