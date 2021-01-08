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

#root.geometry('400x200')



#def update():
    



mstrFrm = tk.Frame(width=root.winfo_width(),
                   height=root.winfo_height(),
                   bg=rgb_color((25,31,38)))

loadingCanvas = tk.Canvas(master=mstrFrm,
                          width=root.winfo_screenwidth(),
                          height=root.winfo_screenheight())

loadingCanvas.configure(bg = rgb_color((25,31,38)),
                        highlightthickness = 0)

mstrFrm.pack(fill=tk.BOTH, expand=True)


loadingCanvas.update_idletasks()

print(str(root.winfo_width()))
print(str(root.winfo_height()))

loadingCanvas.create_image(root.winfo_screenwidth()/2,
                           root.winfo_screenheight()/2,
                           image = photo)

loadingCanvas.pack()

root.update()
root.mainloop()
