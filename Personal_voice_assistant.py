import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pyautogui
from bs4 import BeautifulSoup
import requests
import pyjokes
import speedtest


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

############################# greetings###############################


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("how can i help you")

################################ voice commands#######################


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "go to sleep" in query:
            speak("ok sir, you can call me anytime")
            print("ok sir, you can call me anytime")
            break
############################# wikipedia searches####################################
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
############################### play music############################################
        elif 'play music' in query:
            music_dir = "C:\music"
            song = os.listdir(music_dir)
            rd = random.choice(song)
            os.startfile(os.path.join(music_dir, rd))
            
            break
######################################### task from browser###########################
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open Google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=3GI_uE4SxSU")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open erp' in query:
            webbrowser.open(
                "https://erp.mpgi.net/index.aspx?openFor=Students&institute=b05cec9c-2415-42e7-8c12-92cd3c4afe4d")
        elif 'mpgi kanpur' in query:
            webbrowser.open("mpgi.edu.in")
        elif'tell me a joke'in query:
            joke=pyjokes.get_joke()
            speak(joke)
            print(joke)
 ###################################### shutdown system#################################
        elif "shutdown the system" in query:
            speak("you want to shutdown")
            shutdown = input("do you want to shutdown your system? (Yes/No)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")
            elif shutdown == "no":
                break
 ############################################## weather#####################################
        elif 'weather report' in query:
            search = "temperature in kanpur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")
            print("current temperature in kanpur is", temp)
###################################### conversations######################################
        elif 'hello' in query:
            speak('hello sir, how can i help you')
            print('hello sir, how can i help you')
        elif 'i am also fine' in query:
            speak('i am glad to hear this, so what can i do for you')
        elif 'who created you' in query:
            speak('i am created by vaibhav dixit, just for you')
        elif 'tell me something about me' in query:
            speak('you are smart and you like to ask me great question')
        elif 'tell me something about you' in query:
            speak(
                'i am your personal assistent, i can look up answer for you, and ready to help you everytime')
        elif 'how r u' in query:
            speak('i am fine, thanks for asking, and what about you')
            print('i am fine, thanks for asking, and what about you')
        elif 'what is your name' in query:
            speak('my name is edith')
            print('my name is edith')
        elif 'thank you' in query:
            speak("you are welcome sir, i am happy to help you")
        elif 'i love you' in query:
            speak("i love you to sir")
        elif 'who r you' in query:
            speak("i am edith sir,created by vaibhav dixit")
################################## camera & ss#############################
        elif "take screenshot" in query:
            im = pyautogui.screenshot()
            im.save("ss.jpg")
        elif "click photo" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
########################### time###########################################
        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print("the time is", strTime)
######################### master function###################################
       # elif 'none' in query:
            query = query.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(3)
            pyautogui.press("enter")
            
