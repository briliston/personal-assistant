import speech_recognition as sr
import time
from time import strftime
import os
from gtts import gTTS
import requests, json
from pygame import mixer
import random

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = recognizer.listen(source)
    data = ""
    try:
        data = recognizer.recognize_google(audio)
        print("you said: " + data)
    except sr.UnknownValueError:
        print("Google speach recognition did not understand audio.")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data

def respond(audioString):
    print(audioString)

    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    mixer.init()
    mixer.music.load("speech.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    mixer.quit()
    os.remove("speech.mp3")

def personal_assistant(data):
    if "how are you" in data:
        listening = True
        respond("I'm good.")
    elif "want to play a game" in data:
        listening = True
        respond("sure, which one?")
    elif "guess the number" in data:
        listening = True
        respond("Okay. I'm thinking of a number between 1 and 20.")
        num_to_guess = random.randint(1, 20)
#        while int(data) != num_to_guess:
#            if int(data) < num_to_guess:
#                respond("too high")
#            elif int(data) > num_to_guess:
#                respond("too low")
#        respond("You got it! the number was" + str(num_to_guess))
    elif "what time is it" in data:
        listening = True
        respond(strftime('%H:%M%p'))
    elif "thank you" in data:
        listening = True
        respond("You're welcome.")
    elif "tell her" in data:
        listening = True
        respond("Of course! Happy Birthday G share! Your grand daughter loves you!")
    elif "open Google Chrome" in data:
        listening = True
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        respond("Sure thing.")
    elif "where is" in data:
        listening = True
        data = data.split(" ")
        location_url = "https://www.google.com/maps/place/" + str(data[2])
        respond("Hold on, I will show you where " + data[2] + " is.") 
        maps_arg = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe -a "/Applications/Google Chrome.app" ' + location_url
        os.system(maps_arg)
    elif "open Steam" in data:
        listening = True
        os.startfile("C:\Program Files (x86)\Steam\steam.exe")
        respond("Sure thing.")
    elif "stop listening" in data:
        listening = False
        print('Listening stopped')
        return listening
    else:
        listening = True
        respond("Sorry I didn't catch that?")

    return listening

time.sleep(2)
respond("Hi Bri, what's up?")
listening = True
while listening == True:
    data = listen()
    listening = personal_assistant(data)