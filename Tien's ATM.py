#Author: Tien mai
#project: Tien's ATM
#class: SDEV-140
#professor: Louis Viction



#impot libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root=tk.Tk()
class Login:
    def __init__(self,master):
        #setting up window
        self.master=master
        master.title("Tien's ATM")
        master.state('zoomed')
        master.resizable(False, False)
        #variables
        self.username = StringVar()
        self.password = StringVar()
        self.count=0
        # HEADINGS
        self.head = Label(master, text=" WELCOME TO THE TIEN'S ATM ", justify='center', font='Courier 15')
        self.head.grid(row=0, column=1, pady=6)
        self.head1 = Label(master, text="Login", justify='center', font='Courier 15')
        self.head1.grid(row=1, column=1, pady=6)
        #login section
        self.usernameLabel = Label(master, text="User Name", justify='center', font='Courier 10')
        self.usernameLabel.grid(row=2, column=0, pady=6,padx=10)
        self.username = Entry(master)
        self.username.grid(row=2, column=1, padx=2)

        self.PassLabel = Label(master, text="Pass Word", justify='center', font='Courier 10')
        self.PassLabel.grid(row=3, column=0, pady=6)
        self.password = Entry(master,show='*')
        self.password.grid(row=3, column=1, padx=2)

        self.loginbutton= Button(master, text="Login", justify='center', command=self.verified)
        self.loginbutton.grid(row=4, column=1, padx=2)

        self.note=Label(master, text="*Note: If more than 3 unsuccessful login attempts, the program will issue a message and automatically end!",justify='center', font='Courier 10')
        self.note.grid(row=5, column=1,padx=2)


    #user authentication
    def verified(self):
        username=self.username.get()
        password=self.password.get()
        self.count+=1        
        account=open("Accounts.txt","r")
        for i in account:
            a,b,c,d=i.split(", ")
            if (a==username and b==password):
                check=True 
                break                                           
            if (username=="" or password==""):
                check=False
                message="username and password cannot be blank!"                
            elif (a!=username or b!=password):
                check=False
                message="username or password is incorrect!"             
        if check==False:
            if self.count<3:
                messagebox.showwarning("Error",message)
                #clear boxes
                self.username.delete(0,'end')
                self.password.delete(0,'end')
            else:
                messagebox.showwarning("Error","You have failed to login 3 times, the program will end automatically!")
                Exit()
        else:
            root.withdraw()
            ATMmenu(self.master,username)
        
            
            

class ATMmenu:
    def __init__(self, master, username):
        #setting up window
        self.master=master
        master=Toplevel(root)
        master.title("Tien's ATM/Menu")
        master.state('zoomed')
        master.resizable(False, False)
        master.deiconify()
        #variables
        self.username=username
        user=self.username

        # ACTION BUTTONS
        self.checkbalancebutton= Button(master, text="Check balance", justify='center', command=lambda: balanceClicked())
        self.checkbalancebutton.grid(row=1, column=1, padx=2)
        self.Depositbutton= Button(master, text="Deposit", justify='center', command=lambda: depositClicked())
        self.Depositbutton.grid(row=2, column=1, padx=2)
        self.withdrawbutton= Button(master, text="Withdraw", justify='center', command=lambda:  withdrawClicked())
        self.withdrawbutton.grid(row=3, column=1, padx=2)
        self.exitbutton= Button(master, text="Exit", justify='center', command=lambda : Exit())
        self.exitbutton.grid(row=4, column=1, padx=2)
        self.note=Label(master, text="*Note: you can make up to 3 transactions at a time.\n After 3 transactions, the program will send a notification to you and the program will end",justify='center', font='Courier 10')
        self.note.grid(row=5, column=1,padx=2)
        
        def balanceClicked():
            master.withdraw()
            Balance(self.master,user)
        def depositClicked():
            master.withdraw()
            Deposit(self.master,user)
        def withdrawClicked():
            master.withdraw()
            Withdraw(self.master,user)

class Balance:
    def __init__(self, master, user):
        #setting up window
        self.master=master
        master=Toplevel(root)
        master.title("Tien's ATM/Menu/Balance")
        master.state('zoomed')
        master.resizable(False, False)
        master.deiconify()
        #get variables
        self.user=user
        username=self.user
        #check and show user's data in txt file
        account=open("Accounts.txt","r")
        for i in account:
            a,b,c,d=i.split(", ")
            d=d.strip()
            if (a==username):
                self.printBalance = Label(master, text="Your account balance is: {}".format(d), justify='center', font='Courier 10')
                self.printBalance.grid(row=2, column=0, pady=6,padx=10)
        self.backbutton= Button(master, text="Go back", justify='center', command=lambda: backbuttonClicked())
        self.backbutton.grid(row=4, column=1, padx=2)
        account.close()
        def backbuttonClicked():
            master.withdraw()
            ATMmenu(self.master,username)

