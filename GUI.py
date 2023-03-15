#!/usr/bin/python
import sys
import os
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

window=tkinter.Tk()
window.title("Smart Maze Solver")
window.geometry('600x400')

my_label = Label(window,
                 text = "Smart Maze Solver",font=("Arial", 24),borderwidth=3, relief="solid",bg="lightgreen")
my_label.place(x=180,y=5)
my_label = Label(window,
                 text = "Algorithms",font=("Arial", 16),borderwidth=3, relief="solid",bg="pink")
my_label.place(x=250,y=60)

# Create a photoimage object of the image in the path
image1 = Image.open("download.jpg")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=200, y=100)


def runbfs():
    os.system('python New_bfs.py')

B=tkinter.Button(window,text="BFS_GUI",command=runbfs,bg="lightblue")
B.place(x=160, y=310)

def rundfs():
    os.system('python New_dfs.py')

d=tkinter.Button(window,text="DFS_GUI",command=rundfs,bg="lightblue")
d.place(x=280, y=310)

def runastar():
    os.system('python New_astar.py')

astar=tkinter.Button(window,text="Astar_GUI",command=runastar,bg="lightblue")
astar.place(x=400, y=310)

infobfs=tkinter.Button(window,text="INFO BFS",bg="orange")
infobfs.place(x=160, y=350)

infobfs=tkinter.Button(window,text="INFO DFS",bg="orange")
infobfs.place(x=280, y=350)

infobfs=tkinter.Button(window,text="INFO A-STAR",bg="orange")
infobfs.place(x=400, y=350)

# About window
def show_about():
    messagebox.showinfo("showinfo", "Information\n\n"+"This is a GUI interface to solve a maze\n\n"+"It is a team work done by chanchal kumari,   chandrahas thakur AND   aditi bansal\n\n")
about_button=tkinter.Button(window,text="SHOW_ABOUT",command=show_about,bg="lightblue")
about_button.place(x=500, y=10)
window.mainloop()