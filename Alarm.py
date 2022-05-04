import datetime
from time import sleep
from tkinter import *
from playsound import playsound
from os import path
from threading import Thread



<<<<<<< HEAD
class Alarm:

    def __init__(self):
        self.path2 = path.dirname(path.abspath(__file__))
        self.window = Tk()  
        self.window.title("Input")  
        self.window.geometry('480x480')
        self.window["background"] = "blue"
        self.lbl = LabelFrame(self.window, text="Будильник:")
        self.lbl.pack(side=TOP)
        self.lbl.grid(column=0, row=0)
        self.label_h = Label(self.window, text="Часы:", bg="blue", font=("OpenSansBold", 14), fg="white")
        self.label_h.place(x=5, y=20)
        self.txt_h = Entry(self.window,width=10)
        self.txt_h.place(x=95, y=25)
        self.label_m = Label(self.window, text="Минуты:", bg="blue", font=("OpenSansBold", 14), fg="white")
        self.label_m.place(x=5, y=45)
        #txt_h.grid(column=10, row=10).pack
        self.txt_m = Entry(self.window,width=10)
        self.txt_m.place(x=95, y=50)
        #txt_m.grid(column=10, row=20)
        self.label_s = Label(self.window, text="Секунды:", bg="blue", font=("OpenSansBold", 14), fg="white")
        self.label_s.place(x=5, y=70)
        self.txt_s = Entry(self.window,width=10)
        self.txt_s.place(x=95, y=75)
        img = PhotoImage(file = self.path2 + "\\gobtn.png")    
        self.btn = Button(self.window, command=self.clicked, image=img, width=100, height=100)
        self.btn.place(x = 180, y = 25)
        self.timelabel = Label(self.window, bg="blue", anchor=CENTER, width=10, height=5, font=("OpenSansBold", 14), fg="white")
        #btn.image = img
        #self.warn = LabelFrame(self.window)
        #self.warn.pack(side=BOTTOM)
        self.window.mainloop()
        
    def valuecheck(self):
        s = self.al_h + self.al_m + self.al_s    
        for i in s:
            if 46 > ord(i) or ord(i) > 57:
                return False
        return True
        


    def time_check(self):
        self.al_h = int(self.al_h)
        self.al_m = int(self.al_m)
        self.al_s = int(self.al_s)
        now = datetime.datetime.now()
        if 24 > self.al_h > now.hour:
            return True
        elif 24 > self.al_h == now.hour:
            if 60 > self.al_m > now.minute:
                return True
        return False

    def clicked(self):
        self.al_h, self.al_m, self.al_s = self.txt_h.get(), self.txt_m.get(), self.txt_s.get()
        if self.valuecheck():
            if self.time_check():
                self.cleanup()
                self.timelabel = Label(self.window, text="Tap to update", anchor=CENTER, width=10, height=5, font=("OpenSansBold", 20),fg="white" , bg="blue") #Design
                self.timelabel.grid(column=100, row=60)   #Design
                self.count_down()
            else:
                self.lbl.configure(text="Введите корректное значение!")
        else:
            self.lbl.configure(text="Введите корректное значение!")

    def time_set(self):
        
        now = datetime.datetime.now()
        n_s = now.second
        n_m = now.minute
        n_h = now.hour
        alarm_sec = self.al_s
        alarm_min = self.al_m
        alarm_hour = self.al_h
        if alarm_sec - n_s < 0:
            alarm_min -= 1
            alarm_sec += 60
        if alarm_min - n_m < 0:
            alarm_hour -= 1
            alarm_min += 60
        if alarm_hour - n_h < 10:   a = "0" + str(alarm_hour - n_h)
        else:   a = str(alarm_hour - n_h)
        if alarm_min - n_m < 10:   b = "0" + str(alarm_min - n_m)
        else:   b = str(alarm_min - n_m)
        if alarm_sec - n_s < 10:   c = "0" + str(alarm_sec - n_s)
        else:   c = str(alarm_sec - n_s)
        timer = a + ':' + b + ':' + c
        return timer


    def count_down(self):
        while True:
            now = datetime.datetime.now()
                
            if self.al_h == now.hour:
                if self.al_m == now.minute:
                    if self.al_s <= now.second:
                        #self.timeremaining.set("Wake up!")
                        self.timelabel.config(text="Wake up!")
                        Thread(target = self.sound, daemon=True).start()
                        break
            self.timelabel.config(text=self.time_set())
            sleep(0.5)
            self.window.update()
                    

    def cleanup(self):
        self.label_h.destroy()
        self.label_m.destroy()
        self.label_s.destroy()
        self.btn.destroy()
        self.lbl.destroy()
        self.txt_h.destroy()
        self.txt_m.destroy()
        self.txt_s.destroy()

    def sound(self):
        playsound(self.path2 + "\\rota_podeoom.mp3")

    def alarm(self):
        self.timelabel.place(x=10, y=10)
        self.count_down()
        #self.time_set()


Alarm()
>>>>>>> testing
