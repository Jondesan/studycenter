#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:27:50 2021

@author: joonahuh
"""
# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk
#import loading.py as tkloading



class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        
        mainCont = tk.Frame(width=800,
                            height=400)
        
                
        header = tk.Frame(mainCont,
                          bg='black')
        
        footer = tk.Frame(mainCont,
                          bg='black')
    
        
        #XXX: HEADER BUTTONS
        fileBtn = tk.Button(header,
                            text='File',
                            fg='white',
                            bg='black',
                            height=1)

        editBtn = tk.Button(header,
                            text='Edit',
                            fg='white',
                            bg='black',
                            height=1)
        
        appsBtn = tk.Button(header,
                            text='Apps',
                            fg='white',
                            bg='black',
                            height=1)
        
        exitBtn = tk.Button(header,
                            text='Exit',
                            fg='white',
                            bg='black',
                            height=1,
                            command=root.quit)


        #XXX: SIDE PANEL AND BODY        
        sidePane = tk.Frame(mainCont,
                            bg = 'MediumPurple1',
                            width = 100,
                            height = 400)

        body = tk.Frame(mainCont,
                        bg='black',
                        width=400,
                        height=400)
        
        
        fileBtn.pack(side=tk.LEFT)
        editBtn.pack(side=tk.LEFT)
        appsBtn.pack(side=tk.LEFT)
        exitBtn.pack(side=tk.LEFT)
        
        header.pack(side=tk.TOP)
        sidePane.pack(side=tk.LEFT)
        body.pack(side=tk.RIGHT,
                  fill=tk.BOTH,
                  expand=True)
        
        mainCont.pack(expand=True,
                      fill=tk.BOTH)
        
        root.title('Study Center')
        
        
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top",
                               fill="both",
                               expand=True)
    root.mainloop()
        
