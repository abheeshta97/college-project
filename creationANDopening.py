import subprocess as sp
import os
from tkinter import filedialog, messagebox

def selectFile(root):
    try:
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        return root.filename
    except:
        pass



def selectImageFile(root):
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("PNG files", "*.png"), ("all files", "*.*")))
    return root.filename

def openTextFile(root):
    os.startfile(selectFile(root))

def openImageFile():
    os.startfile(selectImageFile())

def createFile():
    try:
        programName = "notepad.exe"
        sp.Popen([programName])
    except:
        messagebox.showerror("Error", "Notepad Not Installed.\nPlease create file using your system Text Editor")

def save_as(data):
    try:
        file = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(("Text file", ".txt"), ("All files", "*.*")))
    except:
        pass
    if file !=None:
        file.write(data)
        file.close()

def save_asIMG(data):
    try:
        file = filedialog.asksaveasfilename(parent=None, title='Save As', filetypes=(("png file", ".png"), ("All files", "*")))
    except:
        pass
    if file !=None:
        data.save(file, str(file.split(".")[1].upper()))


#filetypes=(("Pictures", "*.png|*.PNG|*.jpg|*.JPG'), ("All files", "*"))