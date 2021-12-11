#Author: Tien mai
#project: Tien's ATM
#class: SDEV-140
#professor: Louis Vician



#impot libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root=tk.Tk()


#CREATED TO REQUIRE THE USER TO ENTER THEIR USER NAME AND PASSWORD THAT WILL CHECK THE USER AUTHENTICITY
class Login:
    def __init__(self,master):
        #SETTING UP WINDOW
        self.master=master
        master.title("Tien's ATM")
        master.state('zoomed')
        master.resizable(False, False)
        master.bg=PhotoImage(file="loginbg.png")
        master.background=Label(master, image=master.bg)
        master.background.place(x=0,y=0)
        
        #SET VARIABLES
        self.username = StringVar()
        self.password = StringVar()
        self.count=0
        self.countTrans=0

        # HEADINGS
        self.head = Label(master, text=" WELCOME TO THE TIEN'S ATM ", justify='center', font='Courier 25', relief="flat")
        self.head.place(relx=0.5, rely=0.1,anchor=CENTER)
        self.head1 = Label(master, text="Login", justify='center', font='Courier 25')
        self.head1.place(relx=0.5, rely=0.2,anchor=CENTER)
        
        #LOGIN SECTION
        self.usernameLabel = Label(master, text="UserName", justify='center', font='Courier 15')
        self.usernameLabel.place(relx=0.3, rely=0.3, anchor=CENTER)
        self.username = Entry(master)
        self.username.place(relx=0.5, rely=0.3, width=300, height=40, anchor=CENTER)

        self.PassLabel = Label(master, text="PassWord", justify='center', font='Courier 15')
        self.PassLabel.place(relx=0.3, rely=0.4,anchor=CENTER)
        self.password = Entry(master,show='*')
        self.password.place(relx=0.5, rely=0.4, width=300, height=40, anchor=CENTER)

        self.loginbutton= Button(master, text="Login", justify='center', command=self.verified, width=40, height=5,)
        self.loginbutton.place(relx=0.5, rely=0.55, anchor=CENTER)

        self.exitbutton= Button(master, text="Exit", justify='center', width=40, height=5, command=lambda : Exit())
        self.exitbutton.place(relx=0.5, rely=0.7,anchor=CENTER)

        self.note=Label(master, text="*Note: If more than 3 unsuccessful login attempts,\n the program will send a notification to you and the program will end!",justify='center', font='Courier 20')
        self.note.place(relx=0.5, rely=0.85,anchor=CENTER)


    #USER AUTHENTICATION
    def verified(self):
        username=self.username.get()
        password=self.password.get()
        self.count+=1  
        countTrans=self.countTrans      
        account=open("Accounts.txt","r")
        for i in account:
            a,b,c,d=i.split(", ")
            if (a==username and b==password):
                check=True 
                break                                           
            if (username=="" or password==""):
                check=False
                message="Username and password cannot be blank!"                
            elif (a!=username or b!=password):
                check=False
                message="Username or password is incorrect!"             
        if check==False:
            if self.count<3:
                messagebox.showwarning("Error",message)
                #clear boxes
                self.username.delete(0,'end')
                self.password.delete(0,'end')
            else:
                messagebox.showinfo("Notification","You have failed to login 3 times, the program ends!")
                Exit()
        else:
            root.withdraw()
            ATMmenu(self.master,username,countTrans)
        
            
            
#CLAS ATMMENU USED TO CREATE ATM FUNCTION MENU WINDOW
class ATMmenu:
    def __init__(self, master, username,countTrans):
        #SETTING UP WINDOW
        self.master=master
        master=Toplevel(root)
        master.title("Tien's ATM/Menu")
        master.state('zoomed')
        master.resizable(False, False)
        master.bg=PhotoImage(file="background.png")
        master.background=Label(master, image=master.bg)
        master.background.place(x=0,y=0)
        master.deiconify()
        
        #GET AND SET VARIABLES
        self.username=username
        user=self.username
        self.countTrans=countTrans
        self.name=StringVar()
        
        #GET USER'S NAME
        account=open("Accounts.txt","r")
        for i in account:
            a,b,c,d=i.split(", ")
            if (a==user):
                self.name=c

        # LABELS AND ACTION BUTTONS
        self.head = Label(master, text="Welcome to Tien's ATM Mr/Mrs {}".format(self.name), justify='center', font='Courier 25', relief="flat")
        self.head.place(relx=0.5, rely=0.07,anchor=CENTER)
        self.head = Label(master, text=" Menu ", justify='center', font='Courier 25', relief="flat")
        self.head.place(relx=0.5, rely=0.15,anchor=CENTER)
        self.checkbalancebutton= Button(master, text="Check balance", justify='center', width=40, height=5, command=lambda: balanceClicked())
        self.checkbalancebutton.place(relx=0.5, rely=0.3,anchor=CENTER)
        self.Depositbutton= Button(master, text="Deposit", justify='center', width=40, height=5, command=lambda: depositClicked())
        self.Depositbutton.place(relx=0.5, rely=0.45,anchor=CENTER)
        self.withdrawbutton= Button(master, text="Withdraw", justify='center', width=40, height=5, command=lambda:  withdrawClicked())
        self.withdrawbutton.place(relx=0.5, rely=0.6,anchor=CENTER)
        self.exit= Button(master, text="Exit", justify='center', width=40, height=5, command=lambda : Exit())
        self.exit.place(relx=0.5, rely=0.75,anchor=CENTER)
        self.note=Label(master, text="*Note: you can make up to 3 transactions at a time.\n After 3 transactions, the program will send a notification to you and the program will end",justify='center', font='Courier 15')
        self.note.place(relx=0.5, rely=0.9,anchor=CENTER)
        
        def balanceClicked():
            master.withdraw()
            Balance(self.master,user,self.countTrans)
        def depositClicked():
            master.withdraw()
            Deposit(self.master,user,self.countTrans)
        def withdrawClicked():
            master.withdraw()
            Withdraw(self.master,user, self.countTrans)

