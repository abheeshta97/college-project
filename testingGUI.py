import fib_encrypt_1 as F
import decrypt_1 as D
import FinalSteganography as Steg
import creationANDopening as note
from tkinter import messagebox, ttk
from tkinter import *
def tab(main):
    rows=0
    while rows<50:
        main.rowconfigure(rows,weight=1)
        main.columnconfigure(rows,weight=1)
        rows+=1

    nb=ttk.Notebook(main)
    entry=Entry(nb)
    nb.grid(row=1,column=0,columnspan=50,rowspan=5,sticky='NESW')

try:
    def crfile():
        global root
        note.createFile()
    def opfile():
        global root
        note.openTextFile(root)
    def encr():
        global root
        messagebox.showinfo("Information", "ENTER IN THE NAME FOR FILE TO ENCRYPT ")
        F.encrypted(note.selectFile(root))
        messagebox.showinfo("Information","ENCRYPTION SUCCESSFUL")
    def decr():
        global root
        messagebox.showinfo("Information", "SELECT FILE TO BE DECRYPTED")
        try:
            D.decrypted(note.selectFile(root))
            messagebox.showinfo("Information", "DECRYPTION SUCCESSFUL")
        except:
            messagebox.showerror("ERROR", "CONFIRM SELECTION/ENTRY")
    def enc():
        global root
        try:
            messagebox.showinfo("Information", "SELECT THE FILE TO INSERT")
            Steg.encode(note.selectFile(root),root)
        except:
            messagebox.showerror("ERROR", "CONFIRM SELECTION/ENTRY")
    def dec():
        global root
        try:
            messagebox.showinfo("Information", "SELECT THE ENCODED IMAGE")
            data=Steg.decode(note.selectImageFile(root))
            messagebox.showinfo("Information", "ENTER IN THE FILE NAME TO HOLD THE DECODED DATA")
            note.save_as(data)
            messagebox.showinfo("Information", "EXTRACTION MECHANISM COMPLETED")
        except:
            messagebox.showerror("ERROR", "CONFIRM SELECTION/ENTRY")
except:
    messagebox.showerror("ERROR", "CONFIRM SELECTION/ENTRY")
root=Tk()
root.title('CRYPT-STEG PROJ')
menu=Menu(root)
root.config(menu=menu)
root.minsize(width=300, height=200)
root.geometry('400x250+535+230')
tab(root)

subMenu=Menu(menu)
menu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='Create New File',command=crfile)
subMenu.add_command(label='Open File',command=opfile)

runMenu=Menu(menu)
menu.add_cascade(label='Run',menu=runMenu)
runMenu.add_command(label='Encrypt',command=encr)
runMenu.add_command(label="Decrypt",command=decr)
runMenu.add_separator()
steg=Menu(runMenu)

runMenu.add_cascade(label='Steganography',menu=steg)
steg.add_command(label='Insert Text in Image',command=enc)
runMenu.add_separator()
steg.add_command(label='Extract Text from Image',command=dec)



root.mainloop()