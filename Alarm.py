import datetime
from time import sleep
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()
        self.alarm_hour = int(input("Введите час = "))
        self.alarm_min = int(input("Введите минуты = "))
        self.alarm_sec = int(input("Введите секунды = "))
        self.alarm()
    

    def alarm(self):
        while True:
            now = datetime.datetime.now()
            if self.alarm_hour == now.hour:
                if self.alarm_min == now.minute:
                    if self.alarm_sec == now.second:
                        self.set_txt("Wake up")
                        break
            timeremaining = str(self.alarm_hour - now.hour) + " : " + str(self.alarm_min - now.minute) + " : " + str(self.alarm_sec - now.second)
            self.set_txt(timeremaining)
            
            


    
    def set_txt(self, text):
        self.label.setText(text)
        self.update()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Tech With Tim")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50,50)


    def update(self):
        self.label.adjustSize()


def window():
    
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()


"""

def alarm():
    
    alarm_hour = int(input("Введите час = "))
    alarm_min = int(input("Введите минуты = "))
    alarm_sec = int(input("Введите секунды = "))
    app = QApplication(sys.argv)
    alarm_change(alarm_sec, alarm_hour, alarm_min, app)
    sys.exit(app.exec_())
    

    
def change_clock(timeremaining, app):
    
    win = QMainWindow()
    win.setGeometry(200,200,300,300) 
    win.setWindowTitle("Alarm") 
    label = QLabel(win)
    label.setText("0")
    label.move(50, 50)
    win.show()
    label.setText(timeremaining)
    


def alarm_change(alarm_sec, alarm_min, alarm_hour, app):
    while True:
        now = datetime.datetime.now()
        if alarm_hour == now.hour:
            if alarm_min == now.minute:
                if alarm_sec == now.second:
                    change_clock("Wake up !")
        
        timeremaining = str(alarm_hour - now.hour) + " : " + str(alarm_min - now.minute) + " : " + str(alarm_sec - now.second)
        #print(timeremaining)
        change_clock(timeremaining, app)
        sleep(1)

    
    

    
    


    def window(timeremaining):
        app = QApplication(sys.argv)
        win = QMainWindow()
        win.setGeometry(200,200,300,300) 
        win.setWindowTitle("Its time to wake up!") 
        label = QLabel(win)
        label.setText(timeremaining)
        label.move(50, 50)  

        win.show()
        sys.exit(app.exec_())


def main():
    alarm()
    #window()


if __name__ == "__main__":
    main()
"""