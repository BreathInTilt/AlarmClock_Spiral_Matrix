import datetime
from time import sleep
from tkinter import *
from playsound import playsound
from os import path
from threading import Thread





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
    if al_h - n_h < 10:   a = "0" + str(al_h - n_h)
    else:   a = str(al_h - n_h)
    if al_m - n_m < 10:   b = "0" + str(al_m - n_m)
    else:   b = str(al_m-n_m)
    if al_s - n_s < 10:   c = "0" + str(al_s - n_s)
    else:   c = str(al_s - n_s)
    timer = a + ':' + b + ':' + c
    return timer

def sound():
    path2 = path.dirname(path.abspath(__file__))
    playsound(path2 + "\\rota_podeoom.mp3")

def valuecheck(al_h, al_m, al_s):
    s = al_h + al_m + al_s    
    for i in s:
        if 46 > ord(i) or ord(i) > 57:
            return False
    return True
    


def time_check(al_h, al_m, al_s):
    al_h = int(al_h)
    al_m = int(al_m)
    al_s = int(al_s)
    now = datetime.datetime.now()
    if 24 > al_h > now.hour:
        if 60 > al_m > 0:
            if 60 > al_s > 0:
                return True
    elif 24 > al_h == now.hour:
        if 60 > al_m > now.minute:
            if 60 > al_s > now.second:
                return True
    return False





def get_alarm():
    window = Tk()  
    window.title("Input")  
    window.geometry('400x250')  
    lbl = Label(window, text="Будильник:")
    lbl.grid(column=0, row=0)
    txt_h = Entry(window,width=10)
    txt_h.grid(column=0, row=10)
    txt_m = Entry(window,width=10)
    txt_m.grid(column=0, row=20)
    txt_s = Entry(window,width=10)
    txt_s.grid(column=0, row=30)

    def cleanup():
        btn.destroy()
        lbl.destroy()
        txt_h.destroy()
        txt_m.destroy()
        txt_s.destroy()


    def clicked():
        al_h, al_m, al_s = txt_h.get(), txt_m.get(), txt_s.get()
        if valuecheck(al_h, al_m, al_s) and time_check(al_h, al_m, al_s):
            cleanup()
            alarm(int(al_h), int(al_m), int(al_s), window)
        else:
            lbl.configure(text="Введите корректное значение!")

    btn = Button(window, text="Старт!", command=clicked)
    btn.grid(column=2, row=10)

    window.mainloop()




def alarm(alarm_hour, alarm_min, alarm_sec, window):
    #alarm_hour = int(input("Введите час = "))
    #alarm_min = int(input("Введите минуты = "))
    #alarm_sec = int(input("Введите секунды = "))
    
    timeremaining = StringVar()
    timelabel = Label(window, textvariable=timeremaining, anchor=CENTER, width=10, height=5, font=("Arial", 20)) #Design
    timeremaining.set("Tap to update")
    timelabel.grid(column=60, row=10)   #Design

    def count_down():
     while True:
        now = datetime.datetime.now()
        
        if alarm_hour == now.hour:
            if alarm_min == now.minute:
                if alarm_sec <= now.second:
                    timeremaining.set("Wake up!")
                    Thread(target = sound, daemon=True).start()
                    break
        timeremaining.set(timer_count(alarm_hour, alarm_min, alarm_sec))
        sleep(0.5)
        window.update()

            
    
    Button(window, text="Tap", command=count_down, height=5, width=5).grid(column=150, row=200)  #Design
    

#alarm()
get_alarm()