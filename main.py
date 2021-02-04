import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import weather
from time import sleep
from word2number import w2n


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

name = 'alexa'
name = name.lower()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def listenInput():
    command = False
    listening = True
    if listening is True:
        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
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
            print('Wake word not detected.')
        return command
    else:
        pass


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
        elif 'weather' in command:
            city = command.replace("what's the weather in", '')
            temperature = weather.temperature(city)
            feel_like = weather.feels_like(city)
            country = weather.country(city)
            temp_min = weather.temp_min(city)
            temp_max = weather.temp_max(city)
            basic = weather.basic(city)
            print('Current forecast in ' + str(city) + ","  + str(country) +  ' is ' + str(basic) + ". The temperature now is about "+ str(temperature) + 
            ' degrees. Maximum temperature for today will be ' + str(temp_max) + ' degrees, and lower ' + str(temp_min) + " degrees fahrenheit")
            talk('Current forecast in ' + str(city) + ","  + str(country) +  ' is ' + str(basic) +  ". The temperature now is about "+ str(temperature) + 
            ' degrees. Maximum temperature for today will be ' + str(temp_max) + ' degrees, and lower ' + str(temp_min) + " degrees fahrenheit")


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