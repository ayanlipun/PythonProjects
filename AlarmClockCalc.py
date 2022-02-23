# Importing required libraries to make the application
from tkinter import *       #helps us to create a dialog box with any information
import datetime             #work with the dates and time of the current day
import time                 #import datetime   #work with the dates and time of the current day
import winsound             #access to the basic sound playing machinery provided by Windows platforms


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        currentTime =datetime.datetime.now()
        now= currentTime.strftime("%H:%M:%S")
        date=currentTime.strftime("%d/%m/%Y")
        print("The set date is:",date)
        print(now)

        if now ==set_alarm_timer:
            print("Time t wake up!")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

def actual_time():
    set_alaram_timer= f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alaram_timer)

#Creating GUI

clock =Tk()

clock.title("AR2 alarm clock")
clock.geometry("500x250")
timeFormat = Label(clock, text="Please enter a time in 24 hour format.",fg="red",bg="black",font="Calibri").place(x=60,y=120)
addTime =Label(clock,text="Hour Min Sec",font=60).place(x=110)
setYourAlarm = Label(clock,text="Set your wake up time!",fg="blue",relief="solid",font=("Helevetica",7,"bold")).place(x=0,y=29)

#Variable required to set the alarm
hour  = StringVar()
min = StringVar()
sec =   StringVar()

#Time required to set the alarm clock:

hourTime =Entry(clock,textvariable=hour,bg="pink",width=15).place(x=110,y=30)
minTime = Entry(clock,textvariable=min,bg="pink",width=15).place(x=150,y=30)
secTime = Entry(clock,textvariable=sec,bg="pink",width=15).place(x=200,y=30)

#Take time from user:
submit= Button(clock,text="Set Alarm",fg="red",width=10,command = actual_time).place(x=100,y=70)

clock.mainloop()