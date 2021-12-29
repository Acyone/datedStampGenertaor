# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 14:56:14 2021

@author: Achille
"""

from PIL import Image as img
from PIL import ImageTk
import random
import os

from tkinter import * 
from tkinter import ttk

from datetime import date

from tkcalendar import Calendar, DateEntry
#try:
#    import tkinter as tk
#    from tkinter import ttk
#except ImportError:
#    import Tkinter as tk
#    import ttk

version = 1
maxAngle = 10

        
#def generator(currentDate, maxAngle):
    
    
    
    
class stamp:
    def __init__(self, date=date.today(), maxAngle=10, stampImg=img.new("RGBA", (472,472))):
        self.date = date
        self.maxAngle = maxAngle
#    def generateImg(self, currentDate, maxAngle):
        print("Generating Img...")
        print_sel()
        ############################
        #generate random numbers
        variations = [14,2,2,2,self.maxAngle]
        
        randomVariations = [0,0,0,0,0]
        #for the circle
        randomVariations[0] = random.randint(1,variations[0])
        print(randomVariations[0])
        #for the day
        randomVariations[1] = random.randint(1,variations[1])
        print(randomVariations[1])
        #for the month
        randomVariations[2] = random.randint(1,variations[2])
        print(randomVariations[2])
        #for the year
        randomVariations[3] = random.randint(1,variations[3])
        print(randomVariations[3])
        #for the angle
        randomVariations[4] = random.randint(-variations[4],variations[4])
        print(randomVariations[4])
        
        circle = img.open(os.path.join("data/circles/" + str(randomVariations[0]) + ".png"), "r")
        day = img.open(os.path.join("data/days/" + str(self.date.day) + "/" + str(randomVariations[1]) + ".png"), "r")
        month = img.open(os.path.join("data/months/" + str(self.date.month) + "/" + str(randomVariations[2]) + ".png"), "r")
        year = img.open(os.path.join("data/years/" + str(self.date.year) + "/" + str(randomVariations[3]) + ".png"), "r")
        
        
        #build the image
        tempImg = img.composite( circle, day, circle)
        tempImg = img.composite( tempImg, month, tempImg)
        tempImg = img.composite( tempImg, year, tempImg)
    
        #rotate randomly
        
        tempImg = tempImg.rotate(randomVariations[4], resample=img.BICUBIC)
        
        self.stampImg = tempImg

        
def print_sel():
    currentDate = cal.get_date()#date is now the current date being processed, as a datetime object
    print(currentDate)
    
def showStamp(stamp):
    stampImg.show()
    
def createSingle():
    #
    print("creating single stamp")
    #create stamp object with the correct date
    a = stamp(date.today(),maxAngle)
    #save said object's image as a png
    a.stampImg.show()
    return a
    
titleText = "Générateur de tampons v ", str(version)
print(titleText)



root = Tk()
root.title(titleText)

###### CREATE THE TABS

tabControl = ttk.Notebook(root)

home = ttk.Frame(tabControl)
single = ttk.Frame(tabControl)
multiple = ttk.Frame(tabControl)
options = ttk.Frame(tabControl)

tabControl.add(home, text='Home')
tabControl.add(single, text='Single stamp')
tabControl.add(multiple, text='Multiple stamps')
tabControl.add(options, text='Options')

tabControl.pack()

##############
# HOME
##############


ttk.Label(home, text="Preview").grid(column=3, row=0)
homeButton = ttk.Button(root, text="Home", state=DISABLED)



##############
# SINGLE STAMP
##############
dummyImg = img.new("RGBA", (472,472), "blue")
dummyImgTk = ImageTk.PhotoImage(dummyImg)


# currentDate = date.today()
# print(currentDate)

#col 0


ttk.Label(single, text='Choose date').grid(column=0, row=0)
cal = DateEntry(single, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/MM/yyyy')
cal.grid(column=0, row=1)
#ttk.Button(single, text="ok", command=print_sel).grid(column=0, row=2)

#col 1
ttk.Label(single, text="preview").grid(column=1, row=0)
singleImgPreviewLabel = ttk.Label(single, image=ImageTk.PhotoImage(a.stampImg))
singleImgPreviewLabel.image = dummyImgTk
singleImgPreviewLabel .grid(column=1, row=1)
refreshbutton = ttk.Button(single, text="Refresh preview", command=createSingle).grid(column=1, row=2)
#viewbutton = ttk.Button(single, text="Refresh preview", command=showStamp(currentStamp) ).grid(column=1, row=3)

##############
# MULTIPLE STAMPS
##############


#ttk.Label(multiple, text='image').grid(column=0, row=0)


##############
# OPTIONS
##############

#ttk.Label(options, text="max angle").grid(column=0, row=0)
#ttk.Label(options, text="max angle image demo").grid(column=0, row=1)




root.mainloop() 


