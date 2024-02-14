from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import wikipedia
import pyautogui
import keyboard
from time import sleep
import pyjokes
import datetime
from playsound import playsound
import requests
import PyPDF2
from gtts import gTTS
import wolframalpha
import winshell
import subprocess
import ctypes
from ecapture import ecapture as ec
import json
from urllib.request import urlopen
import smtplib
from email_id import password, my_gmail, mess_token, mess_sid, sender_id
from twilio.rest import Client
import wikipedia as googleScrap
import speedtest
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
from googletrans.client import Translator


assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id)
assistant.setProperty('rate', 170)


def speak(audio):
    assistant.say(audio)
    print(f": {audio}")
    print("     ")
    assistant.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    print(hour)

    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 < hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jett")


def user_takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold = 0.6
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio, language='en-in')
            print(f"User Said : {query}")

        except:
            return "none"

        return query.lower()


def taskexe():

    def Music():

        speak("Tell Me The Name Of The Song!")
        music = user_takecommand()

        if 'no lie' in music:
            os.startfile('"C:\\Users\\priya\\Music\\No-Lie.mp3"')

        elif 'Hanuman Chalisa' in music:
            os.startfile('"C:\\Users\\priya\\Music\\Hanumanchalisa.mp3"')

        else:
            pywhatkit.playonyt(music)

        speak("Song Has Been Started")


    dictapp = {"command": "cmd", "paint": "paint", "word": "winword", "excel": "excel", "vs code": "code",
               "powerpoint": "powerpnt", "notepad": "notepad", "vmware": "vmware"}

    def openappweb(query):
        speak("Ok sir, Wait A Second!")
        if ".com" in query or ".co.in" in query or ".org" in query:
            query = query.replace("open", "")
            query = query.replace("jett", "")
            query = query.replace("launch", "")
            query = query.replace(" ", "")
            webbrowser.open(f"https://www.{query}")

        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'chrome' in query:
            webbrowser.open("https://www.google.com/")

        else:
            keys = list(dictapp.keys())
            for app in keys:
                if app in query:
                    os.system(f"start {dictapp[app]}")

    def closeappweb(query):
        speak("Closing sir")
        if "one tab" in query or "1 tab" in query:
            pyautogui.hotkey("ctrl", "w")
            speak("All tabs closed")

        if 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")

        if 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif "2 tab" in query:
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            speak("All tabs closed")

        elif "3 tab" in query:
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            speak("All tabs closed")

        elif "4 tab" in query:
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            speak("All tabs closed")

        elif "5 tab" in query:
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            speak("All tabs closed")

        else:
            keys = list(dictapp.keys())
            for app in keys:
                if app in query:
                    os.system(f"TASKKILL /F /im {dictapp[app]}.exe")

    def YoutubeAuto():
        speak("Youtube Automation started!")
        comm = user_takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'start' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'unmute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'next' in comm:
            keyboard.press('l')

        elif 'open search bar' in comm:
            keyboard.press('/')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'exit full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        elif 'exit film mode' in comm:
            keyboard.press('t')

        speak("Done, sir")

    def ChromeAuto():
        speak("Chrome Automation started!")

        command = user_takecommand()

        if 'close the tab' in command:
            keyboard.press_and_release('ctrl  + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'open history page' in command:
            keyboard.press_and_release('ctrl + h')

        elif 'incognito mode' in command:
            keyboard.press_and_release('Ctrl + Shift + n')

        elif 'jump next tab' in command:
            keyboard.press_and_release('Ctrl + PgDn')

        elif 'jump previous tab' in command:
            keyboard.press_and_release('Ctrl + PgUp')

        elif 'maximize window' in command:
            keyboard.press_and_release('Alt + Space + n')

        elif 'minimize window' in command:
            keyboard.press_and_release('Alt + Space + x')

        elif 'open download page' in command:
            keyboard.press_and_release('Ctrl + j')

        elif 'open chrome menu' in command:
            keyboard.press_and_release('Alt + f')

        elif 'reload page' in command:
            keyboard.press_and_release('Ctrl + r')

        elif 'full screen' in command:
            keyboard.press_and_release('F11')

        elif 'page big size' in command:
            keyboard.press_and_release('Ctrl and +')

        elif 'page small size' in command:
            keyboard.press_and_release('Ctrl and -')

        elif 'return page size' in command:
            keyboard.press_and_release('Ctrl + 0')

        elif 'scroll down' in command:
            keyboard.press_and_release('PgDn')

        elif 'scroll up' in command:
            keyboard.press_and_release('PgUp')

        elif 'go to top page' in command:
            keyboard.press_and_release('Home')

        elif 'go to bottom page' in command:
            keyboard.press_and_release('End')

        speak("Done, sir")

    def Screenshot():
        speak("Ok sir")
        path = user_takecommand()
        path1name = path + ".png"
        path1 = "C:\\Users\\priya\\OneDrive\\Pictures\\Screenshots\\" + path1name
        ss = pyautogui.screenshot()
        ss.save(path1)
        os.startfile("C:\\Users\\priya\\OneDrive\\Pictures\\Screenshots")
        speak("Here Is Your ScreenShot")

    def Temp():
        speak("Ok sir !")
        search = "temperature in vadodara"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_="BNeawe").text
        speak(f"The Temperature Outside Is {temperature} ")

    def Reader():
        speak("Tell Me The Name Of The Book!")

        name = user_takecommand()

        if 'india' in name:
            os.startfile('D:\\program\\ch 1.pdf')
            book = open('D:\\program\\ch 1.pdf', 'rb')
            pdfreader = PyPDF2.PdfReader(book)
            pages = pdfreader.getNumPages()
            speak(f"Number Of Page In This Books Are {pages}")
            speak("From Which Page I Have To Start Reading?")
            numPage = int(input("Enter The Page Number :"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            speak("In Which Language, I Have To Read?")
            lang = user_takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text, 'hi')
                textm = textHin.text
                speech = gTTS(text=textm)

                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                speak(text)

    def sendemail(to, content):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(my_gmail, password)
        server.sendmail(my_gmail, to, content)
        server.close()

    if __name__ == "__main__":
        wishMe()

    while True:

        query = user_takecommand()

        if 'hello' in query:
            speak("Hello sir, I am Jett")
            speak("How are you sir ?")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'what about you' in query:
            speak("I am fine")
            speak("How may i help you ?")

        elif 'you need a break' in query:
            speak("Ok sir, You can call anytime !")
            speak("bye bye sir.")
            break

        elif 'bye' in query:
            speak("bye bye sir.")
            speak("Have a Nice Day!")

        elif 'good night jett' in query:
            speak("Good Night")
            speak("see youu..")

        elif 'youtube search' in query:
            speak("Ok sir, I found for your search")
            query = query.replace("jett", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Open sir...")

        elif 'google search' in query:
            speak("I found for your search")
            query = query.replace("Jett", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            speak("Done sir...")

        elif 'website' in query:
            speak("Ok sir,")
            speak("Launching...")
            query = query.replace("jett", "")
            query = query.replace("website", "")
            query = query.replace(" ", "")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("Open sir...")

        elif 'launch' in query:
            speak("Tell Me The Name Of The Website")
            name = user_takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Open sir...")

        elif 'facebook' in query:
            speak("Ok sir")
            webbrowser.open("https://www.facebook.com")
            speak("Open sir...")

        elif 'instagram' in query:
            speak("Ok sir")
            webbrowser.open("https://www.instagram.com")
            speak("Open sir...")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("jett", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query, 2)
            speak(f"According To Wikipedia : {wiki}")

        elif 'music' in query:
            Music()

        elif 'open' in query:
            openappweb(query)

        elif 'close' in query:
            closeappweb(query)

        elif 'close youtube' in query:
            closeappweb(query)

        elif 'open youtube' in query:
            openappweb(query)

        elif 'close google' in query:
            closeappweb(query)

        elif 'open google' in query:
            openappweb(query)

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'start' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'unmute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'next' in query:
            keyboard.press('l')

        elif 'open search bar' in query:
            keyboard.press('/')

        elif 'exit film mode' in query:
            keyboard.press('t')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'exit full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl  + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'incognito mode' in query:
            keyboard.press_and_release('Ctrl + Shift + n')

        elif 'jump next tab' in query:
            keyboard.press_and_release('Ctrl + PgDn')

        elif 'jump previous tab' in query:
            keyboard.press_and_release('Ctrl + PgUp')

        elif 'maximize window' in query:
            keyboard.press_and_release('Alt + Space + n')

        elif 'minimize window' in query:
            keyboard.press_and_release('Alt + Space + x')

        elif 'open download page' in query:
            keyboard.press_and_release('Ctrl + j')

        elif 'open chrome menu' in query:
            keyboard.press_and_release('Alt + f')

        elif 'reload page' in query:
            keyboard.press_and_release('Ctrl + r')

        elif 'full screen' in query:
            keyboard.press_and_release('F11')

        elif 'page big size' in query:
            keyboard.press_and_release('Ctrl and +')

        elif 'page small size' in query:
            keyboard.press_and_release('Ctrl and -')

        elif 'return page size' in query:
            keyboard.press_and_release('Ctrl + 0')

        elif 'scroll down' in query:
            keyboard.press_and_release('PgDn')

        elif 'scroll up' in query:
            keyboard.press_and_release('PgUp')

        elif 'go to top page' in query:
            keyboard.press_and_release('Home')

        elif 'go to bottom page' in query:
            keyboard.press_and_release('End')

        elif 'chrome tool' in query:
            ChromeAuto()

        elif 'all hide' in query:
            keyboard.press_and_release('Windows + D')

        elif 'all show' in query:
            keyboard.press_and_release('Windows Key + D')

        elif 'open file explorer' in query:
            keyboard.press_and_release('Windows Key + E')

        elif 'open game bar' in query:
            keyboard.press_and_release('Windows + G')

        elif 'open setting' in query:
            keyboard.press_and_release('Windows Key + I')

        elif 'lock computer' in query:
            keyboard.press_and_release('Windows Key + L')

        elif 'open setting' in query:
            keyboard.press_and_release('Windows Key + I')

        elif 'open task view' in query:
            keyboard.press_and_release('Windows Key + Tab')

        elif 'swap right' in query:
            keyboard.press_and_release('Home')

        elif 'right' in query:
            keyboard.press_and_release('Home')

        elif 'swap left' in query:
            keyboard.press_and_release('End')

        elif 'left' in query:
            keyboard.press_and_release('End')

        elif 'play joke' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'repeat my words' in query:
            speak("Speak Sir!")
            rmw = user_takecommand()
            speak(f"You Said: {rmw}")

        elif 'my location' in query:
            speak("Ok Sir, Finding Your Location!")
            webbrowser.open('https://www.google.com/maps/@23.022505,72.5713621,11z?authuser=0&entry=ttu')

        elif 'screenshot' in query:
            Screenshot()

        elif 'alarm' in query:
            speak('Enter The Time !')
            time = input(": Enter The Time :")

            while True:
                Time_al = datetime.datetime.now()
                now = Time_al.strftime("%H:%M:%S")

                if now == time:
                    speak("Time To Wake Up Sir!")
                    playsound('alarm.mp3')
                    speak("Alarm Closed!")

                elif now > time:
                    break

        elif 'remember that' in query:
            remeberMsg = query.replace("remember that", "")
            remeberMsg = query.replace("jett", "")
            speak("You Tell Me T Remind You That :" + remeberMsg)
            remeber = open('data.txt', 'w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'read remember' in query:
            remeber = open('data.txt', 'r')
            speak("You Tell Me That" + remeber.read())

        elif 'what the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'google search' in query:
            query = query.replace("jett", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query, 2)
                speak(result)

            except:
                speak("No Speakable Data Available!")

        elif 'temperature' in query:
            Temp()

        elif 'read a book' in query:
            Reader()

        elif "calculate" in query:

            app_id = "H2EYA9-3YPJ5YRVT8"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'clean recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(user_takecommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jett Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = user_takecommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = user_takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "showing note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'global news' in query:

            try:
                jsonObj = urlopen('https://newsapi.org/v2/top-headlines?country=us&apiKey=59fda92d101048c0b4e4fd450567d24b')
                data = json.load(jsonObj)
                i = 1

                speak('Here Are Some Top News From The Times Of Global News')
                print("_______Global News_______"+ '\n')

                for item in data['articles']:
                    speak(str(i) + '. ' + item['title'] + '\n')
                    speak(item['description'] + '\n')
                    i += 1

            except Exception as e:

                print(str(e))

        elif 'india news' in query:

            try:
                jsonObj = urlopen('https://newsapi.org/v2/top-headlines?country=in&apiKey=59fda92d101048c0b4e4fd450567d24b')
                data = json.load(jsonObj)
                i = 1

                speak('Here Are Some Top News From The Times Of INDIA News')
                print("_______INDIA News_______"+ '\n')

                for item in data['articles']:
                    speak(str(i) + '. ' + item['title'] + '\n')
                    speak(item['description'] + '\n')
                    i += 1

            except Exception as e:

                print(str(e))

        elif 'tech news' in query:

            try:
                jsonObj = urlopen('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=59fda92d101048c0b4e4fd450567d24b')
                data = json.load(jsonObj)
                i = 1

                speak('Here Are Some Top News From The Times Of Tech News')
                print("_______Tech News_______"+ '\n')

                for item in data['articles']:
                    speak(str(i) + '. ' + item['title'] + '\n')
                    speak(item['description'] + '\n')
                    i += 1

            except Exception as e:

                print(str(e))

        elif "send email to priyanshu" in query:
            try:
                speak("What should say sir!")
                content = user_takecommand()
                to = sender_id
                sendemail(to, content)
                speak("Email has ben send successfully.")

            except Exception as error:
                print(error)
                speak("Email has not been sent due to some error.")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = user_takecommand()
                speak("whome should i send")
                to = input()
                sendemail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'check internet speed' in query:
            speak("Checking speed.....")
            speed_test = speedtest.Speedtest()

            def bytes_to_mb(bytes):
                KB = 1024
                MB = KB * 1024
                return int(bytes / MB)

            ds = bytes_to_mb(speed_test.download())
            us = bytes_to_mb(speed_test.upload())
            speak(f"The Downloading Speed Is {ds} MBP S")
            speak(f"The Uploading Speed Is {us} MBP S")

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'volume mute' in query:
            pyautogui.press("volumemute")

        elif 'check phone location' in query:
            speak("Ok sir, Data Connecting To The Server !")
            speak("Enter Phone Number")
            number = '+91' + input()
            phone = phonenumbers.parse(number)
            time = timezone.time_zones_for_number(phone)
            car = carrier.name_for_number(phone, "en")
            reg = geocoder.description_for_number(phone, "en")
            speak(f"{phone}")
            speak(f"Time Zone : {time}")
            speak(f"SIM Card Providers Comparison{car}")
            speak(f"Location : {reg}")



taskexe()

user_takecommand()