import datetime


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

alarm()