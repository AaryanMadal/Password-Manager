import tkinter as tk 
from tkinter import messagebox 
from tkinter import *
import os
import random
import sqlite3

LARGE_FONT= ("Verdana", 12)  

user=""  
class SeaofBTCapp(tk.Tk):  
  
    def __init__(self, *args, **kwargs):  
          
        tk.Tk.__init__(self, *args, **kwargs)  
        container = tk.Frame(self)  
  
        container.pack(fill="both", expand = True)  
        
  
        container.grid_rowconfigure(0,minsize=500, weight=1)  
        container.grid_columnconfigure(0,minsize=500, weight=1)  
  
        self.frames = {}  
  
        for F in (LoginPage,SignupPage,StartPage,PageOne):  
  
            frame = F(container, self)  
  
            self.frames[F] = frame  
  
            frame.grid(row=0, column=0, sticky="nsew")  
  
        self.show_frame(StartPage)  
  
    def show_frame(self, cont):  
  
        frame = self.frames[cont]  
        frame.tkraise()  
  

class StartPage(tk.Frame):  
  
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self,parent)   
        self.configure(bg="black")

        l1=tk.Label(self,text="Password Manager",font=("arial",20,"italic"))
        l1.config(bg="sandybrown")
        l1.place(relx=0.5,rely=0.1,anchor=tk.CENTER)
        #self.title("Login and Signup system")
        #adding the label "Register Here"

        label1 = tk.Label(self, text="Register Here!",bg="black",fg="white",font=("arial",10,"bold"))
        label1.place(relx=0.5,rely=0.25,anchor=tk.CENTER)
        #adding two buttons - login and signup
        button1 = Button(self,text="Login",width=20,command=lambda: controller.show_frame(LoginPage))
        button1.place(relx=0.3,rely=0.35,anchor=tk.CENTER)

        button2 = Button(self,text="Signup",width=20,command=lambda: controller.show_frame(SignupPage))
        button2.place(relx=0.7,rely=0.35,anchor=tk.CENTER)

class LoginPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="black")
        l1=tk.Label(self,text="LOGIN PAGE",font=("arial",20,"italic"))
        l1.config(bg="sandybrown")
        l1.place(relx=0.5,rely=0.1,anchor=tk.CENTER)

        def login_database():
            conn = sqlite3.connect("1.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM test WHERE email=? AND password=?",(e1.get(),e2.get()))
            row=cur.fetchall()
            conn.close()
            print(row)
            if row!=[]:
                user_name=row[0][1]
                global user
                user=user_name
                print(user," logged in")
                e1.delete(0,END)
                e2.delete(0,END)
                controller.show_frame(PageOne)
                #l3.config(text="user name found with name: "+user_name)
            else:
                l3.config(text="user not found")
            # e1.delete(1.0,"end")
            # e2.delete(1.0,"end")

        def gotoStart():
            global user
            user=""
            controller.show_frame(StartPage)
        #self.title("LogIn")  #set title to the window
        #login_window.geometry("400x250")  #set dimensions to the window
        #add 2 Labels to the window
        l1 = tk.Label(self,text="email: ",bg="black",fg="white")
        l1.place(relx=0.3,rely=0.3,anchor=W)

        l2 = tk.Label(self,text="Password: ",bg="black",fg="white")
        l2.place(relx=0.3,rely=0.4,anchor=W)

        l3 = tk.Label(self,bg="black",fg="white")
        l3.place(relx=0.3,rely=0.5,anchor=W)

        #creating 2 adjacent text entries
        email_text = StringVar() #stores string
        e1 = Entry(self,textvariable=email_text)
        e1.place(relx=0.6,rely=0.3,anchor=tk.CENTER)

        password_text = StringVar()
        e2 = Entry(self,textvariable=password_text,show='*')
        e2.place(relx=0.6,rely=0.4,anchor=tk.CENTER)

        #create 1 button to login
        b = Button(self,text="login",width=20,command=login_database)
        b.place(relx=0.5,rely=0.6,anchor=tk.CENTER)
        button1 = tk.Button(self, text="Back to Home",width=20,  
                            command=gotoStart )  
        button1.place(relx=0.5,rely=0.7,anchor=tk.CENTER) 

