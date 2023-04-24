# import pyttsx3
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[1].id)

def speak(audio):
    print('F.R.I.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12: 
        speak("Good morning sir")
    elif 12 <= hour < 18:
        speak("Goof afternon sir")
    elif 12 <= hour < 24:
        speak("Good night sir")
    else:
        speak("It's time to go to the bed Sir")
    speak("How can i help you?")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)

    try:
        query = c.recognize_google(audio, language='en')
        print("You: " + query)

    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query = str(input('You order is: '))
    
    return query


if __name__ == "__main__":
    welcome()
    while True:
        # query = command().lower()
        query = command().lower()
        if "google" in query:
            speak("What should i search on google sir?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here if your {search} on google')

        elif "youtube" in query:
            speak("What should i search on youtube sir?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here if your {search} on youtube')

        # elif "" in query:


        speak("How can i help you sir")
    # speak("Hello")