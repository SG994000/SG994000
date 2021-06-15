from sklearn import linear_model
import pandas as pd
from sklearn.metrics import mean_squared_error

w=open("housing.csv","r")
df=pd.read_csv(w)
x=df[["Avg. Area Income","Avg. Area House Age","Avg. Area Number of Rooms","Area Population"]]

housing_x_train=x[:50]

y=df["Price"]

housing_y_train=y[:50]


modal=linear_model.LinearRegression()
modal.fit(housing_x_train,housing_y_train)



# print("mean_suared error is : ",mean_squared_error(housing_y_test,housing_y_test_predict_value))

print("weight : " ,modal.coef_)
print("intercept :" ,modal.intercept_)



import tkinter as tk
from tkinter import *
from tkinter import messagebox as mg
app=tk.Tk()
app.wm_iconbitmap("1.ico")
app.title("Housing Price Pridiction")
app.config(bg="light blue")
app.geometry("500x400+220+200")

tk.Label(app,text="HOUSING PRIDICTOR",fg="BLUE",font="15").place(x=140,y=12)


tk.Label(app,text="Avg. Area Income : ",fg="green",font="15").place(x=20,y=60)
tk.Label(app,text="Avg. Area House Age : ",fg="green",font="15").place(x=20,y=100)
tk.Label(app,text="Avg. Area Number of Rooms : ",fg="green",font="15").place(x=20,y=140)
tk.Label(app,text="Area Population : ",fg="green",font="15").place(x=20,y=180)

area_income=Variable()
Avg_Area_House_Age=Variable()
Avg_Area_Number_of_Rooms=Variable()
Area_Population=Variable()

area_income.set("")
Avg_Area_House_Age.set("")
Avg_Area_Number_of_Rooms.set("")
Area_Population.set("")

q=Entry(app,width=30,fg="RED",textvariable=area_income)
q.place(x=240,y=65)
q.focus()
tk.Entry(app,width=30,fg="RED",textvariable=Avg_Area_House_Age).place(x=240,y=105)
tk.Entry(app,width=30,fg="RED",textvariable=Avg_Area_Number_of_Rooms).place(x=240,y=145)
tk.Entry(app,width=30,fg="RED",textvariable=Area_Population).place(x=240,y=185)

statusbar=StringVar()
statusbar.set("Ready")
s=Label(app,textvariable=statusbar,font=9,relief=SUNKEN,anchor="w")
s.pack(side=BOTTOM,fill=X)
def get_value():


    x=area_income.get()
    y=Avg_Area_House_Age.get()
    z=Avg_Area_Number_of_Rooms.get()
    v=Area_Population.get()


    if (area_income.get() == ""):
        if (Avg_Area_House_Age.get() == ""):
            if (Avg_Area_Number_of_Rooms.get() == ""):
                if (Area_Population.get() == ""):
                            mg.showinfo("info", "Error")



    elif (area_income.get() == ""):
                b.option_clear()
                mg.showinfo("ERROR", "please enter AREA INCOME")
    elif (Avg_Area_House_Age.get() == ""):
             b.option_clear()
             mg.showinfo("ERROR", "please enter Avg_Area_House_Age")
    elif (Avg_Area_Number_of_Rooms.get() == ""):
            b.option_clear()
            mg.showinfo("ERROR", "please enter Avg_Area_Number_of_Rooms")
    elif (Area_Population.get() == ""):
            b.option_clear()
            mg.showinfo("ERROR", "please enter Area_Population")


    else:
        try:
            float(x)

        except Exception as e:
            mg.showinfo("ERROR", "Enter Only Integer Value In Area_Income")

        try:
            float(y)
        except Exception as e:
            mg.showinfo("ERROR", "Enter Only Integer Value In Avg_Area_House_Age")

        try:
            float(z)
        except Exception as e:
            mg.showinfo("ERROR", "Enter Only Integer Value Avg_Area_Number_of_Rooms")

        try:
            float(v)
        except Exception as e:
            mg.showinfo("ERROR", "Enter Only Integer Value Area_Population")

        finally:

            df2 = pd.DataFrame({'Avg. Area Income': [x], 'Avg. Area House Age': [y],
                                " Avg. Area Number of Rooms": [z], 'Area Population': [v]})
            value = modal.predict(df2)
            area_income.set("")
            Avg_Area_House_Age.set("")
            Avg_Area_Number_of_Rooms.set("")
            Area_Population.set("")

            statusbar.set("loading....")
            s.update()
            import time
            time.sleep(2)
            statusbar.set("Ready")
            s.update()


            price = IntVar()
            price.set(value[0])
            tk.Label(app, text="Your House Price Can Be : ", fg="dark blue",relief=SUNKEN, font=20).place(x=50, y=320)
            tk.Label(app, textvariable=price, fg="green", font=20,relief=SUNKEN).place(x=250, y=320)


b=Button(app,text="Get Predict",fg="dark blue",command=get_value)
b.place(x=190,y=230)

app.mainloop()