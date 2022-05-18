import datetime
from time import sleep
from tkinter import *
from playsound import playsound
from os import path
from threading import Thread
from PIL import ImageTk, Image


class Alarm:
    def __init__(self):
        self.path2 = path.dirname(path.abspath(__file__))
        self.window = Tk()
        self.window.title("Будильник")
        self.window.maxsize(width= 999, height = 562)
        self.window.minsize(width= 999, height = 562)
        img2 = PhotoImage(file=self.path2+'\\background.png')
        self.bckgr = Label(self.window, image=img2)
        self.bckgr.place(x = 0, y = 0)
        self.lbl = LabelFrame(self.window, text="Будильник:")
        self.lbl.pack(side=TOP)
        self.lbl.grid(column=0, row=0)
        self.label_h = Label(self.window, text="Часы:", bg="#171c33", font=("OpenSansBold", 14), fg="white")
        self.label_h.place(x=5, y=20)
        self.txt_h = Entry(self.window, width=10)
        self.txt_h.place(x=95, y=25)
        self.label_m = Label(self.window, text="Минуты:", bg="#171c33", font=("OpenSansBold", 14), fg="white")
        self.label_m.place(x=5, y=45)
        self.txt_m = Entry(self.window, width=10)
        self.txt_m.place(x=95, y=50)
        self.label_s = Label(self.window, text="Секунды:", bg="#171c33", font=("OpenSansBold", 14), fg="white")
        self.label_s.place(x=5, y=70)
        self.txt_s = Entry(self.window, width=10)
        self.txt_s.place(x=95, y=75)
        img = PhotoImage(file=self.path2 + "\\under_the_grib.png")
        self.bp = Image.open(self.path2 + "\\wakeup.png")
        self.bp = self.bp.resize((999, 562))
        self.wakeup = ImageTk.PhotoImage(self.bp)
        self.btn = Button(self.window, command=self.clicked, image=img, width=260, height=150)
        self.btn.place(x=180, y=25)
        
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
                self.timelabel = Label(
                self.window, 
                width=10,
                height=5,
                font=("OpenSansBold", 16), 
                fg="#F2B6CA",
                bg="#686b9f")
                self.timelabel.place(x=620, y=140)
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
        if alarm_hour - n_h < 10:
            a = "0" + str(alarm_hour - n_h)
        else:
            a = str(alarm_hour - n_h)
        if alarm_min - n_m < 10:
            b = "0" + str(alarm_min - n_m)
        else:
            b = str(alarm_min - n_m)
        if alarm_sec - n_s < 10:
            c = "0" + str(alarm_sec - n_s)
        else:
            c = str(alarm_sec - n_s)
        timer = a + ':' + b + ':' + c
        return timer

    def count_down(self):
        while True:
            now = datetime.datetime.now()

            if self.al_h == now.hour:
                if self.al_m == now.minute:
                    if self.al_s <= now.second:
                        self.timelabel.destroy()
                        self.bckgr.config(image=self.wakeup)
                        Thread(target=self.sound, daemon=True).start()
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
        playsound(self.path2 + "\\narutoop.wav")



Alarm()