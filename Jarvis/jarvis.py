import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import pywhatkit as kit
import sys
import pyjokes
import pytz
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    elif hour<=12 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    
    speak("I am Jarvis Sir,Please tell how can I help you")

def takeCommand():
    #its take command from user and return output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=4,phrase_time_limit=7)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        #print(e)    
        #print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def location():
    # IP address
    speak("wait sir, let me check")
    try:
        ipAdd = requests.get('http://api.ipify.org').text
        print(ipAdd)
        url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        city = geo_data['city']
        country = geo_data['country']
        speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
    except Exception as e:
        speak("sorry sir, Due to network issue i am not able to find where we are.")
        pass

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tjhoque8016@gmail.com', '8016223319')
    server.sendmail('tjhoque8016@gmail.com', to, content)
    server.close()

def taskExecution():
    wishme()
    while True:
    
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("wait sir, let me check")
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in query:
            speak("I am fine sir, how are you?")
            ans = takeCommand().lower()
            if 'i am fine' in ans or 'i am also fine' in ans or 'not bad':
                speak("that's great to hear from you")
            elif 'i am not well' in ans or 'not' in ans:
                speak("i am hear sir, how can i help you")

        elif 'i love you' in query:
            speak("i love you too sweetheart")

        elif 'who is your boss' in query:
            speak("TJ is my boss")
            print("TJ is my boss")
        
        elif 'thank you' in query:
            speak("Welcome sir")
        
        # opening code
        elif 'open cmd' in query or 'open command promt' in query:
            os.system("start cmd")

        elif 'open note' in query or 'open notepad' in query:
            os.system("start cmd")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\LOGICA COM\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        #YouTube
        elif 'open youtube' in query:
            speak("What you want to search in youtube")
            search  = takeCommand().lower()
            speak("ok sir")
            if 'just open youtube' in search:
                browser_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                url = 'youtube.com'
                webbrowser.register('chrome',None, webbrowser.BackgroundBrowser(browser_path))
                webbrowser.get('chrome').open_new_tab(url)
            else:
                browser_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                search = search.replace("search", "")
                url = 'https://www.youtube.com/results?search_query=' + search
                webbrowser.register('chrome',None, webbrowser.BackgroundBrowser(browser_path))
                webbrowser.get('chrome').open_new_tab(url)

        #Google
        elif 'open google' in query:
            speak("Sir, What should I search for you ?")
            search  = takeCommand().lower()
            search = search.replace("search", "")
            speak("ok sir")
            if 'just open google' in search:
                browser_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                url = "google.com"
                webbrowser.register('chrome',None, webbrowser.BackgroundBrowser(browser_path))
                webbrowser.get('chrome').open_new_tab(url)
            else:
                webbrowser.open(f"{search}")

        #Facebook
        elif 'open facebook' in query:
            browser_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            url = "facebook.com"
            webbrowser.register('chrome',None, webbrowser.BackgroundBrowser(browser_path))
            webbrowser.get('chrome').open_new_tab(url)
            
        #Music        
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        #Date and Time        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query or 'date' in query:
            date = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
            print(date.strftime('%d %B, %Y'))
            speak("The date is")
            speak(date.strftime('%d %B, %Y'))
        
        #location
        elif 'where i am' in query or 'location' in query or 'where we are' in query:
            location()
        
        # jokes
        elif 'tell me a jokes' in query or 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        
        #send gmail
        elif 'send email' in query or 'send gmail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = input("Enter the gmail whom you want to send:\n")    
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email")

        # for terminate jarvis
        elif 'you can sleep' in query or 'sleep now' in query:
            speak("okay boss, i am going to sleep you can me anytime")
            break
        
        elif 'goodbye' in query or 'deactivate' in query:
            speak("thank for using me, have a good day")
            sys.exit()
            

if __name__=="__main__":
    while True:
        permission = takeCommand().lower()
        if 'wake up' in permission or 'activate' in permission:
            taskExecution()
        elif 'goodbye' in permission or 'deactivate' in permission:
            speak("thank for using me, have a good day")
            sys.exit()