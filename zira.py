
import pyttsx3
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
import smtplib
sr.__version__
chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)#used to know which vocies are available
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis!How may I help you!")

def takeCommand():
    #it takes microphone input from the user and converts into string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold= 1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('camtam1710@gmail.com','akanksha')
    server.sendmail("camtam1710@gmail.com", to, content)
    server.close()




if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query=query.replace("wikipedia","")
            results =wikipedia.summary(query,sentences=2)
            speak("Acoording to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube'in query:
            #webbrowser.open("youtube.com")
            r1=sr.Recognizer()
            url='https://www.youtube.com/results?search_query='
            with sr.Microphone() as source1:
                speak("What would you like to search!")
                audio1=r1.listen(source1)
                try:
                    get=r1.recognize_google(audio1,language='en-in')
                    webbrowser.get(chrome_path).open(url+get)
                except sr.UnknownValueError:
                    print('Error')
                except sr.RequestError as e:
                    print('failed'+format(e))


        elif 'open google'in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow'in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music'in query:
            music_dir='C:\\Users\\AKANKSHA\\Videos\\songs\\Songs'
            songs =os.listdir(music_dir)
            num=random.randint(3,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[num]))
        elif 'the time'in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")

        elif 'open code' in query:
            codePath="C:\\Users\\AKANKSHA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak("what should I say?")
                content= takeCommand()
                to="camtam1710@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send email")
        elif 'quit' in query:
            exit()
        




