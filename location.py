import datetime
import requests
import pyttsx3
from bs4 import BeautifulSoup 
import webbrowser
import os 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) 
engine.setProperty('rate',180) 
import pywhatkit as kit 

def speak(audio) :
        print("  ")
        print(f" {audio} ")
        print("  ")
        engine.say(audio)
        engine.runAndWait() 

def find_location(shout=True):
        try:
            r = requests.get("https://get.geojs.io/")
            ip_request = requests.get("https://get.geojs.io/v1/ip.json")
            ip_address = ip_request.json()['ip']

            url = "https://get.geojs.io/v1/ip/geo/" + ip_address + ".json"
            # # url to get the location
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()

            # # it will give data in the form of dictonary
            # # it mnay throw error sometimws because there may be no state for some plcaes like delhi
            city = geo_data['city']
            state = geo_data['region']
            country = geo_data['country']
            if shout:
                print(ip_address)
                print(geo_data)
                speech = f"Sir we are in {city} city in {state} region of  {country}"
                speak(speech)
            return city
        except:
            speak(
                "Sorry sir,due to poor internet i cannot find the location")
            # finding location takes more time ,so we added exception.
            pass