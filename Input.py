#import datetime
from tkinter import *
#from os import path



def get_alarm():
    window = Tk()  
    window.title("Input")  
    window.geometry('400x250')  
    lbl = Label(window, text="Будильник:")
    lbl.grid(column=0, row=0)
    lbl_h = Label(window, text="Ввёдённые часы:")
    lbl_h.grid(column=0, row=80)
    lbl_m = Label(window, text="Ввёдённые минуты:")
    lbl_m.grid(column=0, row=90)
    lbl_s = Label(window, text="Будильник секунды:")
    lbl_s.grid(column=0, row=100)
    txt_h = Entry(window,width=10)
    txt_h.grid(column=5, row=10)
    txt_m = Entry(window,width=10)
    txt_m.grid(column=5, row=20)
    txt_s = Entry(window,width=10)
    txt_s.grid(column=5, row=30)


    def clicked_h():
        hours = "Ввёдённые часы: {}".format(txt_h.get())
        lbl_h.configure(text=hours)
        lbl_h.Adjustsize()
    def clicked_m():
        minute = "Ввёдённые минуты: {}".format(txt_m.get())
        lbl_m.configure(text=minute)
        lbl_m.Adjustsize()
    def clicked_s():
        second = "Ввёдённые секунды: {}".format(txt_s.get())
        lbl_s.configure(text=second)
        lbl_s.Adjustsize()

    
    btn = Button(window, text="Ввести", command=clicked_h)  
    btn.grid(column=11, row=10)
    btn = Button(window, text="Ввести", command=clicked_m)  
    btn.grid(column=11, row=20)  
    btn = Button(window, text="Ввести", command=clicked_s)  
    btn.grid(column=11, row=30)    
    window.mainloop()


get_alarm()
    