#imported libraries

import numpy as np
import matplotlib.pyplot as plt

from tkinter import *

import pandas as pd
import datetime as dt


# class to return values
class value:
    
    DAY=None
    MONTH=None
    YEAR=None
   
    def GET(self):
        self.DAY=str(d.get())
        self.MONTH=str(m.get())
        self.YEAR=y.get()
        main.destroy()
    
    def GIVE(self):
        return self.DAY,self.MONTH,self.YEAR

# object of value class
v=value()

#graphical interface to display input box
main = Tk(None,None,'project',1)

# Heading
label=Label(main,text="   VACCINATION RATIO",font=('Times New Roman',15,'bold'))
label.pack(side=TOP)

# frame to input values
control=Frame(main,width=300,height=300)
control.pack(side=LEFT,anchor=NW)

# subheading
label=Label(control,text="DATE")
label.grid(row=3,column=6,padx=20,pady=20)

# input box to take day
d=Entry(control,width=20)
d.grid(row=6,column=3,padx=20,pady=20)
d.insert(0,"dd")

# input box to take month
m=Entry(control,width=20)
m.grid(row=6,column=6,padx=20,pady=20)
m.insert(0,"mm")

# input box to take year
y=Entry(control,width=20)
y.grid(row=6,column=9,padx=20,pady=20)
y.insert(0,"yyyy")

# submit button
submit=Button(control,text='SUBMIT',width=25,command=v.GET)
submit.grid(row=9,column=6,padx=20,pady=20)

main.mainloop()

# function returning user input date
day,mon,year=v.GIVE()
day=int(day)
mon=int(mon)
year=int(year)

#count of vaccinated people
vacc=0

DATE=dt.date(year,mon,day)

DATA=pd.read_csv("Data.csv")

# checking no. of vaccinated people
for date in DATA['Appointment_Date']:
    new_date=dt.date(int(date[0:4]),int(date[5:7]),int(date[8:10]))
    if(DATE>=new_date):
        vacc=vacc+1

# part for displaying piechart
status = ['Vaccinated','Non vaccinated']
 
data = [vacc,500-vacc]
 
explode = (0.1, 0.0)
 
colors = ( "green", "red")
 
wp = { 'linewidth' : 1, 'edgecolor' : "black" }
 
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d})".format(pct, absolute)
 
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data,
                                  autopct = lambda pct: func(pct, data),
                                  explode = explode,
                                  labels = status,
                                  shadow = True,
                                  colors = colors,
                                  startangle = 90,
                                  wedgeprops = wp,
                                  textprops = dict(color ="black"))
 
ax.legend(wedges, status,
          title ="Status",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
 
plt.setp(autotexts, size = 12, weight ="bold")
ax.set_title("VACCINATION RATIO")
 
plt.show()
