import datetime
import speech_recognition as sr
import os
import webbrowser
import wikipedia
import random
import re
c=[]
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.speak(str)

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good morning sir".upper())
        speak("Good morning sir")

    elif hour>=12 and hour<22:
        print("Good afternoon sir".upper())
        speak("Good afternoon sir")

    else:
        print("Good night sir")
        speak("Good night sir".upper())

    print("I am jarvis sir..,please tell me how may i help you")
    speak("I am jarvis sir.., please tell me how may i help you")

def takecommand():
   r=sr.Recognizer()
   with sr.Microphone() as source:
       print("Listening...")
       r.pause_threshold=0.5
       audio=r.listen(source)
   try:
       print("Recognize...")
       quary=r.recognize_google(audio,language='en-in')
       print(f"you say \"{quary}\"")
   except Exception as e:
       print("say that again please...")

       return 'say again'
   return quary

             

        
       
def call():
            w=takecommand()
            if(w=='again say'):
                 exit()
            else:
                return w

def again_call():
    a=takecommand()
    if a=='say again':
        exit()
    else:
       return a
                        
def add_item():
              
            for i in range(1,100):
                    print(f"item: {i}..")
                    q=takecommand()
                    if(q=='again say'):
                        speak('say again')
                        print("say again")
                        p=call()
                        speak(p)
                        c.append(p)
                        print(c)
                        speak(q)
                    else:
                         c.append(q)
                         print(c)
                         speak(q)
                                
                   
def wiki_s():
            result=wikipedia.summary(quary,sentences=2)
            print(result)
            speak(result)
            exit()

def music():

           
            music_dir='C:\\Users\\agraw\\OneDrive\\Desktop\\ss'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randrange(2)]))
            exit()

def show_time():
            
            time=datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(f"sir your time {time}")
            exit()

            
def fun_quit():
    exit()
    
if __name__ == '__main__':
            wish()
            quary = takecommand().lower()
        
            if  quary==('add item') or quary==('item'):
                speak(quary)
                add_item()
                exit()
            elif quary=='wikipedia':
                 speak(quary)
                 wiki_s()
                 exit()
               
            elif  quary==('the time') or quary==('time'):
                  speak(quary)
                  show_time()
                  exit()
            elif  quary==('play music') or quary==('play song'):
                  speak(quary)
                  music()
                  exit()
            elif quary==("quit") or quary==("exit"):
                 speak(quary)
                 fun_quit()
                 exit()      
                        
            elif     quary=='say again':
                     print('say again ')
                     speak(quary)
                     p=again_call()
                     if  p==('add item') or p==('item'):
                         speak(P)
                         add_item()
                         exit()
                    
                     elif  p==('play music')or p==('play song'):
                           speak(P)
                           music()
                           exit()
                     elif  p==('the time') or p==('time'):
                           speak(P)
                           show_time()
                           exit()

                     elif p==('quit') or p==('exit'):
                          speak(P)
                          fun_quit()
                          exit()
                     elif  p== ('wikipedia'):
                           wiki_s()
                           speak(P)
                           exit()     
                     else:
                            webbrowser.open(f"{p}")
                            exit()
            
            else:
                  speak(quary)
                  webbrowser.open(f'{quary}')
                  exit()