#CLASS BALANCE WAS CREATED TO ALLOW USERS TO CHECK THEIR ACCOUNT BALANCE
class Balance:
    def __init__(self, master, user, countTrans):
        #SETTING UP WINDOW
        self.master=master
        master=Toplevel(root)
        master.title("Tien's ATM/Menu/Balance")
        master.state('zoomed')
        master.resizable(False, False)
        master.bg=PhotoImage(file="bg.png")
        master.background=Label(master, image=master.bg)
        master.background.place(x=0,y=0)
        master.deiconify()

        #GET AND SET VARIABLES
        self.user=user
        username=self.user
        self.countTrans=countTrans

        #CHECK AND SHOW USER'S DATA IN TXT FILE
        account=open("Accounts.txt","r")
        for i in account:
            a,b,c,d=i.split(", ")
            d=d.strip()
            if (a==username):
                self.printBalance = Label(master, text="Your account balance is: {}".format(d), justify='center', font='Courier 25')
                self.printBalance.place(relx=0.5, rely=0.4,anchor=CENTER)
        self.backbutton= Button(master, text="Go back", justify='center', width=40, height=5, command=lambda: backbuttonClicked())
        self.backbutton.place(relx=0.5, rely=0.5,anchor=CENTER)
        account.close()
        def backbuttonClicked():
            master.withdraw()
            ATMmenu(self.master,username,self.countTrans)

#CLASS DEPOSIT WAS CREATED TO ALLOW USERS TO DEPOSIT MONEY TO THEIR BANK ACCOUNT
class Deposit:
    def __init__(self, master, user,countTrans):
        #SETTING UP WINDOW
        self.master=master
        master=Toplevel(root)
        master.title("Tien's ATM/Menu/Deposit")
        master.state('zoomed')
        master.resizable(False, False)
        master.bg=PhotoImage(file="bg.png")
        master.background=Label(master, image=master.bg)
        master.background.place(x=0,y=0)
        master.deiconify()

        #GET AND SET VARIABLES
        self.user=user
        username=self.user
        self.countTrans=countTrans

        #LABEL, ENTRY, BUTTONS
        self.label = Label(master, text="Enter the amount you want to deposit into your account:", justify='center', font='Courier 25')
        self.label.place(relx=0.5, rely=0.3,anchor=CENTER)
        self.textlabel= Entry(master)
        self.textlabel.place(relx=0.5, rely=0.4, width=300, height=40, anchor=CENTER)
        self.checkbutton=Button(master, text="Enter", justify="center", width=40, height=5, command=lambda :checkbutton(self))
        self.checkbutton.place(relx=0.5, rely=0.55,anchor=CENTER) 
        self.backbutton= Button(master, text="Go back", justify='center', width=40, height=5, command=lambda : backbuttonClicked(self))
        self.backbutton.place(relx=0.5, rely=0.70,anchor=CENTER)

        #GO BACK TO ATM MENU
        def backbuttonClicked(self):
            master.withdraw()
            ATMmenu(self.master,username,self.countTrans)

        #CHECK THE AMOUNT ENTERED BY THE USER
        def checkbutton(self):
            count=-1
            
            number=self.textlabel.get()
            checknumber=number.isdigit()
            accountdata=open("Accounts.txt","r")
            data=accountdata.readlines()
            if (checknumber==True):
                accountR=open("Accounts.txt","r")   
                number=int(number)  
                for i in accountR:
                    count+=1
                    a,b,c,d=i.split(", ")
                    d=int(d)
                    if (a==username):
                        #CHECK THE USER ENTERING AMOUNT MATCHES THE CONDITIONS
                        if (number<=0 or number>2000):
                            depositmessage="You can deposit up to $2000 and no less than $0 per transaction!"
                            messagebox.showwarning("Error",depositmessage)
                            self.textlabel.delete(0,'end')
                        else:
                            #UPDATE NEW DATA TO FILE TXT
                            self.countTrans+=1
                            number=int(d)+number
                            data[count]="{}, {}, {}, {}\n".format(a,b,c,str(number)) 
                            newdata="".join(data)                           
                            accountW=open("Accounts.txt","w")
                            accountW.write(newdata)
                            messagebox.showinfo("Congratulation!","Successful transaction! Your current balance is: {}".format(number))
                            master.withdraw()
                            if self.countTrans==3:
                                messagebox.showinfo("Notification","You have made 3 transactions, the program ends!")
                                Exit()
                            else:
                                ATMmenu(self.master,username,self.countTrans)      
                        break
            elif number=="":
                messagebox.showwarning("Error","The amount cannot be blank!")
            elif checknumber==False:
                messagebox.showwarning("Error","You have to input a number, not a string")
                self.textlabel.delete(0,'end')
            