class SignupPage(tk.Frame):
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self,parent) 
        self.configure(bg="black")
        l1=tk.Label(self,text="SIGNUP PAGE",font=("arial",20,"italic"))
        l1.config(bg="sandybrown")
        l1.place(relx=0.5,rely=0.1,anchor=tk.CENTER)

        def signup_database():
            conn = sqlite3.connect("1.db") #create an object to call sqlite3 module & connect to a database 1.db
            #once you have a connection, you can create a cursor object and call its execute() method to perform SQL commands
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text,password text)")
            cur.execute("INSERT INTO test Values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
            
            #execute message after account successfully created
            l4 = Label(self,text="account created",bg="black",fg="white",font=("arial",5))
            l4.grid(row=6,column=2)
            
            conn.commit()  #save the changes 
            conn.close() #close the connection
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)

        def gotoStart():
            global user
            user=""
            controller.show_frame(StartPage)
        #self.title("Sign Up") #title for the window
        #create 3 Labels
        l1 = Label(self,text="User Name: ",bg="black",fg="white")
        l1.place(relx=0.3,rely=0.3,anchor=W)

        l2 = Label(self,text="User email: ",bg="black",fg="white")
        l2.place(relx=0.3,rely=0.4,anchor=W)

        l3 = Label(self,text="Password: ",bg="black",fg="white")
        l3.place(relx=0.3,rely=0.5,anchor=W)

        #create 3 adjacent text entries
        name_text = StringVar() #declaring string variable for storing name and password
        e1 = Entry(self,textvariable=name_text)
        e1.place(relx=0.6,rely=0.3,anchor=tk.CENTER)

        email_text = StringVar()
        e2 = Entry(self,textvariable=email_text)
        e2.place(relx=0.6,rely=0.4,anchor=tk.CENTER)

        password_text = StringVar()
        e3 = Entry(self,textvariable=password_text,show='*')
        e3.place(relx=0.6,rely=0.5,anchor=tk.CENTER)

        #create 1 button to signup
        b1 = Button(self,text="signup",width=20,command=signup_database)
        b1.place(relx=0.5,rely=0.6,anchor=tk.CENTER)

        button1 = tk.Button(self, text="Back to Home",width=20,  
                            command=gotoStart )  
        button1.place(relx=0.5,rely=0.7,anchor=tk.CENTER) 

    
