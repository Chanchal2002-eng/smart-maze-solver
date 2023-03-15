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

def infobfs():
    messagebox.showinfo("showinfo", "Information\n\nBreadth-first search (BFS) is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level. Extra memory, usually a queue, is needed to keep track of the child nodes that were encountered but not yet explored.")
infobfs=tkinter.Button(window,text="INFO BFS",command=infobfs,bg="orange")
infobfs.place(x=160, y=350)


def infodfs():
    messagebox.showinfo("showinfo", "Information\n\nDepth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.")
    
infodfs=tkinter.Button(window,text="INFO DFS",command=infodfs,bg="orange")
infodfs.place(x=280, y=350)

def infoastar():
    messagebox.showinfo("showinfo", "Information\n\n A* (pronounced A-star) A-star is a graph traversal and path search algorithm, which is often used in many fields of computer science due to its completeness, optimality, and optimal efficiency. One major practical drawback is its  {\displaystyle O(b^{d})}O(b^d) space complexity, as it stores all generated nodes in memory. Thus, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance,as well as memory-bounded approaches; however, A* is still the best solution in many cases.")

infoastar=tkinter.Button(window,text="INFO A-STAR",command=infoastar,bg="orange")
infoastar.place(x=400, y=350)

# About window
def show_about():
    messagebox.showinfo("showinfo", "Information\n\n"+"This is a GUI interface to solve a maze\n\n"+"It is a team work done by chanchal kumari,   chandrahas thakur AND   aditi bansal\n\n")
about_button=tkinter.Button(window,text="SHOW_ABOUT",command=show_about,bg="lightblue")
about_button.place(x=500, y=10)
window.mainloop()