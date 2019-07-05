from tkinter import *
import pymysql
noc=""
cn=""
m1=0
y1=0
UserName=""
Password=""
MobNo=""
def signup():
    win=Tk()
    win.title("SIGN UP")
    win.config(bg="pink")
    f2=Frame(win,bg="pink")
    f2.pack()
    win.geometry("1500x1500")
    label2=Label(f2,text="SIGN UP",width=50,font=("bold",40),bg="black",fg="white")
    label2.pack(padx=40,pady=10)
    
    label4=Label(f2,text="UserName",width=10,font=40)
    label4.pack(padx=40,pady=10)
    e1=Entry(f2,bg="cyan",font=40)
    e1.pack(padx=40,pady=10)
    

    label5=Label(f2,text="Password",width=20,font=40)
    label5.pack(padx=40,pady=10)
    e2=Entry(f2,bg="cyan",font=40)
    e2.pack(padx=40,pady=10)
    

    label6=Label(f2,text="MobNo",width=10,font=40)
    label6.pack(padx=40,pady=10)
    e3=Entry(f2,bg="cyan",font=40)
    e3.pack(padx=40,pady=10)
    
        
    #db=pymysql.connect(user="root",
                          #password="",
                          #host="localhost",
                       #database="bank")
    #mycursor=db.cursor()
    #mycursor.execute("insert into atm(username,password,mobno)VALUES(%s,%s,%s)",(UserName,Password,MobNo))
    #db.commit()
    

    #button=Button(f1,text="SIGN UP",bg="brown",fg="white",width=10,font=("bold",15),command=signup)
    

    def details():
        global UserName
        UserName=e1.get()
        global Password
        Password=e2.get()
        global MobNo
        MobNo =e3.get()

    
        #os.system("")
        win1=Tk()
        win1.title("Card Details")
        win1.config(bg="pink")
        f3=Frame(win1,bg="pink")
        f3.pack()
        win1.geometry("1500x1500")
        label10=Label(f3,text="BANK DETAILS",width=50,font=("bold",40),bg="black",fg="white")
        label10.pack(padx=40,pady=10)
    
        
        #def sel():
            #selection= str(var.get())
            #label15.config(text=selection)
        #label15=Label(f3,text="Choose Type of Card",width=16,font=40)
        #label15.pack(padx=40,pady=10)
        
        #var=IntVar()
        #R1= Radiobutton(f3,text="Debit Card",variable=var,value=1,command=sel)
        #R1.pack(padx=(40,0),pady=10)

        #R2= Radiobutton(f3,text="Credit Card",variable=var,value=2,command=sel)
        #R2.pack(padx=(40,0),pady=10)

        #R3= Radiobutton(f3,text="Master Card",variable=var,value=3,command=sel)
        #R3.pack(padx=(40,0),pady=10)

        label8=Label(f3,text="Name on card",width=20,font=40)
        label8.pack(padx=40,pady=10)
        e4=Entry(f3,bg="cyan",font=40)
        e4.pack(padx=40,pady=10)
        

        label9=Label(f3,text="Enter Card Number",width=16,font=40)
        label9.pack(padx=40,pady=10)
        e5=Entry(f3,bg="cyan",font=40)
        e5.pack(padx=40,pady=10)
        
        
        label14=Label(f3,text="Enter Validity Dates",width=16,font=40)
        label14.pack(padx=40,pady=10)
        
        months=[1,2,3,4,5,6,7,8,9,10,11,12]
        year=[19,20,21,22,23,24,25,26,27,28,29]
        variable1 = StringVar(f3)
        variable2 = StringVar(f3)
        variable1.set(months[0])
        variable2.set(year[0])

        dd1= OptionMenu(f3,variable1,*months)
        dd1.pack(pady=20)
        dd2= OptionMenu(f3,variable2,*year)
        dd2.pack(pady=20)
        def ok():
            global noc
            noc=e4.get()
            global cn
            cn=e5.get()
            global m1
            global y1
            m1= variable1.get()
            y1=variable2.get()
            #mycursor.execute("insert into atm(m,y)VALUES(%d,%d)",(m1,y1))
            #db.commit()

        button5 = Button(f3, text="OK", command=ok)
        button5.pack()

        def insert():
            db=pymysql.connect(user="root",
                          password="",
                          host="localhost",
                       database="bank")
            mycursor=db.cursor()
            mycursor.execute("insert into atm(username,password,mobno,type,cardname,accno,m,y,balance,pin)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(UserName,Password,MobNo,"0",noc,cn,m1,y1,"120000","0"))
            db.commit()
    
            
        

        button6=Button(f3,text="Submit",width=25,font=("bold",20),bg="black",fg="white",command=insert)
        button6.pack(padx=40,pady=10)
    



        
    button3=Button(f2,text="Enter Card Details",width=25,font=("bold",20),bg="black",fg="white",command=details)
    button3.pack(padx=40,pady=10)
    
    


    
    

    

    win.mainloop
#signup()

