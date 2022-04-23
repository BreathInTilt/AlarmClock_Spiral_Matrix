import datetime
from time import sleep
from tkinter import *
from playsound import playsound
from os import path


def timer_count(al_h, al_m, al_s):
    now = datetime.datetime.now()
    n_s = now.second
    n_m = now.minute
    n_h = now.hour
    if al_s - n_s < 0:
        al_m -= 1
        al_s += 60
    if al_m - n_m < 0:
        al_h -= 1
        al_m += 60
    timer = str(al_h-n_h) + ':' + str(al_m-n_m) + ':' + str(al_s-n_s)
    return timer






def alarm():
    alarm_hour = int(input("Введите час = "))
    alarm_min = int(input("Введите минуты = "))
    alarm_sec = int(input("Введите секунды = "))
    window = Tk()
    window.title("Alarm")
    window.geometry("600x400")
    timeremaining = StringVar()
    timelabel = Label(window, textvariable=timeremaining, anchor=CENTER, width=10, height=5, font=("Arial", 20))
    timeremaining.set("Tap to update")
    timelabel.grid(column=60, row=100)

    def count_down():
     while True:
        
        now = datetime.datetime.now()
        
        if alarm_hour == now.hour:
            if alarm_min == now.minute:
                if alarm_sec == now.second:
                    timeremaining.set("Wake up!")
                    path2 = path.dirname(path.abspath(__file__))
                    playsound(path2 + "\\rota_podeoom.mp3")
                    break
        timeremaining.set(timer_count(alarm_hour, alarm_min, alarm_sec))
        sleep(0.5)
        window.update()

            
    
    Button(window, text="Tap", command=count_down, height=5, width=5).grid(column=150, row=200)  
    window.mainloop()
    

alarm()