class Deposit:
    def __init__(self, master, user):
        #setting up window
        self.master=master
        master=Toplevel(root)
        master.title("Tien's ATM/Menu/Deposit")
        master.state('zoomed')
        master.resizable(False, False)
        master.deiconify()
        #get variable
        self.user=user
        username=self.user
        
        #LABEL, ENTRY, BUTTONS
        self.label = Label(master, text="Enter the amount you want to deposit", justify='center', font='Courier 10')
        self.label.grid(row=2, column=0, pady=6,padx=10)
        self.textlabel= Entry(master)
        self.textlabel.grid(row=2, column=1, padx=2)
        self.checkbutton=Button(master, text="Enter", justify="center", command=lambda :checkbutton())
        self.checkbutton.grid(row=4, column=1, padx=2)        
        self.backbutton= Button(master, text="Go back", justify='center', command=lambda : backbuttonClicked())
        self.backbutton.grid(row=5, column=1, padx=2)

        def backbuttonClicked():
            master.withdraw()
            ATMmenu(self.master,username)

        #CHECK THE AMOUNT ENTERED BY THE USER
        def checkbutton():
            count=-1
            number=self.textlabel.get()
            checknumber=number.isdigit()
            accountdata=open("Accounts.txt","r")
            data=accountdata.readlines()
            if (number!="" and checknumber==True):
                accountR=open("Accounts.txt","r")   
                number=int(number)  
                for i in accountR:
                    count+=1
                    a,b,c,d=i.split(", ")
                    d=int(d)
                    if (a==username):
                        #CHECK THE USER ENTERING AMOUNT MATCHES THE CONDITIONS
                        if (number<=0 or number>2000):
                            depositmessage="you can deposit up to $2000 and no less than $0  at a time!"
                            messagebox.showinfo("Error",depositmessage)
                            #clear box
                            self.textlabel.delete(0,'end')
                        else:
                            #UPDATE NEW DATA TO FILE TXT
                            number=int(d)+number
                            data[count]="{}, {}, {}, {}\n".format(a,b,c,str(number)) 
                            newdata="".join(data)                           
                            accountW=open("Accounts.txt","w")
                            accountW.write(newdata)
                            messagebox.showinfo("Congratulation!","successful transaction, your balance is: {}".format(number))
                            master.withdraw()
                            ATMmenu(self.master,username)      
                        break
            else:
                print("cannot be blank!")
                    
class Withdraw:
    def __init__(self, master, user):
        #SETTING UP WINDOW
        self.master=master
        master=Toplevel(root)
        master.title("Tien's ATM/Menu/Withdraw")
        master.state('zoomed')
        master.resizable(False, False)
        master.deiconify()

        #get variable
        self.user=user
        username=self.user
        
        #LABEL, ENTRY, BUTTONS
        self.label = Label(master, text="Enter the amount you want to withdraw", justify='center', font='Courier 10')
        self.label.grid(row=2, column=0, pady=6,padx=10)
        self.textlabel= Entry(master)
        self.textlabel.grid(row=2, column=1, padx=2)
        self.checkbutton=Button(master, text="Enter", justify="center", command=lambda : checkbutton())
        self.checkbutton.grid(row=4, column=1, padx=2)        
        self.backbutton= Button(master, text="Go back", justify='center', command=lambda : backbuttonClicked())
        self.backbutton.grid(row=5, column=1, padx=2)

        def backbuttonClicked():
            master.withdraw()
            ATMmenu(self.master,username)

        #CHECK THE AMOUNT ENTERED BY THE USER
        def checkbutton():
            count=-1
            number=self.textlabel.get()
            checknumber=number.isdigit()
            accountdata=open("Accounts.txt","r")
            data=accountdata.readlines()
            if (number!="" and checknumber==True):
                accountR=open("Accounts.txt","r")   
                number=int(number)  
                for i in accountR:
                    count+=1
                    a,b,c,d=i.split(", ")
                    d=int(d)
                    if (a==username):
                        #CHECK THE USER ENTERING AMOUNT MATCHES THE CONDITIONS
                        if (number<=0 or number>2000 or number>d):
                            depositmessage="you can deposit up to $2000 and no less than $0  at a time!"
                            messagebox.showinfo("Error",depositmessage)
                            #clear box
                            self.textlabel.delete(0,'end')
                        else:
                            #UPDATE NEW DATA TO FILE TXT
                            number=d-number
                            data[count]="{}, {}, {}, {}\n".format(a,b,c,str(number)) 
                            newdata="".join(data)                           
                            accountW=open("Accounts.txt","w")
                            accountW.write(newdata)
                            messagebox.showinfo("Congratulation!","successful transaction, your balance is: {}".format(number))
                            master.withdraw()
                            ATMmenu(self.master,username)      
                        break
            else:
                print("cannot be blank!")        
        



#THIS FUNCTION USED TO OFF PROGRAM
def Exit():
    root.destroy()

Login(root)
mainloop()

