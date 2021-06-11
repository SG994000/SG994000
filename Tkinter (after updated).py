import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mg
import pandas as pd
from csv import *
import os
import numpy as np
import json
app=tk.Tk()
# app.configure(bg='green')
app.geometry("400x500")
app.maxsize(400,500)
app.minsize(400,500)
app.title("Information")

f_name=tk.StringVar(app)
Email=tk.Variable(app)
Class=tk.Variable(app)
Pass=tk.Variable(app)
age=tk.StringVar(app)
mobile=tk.StringVar(app)

age.set("")
mobile.set("")


l=Label(app,text="INFORMATION",font="16",fg="blue").place(x=130,y=8)


tk.Label(app,text="Name :",font="16").place(x=10,y=50)
tk.Label(app,text="Email :",font="16").place(x=10,y=80)
tk.Label(app,text="Class :",font="16").place(x=10,y=110)
tk.Label(app,text="Password :",font="16").place(x=10,y=140)              #
tk.Label(app,text="age :",font="16").place(x=10,y=170)
tk.Label(app,text="mobile :",font="16").place(x=10,y=200)

# tk.Entry(app,textvariable=f_name ,bg="white").place(x=90,y=50)

t= Entry(app,textvariable=f_name ,bg="white",width=22)
t.grid(padx=95,pady=50)
t.focus()
tk.Entry(app,textvariable=Email ,bg="white",width=22).place(x=95,y=80)
tk.Entry(app,textvariable=Class ,bg="white",width=22).place(x=95,y=110)
tk.Entry(app,textvariable=Pass ,bg="white",width=22).place(x=95,y=140)
tk.Entry(app,textvariable=age ,bg="white",width=22).place(x=95,y=170)
tk.Entry(app,textvariable=mobile ,bg="white",width=22).place(x=95,y=200)


#TODO radio button
stu=IntVar()
tk.Radiobutton(app,text="Student",variable=stu,value=1,fg="blue").place(x=60,y=240)
tk.Radiobutton(app,text="Bussiness",variable=stu,value=2,fg="blue").place(x=140,y=240)


# todo check button
check=IntVar()
tk.Checkbutton(app,text="Are you sure to submit",fg="red",variable=check).place(x=60,y=270)

#todo commbobox button
Gen=StringVar()
Gender=ttk.Combobox(app,width=12,text="Gender",values=["Gender","Male","Female","Other"],textvariable=Gen,state="readonly")
Gender.place(x=230,y=240)
Gender.current(0)


