import datetime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

def alarm():
    alarm_hour = int(input("Введите час = "))
    alarm_min = int(input("Введите минуты = "))
    alarm_sec = int(input("Введите секунды = "))
    
    while True:
        now = datetime.datetime.now()
        if alarm_hour == now.hour:
            if alarm_min == now.minute:
                if alarm_sec == now.second:
                    print("Подъем!!!")
                    print("Подъем!!!")
                    print("Подъем!!!")
                    window()
                    break


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300) 
    win.setWindowTitle("Its time to wake up!") 
    
    label = QLabel(win)
    label.setText("Wake up")
    label.move(50, 50)  

    win.show()
    sys.exit(app.exec_())


def main():
    alarm()
    #window()


if __name__ == "__main__":
    main()