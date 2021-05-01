import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from requests import get
import time
import smtplib
import cv2 #for camera
import random
import pywhatkit as kit
import sys
import pyautogui
from gtts import gTTS

engine = pyttsx3.init('sapi5')
# to change the rate of voice 
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# to convert text to speech
def speak(audio):
    # helps to say for us 
    engine.say(audio)
    # ask computer to wait until sentence is finished
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    elif hour >= 18 and hour <= 21:
        speak("Good Evening!")
    
    else:
        speak("Good Night!")
    
    speak("I am your Assistant Sir. Please let me know How  I can help you!")
    
# to covert voice into text(string)
def takeCommand():
    # It takes Microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n\nListening.....")
        r.pause_threshold=1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(query)  
    
    except Exception as e:

        print("Say that again please.....")
        return "None"
    return query

# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('munivashisht895330@gmail.com', 'Vashisht@20')
    server.sendmail('munivashisht895330@gmail.com', to , content)
    server.close()



if __name__ == "__main__":
    clear = lambda: os.system('cls')
    speak("Hello Vashisht!")
    clear()
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia.... ')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com")
        
        elif 'google' in query:
            webbrowser.open("https://www.google.com")
            
        elif 'stack overflow' in query:
            speak("hello welcome to stackoverflow!")
            webbrowser.open("https://www.stackoverflow.com")
        

        elif 'play music' in query:
            music_dir ='C:\\Users\\Vashisht\\Music'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        
        elif 'increase volume' in query:
            pyautogui.press("volumeup")
        
        elif 'decrease volume' in query:
            pyautogui.press("volumedown")
        
        elif 'mute volume' in query or 'mute' in query:
            pyautogui.press("volumemute")
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\Vashisht\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email to vashisht' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Whom should I send?")
                to = "munivashisht895330@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Sir , I am not able to send this email at the moment")
        
        elif 'open notepad' in query:
            notepadpath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(notepadpath)
        
        elif 'open adobe reader' in query:
            adobereaderpath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(adobereaderpath)
        
        elif 'open command prompt' in query:
            os.system("start cmd")
        
        elif 'open camera' in query:
            TIMER = int(10)
            cap = cv2.VideoCapture(0) # open the camera
            while True:
                ret, img = cap.read() #read and display each frame
                cv2.imshow('a', img)
                k = cv2.waitKey(125)
                if k == ord('q'): # if key pressed is q
                    prev = time.time()

                    while TIMER >= 0:
                        ret, img = cap.read()

                        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
                        #specify the font and draw
                        cv2.putText(img, str(TIMER), (200, 250), font, 7, (0, 255, 255), 4, cv2.LINE_AA)
                        cv2.imshow('a', img)
                        cv2.waitKey(125)

                        cur = time.time()

                        if cur-prev >= 1:
                            prev = cur
                            TIMER = TIMER - 1
                    else:
                        ret, img = cap.read()
                        cv2.imshow('a', img)
                        cv2.waitKey(2000) #time for which image displayed
                        cv2.imwrite('nature.jpg', img)
                elif k == 27:
                    break
            cap.release() # close the camera
            cv2.destroyAllWindows() # close all the  runing windows
        
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"Your Ip address is {ip}")
        
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
        
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
        
        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com")
        
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
        
        elif 'send message' in query:
            kit.sendwhatmsg("+919616988692", "this is vashisht", 13, 50)
        


            
        

               
               


               
               



  
  

