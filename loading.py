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
root.geometry('800x400')
photo = tk.PhotoImage(file="img/loading_low.gif")
gif_index = 0




def get_width(tkobject):
    return tkobject.winfo_width()

def get_height(tkobject):
    return tkobject.winfo_height()

def resize(tkobject, sizeobject):
    tkobject.configure(width = get_width(sizeobject),
                       height = get_height(sizeobject))
    return 1

def next_frame():
    global gif_index
    try:
        #XXX: Move to the next frame
        photo.configure(format="gif -index {}".format(gif_index))
        
        #XXX: Print size parameters for debugging purposes
        #print('(' + str(get_width(loadingCanvas)) + ', ' + str(get_height(loadingCanvas)) + ')')
        
        
        #XXX:   For some fucktard of a reason moveto isn't a real implementation and doesn't work as it should
        #XXX:   Somehow it doesn't understand the fact that the image anchor SHOULD be in the middle, and it thinks
        #XXX:   it resides in the upper left corner.
        #XXX:   TRY to fix this at some point and move to another place, doesn't really belong here,
        #XXX:   but it will suffice for now.
        loadingCanvas.moveto(loadingIcon, get_width(loadingCanvas)/2-81, get_height(loadingCanvas)/2-81)
        
        
        resize(loadingCanvas, root)
        resize(mstrFrm, root)
        
        
        gif_index += 1
    except tk.TclError:
        gif_index = 0
        return next_frame()
    else:
        root.after(10, next_frame) # XXX: Fixed animation speed



mstrFrm = tk.Frame(width=800,
                   height=400,
                   bg=rgb_color((25,31,38)))




loadingCanvas = tk.Canvas(master=mstrFrm,
                          width=get_width(root),
                          height=get_height(root),
                          bg = rgb_color((25,31,38)),
                          highlightthickness = 0)



mstrFrm.pack(fill=tk.BOTH, expand=True)


loadingCanvas.pack(fill=tk.BOTH, expand=1)
loadingCanvas.update_idletasks()


loadingIcon = loadingCanvas.create_image(get_width(loadingCanvas)/2,
                                         get_height(loadingCanvas)/2,
                                         image = photo,
                                         anchor='n')




root.update_idletasks()
root.after_idle(next_frame)

root.mainloop()