#CLASS WITHDRAW WAS CREATED TO ALLOW USERS TO WITHDRAW MONEY FROM THEIR BANK ACCOUNT                    
class Withdraw:
    def __init__(self, master, user,countTrans):
        #SETTING UP WINDOW
        self.master=master
        master=Toplevel(root)
        master.title("Tien's ATM/Menu/Withdraw")
        master.state('zoomed')
        master.resizable(False, False)
        master.bg=PhotoImage(file="bg.png")
        master.background=Label(master, image=master.bg)
        master.background.place(x=0,y=0)
        master.deiconify()

        #GET AND SET VARIABLES
        self.user=user
        username=self.user
        self.countTrans=countTrans

        #LABEL, ENTRY, BUTTONS
        self.label = Label(master, text="Enter the amount you want to withdraw from your account: ", justify='center', font='Courier 25')
        self.label.place(relx=0.5, rely=0.3,anchor=CENTER)
        self.textlabel= Entry(master)
        self.textlabel.place(relx=0.5, rely=0.4, width=300, height=40, anchor=CENTER)
        self.checkbutton=Button(master, text="Enter", justify="center", width=40, height=5, command=lambda :checkbutton(self))
        self.checkbutton.place(relx=0.5, rely=0.55,anchor=CENTER) 
        self.backbutton= Button(master, text="Go back", justify='center', width=40, height=5, command=lambda : backbuttonClicked(self))
        self.backbutton.place(relx=0.5, rely=0.70,anchor=CENTER)

        #GO BACK TO ATM MENU
        def backbuttonClicked(self):
            master.withdraw()
            ATMmenu(self.master,username,self.countTrans)

        #CHECK THE AMOUNT ENTERED BY THE USER
        def checkbutton(self):
            count=-1
            number=self.textlabel.get()
            checknumber=number.isdigit()
            accountdata=open("Accounts.txt","r")
            data=accountdata.readlines()
            if (checknumber==True):
                accountR=open("Accounts.txt","r")   
                number=int(number)  
                for i in accountR:
                    count+=1
                    a,b,c,d=i.split(", ")
                    d=int(d)
                    if (a==username):
                        #CHECK THE USER ENTERING AMOUNT MATCHES THE CONDITIONS
                        if (number<=0 or number>2000):
                            depositmessage="You can withdraw up to $2000 and no less than $0 per transaction!"
                            messagebox.showwarning("Error",depositmessage)
                            self.textlabel.delete(0,'end')
                        elif number>d:
                            depositmessage="The amount you want to withdraw cannot be more than your current balance!"
                            messagebox.showwarning("Error",depositmessage)
                            self.textlabel.delete(0,'end')
                        else:
                            #UPDATE NEW DATA TO FILE TXT
                            self.countTrans+=1
                            number=d-number
                            data[count]="{}, {}, {}, {}\n".format(a,b,c,str(number)) 
                            newdata="".join(data)                           
                            accountW=open("Accounts.txt","w")
                            accountW.write(newdata)
                            messagebox.showinfo("Congratulation!","Successful transaction! Your current balance is: {}".format(number))
                            master.withdraw()
                            if self.countTrans==3:
                                messagebox.showinfo("Notification","you have made 3 transactions, the program ends!")
                                Exit()
                            else:
                                ATMmenu(self.master,username,self.countTrans)        
                        break
            elif number=="":
                messagebox.showwarning("Error","The amount cannot be blank!")
            elif checknumber==False:
                messagebox.showwarning("Error","you have to input a number, not a string")
                self.textlabel.delete(0,'end')



#THIS FUNCTION USED TO END PROGRAM
def Exit():
    root.destroy()


Login(root)
mainloop()

