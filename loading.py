# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 02:36:22 2021

@author: jonde
"""

import tkinter as tk

def rgb_color(rgb):
    return '#%02x%02x%02x' % rgb

root = tk.Tk()
root.title('Study Center Experimental build')
photo = tk.PhotoImage(file="img/loading_low.gif")
gif_index = 0

def next_frame():
    global gif_index
    try:
        #XXX: Move to the next frame
        photo.configure(format="gif -index {}".format(gif_index))
        gif_index += 1
    except tk.TclError:
        gif_index = 0
        return next_frame()
    else:
        root.after(10, next_frame) # XXX: Fixed animation speed



loadingCanvas = tk.Canvas(root, width=400, height=200)
loadingCanvas.configure(bg = rgb_color((25,31,38)),
                        highlightthickness = 0)

loadingCanvas.pack(expand = 1,
                   fill = tk.BOTH)

loadingCanvas.create_image(0,
                           0,
                           image = photo,
                           anchor='nw')


root.after_idle(next_frame)
root.mainloop()