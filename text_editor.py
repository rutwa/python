import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
filename = None
si=10
c='black'
fon='Times New Roman'
def createNewFile():
    global filename
    filename= "Untitled"
    textarea.delete(0.0,END)
   
   
def saveFile():
    global file
    t = textarea.get(0.0,END)
    f= open(file,'w')
    f.write(t)
    f.seek(0)
    f.close()
 
def saveFileAs():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(textarea.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.seek(0)
    f.close()
 
def openNewFile():
    global file
    file= askopenfilename(title='Select a file')
    f=open(file)
    txt=f.read()
    textarea.delete('1.0',END)
    textarea.insert('0.0',txt)
    f.seek(0)
    f.close()
   

root =Tk()
root.title("Python Editor")
root.minsize(width=400,height=400)
 
 
 
textarea =Text(root,width=400,height=400)
 
textarea.pack()
font=Menubutton(root, text="Font")
 
 
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New File",command=createNewFile)
filemenu.add_command(label="Open File",command=openNewFile)
filemenu.add_command(label="Save File",command=saveFile)
filemenu.add_command(label="Save File As",command=saveFileAs)
filemenu.add_separator()
filemenu.add_command(label="Quit",command="")
menubar.add_cascade(label='File',menu=filemenu)
fontmenu = Menu(menubar)

menubar.add_cascade(label='Font',menu=fontmenu)
 
root.config(menu=menubar)
root.mainloop()
