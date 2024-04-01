import os
import shutil
from tkinter import *
import tkinter.messagebox as tmsg
import tkinter as tk
root = Tk()

root.title('File organizer')
path=StringVar()
textbox1=Entry(root,textvariable=path)
textbox1.grid(row=0,column=1)

def submit():
    path=textbox1.get()
    list=os.listdir(path)


    for file in list:
       name,ext=os.path.splitext(file)
       ext=ext[1:]
    
       if os.path.exists(path+'/'+ext):
           shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
       else:
          os.makedirs(path+'/'+ext)
          shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
       '''if radio.get()=='alphabetical':
           file.sort()
           print('files moved alphabetically')
       else:
           print('Numeric')'''
    print('Your files are successfully moved')
    exit()
    
    
        
    

label0=Label(root,text='Enter the path= ',fg='blue',font=('Arial',14))
label0.grid(row=0,column=0,padx=5,pady=10)




             

label1=Label(root,text="which way you wanna organize your files?",font="lucida 11 bold")
label1.grid(row=1,column=1,padx=0,pady=0)


var=StringVar()
var.set("radio")

radio=Radiobutton(root,text="Alphabetical",padx=14,variable=var,value='alphabetical',anchor="w")
radio.grid(row=2,column=1)

radio=Radiobutton(root,text="Numeric",padx=14,variable=var,value='Numeric',anchor="w")
radio.grid(row=3,column=1)


button=Button(root,command=submit,text='Submit')
button.grid(row=4,column=1,padx=15,pady=30,sticky=W)


root.mainloop()
submit()




















           
