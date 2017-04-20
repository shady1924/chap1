from tkinter import *

def processOk():
   # button2.text("button checked")
    button2["text"]="asdasdasd"

root = Tk()
label =  Label(root, text="welcome to python")
button=Button(root,text="click me", command=processOk)
button2=Button(root,text="click me2")
label.pack()
button.pack()
button2.pack()
root.mainloop()