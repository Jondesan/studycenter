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
root.geometry('400x200')
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


mstrFrm = tk.Frame(width=400,
                   height=200,
                   bg=rgb_color((25,31,38)))

loadingCanvas = tk.Canvas(master=mstrFrm)
loadingCanvas.configure(bg = rgb_color((25,31,38)),
                        highlightthickness = 0)

mstrFrm.pack(fill=tk.BOTH, expand=True)


loadingCanvas.create_image(loadingCanvas.winfo_width()/2,
                           loadingCanvas.winfo_height()/2,
                           image = photo,
                           anchor='nw')

loadingCanvas.place(in_=mstrFrm)

root.after_idle(next_frame)
root.mainloop()