import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as whats
import sys
import time
import pyjokes
# from PySide2.QtCore
# from PySide2.QtGui
# from PySide2.QtWidgets
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QTimer, QTime, QDate,Qt
from PySide2.QtGui import QMovie
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import loadUiType
from jarvisUi import Ui_MainWindow






engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

#text to speech 
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)# Gives Current time
    tt = time.strftime("%r")
    if hour>=0 and hour<=12:
        speak(f"Good Morning, it's {tt}")
    elif hour>12 and hour<=18:
        speak(f"Good Afternoon, it's {tt}")
    else:
        speak(f"Good Evening Captain, it's {tt}")
    speak(" The heem Sir, how can i help you today")



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.start
    #voice to text
    def takecommand(self):

        r = sr.Recognizer()
        with sr.Microphone() as source: #Microphone will work as sourse(it will take command)
            print("listning...") #if it's listning or not
            r.pause_threshold = 1 #robo should not stop listning if user stops for a while.
            audio = r.listen(source,timeout=0,phrase_time_limit=5)
        
        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language = "en-in")
            print(f"User said: {self.query}")
        

        except Exception as e: #if robo cannot understand the speech
            speak("Sorry, say that again")
            return "none"
        return self.query

        # Task execution
    def start(self):
        wish()
        xy = 1
        while xy >0:
            self.query = self.takecommand().lower()
            xy= xy-1
            if"open notepad" in self.query:
                npath="C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif"close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")


            elif"open chrome" in self.query:
                gcpath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(gcpath)
            elif"close chrome" in self.query:
                speak("okay sir, closing chrome")
                os.system("taskkill /f /im chrome.exe")

            elif"open command prompt" in self.query:
                cmdpath="C:\\WINDOWS\\system32\\cmd.exe"
                os.startfile(cmdpath)
            elif"close command prompt" in self.query:
                speak("okay sir, closing command prompt")
                os.system("taskkill /f /im command prompt.exe")

            elif"open my project" in self.query:
                gcpath="C:\\Users\\dm555\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
                os.startfile(gcpath)    

            elif"open camera" in self.query:
                cap= cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow("webcam",img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
            elif"introduce yourself" in self.query:
                music_dir ="C:\\Users\\dm555\\Music\\jarvis intro"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))

            elif"IP address" in self.query:
                ip = get("https://api.ipify.org").text
                speak(f"your ip address is {ip}")

            elif"tell me about" in self.query:
                speak("collecting information about your query")
                query = query.replace("tell me", " ")
                results = wikipedia.summary(query, sentences=1)
                speak("According to me")
                speak(results)
                print(results)

            elif"what is synthetic reality" in self.query:
                webbrowser.open("https://youtu.be/oxXpB9pSETo")
            elif"who is my brother" in self.query:
                webbrowser.open("https://www.instagram.com/p/CfjV0aQPMGg/?utm_source=ig_web_copy_link")
            
            # elif"freak me out" in query:
            #     cap=cv2.VideoCapture("videos1/synthetic reality.mp4")
            #     while(cap.isOpened()):
            #         ret,frame = cap.read()
            #         frame = cv2.resize(frame,(1200,900))
            #         cv2.imshow("video",frame)
            #         if cv2.waitKey(10) & 0xff == ord('q'):
            #             break
            #     cap.relese()
            #     cap.destroyAllWindows()
            elif"open google" in self.query:
                speak("What should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}") 

            elif "send my salam" in self.query:
                whats.sendwhatmsg("+919596780440", "Asalam Mu Alaikum Soliha", 10,31)

            elif"sleep now" in self.query: 
                speak("Thanks for using me sir, have a good day")   
                sys.exit()
            
            elif"set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn== 22:
                    webbrowser.open("https://youtu.be/oxXpB9pSETo")

            elif"tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)





            speak("do you have any other work")

startExecution = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

        def startTask(self):
            self.ui.movie = QtGui.QMovie("images/RBte.gif")
            self.ui.label.setMovie(self.ui.movie)
            self.movie.start()
            self.ui.movie = QtGui.QMovie("images/XDZT.gif")
            self.ui.label_2.setMovie(self.ui.movie)
            self.movie.start()
            startExecution.start()
app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

# if __name__ == "__main__":
#     start()
    # takecommand() 
    # speak("hello sir")
    