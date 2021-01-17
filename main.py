import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

name = 'Alexa'
name = name.lower()

def talk(text):
    engine.say(text)
    engine.runAndWait()

    
def listenInput():
    command = False
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            audio = listener.recognize_google(voice)
            audio = audio.lower()
            print(audio)
            if name in audio:
                command = audio.replace(name, '')
                print('listeningInput= ' + command)
                return command
            else:
                pass
    except:
        print('Wake word not detecting.')
    return command

def executeOutput():
    command = listenInput()
    if command == False:
        return
    else:
        print('executeOutput= ' + command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'who are you' in command:
            talk('I am your private assistant')
        elif 'tell me something fun' in command:
            talk(pyjokes.get_joke())
        else:
            if 'what is' in command:
                googleSearch = command.replace('what is', '')
                talk('This is what I have found on Google for ' + googleSearch)
                pywhatkit.search(googleSearch)
            else:
                pywhatkit.search(command)
                talk('This is what I have found on Google for ' + command)


while True:
    executeOutput()