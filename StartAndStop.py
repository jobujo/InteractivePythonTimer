#!/usr/bin/python3
#    _                       _       _           _ 
#   / \   ___ ___  ___   ___(_) __ _| |_ ___  __| |
#  / _ \ / __/ __|/ _ \ / __| |/ _` | __/ _ \/ _` |
# / ___ \\__ \__ \ (_) | (__| | (_| | ||  __/ (_| |
#/_/   \_\___/___/\___/ \___|_|\__,_|\__\___|\__,_|
#                                                  
# _____ _                                __                      _             
#|_   _| |__   ___ _ __ _ __ ___   ___  / _| ___  _ __ _ __ ___ (_)_ __   __ _ 
#  | | | '_ \ / _ \ '__| '_ ` _ \ / _ \| |_ / _ \| '__| '_ ` _ \| | '_ \ / _` |
#  | | | | | |  __/ |  | | | | | | (_) |  _| (_) | |  | | | | | | | | | | (_| |
#  |_| |_| |_|\___|_|  |_| |_| |_|\___/|_|  \___/|_|  |_| |_| |_|_|_| |_|\__, |
#                                                                        |___/ 
# ___              
#|_ _|_ __   ___   
# | || '_ \ / __|  
# | || | | | (__ _ 
#|___|_| |_|\___(_)
#
#-----About-----
# Creator: Joshua Bunce
# Email: joshua.bunce@outlook.com
# Purpose: This code was developed for ATI(Associated Thermoforming INC.)
#   -This was designed to be one of two programs for their timer.
#   -The first of the two programs is the GUI that wil allow them to change the timers.
#   -The second is to calculate their times for each stage. Then will allow them to
#    run the time and light up the LED's on the front.
#-----Descriptions-----
#1a: This was not desired but had to happen. Due to using "global x" inside of a def and if x is a parameter then
#    this will result in an error. So to keep from repeating the CalculateAndStartTimer function for all 10 timers#    I just set the global variables in a fucntion and called them as needed.
#1a: Light Action
#   -This is Defining a function called Action:
#       -When the the timer reaches it desired timer number it will tuen the LED on.
#
#2a Starting Timer
#   -This is using the "threading" library to start the timer. 
#   -timer=threading.Timer(time, PrintH)
#                           ^       ^
#                           |       |_______
#                Seconds for the timer      |
#                                           |
#                       What happens when the timer reaches the end? In this case it
#                       is calling the funtion PrintH. Which will print "hello".
#
#3a Calculating the Times and executing the timers
#   -Because all the times are only how long each stage individual stage is we need to add all
#    the times together. For example, if Stage 1 is 10 seconds long and Stage 2 is 20 seconds long
#    we need to add Stage 1 + Stage 2 and get that Stage 2 will be 30 seconds So when they are all
#    started Stage 2 will be finish 20 seconds after Stage 1 and not 10 seconds after Stage 1.
#4a This is a function that will run all timers 1 through 10!

#-----Import Essentials-----
import threading
import json
import tkinter.messagebox
from tkinter import *
#import RPi.GPIO as GPIO
#----Predefine Variables----
stage1=None
stage2=None
stage3=None
stage4=None
stage5=None
stage6=None
stage7=None
stage8=None
stage9=None
stage10=None
#---Open the json file "TimeData.json" for reading of the data. The TimeData.json is where the ChangeTimer Programstores the data that will be accessd by this program. 
with open("TimeData.json", "r") as timedata:
    json_data = json.load(timedata)
#---Description at 1a---
def stage1stop(timerdata):
    global stage1
    stage1 = timerdata
def stage2stop(timerdata):
    global stage2
    stage2 = timerdata
def stage3stop(timerdata):
    global stage3
    stage3 = timerdata
def stage4stop(timerdata):
    global stage4
    stage4 = timerdata
def stage5stop(timerdata):
    global stage5
    stage5 = timerdata
def stage6stop(timerdata):
    global stage6
    stage6 = timerdata
def stage7stop(timerdata):
    global stage7
    stage7 = timerdata
def stage8stop(timerdata):
    global stage8
    stage8 = timerdata
def stage9stop(timerdata):
    global stage9
    stage9 = timerdata
def stage10stop(timerdata):
    global stage10
    stage10 = timerdata
#-----Description at 1a-----
def PrintH():
    print("HELLO")
#-----Description at 2a-----
def StopTimer():
    stage1.cancel()
    stage2.cancel()
    stage3.cancel()
    stage4.cancel()
    stage5.cancel()
    stage6.cancel()
    stage7.cancel()
    stage8.cancel()
    stage9.cancel()
    stage10.cancel()
#-----Description at 3a-----
def CalcAndStartTimer(fromthis,tothis,wstage,tstage):
    CalculatedTimeSum=0
    for stagerange in range(fromthis,tothis):
        stage="Stage {}".format(stagerange)
        timedata=int(json_data[stage]["time"])
        CalculatedTimeSum+=timedata
#    StartTimer(CalculatedTimeSum,stage)
    wstage=threading.Timer(CalculatedTimeSum,PrintH)
    tstage(wstage)
    wstage.start()
#    GPIO.output(LEDPIN, GPIO.HIGH)
#-----Description at 4a-----
def StartAll():
    #-----Timer1-----
    CalcAndStartTimer(1,2,stage1,stage1stop)
    #-----Timer2-----
    CalcAndStartTimer(1,3,stage2,stage2stop)
    #-----Timer3-----
    CalcAndStartTimer(1,4,stage3,stage3stop)
    #-----Timer4-----
    CalcAndStartTimer(1,5,stage4,stage4stop)
    #-----Timer5-----
    CalcAndStartTimer(1,6,stage5,stage5stop)
    #-----Timer6-----
    CalcAndStartTimer(1,7,stage6,stage6stop)
    #-----Timer7-----
    CalcAndStartTimer(1,8,stage7,stage7stop)
    #-----Timer8-----
    CalcAndStartTimer(1,9,stage8,stage8stop)
    #-----Timer9-----
    CalcAndStartTimer(1,10,stage9,stage9stop)
    #-----Timer10-----
    CalcAndStartTimer(1,11,stage10,stage10stop)
root=Tk()
root.title("ATI Timer Interface")
text = Label(root,text="Hit Start to start timer")
text.grid(row=0)
startbtn = Button(root,text = "Start Timer",command=StartAll)
startbtn.grid(row=2)
stopbtn=Button(root,text="Stop Timer",command=StopTimer)
stopbtn.grid(row=3)
root.mainloop()