class PageOne(tk.Frame):  
  
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent)  
        self.configure(bg="black")
      
        ############# encryption and decryption #################
        


        '''
        Euclid's algorithm for determining the greatest common divisor
        Use iteration to make it faster for larger integers
        '''


        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a


        '''
        Euclid's extended algorithm for finding the multiplicative inverse of two numbers
        '''


        def multiplicative_inverse(e, phi):
            d = 0
            x1 = 0
            x2 = 1
            y1 = 1
            temp_phi = phi

            while e > 0:
                temp1 = temp_phi//e
                temp2 = temp_phi - temp1 * e
                temp_phi = e
                e = temp2

                x = x2 - temp1 * x1
                y = d - temp1 * y1

                x2 = x1
                x1 = x
                d = y1
                y1 = y

            if temp_phi == 1:
                return d + phi


        '''
        Tests to see if a number is prime.
        '''


        def is_prime(num):
            if num == 2:
                return True
            if num < 2 or num % 2 == 0:
                return False
            for n in range(3, int(num**0.5)+2, 2):
                if num % n == 0:
                    return False
            return True


        def generate_key_pair(p, q):
            if not (is_prime(p) and is_prime(q)):
                raise ValueError('Both numbers must be prime.')
            elif p == q:
                raise ValueError('p and q cannot be equal')
            # n = pq
            n = p * q

            # Phi is the totient of n
            phi = (p-1) * (q-1)

            # Choose an integer e such that e and phi(n) are coprime
            e = random.randrange(1, phi)

            # Use Euclid's Algorithm to verify that e and phi(n) are coprime
            g = gcd(e, phi)
            while g != 1:
                e = random.randrange(1, phi)
                g = gcd(e, phi)

            # Use Extended Euclid's Algorithm to generate the private key
            d = multiplicative_inverse(e, phi)

            # Return public and private key_pair
            # Public key is (e, n) and private key is (d, n)
            return ((e, n), (d, n))


        def encrypt(pk, plaintext):
            # Unpack the key into it's components
            key, n = pk
            # Convert each letter in the plaintext to numbers based on the character using a^b mod m
            cipher = [pow(ord(char), key, n) for char in plaintext]
            # Return the array of bytes
            return cipher



        def decrypt(pk, ciphertext):
            # Unpack the key into its components
            key, n = pk
            # Generate the plaintext based on the ciphertext and key using a^b mod m
            aux = [str(pow(char, key, n)) for char in ciphertext]
            # Return the array of bytes as a string
            plain = [chr(int(char2)) for char2 in aux]
            return ''.join(plain)
        p = 131
        q= 149
        public, private = generate_key_pair(p, q)
        ############# functions ################
        def modify(s):
            words=s.split(", ")
            words[0]=words[0][1:]
            words[len(words)-1]=words[len(words)-1][:len(words[len(words)-1])-1]
            li=[]
            for word in words:
                li.append(int(word,10))
            
            print(li)
            return li

        def clear():
            inputtxt1.delete(1.0,'end')
            inputtxt2.delete(1.0,'end')
            inputtxt3.delete(1.0,'end')

        def savepass():
            global user
            web=inputtxt1.get(1.0,"end-1c")
            email=inputtxt2.get(1.0,"end-1c")
            pas=inputtxt3.get(1.0,"end-1c")
            enc=encrypt(public,pas)
            print(enc)

            file=open("passwords.txt",'r')
            lines=file.readlines()
            file.close()

            already=0
            c=0
            for line in lines:
                words=line.split(' : ')
                if(words[0]== user and words[1]==web and words[2]==email):
                    already=1
                    break  
                c=c+1

            if already==1:
                s=f"{user} : {web} : {email} : {enc}\n"
                lines[c]=s
                file1=open("passwords.txt","w")
                file1.writelines(lines)
                file1.close()
                print("Password is updated")
            else:
                file1=open("passwords.txt","a")
                file1.write(f"{user} : {web} : {email} : {enc}\n")
                file1.close()

            inputtxt1.delete(1.0,'end')
            inputtxt2.delete(1.0,'end')
            inputtxt3.delete(1.0,'end')

        def openpass():
            global user
            web=inputtxt1.get(1.0,"end-1c")
            email=inputtxt2.get(1.0,"end-1c")

            file=open("passwords.txt",'r')
            lines=file.readlines()
            file.close()

            already=0
            c=0
            for line in lines:
                words=line.split(' : ')
                if(words[0] == user and words[1]==web and words[2]==email):
                    already=1
                    break  
                c=c+1

            if already==1:
                inputtxt3.delete(1.0,'end')
                line=lines[c]
                words=line.split(' : ')
                pas=words[3].split('\n')
                print(pas)
                print(pas[0])
                li=modify(pas[0])
                dec=decrypt(private,li)
                inputtxt3.insert(1.0,dec)
            else:
                
                inputtxt3.delete(1.0,'end')
                inputtxt3.insert(1.0,"No record found")

        def backToHome():
            inputtxt1.delete(1.0,'end')
            inputtxt2.delete(1.0,'end')
            inputtxt3.delete(1.0,'end')
            controller.show_frame(StartPage)

        #################### Buttons #######################
        b_savepass=tk.Button(self,text='Save Password',width=15,command=savepass)
        b_savepass.place(relx=0.5,rely=0.6,anchor=tk.CENTER)


        b_openpass=tk.Button(self,text="Open Saved Password",width=15, command=openpass)
        b_openpass.place(relx=0.5,rely=0.7,anchor=tk.CENTER)


        b_clear=tk.Button(self,text="Clear All",width=10,command=clear )
        b_clear.place(relx=0.9,rely=0.4,anchor=tk.E)

        button1 = tk.Button(self, text="Back to Home",width=15,  
                            command=backToHome)  
        button1.place(relx=0.5,rely=0.8,anchor=tk.CENTER) 
        ################# Labels ##################

        l1=tk.Label(self,text="Password Manager",font=("arial",20,"italic"))
        l1.config(bg="sandybrown")
        l1.place(relx=0.5,rely=0.1,anchor=tk.CENTER)

        ################# LABELS AND INPUTS ################


        inputtxt1=tk.Text(self,height=1,width=20)
        inputtxt1.place(relx=0.7,rely=0.3,anchor=E)

        lbl1=tk.Label(self,text="website",bg="black",fg="white",font=("arial",10,"bold"))
        lbl1.place(relx=0.2,rely=0.3,anchor=W)

        ###############

        inputtxt2=tk.Text(self,height=1,width=20)
        inputtxt2.place(relx=0.7,rely=0.4,anchor=E)
        
        lbl2=tk.Label(self,text="Email",bg="black",fg="white",font=("arial",10,"bold"))
        lbl2.place(relx=0.2,rely=0.4,anchor=W)

        #################

        inputtxt3=tk.Text(self,height=1,width=20)
        inputtxt3.place(relx=0.7,rely=0.5,anchor=E)

        lbl3=tk.Label(self,text='Password',bg='black',fg="white",font=('arial',10,'bold'))
        lbl3.place(relx=0.2,rely=0.5,anchor=W)

app = SeaofBTCapp()  
app.mainloop()  