import pyttsx3
import datetime
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import random
import pywhatkit as kit
import smtplib
import sys



engine = pyttsx3.init('sapi5') # pyttsx3 provide an speeak function which convert the text to speech in engine which uses the saapi5 for windows

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




# convert text to voice

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()




  
def wishme():
    hour=int(datetime.datetime.now().hour) #jo current time hai wo aajyega
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<15:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hello , I am your friend ,how can i help you!")

#convert voice to text
def takecommand():
    # it takes microphone input from user and returns string output
    r=sr.Recognizer()
    # reconizer is a class which helps in detecting the audio
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold=1
        audio = r.listen(source)
    
    try:
        print("reconizing....")
        query=r.recognize_google(audio, language="en-in")
        print("user said:",query)
    except Exception as e:
        print(e)
        print("please say again....")
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('deekshapatel191002@gmail.com', 'rpnenxxckxfzwcke')
    server.sendmail('deekshapatel191002@gmail.com', to, content)
    server.close()




    
if __name__ == '__main__':
    wishme()
    while True:
        query=takecommand().lower()
        if"open notepad" in query:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)
        
        elif "open powerpoint" in query:
            ppath="C:\\Program Files\\Microsoft Office\\root\\Office16\POWERPNT.EXE"
            os.startfile(ppath)
        
        elif "open adobe acrobat" in query:
            apath="C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
            os.startfile(apath)
        
        elif "open word" in query:
            wpath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wpath)
        
        elif "open excel" in query:
            epath="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(epath)

        elif "open command prompt" in query:
            mpath="C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(mpath)
        
        elif "open studio code" in query:
            vpath="C:\\Users\\Deeksha Patel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vpath)

        elif "wikipedia"in query:
            speak("searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("accoridng to wikipedia..")
            print(results)
            speak(results)
        
        elif "open youtube"in query:
            webbrowser.open("youtube.com")

        elif "open google"in query:
            webbrowser.open("google.com")
        
        

         

        elif "play music" in query:
            music_dir="C:\\Users\\Deeksha Patel\\Music"  
            songs=os.listdir(music_dir)
            
            
            os.startfile(os.path.join(music_dir,random.choice(songs)))

        elif "send message"in query:
            kit.sendwhatmsg(phone_no="+91 7668793353", message="Howdy! This message will be sent instantly!",time_hour=19,time_min=1)

        elif "play songs on youtube" in query:
            kit.playonyt("see you again")   

        elif "send email to sara" in query:
            try:
                speak("what should i say?")
                content=takecommand().lower()
                to="itssara238@gmail.com"
                sendEmail(to,content)
                speak("email has been sent to sara")
            except Exception as e:
                print(e)  
                speak("sorry! i am unable to send your email")  
        
        elif "no thanks" in query:
            speak("thanks for using me , have a good day!")
            sys.exit()
        speak("do you have any other work!")
        
        
 
