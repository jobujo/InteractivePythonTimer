#!/usr/bin/python3
from tkinter import *
import tkinter.messagebox
import json
import hashlib
root = Tk()
def ChangeData(whatstage):
    stage=("Stage {}".format(whatstage))
    def writeData():
        setTime=changetimer.get()
#        setDescription=description_1.get()
        with open("TimeData.json", "r") as timedata:
            json_data=json.load(timedata)
            json_data[stage]["time"]=setTime
#            json_data[stage]["Description"]=setDescription
        with open("TimeData.json","w") as timedata:
            timedata.write(json.dumps(json_data))
    def MessageBox():
        passthis=changetimer.get()
        answer=tkinter.messagebox.askquestion("Make Changes","Are you sure you want to change this timer to {} seconds?".format(passthis))
        if answer=="yes":
#            print(passthis)
            writeData()
            tkinter.messagebox.showinfo("Updated","Time Updated To: [{}] seconds.".format(changetimer.get()))
            window.withdraw()
    window=Toplevel(root)
    window.title("Edit {}".format(stage))
    title=Label(window,text="Please enter the time in seconds!")
    title.grid(row=0)
    text=Label(window,text="Enter Time")
    text.grid(row=1)
    changetimer=Entry(window)
    changetimer.grid(row=1,column=1)
#    text1 = Label(window,text="Enter Description")
#    text1.grid(row=2)
#   description_1=Entry(window)
#   description_1.grid(row=2,column=1 )
    submitBtn = Button(window,text="Submit Change",command = MessageBox)
    submitBtn.grid(row=3)
def ShowCurrentTimes():
    with open("TimeData.json", "r") as timedata:
        json_data=json.load(timedata)
    window=Toplevel(root)
    window.title("Show Info!")
    r = 0
    for i in range(1,11):
        stage = ("Stage {}".format(i))
        tkinter.Label(window,text="{}".format(stage),relief=tkinter.RIDGE,width=10,height=2).grid(row=r,column=0)
        tkinter.Label(window,text="Time:{}sec".format(json_data[stage]["time"]),relief=tkinter.RIDGE,height=2,width=15).grid(row=r,column=1)
        r += 1
def pickstage():
    Stage1=Button(root,text="Stage 1",height=5,width=20,command=lambda:ChangeData(1))
    Stage1.grid(row=0)
    Stage2=Button(root,text="Stage 2",height=5,width=20,command=lambda:ChangeData(2))
    Stage2.grid(row=0,column=1)
    Stage3=Button(root,text="Stage 3",height=5,width=20,command=lambda:ChangeData(3))
    Stage3.grid(row=1,)
    Stage4=Button(root,text="Stage 4",height=5,width=20,command=lambda:ChangeData(4))
    Stage4.grid(row=1,column=1)
    Stage5=Button(root,text="Stage 5",height=5,width=20,command=lambda:ChangeData(5))
    Stage5.grid(row=2)
    Stage6=Button(root,text="Stage 6",height=5,width=20,command=lambda:ChangeData(6))
    Stage6.grid(row=2,column=1)
    Stage7=Button(root,text="Stage 7",height=5,width=20,command=lambda:ChangeData(7))
    Stage7.grid(row=3)
    Stage8=Button(root,text="Stage 8",height=5,width=20,command=lambda:ChangeData(8))
    Stage8.grid(row=3,column=1)
    Stage9=Button(root,text="Stage 9",height=5,width=20,command=lambda:ChangeData(9))
    Stage9.grid(row=4)
    Stage10=Button(root,text="Stage 10",height=5,width=20,command=lambda:ChangeData(10))
    Stage10.grid(row=4, column=1)
    ShowTimers=Button(root,text="Show Current Timers",height=5,width=43,command=lambda:ShowCurrentTimes())
    ShowTimers.grid(row=5,columnspan=2)
def PasswordProtection():
    GPassword=Password.get()
    hashPassword=hashlib.md5(GPassword.encode())
    HexPassword=hashPassword.hexdigest()
    thepassword="9226517c71b3f7b312731720cee72f76"
    if HexPassword==thepassword:
        pickstage()
        root.title("ATI Edit Timers")
    else:
        tkinter.messagebox.showinfo("Error: Invalid Password", "Invalid Password")
root.title("ATI Login")
text = Label(root,text="Please Enter The Password")
text.grid(row=0)
Password = Entry(root,show="*")
Password.grid(row=1)
submitButton = Button(root,text="Submit",command = PasswordProtection)
submitButton.grid(row=2)
root.mainloop()
