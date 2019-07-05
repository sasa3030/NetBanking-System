from tkinter import *
import pymysql
db=pymysql.connect(user="root",
                          password="",
                          host="localhost",
                       database="bank")
            
def tasks():
    wid_amt=""
    root1=Tk()
    root1.title("Tasks")
    root1.config(bg="grey")
    root1.geometry("1500x1500")
    f5=Frame(root1,bg="grey")
    f5.pack()
    def wid():
        
        root2=Tk()
        root2.title("Withdraw")
        root2.config(bg="grey")
        root2.geometry("1500x1500")
        f6=Frame(root2,bg="grey")
        f6.pack()
        label20= Label(f6,text="Enter Amount to Withdraw",width=40,font=("bold",40),bg="black",fg="white")
        label20.pack(side=TOP,padx=40,pady=10)
        e10=Entry(f6,bg="white",fg="black",font=40,width=30)
        e10.pack(padx=40,pady=10)
        label21= Label(f6,text="Enter PIN",width=40,font=("bold",40),bg="black",fg="white")
        label21.pack(side=TOP,padx=40,pady=10)
        e11=Entry(f6,bg="white",fg="black",font=40,width=30)
        e11.pack(padx=40,pady=10)
        def show1():
            new_amt=0
            x=open("sona.txt")
            temp=x.read()
            x.close()
            mycursor=db.cursor()
            wid_amt=e10.get()
            mycursor.execute("select balance from atm where username=%s",(temp))
            old_amt=mycursor.fetchall()
            print(old_amt)

##           if(int(old_amt)<=3000):
##            tkMessageBox.showinfo("CURRENT BALANCE LOW FOR WITHHDRAWL")
##            if(iold_amt>wid_amt):
##                new_amt=iold_amt-wid_amt
##                print(new_amt)
##                tkMessageBox("Amount Succesfully withdrawn \n Current Balance is: ",new_amt)
##            mycursor.execute("update atm set balance=%s,(new_amt) where username=%s",(temp))
##            
##            
##                
            
            
            
            
             
        button20=Button(f6,text="OK",bg="black",fg="white",width=30,font=("bold",30),command=show1)
        button20.pack(side=TOP,padx=(50,0),pady=(50,50))
        
        root2.mainloop()
        
        
    button5=Button(f5,text="WITHDRAWAL",bg="black",fg="white",width=30,font=("bold",30),command=wid)
    button5.pack(side=TOP,padx=(50,0),pady=(50,50))
    def dep():
        
        root2=Tk()
        root2.title("Deposit")
        root2.config(bg="grey")
        root2.geometry("1500x1500")
        f7=Frame(root2,bg="grey")
        f7.pack()
        
    button6=Button(f5,text="DEPOSIT",bg="black",fg="white",width=30,font=("bold",30),command=dep)
    button6.pack(side=TOP,padx=(50,0),pady=(50,50))
    def be():
        root2=Tk()
        root2.title("Enquiry")
        root2.config(bg="grey")
        root2.geometry("1500x1500")
        f8=Frame(root2,bg="grey")
        f8.pack()
        
    button7=Button(f5,text="BALANCE ENQUIRY",bg="black",fg="white",width=30,font=("bold",30),command=be)
    button7.pack(side=TOP,padx=(50,0),pady=(50,50))




    root1.mainloop()
#tasks()