def show():

        check.get()
        stu.get()
        Gen.get()
        f_name.get()
        if (f_name.get()==""):
            if(Email.get()==""):
                if(Class.get()==""):
                    if(Pass.get()==""):
                        if(age.get()==""):
                            if(mobile.get()==""):
                                mg.showinfo("info","Error")



        elif (f_name.get()==""):
            b.option_clear()
            mg.showinfo("ERROR","please enter Name")
        elif(Email.get()==""):
            b.option_clear()
            mg.showinfo("ERROR","please enter Email")
        elif(Class.get()==""):
            b.option_clear()
            mg.showinfo("ERROR","please enter Class")
        elif(Pass.get()==""):
            b.option_clear()
            mg.showinfo("ERROR","please enter Password")
        elif(age.get()=="" ):
            b.option_clear()
            mg.showinfo("ERROR", "please enter Age")
        elif(mobile.get()==""):
            b.option_clear()
            mg.showinfo("ERROR","please enter Mobile number")
        elif (Gen.get() == "Gender"):
            b.option_clear()
            mg.showinfo("ERROR","please enter Gender")
        elif ((stu.get() == 0)):
            b.option_clear()
            mg.showinfo("ERROR","please enter option")
        elif (check.get() == 0):
            b.option_clear()
            mg.showinfo("ERROR","please fill check box")
        elif (int(age.get())>100 or int(age.get())<5):
            mg.showerror("Error", "please enter valid age 5 to 100")
        elif  (len(str(mobile.get())) > 10 or len(str(mobile.get())) < 10):
              mg.showerror("Error", "Nuber Error ")

        else:
            if (check.get() == 0):
                        submited = "Not Submited"
                        print(submited)
        #
            else:
                submited = "Yes Sumbmited"
                print(submited)


            if(stu.get()==0):
                categry="Bussiness"

            else:
                categry="student"

            print("Your Categry :",categry)

            if(Gen.get()=="Male"):
                print("Your Gender :",Gen.get())

            elif(Gen.get()=="Female") :
                print("Your Gender :",Gen.get())

            else:
             print("Your Gender :",Gen.get())
            dicti = {"name": f"{f_name.get()}", "EMAIL": f"{Email.get()}", "Class": f"{Class.get()}",
                    "Pass": f"{Pass.get()}", "Age": f"{int(age.get())}", "Mobile": f"{int(mobile.get())}"}
            # print("your detail is : ", dicti, "Please check out")

            with open("INFORMATION.csv","a",newline="") as f:

                dict_writer=DictWriter(f,fieldnames=["Name","Email","Class","Pass","Age","Mobile"])
                if os.stat("INFORMATION.csv").st_size==0:
                    dict_writer.writeheader()


                # for mail in g:
                #     s = mail.split('@')[1]
                #     c.append(s)
                dict_writer.writerow({
                        "Name": f_name.get(),
                        "Email": Email.get(),
                        "Class": Class.get(),
                        "Pass": Pass.get(),
                        "Age": age.get(),
                        "Mobile": mobile.get()})




            j = mg.askquestion("OHH", "DO YOU WANT TO SUBMITED")
            if (j == "yes"):
                mg.showinfo("information", "information sucssesfully submited")
                f_name.set("")
                Email.set("")
                Class.set("")
                Pass.set("")
                age.set("")
                mobile.set("")


                app2 = tk.Tk()
                app2.geometry("400x400")
                app2.maxsize(400, 400)
                app2.minsize(400, 400)

                df = pd.read_csv("INFORMATION.csv")
                g = df["Age"]
                z = df["Name"]
                a=df["Email"]

                tk.Label(app2, text="YOUR DETAILS : ").place(x=20, y=5)

                tk.Label(app2, text="Name : ").place(x=20, y=30)
                tk.Label(app2, text=dicti["name"]).place(x=80, y=30)

                tk.Label(app2, text="Email : ").place(x=20, y=50)
                tk.Label(app2, text=dicti["EMAIL"]).place(x=80, y=50)

                tk.Label(app2, text="Class : ").place(x=20, y=70)
                tk.Label(app2, text=dicti["Class"]).place(x=80, y=70)

                tk.Label(app2, text="Pass : ").place(x=20, y=90)
                tk.Label(app2, text=dicti["Pass"]).place(x=80, y=90)

                tk.Label(app2, text="Age : ").place(x=20, y=110)
                tk.Label(app2, text=dicti["Age"]).place(x=80, y=110)

                tk.Label(app2, text="Mobile : ").place(x=20, y=130)
                tk.Label(app2, text=dicti["Mobile"]).place(x=80, y=130)

                tk.Label(app2, text="Total users : ").place(x=20, y=175)
                tk.Label(app2, text=np.shape(z)).place(x=90, y=175)

                tk.Label(app2, text="Avrage Age : ").place(x=20, y=195)
                tk.Label(app2, text=np.mean(g)).place(x=95, y=195)

                tk.Label(app2, text="Total Mails : ").place(x=20, y=215)
                tk.Label(app2, text=np.shape(a)).place(x=100, y=215)


                bi=[]
                ki=[]
                i=np.array(a)
                for item in i:
                    e=item.split(" ")
                    p=",".join(e)
                    bi.append(p)

                for items in bi:
                    f = items.split('@')[1]
                    ki.append(f)

                y=len(ki)
                other_mail=y-(ki.count("google.com"))-(ki.count("yahoo.com"))-(ki.count("gmail.com"))

                tk.Label(app2, text="Google.com : ").place(x=20, y=235)
                tk.Label(app2, text=ki.count("google.com")).place(x=110, y=235)

                tk.Label(app2, text="yahoo.com : ").place(x=20, y=255)
                tk.Label(app2, text=ki.count("yahoo.com")).place(x=100, y=255)

                tk.Label(app2, text="Gmail.com : ").place(x=20, y=275)
                tk.Label(app2, text=ki.count("gmail.com")).place(x=100, y=275)

                tk.Label(app2, text="Other_mail : ").place(x=20, y=295)
                tk.Label(app2, text=other_mail).place(x=100, y=295)

                app2.mainloop()



            else:
                mg.showinfo("information", "you exit")

                f_name.set("")
                Email.set("")
                Class.set("")
                Pass.set("")
                age.set("")
                mobile.set("")


def Exit():
        exit()

b=Button(app,text="SUBMIT",fg="green",command=show,height=2,width=5)
b.place(x=150,y=300)
tk.Button(app,text="exit",fg="black",height=2,width=5,command=Exit).place(x=150,y=350)
app.mainloop()





