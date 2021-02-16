import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
from gtts import gTTS
import playsound
import os
import subprocess ,sys
import smtplib
import time
import cv2
import dlib

# engine = pyttsx3.init()
# voices = engine.setProperty("voices")
# engine.setProperty("voice",voices[1].id)
def open_Cam():
    video = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()

    while True:
        ret , frame = video.read()
        frame = cv2.flip(frame,1)

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        num = 0
        for face in faces:
            x,y = face.left() , face.top()
            hi,wi = face.right() , face.bottom()
            cv2.rectangle(frame,(x,y),(hi,wi),(0,0,255),2)
            num = num+1

            cv2.putText(frame,"face"+str(num),(x-5,y-12),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)

        cv2.imshow("faces",frame)

        if cv2.waitKey(1) == 27:        
            break
    video.release()
    cv2.destroyAllWindows()
        
def speak(text):
    tts = gTTS(text=text,lang="en",slow=False)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    # engine.say(audio)
    # engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning!")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon!")
    else: 
        speak("Good Evening!") 
    speak("My name is Alice. I am creater by bilal Khan. Please tell me. how may i help you")
    
def takeCommad():
    # it takes microphone input user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gamil.com","your-passworld-here")
    server.sendmail("youremail@gmail.com",to,content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    while True:
    # if True:
        query = takeCommad().lower()
        # Logic for executing tasks base on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            speak("opening Youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif "open facebook" in query:
            speak("opening facebook ")
            webbrowser.open("facebook.com")

        elif "open instagram" in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")

        elif "who are you" in query:
            speak("My name is Alice. I am virtual Assistan programmed in python")

        elif "are you single" in query:
            speak("I am in relationship with my code")

        elif "thanks" in query:
            speak("you are welcome sir")
            
        elif "joke" in query:
            speak(pyjokes.get_joke())

        elif "play music" in query:
            music_dir = "/home/bilal/Downloads/songs/rockstar.mp3"
            # songs = os.listdir(music_dir)
            # print(songs)
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, music_dir])
            #os.startfile(os.path.join(music_dir,songs[0]))

        elif "play" in query:
            song = query.replace("play","")
            speak("playing song")
            pywhatkit.playonyt(song)

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir the time is {strTime}")

        elif "open code" in query:
            speak("opening code")
            codePath = "/home/bilal/Desktop/code.desktop"
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, codePath])

        elif "date" in query:
            speak("Sorry I am a Robot. you can not go on date with me")
        
        elif "open camera" in query:
            speak("opening camera")
            time.sleep(0.1)
            speak("you can press escape key to exit the camera")
            open_Cam()
        elif "email to bilal" in query:
            try:
                speak("what should i say ")
                content = takeCommad()
                to = "yourEmail@gmail.com"
                sendEmail(to,content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak('Sorry Sir. I am not able to send this email ')

        elif "close the program" in query:
            speak("closing the virtual system")
            time.sleep(0.1)
            speak("have a nice day Sir.")
            time.sleep(0.1)
            speak("Alice is signing Out now")
            sys.exit()
    


        

            
            






