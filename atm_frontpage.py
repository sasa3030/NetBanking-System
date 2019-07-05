from tkinter import *
import os
from atm_tasks import tasks
from atm_signup import signup

root=Tk()
root.config(bg="cyan")
root.geometry("1500x1500")
f1=Frame(root,bg="cyan")
f1.pack()

    
UserName1=""
Password1=""

def login():
    win3=Tk()
    win3.title("LOG IN")
    win3.config(bg="pink")
    f4=Frame(win3,bg="pink")
    f4.pack()
    win3.geometry("1500x1500")
    label11=Label(f4,text="LOG IN",width=50,font=("bold",40),bg="black",fg="white")
    label11.pack(padx=40,pady=10)
    
    label12=Label(f4,text="UserName",width=10,font=40)
    label12.pack(padx=40,pady=10)
    e6=Entry(f4,bg="cyan",font=40)
    e6.pack(padx=40,pady=10)
    

    label13=Label(f4,text="Password",width=20,font=40)
    label13.pack(padx=40,pady=10)
    e7=Entry(f4,bg="cyan",font=40)
    e7.pack(padx=40,pady=10)
    
    def conti():
        global UserName1
        UserName1=e6.get()
        x=open("sona.txt","w")
        x.write(UserName1)
        x.close()
        global Password1
        Password1=e7.get()
        tasks()
        #os.system("atm_tasks.py")
    button4=Button(f4,text="CONTINUE",width=20,font=("bold",20),bg="cyan",command=conti)
    button4.pack(padx=40,pady=(100,0))

label1=Label(f1,text="WELCOME",width=50,font=("bold",60),bg="blue",fg="cyan")
label1.pack(side=TOP,padx=(0,0),pady=(250,0))
button1=Button(f1,text="LOG IN",bg="brown",fg="white",width=10,font=("bold",15),command=login)
button1.pack(side=LEFT,padx=(400,400),pady=100)
def sign():
        
    signup()
    #os.system("atm_signup.py")

button2=Button(f1,text="SIGN UP",bg="brown",fg="white",width=10,font=("bold",15),command=sign)
button2.pack(side=LEFT,padx=(0,0),pady=100)








root.mainloop()
