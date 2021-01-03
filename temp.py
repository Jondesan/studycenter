# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 00:56:49 2021

@author: jonde
"""

import tkinter as tk
from PIL import ImageTk,Image
import random as rnd
import time


loading_icon_path = 'loading.gif'

frames = 80

def load_gif(path):
    loading_icon = []
    numberOfFrames = 80
    for i in range(numberOfFrames):
        print(str(i+1))
        loading_icon.append(ImageTk.PhotoImage(file=path, format='gif -index %i' %i))
    return loading_icon




gui = tk.Tk()
gui.title('Graphics')

wndHeight  = 500
wndWidth   = 500

canvas = tk.Canvas(gui, width = wndWidth, height = wndHeight)



ball = canvas.create_oval(wndWidth/2,wndHeight/2,100,100,fill='red')
xspeed = 1
yspeed = 0


while True:
    
    canvas.move(ball,xspeed,yspeed)
    gui.update()
    time.sleep(0.1)


#gui.mainloop()

